"""Official arXiv author versions for inaccessible publisher PDFs; title/author checked.

The accepted venue is established separately. An arXiv copy is never called the
conference final version. API requests are spaced at least three seconds apart.
"""
from common import *
import xml.etree.ElementTree as ET
import urllib.parse, re, io, difflib, logging
import argparse
from pypdf import PdfReader
logging.getLogger('pypdf').setLevel(logging.ERROR)
papers=load_json('sources/resolved_universe.json.gz');by_id={p['id']:p for p in papers}
results={}
for line in (ROOT/'checks/download_results.jsonl').read_text().splitlines():
    try:r=json.loads(line);results[r['id']]=r
    except Exception:pass
todo=[by_id[pid] for pid,r in results.items() if pid in by_id and r.get('status')!='downloaded']
finance=json.loads((ROOT/'checks/finance_review.json').read_text())['included']
parser=argparse.ArgumentParser()
parser.add_argument('--finance-only',action='store_true')
args=parser.parse_args()
if args.finance_only:todo=[p for p in todo if p['id'] in finance]
todo.sort(key=lambda p:(p['id'] not in finance,not bool(p['awards']),p['venue'],p['year']))
ns={'a':'http://www.w3.org/2005/Atom'};matchlog=ROOT/'checks/arxiv_matches.jsonl'
known={}
if matchlog.exists():
    for line in matchlog.read_text().splitlines():
        row=json.loads(line);known[row['id']]=row
todo=[p for p in todo if p['id'] not in known]
print('arXiv fallback candidates',len(todo),flush=True)
last_request=0;count=0;matched=0;downloaded=0

def title_terms(title):
    title=re.sub(r'\\[a-zA-Z]+',' ',title)
    words=re.findall(r'[A-Za-z0-9]+',title)
    return ' '.join(words[:13])

for start in range(0,len(todo),5):
    group=todo[start:start+5]
    query=' OR '.join('ti:"'+title_terms(p['title'])+'"' for p in group)
    url='https://export.arxiv.org/api/query?'+urllib.parse.urlencode({'search_query':query,'max_results':30})
    delta=time.monotonic()-last_request
    if delta<3.1:time.sleep(3.1-delta)
    last_request=time.monotonic();raw,meta=fetch(url,'arxiv-search-'+hashlib.sha256(query.encode()).hexdigest()[:20],timeout=50,retries=1)
    entries=[]
    if raw:
        try:
            root=ET.fromstring(raw)
            for e in root.findall('a:entry',ns):
                title=' '.join((e.findtext('a:title','',ns)).split())
                authors=[a.findtext('a:name','',ns) for a in e.findall('a:author',ns)]
                ident=e.findtext('a:id','',ns)
                pdf=next((l.get('href') for l in e.findall('a:link',ns) if l.get('title')=='pdf'),'')
                entries.append({'title':title,'authors':authors,'arxiv_url':ident.replace('http:','https:'),
                                'pdf_url':pdf.replace('http:','https:'),'published':e.findtext('a:published','',ns),
                                'updated':e.findtext('a:updated','',ns)})
        except Exception:pass
    for p in group:
        count+=1;match=None;tn=norm(p['title'])
        for row in entries:
            exact=norm(row['title'])==tn
            sim=difflib.SequenceMatcher(None,tn,norm(row['title'])).ratio()
            official_names={norm(a.split()[-1]) for a in p.get('authors',[]) if a.split()}
            archive_names={norm(a.split()[-1]) for a in row['authors'] if a.split()}
            if exact or (sim>=.965 and official_names&archive_names):
                match=dict(row,title_match='exact_normalized' if exact else 'near_exact_plus_author',title_similarity=sim);break
        record={'id':p['id'],'title':p['title'],'query_url':url,'match':match,'searched_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
        if not raw:record['search_error']=meta.get('error','unreadable API response')
        if match:
            matched+=1
            try:
                r=requests.get(match['pdf_url'],timeout=(15,70),headers={'User-Agent':AGENT})
                data=r.content
                if r.status_code==200 and data.lstrip().startswith(b'%PDF-'):
                    pages=len(PdfReader(io.BytesIO(data),strict=False).pages)
                    if pages>0:
                        slug=re.sub(r'[^A-Za-z0-9]+','_',p['title']).strip('_')[:105]
                        target=ROOT/'pdfs'/p['venue']/str(p['year'])/(p['id']+'__'+slug+'.pdf')
                        target.parent.mkdir(parents=True,exist_ok=True);tmp=target.with_suffix('.pdf.part');tmp.write_bytes(data);tmp.replace(target)
                        result={'id':p['id'],'title':p['title'],'venue':p['venue'],'year':p['year'],'status':'downloaded',
                            'requested_url':match['pdf_url'],'final_url':r.url,'publisher_pdf_url':p.get('pdf_url',''),
                            'pdf_version':'arxiv_author_version','arxiv_url':match['arxiv_url'],'title_match':match['title_match'],
                            'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'pages':pages,
                            'local_path':str(target.relative_to(ROOT)),'downloaded_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
                        with (ROOT/'checks/download_results.jsonl').open('a') as f:f.write(json.dumps(result,ensure_ascii=False)+'\n')
                        downloaded+=1;record['download_status']='downloaded'
                    else:record['download_status']='empty_pdf'
                else:record['download_status']=f'HTTP {r.status_code} or not a PDF'
            except Exception as exc:record['download_status']=str(exc)
        with matchlog.open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
    print(count,'/',len(todo),'matched',matched,'downloaded',downloaded,flush=True)
print('ARXIV COMPLETE',count,matched,downloaded,flush=True)
