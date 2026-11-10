"""Extract main-body finance evidence from locally available papers, excluding references."""
from common import *
import csv
import re
import subprocess
import argparse

DEST = ROOT/'checks/finance_expansion'
TEXTS = DEST/'pdf_texts'
TEXTS.mkdir(exist_ok=True)
rows = list(csv.DictReader((ROOT/'catalog.csv').open(encoding='utf-8-sig')))
parser=argparse.ArgumentParser()
parser.add_argument('--review-results',action='store_true')
parser.add_argument('--output-prefix')
args=parser.parse_args()
if args.review_results:
    meta={p['id']:p for p in load_json('sources/resolved_universe.json.gz')}
    finance=json.loads((ROOT/'checks/finance_review.json').read_text())['included']
    already={p['id'] for p in json.loads((DEST/'pdf_evidence.json').read_text())}
    rows=[]
    for r in json.loads((DEST/'review_downloads.json').read_text()):
        if r['id'] in already or r.get('status')!='downloaded':continue
        p=meta[r['id']]
        rows.append(dict(r,title=p['title'],venue=p['venue'],year=p['year'],download_status='downloaded',finance_scope=finance.get(r['id'],{}).get('scope','')))

DATASET = re.compile(r'\b(?:FinQA|ConvFinQA|TAT[- ]?QA|MultiHiertt|FinRL|StockNet|FiQA|FinancialPhraseBank|FinanceBench|FinTextQA|FinanceMATH|BizBench|DocFinQA|FinBERT|FICO|LendingClub|Home[- ]Credit|PaySim|BankSim|AMLSim|Elliptic|NASDAQ|NYSE|CSI[- ]?300|CSI[- ]?500|S\s*&\s*P\s*500|SP500|Dow[- ]?Jones|Hang[- ]Seng|German[- ]Credit|credit[- ]card|bank[- ]marketing|banknote|EDGAR|XBRL|EDINET)\b',re.I)
DOMAIN = re.compile(r'\bfinanc(?:e|ial)\b|\bstock[- ](?:market|price|return|data|predict|forecast)|\boption[- ]pric|\bBlack[- ]Scholes\b|\bportfolio[- ](?:optim|alloc|manag|select)|\bloan[- ](?:approv|default|data)|\bcredit[- ](?:scor|risk|data)|\bmoney[- ]launder|\b(?:cryptocurrency|macroeconomic|monetary policy|fiscal policy)\b',re.I)
ADDITIONAL_DATASET=re.compile(r'\b(?:FinRE|ChFinAnn|DuEE[- ]?Fin|Doc2EDAG|Numeracy600K|Financial[- ]Phrase[- ]?Bank|HELOC|Australian[- ]Credit|GiveMeSomeCredit|Allstate|SROIE|Kleister[- ]Charity|FinCausal|FOMC|FinBen|FinTrust|FiNER|FinDVer|FinMME|FinMTEB|FinSearchComp|StockMix|LOB[- ]Bench)\b',re.I)
DOCUMENT_FINANCE=re.compile(r'\b(?:invoices?|receipts?|taxation|accounting|annual reports?|earnings calls?|debt collection|insurance claims?|ESG)\b',re.I)
EXPERIMENT = re.compile(r'\b(?:experiment\w*|evaluat\w*|benchmark\w*|dataset\w*|data set\w*|train\w*|test\w*|empiric\w*|case study|simulat\w*|performance|accuracy|Table\s+\d|AUC|F1)\b|\d\.\d',re.I)

def job(row):
    cache = finance_text_cache(row['id'])
    try:
        if cache.exists():text=gzip.decompress(cache.read_bytes()).decode()
        else:
            result=subprocess.run(['pdftotext','-layout',str(ROOT/row['local_path']),'-'],capture_output=True,text=True,timeout=60)
            if result.returncode: return {'id':row['id'],'error':'pdftotext failed'}
            text=result.stdout
            cache.parent.mkdir(parents=True, exist_ok=True)
            cache.write_bytes(gzip.compress(text.encode()))
        # References end at an appendix heading where one exists. Otherwise truncate.
        refs=[]
        cursor=0
        # Use line scans: PDF layouts can contain very long whitespace runs.
        # A regex with greedy whitespace alternatives can become quadratic there.
        for line in text.splitlines(keepends=True):
            stripped=line.lstrip(' \t')
            for heading in ['References','Bibliography']:
                position=line.find(heading)
                if position>=0 and (stripped.startswith(heading) or (position>=3 and line[position-3:position]=='   ')):
                    refs.append((cursor+position,cursor+position+len(heading)))
            cursor+=len(line)
        body=text
        if refs:
            start,end=refs[0]
            appendix=re.search(r'(?mi)^[ \t]*(?:Appendix|[A-Z][ \t]+(?:Additional|Proof|Experiment|Implementation|Data|Details))\b',text[end:])
            body=text[:start]+('\n'+text[end+appendix.start():] if appendix else '')
        hits=[]
        for rx,kind in [(DATASET,'named_financial_dataset'),(ADDITIONAL_DATASET,'named_financial_dataset'),(DOMAIN,'financial_domain'),(DOCUMENT_FINANCE,'financial_document_or_task')]:
            for match in rx.finditer(body):
                lo=max(0,match.start()-220);hi=min(len(body),match.end()+350)
                context=re.sub(r'\s+',' ',body[lo:hi]).strip()
                if match.group().lower()=='edgar' and match.group()!='EDGAR':continue
                if match.group().lower()=='elliptic' and not re.search(r'bitcoin|launder|crypto|transaction|fraud|dataset',context,re.I):continue
                if kind=='financial_domain' and re.search(r'financial (?:support|grant|assistance|interest|times)|financial.*(?:cost|burden).*train|(?:center|centre|institute|department).*financial',context,re.I):continue
                experimental=bool(EXPERIMENT.search(context))
                hits.append({'kind':kind,'match':match.group(),'offset':match.start(),
                             'experimental_context':experimental,'excerpt':context})
        hits.sort(key=lambda h:(h['kind']!='named_financial_dataset',not h['experimental_context'],h['offset']<4000,h['offset']))
        unique=[]
        for h in hits:
            if not any(abs(h['offset']-x['offset'])<180 for x in unique):unique.append(h)
        return {'id':row['id'],'title':row['title'],'venue':row['venue'],'year':row['year'],
                'previous_finance':bool(row['finance_scope']),'local_path':row['local_path'],
                'text_characters':len(text),'main_body_characters':len(body),
                'evidence':unique[:18],'total_marker_hits':len(hits)}
    except Exception as exc:return {'id':row['id'],'error':str(exc)}

selected=[r for r in rows if r['download_status']=='downloaded']
print('PDF text scan queue',len(selected),flush=True)
out=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
    futures={pool.submit(job,row):row['id'] for row in selected}
    for i,future in enumerate(concurrent.futures.as_completed(futures),1):
        result=future.result()
        out.append(result)
        if i%100==0:print('PDF text scans',i,'/',len(selected),flush=True)
prefix=args.output_prefix or ('review_pdf_evidence' if args.review_results else 'pdf_evidence')
save_json(f'checks/finance_expansion/{prefix}.json',out)
save_json(f'checks/finance_expansion/{prefix}_candidates.json',[
    x for x in out if x.get('evidence') and not x.get('previous_finance')])
print('COMPLETE',len(out),'new finance evidence candidates',sum(bool(x.get('evidence')) and not x.get('previous_finance') for x in out),flush=True)
