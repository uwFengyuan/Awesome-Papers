"""Additional reviewed financial tasks and cases found in newly retrieved papers."""
from common import *
import re

base=ROOT/'checks/finance_expansion'
queue=json.loads((base/'new_domain_pdf_queue.json').read_text())
accepted={2,4,6,10,11,15,17,19,20,29,32,33,36,40,45,50,51,52,60,62,64,66,67,74,75,81,83,87,88,89,92,93,96,98,100,101,106,107,110,113,115,116,121,126,132,141,144,152,154,165,170,173,174,181,187,188,189,192,194,195,200,205,206,210,211,213,215,219,220,226,229,235,238,243,252,253,257,258,259,261,262}
overrides={192:r'[Ss]tocks? (?:data|dataset)|[Ss]tock data',6:r'financial QA'}
out=base/'supplementary_decisions.json';result=json.loads(out.read_text())
for i in sorted(accepted):
    x=queue[i];excerpt=x['review_evidence'][0]['excerpt']
    if i in overrides:
        text=gzip.decompress(finance_text_cache(x['id']).read_bytes()).decode()
        compact=re.sub(r'\s+',' ',text);match=re.search(overrides[i],compact)
        assert match,(i,overrides[i])
        excerpt=compact[max(0,match.start()-100):match.end()+500]
    theory=i in {106,187,211,213,226,253}
    survey=i in {2,29}
    result['decisions'][x['id']]={
        'scope':'core' if i in {17,33,64,67} else 'application',
        'evidence_type':'survey_of_financial_tasks' if survey else 'fulltext_financial_case_or_formal_model' if theory else 'fulltext_financial_data_or_task',
        'evidence_excerpt':excerpt,'evidence_local_path':x['local_path'],
        'relevance_zh':'正文综述金融领域任务和方法。' if survey else '正文包含金融场景的案例或形式化分析。' if theory else '正文包含金融数据、金融任务或金融领域评测。',
        'review_basis':'Human review of local full text; finance in funding, references alone, and generic potential uses excluded.',
        'frozen_queue':'new_domain_pdf_queue.json','frozen_queue_index':i}
result['new_domain_queue_sha256']=hashlib.sha256((base/'new_domain_pdf_queue.json').read_bytes()).hexdigest()
result['new_domain_excluded_indices']=sorted(set(range(len(queue)))-accepted)
save_json('checks/finance_expansion/supplementary_decisions.json',result)
print('new domain additions',len(accepted))
