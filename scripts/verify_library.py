from common import *
import csv,subprocess,re,unicodedata,concurrent.futures

with (ROOT/'catalog.csv').open(encoding='utf-8-sig',newline='') as f:rows=list(csv.DictReader(f))
def title_norm(s):
    s=re.sub(r'\\(?:texttt|text|mathrm|mathbf|mathcal|mathbb|mathsf|operatorname|emph|textsc|mathit|boldsymbol)','',s)
    s=s.replace('\\ell','l').replace('\\infty','infinity')
    return norm(s)
unique={}
for r in rows:
    if r['local_path']:unique.setdefault(r['local_path'],r)

def job(item):
    path,row=item;p=ROOT/path
    out={'id':row['id'],'path':path,'exists':p.is_file(),'title_status':'unverified'}
    if not p.is_file():out['status']='missing_file';return out
    out['bytes']=p.stat().st_size
    if out['bytes']!=int(row['bytes']):out['status']='size_mismatch';return out
    data=p.read_bytes();out['sha256']=hashlib.sha256(data).hexdigest()
    if out['sha256']!=row['sha256']:out['status']='hash_mismatch';return out
    out['status']='file_verified'
    try:
        r=subprocess.run(['pdftotext','-f','1','-l','1',str(p),'-'],capture_output=True,timeout=25)
        text=r.stdout.decode('utf8',errors='replace');pn=title_norm(row['title']);tn=title_norm(text)
        if pn in tn:out['title_status']='exact_normalized'
        else:
            title=re.sub(r'\\[a-zA-Z]+',' ',row['title']);words=set(re.findall('[a-z]{3,}',unicodedata.normalize('NFKD',title).lower()))
            words-={'the','and','for','with','from','via','towards','into','through','under','over','how','are','can'}
            present={w for w in words if w in tn};score=len(present)/max(1,len(words))
            out['title_word_coverage']=round(score,3)
            out['title_status']='word_match' if score>=.8 and len(words)>=3 else 'manual_review'
            if out['title_status']=='manual_review':out['first_page_excerpt']=text[:800]
    except Exception as exc:out['text_extract_error']=str(exc)
    return out

checks=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    for result in pool.map(job,unique.items()):
        checks.append(result)
        if len(checks)%500==0:print('Verified PDF files',len(checks),'/',len(unique),flush=True)
save_json('checks/pdf_integrity_and_title_checks.json',checks)
problems=[r for r in checks if r['status']!='file_verified' or r['title_status']=='manual_review']
save_json('checks/pdf_manual_review.json',problems)
ids=[r['id'] for r in rows]
report={'catalog_rows':len(rows),'unique_ids':len(set(ids)),'unique_local_pdf_files':len(unique),
        'file_integrity_failures':sum(r['status']!='file_verified' for r in checks),
        'title_checks':dict(__import__('collections').Counter(r['title_status'] for r in checks)),
        'finance_rows':sum(bool(r['finance_scope']) for r in rows),
        'track_values':sorted(set(r['track'] for r in rows))}
save_json('checks/validation_summary.json',report)
print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)
