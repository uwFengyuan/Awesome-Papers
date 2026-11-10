"""Materialize reviewed decisions against frozen queues; IDs are the join keys."""
from common import *
import re

base=ROOT/'checks/finance_expansion'
queue=json.loads((base/'focused_queue.json').read_text())
newmain=json.loads((base/'new_main_candidate_queue.json').read_text())
papers={p['id']:p for p in load_json('sources/resolved_universe.json.gz')}
core={19,39,46,247,265,585,598,635,643,701}
applications={0,7,8,9,10,13,15,20,23,34,37,38,42,45,58,66,71,75,88,90,92,108,110,125,
129,131,132,134,135,142,143,144,145,149,150,153,154,157,160,166,169,172,174,176,180,186,200,205,208,
214,216,242,248,250,259,276,279,282,288,304,314,316,317,318,321,324,332,342,343,349,356,358,362,366,
371,377,380,389,399,402,403,406,412,413,418,420,423,425,431,436,438,440,442,
451,453,457,458,461,470,472,477,485,494,499,507,513,550,555,556,561,563,565,572,594,
613,618,621,622,634,644,662,672,685,709,716,718,719,720}
theory={129,131,132,134,135,144,153,154,160,169,180,214,216,250,314,316,343,418,420,423,431,438,440,442,451,458,494,499,507,561,644,718,719,720}
decisions={}
for i in sorted(core|applications):
    p=queue[i]
    decisions[p['id']]={
        'scope':'core' if i in core else 'application',
        'evidence_type':'financial_method_or_formal_case' if i in theory else 'title_abstract_financial_task_or_data',
        'evidence_excerpt':' / '.join(p['evidence_sentences']) or p['abstract'],
        'relevance_zh':('研究金融业务、金融市场或金融系统中的具体问题。' if i in core else
                        '研究金融风险度量、金融决策或信贷场景的建模与理论方法。' if i in theory else
                        '包含明确的金融任务、金融领域数据或金融案例验证。'),
        'frozen_queue':'focused_queue.json','frozen_queue_index':i,
    }
for i in [120,121,126,149,150,151,154,156,157,160,161,172]:
    p=newmain[i]
    decisions[p['id']]={
        'scope':'core' if i in [120,121,151,154,172] else 'application',
        'evidence_type':'title_abstract_financial_task_or_data',
        'evidence_excerpt':' / '.join(p['finance_sentences']) or p['abstract'],
        'relevance_zh':'以金融市场为研究对象，或包含明确的金融领域数据和应用评测。',
        'frozen_queue':'new_main_candidate_queue.json','frozen_queue_index':i,
    }
direct={
    '2025.acl-long.27':('application','包含税务法规推理任务的多领域规则推理评测。'),
    '2026.acl-long.1642':('core','研究区块链交易脚本生成与执行验证。'),
    'icml-2023-24426':('application','研究模型风险管理中的单调性约束；需结合正文保留具体金融依据。'),
}
for pid,(scope,note) in direct.items():
    p=papers[pid]
    decisions[pid]={'scope':scope,'evidence_type':'title_abstract_financial_task_or_data',
                    'evidence_excerpt':p.get('abstract',''),'relevance_zh':note,'frozen_queue':'direct_official_metadata'}
save_json('checks/finance_expansion/manual_decisions.json',{
    'decisions':decisions,
    'queue_sha256':hashlib.sha256((base/'focused_queue.json').read_bytes()).hexdigest(),
    'new_main_queue_sha256':hashlib.sha256((base/'new_main_candidate_queue.json').read_bytes()).hexdigest(),
    'note':'Decisions join by paper ID. The frozen queue indices document the review, not regeneration order.'})
print('reviewed additions',len(decisions))
