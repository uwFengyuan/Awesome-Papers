"""Build the main-track universe from official sources; attach independently evidenced labels."""
from common import *
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET
from urllib.parse import urljoin, urlparse, parse_qs
from collections import Counter, defaultdict

def cached(key):
    p = RAW / (key + '.gz')
    return gzip.decompress(p.read_bytes()) if p.exists() else None

def source(key):
    p = RAW / (key + '.meta.json')
    return json.loads(p.read_text()).get('url','') if p.exists() else ''

def txt(e):
    return re.sub(r'\s+', ' ', ''.join(e.itertext())).strip() if e is not None else ''

def pdf_url(url):
    url = (url or '').replace('http://','https://')
    if 'openreview.net/' in url:
        ident = parse_qs(urlparse(url).query).get('id',[''])[0]
        return 'https://openreview.net/pdf?id=' + ident if ident else ''
    if re.search(r'-Abstract(?:-Conference)?\.html',url):
        return url.replace('/hash/','/file/').replace('-Abstract-Conference.html','-Paper-Conference.pdf').replace('-Abstract.html','-Paper.pdf')
    return url if url.lower().endswith('.pdf') else ''

papers = {}
by_title = {}
exclusions = []

def add(p):
    p.setdefault('authors',[]);p.setdefault('abstract','');p.setdefault('paper_url','');p.setdefault('pdf_url','')
    p.setdefault('awards',[]);p.setdefault('award_evidence',[]);p.setdefault('oral',False);p.setdefault('oral_evidence',[])
    p.setdefault('presentation_original',[]);p.setdefault('code_urls',[]);p.setdefault('metadata_sources',[])
    p.setdefault('track','main');p.setdefault('abstract_source','')
    key = (p['venue'],p['year'],norm(p['title']))
    if key in by_title:
        old = papers[by_title[key]]
        for f in ['authors','abstract','pdf_url','paper_url','abstract_source']:
            if not old.get(f) and p.get(f):old[f]=p[f]
        for f in ['awards','award_evidence','oral_evidence','presentation_original','code_urls','metadata_sources']:
            for val in p.get(f,[]):
                if val and val not in old[f]:old[f].append(val)
        old['oral'] |= p['oral']
        return old
    papers[p['id']] = p;by_title[key]=p['id'];return p

# ACL Anthology maintained XML explicitly identifies proceedings volumes and awards.
for venue in ['ACL','EMNLP']:
    for year in range(2017,2027):
        key=f'{venue.lower()}-{year}-anthology';raw=cached(key)
        if not raw:continue
        root=ET.fromstring(raw);coll=root.get('id')
        for vol in root.findall('volume'):
            vid=vol.get('id');book=txt(vol.find('meta/booktitle'))
            is_main = (vid in ['long','short','main'] if venue=='ACL' else vid=='main') if year>=2020 else (vid in ['1','2'] if venue=='ACL' else vid=='1')
            if not is_main:continue
            for e in vol.findall('paper'):
                pid=(f'{coll}-{vid}{int(e.get("id")):03d}' if year<2020 else f'{coll}-{vid}.{e.get("id")}')
                url='https://aclanthology.org/'+pid+'/'
                p={'id':pid,'venue':venue,'year':year,'title':txt(e.find('title')),
                   'authors':[txt(a.find('first'))+' '+txt(a.find('last')) for a in e.findall('author')],
                   'abstract':txt(e.find('abstract')),'abstract_source':url,'paper_url':url,
                   'pdf_url':url[:-1]+'.pdf','booktitle':book,'bibkey':txt(e.find('bibkey')),
                   'doi':txt(e.find('doi')),'pages':txt(e.find('pages')),
                   'awards':[a.get('name') for a in e.findall('award')],
                   'award_evidence':[url] if e.findall('award') else [],'metadata_sources':[source(key)]}
                p['code_urls'] = sorted(set(re.findall(r'https?://(?:github\.com|gitlab\.com)/[^\s<>\\)]+',p['abstract'])))
                add(p)

# Main-track event records. A paper can occur as both a poster and an oral.
for venue in ['ICML','ICLR','NeurIPS']:
    v=venue.lower()
    for year in range(2020,2027):
        key=f'{v}-{year}-events';raw=cached(key)
        if not raw:continue
        events=json.loads(raw).get('results',[])
        abstracts={}
        ar=cached(f'{v}-{year}-abstracts')
        if ar:
            aj=json.loads(ar)
            if isinstance(aj,dict):abstracts=aj
            elif isinstance(aj,list):abstracts={str(x.get('id')):x.get('abstract','') for x in aj}
        for e in events:
            su=e.get('sourceurl') or '';etype=e.get('eventtype') or '';virt=e.get('virtualsite_url') or ''
            if etype not in ['Poster','Oral','Spotlight'] or (virt and not any(w in virt for w in ['/poster/','/oral/','/spotlight/'])):continue
            if su and '/Conference' not in su and year>=2022 and not (venue=='ICML' and year==2022 and 'cmt3.research.microsoft.com' in su):
                exclusions.append({'venue':venue,'year':year,'title':e['name'],'sourceurl':su,'reason':'outside main conference track'});continue
            if not su and year>=2022:continue
            title=e.get('name','').strip()
            if not title:continue
            if venue=='ICML' and year>=2024 and title.lower().startswith('position:'):continue
            abstract=e.get('abstract') or abstracts.get(str(e['id'])) or ''
            if isinstance(abstract,dict):abstract=abstract.get('abstract','')
            url=e.get('paper_url') or ''
            media=e.get('eventmedia',[])
            if not url:
                url=next((m.get('uri') for m in media if m.get('name') in ['OpenReview','Paper','PDF'] and m.get('uri')), '')
            direct=e.get('paper_pdf_url') or ''
            pdf=pdf_url(direct) or pdf_url(url)
            if not url or url.startswith('/'):
                url=urljoin(f'https://{v}.cc',virt or f'/virtual/{year}/poster/{e["id"]}')
            eventurl=urljoin(f'https://{v}.cc',virt or f'/virtual/{year}/poster/{e["id"]}')
            ident=parse_qs(urlparse(url).query).get('id',[''])[0]
            uid=f'{v}-{year}-'+(ident or str(e['id']))
            dec=e.get('decision') or '';isoral=etype=='Oral' or bool(re.search(r'\boral\b',dec,re.I))
            if venue=='ICLR' and year==2023 and 'notable-top-25%' in dec:isoral=False
            p={'id':uid,'venue':venue,'year':year,'title':title,
               'authors':[a.get('fullname','') for a in e.get('authors',[])],
               'abstract':abstract.strip(),'abstract_source':eventurl,'paper_url':url,'pdf_url':pdf,
               'oral':isoral,'oral_evidence':[source(key),eventurl] if isoral else [],
               'presentation_original':list(filter(None,[dec,etype,e.get('event_type')])),
               'metadata_sources':[source(key)],'virtual_url':eventurl,'source_venue':su,
               'topic_original':e.get('topic','')}
            p['code_urls']=sorted(set(re.findall(r'https?://(?:github\.com|gitlab\.com)/[^\s<>\\)]+',p['abstract'])))
            add(p)

# Official historical Downloads form supplies accepted papers and full abstracts.
for venue in ['ICML','ICLR','NeurIPS']:
    v=venue.lower()
    for year in range(2017,2020):
        key=f'{v}-{year}-download-json';raw=cached(key)
        if not raw:continue
        rows=json.loads(raw)
        for e in rows:
            title=e.get('name','').strip();url=e.get('virtualsite_url','')
            if not title:continue
            authors=re.sub(r'\s*\([^)]*\)','',e.get('speakers/authors','')).split(', ')
            p={'id':f'{v}-{year}-'+url.rstrip('/').split('/')[-1],'venue':venue,'year':year,
               'title':title,'authors':authors,'abstract':e.get('abstract',''),'abstract_source':source(key),
               'paper_url':url,'virtual_url':url,'metadata_sources':[source(key)],'presentation_original':['Poster']}
            add(p)
        # Oral event cards provide explicit title and presentation evidence.
        raw=cached(f'{v}-{year}-oralhtml')
        if raw:
            soup=BeautifulSoup(raw,'lxml')
            for card in soup.select('.event-card'):
                title=card.select_one('.event-title');a=title.find('a') if title else None
                if not a:continue
                pkey=(venue,year,norm(a.get_text(' ',strip=True)));pid=by_title.get(pkey)
                if pid:
                    p=papers[pid];p['oral']=True;p['oral_evidence'].append(source(f'{v}-{year}-oralhtml'))
                    p['oral_evidence'].append(urljoin(f'https://{v}.cc',a.get('href')))
                    p['presentation_original'].append('Oral')

# ICLR 2017 is in the legacy official archive, with separate conference and workshop lists.
archive=cached('iclr-2017-schedule')
legacy_copilot=cached('iclr-2017-copilot')
if legacy_copilot:
    records=json.loads(legacy_copilot)
    for e in records:
        if e.get('status') not in ['Poster','Oral','Spotlight']:continue
        pid=e['id'];url='https://openreview.net/forum?id='+pid
        add({'id':'iclr-2017-'+pid,'venue':'ICLR','year':2017,'title':e['title'],'authors':e.get('author','').split(';'),
             'abstract':e.get('abstract',''),'abstract_source':source('iclr-2017-copilot'),'paper_url':url,
             'pdf_url':'https://openreview.net/pdf?id='+pid,'metadata_sources':[source('iclr-2017-copilot')],
             'presentation_original':[e['status']],'main_verification':'pending archive conference-list cross-check'})
    if archive:
        soup=BeautifulSoup(archive,'lxml')
        for a in soup.select('a[href*="openreview.net/forum"]'):
            title=a.get_text(' ',strip=True);pid=by_title.get(('ICLR',2017,norm(title)))
            if not pid:continue
            p=papers[pid];p['oral']=True;p['oral_evidence']=[source('iclr-2017-schedule')]
            p['main_verification']='official conference contributed-talk schedule'
            if 'BEST PAPER AWARD' in a.parent.get_text(' ',strip=True):
                p['awards']=['Best Paper Award'];p['award_evidence']=[source('iclr-2017-schedule')]

    # Cross-check the complete legacy list, not just contributed talks.
    raw=cached('iclr-2017-conference-posters')
    if raw:
        soup=BeautifulSoup(raw,'lxml')
        ids={parse_qs(urlparse(a.get('href')).query).get('id',[''])[0] for a in soup.select('a[href*="openreview.net/"]')}
        for p in papers.values():
            if p['venue']=='ICLR' and p['year']==2017 and p['id'].removeprefix('iclr-2017-') in ids:
                p['main_verification']='official legacy conference poster list'
                p['metadata_sources'].append(source('iclr-2017-conference-posters'))

# PMLR supplies final proceedings URLs and papers absent from the event snapshot.
for year in range(2017,2026):
    key=f'icml-{year}-pmlr';raw=cached(key)
    if not raw:continue
    soup=BeautifulSoup(raw,'lxml')
    for block in soup.select('div.paper'):
        title_el=block.select_one('.title');links=block.select_one('.links')
        if not title_el or not links:continue
        title=title_el.get_text(' ',strip=True)
        if year>=2024 and title.lower().startswith('position:'):continue
        a=next((a for a in links.find_all('a') if a.get_text(strip=True)=='abs'),None)
        pa=next((a for a in links.find_all('a') if a.get_text(strip=True)=='Download PDF'),None)
        if not a or not pa:continue
        url=a['href'].replace('http://','https://');direct=pa['href'].replace('http://','https://')
        pid=by_title.get(('ICML',year,norm(title)))
        if pid:
            p=papers[pid];p['pdf_url']=direct;p['proceedings_url']=url
            if source(key) not in p['metadata_sources']:p['metadata_sources'].append(source(key))
        else:
            slug=url.rsplit('/',1)[-1].replace('.html','')
            authors=block.select_one('.authors')
            add({'id':f'icml-{year}-pmlr-{slug}','venue':'ICML','year':year,'title':title,
                 'authors':authors.get_text(' ',strip=True).split(',') if authors else [],
                 'paper_url':url,'pdf_url':direct,'proceedings_url':url,'metadata_sources':[source(key)],
                 'main_verification':'official PMLR proceedings'})

for year in range(2017,2020):
    key=f'neurips-{year}-proceedings';raw=cached(key)
    if not raw:continue
    soup=BeautifulSoup(raw,'lxml')
    for a in soup.find_all('a',href=re.compile(r'-Abstract\.html$')):
        title=a.get_text(' ',strip=True);url=urljoin(source(key),a['href'])
        pid=by_title.get(('NeurIPS',year,norm(title)))
        if pid:
            p=papers[pid];p['paper_url']=url;p['pdf_url']=pdf_url(url)
            p['metadata_sources'].append(source(key))
        else:
            add({'id':f'neurips-{year}-'+url.split('/')[-1].split('-')[0],'venue':'NeurIPS','year':year,
                 'title':title,'paper_url':url,'pdf_url':pdf_url(url),'metadata_sources':[source(key)]})

# Explicit historical oral cards where the event feed omits the decision field.
for venue in ['ICML','ICLR','NeurIPS']:
    year=2020;key=f'{venue.lower()}-{year}-oralhtml';raw=cached(key)
    if not raw:continue
    soup=BeautifulSoup(raw,'lxml')
    for card in soup.select('.event-card'):
        title=card.select_one('.event-title')
        if not title:continue
        pid=by_title.get((venue,year,norm(title.get_text(' ',strip=True))))
        if pid:
            p=papers[pid];p['oral']=True;p['oral_evidence'].append(source(key))

# ICML 2017 handbook explicitly states that each accepted paper has an oral presentation.
for p in papers.values():
    if p['venue']=='ICML' and p['year']==2017:
        p['oral']=True;p['oral_evidence']=[source('icml-2017-book')]
        p['presentation_original'].append('Oral (all accepted papers; official 2017 handbook)')

# Attach independently recorded URLs from historical indexes only after an official title join.
for venue in ['ICML','ICLR']:
    for year in range(2017,2020):
        raw=cached(f'{venue.lower()}-{year}-copilot')
        if not raw:continue
        for e in json.loads(raw):
            pid=by_title.get((venue,year,norm(e.get('title',''))))
            if not pid:continue
            p=papers[pid]
            if venue=='ICLR':
                p['paper_url']='https://openreview.net/forum?id='+e['id'];p['pdf_url']='https://openreview.net/pdf?id='+e['id']
            for k in ['pdf','proceeding','openreview','paper','site']:
                value=e.get(k)
                if isinstance(value,str) and pdf_url(value) and not p['pdf_url']:p['pdf_url']=pdf_url(value)

# Award discovery index; no "most cited" entries are admitted.
secondary=RAW/'probe_awards.txt';award_candidates=[]
if secondary.exists():
    soup=BeautifulSoup(secondary.read_bytes(),'lxml')
    for block in soup.find_all('div',id=re.compile(r'^(ICML|ICLR|ACL|EMNLP|NeurIPS|NIPS)20\d\d$')):
        m=re.match(r'^(.*?)(20\d\d)$',block.get('id'));venue=m[1];year=int(m[2])
        if year<2017 or year>2026:continue
        if venue=='NIPS':venue='NeurIPS'
        current=''
        for elem in block.find_all('div',class_=lambda c:c and ('award-title' in c or 'award-info' in c)):
            if 'award-title' in elem.get('class',[]):current=elem.get_text(' ',strip=True).rstrip(':')
            else:
                a=elem.select_one('.paper-title a')
                if not a:continue
                award_candidates.append({'venue':venue,'year':year,'title':a.get_text(' ',strip=True),'award':current,'url':a.get('href'),'discovery_source':'https://aibestpape.rs/'})

# Award text snapshots from official conference sites, blogs and the ACL Wiki.
evidence=defaultdict(list)
for file in RAW.glob('*.gz'):
    k=file.name[:-3]
    m=re.match(r'(icml|iclr|neurips|acl|emnlp)-(20\d\d)-(?:awards|bestpapers|blogawards)',k)
    if m:
        venue={'icml':'ICML','iclr':'ICLR','neurips':'NeurIPS','acl':'ACL','emnlp':'EMNLP'}[m[1]];year=int(m[2])
        soup=BeautifulSoup(gzip.decompress(file.read_bytes()),'lxml')
        for junk in soup(['script','style','nav','footer']):junk.decompose()
        evidence[(venue,year)].append((source(k),norm(soup.get_text(' ',strip=True))))
for venue in ['icml','iclr','neurips']:
    raw=cached(venue+'-blog-awards')
    if not raw:continue
    for post in json.loads(raw):
        title=BeautifulSoup(post['title']['rendered'],'lxml').get_text()
        if not any(w in title.lower() for w in ['paper award','outstanding paper','icml 2026 awards','2022 awards','award recipients']):continue
        v={'icml':'ICML','iclr':'ICLR','neurips':'NeurIPS'}[venue]
        evidence[(v,int(post['date'][:4]))].append((post['link'],norm(BeautifulSoup(post['content']['rendered'],'lxml').get_text(' ',strip=True))))

pending_awards=[];outside_awards=[]
for a in award_candidates:
    if any(s in a['award'].lower() for s in ['test of time','time award','most cited','influential']):
        outside_awards.append(a);continue
    pid=by_title.get((a['venue'],a['year'],norm(a['title'])))
    if not pid:
        # Exact normalized title can vary by subtitles or TeX notation; no fuzzy automatic admission.
        pending_awards.append(dict(a,reason='no exact official main-track title match'));continue
    p=papers[pid];ev=[url for url,t in evidence[(a['venue'],a['year'])] if norm(a['title']) in t]
    if ev:
        if a['award'] not in p['awards']:p['awards'].append(a['award'])
        for u in ev:
            if u not in p['award_evidence']:p['award_evidence'].append(u)
    elif not p['awards']:pending_awards.append(dict(a,reason='award discovery awaiting official award evidence',paper_id=pid))

save_json('sources/award_candidates.json',award_candidates)
save_json('checks/award_pending.json',pending_awards)
save_json('checks/non_main_events_excluded.json',exclusions)
save_json('checks/historical_awards_separate.json',outside_awards)
save_json('sources/main_universe.json.gz',list(papers.values()))
print('Main universe',len(papers))
for v in ['ICML','ICLR','ACL','EMNLP','NeurIPS']:
    print(v,[(y,sum(p['venue']==v and p['year']==y for p in papers.values()),sum(p['venue']==v and p['year']==y and p['oral'] for p in papers.values()),sum(p['venue']==v and p['year']==y and bool(p['awards']) for p in papers.values())) for y in range(2017,2027)])
print('Pending awards',len(pending_awards))
