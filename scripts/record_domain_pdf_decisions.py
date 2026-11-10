"""Record reviewed finance domains, financial models and financial case studies."""
from common import *
import re

base=ROOT/'checks/finance_expansion'
queue=json.loads((base/'domain_pdf_queue.json').read_text())
accepted={0,8,9,14,16,19,20,24,25,26,31,32,34,37,47,48,53,58,59,60,71,73,74,80,84,86,90,95,
100,101,108,110,115,116,120,121,122,123,124,125,130,136,138,139,141,142,143,145,146,151,152,154,155,156,157,159,160,161,165,171,172,174,
181,184,187,189,190,193,197,199,202,204,210,214,215,216,217,219,220,222,225,226,230,232,234,238,240,244,249,253,258,259,260,262,276,279,281,287,288,296,299,300,304,305,306,
307,308,313,316,319,321,327,328,330,331,340,342,346,350,353,354,356,357,359,363,365,370,374,375,378,381,382,386,394,395,400}
overrides={
 71:r'Quantitative Finance',
 171:r'SROIE|receipt',
 189:r'\(1\) Financial Reports',
 374:r'purely financial one',
}
case_indices={116,121,125,156,214,215,220,230,253,258,260,288,296,306,313,346,354,357,370,386,394}
out=base/'pdf_decisions.json'
result=json.loads(out.read_text())
for i in sorted(accepted):
    x=queue[i];excerpt=x['review_evidence'][0]['excerpt']
    if i in overrides:
        text=gzip.decompress(finance_text_cache(x['id']).read_bytes()).decode()
        compact=re.sub(r'\s+',' ',text)
        match=re.search(overrides[i],compact,re.I)
        assert match,(i,overrides[i])
        excerpt=compact[max(0,match.start()-130):match.end()+450]
    result['decisions'][x['id']]={
        'scope':'core' if i in {143,202} else 'application',
        'evidence_type':'fulltext_financial_case_or_formal_model' if i in case_indices else 'fulltext_financial_domain_data_or_experiment',
        'evidence_excerpt':excerpt,'evidence_local_path':x['local_path'],
        'review_basis':'Human review of financial domain/data/model/case in the local paper. Citations, funding statements and incidental lexical examples were excluded.',
        'relevance_zh':'正文包含金融场景的案例或形式化分析。' if i in case_indices else '正文包含金融领域数据、模型、实验或分领域评测。',
        'frozen_queue':'domain_pdf_queue.json','frozen_queue_index':i}
result['domain_queue_sha256']=hashlib.sha256((base/'domain_pdf_queue.json').read_bytes()).hexdigest()
result['domain_excluded_indices']=sorted(set(range(len(queue)))-accepted)
write=ROOT/'checks/finance_expansion/pdf_decisions.json'
save_json('checks/finance_expansion/pdf_decisions.json',result)
print('domain additions',len(accepted),'fulltext decisions total',len(result['decisions']))
