# Finance reconciliation / 金融论文核对

参考库：`/home/qi/aiagent/Awesome-AI4Finance-Papers`。来源清单及 SHA-256 见 [source_manifest.json](source_manifest.json)。两库按逐篇证据修正；PDF 均复用本地文件，没有重新下载。

| Collection | Reference | Awesome-Papers |
|---|---:|---:|
| main | 1310 | 1310 |
| findings | 187 | 187 |

共同记录：1497；参考库已收录但本库缺失：0；本库额外收录：0。

## 核对结果 / Results

初始差异：缺少 3 篇 Findings，多出 4 篇 Main 和 6 篇 Findings。逐篇依据见 [decisions.json](decisions.json)。

- 缺少的 3 篇已依据出版 PDF 的正文和身份信息补入 Findings。
- 7 篇的旧长文证明计入了致谢或 Limitations，已转入待核验；这不等于已确认是短文。
- 同步参考库 187 篇 Findings 的人工金融分类修订（含本次补回的综述）；原始分类差异见 [initial_annotation_differences.csv](initial_annotation_differences.csv)。
- 另有 3 篇在 PDF 第六页及之后仍有正文；参考库把正文中换行的 Appendix 引用、表格列标题或图标签当作章节边界。本库保留，参考库同步补回，并将人工边界证据与 PDF SHA-256 绑定。

## 参考库纠正 / Reference corrections

- [2023.emnlp-main.111: Augmenting Zero-Shot Dense Retrievers with Plug-in Mixture-of-Memories](https://aclanthology.org/2023.emnlp-main.111/) — Page 6 contains BEIR results and analysis, followed by further main sections. The reference parser matched the inline sentence "Appendix A.4" split across lines on page 5; actual Limitations starts on page 10.
- [2026.emnlp-main.2572: Multimodal Collaborative Debate for Zero-Shot Time Series Reasoning](https://aclanthology.org/2026.emnlp-main.2572/) — Page 6 contains the TS-Debate synthesis method and section 4 Experiments. A figure label Limitations on page 1 is not the actual Limitations section on page 9.
- [2025.findings-emnlp.972: Large Language Model Agents in Finance: A Survey Bridging Research, Practice, and Real-World Deployment](https://aclanthology.org/2025.findings-emnlp.972/) — Page 6 contains Table 3 and the Financial QA discussion. Limitations on page 3 is a table column label; the actual Limitations section starts on page 10.

## 差异表与校验 / Evidence

- [缺失记录](missing_in_library.csv) · [额外记录](only_in_library.csv) · [初始缺失](initial_missing.csv) · [初始额外](initial_extra.csv)
- [身份、轨道和长文标签差异](metadata_differences.csv) · [金融分类标签差异](annotation_differences.csv) · [PDF 版本或下载状态差异](pdf_differences.csv)
- 两库均暂无本地正文的论文：50 篇；[状态标签对照](download_status_labels.csv)仅记录 not_available_locally 与 access_blocked 等粒度差异，不表示文件或收录不一致。
- 已对两库 2894 个金融 PDF 路径重新计算 SHA-256，完整性问题 0 个。

当前共有 0 篇存在金融分类标签差异。分类属于两库各自的注释，不用于判断是否漏收；身份、Main/Findings、金融相关性及正文版本分别核对。

覆盖一致仅指参考库当前已正式收录的长文清单；参考库自身未完成的全文筛查或长文类型核验不据此视为已穷尽。

[Machine-readable summary](summary.json)
