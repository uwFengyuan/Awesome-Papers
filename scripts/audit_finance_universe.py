"""High recall rescreen of every main-paper title/abstract, independent of presentation."""
from common import *
import re
import shutil
from collections import Counter

AUDIT = ROOT / 'checks/finance_expansion'
AUDIT.mkdir(exist_ok=True)
for name in ['finance_review.json', 'summary.json', 'validation_summary.json']:
    target = AUDIT / ('previous_' + name)
    if not target.exists():
        shutil.copy2(ROOT / 'checks' / name, target)

patterns = {
    'finance': r'\bfinanc(?:e|es|ial|ially|ing)\b|\bfintech\b|\beconometric\w*\b',
    'markets': r'\bstock(?:s|[- ]market|[- ]price)?\b|\bequit(?:y|ies)\b|\basset[- ](?:pric|alloc|manag)|\bcapital markets?\b|\bsecurit(?:y|ies)[- ](?:market|trad|pric)|\bcommodit(?:y|ies)\b|\bforex\b|\bforeign exchange\b',
    'investing': r'\bportfolio\w*\b|\binvest(?:ing|ment|ments|or|ors)\b|\bhedg(?:e|ing)\b|\barbitrage\b|\bSharpe\b|\bBlack[- ]Scholes\b|\boption[- ]pric|\bderivative[- ]pric|\bmarket[- ](?:making|impact|microstructure)\b|\border[- ]books?\b',
    'banking': r'\bbank(?:ing|s)?\b|\bloan(?:s|word)?\b|\blend(?:ing|er|ers)\b|\bcredit\b(?![- ]assignment)|\bdebt\b|\bmortgage\w*\b|\binsur(?:ance|er|ers)\b|\breinsur\w*\b|\bactuari\w*\b|\bbankrupt\w*\b|\bdefault[- ](?:risk|predict)|\bdelinquen\w*\b',
    'transactions': r'\bfraud\w*\b|\banti[- ]money\b|\bmoney[- ]launder\w*\b|\bpayment\w*\b|\btransaction\w*\b|\bBitcoin\b|\bcrypto(?:currency|currencies)?\b|\bblockchain\b|\bdecentralized finance\b',
    'economics': r'\bmacro[- ]?econom\w*\b|\bmonetary\b|\bfiscal\b|\binflation\b|\binterest[- ]rates?\b|\bexchange[- ]rates?\b|\bGDP\b|\bnowcast\w*\b|\btax(?:ation|es)?\b|\baccounting\b|\bearnings\b|\bbond[- ](?:market|pric|yield)|\byield[- ]curve\b',
    'datasets': r'\b(?:FinQA|ConvFinQA|TAT[- ]QA|MultiHiertt|FinRL|StockNet|FinBERT|FinanceBench|FinancialPhraseBank|financial[- ]phrasebank|FiQA|FOMC|FinGPT|FinTextQA|FinanceMATH|BizBench|DocFinQA|FICO|LendingClub|Home[- ]Credit|IEEE[- ]CIS|Elliptic|PaySim|BankSim|AMLSim|credit[- ]?card|NASDAQ|NYSE|CSI[- ]?300|CSI[- ]?500|S&P[- ]?500|SP500|Dow[- ]?Jones|Dow[- ]?30|Hang[- ]Seng|XBRL|EDGAR|EDINET)\b',
    'financial_documents': r'\binvoices?\b|\breceipts?\b|\bannual[- ]reports?\b|\bearnings[- ]calls?\b|\baccountan(?:cy|t|ts)\b|\bESG\b|\bgreenwash\w*\b|\bsustainable[- ]invest\w*\b',
    'financial_names': r'\bFin[A-Z][A-Za-z0-9-]+\b',
}
compiled = {k: re.compile(v, 0 if k=='financial_names' else re.I) for k, v in patterns.items()}
old = json.loads((ROOT / 'checks/finance_candidates.json').read_text())
old_ids = {x['id'] for x in old}
review = json.loads((ROOT / 'checks/finance_review.json').read_text())
papers = load_json('sources/resolved_universe.json.gz')

# The full official Downloads export supplies missing abstracts even where the event
# abstract feed is incomplete. Match only papers already verified as main.
export = json.loads(gzip.decompress((RAW / 'neurips-2026-download-json.gz').read_bytes()))
by_title = {norm(x['name']): x for x in export}
patched = []
for p in papers:
    if p['venue'] == 'NeurIPS' and p['year'] == 2026 and not p.get('abstract'):
        x = by_title.get(norm(p['title']))
        if x and x.get('abstract'):
            p['abstract'] = x['abstract']
            p['abstract_source'] = 'https://neurips.cc/Downloads/2026'
            p['metadata_sources'] = list(dict.fromkeys(p['metadata_sources'] + [p['abstract_source']]))
            patched.append(p['id'])
save_json('sources/resolved_universe.json.gz', papers)

out = []
for p in papers:
    title, abstract = p['title'], p.get('abstract', '')
    hits = {k: sorted(set(rx.findall(title + '\n' + abstract))) for k, rx in compiled.items() if rx.search(title + '\n' + abstract)}
    if not hits and p['id'] not in old_ids:
        continue
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+|\n+', abstract)
                 if any(rx.search(s) for rx in compiled.values())]
    out.append({
        'id': p['id'], 'venue': p['venue'], 'year': p['year'], 'title': title,
        'abstract': abstract, 'paper_url': p['paper_url'], 'pdf_url': p.get('pdf_url', ''),
        'hits': hits, 'finance_sentences': sentences, 'previous_candidate': p['id'] in old_ids,
        'previous_included': p['id'] in review['included'],
    })
save_json('checks/finance_expansion/candidates.json', out)
save_json('checks/finance_expansion/screening_summary.json', {
    'universe_rows': len(papers), 'abstracts_filled_from_official_export': len(patched),
    'abstracts_missing': sum(not p.get('abstract') for p in papers),
    'candidate_rows': len(out), 'previous_included': len(review['included']),
    'additional_candidates': sum(not p['previous_candidate'] for p in out),
    'patterns': patterns,
    'candidate_counts': dict(Counter(f"{p['venue']} {p['year']}" for p in out)),
})
print('screened', len(papers), 'candidates', len(out), 'new', sum(not p['previous_candidate'] for p in out), 'abstracts filled', len(patched))
