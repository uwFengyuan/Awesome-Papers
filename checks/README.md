# Evidence and maintenance / 核验与维护

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
