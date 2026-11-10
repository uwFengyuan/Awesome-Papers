"""Validate scoped admission, split exports, physical PDFs, hashes, and generated links."""
from common import *
import csv
import re
from collections import Counter
from urllib.parse import unquote
from concurrent.futures import ThreadPoolExecutor
import openpyxl


def read_csv(path):
    with path.open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))


def main():
    rows=read_csv(ROOT/'catalog.csv');byid={r['id']:r for r in rows}
    records={p['id']:p for p in map(json.loads,(ROOT/'catalog.jsonl').read_text().splitlines())}
    selected={p['id']:p for p in load_json('checks/scope_revision/selected_papers.json.gz')}
    assert len(rows)==len(byid)==len(records)==len(selected)
    assert set(byid)==set(records)==set(selected)
    publication_keys=[(r['venue'],r['year'],r['track'],norm(r['title'])) for r in rows]
    assert len(publication_keys)==len(set(publication_keys)), 'Duplicate publication records'
    for row in rows:
        p=records[row['id']]
        assert row['venue'] in {'ICML','ICLR','ACL','EMNLP','NeurIPS','AAAI'}
        assert 2017<=int(row['year'])<=2026
        assert row['paper_length']=='long' and p['paper_length']=='long' and row['paper_length_evidence']
        assert row['track'] in {'main','findings','datasets_benchmarks','evaluations'}
        if row['track']=='findings':assert row['finance_scope'] and row['is_curated']=='False'
        if not row['finance_scope'] or row['track'] not in {'main','findings'}:
            assert row['track']!='findings' and row['is_curated']=='True'
            assert row['is_best']=='True' or row['is_outstanding']=='True' or row['is_oral']=='True'
        if row['is_curated']=='True':
            assert any(a['type'] in {'best','outstanding'} and a['evidence'] for a in p['award_types']) or (p['oral'] and p['oral_evidence'])
        assert row['is_best']==str(any(a['type']=='best' for a in p['award_types']))
        assert row['is_outstanding']==str(any(a['type']=='outstanding' for a in p['award_types']))
        if row['finance_scope'] and row['local_path']:
            assert row['local_path'].startswith('pdfs/finance/'+row['track']+'/')
        if row['local_path']:
            assert (ROOT/row['local_path']).is_file(),row['local_path']
            assert '[Long]' in row['local_path']
            if row['track']=='main':assert '[Main]' in row['local_path']
            if row['is_oral']=='True':assert '[Oral]' in row['local_path']
            if row['is_best']=='True':assert '[Best]' in row['local_path']
            if row['is_outstanding']=='True':assert '[Outstanding]' in row['local_path']
            assert p['download']['local_path']==row['local_path']
            assert p['download']['sha256']==row['sha256']
        assert row['classification_path']==p['fine_classification']['classification_path']
    # Exactly the admitted PDF paths are present in the working tree.
    files={r['local_path']:r for r in rows if r['local_path']}
    assert {str(p.relative_to(ROOT)) for p in (ROOT/'pdfs').rglob('*.pdf')}==set(files)
    problems=[]
    def verify_file(item):
        name,row=item;path=ROOT/name
        if path.stat().st_size!=int(row['bytes']):return name+' size mismatch'
        with path.open('rb') as f:actual=hashlib.file_digest(f,'sha256').hexdigest()
        if actual!=row['sha256']:return name+' SHA-256 mismatch'
        return None
    with ThreadPoolExecutor(max_workers=4) as pool:
        for n,problem in enumerate(pool.map(verify_file,files.items()),1):
            if problem:problems.append(problem)
            if n%1000==0:print('PDF hashes verified',n,'/',len(files),flush=True)
    assert not problems,problems
    finance={r['id'] for r in rows if r['finance_scope']}
    assert {r['id'] for r in read_csv(ROOT/'finance_catalog.csv')}==finance
    for track in ['main','findings']:
        data=read_csv(ROOT/f'finance/{track}/catalog.csv')
        expected={r['id'] for r in rows if r['finance_scope'] and r['track']==track}
        assert {r['id'] for r in data}==expected and all(r['track']==track for r in data)
        jsonl={r['id'] for r in map(json.loads,(ROOT/f'finance/{track}/catalog.jsonl').read_text().splitlines())}
        assert jsonl==expected
        wb=openpyxl.load_workbook(ROOT/f'finance/{track}/catalog.xlsx',read_only=True,data_only=True)
        values=wb['Papers'].iter_rows(values_only=True);header=next(values);index=header.index('id')
        assert {r[index] for r in values}==expected;wb.close()
    wb=openpyxl.load_workbook(ROOT/'catalog.xlsx',read_only=True,data_only=True)
    values=wb['All Papers'].iter_rows(values_only=True);header=next(values);index=header.index('id')
    assert {r[index] for r in values}==set(byid);wb.close()
    assert len(re.findall(r'^@inproceedings\{',(ROOT/'references.bib').read_text(),re.M))==len(rows)
    baseline=load_json('checks/scope_revision/baseline.json')
    for p in baseline['papers']:
        old=p.get('download') or {};new=byid.get(p['id'])
        if new and old.get('status')=='downloaded':assert new['sha256']==old['sha256'],p['id']
    generated=load_json('checks/generated_paths.json')
    # The report itself is a generated target referenced by both homepages.
    save_json('checks/current_validation.json',{'status':'checking links'})
    links=0
    for name in generated:
        path=ROOT/name
        assert path.is_file(),name
        if path.suffix!='.md':continue
        for target in re.findall(r'\]\(([^\n)]+)\)',path.read_text()):
            if re.match(r'^[a-zA-Z][\w+.-]*:',target) or target.startswith('#'):continue
            assert (path.parent/unquote(target.strip('<>').split('#')[0])).exists(),(name,target)
            links+=1
    for name in ['README.md', 'README.zh-CN.md']:
        content = (ROOT/name).read_text()
        if content.startswith('---\n'):
            _, delimiter, content = content[4:].partition('\n---\n')
            assert delimiter, (name, 'Unclosed YAML front matter')
        assert content.lstrip('\n').startswith('# Awesome Papers'), name
    assert '[简体中文](README.zh-CN.md)' in (ROOT/'README.md').read_text()
    assert '[English](README.md)' in (ROOT/'README.zh-CN.md').read_text()
    active_sizes=[(p.stat().st_size,str(p.relative_to(ROOT))) for parent in ['pdfs','sources','checks','scripts','finance','indexes']
        for p in (ROOT/parent).rglob('*') if p.is_file()]
    active_sizes.extend((p.stat().st_size,p.name) for p in ROOT.iterdir() if p.is_file())
    oversized=[dict(path=name,bytes=size) for size,name in active_sizes if size>=100*1024*1024]
    assert not oversized,oversized
    report=dict(status='passed',papers=len(rows),finance=len(finance),
        tracks=dict(Counter(r['track'] for r in rows)),venues=dict(Counter(r['venue'] for r in rows)),
        only_verified_long_papers=True,excluded_tracks_absent=True,finance_main_findings_separated=True,
        best_outstanding_oral_independent=True,unique_pdf_files=len(files),pdf_sha256_failures=problems,
        duplicate_publication_records_absent=True,
        original_retained_pdf_hashes_preserved=True,local_links_checked=links,
        csv_jsonl_excel_memberships_match=True,bilingual_readmes_present=True,
        files_at_or_above_100_mib=oversized,largest_file=dict(zip(['bytes','path'],max(active_sizes))))
    save_json('checks/current_validation.json',report)
    print(json.dumps(report,ensure_ascii=False,indent=2),flush=True)


if __name__=='__main__':main()
