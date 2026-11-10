"""Register confirmed financial papers in the canonical PDF library."""
from common import *
import os
import re

base=ROOT/'checks/finance_expansion'
papers={p['id']:p for p in load_json('sources/resolved_universe.json.gz')}
review=json.loads((ROOT/'checks/finance_review.json').read_text())
main={};retrieved={}
for log,dest in [(ROOT/'checks/download_results.jsonl',main),(base/'review_downloads.jsonl',retrieved)]:
    for line in log.read_text().splitlines():
        try:r=json.loads(line)
        except Exception:continue
        if r.get('status')=='downloaded' and (ROOT/r['local_path']).is_file():dest[r['id']]=r
registered=[]
manifest_path=base/'promoted_pdf_manifest.json'
manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else []
for pid,info in review['included'].items():
    if pid in main:
        if info.get('evidence_local_path'):info['evidence_local_path']=main[pid]['local_path']
        continue
    if pid not in retrieved:continue
    r=retrieved[pid];p=papers[pid];source=ROOT/r['local_path']
    assert source.stat().st_size==r['bytes']
    assert hashlib.sha256(source.read_bytes()).hexdigest()==r['sha256']
    slug=re.sub(r'[^A-Za-z0-9]+','_',p['title']).strip('_')[:105]
    target=ROOT/'pdfs'/p['venue']/str(p['year'])/(pid+'__'+slug+'.pdf')
    target.parent.mkdir(parents=True,exist_ok=True)
    if target.exists():assert hashlib.sha256(target.read_bytes()).hexdigest()==r['sha256']
    else:os.link(source,target)
    record=dict(r,local_path=str(target.relative_to(ROOT)),screening_pdf_path=r['local_path'])
    with (ROOT/'checks/download_results.jsonl').open('a') as f:f.write(json.dumps(record,ensure_ascii=False)+'\n')
    info['evidence_local_path']=record['local_path']
    manifest.append({'id':pid,'screening_path':r['local_path'],'canonical_path':record['local_path'],'sha256':r['sha256']})
    registered.append(pid)
save_json('checks/finance_review.json',review)
save_json('checks/finance_expansion/promoted_pdf_manifest.json',manifest)
print('financial PDFs registered',len(registered),'total registered by audit',len(manifest),flush=True)
