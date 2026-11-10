"""Acquire only newly selected PDFs absent from the repository and local finance caches."""
from common import *
import re
import subprocess
from collections import Counter
from bs4 import BeautifulSoup

DEST=ROOT/'checks/scope_revision'
CACHE=pathlib.Path('/tmp/awesome_papers_selected_pdfs')
REF=pathlib.Path('/home/qi/aiagent/Awesome-AI4Finance-Papers')


def identity(path,paper):
    text=subprocess.check_output(['pdftotext','-f','1','-l','2',str(path),'-'],stderr=subprocess.DEVNULL,timeout=20).decode(errors='replace')
    content=norm(text);title=norm(paper['title'])
    words=set(re.findall('[a-z]{3,}',paper['title'].lower()))
    score=sum(norm(w) in content for w in words)/max(1,len(words))
    authors=[a for a in paper['authors'] if norm(a) in content]
    return dict(title_exact=title in content,title_word_coverage=score,matched_authors=authors,
                identity_verified=(title in content or (len(words)>=6 and score>=.95 and bool(authors))))


def main():
    CACHE.mkdir(exist_ok=True)
    selected=load_json('checks/scope_revision/selected_papers.json.gz')
    baseline=load_json('checks/scope_revision/baseline.json')
    baseline_ids={p['id'] for p in baseline['papers']}
    local_reuse=load_json('checks/scope_revision/reference_pdf_reuse.json')
    previous=load_json('checks/scope_revision/new_pdf_results.json') if (DEST/'new_pdf_results.json').exists() else []
    old={p['id']:p for p in previous}
    queue=[p for p in selected if p['id'] not in baseline_ids and p['id'] not in local_reuse and p['id'] not in old]
    discovery_path=REF/'main/checks/aaai_expansion/fulltext_discovery.json'
    if not discovery_path.exists():discovery_path=REF/'checks/aaai_expansion/fulltext_discovery.json'
    discovery={p['id']:p for p in json.loads(discovery_path.read_text())} if discovery_path.exists() else {}
    def job(paper):
        pid=paper['id'];target=CACHE/(pid+'.pdf');attempts=[]
        for cached in [pathlib.Path('/tmp/ai4finance_aaai_pdf_review')/(pid+'.pdf'),pathlib.Path('/tmp/ai4finance_findings_review')/(pid+'.pdf')]:
            if cached.exists():
                proof=identity(cached,paper)
                if proof['identity_verified']:
                    source=cached.with_suffix('.source.json')
                    info=json.loads(source.read_text()) if source.exists() else {}
                    return dict(id=pid,status='downloaded',source_path=str(cached),bytes=cached.stat().st_size,
                        sha256=hashlib.sha256(cached.read_bytes()).hexdigest(),identity=proof,
                        pdf_version=info.get('version','publisher_version'),reused_local_cache=True)
        urls=[(paper.get('pdf_url',''),'publisher_version')]
        if discovery.get(pid,{}).get('arxiv_id'):urls.append(('https://arxiv.org/pdf/'+discovery[pid]['arxiv_id'],'arxiv_author_version'))
        for url,version in urls:
            if not url:continue
            try:
                response=requests.get(url,timeout=(8,15),headers={'User-Agent':AGENT})
                payload=response.content
                if response.status_code!=200 or not payload.startswith(b'%PDF-'):
                    attempts.append(dict(url=url,http_status=response.status_code));continue
                target.write_bytes(payload)
                proof=identity(target,paper)
                if not proof['identity_verified']:
                    attempts.append(dict(url=url,error='PDF identity requires review',identity=proof));continue
                info=subprocess.check_output(['pdfinfo',str(target)],stderr=subprocess.DEVNULL,timeout=15).decode(errors='replace')
                pages=int(re.search(r'(?m)^Pages:\s+(\d+)',info)[1])
                return dict(id=pid,status='downloaded',source_path=str(target),bytes=len(payload),pages=pages,
                    sha256=hashlib.sha256(payload).hexdigest(),identity=proof,pdf_version=version,
                    requested_url=url,final_url=response.url,attempts=attempts)
            except Exception as exc:attempts.append(dict(url=url,error=str(exc)[:150]))
        return dict(id=pid,status='not_available_locally',attempts=attempts)
    print('New PDF queue (existing finance PDFs excluded):',len(queue),flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for index,result in enumerate(pool.map(job,queue),1):
            old[result['id']]=result
            if index%25==0:
                save_json('checks/scope_revision/new_pdf_results.json',list(old.values()))
                print('PDF acquisition',index,'/',len(queue),dict(Counter(r['status'] for r in old.values())),flush=True)
    save_json('checks/scope_revision/new_pdf_results.json',list(old.values()))
    print('New PDF acquisition complete:',dict(Counter(r['status'] for r in old.values())),flush=True)


if __name__=='__main__':main()
