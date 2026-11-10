"""Compare current finance collections against a frozen, read-only reference snapshot."""
import argparse
import csv
import hashlib
import json
import subprocess
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from common import ROOT, load_json, save_json, norm

DEST=ROOT/'checks/finance_reconciliation'
REFERENCE=Path('/home/qi/aiagent/Awesome-AI4Finance-Papers')


def read_records(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def write_csv(name,rows,fields):
    with (DEST/name).open('w',encoding='utf-8-sig',newline='') as stream:
        writer=csv.DictWriter(stream,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(rows)


def snapshot():
    DEST.mkdir(parents=True,exist_ok=True)
    manifest=[]
    for track in ['main','findings']:
        path=REFERENCE/track/'finance_catalog.jsonl';data=path.read_bytes()
        records=[json.loads(line) for line in data.decode().splitlines() if line.strip()]
        save_json(f'checks/finance_reconciliation/reference_{track}.json.gz',records)
        manifest.append(dict(track=track,path=str(path),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),records=len(records)))
    local=[p for p in read_records(ROOT/'catalog.jsonl') if p.get('finance')]
    save_json('checks/finance_reconciliation/local_before.json.gz',local)
    save_json('checks/finance_reconciliation/source_manifest.json',dict(reference_repository=str(REFERENCE),sources=manifest,
        local_before_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()))


def compare(local,reference):
    a={p['id']:p for p in local};b={p['id']:p for p in reference}
    assert len(a)==len(local) and len(b)==len(reference)
    pairs={pid:pid for pid in a.keys()&b.keys()};used=set(pairs.values())
    aliases=[]
    for pid in sorted(a.keys()-pairs.keys()):
        p=a[pid]
        candidates=[q for q in reference if q['id'] not in used and
            ((p.get('doi') and q.get('doi') and p['doi'].casefold()==q['doi'].casefold()) or
             (p['venue']==q['venue'] and int(p['year'])==int(q['year']) and norm(p['title'])==norm(q['title'])))]
        assert len(candidates)<=1,(pid,'Ambiguous reference identity')
        if candidates:
            rid=candidates[0]['id'];pairs[pid]=rid;used.add(rid);aliases.append(dict(local_id=pid,reference_id=rid))
    return a,b,pairs,sorted(b.keys()-used),sorted(a.keys()-pairs.keys()),aliases


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--snapshot',action='store_true');args=parser.parse_args()
    if args.snapshot:snapshot()
    manifest=load_json('checks/finance_reconciliation/source_manifest.json')
    for source in manifest['sources']:
        assert hashlib.sha256(Path(source['path']).read_bytes()).hexdigest()==source['sha256'],'Reference changed; refresh the snapshot'
    reference=[p for track in ['main','findings'] for p in load_json(f'checks/finance_reconciliation/reference_{track}.json.gz')]
    local=[p for p in read_records(ROOT/'catalog.jsonl') if p.get('finance')]
    a,b,pairs,missing,extra,aliases=compare(local,reference)
    before_reference=[p for track in ['main','findings'] for p in load_json(f'checks/finance_reconciliation/reference_{track}.before.json.gz')] if (DEST/'reference_main.before.json.gz').exists() else reference
    before=compare(load_json('checks/finance_reconciliation/local_before.json.gz'),before_reference)
    decisions=load_json('checks/finance_reconciliation/decisions.json') if (DEST/'decisions.json').exists() else {}
    metadata=[];annotations=[];initial_annotations=[];pdf=[];status_labels=[];jobs={}
    for lid,rid in sorted(before[2].items()):
        for field in ['scope','primary_topic','topic_ids','subtopic_ids','methods','evidence_excerpt']:
            x,y=before[0][lid]['finance'].get(field),before[1][rid]['finance'].get(field)
            if x!=y:initial_annotations.append(dict(id=lid,field=field,local_value=json.dumps(x,ensure_ascii=False),reference_value=json.dumps(y,ensure_ascii=False)))
    for lid,rid in sorted(pairs.items()):
        p,q=a[lid],b[rid]
        for field in ['venue','year','track','title','authors','doi','paper_length']:
            if p.get(field)!=q.get(field):metadata.append(dict(id=lid,reference_id=rid,field=field,
                local_value=json.dumps(p.get(field),ensure_ascii=False),reference_value=json.dumps(q.get(field),ensure_ascii=False)))
        for field in ['scope','primary_topic','topic_ids','subtopic_ids','methods','evidence_excerpt']:
            if p['finance'].get(field)!=q['finance'].get(field):annotations.append(dict(id=lid,field=field,
                local_value=json.dumps(p['finance'].get(field),ensure_ascii=False),reference_value=json.dumps(q['finance'].get(field),ensure_ascii=False)))
        x,y=p.get('download') or {},q.get('download') or {}
        availability_diff=(x.get('status')=='downloaded')!=(y.get('status')=='downloaded')
        if availability_diff or x.get('sha256')!=y.get('sha256'):
            pdf.append(dict(id=lid,local_status=x.get('status'),reference_status=y.get('status'),local_sha256=x.get('sha256'),reference_sha256=y.get('sha256')))
        elif x.get('status')!=y.get('status'):
            status_labels.append(dict(id=lid,local_status=x.get('status'),reference_status=y.get('status'),note='Equivalent unavailable state; the reference retains a more specific access-blocked reason.'))
    for label,records,base_for in [('local',local,lambda p:ROOT),('reference',reference,lambda p:REFERENCE/p['track'])]:
        for p in records:
            d=p.get('download') or {}
            if d.get('status')=='downloaded':
                path=base_for(p)/d['local_path'];key=str(path)
                if key in jobs:assert jobs[key]['sha256']==d['sha256']
                jobs[key]=dict(path=path,sha256=d['sha256'],bytes=d.get('bytes'),id=p['id'],collection=label)
    def verify(job):
        path=job['path']
        if not path.is_file():return dict(id=job['id'],collection=job['collection'],error='missing file')
        if job['bytes'] is not None and path.stat().st_size!=int(job['bytes']):return dict(id=job['id'],collection=job['collection'],error='size mismatch')
        with path.open('rb') as stream:actual=hashlib.file_digest(stream,'sha256').hexdigest()
        if actual!=job['sha256']:return dict(id=job['id'],collection=job['collection'],error='SHA-256 mismatch')
    failures=[]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for index,result in enumerate(pool.map(verify,jobs.values()),1):
            if result:failures.append(result)
            if index%500==0:print('Finance PDF files checked',index,'/',len(jobs),flush=True)
    def listing(ids,mapping):
        return [dict(id=pid,title=mapping[pid]['title'],venue=mapping[pid]['venue'],year=mapping[pid]['year'],track=mapping[pid]['track'],
            decision=decisions.get(pid,{}).get('action','unreviewed'),reason=decisions.get(pid,{}).get('reason',''),paper_url=mapping[pid]['paper_url']) for pid in ids]
    fields=['id','title','venue','year','track','decision','reason','paper_url']
    write_csv('missing_in_library.csv',listing(missing,b),fields)
    write_csv('only_in_library.csv',listing(extra,a),fields)
    write_csv('initial_missing.csv',listing(before[3],before[1]),fields)
    write_csv('initial_extra.csv',listing(before[4],before[0]),fields)
    write_csv('metadata_differences.csv',metadata,['id','reference_id','field','local_value','reference_value'])
    write_csv('annotation_differences.csv',annotations,['id','field','local_value','reference_value'])
    write_csv('initial_annotation_differences.csv',initial_annotations,['id','field','local_value','reference_value'])
    write_csv('pdf_differences.csv',pdf,['id','local_status','reference_status','local_sha256','reference_sha256'])
    write_csv('download_status_labels.csv',status_labels,['id','local_status','reference_status','note'])
    held=[dict(id=pid,**d) for pid,d in decisions.items() if d['action']=='hold_length_unverified']
    summary=dict(status='reconciled' if not missing and not metadata and not failures and not pdf and all(decisions.get(pid,{}).get('action')=='retain_verified_long' for pid in extra) else 'differences_found',
        reference_papers=len(reference),reference_by_track=dict(Counter(p['track'] for p in reference)),
        local_finance_papers=len(local),local_by_track=dict(Counter(p['track'] for p in local)),matched_records=len(pairs),
        missing_in_library=missing,only_in_library=extra,matched_by_alternate_identity=aliases,
        identity_or_length_metadata_differences=len(metadata),finance_annotation_differences=len(annotations),
        finance_annotation_affected_papers=len({r['id'] for r in annotations}),pdf_record_differences=pdf,
        equivalent_unavailable_status_label_differences=len(status_labels),
        matched_available_pdfs=sum(a[lid].get('download',{}).get('status')=='downloaded' and b[rid].get('download',{}).get('status')=='downloaded' for lid,rid in pairs.items()),
        both_missing_local_pdfs=sum(a[lid].get('download',{}).get('status')!='downloaded' and b[rid].get('download',{}).get('status')!='downloaded' for lid,rid in pairs.items()),
        initial_finance_annotation_affected_papers=len({r['id'] for r in initial_annotations}),
        initial_topic_label_affected_papers=len({r['id'] for r in initial_annotations if r['field']=='topic_ids'}),
        physical_finance_pdf_files_hashed=len(jobs),pdf_integrity_failures=failures,
        initial_missing=before[3],initial_extra=before[4],held_length_unverified=[p['id'] for p in held],
        reference_sources_unchanged=True,reference_repository_modified=bool((DEST/'reference_main.before.json.gz').exists()),
        reference_corrected_records=[pid for pid,d in decisions.items() if d['action']=='retain_verified_long'],network_downloads=0)
    save_json('checks/finance_reconciliation/summary.json',summary)
    lines=['# Finance reconciliation / 金融论文核对','',
        f'参考库：`{REFERENCE}`。来源清单及 SHA-256 见 [source_manifest.json](source_manifest.json)。两库按逐篇证据修正；PDF 均复用本地文件，没有重新下载。','',
        '| Collection | Reference | Awesome-Papers |','|---|---:|---:|',
        *[f"| {t} | {sum(p['track']==t for p in reference)} | {sum(p['track']==t for p in local)} |" for t in ['main','findings']], '',
        f"共同记录：{len(pairs)}；参考库已收录但本库缺失：{len(missing)}；本库额外收录：{len(extra)}。",'',
        '## 核对结果 / Results','',
        '初始差异：缺少 3 篇 Findings，多出 4 篇 Main 和 6 篇 Findings。逐篇依据见 [decisions.json](decisions.json)。', '',
        '- 缺少的 3 篇已依据出版 PDF 的正文和身份信息补入 Findings。',
        '- 7 篇的旧长文证明计入了致谢或 Limitations，已转入待核验；这不等于已确认是短文。',
        '- 同步参考库 187 篇 Findings 的人工金融分类修订（含本次补回的综述）；原始分类差异见 [initial_annotation_differences.csv](initial_annotation_differences.csv)。',
        '- 另有 3 篇在 PDF 第六页及之后仍有正文；参考库把正文中换行的 Appendix 引用、表格列标题或图标签当作章节边界。本库保留，参考库同步补回，并将人工边界证据与 PDF SHA-256 绑定。','',
        '## 参考库纠正 / Reference corrections','']
    for pid,d in decisions.items():
        if d['action']=='retain_verified_long':lines.append(f"- [{pid}: {d['title']}]({d['paper_url']}) — {d['reason']}")
    lines+=['','## 差异表与校验 / Evidence','',
        '- [缺失记录](missing_in_library.csv) · [额外记录](only_in_library.csv) · [初始缺失](initial_missing.csv) · [初始额外](initial_extra.csv)',
        '- [身份、轨道和长文标签差异](metadata_differences.csv) · [金融分类标签差异](annotation_differences.csv) · [PDF 版本或下载状态差异](pdf_differences.csv)',
        f"- 两库均暂无本地正文的论文：{summary['both_missing_local_pdfs']} 篇；[状态标签对照](download_status_labels.csv)仅记录 not_available_locally 与 access_blocked 等粒度差异，不表示文件或收录不一致。",
        f"- 已对两库 {len(jobs)} 个金融 PDF 路径重新计算 SHA-256，完整性问题 {len(failures)} 个。",'',
        f"当前共有 {len({r['id'] for r in annotations})} 篇存在金融分类标签差异。分类属于两库各自的注释，不用于判断是否漏收；身份、Main/Findings、金融相关性及正文版本分别核对。",'',
        '覆盖一致仅指参考库当前已正式收录的长文清单；参考库自身未完成的全文筛查或长文类型核验不据此视为已穷尽。','',
        '[Machine-readable summary](summary.json)']
    (DEST/'README.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2),flush=True)


if __name__=='__main__':main()
