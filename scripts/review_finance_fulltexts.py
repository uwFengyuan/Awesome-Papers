"""Retrieve full texts for a high-recall finance audit; candidates stay outside the catalog.

This includes general time-series, retrieval, tabular, fairness and document methods
whose financial experiments are often absent from the abstract.
"""
from common import *
import csv
import io
import logging
import re
import difflib
import urllib.parse
import xml.etree.ElementTree as ET
import argparse
from pypdf import PdfReader
logging.getLogger('pypdf').setLevel(logging.ERROR)
parser=argparse.ArgumentParser()
parser.add_argument('--arxiv-only',action='store_true')
args=parser.parse_args()

DEST=ROOT/'checks/finance_expansion'
papers=load_json('sources/resolved_universe.json.gz')
finance=json.loads((ROOT/'checks/finance_review.json').read_text())['included']
focused=json.loads((DEST/'focused_queue.json').read_text())
focus_ids={p['id'] for p in focused}
family=re.compile(r'time.?series|forecasting|temporal point process|neural.*(?:SDE|stochastic differential)|dense retriev|retriever|text embedding|sentence embedding|rerank|re.rank|neural.*retriev|retrieval.*(?:pre.train|learning|zero.shot)|representation.*(?:retriev|matching)|retrieval.augmented|tabular|recourse|strategic classification|fair.*(?:classif|learning|decision)|algorithmic fairness|performative prediction|monotonic.*(?:neural|model)|(?:decision|classification) trees|counterfactual explanations|document.*(?:understand|extract|pre.train)|\binvoices?\b|\breceipts?\b|\bESG\b|\btaxation\b|\baccounting\b|risk measures|conditional value.at.risk|\bCVaR\b|Black.Scholes',re.I)
false=re.compile(r'credit assignment|credit propagation|credit attribution|credit.*(?:reasoning|policy optimization)|giving credit|hedg(?:ing|e).*(?:language|embedding|MDP)|scientific (?:debt|fraud)|taking stock|loanwords?|phonetic loans|(?:tree|proposition) bank',re.I)
explicit=re.compile(r'financ(?:e|ial)|stock market|credit (?:risk|default|scor)|loan(?:s| approv)|money launder|insurance|\bFinQA\b|\bFiQA\b',re.I)
selected=[]
for p in papers:
    if p['id'] in finance:continue
    if family.search(p['title']) or (p['id'] in focus_ids and not false.search(p['title'])):
        if false.search(p['title']) and not explicit.search(p.get('abstract','')):continue
        selected.append(p)
save_json('checks/finance_expansion/fulltext_screening_queue.json',selected)
print('Full-text screening queue',len(selected),flush=True)

local={}
for line in (ROOT/'checks/download_results.jsonl').read_text().splitlines():
    try:r=json.loads(line)
    except Exception:continue
    if r.get('status')=='downloaded' and (ROOT/r['local_path']).is_file():local[r['id']]=r
log=DEST/'review_downloads.jsonl'
existing={}
if log.exists():
    for line in log.read_text().splitlines():
        try:r=json.loads(line);existing[r['id']]=r
        except Exception:pass

def save_result(r):
    with LOCK:
        with log.open('a') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
    existing[r['id']]=r

def download(p,url,version='publisher_version',match=None):
    if 'arxiv.org/' in url:version='arxiv_author_version'
    result={'id':p['id'],'title':p['title'],'venue':p['venue'],'year':p['year'],'requested_url':url,'pdf_version':version}
    try:
        response=requests.get(url,timeout=(15,75),headers={'User-Agent':AGENT})
        data=response.content
        if response.status_code!=200 or not data.lstrip().startswith(b'%PDF-'):
            return dict(result,status='download_failed',error=f'HTTP {response.status_code} or not a PDF')
        pages=len(PdfReader(io.BytesIO(data),strict=False).pages)
        if not pages:return dict(result,status='download_failed',error='empty PDF')
        target=DEST/'review_pdfs'/p['venue']/str(p['year'])/(p['id']+'.pdf')
        target.parent.mkdir(parents=True,exist_ok=True)
        temp=target.with_suffix('.part');temp.write_bytes(data);temp.replace(target)
        result.update(status='downloaded',local_path=str(target.relative_to(ROOT)),bytes=len(data),
                      sha256=hashlib.sha256(data).hexdigest(),pages=pages,final_url=response.url,
                      downloaded_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
        if match:result['arxiv_match']=match
        return result
    except Exception as exc:return dict(result,status='download_failed',error=str(exc))

def direct(p):
    pid=p['id']
    old=local.get(pid) or existing.get(pid)
    if old and old.get('status')=='downloaded' and (ROOT/old['local_path']).is_file():return dict(old,reused=True)
    url=p.get('pdf_url','')
    if not url or 'openreview.net' in url:
        return {'id':pid,'status':'author_version_lookup_needed','publisher_pdf_url':url}
    return download(p,url)

if not args.arxiv_only:
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for i,result in enumerate(pool.map(direct,selected),1):
            save_result(result)
            if i%100==0:print('Direct downloads',i,'/',len(selected),flush=True)
print('Direct phase complete',flush=True)

todo=[p for p in selected if existing.get(p['id'],{}).get('status')!='downloaded']
ns={'a':'http://www.w3.org/2005/Atom'}
searchlog=DEST/'review_arxiv_searches.jsonl'
searched=set()
if searchlog.exists():
    for line in searchlog.read_text().splitlines():
        r=json.loads(line)
        if not r.get('search_error'):searched.add(r['id'])
todo=[p for p in todo if p['id'] not in searched]
print('Author-version lookup queue',len(todo),flush=True)

def terms(title):return ' '.join(re.findall(r'[A-Za-z0-9]+',re.sub(r'\\[A-Za-z]+',' ',title))[:15])

last=0
rate_limits=0
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    futures=[]
    for start in range(0,len(todo),12):
        group=todo[start:start+12]
        query=' OR '.join('ti:"'+terms(p['title'])+'"' for p in group)
        url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':query,'max_results':100})
        elapsed=time.monotonic()-last
        if elapsed<10:time.sleep(10-elapsed)
        last=time.monotonic()
        data,meta=fetch(url,'finance-body-arxiv-'+hashlib.sha256(query.encode()).hexdigest()[:24],timeout=60,retries=1)
        if not data and meta.get('error')=='HTTP 429':
            rate_limits+=1
            print('Rate limited; cooling down',30 if rate_limits==1 else 60,'seconds',flush=True)
            time.sleep(30 if rate_limits==1 else 60)
            if rate_limits>=3:
                print('Stopping author lookups after repeated rate limits; remaining records retained.',flush=True)
                break
        elif data:rate_limits=0
        entries=[]
        if data:
            try:
                for e in ET.fromstring(data).findall('a:entry',ns):
                    entries.append({'title':' '.join(e.findtext('a:title','',ns).split()),
                        'authors':[x.findtext('a:name','',ns) for x in e.findall('a:author',ns)],
                        'arxiv_url':e.findtext('a:id','',ns).replace('http:','https:'),
                        'pdf_url':next((x.get('href','').replace('http:','https:') for x in e.findall('a:link',ns) if x.get('title')=='pdf'),'')})
            except Exception:pass
        for p in group:
            match=None
            for e in entries:
                ratio=difflib.SequenceMatcher(None,norm(p['title']),norm(e['title'])).ratio()
                pa={norm(a.split()[-1]) for a in p['authors'] if a.split()}
                ea={norm(a.split()[-1]) for a in e['authors'] if a.split()}
                if norm(p['title'])==norm(e['title']) or (ratio>=.965 and pa&ea):
                    match=dict(e,title_similarity=ratio,title_match='exact_normalized' if ratio==1 else 'near_exact_plus_author');break
            record={'id':p['id'],'title':p['title'],'query_url':url,'match':match}
            if not data:record['search_error']=meta.get('error','unreadable response')
            with searchlog.open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
            if match and match['pdf_url']:futures.append(pool.submit(download,p,match['pdf_url'],'arxiv_author_version',match))
        # Harvest finished downloads regularly, retaining successful results immediately.
        still=[]
        for future in futures:
            if future.done():save_result(future.result())
            else:still.append(future)
        futures=still
        if start%120==0:print('Author lookups',min(start+len(group),len(todo)),'/',len(todo),flush=True)
    for future in concurrent.futures.as_completed(futures):save_result(future.result())
save_json('checks/finance_expansion/review_downloads.json',list(existing.values()))
print('REVIEW RETRIEVAL COMPLETE',len(selected),'available',sum(existing.get(p['id'],{}).get('status')=='downloaded' for p in selected),flush=True)
