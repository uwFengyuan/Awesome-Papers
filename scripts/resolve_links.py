from common import *
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse, parse_qs
import re

papers=load_json('sources/enriched_universe.json.gz')
idx={(p['venue'],p['year'],norm(p['title'])):p for p in papers}
for year in range(2017,2026):
    key=f'neurips-{year}-proceedings';f=RAW/(key+'.gz')
    if not f.exists():continue
    soup=BeautifulSoup(gzip.decompress(f.read_bytes()),'lxml');base=f'https://proceedings.neurips.cc/paper/{year}'
    n=0
    for a in soup.find_all('a',href=re.compile(r'-Abstract(?:-[A-Za-z_]+)?\.html$')):
        p=idx.get(('NeurIPS',year,norm(a.get_text(' ',strip=True))))
        if not p:continue
        u=urljoin(base,a['href']);pdf=u.replace('/hash/','/file/').replace('-Abstract','-Paper').replace('.html','.pdf')
        p['pdf_url']=pdf;p['proceedings_url']=u
        if base not in p['metadata_sources']:p['metadata_sources'].append(base)
        n+=1
    print('NeurIPS proceedings links',year,n,flush=True)
for year in range(2017,2025):
    key=f'iclr-{year}-copilot';f=RAW/(key+'.gz')
    if not f.exists():continue
    n=0
    for row in json.loads(gzip.decompress(f.read_bytes())):
        p=idx.get(('ICLR',year,norm(row.get('title',''))))
        if not p:continue
        p['pdf_url']='https://openreview.net/pdf?id='+row['id'];p['openreview_url']='https://openreview.net/forum?id='+row['id']
        if not p['paper_url'] or 'iclr.cc/virtual/' in p['paper_url']:p['paper_url']=p['openreview_url']
        n+=1
    print('ICLR paper IDs',year,n,flush=True)
save_json('sources/resolved_universe.json.gz',papers)
