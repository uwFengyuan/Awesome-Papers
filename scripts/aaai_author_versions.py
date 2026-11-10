"""Discover author versions by DOI, then independently verify downloaded PDF identity."""
from common import *
import io
from collections import Counter
import pyarrow.parquet as pq
from acquire_selected_pdfs import identity

DEST=ROOT/'checks/scope_revision'
CACHE=pathlib.Path('/tmp/awesome_papers_selected_pdfs')


def main():
    papers={p['id']:p for p in load_json('checks/scope_revision/selected_papers.json.gz')}
    results={p['id']:p for p in load_json('checks/scope_revision/new_pdf_results.json')}
    discovery={}
    for year in sorted({papers[pid]['year'] for pid,r in results.items() if pid in papers and r['status']!='downloaded' and papers[pid]['venue']=='AAAI'}):
        url=f'https://huggingface.co/datasets/ai-conferences/AAAI{year}/resolve/main/data/train-00000-of-00001.parquet'
        data,info=fetch(url,f'aaai-{year}-author-version-discovery',timeout=50,retries=1)
        if not data:continue
        try:rows=pq.read_table(io.BytesIO(data)).to_pylist()
        except Exception as exc:print('Discovery unavailable',year,str(exc)[:90],flush=True);continue
        bydoi={r.get('doi','').lower():r for r in rows}
        bytitle={norm(r.get('title','')):r for r in rows}
        for pid,paper in papers.items():
            if paper['venue']!='AAAI' or paper['year']!=year:continue
            candidate=bydoi.get(paper.get('doi','').lower()) or bytitle.get(norm(paper['title']))
            if candidate and candidate.get('arxiv_id') and norm(candidate['title'])==norm(paper['title']):
                discovery[pid]=dict(arxiv_id=candidate['arxiv_id'],discovery_source=url,
                    doi=paper['doi'],title=paper['title'])
    save_json('checks/scope_revision/author_version_discovery.json',discovery)
    queue=[(pid,meta) for pid,meta in discovery.items() if pid in results and results[pid]['status']!='downloaded']
    print('Author-version PDF queue:',len(queue),flush=True)
    def job(pair):
        pid,meta=pair;url='https://arxiv.org/pdf/'+meta['arxiv_id'];old=results[pid]
        try:
            response=requests.get(url,timeout=(8,30),headers={'User-Agent':AGENT})
            assert response.status_code==200 and response.content.startswith(b'%PDF-'),f'HTTP {response.status_code}'
            path=CACHE/(pid+'.pdf');path.write_bytes(response.content)
            proof=identity(path,papers[pid]);assert proof['identity_verified'],'Title/author identity needs review'
            return dict(id=pid,status='downloaded',source_path=str(path),bytes=len(response.content),
                sha256=hashlib.sha256(response.content).hexdigest(),identity=proof,pdf_version='arxiv_author_version',
                requested_url=url,final_url=response.url,discovery=meta,attempts=old.get('attempts',[]))
        except Exception as exc:
            old.setdefault('attempts',[]).append(dict(url=url,error=str(exc)[:150]));return old
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for index,result in enumerate(pool.map(job,queue),1):
            results[result['id']]=result
            if index%25==0:
                save_json('checks/scope_revision/new_pdf_results.json',list(results.values()))
                print('Author versions checked',index,'/',len(queue),dict(Counter(r['status'] for r in results.values())),flush=True)
    save_json('checks/scope_revision/new_pdf_results.json',list(results.values()))
    print('Author versions complete:',dict(Counter(r['status'] for r in results.values())),flush=True)


if __name__=='__main__':main()
