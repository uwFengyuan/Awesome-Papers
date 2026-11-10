"""Verify long main-text length without counting references or appendices as content."""
from common import *
import re
import subprocess
from paper_attributes import paper_length
from prepare_curated_scope import length_evidence

DEST=ROOT/'checks/scope_revision'
CACHE=pathlib.Path('/tmp/awesome_papers_scope_pdfs')
SHORT_LIMITS='https://2025.emnlp.org/calls/main_conference_papers/'


def inspect(p):
    pid=p['id'];result={'id':pid}
    registered=p.get('download') or {}
    path=ROOT/registered['local_path'] if registered.get('local_path') else None
    if not path or not path.is_file():
        if p.get('track')!='findings':return result
        path=CACHE/(pid+'.pdf')
        reference_cache=pathlib.Path('/tmp/ai4finance_findings_review')/(pid+'.pdf')
        if not path.exists() and reference_cache.exists():path=reference_cache
        if not path.exists():
            try:
                response=requests.get(p['pdf_url'],timeout=(10,35),headers={'User-Agent':AGENT})
                if response.status_code!=200 or not response.content.startswith(b'%PDF-'):
                    return dict(result,error=f'PDF unavailable: HTTP {response.status_code}')
                path.write_bytes(response.content)
            except Exception as exc:return dict(result,error=str(exc)[:180])
    try:
        text=subprocess.check_output(['pdftotext',str(path),'-'],stderr=subprocess.DEVNULL,timeout=35).decode(errors='replace')
        pages=text.split('\f')
        if p.get('track')=='findings' and norm(p['title']) not in norm(pages[0]):
            return dict(result,error='First-page title needs review')
        heading=None
        for index,page in enumerate(pages):
            # Count substantive content before any excluded back matter.
            # Table/figure labels can cause conservative false negatives;
            # reviewed per-paper exceptions live in finance_reconciliation.
            match=re.search(r'(?im)^\s*(?:\d+[. ]+)?(?:References|Bibliography|Limitations|Ethical Considerations|Ethics Statement|Acknowledg(?:e)?ments|Broader Impact|Appendix|Appendices)\s*$',page)
            if match:
                heading=(index,match.start());break
        if heading:
            index,position=heading
            body='\f'.join(pages[:index])+pages[index][:position]
            if re.search(r'(?m)^\s*(?:Appendix(?:\s+[A-Z])?|[A-Z]\.\s+Appendix|[A-Z]\s+(?:Additional|Supplementary|Experimental Details))\s*$',body):
                return dict(result,error='Appendix precedes references; main-text length requires review')
            # Short camera-ready content is at most five pages. Substantive
            # sixth-page content before back matter establishes a full paper;
            # a five-page body stays unverified, even if the PDF has 30 pages.
            content=max((pages[i] if i<index else pages[i][:position] for i in range(5,index+1)),
                key=lambda s:len(re.findall(r'\b[A-Za-z]{3,}\b',s)),default='')
            if len(re.findall(r'\b[A-Za-z]{3,}\b',content))>=160:
                result.update(paper_length='long',
                    evidence=f'Publisher PDF has substantive content after page five before back matter on page {index+1}. '+p['paper_url'],
                    inspection_version=2,backmatter_start_page=index+1,
                    pdf_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),pdf_cache_path=str(path),
                    main_text_limit_reference=SHORT_LIMITS)
        return result
    except Exception as exc:return dict(result,error=str(exc)[:180])


def main():
    CACHE.mkdir(exist_ok=True)
    candidates={p['id']:p for p in map(json.loads,(ROOT/'catalog.jsonl').read_text().splitlines())}
    candidates.update({p['id']:p for p in load_json('checks/scope_revision/findings_candidates.json.gz') if p.get('finance')})
    labels=length_evidence()
    queue=[p for p in candidates.values() if paper_length(p)[0]=='unverified' and
           (p['venue'],p['year'],norm(p['title'])) not in labels]
    previous=load_json('checks/scope_revision/pdf_length_evidence.json') if (DEST/'pdf_length_evidence.json').exists() else {}
    queue=[p for p in queue if p['id'] not in previous]
    logs=[]
    print('Paper-length PDF queue:',len(queue),flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as pool:
        for index,result in enumerate(pool.map(inspect,queue),1):
            logs.append(result)
            if result.get('paper_length')=='long':previous[result['id']]=result
            if index%100==0:
                save_json('checks/scope_revision/pdf_length_evidence.json',previous)
                print('Length checked',index,'/',len(queue),'verified long:',len(previous),flush=True)
    save_json('checks/scope_revision/pdf_length_evidence.json',previous)
    save_json('checks/scope_revision/pdf_length_attempts.json',logs)
    print('Verified long-paper PDFs:',len(previous),flush=True)


if __name__=='__main__':main()
