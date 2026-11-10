# 金融相关论文扩充审计

范围：2017 年至当前快照，ICML、ICLR、ACL、EMNLP、NeurIPS 的全部 main。**金融收录不依赖 Best / Oral；普通 Poster 同样纳入。** Findings、Workshop、Industry、Demo、独立 Position / Datasets / Evaluations 等 track 排除。

本次从 85,756 条主会记录重新筛查，取得 85,675 条摘要；金融清单由 344 篇扩充为 **1178 篇**，新增 834 篇。其中 200 篇为金融核心问题，978 篇为通用方法中的金融数据、金融实验、金融案例、相关理论或金融任务综述。916 篇没有 Oral 或获奖标签。

题名摘要扩展筛查产生 2,292 个宽松候选；随后对已有资料及额外检索的 11,066 篇 PDF 进行正文机器检索，人工复核具体金融证据。机器检索不等于逐篇完整阅读。另有 410 篇通用方法的复核队列正文暂未取得，不能把它们直接认定为金融或非金融论文。

## 金融相关的判断

- `core`：金融市场、投资与交易、信贷与保险、金融安全、金融文档、企业披露与 ESG 等明确金融问题。

- `application`：有具体金融数据、任务、业务案例或金融场景建模；也保留与金融任务有实质关联的综述。研究主方向可能是通用机器学习或 NLP，不能把这些论文都称为金融专用方法。

- 经费、算力花费、作者的金融机构名称、参考文献中的金融论文、词义示例，以及借用 portfolio / Hedge / credit 名词，都不能单独建立金融相关性。FinGPT/FinBERT 的芬兰语版本、DP privacy accountant、FinFET、医学 FinAl、非金融 ESG 缩写已作歧义处理。

- M4 官方元数据有 24,534 条 Finance 序列，分布在 Yearly / Quarterly / Monthly / Weekly / Daily；Hourly 没有 Finance 序列。只把已确认使用相应金融相关子集的实验纳入，具体来源见 [核验记录](m4_financial_domain_provenance.json)。

## 输出与逐条证据

- [金融 Excel](../../finance_catalog.xlsx)、[金融 CSV](../../finance_catalog.csv)、[金融 BibTeX](../../finance_references.bib)、[主题索引与论文笔记](../../indexes/ai_for_finance.md)。

- [50 个会议年份的金融覆盖](coverage.csv)、[全部题名摘要候选的处置](all_candidate_dispositions.csv)、[待取得全文的金融关键词候选](pending_finance.csv)。

- [人工纳入决策](manual_decisions.json)、[原有 PDF 的正文复核](pdf_decisions.json)、[额外全文与数据集别名复核](supplementary_decisions.json)、[最终补查复核](final_decisions.json)。原始队列冻结，哈希记录在决策文件中，ID 用于关联。

- [额外全文复核队列中尚未取得的文件](fulltext_not_available.csv)；这是通用方法复核队列，不是已确认金融论文的缺失列表。已确认金融论文的下载状态以金融总表为准。

- 筛查中间 PDF 已按 [清理清单](review_cache_cleanup.json) 移除；收录论文的正文保留在正式 `pdfs/` 目录，全文检索缓存、下载记录和校验值保留供追溯。

- NeurIPS 2026 全 track 导出中的金融关键词候选，另有 18 条已明确属于非 main track，16 条尚未核验 track；见 [逐条分类](track_dispositions.json)。未确认 main 的项目不混入正式金融总表。

## 覆盖限制

收集目标是覆盖全部主会金融相关论文；当前公开来源与正文可得性仍有限制，因此不宣称零遗漏。未取得全文时，可能漏掉题名摘要没有披露的金融实验；NeurIPS 2026 的部分 track 记录还待核验。所有缺口保留清单，后续可以在同一目录继续补全。
