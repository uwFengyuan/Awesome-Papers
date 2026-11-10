"""Apply ID-based financial review decisions, preserving previous evidence."""
from common import *
import re
from collections import Counter
from finance_taxonomy import apply_taxonomy

papers={p['id']:p for p in load_json('sources/resolved_universe.json.gz')}
review=json.loads((ROOT/'checks/finance_review.json').read_text())
all_decisions={}
for name in ['manual_decisions.json','pdf_decisions.json','supplementary_decisions.json','extended_metadata_decisions.json','final_decisions.json']:
    f=ROOT/'checks/finance_expansion'/name
    if f.exists():all_decisions.update(json.loads(f.read_text())['decisions'])
for pid,decision in all_decisions.items():
    p=papers[pid]
    if decision.get('decision','include')!='include':continue
    info=dict(decision)
    info.update(evidence_url=p.get('abstract_source') or p['paper_url'],
                review_basis='Expanded review across all main papers, independent of award or presentation type.')
    review['included'][pid]=info
apply_taxonomy(papers,review)
review['pending']=[p for p in review['pending'] if p['id'] not in review['included']]
review['excluded']=[p for p in review['excluded'] if p['id'] not in review['included']]
review['counts']={'core':sum(x['scope']=='core' for x in review['included'].values()),
                  'application':sum(x['scope']=='application' for x in review['included'].values()),
                  'pending':len(review['pending']),'explicit_false_positives':len(review['excluded'])}
review['expansion_audit']='checks/finance_expansion/'
save_json('checks/finance_review.json',review)
print('finance',len(review['included']),review['counts'])
