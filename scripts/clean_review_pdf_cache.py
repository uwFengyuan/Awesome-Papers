"""Remove generated screening PDFs after validating retained text and library copies."""
from common import *
import csv

base=ROOT/'checks/finance_expansion'
records=json.loads((base/'review_downloads.json').read_text())
canonical={r['id']:r for r in csv.DictReader((ROOT/'catalog.csv').open(encoding='utf-8-sig'))}
manifest=[]
for r in records:
    if r.get('status')!='downloaded':continue
    path=ROOT/r['local_path']
    # Some review rows reused the original canonical library; those are retained.
    if not path.resolve().is_relative_to((base/'review_pdfs').resolve()):continue
    cache=finance_text_cache(r['id'])
    assert cache.is_file()
    gzip.decompress(cache.read_bytes())
    selected=canonical.get(r['id'])
    if selected:
        retained=ROOT/selected['local_path']
        assert retained.is_file() and retained!=path
        assert hashlib.sha256(retained.read_bytes()).hexdigest()==selected['sha256']
    if path.exists():
        assert path.stat().st_size==r['bytes']
        assert hashlib.sha256(path.read_bytes()).hexdigest()==r['sha256']
    manifest.append({'id':r['id'],'generated_path':r['local_path'],'bytes':r['bytes'],'sha256':r['sha256'],
        'text_cache':str(cache.relative_to(ROOT)),
        'retained_library_path':selected['local_path'] if selected else None,
        'disposition':'Remove generated screening PDF; retain full-text search cache and provenance.'})
save_json('checks/finance_expansion/review_cache_cleanup.json',{'validated_manifest':manifest,
    'completed':False,'note':'Only paths from this task screening-download manifest are eligible.'})
for r in manifest:
    path=ROOT/r['generated_path']
    if path.exists():path.unlink()
save_json('checks/finance_expansion/review_cache_cleanup.json',{'validated_manifest':manifest,
    'completed':True,'completed_at_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'note':'Selected papers retain canonical PDFs; unselected screening PDFs are represented by compressed full text and provenance.'})
print('Generated screening PDF paths removed',len(manifest),flush=True)
