"""Resumable PDF downloads; valid files only, with SHA-256 and page-count verification."""
from common import *
import argparse, re, os, io, logging
from urllib.parse import urlparse, urljoin, parse_qs
from bs4 import BeautifulSoup
from pypdf import PdfReader

logging.getLogger('pypdf').setLevel(logging.ERROR)
ap=argparse.ArgumentParser();ap.add_argument('--workers',type=int,default=8);ap.add_argument('--finance-only',action='store_true');ap.add_argument('--id');ap.add_argument('--ids',nargs='+');args=ap.parse_args()
papers=load_json('sources/resolved_universe.json.gz')
finance={}
ff=ROOT/'checks/finance_review.json'
if ff.exists():finance=json.loads(ff.read_text()).get('included',{})
selected=[p for p in papers if ((p['oral'] or p.get('oral_candidate') or p.get('award_candidate') or bool(p['awards'])) and not args.finance_only) or p['id'] in finance]
def worth_award(p):
    return any(not re.search(r'^(?:SAC|Area Chair)',a,re.I) for a in p['awards'])
selected=[p for p in selected if p['oral'] or p.get('oral_candidate') or p.get('award_candidate') or worth_award(p) or p['id'] in finance]
if args.id:selected=[p for p in selected if p['id']==args.id]
if args.ids:selected=[p for p in selected if p['id'] in set(args.ids)]
selected.sort(key=lambda p:(p['id'] not in finance,not worth_award(p),p['venue'],p['year'],p['title']))
print('PDF queue',len(selected),flush=True)
results={};log=ROOT/'checks/download_results.jsonl'
if log.exists():
    for line in log.read_text().splitlines():
        try:r=json.loads(line);results[r['id']]=r
        except Exception:pass
blocked={'openreview.net':'HTTP 403 challenge verification required (observed public PDF download endpoint)'}
lock=threading.Lock()

def path_for(p):
    registered=results.get(p['id'],{}).get('local_path')
    if registered and (ROOT/registered).is_file():return ROOT/registered
    slug=re.sub(r'[^A-Za-z0-9]+','_',p['title']).strip('_')[:105]
    return ROOT/'pdfs'/p['venue']/str(p['year'])/(p['id']+'__'+slug+'.pdf')

def resolve(p):
    if p.get('pdf_url'):return p['pdf_url']
    u=p.get('paper_url') or p.get('virtual_url')
    if not u:return ''
    if 'openreview.net/forum' in u:return u.replace('/forum?','/pdf?')
    if u.endswith('.pdf'):return u
    data,meta=fetch(u,'paperpage-'+p['id'],timeout=35,retries=1)
    if not data:return ''
    soup=BeautifulSoup(data,'lxml')
    tag=soup.find('meta',attrs={'name':'citation_pdf_url'})
    if tag:return urljoin(u,tag.get('content',''))
    for a in soup.find_all('a',href=True):
        h=urljoin(u,a['href']);label=a.get_text(' ',strip=True).lower()
        if 'openreview.net/forum?' in h:return h.replace('/forum?','/pdf?')
        if h.endswith('.pdf') and label in ['paper','pdf','download pdf','paper pdf']:return h
    return ''

def job(p):
    pid=p['id'];target=path_for(p);old=results.get(pid,{})
    if old.get('status')=='downloaded' and target.exists() and target.stat().st_size==old.get('bytes'):return dict(old,reused=True)
    url=resolve(p);r={'id':pid,'title':p['title'],'venue':p['venue'],'year':p['year'],'requested_url':url,'local_path':str(target.relative_to(ROOT))}
    if not url:r.update(status='missing_pdf_url',error='No published PDF URL resolved from recorded source');return r
    if urlparse(url).hostname in blocked:
        r.update(status='access_blocked',error=blocked[urlparse(url).hostname]);return r
    error=''
    for attempt in range(3):
        try:
            response=requests.get(url,timeout=(15,90),headers={'User-Agent':AGENT})
            if response.status_code!=200:
                error=f'HTTP {response.status_code}'
                if response.status_code in [401,403]:
                    r.update(status='access_blocked',error=error);return r
                if response.status_code not in [429,500,502,503,504]:break
                time.sleep(2+attempt*3);continue
            data=response.content
            if not data.lstrip().startswith(b'%PDF-'):error='Response is not a PDF';break
            reader=PdfReader(io.BytesIO(data),strict=False);pages=len(reader.pages)
            if pages<1:error='PDF contains no pages';break
            target.parent.mkdir(parents=True,exist_ok=True)
            tmp=target.with_suffix('.pdf.part');tmp.write_bytes(data);tmp.replace(target)
            r.update(status='downloaded',final_url=response.url,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),pages=pages,downloaded_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat())
            return r
        except Exception as exc:error=str(exc)
        time.sleep(1+attempt)
    r.update(status='download_failed',error=error);return r

done=0;counts={}
with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
    pending={pool.submit(job,p):p['id'] for p in selected}
    for fut in concurrent.futures.as_completed(pending):
        try:r=fut.result()
        except Exception as exc:r={'id':pending[fut],'status':'internal_error','error':str(exc)}
        with log.open('a') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
        results[r['id']]=r;done+=1;counts[r['status']]=counts.get(r['status'],0)+1
        if done%50==0:print(done,'/',len(selected),counts,flush=True)
save_json('checks/download_results.json',list(results.values()))
print('COMPLETE',counts,flush=True)
