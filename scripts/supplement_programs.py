from common import *
from bs4 import BeautifulSoup
import re, subprocess, tempfile, unicodedata, bisect
from collections import Counter

papers=load_json('sources/resolved_universe.json.gz')
# Start the supplemental labels from the independently parsed structured schedules.
# This makes reruns idempotent and prevents approximate PDF matches accumulating.
base={p['id']:p for p in load_json('sources/enriched_universe.json.gz')}
for p in papers:
    for field in ['oral','oral_evidence','presentation_original']:
        p[field]=base[p['id']][field]
idx={(p['venue'],p['year'],norm(p['title'])):p for p in papers}
audit=[]
def mark(venue,year,title,url,label,detail):
    p=idx.get((venue,year,norm(title)))
    if not p:return False
    p['oral']=True
    if url not in p['oral_evidence']:p['oral_evidence'].append(url)
    if label not in p['presentation_original']:p['presentation_original'].append(label)
    audit.append({'id':p['id'],'source_url':url,'evidence':detail})
    return True

# Time-stamped individual presentations, excluding poster blocks without per-paper times.
f=RAW/'emnlp-2017-schedule.gz'
if f.exists():
    s=BeautifulSoup(gzip.decompress(f.read_bytes()),'lxml');url=json.loads((RAW/'emnlp-2017-schedule.meta.json').read_text())['url']
    n=0
    for row in s.find_all('tr'):
        cells=row.find_all('td',recursive=False)
        if len(cells)<2:continue
        time_label=cells[0].get_text(' ',strip=True)
        if not re.fullmatch(r'\d{1,2}:\d\d\s*[–—-]+\s*\d{1,2}:\d\d',time_label):continue
        for a in row.find_all('a'):
            n+=mark('EMNLP',2017,a.get_text(' ',strip=True),url,'Oral (individual timed main-paper presentation)',time_label)
    print('EMNLP2017 HTML',n,flush=True)

folder=ROOT/'sources/handbook_texts';folder.mkdir(exist_ok=True)
configs=[('EMNLP',2017,'emnlp-2017-fullhandbook'),('EMNLP',2021,'emnlp-2021-fullhandbook'),
         ('ACL',2022,'acl-2022-fullhandbook'),('EMNLP',2022,'emnlp-2022-fullhandbook'),
         ('EMNLP',2024,'emnlp-2024-fullhandbook-lfs')]
time_rx=re.compile(r'(?<!\d)([0-2]?\d):([0-5]\d)\s*[–—-]+\s*([0-2]?\d):([0-5]\d)')
for venue,year,key in configs:
    raw=RAW/(key+'.gz');out=folder/(key+'.txt')
    if not raw.exists():continue
    if not out.exists():
        data=gzip.decompress(raw.read_bytes())
        if not data.startswith(b'%PDF-'):continue
        with tempfile.NamedTemporaryFile(suffix='.pdf') as tmp:
            tmp.write(data);tmp.flush();subprocess.run(['pdftotext','-layout',tmp.name,str(out)],check=True)
    text=out.read_text();url=json.loads((RAW/(key+'.meta.json')).read_text())['url']
    entries=list(time_rx.finditer(text));starts=[m.start() for m in entries]
    rows=[p for p in papers if p['venue']==venue and p['year']==year];matched=set()
    chars=[];positions=[]
    for i,char in enumerate(text):
        for nc in unicodedata.normalize('NFKD',char).casefold():
            if nc in 'abcdefghijklmnopqrstuvwxyz0123456789':chars.append(nc);positions.append(i)
    normalized=''.join(chars)
    for p in rows:
        pn=norm(p['title']);offset=0
        if len(pn)<15:continue
        while True:
            at=normalized.find(pn,offset)
            if at<0:break
            begin=positions[at];end=positions[at+len(pn)-1]+1;offset=at+len(pn)
            j=bisect.bisect_left(starts,end);proof=None
            # Some handbooks put the time after title+authors, others before title.
            # Associate only the immediately adjacent slot, never the next paper's block.
            if j<len(entries):
                m=entries[j];between=text[end:m.start()]
                duration=int(m[3])*60+int(m[4])-int(m[1])*60-int(m[2])
                if 2<=duration<=30 and len(between)<750 and not re.search(r'\b(Session|Poster|Chair|Parallel|Program)\b',between,re.I):proof=m
            prev=bisect.bisect_right(starts,begin)-1
            if proof is None and prev>=0:
                m=entries[prev];between=text[m.end():begin]
                duration=int(m[3])*60+int(m[4])-int(m[1])*60-int(m[2])
                if 2<=duration<=30 and len(between)<180 and not re.search(r'\b(Session|Poster|Chair|Parallel|Program)\b',between,re.I):proof=m
            if proof:
                mark(venue,year,p['title'],url,'Oral (individual timed main-paper presentation)',text[max(0,min(begin,proof.start())-50):min(len(text),max(end,proof.end())+50)])
                matched.add(p['id']);break
    print('PDF timed oral',venue,year,len(matched),flush=True)

# The original ICLR 2020 virtual site has a separate official paper-data file.
f=RAW/'iclr-2020-papers-json.gz'
if f.exists():
    rows=json.loads(gzip.decompress(f.read_bytes()));print('ICLR2020 original metadata',type(rows).__name__,len(rows),flush=True)
    if isinstance(rows,list):
        for row in rows:
            c=row.get('content',{});title=c.get('title','')
            p=idx.get(('ICLR',2020,norm(title)))
            if not p:continue
            ident=row.get('forum') or row.get('id')
            if ident:
                p['pdf_url']='https://openreview.net/pdf?id='+ident;p['paper_url']='https://openreview.net/forum?id='+ident
            decision=str(c.get('presentation_type') or c.get('decision') or c.get('session') or '')
            if re.search(r'\boral\b',decision,re.I):mark('ICLR',2020,title,'https://iclr.cc/virtual_2020/papers.json',decision,decision)
save_json('checks/supplemental_oral_evidence.json',audit)

# Explicit talk classes in the preserved official ACL 2019 website.
f=RAW/'acl-2019-fullschedule-github.gz'
if f.exists():
    soup=BeautifulSoup(gzip.decompress(f.read_bytes()),'lxml');url=json.loads((RAW/'acl-2019-fullschedule-github.meta.json').read_text())['url'];n=0
    for node in soup.select('.talk-title .titlelink'):
        n+=mark('ACL',2019,node.get_text(' ',strip=True),url,'Oral',node.get_text(' ',strip=True))
    print('ACL2019 preserved schedule',n,flush=True)

import openpyxl, io
f=RAW/'emnlp-2025-program-xlsx.gz'
if f.exists():
    wb=openpyxl.load_workbook(io.BytesIO(gzip.decompress(f.read_bytes())),read_only=True,data_only=True)
    url=json.loads((RAW/'emnlp-2025-program-xlsx.meta.json').read_text())['url'];n=0
    for row in wb.worksheets[0].values:
        if len(row)>7 and str(row[7]).strip().lower()=='oral':
            n+=mark('EMNLP',2025,str(row[2] or ''),url,'Oral',str(row[0])+'; '+str(row[11]))
    print('EMNLP2025 official spreadsheet',n,flush=True)

# Remaining award evidence verified from the association archive, author institution,
# best-paper session, and the program chairs' official announcement read through web.
evidence=[]
for key in ['acl-2019-awards-github','emnlp-2022-awards-report','iclr-2018-awards-cmu','emnlp-2018-schedule']:
    f=RAW/(key+'.gz')
    if f.exists():
        soup=BeautifulSoup(gzip.decompress(f.read_bytes()),'lxml')
        if key=='emnlp-2018-schedule':soup=soup.select_one('.session-papers-best')
        evidence.append((json.loads((RAW/(key+'.meta.json')).read_text())['url'],norm(soup.get_text(' ',strip=True))))
webfile=ROOT/'sources/web_verified_awards_0.txt'
if webfile.exists():evidence.append(('https://iclr-conf.medium.com/announcing-iclr-2021-outstanding-paper-awards-9ae0514734ab',norm(webfile.read_text())))
pending=[]
for row in json.loads((ROOT/'checks/award_pending.json').read_text()):
    p=next((p for p in papers if p['id']==row.get('paper_id')),None)
    ev=[u for u,t in evidence if norm(row['title']) in t]
    if ev and p:
        if row['award'] not in p['awards']:p['awards'].append(row['award'])
        for u in ev:
            if u not in p['award_evidence']:p['award_evidence'].append(u)
    else:pending.append(row)
save_json('checks/award_pending.json',pending)
save_json('checks/supplemental_oral_evidence.json',audit)
save_json('sources/resolved_universe.json.gz',papers)
print('Final oral',sum(p['oral'] for p in papers),flush=True)
