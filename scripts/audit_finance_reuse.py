"""Plan local finance reuse without downloading, copying or modifying either catalog."""
import csv
import hashlib
import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REFERENCE = Path('/home/qi/aiagent/Awesome-AI4Finance-Papers')


def normalized_title(value):
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', value).casefold())


def records(path):
    with path.open(encoding='utf-8-sig', newline='') as stream:
        return list(csv.DictReader(stream))


def main():
    local = records(ROOT / 'catalog.csv')
    reference_root = REFERENCE if (REFERENCE / 'finance_catalog.csv').exists() else REFERENCE / 'main'
    reference_path = reference_root / 'finance_catalog.csv'
    reference_bytes = reference_path.read_bytes()
    reference = records(reference_path)
    by_id = {r['id']: r for r in local}
    by_title = {(r['venue'], r['year'], normalized_title(r['title'])): r for r in local}
    output = []
    for row in reference:
        match = by_id.get(row['id']) or by_title.get((row['venue'], row['year'], normalized_title(row['title'])))
        source = reference_root / row['local_path'] if row.get('local_path') else None
        exists = bool(source and source.is_file())
        same = bool(match and row.get('sha256') and row['sha256'] == match.get('sha256'))
        if match and match.get('download_status') == 'downloaded' and (ROOT / match['local_path']).is_file():
            action = 'reuse_existing_repository_pdf' if same else 'review_pdf_version_difference'
        elif exists:
            action = 'reuse_reference_pdf_after_scope_verification'
        else:
            action = 'metadata_only_no_local_pdf'
        output.append(dict(id=row['id'], title=row['title'], venue=row['venue'], year=row['year'],
                           track=row.get('track', ''), existing_id=match['id'] if match else '',
                           reference_local_path=row.get('local_path', ''),
                           reference_pdf_exists=exists, reference_sha256=row.get('sha256', ''),
                           existing_pdf_same_recorded_sha256=same, action=action))
    # Refuse a mixed snapshot if another process is updating the reference export.
    assert reference_path.read_bytes() == reference_bytes, 'Reference catalog changed during the audit; retry.'
    folder = ROOT / 'checks/scope_revision'
    folder.mkdir(exist_ok=True)
    with (folder / 'finance_reuse_plan.csv').open('w', encoding='utf-8-sig', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(output[0]))
        writer.writeheader()
        writer.writerows(output)
    summary = dict(reference_repository=str(REFERENCE),
                   reference_catalog_sha256=hashlib.sha256(reference_bytes).hexdigest(),
                   reference_records=len(reference),
                   reference_track_counts=dict(Counter(r['track'] for r in output)),
                   reference_venue_counts=dict(Counter(r['venue'] for r in output)),
                   actions=dict(Counter(r['action'] for r in output)),
                   downloaded_files=0, copied_files=0, reference_repository_modified=False,
                   note='This is a reuse plan. Publication track and long-paper eligibility still need validation.')
    (folder / 'finance_reuse_audit.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
