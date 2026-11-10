"""Check taxonomy relationships, preservation of admission, and exported filters."""
import csv
import json
from pathlib import Path
import openpyxl

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'checks/finance_taxonomy'
schema=json.loads((DEST/'schema.json').read_text())
assignments=json.loads((DEST/'assignments.json').read_text())
before=json.loads((DEST/'finance_review_before_taxonomy.json').read_text())['included']
after=json.loads((ROOT/'checks/finance_review.json').read_text())['included']
assert set(before)==set(after)==set(assignments)
assert all(before[pid]['scope']==after[pid]['scope'] for pid in before)
topics={x['id']:x for x in schema['topics']}
subtopics={x['id']:x for x in schema['subtopics']}
methods={x['id']:x for x in schema['methods']}
assert len(subtopics)==len(schema['subtopics'])
for pid,a in assignments.items():
    assert a['primary_topic_id'] in a['topic_ids'],pid
    for field,allowed in [('topic_ids',topics),('subtopic_ids',subtopics),('method_ids',methods)]:
        assert len(a[field])==len(set(a[field])) and set(a[field])<=set(allowed),(pid,field)
    assert all(subtopics[s]['parent_id'] in a['topic_ids'] for s in a['subtopic_ids']),pid
    assert 'other_finance' not in a['topic_ids'] or len(a['topic_ids'])==1,pid
    assert {e['topic_id'] for e in a['topic_evidence']}>=set(a['topic_ids']),pid
    assert after[pid]['topics']==[topics[t]['label'] for t in a['topic_ids']],pid
    assert after[pid]['primary_topic']==topics[a['primary_topic_id']]['label'],pid

def readcsv(path):return list(csv.DictReader(path.open(encoding='utf-8-sig')))
rows=readcsv(ROOT/'finance_catalog.csv')
assert {r['id'] for r in rows}==set(after)
for r in rows:
    a=assignments[r['id']]
    assert r['finance_primary_topic']==topics[a['primary_topic_id']]['label']
    assert r['finance_topic_ids'].split('; ')==a['topic_ids']
    assert r['finance_subtopics']=='; '.join(subtopics[s]['label'] for s in a['subtopic_ids'])
    assert r['finance_methods']=='; '.join(methods[m]['label'] for m in a['method_ids'])

wb=openpyxl.load_workbook(ROOT/'finance_catalog.xlsx',read_only=True,data_only=True)
for ident,topic in topics.items():
    expected={pid for pid,a in assignments.items() if ident in a['topic_ids']}
    subset=readcsv(ROOT/f'indexes/finance_topics/{ident}.csv')
    assert {r['id'] for r in subset}==expected and len(subset)==len(expected),ident
    ws=wb[topic['sheet']];header=next(ws.iter_rows(values_only=True));column=header.index('id')
    actual={r[column] for r in ws.iter_rows(min_row=2,values_only=True)}
    assert actual==expected,ident
    assert (ROOT/f'indexes/finance_topics/{ident}.md').is_file()
assert wb['Topics'].max_row-1==len(topics)
assert wb['Subtopics'].max_row-1==len(subtopics)
assert wb['Methods'].max_row-1==len(methods)
wb.close()

# Concrete ambiguity checks based on inspected papers, not just rule matching.
assert 'alpha_mining' in assignments['iclr-2026-d97Q8r7ZKZ']['topic_ids']
assert assignments['neurips-2026-NZHuWIlAUx']['primary_topic_id']=='asset_pricing'
assert 'alpha_mining' not in assignments['icml-2025-Pedm1880A2']['topic_ids']
assert 'portfolio' not in assignments['iclr-2026-iqUMjxfDNH']['topic_ids']
assert assignments['icml-2026-EKmiOtjZjI']['topic_ids']==['time_series']
assert assignments['iclr-2026-RzT2sombPD']['primary_topic_id']=='time_series'
assert assignments['P17-1126']['primary_topic_id']=='financial_nlp'
assert assignments['2026.emnlp-main.1329']['primary_topic_id']=='corporate_finance'

report=dict(finance_papers=len(after),topics=len(topics),subtopics=len(subtopics),methods=len(methods),
    original_finance_ids_and_scope_preserved=True,
    primary_topic_counts_sum=sum(sum(a['primary_topic_id']==i for a in assignments.values()) for i in topics),
    every_primary_topic_and_subtopic_valid=True,every_topic_has_classification_evidence=True,
    csv_and_excel_topic_memberships_match=True,reviewed_ambiguity_checks_passed=True,
    financial_pdfs=sum(r['download_status']=='downloaded' for r in rows),
    manual_overrides=sum('manual_override' in a for a in assignments.values()))
(DEST/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
