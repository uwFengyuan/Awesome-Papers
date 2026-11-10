"""Decisions for newly retrieved full texts with financial datasets or tasks."""
from common import *
import re

base=ROOT/'checks/finance_expansion'
queue=json.loads((base/'new_named_pdf_queue.json').read_text())
excluded={8,20,21,24,39,41,48,53,68,70,94}
accepted=set(range(len(queue)))-excluded
overrides={9:r'paired language with time',14:r'Financial Secure',29:r'observed in financial data',43:r'cover the academic, financial',67:r'German Credit \(Dua & Graff, 2019\)',81:r'financial tasks'}
decisions={}
for i in sorted(accepted):
    x=queue[i];excerpt=x['review_evidence'][0]['excerpt']
    if i in overrides:
        text=gzip.decompress(finance_text_cache(x['id']).read_bytes()).decode()
        compact=re.sub(r'\s+',' ',text)
        match=re.search(overrides[i],compact,re.I)
        assert match,(i,overrides[i])
        excerpt=compact[max(0,match.start()-150):match.end()+480]
    decisions[x['id']]={'scope':'core' if i in {13,25,46} else 'application',
        'evidence_type':'fulltext_financial_case_or_formal_model' if i in {29,57,62} else 'fulltext_financial_data_or_task',
        'evidence_excerpt':excerpt,'evidence_local_path':x['local_path'],
        'relevance_zh':'正文包含明确金融数据、金融任务或金融案例；金融应用可属于通用方法的一个实验。',
        'review_basis':'Human review of the downloaded full text; references and financial keywords alone do not establish inclusion.',
        'frozen_queue':'new_named_pdf_queue.json','frozen_queue_index':i}
save_json('checks/finance_expansion/supplementary_decisions.json',{
    'decisions':decisions,'new_named_queue_sha256':hashlib.sha256((base/'new_named_pdf_queue.json').read_bytes()).hexdigest(),
    'new_named_excluded_indices':sorted(excluded)})
print('newly retrieved full texts confirmed',len(decisions))
