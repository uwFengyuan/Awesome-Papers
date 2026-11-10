"""Reproducible long-paper catalog, topic storage, and bilingual browsing views."""
from common import *
import argparse
import csv
import os
import re
import shutil
import subprocess
from collections import Counter, defaultdict
from urllib.parse import quote
from paper_attributes import presentation_types
from fine_topics import leaf, RULES as LEAF_RULES
from research_taxonomy import apply_research_taxonomy
from finance_taxonomy import apply_taxonomy

DEST=ROOT/'checks/scope_revision'
VENUES=['ICML','ICLR','ACL','EMNLP','NeurIPS','AAAI']


def clean(value):
    return re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]','',str(value or '')).replace('|','\\|').replace('\n',' ')


def relative(path, base):
    return quote(os.path.relpath(path,base),safe='/._-')


class Exporter:
    def __init__(self):self.generated=[]
    def text(self,path,text):
        path=ROOT/path;path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(text.rstrip()+'\n');self.generated.append(str(path.relative_to(ROOT)))
    def csv(self,path,rows,keys):
        path=ROOT/path;path.parent.mkdir(parents=True,exist_ok=True)
        with path.open('w',encoding='utf-8-sig',newline='') as stream:
            writer=csv.DictWriter(stream,fieldnames=keys,extrasaction='ignore');writer.writeheader();writer.writerows(rows)
        self.generated.append(str(path.relative_to(ROOT)))
    def table(self,path,title,rows,description=''):
        base=(ROOT/path).parent
        lines=[f'# {title}','',description,'',f'Papers / 论文：**{len(rows)}**','',
            '| Year | Venue | Track | Paper | Labels | Topic / task | PDF |',
            '|---|---|---|---|---|---|---|']
        for row in rows:
            pdf=f"[PDF]({relative(ROOT/row['local_path'],base)})" if row['local_path'] else f"[Online]({row['pdf_url'] or row['paper_url']})"
            lines.append(f"| {row['year']} | {row['venue']} | {row['track']} | [{clean(row['title'])}]({row['paper_url']}) | {row['labels']} | {clean(row['storage_topic'])} / {clean(row['storage_subtopic'])} / {clean(row['fine_topic'])} | {pdf} |")
        self.text(path,'\n'.join(lines))


def download_registry():
    output={}
    canonical=ROOT/'checks/download_results.json'
    for path in ([] if canonical.exists() else [ROOT/'checks/download_results.jsonl']):
        if path.exists():
            for line in path.open():
                try:r=json.loads(line)
                except ValueError:continue
                if r.get('status')=='downloaded' and r.get('local_path') and (ROOT/r['local_path']).is_file():output[r['id']]=r
    path=ROOT/'checks/download_results.json'
    if path.exists():
        for r in load_json(path):
            if r.get('status')=='downloaded' and r.get('local_path') and (ROOT/r['local_path']).is_file():output[r['id']]=r
    path=DEST/'new_pdf_results.json'
    if path.exists():
        for r in load_json(path):
            if r.get('status')=='downloaded':output.setdefault(r['id'],r)
    reuse=load_json('checks/scope_revision/reference_pdf_reuse.json')
    for pid,r in reuse.items():
        if (pathlib.Path(r['reference_repository'])/r['local_path']).is_file():
            output.setdefault(pid,dict(r,source_path=str(pathlib.Path(r['reference_repository'])/r['local_path'])))
    lengths=load_json('checks/scope_revision/pdf_length_evidence.json')
    for pid,r in lengths.items():
        if 'findings-' in pid and pathlib.Path(r['pdf_cache_path']).is_file():
            output.setdefault(pid,dict(id=pid,status='downloaded',source_path=r['pdf_cache_path'],
                sha256=r['pdf_sha256'],pdf_version='publisher_version'))
    return output


def workbook(path,sheets,fields):
    import openpyxl
    from openpyxl.cell import WriteOnlyCell
    wb=openpyxl.Workbook(write_only=True)
    keys=[k for k in fields if k not in {'abstract','award_evidence','oral_evidence','metadata_sources','paper_length_evidence','finance_evidence_excerpt'}]
    for name,rows in sheets:
        ws=wb.create_sheet(name);ws.freeze_panes='A2';ws.append(keys)
        for row in rows:
            values=[]
            for key in keys:
                value=row.get(key,'')
                if isinstance(value,str):
                    cell=WriteOnlyCell(ws,value=value[:32760]);cell.data_type='s'
                    if key in {'paper_url','local_path'} and value:cell.hyperlink=value
                    values.append(cell)
                else:values.append(value)
            ws.append(values)
    wb.save(path)


def run():
    parser=argparse.ArgumentParser();parser.add_argument('--plan-only',action='store_true');args=parser.parse_args()
    papers=load_json('checks/scope_revision/selected_papers.json.gz')
    assert papers and all(p['paper_length']=='long' for p in papers)
    # Retain the reference library's reviewed taxonomy overrides for the new AAAI records.
    overrides=load_json('checks/finance_taxonomy/manual_overrides.json')
    extra=DEST/'reference_finance_overrides.json'
    if extra.exists():overrides.update(json.loads(extra.read_text()))
    save_json('checks/finance_taxonomy/manual_overrides.json',overrides)
    review={'included':{p['id']:p['finance'] for p in papers if p.get('finance')}}
    paper_map={p['id']:p for p in papers}
    apply_taxonomy(paper_map,review)
    finance=review['included']
    for p in papers:p['finance']=finance.get(p['id'])
    research=apply_research_taxonomy(papers,finance)
    schema=load_json('checks/research_taxonomy/schema.json')
    topic_map={x['id']:x for x in schema['topics']};sub_map={x['id']:x for x in schema['subtopics']}
    fin_schema=load_json('checks/finance_taxonomy/schema.json')
    fin_topics={x['id']:x for x in fin_schema['topics']};fin_subs={x['id']:x for x in fin_schema['subtopics']}
    downloads=download_registry();rows=[];plans=[];sha_paths={};assignments={}
    for p in papers:
        pid=p['id'];a=research[pid];fin=finance.get(pid);r=downloads.get(pid,{})
        if fin:
            primary=next(x['id'] for x in fin_schema['topics'] if x['label']==fin['primary_topic'])
            subtopics=[sid for sid in fin['subtopic_ids'] if fin_subs[sid]['parent_id']==primary]
            sub=subtopics[0] if subtopics else 'general'
            topic_label=fin_topics[primary]['label'];sub_label=fin_subs[sub]['label'] if sub!='general' else 'General / 综合'
            base=pathlib.Path('pdfs/finance')/p['track']
        else:
            primary=a['primary_topic_id'];children=[s for s in a['subtopic_ids'] if sub_map[s]['parent_id']==primary]
            scores={e.get('subtopic_id'):e.get('score',0) for e in a['evidence']}
            sub=max(children,key=lambda s:scores.get(s,0)) if children else 'general'
            topic_label=topic_map[primary]['label'];sub_label=sub_map[sub]['label'] if sub!='general' else 'General / 综合'
            base=pathlib.Path('pdfs')/p['track']
        leaf_id,leaf_label,leaf_evidence=leaf(p,primary)
        folder=base/primary/sub/leaf_id
        types={x['type'] for x in p['award_types']}
        badge=['Long',{'main':'Main','findings':'Findings','datasets_benchmarks':'Datasets-Benchmarks','evaluations':'Evaluations'}[p['track']]]
        if 'best' in types:badge.append('Best')
        if 'outstanding' in types:badge.append('Outstanding')
        presentation=presentation_types(p)
        badge.extend(x for x in presentation if x in {'Oral','Spotlight','Poster'})
        if fin:badge.append('Finance')
        title=re.sub('[^A-Za-z0-9]+','_',p['title']).strip('_')[:100]
        filename=f"{p['year']}_{p['venue']}_"+''.join('['+x+']' for x in badge)+'__'+pid+'__'+title+'.pdf'
        # Ensure portable individual filename limits even for long source IDs.
        if len(filename.encode())>240:filename=filename[:235]+'.pdf'
        target=str(folder/filename)
        local_source=ROOT/r['local_path'] if r.get('local_path') else None
        source=str(local_source) if local_source and local_source.is_file() else r.get('source_path','')
        available=bool(source and pathlib.Path(source).is_file())
        if available and r.get('sha256'):
            key=(p['track'],r['sha256'])
            if key in sha_paths:target=sha_paths[key]
            else:sha_paths[key]=target
        local_path=target if available else ''
        row=dict(id=pid,title=p['title'],authors='; '.join(p['authors']),venue=p['venue'],year=p['year'],track=p['track'],
            paper_length='long',paper_length_evidence=p['paper_length_evidence'],is_curated=p['is_curated'],
            is_best='best' in types,is_outstanding='outstanding' in types,is_best_or_outstanding=bool(types & {'best','outstanding'}),
            award_categories='; '.join(sorted(types)),awards_original='; '.join(p['awards']),
            is_oral='Oral' in presentation,presentation_type='; '.join(presentation),labels=' '.join('['+x+']' for x in badge),
            oral_candidate_unverified=bool(p.get('oral_candidate')),code_urls='; '.join(p.get('code_urls',[])),
            research_primary_topic=topic_map[a['primary_topic_id']]['label'],research_topic_ids='; '.join(a['topic_ids']),
            research_topics='; '.join(topic_map[x]['label'] for x in a['topic_ids']),
            research_subtopics='; '.join(sub_map[x]['label'] for x in a['subtopic_ids']),research_review_status=a['review_status'],
            storage_topic=topic_label,storage_subtopic=sub_label,fine_topic=leaf_label,classification_path=str(folder),
            finance_scope=fin['scope'] if fin else '',finance_primary_topic=fin['primary_topic'] if fin else '',
            finance_topic_ids='; '.join(fin['topic_ids']) if fin else '',finance_topics='; '.join(fin['topics']) if fin else '',
            finance_subtopics='; '.join(fin['subtopics']) if fin else '',finance_methods='; '.join(fin['methods']) if fin else '',
            finance_evidence_type=fin.get('evidence_type','') if fin else '',finance_evidence_excerpt=fin.get('evidence_excerpt','') if fin else '',
            paper_url=p['paper_url'],pdf_url=p.get('pdf_url',''),local_path=local_path,
            download_status='downloaded' if available else 'not_available_locally',pdf_version=r.get('pdf_version','publisher_version') if available else '',
            bytes=pathlib.Path(source).stat().st_size if available else '',sha256=r.get('sha256','') if available else '',
            award_evidence='; '.join(p['award_evidence']),oral_evidence='; '.join(p['oral_evidence']),
            metadata_sources='; '.join(p['metadata_sources']),abstract=p.get('abstract',''))
        rows.append(row);plans.append(dict(id=pid,source=source,target=target,available=available,sha256=r.get('sha256',''),registry=r))
        assignments[pid]=dict(primary_topic=primary,primary_subtopic=sub,leaf_id=leaf_id,leaf_label=leaf_label,
                             leaf_evidence=leaf_evidence,classification_path=str(folder))
    # Keep broad residual topics browsable without inventing narrower semantic labels.
    counts=Counter(r['classification_path'] for r in rows)
    remapped={}
    for row,plan in zip(rows,plans):
        if counts[row['classification_path']]<=100:continue
        old_target=plan['target']
        folder=pathlib.Path(row['classification_path'])/row['venue']/str(row['year'])
        target=remapped.setdefault(old_target,str(folder/pathlib.Path(old_target).name))
        plan['target']=target;row['classification_path']=str(folder)
        assignments[row['id']]['classification_path']=str(folder)
        if row['local_path']:row['local_path']=target
    save_json('checks/scope_revision/layout_plan.json',plans)
    save_json('checks/fine_taxonomy/assignments.json',assignments)
    save_json('checks/fine_taxonomy/schema.json',{'leaf_rules':[dict(parent=p,id=i,label=l,pattern=rx) for p,i,l,rx in LEAF_RULES]})
    if args.plan_only:
        print(json.dumps(dict(rows=len(rows),available=sum(r['download_status']=='downloaded' for r in rows),
            leaf_folders=len({r['classification_path'] for r in rows}),largest_folder=Counter(r['classification_path'] for r in rows).most_common(3)),ensure_ascii=False));return
    gitdir=pathlib.Path(subprocess.check_output(['git','rev-parse','--absolute-git-dir'],text=True).strip())
    archive=gitdir/'curated_scope_archive/b1af8187';archive.mkdir(parents=True,exist_ok=True)
    subprocess.run(['git','update-ref','refs/backup/pre-long-paper-scope-20261110','b1af8187d846491a00d07a7cb50055c758478f8d'],check=True)
    before_files=list((ROOT/'pdfs').rglob('*.pdf'))
    registered=[];migrations=[]
    for number,(plan,row) in enumerate(zip(plans,rows),1):
        if not plan['available']:continue
        source=pathlib.Path(plan['source']);target=ROOT/row['local_path'];target.parent.mkdir(parents=True,exist_ok=True)
        if source!=target and not target.exists():
            if source.is_relative_to(ROOT) and not source.is_relative_to(gitdir):
                source.rename(target)
            else:
                temp=target.with_suffix('.pdf.part');shutil.copyfile(source,temp)
                assert hashlib.sha256(temp.read_bytes()).hexdigest()==plan['sha256'],plan['id']
                temp.replace(target)
            migrations.append(dict(id=plan['id'],source=str(source),target=row['local_path']))
        assert target.stat().st_size==row['bytes'],row['id']
        registered.append(dict(plan['registry'],id=row['id'],status='downloaded',local_path=row['local_path'],
                               sha256=row['sha256'],bytes=row['bytes']))
        if number%1000==0:print('PDF layout records processed',number,'/',len(rows),flush=True)
    active={ROOT/r['local_path'] for r in rows if r['local_path']}
    excluded=[]
    for path in before_files:
        if path.exists() and path not in active:
            target=archive/path.relative_to(ROOT);target.parent.mkdir(parents=True,exist_ok=True)
            assert not target.exists(),target
            path.rename(target);excluded.append(str(path.relative_to(ROOT)))
    for folder in sorted((ROOT/'pdfs').rglob('*'),key=lambda p:len(p.parts),reverse=True):
        if folder.is_dir() and not any(folder.iterdir()):folder.rmdir()
    # Preserve the previous complete index set as local provenance; regenerate all views.
    if not (archive/'indexes').exists():(ROOT/'indexes').rename(archive/'indexes')
    previous=ROOT/'checks/generated_paths.json'
    if previous.exists():
        for name in load_json(previous):
            path=ROOT/name
            if path.is_file() and path.suffix in {'.md','.csv'}:path.unlink()
    (ROOT/'indexes').mkdir(exist_ok=True)
    save_json('checks/download_results.json',registered)
    save_json('checks/finance_review.json',review)
    save_json('checks/scope_revision/layout_migrations.json',migrations)
    if excluded:
        prior=DEST/'archived_pdf_paths.json'
        archived=load_json(prior) if prior.exists() else []
        save_json('checks/scope_revision/archived_pdf_paths.json',sorted(set(archived+excluded)))
    exporter=Exporter();fields=list(rows[0])
    exporter.csv('catalog.csv',rows,fields)
    coverage=[]
    for venue in VENUES:
        for year in range(2017,2027):
            group=[r for r in rows if r['venue']==venue and r['year']==year]
            coverage.append(dict(venue=venue,year=year,selected_records=len(group),
                curated=sum(r['is_curated'] for r in group),best=sum(r['is_best'] for r in group),
                outstanding=sum(r['is_outstanding'] for r in group),oral=sum(r['is_oral'] for r in group),
                finance_main=sum(bool(r['finance_scope']) and r['track']=='main' for r in group),
                finance_findings=sum(bool(r['finance_scope']) and r['track']=='findings' for r in group),
                pdf_downloaded=sum(bool(r['local_path']) for r in group)))
    exporter.csv('checks/coverage.csv',coverage,list(coverage[0]))
    sources=[]
    for path in sorted((ROOT/'sources/raw').glob('*.meta.json')):
        info=json.loads(path.read_text());info['metadata_file']=str(path.relative_to(ROOT));sources.append(info)
    source_fields=list(dict.fromkeys(key for info in sources for key in info))
    exporter.csv('sources/manifest.csv',sources,source_fields)
    registered_by_id={r['id']:r for r in registered}
    records={p['id']:dict(p,research=research[p['id']],fine_classification=assignments[p['id']],
        download=registered_by_id.get(p['id'],{'status':'not_available_locally'})) for p in papers}
    with (ROOT/'catalog.jsonl').open('w') as stream:
        for p in papers:stream.write(json.dumps(records[p['id']],ensure_ascii=False)+'\n')
    curated=[r for r in rows if r['is_curated']];financial=[r for r in rows if r['finance_scope']]
    exporter.csv('finance_catalog.csv',financial,fields)
    exporter.csv('checks/missing_pdfs.csv',[r for r in rows if not r['local_path']],fields)
    exporter.table(pathlib.Path('indexes/all_papers.md'),'All papers / 全部收录论文',rows)
    exporter.table(pathlib.Path('indexes/best_papers.md'),'Best Paper', [r for r in rows if r['is_best']])
    exporter.table(pathlib.Path('indexes/outstanding_papers.md'),'Outstanding Paper',[r for r in rows if r['is_outstanding']])
    exporter.table(pathlib.Path('indexes/oral_papers.md'),'Oral',[r for r in rows if r['is_oral']])
    exporter.table(pathlib.Path('indexes/neurips_datasets_benchmarks.md'),'NeurIPS Datasets / Benchmarks / Evaluations',[r for r in rows if r['track'] not in {'main','findings'}])
    for venue in VENUES:exporter.table(pathlib.Path(f'indexes/venues/{venue}.md'),venue,[r for r in rows if r['venue']==venue])
    for track in ['main','findings']:
        group=[r for r in financial if r['track']==track]
        exporter.csv(f'finance/{track}/catalog.csv',group,fields)
        exporter.table(pathlib.Path(f'finance/{track}/README.md'),f'AI for Finance — {track}',group)
        with (ROOT/f'finance/{track}/catalog.jsonl').open('w') as stream:
            for p in papers:
                if p['finance'] and p['track']==track:stream.write(json.dumps(records[p['id']],ensure_ascii=False)+'\n')
        workbook(ROOT/f'finance/{track}/catalog.xlsx',[('Papers',group)],fields)
        for topic in fin_topics:
            subgroup=[r for r in group if topic in r['finance_topic_ids'].split('; ')]
            exporter.table(pathlib.Path(f'finance/{track}/topics/{topic}.md'),fin_topics[topic]['label'],subgroup)
            exporter.csv(f'finance/{track}/topics/{topic}.csv',subgroup,fields)
    for topic in topic_map:
        group=[r for r in rows if topic in r['research_topic_ids'].split('; ')]
        exporter.table(pathlib.Path(f'indexes/research_topics/{topic}.md'),topic_map[topic]['label'],group)
        exporter.csv(f'indexes/research_topics/{topic}.csv',group,fields)
    for row in financial:
        exporter.text(f"indexes/finance_notes/{row['id']}.md",f"# {row['title']}\n\n{row['venue']} {row['year']} · {row['track']} · Long\n\n{row['labels']}\n\nFinancial evidence / 金融依据：{row['finance_evidence_excerpt']}\n\n[Paper]({row['paper_url']})\n\nClassification / 分类：{row['storage_topic']} → {row['storage_subtopic']} → {row['fine_topic']}\n\n## Abstract / 摘要\n\n{row['abstract']}")
    # Actual PDF folders have their own READMEs, including parent navigation.
    folders=defaultdict(list)
    for row in rows:
        folder=pathlib.Path(row['classification_path'])
        while folder!=pathlib.Path('.'):
            folders[folder].append(row)
            if folder==pathlib.Path('pdfs'):break
            folder=folder.parent
    for folder,group in folders.items():
        children=sorted(x for x in folders if x.parent==folder)
        if children:
            exporter.text(str(folder/'README.md'),f'# {folder.name}\n\nPapers / 论文：{len(group)}\n\n'+
                '\n'.join(f'- [{child.name}]({quote(child.name)}/README.md) — {len(folders[child])}' for child in children))
        else:exporter.table(folder/'README.md',str(folder),group)
    sheets=[('All Papers',rows),('Curated Main',curated),('Finance Main',[r for r in financial if r['track']=='main']),
            ('Finance Findings',[r for r in financial if r['track']=='findings'])]
    workbook(ROOT/'catalog.xlsx',sheets,fields)
    workbook(ROOT/'finance_catalog.xlsx',sheets[2:],fields)
    bib=[];fin_bib=[]
    for p in papers:
        title=p['title'].replace('&',r'\&').replace('%',r'\%').replace('#',r'\#')
        entry='@inproceedings{'+re.sub('[^A-Za-z0-9_-]','_',p['id'])+',\n  title = {{'+title+'}},\n  author = {'+' and '.join(p['authors'])+'},\n  year = {'+str(p['year'])+'},\n  url = {'+p['paper_url']+'}\n}\n'
        bib.append(entry)
        if p['finance']:fin_bib.append(entry)
    (ROOT/'references.bib').write_text('\n'.join(bib));(ROOT/'finance_references.bib').write_text('\n'.join(fin_bib))
    summary=dict(papers=len(rows),curated=len(curated),finance=len(financial),
        finance_main=sum(r['track']=='main' for r in financial),finance_findings=sum(r['track']=='findings' for r in financial),
        best=sum(r['is_best'] for r in rows),outstanding=sum(r['is_outstanding'] for r in rows),oral=sum(r['is_oral'] for r in rows),
        local_pdfs=sum(bool(r['local_path']) for r in rows),unique_pdf_paths=len(active),
        missing_pdf_records=sum(not r['local_path'] for r in rows),
        by_venue=dict(Counter(r['venue'] for r in rows)),by_track=dict(Counter(r['track'] for r in rows)),
        leaf_folders=len({r['classification_path'] for r in rows}),
        largest_leaf_folders=Counter(r['classification_path'] for r in rows).most_common(5),
        long_paper_rule='Official long/full-paper track or verified main-text evidence; short and unverified types withheld.',
        source_snapshot='2026-11-10',reference_finance_repository='Awesome-AI4Finance-Papers')
    save_json('checks/summary.json',summary)
    write_homepages(exporter,rows,summary,topic_map,fin_topics)
    write_evidence_notes(exporter)
    save_json('checks/generated_paths.json',exporter.generated)
    for folder in sorted((ROOT/'pdfs').rglob('*'),key=lambda p:len(p.parts),reverse=True):
        if folder.is_dir() and not any(folder.iterdir()):folder.rmdir()
    print(json.dumps(summary,ensure_ascii=False,indent=2),flush=True)


def write_homepages(exporter,rows,summary,topics,fin_topics):
    for chinese,path in [(False,'README.md'),(True,'README.zh-CN.md')]:
        lines=['# Awesome Papers','', '[English](README.md) · [简体中文](README.zh-CN.md)','',
            '[GitHub](https://github.com/uwFengyuan/Awesome-Papers) · [Hugging Face](https://huggingface.co/datasets/OxFengyuan/Awesome-Papers)', '',
            '按研究方向、具体任务和会议属性组织的精选长文论文库。' if chinese else 'A curated library of full-length papers, organized by research area, task, and conference attributes.',
            '', '## 收录范围' if chinese else '## Scope','',
            '涵盖 2017–2026 年 ICML、ICLR、ACL、EMNLP、NeurIPS、AAAI 的长文。' if chinese else
            'Covers full-length papers from ICML, ICLR, ACL, EMNLP, NeurIPS, and AAAI, 2017–2026.',
            '', '- **精选论文**：Main 中的 Best、Outstanding、Oral，以及符合相同条件的 NeurIPS Datasets / Benchmarks / Evaluations track 论文。' if chinese else
            '- **Curated papers**: Best, Outstanding, and Oral papers from Main, plus papers meeting the same criteria from the NeurIPS Datasets / Benchmarks / Evaluations tracks.',
            '- **AI for Finance**：上述会议 Main 和 Findings 中的金融相关长文，不限奖项或展示形式；Main 与 Findings 分别浏览。Findings 仅收录金融相关论文。' if chinese else
            '- **AI for Finance**: finance-related full-length papers from Main and Findings, regardless of awards or presentation. Main and Findings have separate catalogs; Findings is included only for finance.',
            '', '不收录短文、Workshop、Demo、Industry、Journal-to-Conference 和独立 Position track 论文。' if chinese else
            'Short papers, Workshops, Demos, Industry, Journal-to-Conference, and standalone Position tracks are excluded.',
            '', '## 浏览' if chinese else '## Browse','',
            '- [All papers / 全部论文](indexes/all_papers.md) · [Excel](catalog.xlsx) · [CSV](catalog.csv) · [JSONL](catalog.jsonl)',
            '- [Best](indexes/best_papers.md) · [Outstanding](indexes/outstanding_papers.md) · [Oral](indexes/oral_papers.md)',
            '- [AAAI](indexes/venues/AAAI.md) · [NeurIPS Datasets / Benchmarks / Evaluations](indexes/neurips_datasets_benchmarks.md)',
            '- [Finance Main](finance/main/README.md) · [Main CSV](finance/main/catalog.csv) · [Main Excel](finance/main/catalog.xlsx)',
            '- [Finance Findings](finance/findings/README.md) · [Findings CSV](finance/findings/catalog.csv) · [Findings Excel](finance/findings/catalog.xlsx)',
            '- [PDF folders / 分类目录](pdfs/README.md) · [Missing PDFs / 缺失 PDF](checks/missing_pdfs.csv)',
            '', '## 总览' if chinese else '## Overview','', '| Collection / 类别 | Papers / 篇数 |','|---|---:|',
            *[f'| {label} | {summary[key]} |' for key,label in [('papers','All / 总数'),('curated','Best / Outstanding / Oral'),('finance_main','Finance Main'),('finance_findings','Finance Findings'),('best','Best'),('outstanding','Outstanding'),('oral','Oral'),('local_pdfs','Local PDFs / 本地正文'),('missing_pdf_records','Missing local PDFs / 暂缺本地正文'),('leaf_folders','Fine topic folders / 细分目录')]],
            '', '奖项、展示形式和金融标签可重叠；总数按论文 ID 去重，跨主题计数也可重叠。' if chinese else
            'Award, presentation, and finance labels can overlap. The total counts unique paper IDs; cross-topic counts can also overlap.',
            '', '## 研究方向' if chinese else '## Research areas','', '| Topic / 主题 | Papers / 篇数 |','|---|---:|']
        for ident,topic in topics.items():
            group=[r for r in rows if ident in r['research_topic_ids'].split('; ')]
            if group:lines.append(f"| [{topic['label']}](indexes/research_topics/{ident}.md) | {len(group)} |")
        lines+=['','## 金融任务' if chinese else '## Financial tasks','', '| Task / 任务 | Main | Findings |','|---|---:|---:|']
        for ident,topic in fin_topics.items():
            main=sum(r['track']=='main' and ident in r['finance_topic_ids'].split('; ') for r in rows)
            findings=sum(r['track']=='findings' and ident in r['finance_topic_ids'].split('; ') for r in rows)
            lines.append(f"| {topic['label']} | [{main}](finance/main/topics/{ident}.md) | [{findings}](finance/findings/topics/{ident}.md) |")
        lines+=['','## 目录与标签' if chinese else '## Storage and labels','',
            'PDF 按 track、研究主题、子方向和细分任务存放。文件名标明年份、会议、Long、Main／Findings、Best／Outstanding／Oral 等标签；每个目录附论文索引。' if chinese else
            'PDFs are organized by track, research topic, subtopic, and task. Filenames show year, venue, Long, Main/Findings, and Best/Outstanding/Oral labels. Each folder includes a paper index.',
            '', '作者 arXiv 版本在目录中单独标注；暂缺 PDF 的论文保留在线链接。' if chinese else
            'Author arXiv versions are labeled in the catalog; papers without a local PDF retain online links.']
        exporter.text(path,'\n'.join(lines))


def write_evidence_notes(exporter):
    exporter.text('checks/README.md', '''# Evidence and maintenance / 核验与维护

Current scope and file/link checks / 当前范围与文件校验：[current_validation.json](current_validation.json)。
Finance reference reconciliation / 金融参考库核对：[finance_reconciliation/README.md](finance_reconciliation/README.md)。

## Eligibility and coverage / 类型与覆盖

长文类型依据官方卷册、程序标记、完整论文 track 或正文边界证据，不按 PDF 总页数推断。无法核验的类型暂不纳入正式清单；未知类型不等于短文。候选及排除原因见 [scope_revision/excluded_or_pending.json](scope_revision/excluded_or_pending.json)。

Full-paper eligibility uses official volumes, programme labels, full-paper tracks, or inspected main-text boundaries, rather than total PDF pages. Unverified types are withheld, not assumed to be short papers. Pending and excluded records are retained in [scope_revision/](scope_revision/).

当前来源快照已恢复 AAAI 2025、2026 官方 Main Oral 程序，其他年份及 ICLR 2020、部分线上会议的程序覆盖仍有缺口。奖项、展示形式和长文类型均保留逐篇证据。

The current snapshot recovers official AAAI Main Oral programmes for 2025 and 2026. Other years, ICLR 2020, and some virtual programmes retain coverage gaps. Awards, presentation, and paper type have per-paper evidence.

## Classification and files / 分类与文件

分类基于题名、摘要、金融证据及按 ID 的人工修订，并非逐篇全文精读或官方领域标签。金融 PDF 优先复用本地参考库。超过 100 条的综合分类按会议和年份细分。

Labels use titles, abstracts, financial evidence, and ID-based reviewed corrections; they do not imply full-text review or official conference area labels. Existing local finance PDFs are reused. Residual categories above 100 records are grouped by venue/year.

压缩全文缓存按 `finance_expansion/pdf_texts/<venue>/<year>/` 存放，以满足托管平台单目录文件数量限制。来源缓存和历史审计属于处理证据，不是正式收录清单。

Compressed full-text caches use `finance_expansion/pdf_texts/<venue>/<year>/` to stay within hosting directory limits. Source caches and historical audits are provenance, not admitted papers.

## Rebuild and verify / 重建与校验

Run from the repository root / 在仓库根目录执行：

```bash
python -m pip install -r scripts/requirements.txt
python scripts/build_library.py
python scripts/verify_curated_library.py
```

## Historical records / 历史记录

首次范围迁移将被排除的原 PDF 和旧索引保存到本地 `.git/curated_scope_archive/`，原 Git 历史保留在本地备份引用中。此前的 finance_expansion、validation_summary、root_layout_validation 等报告属于历史快照，不代表当前收录数量。

The initial scope migration archives excluded original PDFs and prior indexes locally in `.git/curated_scope_archive/`; prior Git history remains in local backup refs. Earlier finance_expansion, validation_summary, and root_layout_validation reports are historical snapshots, not current collection counts.
''')


if __name__=='__main__':run()
