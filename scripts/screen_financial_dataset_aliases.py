"""Find financial benchmarks hidden under dataset aliases, without inferring from background."""
from common import *
import re
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--output-file',default='dataset_alias_queue.json')
args=parser.parse_args()

base=ROOT/'checks/finance_expansion'
papers={p['id']:p for p in load_json('sources/resolved_universe.json.gz')}
finance=json.loads((ROOT/'checks/finance_review.json').read_text())['included']
locations={}
for log in [ROOT/'checks/download_results.jsonl',base/'review_downloads.jsonl']:
    for line in log.read_text().splitlines():
        try:r=json.loads(line)
        except Exception:continue
        if r.get('status')=='downloaded' and (ROOT/r['local_path']).is_file():locations[r['id']]=r['local_path']

alias=re.compile(r'\b(?:credit[-_ ]g|credit[-_]a|creditcard|German[- ]Credit|Australian[- ]Credit|bank[-_ ]marketing|bank32nh|HELOC|Home[- ]Equity[- ]Line[- ]of[- ]Credit|FRED[-_]MD|FRED[-_]QD|SROIE|CORD|exchange[-_ ]rates?|M4[-_ ](?:Yearly|Quarterly|Monthly|Weekly|Daily))\b',re.I)
ts=re.compile(r'time.?series|forecast|temporal|SDE|stochastic differential',re.I)
experimental=re.compile(r'\b(?:dataset|train|test|experiment|evaluation|benchmark|we use|we evaluate|we test|we consider)\b',re.I)

def body_only(text):
    cursor=0;cut=None
    for line in text.splitlines(keepends=True):
        for heading in ['References','Bibliography']:
            pos=line.find(heading)
            if pos>=0 and (line.lstrip().startswith(heading) or (pos>=3 and line[pos-3:pos]=='   ')):
                cut=cursor+pos;break
        if cut is not None:break
        cursor+=len(line)
    if cut is None:return text
    appendix=re.search(r'(?mi)^[ \t]*(?:Appendix|[A-Z][ \t]+(?:Additional|Proof|Experiment|Implementation|Data|Details))\b',text[cut+10:])
    return text[:cut]+('\n'+text[cut+10+appendix.start():] if appendix else '')

out=[]
for cache in sorted((base/'pdf_texts').rglob('*.txt.gz')):
    pid=cache.name[:-7]
    if pid in finance or pid not in papers or pid not in locations:continue
    p=papers[pid];text=gzip.decompress(cache.read_bytes()).decode();body=body_only(text)
    markers=[]
    for match in alias.finditer(body):
        value=match.group()
        if value.lower()=='cord' and not re.search(r'\breceipts?\b',body,re.I):continue
        if value.lower().startswith(('exchange','m4')) and not ts.search(p['title']):continue
        lo=max(0,match.start()-200);hi=min(len(body),match.end()+420)
        context=re.sub(r'\s+',' ',body[lo:hi]).strip()
        numeric=len(re.findall(r'\d+\.\d+',context))>=2
        if match.start()>2500 and (numeric or experimental.search(context)):
            markers.append({'match':value,'offset':match.start(),'numeric_results':numeric,'excerpt':context})
    # 'Exchange' is the short name of the currency benchmark in forecasting tables.
    if ts.search(p['title']):
        for match in re.finditer(r'\bExchange\b',body):
            context=re.sub(r'\s+',' ',body[max(0,match.start()-150):match.end()+420]).strip()
            if len(re.findall(r'\d+\.\d+',context))>=3:
                markers.append({'match':'Exchange benchmark (currency series)','offset':match.start(),'numeric_results':True,'excerpt':context})
    if markers:
        markers.sort(key=lambda m:(not m['numeric_results'],m['offset']))
        out.append({'id':pid,'title':p['title'],'venue':p['venue'],'year':p['year'],
                    'local_path':locations[pid],'evidence':markers[:12]})
save_json('checks/finance_expansion/'+args.output_file,out)
print('financial dataset alias candidates',len(out),flush=True)
