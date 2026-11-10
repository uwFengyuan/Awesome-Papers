"""Inventory existing records before scope changes; does not remove or move files."""
import csv
import json
import subprocess
from collections import Counter
from pathlib import Path
from paper_attributes import award_types, paper_length, presentation_types, publication_track

ROOT = Path(__file__).resolve().parents[1]


def main():
    folder = ROOT / 'checks/scope_revision'
    folder.mkdir(exist_ok=True)
    rows = []
    for line in (ROOT / 'catalog.jsonl').open(encoding='utf-8'):
        paper = json.loads(line)
        length, evidence = paper_length(paper)
        awards = award_types(paper)
        download = paper.get('download', {}) or {}
        rows.append(dict(id=paper['id'], title=paper['title'], venue=paper['venue'],
                         year=paper['year'], track=publication_track(paper),
                         paper_length=length, paper_length_evidence=evidence,
                         award_types='; '.join(dict.fromkeys(a['type'] for a in awards)),
                         awards_original='; '.join(a['original_name'] for a in awards),
                         presentation_types='; '.join(presentation_types(paper)),
                         is_finance=bool(paper.get('finance')),
                         local_path=download.get('local_path', ''),
                         sha256=download.get('sha256', '')))
    with (folder / 'paper_attribute_inventory.csv').open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    report = dict(source_commit=subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip(),
                  records=len(rows), paper_length_counts=dict(Counter(r['paper_length'] for r in rows)),
                  by_venue_and_length=dict(Counter(r['venue'] + '/' + r['paper_length'] for r in rows)),
                  publication_track_counts=dict(Counter(r['track'] for r in rows)),
                  pdf_page_counts_used_to_infer_paper_type=False,
                  catalog_and_pdfs_modified=False,
                  note='Attribute audit only; final collection scope awaits clarification.')
    (folder / 'attribute_audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
