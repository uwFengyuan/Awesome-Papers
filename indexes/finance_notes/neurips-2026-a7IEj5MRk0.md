# The SEC Filings Dataset: Reconstructing U.S. Corporate and Financial Disclosures into Layout-Faithful and Token-Efficient Pretraining Data

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We introduce the Stanford EDGAR Filings Dataset (SFD), an open reconstruction of SEC filings into layout-faithful MultiMarkdown for financial language modeling and evaluation. / SFD makes audited financial statements, risk disclosures, ownership reports, accounting notes, and market-moving event filings usable as long-context pretraining data and as a basis for financial reasoning, forecasting, compliance, and document understanding. / We further introduce two SFD-derived benchmarks: EDGAR-Forecast, which evaluates filing-grounded numerical forecasting after model knowledge cutoffs, and EDGAR-OCR, which evaluates transcription of complex financial tables.

[Paper](https://openreview.net/forum?id=a7IEj5MRk0)

Classification / 分类：Document AI / 票据、财报与图表理解 → Report Layout & Structured Extraction / 财报版面与结构提取 → General / 综合

## Abstract / 摘要

As high-quality public web corpora become increasingly exhausted, clean long-context documents have become a scarce and expensive source of training data for large language models (LLMs). Existing long-context corpora are often proprietary and costly to acquire, synthetically generated, or concentrated in narrow domains such as programming. We introduce the Stanford EDGAR Filings Dataset (SFD), an open reconstruction of SEC filings into layout-faithful MultiMarkdown for financial language modeling and evaluation. SFD makes audited financial statements, risk disclosures, ownership reports, accounting notes, and market-moving event filings usable as long-context pretraining data and as a basis for financial reasoning, forecasting, compliance, and document understanding. The resulting corpus is token-efficient, model-ready, and has less than 0.1\% overlap with Common Crawl-derived corpora. We release SFD-v1, a 152B-token snapshot of a larger 18.4M-filing corpus estimated at 500B tokens. We further introduce two SFD-derived benchmarks: EDGAR-Forecast, which evaluates filing-grounded numerical forecasting after model knowledge cutoffs, and EDGAR-OCR, which evaluates transcription of complex financial tables.
