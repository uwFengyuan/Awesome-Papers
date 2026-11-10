from common import *

# Manually cross-checked final PMLR titles and author lists against the official
# conference program. These are title changes/abbreviations, not fuzzy admissions.
mapping={
'icml-2017-612':'icml-2017-pmlr-bernstein17a',
'icml-2017-462':'icml-2017-pmlr-simsekli17a',
'icml-2017-740':'icml-2017-pmlr-vorontsov17a',
'icml-2017-565':'icml-2017-pmlr-gonzalez17a',
'icml-2017-826':'icml-2017-pmlr-nagamine17a',
'icml-2018-2362':'icml-2018-pmlr-wang18i',
'icml-2018-2109':'icml-2018-pmlr-kasai18a',
'icml-2019-3817':'icml-2019-pmlr-mahloujifar19a',
'icml-2019-4227':'icml-2019-pmlr-romoff19a'}
papers=load_json('sources/resolved_universe.json.gz');idx={p['id']:p for p in papers}
results={}
for line in (ROOT/'checks/download_results.jsonl').read_text().splitlines():
    try:r=json.loads(line);results[r['id']]=r
    except Exception:pass
audit=[]
for old_id,final_id in mapping.items():
    if old_id not in idx or final_id not in idx:continue
    p,q=idx[old_id],idx[final_id]
    audit.append({'retained_id':old_id,'merged_id':final_id,'program_title':p['title'],'final_pmlr_title':q['title'],
                  'program_authors':p['authors'],'pmlr_authors':q['authors'],'primary_source':q['paper_url'],'verification':'title change; author lists manually cross-checked'})
    p['program_title']=p['title'];p['title']=q['title'];p['authors']=q['authors'];p['pdf_url']=q['pdf_url'];p['proceedings_url']=q['paper_url']
    for field in ['metadata_sources','oral_evidence','awards','award_evidence','presentation_original']:
        p[field]=list(dict.fromkeys(p.get(field,[])+q.get(field,[])))
    p['oral']|=q['oral']
    r=results.get(final_id,{})
    if r.get('status')=='downloaded' and (ROOT/r['local_path']).is_file():
        r=dict(r,id=old_id,title=p['title'],alias_of=final_id)
        with (ROOT/'checks/download_results.jsonl').open('a') as f:f.write(json.dumps(r,ensure_ascii=False)+'\n')
papers=[p for p in papers if p['id'] not in set(mapping.values())]
save_json('checks/verified_title_aliases.json',audit)
save_json('sources/resolved_universe.json.gz',papers)
print('Verified title aliases',len(audit),'retained main universe',len(papers),flush=True)
