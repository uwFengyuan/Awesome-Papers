"""Reviewed aliases refer to actual financial benchmarks, not financial background."""
from common import *

base=ROOT/'checks/finance_expansion'
queue=json.loads((base/'dataset_alias_queue.json').read_text())
out=base/'supplementary_decisions.json';result=json.loads(out.read_text())
for i,x in enumerate(queue):
    if i in {0,46}:continue
    evidence=x['evidence'][0]
    is_m4=evidence['match'].lower().startswith('m4')
    result['decisions'][x['id']]={
        'scope':'application','evidence_type':'benchmark_with_financial_subset' if is_m4 else 'fulltext_financial_benchmark',
        'evidence_excerpt':evidence['excerpt'],'evidence_local_path':x['local_path'],
        'benchmark_name':evidence['match'],
        'benchmark_taxonomy_source':'https://raw.githubusercontent.com/Mcompetitions/M4-methods/master/Dataset/M4-info.csv' if is_m4 else '',
        'relevance_zh':'实验使用包含金融序列的 M4 非小时子集；金融子集由官方元数据核验。' if is_m4 else '实验使用汇率、宏观金融、信用评估或财务文档等金融相关基准。',
        'review_basis':'Human review of the reported dataset/experiment. M4 hourly-only was not treated as financial.',
        'frozen_queue':'dataset_alias_queue.json','frozen_queue_index':i}
result['dataset_alias_queue_sha256']=hashlib.sha256((base/'dataset_alias_queue.json').read_bytes()).hexdigest()
result['dataset_alias_excluded_indices']=[0,46]
save_json('checks/finance_expansion/supplementary_decisions.json',result)
print('financial dataset aliases confirmed',len(queue)-2)
