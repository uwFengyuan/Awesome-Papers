"""Verify catalog preservation, taxonomy relations, grouped exports and workbook views."""
import csv
import json
import re
from pathlib import Path
from urllib.parse import unquote
import openpyxl

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'checks/research_taxonomy'
def readcsv(path):return list(csv.DictReader(path.open(encoding='utf-8-sig')))
rows=readcsv(ROOT/'catalog.csv');byid={r['id']:r for r in rows}
before=json.loads((BASE/'catalog_before_taxonomy.json').read_text())
schema=json.loads((BASE/'schema.json').read_text())
assignments=json.loads((BASE/'assignments.json').read_text())
summary=json.loads((BASE/'summary.json').read_text())
finance=json.loads((ROOT/'checks/finance_review.json').read_text())['included']
topics={x['id']:x for x in schema['topics']}
children={x['id']:x for x in schema['subtopics']}
assert len(rows)==len(byid)==len(assignments)==len(before)==summary['papers']
assert set(byid)==set(assignments)=={r['id'] for r in before}
for old in before:
    new=byid[old['id']]
    assert all(new[k]==v for k,v in old.items()),old['id']
for pid,a in assignments.items():
    r=byid[pid]
    assert a['primary_topic_id'] in a['topic_ids']
    assert len(a['topic_ids'])==len(set(a['topic_ids'])) and set(a['topic_ids'])<=set(topics),pid
    assert len(a['subtopic_ids'])==len(set(a['subtopic_ids'])) and set(a['subtopic_ids'])<=set(children),pid
    assert all(children[i]['parent_id'] in a['topic_ids'] for i in a['subtopic_ids']),pid
    assert {e['topic_id'] for e in a['evidence']}>=set(a['topic_ids']),pid
    assert r['research_primary_topic']==topics[a['primary_topic_id']]['label']
    assert r['research_topic_ids'].split('; ')==a['topic_ids']
    assert r['research_topics']=='; '.join(topics[i]['label'] for i in a['topic_ids'])
    assert r['research_subtopics']=='; '.join(children[i]['label'] for i in a['subtopic_ids'])
    assert r['research_review_status']==a['review_status']
assert {pid for pid,a in assignments.items() if 'finance' in a['topic_ids']}==set(finance)
assert sum(summary['primary_counts'].values())==len(rows)
jsonl=[json.loads(l) for l in (ROOT/'catalog.jsonl').read_text().splitlines()]
assert {p['id'] for p in jsonl}==set(byid)
assert all(p['research']==assignments[p['id']] for p in jsonl)
stats=readcsv(BASE/'topic_counts.csv')
for s in stats:
    expected={pid for pid,a in assignments.items() if s['topic_id'] in a['topic_ids']}
    group=readcsv(ROOT/f"indexes/research_topics/{s['topic_id']}.csv")
    assert {r['id'] for r in group}==expected and len(group)==len(expected),s['topic_id']
    assert int(s['papers'])==len(group)
    assert int(s['primary_papers'])==sum(assignments[pid]['primary_topic_id']==s['topic_id'] for pid in expected)
    assert int(s['best_or_outstanding'])==sum(byid[pid]['is_best_or_outstanding']=='True' for pid in expected)
    assert int(s['oral'])==sum(byid[pid]['is_oral']=='True' for pid in expected)
    assert (ROOT/f"indexes/research_topics/{s['topic_id']}.md").is_file()

wb=openpyxl.load_workbook(ROOT/'catalog.xlsx',read_only=True,data_only=True)
for name,expected in [('All Papers',set(byid)),('Other Papers',set(byid)-set(finance)),('AI for Finance',set(finance))]:
    ws=wb[name];header=next(ws.iter_rows(values_only=True));col=header.index('id')
    ids={r[col] for r in ws.iter_rows(min_row=2,values_only=True)}
    assert ids==expected and ws.max_row-1==len(expected),name
assert wb['Research Topics'].max_row-1==len(topics)
assert wb['Research Subtopics'].max_row-1==len(children)
wb.close()

# Inspected boundary cases cover early ML, modern LLMs, and independent finance tags.
checks={'icml-2017-601':'optimization','icml-2017-811':'probabilistic',
        'icml-2017-850':'fairness_explainability','icml-2019-4270':'robustness',
        'neurips-2023-72164':'alignment','2024.emnlp-main.419':'information_extraction'}
for pid,expected in checks.items():assert assignments[pid]['primary_topic_id']==expected,(pid,assignments[pid]['primary_topic_id'])
assert 'finance' in assignments['2024.emnlp-main.419']['topic_ids']
assert assignments['2024.emnlp-main.122']['review_status']=='manually_reviewed_metadata'

links=0
for path in [ROOT/'README.md',ROOT/'indexes/research_topics.md',ROOT/'indexes/research_taxonomy.md',*sorted((ROOT/'indexes/research_topics').glob('*.md'))]:
    for target in re.findall(r'\]\(([^\n)]+)\)',path.read_text()):
        if re.match(r'^[a-zA-Z][\w+.-]*:',target) or target.startswith('#'):continue
        assert (path.parent/unquote(target.split('#')[0])).exists(),(path,target)
        links+=1
pending=readcsv(BASE/'pending_review.csv')
assert len(pending)==summary['needs_review']
report=dict(papers=len(rows),nonfinance_papers=len(rows)-len(finance),finance_papers=len(finance),
    topics=len(topics),subtopics=len(children),manual_metadata_reviews=summary['manual_overrides'],
    pending_finer_review=len(pending),catalog_ids_awards_oral_finance_and_pdf_records_preserved=True,
    primary_topic_count_sum=sum(summary['primary_counts'].values()),
    all_topic_evidence_and_subtopic_relations_valid=True,topic_csv_and_workbook_memberships_verified=True,
    local_links_verified=links,semantic_boundary_checks_passed=True)
(BASE/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
