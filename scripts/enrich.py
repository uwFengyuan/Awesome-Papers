from common import *
from bs4 import BeautifulSoup
import re, csv, io, difflib
from collections import defaultdict, Counter
from urllib.parse import urlparse, parse_qs

def cached(key):
    f=RAW/(key+'.gz');return gzip.decompress(f.read_bytes()) if f.exists() else None
def src(key):
    f=RAW/(key+'.meta.json');return json.loads(f.read_text()).get('url','') if f.exists() else ''

papers=load_json('sources/main_universe.json.gz')
print('Loaded',len(papers),flush=True)

# Merge duplicate title variants only when a near-identical final-proceedings title
# is paired to a conference record. Keep an audit trail of every such merge.
groups=defaultdict(list)
for p in papers:groups[(p['venue'],p['year'])].append(p)
removed=set();merges=[]
for (venue,year),rows in groups.items():
    if venue not in ['ICML','NeurIPS']:continue
    extras=[p for p in rows if ('-pmlr-' in p['id'] or (venue=='NeurIPS' and year<=2019 and not p.get('abstract')))]
    extra_ids={p['id'] for p in extras}
    existing=[p for p in rows if p['id'] not in extra_ids]
    for p in extras:
        pn=norm(p['title'])
        choices=[q for q in existing if abs(len(norm(q['title']))-len(pn))<=max(18,len(pn)*.15)]
        ranked=sorted(((difflib.SequenceMatcher(None,pn,norm(q['title'])).ratio(),q) for q in choices),key=lambda x:x[0],reverse=True)
        if not ranked or ranked[0][0]<.92 or len(pn)<22:continue
        score,q=ranked[0]
        if len(ranked)>1 and ranked[1][0]>.88:continue
        # A match must also preserve substantial title words.
        pw=set(re.findall(r'[a-z]{4,}',p['title'].lower()));qw=set(re.findall(r'[a-z]{4,}',q['title'].lower()))
        if len(pw&qw)/max(1,min(len(pw),len(qw)))<.75:continue
        for field in ['pdf_url','proceedings_url']:
            if p.get(field):q[field]=p[field]
        for field in ['metadata_sources','awards','award_evidence','oral_evidence','presentation_original']:
            for value in p.get(field,[]):
                if value not in q.setdefault(field,[]):q[field].append(value)
        q['oral']=q.get('oral',False) or p.get('oral',False)
        removed.add(p['id']);merges.append({'removed_id':p['id'],'retained_id':q['id'],'proceedings_title':p['title'],'event_title':q['title'],'title_similarity':score})
papers=[p for p in papers if p['id'] not in removed]
save_json('checks/title_variant_merges.json',merges)
idx={(p['venue'],p['year'],norm(p['title'])):p for p in papers}
for m in merges:
    p=next(x for x in papers if x['id']==m['retained_id']);idx[(p['venue'],p['year'],norm(m['proceedings_title']))]=p

def find(venue,year,title):
    key=(venue,year,norm(title))
    if key in idx:return idx[key]
    # Schedules occasionally include a final period or a [Best Paper] badge.
    title=re.sub(r'\[(?:best|outstanding|main|long|short)[^\]]*\]','',title,flags=re.I)
    return idx.get((venue,year,norm(title)))

def mark(venue,year,title,url,label='Oral'):
    p=find(venue,year,title)
    if p:
        p['oral']=True
        if url not in p['oral_evidence']:p['oral_evidence'].append(url)
        if label not in p['presentation_original']:p['presentation_original'].append(label)
        return True
    return False

# Official HTML schedules with a separate CSS class for oral-paper titles.
for venue,year,key,selector in [
    ('ACL',2017,'acl-2017-schedule','.paper-title'),
    ('ACL',2018,'acl-2018-schedule2','.talk-title'),
    ('EMNLP',2018,'emnlp-2018-schedule','.paper-title'),
    ('EMNLP',2019,'emnlp-2019-schedule2','.paper-title')]:
    raw=cached(key)
    if not raw:continue
    soup=BeautifulSoup(raw,'lxml');n=0
    for node in soup.select(selector):n+=mark(venue,year,node.get_text(' ',strip=True),src(key))
    print('HTML oral',venue,year,n,flush=True)

# The ICLR 2017 complete official poster list contains the titles as text.
raw=cached('iclr-2017-conference-posters')
if raw:
    text=norm(BeautifulSoup(raw,'lxml').get_text(' ',strip=True))
    for p in papers:
        if p['venue']=='ICLR' and p['year']==2017 and norm(p['title']) in text:
            p['main_verification']='official legacy conference poster list';p['metadata_sources'].append(src('iclr-2017-conference-posters'))

# ACL 2021 gives an individual timed presentation to each paper in the main schedule.
raw=cached('acl-2021-overview')
if raw:
    soup=BeautifulSoup(raw,'lxml');n=0
    for row in soup.find_all('tr'):
        cells=row.find_all('td',recursive=False)
        if len(cells)<2 or not re.fullmatch(r'\d{1,2}:\d{2}\s*[–-]\s*\d{1,2}:\d{2}',cells[0].get_text(' ',strip=True)):continue
        for e in cells[1].find_all('em'):
            n+=mark('ACL',2021,e.get_text(' ',strip=True),src('acl-2021-overview'),'Scheduled individual paper talk (2021 virtual main program)')
    print('ACL2021 timed talks',n,flush=True)

# Explicit Oral event membership in the official ACL 2023 virtual-site dataset.
raw=cached('acl-2023-conference-json')
if raw:
    data=json.loads(raw);n=0
    for e in data['events'].values():
        if e.get('type')!='Oral':continue
        for pid in e.get('paper_ids',[]):
            row=data['papers'].get(pid,{})
            n+=mark('ACL',2023,row.get('title',''),src('acl-2023-conference-json'))
    print('ACL2023 oral',n,flush=True)
raw=cached('emnlp-2023-oral-tsv')
if raw:
    n=0
    for row in csv.DictReader(io.StringIO(raw.decode('utf-8-sig')),delimiter='\t'):
        if row.get('Category')=='Main-Oral':n+=mark('EMNLP',2023,row.get('Title',''),src('emnlp-2023-oral-tsv'))
    print('EMNLP2023 oral',n,flush=True)

# Authoritative public spreadsheets linked from the official program pages.
import openpyxl
for venue,year,key,title_col,type_col in [('ACL',2025,'acl-2025-schedule-xlsx',1,5),('ACL',2026,'acl-2026-schedule-xlsx',1,9),('EMNLP',2026,'emnlp-2026-schedule-xlsx',1,2)]:
    raw=cached(key)
    if not raw:continue
    wb=openpyxl.load_workbook(io.BytesIO(raw),read_only=True,data_only=True);n=0
    for row in wb.worksheets[0].values:
        if len(row)<=max(title_col,type_col):continue
        if re.search(r'\boral\b',str(row[type_col] or ''),re.I):n+=mark(venue,year,str(row[title_col] or ''),src(key),str(row[type_col]))
    print('XLSX oral',venue,year,n,flush=True)

# Official award pages: admitted only with a matching main-track paper title.
evidence=defaultdict(list)
for f in RAW.glob('*.gz'):
    key=f.name[:-3];m=re.match(r'(icml|iclr|neurips|acl|emnlp)-(20\d\d)-(?:awards|bestpapers|blogawards|awarddetail|awardorigin|honmention|award2)',key)
    if not m:continue
    soup=BeautifulSoup(gzip.decompress(f.read_bytes()),'lxml')
    for junk in soup(['script','style','nav','footer']):junk.decompose()
    v={'icml':'ICML','iclr':'ICLR','neurips':'NeurIPS','acl':'ACL','emnlp':'EMNLP'}[m[1]]
    evidence[(v,int(m[2]))].append((src(key),norm(soup.get_text(' ',strip=True))))
# ACL Wiki is maintained by the scientific association; the year is checked by main-track title join.
raw=cached('acl-wiki-awards')
if raw:
    wiki=norm(BeautifulSoup(raw,'lxml').get_text(' ',strip=True))
    for v in ['ACL','EMNLP']:
        for y in range(2017,2027):evidence[(v,y)].append((src('acl-wiki-awards'),wiki))
pending=[];excluded=[]
candidates=json.loads((ROOT/'sources/award_candidates.json').read_text())
for a in candidates:
    if any(w in a['award'].lower() for w in ['test of time','influential','most cited']):continue
    p=find(a['venue'],a['year'],a['title'])
    if not p:
        excluded.append(dict(a,reason='not matched to main proceedings; includes non-main tracks and title variants'));continue
    ev=[u for u,t in evidence[(a['venue'],a['year'])] if norm(a['title']) in t or norm(p['title']) in t]
    if ev:
        if a['award'] not in p['awards']:p['awards'].append(a['award'])
        for u in ev:
            if u not in p['award_evidence']:p['award_evidence'].append(u)
    elif not p.get('awards'):pending.append(dict(a,paper_id=p['id'],reason='official award announcement not yet verified'))
save_json('checks/award_pending.json',pending)
save_json('checks/award_outside_or_title_unmatched.json',excluded)

save_json('sources/enriched_universe.json.gz',papers)
print('Enriched universe',len(papers),'merges',len(merges),'oral',sum(p['oral'] for p in papers),'award',sum(bool(p['awards']) for p in papers),'pending awards',len(pending),flush=True)
