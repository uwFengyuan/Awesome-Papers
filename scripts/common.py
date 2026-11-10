"""Cached, auditable downloads. Run scripts with PYTHONPATH=/tmp/paper_collection_deps."""
import concurrent.futures
import datetime
import gzip
import hashlib
import json
import pathlib
import threading
import time
import requests

ROOT = pathlib.Path(__file__).resolve().parents[1]
RAW = ROOT / 'sources' / 'raw'
RAW.mkdir(parents=True, exist_ok=True)
LOCK = threading.Lock()
AGENT = 'AcademicLiteratureCollection/1.0 (public research papers; polite cached requests)'

def finance_text_cache(paper_id):
    """Locate full-text evidence by venue/year to stay below Hub directory limits."""
    import re
    venues = {'acl': 'ACL', 'emnlp': 'EMNLP', 'icml': 'ICML',
              'iclr': 'ICLR', 'neurips': 'NeurIPS', 'aaai': 'AAAI'}
    match = re.match(r'^(icml|iclr|neurips|aaai)-(\d{4})-', paper_id)
    if match:
        venue, year = match.groups()
    else:
        match = re.match(r'^(\d{4})\.(?:findings-)?(acl|emnlp)[.-]', paper_id)
        if match:
            year, venue = match.groups()
        else:
            match = re.match(r'^([PD])(\d{2})-', paper_id)
            if not match:
                raise ValueError(f'Unsupported finance text-cache paper ID: {paper_id}')
            prefix, short_year = match.groups()
            venue, year = {'P': 'acl', 'D': 'emnlp'}[prefix], '20' + short_year
    return ROOT / 'checks' / 'finance_expansion' / 'pdf_texts' / venues[venue] / year / (paper_id + '.txt.gz')

def fetch(url, key=None, timeout=80, retries=2):
    key = key or hashlib.sha256(url.encode()).hexdigest()[:24]
    path = RAW / (key + '.gz')
    meta = RAW / (key + '.meta.json')
    if path.exists() and meta.exists():
        info = json.loads(meta.read_text())
        if info.get('url') == url:
            return gzip.decompress(path.read_bytes()), info
        return fetch(url, key + '-' + hashlib.sha256(url.encode()).hexdigest()[:10], timeout, retries)
    error = ''
    for attempt in range(retries):
        try:
            headers={'User-Agent': AGENT}
            if 'app.underline.io/api/' in url:headers['Accept']='application/vnd.api+json'
            r = requests.get(url, timeout=timeout, headers=headers)
            info = {'url': url, 'final_url': r.url, 'http_status': r.status_code,
                    'retrieved_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    'bytes': len(r.content), 'sha256': hashlib.sha256(r.content).hexdigest(),
                    'content_type': r.headers.get('content-type', ''), 'cache_path': str(path.relative_to(ROOT))}
            if r.status_code == 200:
                path.write_bytes(gzip.compress(r.content))
                meta.write_text(json.dumps(info, ensure_ascii=False, indent=2))
                return r.content, info
            error = f'HTTP {r.status_code}'
            if r.status_code not in [429, 500, 502, 503, 504]:
                break
        except Exception as exc:
            error = str(exc)
        time.sleep(1 + attempt * 2)
    info = {'url': url, 'error': error, 'retrieved_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat()}
    with LOCK:
        with (ROOT / 'checks' / 'fetch_errors.jsonl').open('a') as f:
            f.write(json.dumps(info, ensure_ascii=False) + '\n')
    return None, info

def load_json(path):
    """Read a UTF-8 JSON document, optionally compressed as .json.gz."""
    path = ROOT / path
    opener = gzip.open if path.suffix == '.gz' else open
    with opener(path, 'rt', encoding='utf8') as stream:
        return json.load(stream)

def save_json(path, data):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    if path.suffix == '.gz':
        with gzip.open(temp, 'wt', encoding='utf8', compresslevel=6) as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2)
    else:
        temp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf8')
    temp.replace(path)

def batch(jobs, workers=8):
    def one(job):
        key, url = job
        data, meta = fetch(url, key)
        return key, data, meta
    out = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for key, data, meta in pool.map(one, jobs):
            out[key] = (data, meta)
            print(key, 'OK' if data else meta.get('error'), len(data or b''), flush=True)
    return out

def norm(s):
    import re, unicodedata
    return re.sub(r'[^a-z0-9]', '', unicodedata.normalize('NFKD', s).casefold())
