"""Human-reviewed full-text evidence: reject citations and lexical lookalikes."""
from common import *
import re

base=ROOT/'checks/finance_expansion'
queue=json.loads((base/'named_dataset_pdf_queue.json').read_text())
accepted={1,2,3,4,5,6,7,8,9,10,11,16,17,18,19,20,21,22,24,25,26,28,29,30,34,36,37,38,39,40,41,42,43,44,45,46,47,48,50,51,52,53,54,55,56,57,58,59,60,62,63,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,91,93,94,95,96,100,101}
overrides={
 50:r'additional experiment.{0,160}finance domain',
 54:r'we defined five domains',
 56:r'document domains.{0,100}finance',
 95:r'HELOC 5564',
}
decisions={}
for i in sorted(accepted):
    x=queue[i];e=x['review_evidence'][0]
    if i in overrides:
        text=gzip.decompress(finance_text_cache(x['id']).read_bytes()).decode()
        compact=re.sub(r'\s+',' ',text)
        match=re.search(overrides[i],compact,re.I)
        assert match,(i,overrides[i])
        e={'excerpt':compact[max(0,match.start()-120):match.end()+420],'kind':'manually_verified_financial_experiment'}
    decisions[x['id']]={'scope':'core' if i==41 else 'application','evidence_type':'fulltext_financial_data_model_or_task',
        'evidence_excerpt':e['excerpt'],'evidence_local_path':x['local_path'],
        'review_basis':'Human review of named financial dataset/model/task in local full text; citation-only matches rejected.',
        'relevance_zh':'正文包含金融领域的数据、模型、任务或独立金融评测。',
        'frozen_queue':'named_dataset_pdf_queue.json','frozen_queue_index':i}
save_json('checks/finance_expansion/pdf_decisions.json',{
    'decisions':decisions,'queue_sha256':hashlib.sha256((base/'named_dataset_pdf_queue.json').read_bytes()).hexdigest(),
    'excluded_indices':sorted(set(range(len(queue)))-accepted),
    'exclusion_note':'Excluded entries were citation-only, Finnish-language FinBERT, incidental lexical examples, or lacked a financial task.'})
print('full-text confirmed additions',len(decisions))
