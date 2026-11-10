"""Current, reproducible coverage and pending lists for the expanded finance collection."""
from common import *
import csv
import re
from collections import Counter,defaultdict
from urllib.parse import quote

base=ROOT/'checks/finance_expansion'
papers=load_json('sources/resolved_universe.json.gz');byid={p['id']:p for p in papers}
review=json.loads((ROOT/'checks/finance_review.json').read_text());finance=review['included']
screen=json.loads((base/'screening_summary.json').read_text())
previous=json.loads((base/'previous_finance_review.json').read_text())['included']
candidates=json.loads((base/'candidates.json').read_text())

def writecsv(path,rows,fields):
    with path.open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(rows)

downloads={}
for log in [ROOT/'checks/download_results.jsonl',base/'review_downloads.jsonl']:
    for line in log.read_text().splitlines():
        try:r=json.loads(line)
        except Exception:continue
        if r.get('status')=='downloaded' and (ROOT/r['local_path']).is_file():downloads.setdefault(r['id'],r)

# Main-track evidence is an explicit field, never inferred from a title's subject.
track_evidence=defaultdict(dict)
for path in [RAW/'neurips-2026-events.gz',*sorted(RAW.glob('finance-expansion-neurips-2026-events*.gz'))]:
    for e in json.loads(gzip.decompress(path.read_bytes()))['results']:
        label=e.get('sourceurl')
        if label:track_evidence[norm(e['name'])][label]=str(path.relative_to(ROOT))
main_titles={norm(p['title']) for p in papers if p['venue']=='NeurIPS' and p['year']==2026}
export=json.loads(gzip.decompress((RAW/'neurips-2026-download-json.gz').read_bytes()))
finrx=re.compile(r'financ(?:e|ial)|\bstocks?\b|portfolio|credit[- ](?:risk|scor|default|card)|\b(?:loan|fraud|insurance|banking|cryptocurrency|bitcoin|macroeconomic|taxation)\b|money launder|\bESG\b',re.I)
finname=re.compile(r'\bFin[A-Z][A-Za-z0-9-]+\b')
tracks={'confirmed_main':[],'excluded_nonmain':[],'unverified':[]}
for e in export:
    text=e['name']+' '+e.get('abstract','')
    if not (finrx.search(text) or finname.search(text)):continue
    labels=track_evidence.get(norm(e['name']),{})
    row=dict(e,track_evidence=labels)
    if norm(e['name']) in main_titles:tracks['confirmed_main'].append(row)
    elif labels:tracks['excluded_nonmain'].append(row)
    else:tracks['unverified'].append(row)
save_json('checks/finance_expansion/track_dispositions.json',tracks)

pdf_checks=[]
for name in ['pdf_evidence.json','review_pdf_evidence_v2.json','review_pdf_evidence_final.json']:
    f=base/name
    if f.exists():pdf_checks.extend(json.loads(f.read_text()))
scanned={x['id']:x for x in pdf_checks}
fullqueue=[byid[r['id']] for r in json.loads((base/'review_downloads.json').read_text())]
reviewed_texts={r['id'] for r in json.loads((base/'review_downloads.json').read_text())
    if r.get('status')=='downloaded' and finance_text_cache(r['id']).is_file()}
unavailable=[dict(id=p['id'],venue=p['venue'],year=p['year'],title=p['title'],paper_url=p['paper_url'],
    status='fulltext_not_available; financial relevance not established by this status') for p in fullqueue if p['id'] not in downloads and p['id'] not in reviewed_texts]
writecsv(base/'fulltext_not_available.csv',unavailable,['id','venue','year','title','paper_url','status'])

rejected={}
for decision_file,queue_fields in [
    ('pdf_decisions.json',[('named_dataset_pdf_queue.json','excluded_indices'),('domain_pdf_queue.json','domain_excluded_indices')]),
    ('supplementary_decisions.json',[('new_named_pdf_queue.json','new_named_excluded_indices'),('new_domain_pdf_queue.json','new_domain_excluded_indices'),('dataset_alias_queue.json','dataset_alias_excluded_indices'),('extended_metadata_queue.json','extended_metadata_excluded_indices')]),
]:
    obj=json.loads((base/decision_file).read_text())
    for qname,field in queue_fields:
        q=json.loads((base/qname).read_text())
        for i in obj.get(field,[]):rejected[q[i]['id']]='Reviewed match was background, citation, lexical ambiguity, or did not establish a financial task.'
for x in review['excluded']:rejected[x['id']]=x.get('reason_zh','Previously reviewed non-financial meaning')
final_decisions=base/'final_decisions.json'
if final_decisions.exists():
    for pid,info in json.loads(final_decisions.read_text()).get('excluded',{}).items():
        rejected[pid]=info['reason']

decisions=[];pending=[]
cost_or_lexical=re.compile(r'taking stock|trading.off|loanword|phonetic loan|credit assignment|privacy accountan|moments accountant|financial (?:cost|burden|support)|financial.*(?:train|comput)|FinFET|fine.grained alignment.*medical',re.I)
strong=re.compile(r'financ(?:e|ial)|\bstocks?\b|portfolio|\b(?:loan|fraud|insurance|banking|cryptocurrency|bitcoin|macroeconomic|taxation)\b|credit (?:risk|scor|default)|money launder|\bESG\b|invoices?|receipts?',re.I)
for c in candidates:
    pid=c['id'];text=c['title']+' '+c['abstract']
    if pid in finance:status='confirmed_finance';reason=finance[pid].get('relevance_zh','')
    elif pid in rejected:status='reviewed_not_admitted';reason=rejected[pid]
    elif cost_or_lexical.search(text) and not any(strong.search(s) and not cost_or_lexical.search(s) for s in c['finance_sentences']):
        status='lexical_or_cost_match';reason='Keyword refers to computing costs, a non-financial sense, or a method name.'
    elif pid in scanned:
        status='text_screened_not_confirmed';reason='Local text searched; no reviewed substantive financial evidence admitted. This is not a proof of irrelevance.'
    else:status='needs_fulltext_review';reason='Title/abstract match remains insufficient; full text not reviewed.'
    row={k:c[k] for k in ['id','venue','year','title','paper_url']};row.update(status=status,reason=reason)
    decisions.append(row)
    if status=='needs_fulltext_review' and strong.search(text):pending.append(dict(row,abstract=c['abstract']))
writecsv(base/'all_candidate_dispositions.csv',decisions,['id','venue','year','title','paper_url','status','reason'])
writecsv(base/'pending_finance.csv',pending,['id','venue','year','title','paper_url','status','reason','abstract'])

coverage=[]
for venue in ['ICML','ICLR','ACL','EMNLP','NeurIPS']:
    for year in range(2017,2027):
        ps=[p for p in papers if p['venue']==venue and p['year']==year]
        fs=[p for p in ps if p['id'] in finance]
        coverage.append({'venue':venue,'year':year,'main_records_screened':len(ps),
            'abstracts_available':sum(bool(p.get('abstract')) for p in ps),
            'financial_core':sum(finance[p['id']]['scope']=='core' for p in fs),
            'financial_application_or_case':sum(finance[p['id']]['scope']=='application' for p in fs),
            'financial_pdfs':sum(p['id'] in downloads for p in fs),
            'financial_missing_pdfs':sum(p['id'] not in downloads for p in fs),
            'texts_machine_screened':sum(p['id'] in scanned for p in ps)})
writecsv(base/'coverage.csv',coverage,list(coverage[0]))
counts={'main_papers_screened':len(papers),'abstracts_available':sum(bool(p.get('abstract')) for p in papers),
        'metadata_candidates':len(candidates),'confirmed_finance':len(finance),'previous_finance':len(previous),
        'added_finance':len(set(finance)-set(previous)),
        'core':sum(x['scope']=='core' for x in finance.values()),
        'application_or_case':sum(x['scope']=='application' for x in finance.values()),
        'financial_pdfs':sum(pid in downloads for pid in finance),
        'financial_missing_pdfs':sum(pid not in downloads for pid in finance),
        'financial_papers_without_oral_or_award':sum(not byid[pid]['oral'] and not byid[pid]['awards'] for pid in finance),
        'texts_machine_screened':len(scanned),'fulltext_screening_queue':len(fullqueue),
        'review_queue_fulltext_not_available':len(unavailable),
        'pending_metadata_finance_review':len(pending),'candidate_dispositions':dict(Counter(r['status'] for r in decisions)),
        'neurips_2026_keyword_candidates_unverified_track':len(tracks['unverified']),
        'neurips_2026_keyword_candidates_excluded_nonmain':len(tracks['excluded_nonmain'])}
save_json('checks/finance_expansion/summary.json',counts)

md=['# 金融相关论文扩充审计\n',
    '范围：2017 年至当前快照，ICML、ICLR、ACL、EMNLP、NeurIPS 的全部 main。**金融收录不依赖 Best / Oral；普通 Poster 同样纳入。** Findings、Workshop、Industry、Demo、独立 Position / Datasets / Evaluations 等 track 排除。\n',
    f"本次从 {counts['main_papers_screened']:,} 条主会记录重新筛查，取得 {counts['abstracts_available']:,} 条摘要；金融清单由 {len(previous)} 篇扩充为 **{len(finance)} 篇**，新增 {counts['added_finance']} 篇。其中 {counts['core']} 篇为金融核心问题，{counts['application_or_case']} 篇为通用方法中的金融数据、金融实验、金融案例、相关理论或金融任务综述。{counts['financial_papers_without_oral_or_award']} 篇没有 Oral 或获奖标签。\n",
    f"题名摘要扩展筛查产生 {len(candidates):,} 个宽松候选；随后对已有资料及额外检索的 {counts['texts_machine_screened']:,} 篇 PDF 进行正文机器检索，人工复核具体金融证据。机器检索不等于逐篇完整阅读。另有 {len(unavailable)} 篇通用方法的复核队列正文暂未取得，不能把它们直接认定为金融或非金融论文。\n",
    '## 金融相关的判断\n',
    '- `core`：金融市场、投资与交易、信贷与保险、金融安全、金融文档、企业披露与 ESG 等明确金融问题。\n',
    '- `application`：有具体金融数据、任务、业务案例或金融场景建模；也保留与金融任务有实质关联的综述。研究主方向可能是通用机器学习或 NLP，不能把这些论文都称为金融专用方法。\n',
    '- 经费、算力花费、作者的金融机构名称、参考文献中的金融论文、词义示例，以及借用 portfolio / Hedge / credit 名词，都不能单独建立金融相关性。FinGPT/FinBERT 的芬兰语版本、DP privacy accountant、FinFET、医学 FinAl、非金融 ESG 缩写已作歧义处理。\n',
    '- M4 官方元数据有 24,534 条 Finance 序列，分布在 Yearly / Quarterly / Monthly / Weekly / Daily；Hourly 没有 Finance 序列。只把已确认使用相应金融相关子集的实验纳入，具体来源见 [核验记录](m4_financial_domain_provenance.json)。\n',
    '## 输出与逐条证据\n',
    '- [金融 Excel](../../finance_catalog.xlsx)、[金融 CSV](../../finance_catalog.csv)、[金融 BibTeX](../../finance_references.bib)、[主题索引与论文笔记](../../indexes/ai_for_finance.md)。\n',
    '- [50 个会议年份的金融覆盖](coverage.csv)、[全部题名摘要候选的处置](all_candidate_dispositions.csv)、[待取得全文的金融关键词候选](pending_finance.csv)。\n',
    '- [人工纳入决策](manual_decisions.json)、[原有 PDF 的正文复核](pdf_decisions.json)、[额外全文与数据集别名复核](supplementary_decisions.json)、[最终补查复核](final_decisions.json)。原始队列冻结，哈希记录在决策文件中，ID 用于关联。\n',
    '- [额外全文复核队列中尚未取得的文件](fulltext_not_available.csv)；这是通用方法复核队列，不是已确认金融论文的缺失列表。已确认金融论文的下载状态以金融总表为准。\n',
    '- 筛查中间 PDF 已按 [清理清单](review_cache_cleanup.json) 移除；收录论文的正文保留在正式 `pdfs/` 目录，全文检索缓存、下载记录和校验值保留供追溯。\n',
    f"- NeurIPS 2026 全 track 导出中的金融关键词候选，另有 {len(tracks['excluded_nonmain'])} 条已明确属于非 main track，{len(tracks['unverified'])} 条尚未核验 track；见 [逐条分类](track_dispositions.json)。未确认 main 的项目不混入正式金融总表。\n",
    '## 覆盖限制\n',
    '收集目标是覆盖全部主会金融相关论文；当前公开来源与正文可得性仍有限制，因此不宣称零遗漏。未取得全文时，可能漏掉题名摘要没有披露的金融实验；NeurIPS 2026 的部分 track 记录还待核验。所有缺口保留清单，后续可以在同一目录继续补全。\n']
(base/'README.md').write_text('\n'.join(md))

lines=['# 待核验项目\n','## ICLR 2020 展示类型\n','以下候选不计入已核验 Oral。\n']
for x in json.loads((ROOT/'checks/oral_pending.json').read_text()):
    lines.append(f"- {x.get('title',x.get('id',''))} — {x.get('paper_url',x.get('url',''))}")
lines.append('\n## 历史奖项\n')
for x in json.loads((ROOT/'checks/award_pending.json').read_text()):lines.append('- '+json.dumps(x,ensure_ascii=False))
lines.append('\n## NeurIPS 2026：金融关键词命中，main track 尚未核验\n')
for x in tracks['unverified']:lines.append(f"- [{x['name']}]({x['virtualsite_url']})")
lines.append('\n已明确属于独立非 main track 的记录见 [track_dispositions.json](../checks/finance_expansion/track_dispositions.json)。金融正文复核候选见 [pending_finance.csv](../checks/finance_expansion/pending_finance.csv)。\n')
(ROOT/'indexes/pending.md').write_text('\n'.join(lines))
print(json.dumps(counts,ensure_ascii=False,indent=2),flush=True)
