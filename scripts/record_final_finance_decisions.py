"""Record the final human review of recovered full texts, using frozen queues."""
from common import *
import re

base = ROOT/'checks/finance_expansion'
out = {'decisions': {}, 'excluded': {}, 'queue_sha256': {}}
for filename, excluded in [('final_named_pdf_queue.json', {37, 43, 62}),
                           ('dataset_alias_final_queue.json', {0, 8, 78})]:
    path = base/filename
    queue = json.loads(path.read_text())
    out['queue_sha256'][filename] = hashlib.sha256(path.read_bytes()).hexdigest()
    for i, x in enumerate(queue):
        if i in excluded:
            out['excluded'][x['id']] = {'queue': filename, 'index': i,
                'reason': 'Reference, background discussion without financial evaluation, or unrelated NASDAQ method acronym.'}
            continue
        if x['id'] in out['decisions']:
            continue
        evidence = x.get('review_evidence', x['evidence'])
        selected = next((e for e in evidence if not re.search(r'arxiv preprint|Expert systems with applications|References|In International Conference', e['excerpt'], re.I)), evidence[0])
        excerpt = selected['excerpt']
        patterns = {16: r'39,463', 17: r'HomeCredit Default',
                    26: r'FinMultiTime.*?is a dataset', 43: None}
        if filename == 'final_named_pdf_queue.json' and i in patterns and patterns[i]:
            t = re.sub(r'\s+', ' ', gzip.decompress(finance_text_cache(x['id']).read_bytes()).decode())
            m = re.search(patterns[i], t, re.I)
            assert m, (i, patterns[i])
            excerpt = t[max(0, m.start()-120):m.end()+600]
        if filename == 'dataset_alias_final_queue.json' and i == 29:
            excerpt = next(e['excerpt'] for e in evidence if 'Exchange Rate dataset includes' in e['excerpt'])
        case = filename == 'final_named_pdf_queue.json' and i in {28, 39}
        label = selected['match']
        out['decisions'][x['id']] = {
            'scope': 'application',
            'evidence_type': 'fulltext_financial_case_or_formal_model' if case else 'fulltext_financial_data_or_task',
            'evidence_excerpt': excerpt, 'evidence_local_path': x['local_path'],
            'relevance_zh': ('金融隐私或支付操作的实际评测案例。' if case else
                '通用方法包含金融数据、金融训练数据或金融任务评测；证据标记：'+label+'。'+
                ('M4 年度至日度子集包含金融序列，未把仅使用 M4 Hourly 的论文据此纳入。' if 'M4' in label.upper() else '')),
            'review_basis': 'Human review of financial dataset/task evidence; excludes reference-only hits and nonfinancial acronyms.',
            'frozen_queue': filename, 'frozen_queue_index': i}
filename = 'final_domain_pdf_queue.json'
path = base/filename
queue = json.loads(path.read_text())
out['queue_sha256'][filename] = hashlib.sha256(path.read_bytes()).hexdigest()
accepted = {4,10,11,13,14,18,19,23,25,30,31,33,34,36,37,38,39,42,49,50,52,53,57,64,66,69,73,78,80,83,84,86,89,96,98,100,102,110,112,115,117,119,125,126,127,129,130,132,134,138,142,143,144,148,150,152}
overrides = {10:r'Credit \(CR\)', 25:r'credit-approval', 30:r'PAIRS T RADING',
             31:r'experiments, including stock data', 38:r'Bank \.9420',
             42:r'Unemployment rate time series', 49:r'AMD stock price',
             50:r'Loan-Decision dataset', 57:r'Company JPMorgan',
             66:r'loan 95\.3',78:r'credit-g 21', 80:r'Loan Default P',
             83:r'Finance domain',86:r'TAIWAN credit-default dataset',
             89:r'credit-g 1000',96:r'Financial time series',
             100:r'We construct the finance datasets',112:r'two real-world settings',
             115:r'Credit \(CR\)',117:r'Finance Healthcare',
             125:r'bank-marketing',126:r'Specifi- cally, we utilize',
             127:r'credit 16714',138:r'such as sports, technology, and finance',
             144:r'Bank 0\.929',148:r'Portfolio Benchmark with Piecewise-Linear',
             150:r'AAPL_stock_price'}
for i, x in enumerate(queue):
    if i not in accepted:
        out['excluded'][x['id']] = {'queue':filename,'index':i,
            'reason':'Financial task not confirmed from reviewed evidence; keyword/background/reference alone is insufficient.'}
        continue
    excerpt = x['review_evidence'][0]['excerpt']
    if i in overrides:
        t = re.sub(r'\s+', ' ', gzip.decompress(finance_text_cache(x['id']).read_bytes()).decode())
        m = re.search(overrides[i],t,re.I)
        assert m, (i,overrides[i])
        excerpt = t[max(0,m.start()-100):m.end()+620]
    out['decisions'][x['id']] = {
        'scope':'application', 'evidence_type':'fulltext_financial_case_or_formal_model' if i in {18,49,50} else 'fulltext_financial_data_or_task',
        'evidence_excerpt':excerpt,'evidence_local_path':x['local_path'],
        'relevance_zh':'正文包含金融数据、金融训练数据、金融任务评测或具体金融场景案例。'+('本篇使用健康保险理赔记录开展医疗事件预测，属于保险数据应用。' if i==19 else ''),
        'frozen_queue':filename,'frozen_queue_index':i,
        'review_basis':'Human review of recovered full-text financial evidence.'}
metadata_path = base/'final_metadata_queue.json'
if metadata_path.exists():
    out['queue_sha256'][metadata_path.name] = hashlib.sha256(metadata_path.read_bytes()).hexdigest()
    for x in json.loads(metadata_path.read_text()):
        out['decisions'][x['id']] = {
            'scope':'application','evidence_type':'official_abstract_financial_experiment',
            'evidence_excerpt':x['abstract'],
            'relevance_zh':'官方摘要明确报告 portfolio 组合优化基准上的实验；属于通用决策学习方法的金融应用。',
            'frozen_queue':metadata_path.name,
            'review_basis':'Official main-track abstract reports portfolio benchmark; PDF unavailable at this snapshot.'}
save_json('checks/finance_expansion/final_decisions.json', out)
print('Final reviewed inclusions', len(out['decisions']), 'excluded', len(out['excluded']))
