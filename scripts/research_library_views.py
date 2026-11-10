"""Research-topic indexes and README overview shared by all library categories."""
import csv
import json
from collections import Counter
from urllib.parse import quote

def clean(s):return str(s or '').replace('|','\\|').replace('\n',' ')

def build_research_views(root,rows,assignments):
    dest=root/'checks/research_taxonomy'
    schema=json.loads((dest/'schema.json').read_text())
    summary=json.loads((dest/'summary.json').read_text())
    subtopics={x['id']:x for x in schema['subtopics']}
    topics={x['id']:x for x in schema['topics']}
    folder=root/'indexes/research_topics';folder.mkdir(exist_ok=True)
    keys=['id','title','authors','venue','year','research_primary_topic','research_topics','research_subtopics',
        'is_best_or_outstanding','awards_original','is_oral','finance_scope','finance_primary_topic',
        'paper_url','local_path','pdf_version','download_status','research_review_status']
    def writecsv(path,data,fields):
        with path.open('w',encoding='utf-8-sig',newline='') as f:
            w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(data)
    def rowlink(row,prefix='../../'):
        return f"[PDF]({prefix}{quote(row['local_path'],safe='/._-')})" if row['local_path'] else f"[在线]({row['paper_url']})"
    stats=[]
    for ident,topic in topics.items():
        group=[r for r in rows if ident in assignments[r['id']]['topic_ids']]
        stat=dict(topic_id=ident,topic=topic['label'],papers=len(group),
            primary_papers=sum(assignments[r['id']]['primary_topic_id']==ident for r in group),
            best_or_outstanding=sum(r['is_best_or_outstanding'] for r in group),
            oral=sum(r['is_oral'] for r in group),
            finance=sum(bool(r['finance_scope']) for r in group),
            nonfinance=sum(not r['finance_scope'] for r in group),
            pdfs=sum(r['download_status']=='downloaded' for r in group),definition=topic['description'])
        stats.append(stat)
        writecsv(folder/f'{ident}.csv',group,keys)
        lines=[f"# {topic['label']}\n\n{topic['description']}\n\n共 {len(group):,} 篇，含 Best / Outstanding 主奖 {stat['best_or_outstanding']} 篇、Oral {stat['oral']} 篇；不同收录类别和研究主题均可能重叠。\n",
            f'[全部研究方向](../research_topics.md) · [分类说明](../research_taxonomy.md) · [本方向 CSV]({ident}.csv) · [Excel 总表](../../catalog.xlsx)\n',
            '| 子方向 | 篇数 |','|---|---:|']
        children=[s for s in schema['subtopics'] if s['parent_id']==ident]
        for child in children:
            lines.append(f"| {child['label']} | {sum(child['id'] in assignments[r['id']]['subtopic_ids'] for r in group)} |")
        if ident=='finance':lines.append('\n金融任务的进一步细分见 [AI for Finance](../ai_for_finance.md)，包括 Alpha Mining、Time Series 等23类。\n')
        lines.extend(['\n| 年份 | 会议 | 论文 | 主方向 | 本类子方向 | 收录标签 | 文件 |','|---|---|---|---|---|---|---|'])
        for r in group:
            a=assignments[r['id']]
            childlabels='；'.join(subtopics[s]['label'] for s in a['subtopic_ids'] if subtopics[s]['parent_id']==ident)
            tags=[]
            if r['is_best_or_outstanding']:tags.append('Best / Outstanding')
            elif r['awards_original']:tags.append('主会奖项')
            if r['is_oral']:tags.append('Oral')
            if r['oral_candidate_unverified']:tags.append('Oral 候选待核验')
            if r['finance_scope']:tags.append('Finance '+r['finance_scope'])
            lines.append(f"| {r['year']} | {r['venue']} | [{clean(r['title'])}]({r['paper_url']}) | {clean(r['research_primary_topic'])} | {clean(childlabels)} | {'；'.join(tags)} | {rowlink(r)} |")
        (folder/f'{ident}.md').write_text('\n'.join(lines)+'\n')
    writecsv(dest/'topic_counts.csv',stats,list(stats[0]))
    childstats=[dict(topic_id=s['parent_id'],topic=topics[s['parent_id']]['label'],subtopic_id=s['id'],subtopic=s['label'],
        papers=sum(s['id'] in a['subtopic_ids'] for a in assignments.values())) for s in schema['subtopics']]
    writecsv(dest/'subtopic_counts.csv',childstats,list(childstats[0]))
    pending=[dict(id=r['id'],title=r['title'],venue=r['venue'],year=r['year'],
        research_primary_topic=r['research_primary_topic'],status=r['research_review_status'],paper_url=r['paper_url'])
        for r in rows if r['research_review_status']=='needs_review']
    writecsv(dest/'pending_review.csv',pending,['id','title','venue','year','research_primary_topic','status','paper_url'])
    lines=[f'# 全库研究方向总览\n\n分类范围为当前资料库的 **{len(rows):,} 篇**论文，包括 Best / Outstanding、其他主会奖项、Oral、已确认金融论文及明确标注的候选。研究方向覆盖全部收录记录，包含 {sum(not r["finance_scope"] for r in rows):,} 篇非金融论文。\n',
        '每篇有一个主方向和可重叠的主题、子方向。各主题篇数不能相加；主方向计数合计为论文总数。标签依据题名和官方摘要辅助生成，并保留匹配证据及人工修订，不是会议官方分区。\n',
        '[Excel 总表](../catalog.xlsx) · [CSV 总表](../catalog.csv) · [分类说明](research_taxonomy.md) · [细粒度金融索引](ai_for_finance.md)\n',
        '| 研究方向 | 篇数 | 主方向 | Best / Outstanding | Oral | 金融相关 | 分类数据 |','|---|---:|---:|---:|---:|---:|---|']
    for s in stats:
        lines.append(f"| [{s['topic']}](research_topics/{s['topic_id']}.md) | {s['papers']} | {s['primary_papers']} | {s['best_or_outstanding']} | {s['oral']} | {s['finance']} | [CSV](research_topics/{s['topic_id']}.csv) |")
    (root/'indexes/research_topics.md').write_text('\n'.join(lines)+'\n')
    guide=[f'# 全库研究分类说明\n\n版本 {schema["version"]}；覆盖 {len(rows):,} 篇当前收录论文，其中 {summary["abstracts_available"]:,} 篇有官方摘要。\n',
        '- `research_primary_topic`：用于单一归档的主方向；每篇恰有一个。\n',
        '- `research_topics` / `research_topic_ids`：多个研究主题及稳定标识，支持交叉筛选。\n',
        '- `research_subtopics`：具体任务或技术方向。\n',
        '- `research_review_status`：元数据规则分类、已人工复核元数据，或待进一步复核。\n',
        '- 分类规则使用题名和官方摘要，匹配片段保存在 [逐篇分类证据](../checks/research_taxonomy/assignments.json)。主要按题名中明确的任务和方法确定主方向，允许保留交叉领域标签。不是逐篇全文精读，也不声称与作者或会议的领域标签完全一致。\n',
        '- 金融标签仅沿用已确认的金融清单，不因摘要出现 finance 重新扩大收录；金融主题分类仍使用独立的23类任务体系。金融核心论文以 Finance 为主方向，金融应用论文通常以具体方法或任务为主方向。\n',
        '- Best / Oral 是收录和展示属性，研究方向是另一个维度。Spotlight、候选 Oral、不同主会奖项的原有区分保留。\n',
        f'- 当前有 {len(pending)} 条需要进一步细化或补充元数据的记录，见 [待复核列表](../checks/research_taxonomy/pending_review.csv)。分类规则和按ID保存的人工修订可继续更新。\n',
        '[方向总览](research_topics.md) · [分类定义](../checks/research_taxonomy/schema.json) · [人工修订](../checks/research_taxonomy/manual_overrides.json)\n']
    for ident,topic in topics.items():
        guide.append(f"## [{topic['label']}](research_topics/{ident}.md)\n\n{topic['description']}\n")
        guide.extend('- '+s['label']+'\n' for s in schema['subtopics'] if s['parent_id']==ident)
    (root/'indexes/research_taxonomy.md').write_text('\n'.join(guide))
    return stats,childstats

def render_research_overview(root,stats):
    summary=json.loads((root/'checks/research_taxonomy/summary.json').read_text())
    schema=json.loads((root/'checks/research_taxonomy/schema.json').read_text())
    lines=['<!-- research-overview:start -->','## 全库研究方向总览','',
        f"**全部 {summary['papers']:,} 篇收录论文**均已加入研究方向标签，覆盖 Best / Outstanding、其他主会奖项、Oral 和金融论文。共 {len(schema['topics'])} 个主题、{len(schema['subtopics'])} 个子方向；支持一个主方向和多个主题。",'',
        '分类依据题名、官方摘要与保留的修订记录。主题可能重叠，不能把各行篇数相加；主方向篇数合计等于全库篇数。', '',
        '| 研究方向与索引 | 篇数 | 主方向 | Best / Outstanding | Oral | 分类数据 |','|---|---:|---:|---:|---:|---|']
    for s in stats:
        i=s['topic_id'];lines.append(f"| [{s['topic']}](indexes/research_topics/{i}.md) | {s['papers']} | {s['primary_papers']} | {s['best_or_outstanding']} | {s['oral']} | [CSV](indexes/research_topics/{i}.csv) |")
    lines += ['', '[全库分类详细总览](indexes/research_topics.md) · [分类口径与待复核项](indexes/research_taxonomy.md) · [Excel 总表](catalog.xlsx)', '',
        'Excel 的 `Research Topics`、`Research Subtopics` 提供分类统计；在 `All Papers` 中可按 `research_primary_topic`、`research_topics`、`research_subtopics` 和 Best / Oral 标签交叉筛选。金融任务的进一步细分类见下表。',
        '<!-- research-overview:end -->']
    return '\n'.join(lines)
