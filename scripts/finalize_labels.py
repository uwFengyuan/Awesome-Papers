from common import *
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse,parse_qs

papers=load_json('sources/resolved_universe.json.gz')
idx={(p['venue'],p['year'],norm(p['title'])):p for p in papers}
byid={p['id']:p for p in papers}
proofs=[]

# The clearly titled Oral Presentations chapter is stronger than proximity to a clock.
file=ROOT/'sources/handbook_texts/emnlp-2024-fullhandbook-lfs.txt'
url='https://media.githubusercontent.com/media/acl-org/emnlp-2024/main/downloads/EMNLP_2024_Handbook_digital.pdf'
if file.exists():
    pages=file.read_text().split('\f');selected=[(i+1,t) for i,t in enumerate(pages) if re.search(r'(?m)^\s*Oral Presentations\s*$',t[:350])]
    whole=norm('\n'.join(t for _,t in selected))
    for p in papers:
        if p['venue']!='EMNLP' or p['year']!=2024:continue
        p['oral']=False;p['oral_evidence']=[]
        if norm(p['title']) in whole:
            p['oral']=True;p['oral_evidence']=[url]
            p['presentation_original'].append('Oral (official handbook Oral Presentations chapter)')
            proofs.append({'id':p['id'],'source_url':url,'basis':'explicit Oral Presentations chapter, PDF pages 47-87'})

# Public platform metadata is used only when both the paper identity and a non-poster
# named main-paper session are clear. "poster_lecture" alone is not reliable for every year.
for venue,year in [('ACL',2024),('EMNLP',2021),('EMNLP',2024)]:
    rows={};sessions={}
    for f in RAW.glob(f'{venue.lower()}-{year}-underline-lectures-*.gz'):
        j=json.loads(gzip.decompress(f.read_bytes()));rows.update({x['id']:x for x in j.get('data',[])})
        sessions.update({x['id']:x['attributes'] for x in j.get('included',[]) if x['type']=='thin_event_sessions'})
    added=0
    for row in rows.values():
        a=row['attributes']
        if a.get('poster_lecture') is not False:continue
        p=idx.get((venue,year,norm(a.get('title',''))))
        if not p:continue
        rel=row.get('relationships',{}).get('event_session',{}).get('data') or {};session=sessions.get(rel.get('id'),{})
        name=session.get('name','')
        if session.get('poster_only') is not False or not name:continue
        if re.search(r'poster|workshop|tutorial|student research|\bSRW\b|^W\d|keynote|opening|closing|day \d',name,re.I):continue
        was=p['oral'];p['oral']=True;source=f'https://underline.io/events/{ {("ACL",2024):466,("EMNLP",2021):192,("EMNLP",2024):469}[(venue,year)]}/sessions/{rel["id"]}/lecture/{row["id"]}'
        if source not in p['oral_evidence']:p['oral_evidence'].append(source)
        p['presentation_original'].append('Oral (non-poster main-paper session: '+name+')')
        proofs.append({'id':p['id'],'source_url':source,'basis':'named non-poster session and exact main-track title','session':name})
        added+=not was
    print('Platform additional Oral',venue,year,added,flush=True)

# The legacy ICLR 2020 official program combines orals and spotlights. Retain the
# secondary 48-paper oral tier separately until primary tier evidence is recovered.
f=RAW/'iclr-2020-copilot.gz';cal=RAW/'iclr-2020-calendar.gz'
if f.exists() and cal.exists():
    text=norm(BeautifulSoup(gzip.decompress(cal.read_bytes()),'lxml').get_text(' ',strip=True));pending=[]
    for row in json.loads(gzip.decompress(f.read_bytes())):
        if row.get('status') not in ['Oral','Talk']:continue
        p=idx.get(('ICLR',2020,norm(row.get('title',''))))
        if not p and row.get('title')=='Dynamics-Aware Unsupervised Discovery of Skills':
            # Official legacy title changed word order; all five authors agree.
            p=byid.get('iclr-2020-1966')
        if not p:continue
        p['pdf_url']='https://openreview.net/pdf?id='+row['id']
        p['openreview_url']='https://openreview.net/forum?id='+row['id']
        p['oral_candidate']=True;p['oral_candidate_source']='https://raw.githubusercontent.com/papercopilot/paperlists/main/iclr/iclr2020.json'
        p['oral_candidate_note']='Secondary oral tier; official 2020 program groups orals and spotlights together. Not counted as confirmed Oral.'
        p['official_combined_session_verified']=norm(p['title']) in text
        pending.append({'id':p['id'],'title':p['title'],'candidate_source':p['oral_candidate_source'],'official_program':'https://iclr.cc/virtual_2020/calendar.html','combined_session_match':p['official_combined_session_verified']})
    save_json('checks/oral_pending.json',pending);print('ICLR2020 candidate tier',len(pending),flush=True)

for a in json.loads((ROOT/'checks/award_pending.json').read_text()):
    if a.get('paper_id') in byid:byid[a['paper_id']]['award_candidate']=a['award']

# Make the additional 2026 records reviewable without assigning an unverified main-track label.
f=ROOT/'checks/neurips_2026_additional_finance_candidates.json'
if f.exists():
    rows=json.loads(f.read_text())
    for i,row in enumerate(rows):
        row['main_track_status']='unverified; official all-track export; not admitted to main catalog'
        h=RAW/f'neurips-2026-additional-finance-{i}.gz'
        if h.exists():
            soup=BeautifulSoup(gzip.decompress(h.read_bytes()),'lxml')
            a=next((a for a in soup.select('a[href]') if 'openreview.net/forum' in a['href']),None)
            if a:row['openreview_url']=a['href']
    save_json('checks/neurips_2026_additional_finance_candidates.json',rows)

for p in papers:
    for field in ['awards','award_evidence','oral_evidence','presentation_original','metadata_sources']:
        p[field]=list(dict.fromkeys(p.get(field,[])))
save_json('checks/final_oral_evidence.json',proofs)
save_json('sources/resolved_universe.json.gz',papers)
print('Confirmed oral',sum(p['oral'] for p in papers),flush=True)
