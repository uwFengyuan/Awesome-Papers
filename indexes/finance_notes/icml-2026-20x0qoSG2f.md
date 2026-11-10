# SpreadsheetArena: Decomposing Preference in LLM Generation of Spreadsheet Workbooks

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Expert evaluations of spreadsheets for finance prompts suggest that even highly ranked models do not reliably produce spreadsheets aligned with domain-specific best practices.

[Paper](https://openreview.net/forum?id=20x0qoSG2f)

Classification / 分类：Document AI / 票据、财报与图表理解 → Financial Tables & Spreadsheets / 财务表格与电子表格 → General / 综合

## Abstract / 摘要

We consider the task of end-to-end **spreadsheet generation**, where language models are prompted to produce spreadsheet artifacts to satisfy users' explicit and implicit constraints, specified in natural language.  We introduce **SpreadsheetArena**, a platform for evaluating models' performance on the task via blind pairwise evaluations of LLM-generated spreadsheet workbooks. As with other complex, open-ended tasks, relevant evaluation criteria can vary greatly across use cases and prompts, often in ways that are difficult to formalize. Compared to general dialogue or text generation settings, spreadsheet generation presents unique challenges and opportunities: the task output structure is well-defined and multi-dimensional, and there are often complex interactivity and layout considerations. We observe that stylistic, structural, and functional features of preferred spreadsheets vary meaningfully across prompts. Expert evaluations of spreadsheets for finance prompts suggest that even highly ranked models do not reliably produce spreadsheets aligned with domain-specific best practices. We host a live arena and release a dataset of prompts, generated spreadsheets, and preference votes, which we hope will facilitate further study of tasks operating over spreadsheets as a challenging and interesting class of complex, open-ended tasks for LLMs.
