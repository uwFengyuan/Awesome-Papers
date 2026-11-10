"""Render the README finance overview from the existing taxonomy and counts."""
import csv
import json
from pathlib import Path

START = '<!-- finance-overview:start -->'
END = '<!-- finance-overview:end -->'


def render_finance_overview(root, topic_stats=None):
    base = root/'checks/finance_taxonomy'
    schema = json.loads((base/'schema.json').read_text())
    summary = json.loads((base/'summary.json').read_text())
    if topic_stats is None:
        with (base/'topic_counts.csv').open(encoding='utf-8-sig', newline='') as f:
            topic_stats = list(csv.DictReader(f))
    lines = [START, '## AI for Finance 分类总览', '',
        f"当前 {summary['finance_papers']:,} 篇金融相关论文按 **{len(schema['topics'])} 个主题、{len(schema['subtopics'])} 个子方向**整理，另有 **{len(schema['methods'])} 类技术方法标签**。点击主题查看论文、证据笔记和 PDF；CSV 可单独下载筛选。", '',
        '主题采用多标签，一篇论文可同时属于多个方向，因此下表篇数不能相加。每篇另有一个主方向；`core` 为金融核心研究，`application` 为通用方法中的金融数据、任务或案例应用。', '',
        '| 主题与论文索引 | 篇数 | 金融核心 | 金融应用 | 主要子方向 | 分类数据 |',
        '|---|---:|---:|---:|---|---|']
    for row in topic_stats:
        ident = row['topic_id']
        subtopics = [s['label'].split(' / ', 1)[-1] for s in schema['subtopics'] if s['parent_id'] == ident]
        detail = '、'.join(subtopics[:4])
        if len(subtopics) > 4:
            detail += '等'
        if not detail:
            detail = '金融相关性已确认、具体任务待细分的应用'
        lines.append(f"| [{row['topic']}](indexes/finance_topics/{ident}.md) | {row['papers']} | {row['core']} | {row['application']} | {detail} | [CSV](indexes/finance_topics/{ident}.csv) |")
    lines += ['',
        '**按技术方法交叉筛选：**语言模型与 LLM、强化学习、图学习、扩散与流模型、因果学习、公平性与算法追索、隐私与联邦学习等，与金融任务分列。', '',
        '[金融 Excel](finance_catalog.xlsx) 的 `Topics`、`Subtopics`、`Methods` 工作表提供统计，各主题有独立工作表；`Confirmed Finance` 可按主方向、主题、子方向和技术方法筛选。', '',
        '[完整主题索引](indexes/ai_for_finance.md) · [分类定义与使用说明](indexes/finance_taxonomy.md) · [金融时间序列索引](indexes/financial_time_series.md) · [覆盖缺口与待补项](checks/finance_expansion/README.md)',
        END]
    return '\n'.join(lines)


if __name__ == '__main__':
    root = Path(__file__).resolve().parents[1]
    path = root/'README.md'
    text = path.read_text()
    overview = render_finance_overview(root)
    if START in text:
        start, end = text.index(START), text.index(END) + len(END)
        text = text[:start] + overview + text[end:]
    else:
        anchor = '## 覆盖边界与待补项'
        assert text.count(anchor) == 1
        text = text.replace(anchor, overview + '\n\n' + anchor)
    path.write_text(text)
    print('README finance overview updated from taxonomy statistics.')
