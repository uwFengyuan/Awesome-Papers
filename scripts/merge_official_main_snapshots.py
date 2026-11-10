"""Union explicitly main-labelled official snapshots; record any track conflicts."""
from common import *
from urllib.parse import parse_qs, urlparse

papers = load_json('sources/resolved_universe.json.gz')
by_title = {(p['venue'],p['year'],norm(p['title'])):p for p in papers}
by_id = {p['id']:p for p in papers}
export = {norm(p['name']):p for p in json.loads(gzip.decompress((RAW/'neurips-2026-download-json.gz').read_bytes()))}
all_tracks = {}
keys = ['neurips-2026-events'] + [p.stem for p in sorted(RAW.glob('finance-expansion-neurips-2026-events*.gz'))]
added = []
for key in keys:
    events = json.loads(gzip.decompress((RAW/(key+'.gz')).read_bytes()))['results']
    for e in events:
        label = e.get('sourceurl') or ''
        if not label or e.get('eventtype') not in ['Poster','Oral','Spotlight']:
            continue
        nt = norm(e['name'])
        all_tracks.setdefault(nt,set()).add(label)
        if label != 'https://openreview.net/group?id=NeurIPS.cc/2026/Conference':
            continue
        evidence = f'sources/raw/{key}.gz'
        old = by_title.get(('NeurIPS',2026,nt))
        if old:
            old.setdefault('main_track_evidence',[])
            if evidence not in old['main_track_evidence']:old['main_track_evidence'].append(evidence)
            continue
        url = e.get('paper_url') or next((m['uri'] for m in e.get('eventmedia',[]) if m.get('name')=='OpenReview'), '')
        uid = parse_qs(urlparse(url).query).get('id',[''])[0]
        pid = 'neurips-2026-' + (uid or str(e['id']))
        if pid in by_id:
            raise ValueError(f'Unresolved identity collision {pid}')
        virt = 'https://neurips.cc' + e['virtualsite_url']
        abstract = export.get(nt,{}).get('abstract','')
        p = {'id':pid,'venue':'NeurIPS','year':2026,'title':e['name'],
             'authors':[x['fullname'] for x in e.get('authors',[])],
             'abstract':abstract,'abstract_source':'https://neurips.cc/Downloads/2026',
             'paper_url':url or virt,'pdf_url':'https://openreview.net/pdf?id='+uid if uid else '',
             'awards':[],'award_evidence':[],'oral':e['eventtype']=='Oral',
             'oral_evidence':[virt] if e['eventtype']=='Oral' else [],
             'presentation_original':[e.get('decision') or e['eventtype']],
             'metadata_sources':['https://neurips.cc/static/virtual/data/neurips-2026-orals-posters.json'],
             'code_urls':[],'track':'main','virtual_url':virt,'source_venue':label,
             'main_track_evidence':[evidence]}
        papers.append(p);by_id[pid]=p;by_title[('NeurIPS',2026,nt)]=p;added.append(pid)
conflicts = {k:sorted(v) for k,v in all_tracks.items() if len(v)>1}
assert not conflicts, 'Conflicting track labels require manual review before applying'
save_json('sources/resolved_universe.json.gz',papers)
save_json('checks/finance_expansion/main_snapshot_merge.json',{
    'source_snapshots':keys,'added_ids':added,'added_rows':len(added),
    'neurips_2026_verified_main':sum(p['venue']=='NeurIPS' and p['year']==2026 for p in papers),
    'track_conflicts':conflicts,
})
print('added',len(added),'NeurIPS 2026 main',sum(p['venue']=='NeurIPS' and p['year']==2026 for p in papers))
