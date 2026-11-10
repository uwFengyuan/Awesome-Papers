"""Verify the expanded finance deliverables against metadata and stored evidence."""
from common import *
import csv
import re
import zipfile
from urllib.parse import unquote
import openpyxl

base = ROOT/'checks/finance_expansion'
finance = json.loads((ROOT/'checks/finance_review.json').read_text())['included']
universe = {x['id']:x for x in load_json('sources/resolved_universe.json.gz')}
rows = list(csv.DictReader((ROOT/'finance_catalog.csv').open(encoding='utf-8-sig')))
catalog = list(csv.DictReader((ROOT/'catalog.csv').open(encoding='utf-8-sig')))
problems=[]
assert len(rows)==len(finance)==len({r['id'] for r in rows})
assert set(finance)=={r['id'] for r in rows}=={r['id'] for r in catalog if r['finance_scope']}
assert all(r['track']=='main' and r['id'] in universe for r in rows)
assert all(r['finance_scope'] in {'core','application'} for r in rows)
assert len(re.findall(r'^@inproceedings\{',(ROOT/'finance_references.bib').read_text(),re.M))==len(rows)
for r in rows:
    if r['download_status']=='downloaded':
        assert (ROOT/r['local_path']).is_file(),r['id']
    info=finance[r['id']]
    if info.get('evidence_local_path'):assert (ROOT/info['evidence_local_path']).is_file(),r['id']
    assert (ROOT/'indexes/finance_notes'/f"{r['id']}.md").is_file()
    assert r['pdf_version']!='publisher_version' or 'arxiv.org' not in r['pdf_url']

workbooks={}
for filename in ['catalog.xlsx','finance_catalog.xlsx']:
    with zipfile.ZipFile(ROOT/filename) as z:assert z.testzip() is None
    wb=openpyxl.load_workbook(ROOT/filename,read_only=True,data_only=True)
    workbooks[filename]={s.title:s.max_row-1 for s in wb}
    if filename=='finance_catalog.xlsx':
        ws=wb['Confirmed Finance'];header=[c.value for c in next(ws.iter_rows())];col=header.index('id')
        ids={r[col] for r in ws.iter_rows(min_row=2,values_only=True)}
        assert ids==set(finance)
        assert wb['Time Series'].max_row-1==sum('time_series' in r['finance_topic_ids'].split('; ') for r in rows)
    wb.close()

mdfiles=[ROOT/'README.md',base/'README.md',*sorted((ROOT/'indexes').rglob('*.md'))]
links=0
for path in mdfiles:
    for target in re.findall(r'\]\(([^\n)]+)\)',path.read_text()):
        target=target.strip('<>')
        if re.match(r'^[a-zA-Z][\w+.-]*:',target) or target.startswith('#'):continue
        target=unquote(target.split('#')[0])
        links+=1
        if not (path.parent/target).exists():problems.append({'file':str(path.relative_to(ROOT)),'target':target})

sources=0;source_problems=[]
for path in sorted(RAW.glob('*.meta.json')):
    meta=json.loads(path.read_text());cache=ROOT/meta['cache_path']
    try:
        data=gzip.decompress(cache.read_bytes())
        if len(data)!=meta['bytes'] or hashlib.sha256(data).hexdigest()!=meta['sha256']:
            source_problems.append(str(path.relative_to(ROOT)))
    except Exception as exc:source_problems.append({'path':str(path.relative_to(ROOT)),'error':str(exc)})
    sources+=1
save_json('checks/source_integrity.json',{'checked_sources':sources,'problems':source_problems})
report={'finance_rows':len(rows),'finance_pdf_records':sum(r['download_status']=='downloaded' for r in rows),
        'finance_missing_pdfs':sum(r['download_status']!='downloaded' for r in rows),
        'financial_time_series':sum('time_series' in r['finance_topic_ids'].split('; ') for r in rows),
        'workbook_data_rows':workbooks,'local_markdown_links_checked':links,
        'broken_local_links':problems,'sources_checked':sources,'source_problems':source_problems,
        'all_finance_ids_verified_in_main_universe':True}
save_json('checks/finance_expansion/deliverable_validation.json',report)
print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)
assert not problems and not source_problems
