# Document Summarization with Conformal Importance Guarantees

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：stractive summarization with an LLM to our hybrid extractive-abstractive approach. 4.1 Datasets We use 5 datasets to evaluate the performance of our framework: ECTSum [46] contains complete transcripts from corporate earnings calls, as well as expert-curated extractive summaries at the sentence level; CSDS [40] is a dataset of Chinese language customer-client conversations. Although the summaries are abstractive, each conversation has sentence-level labels for use as an extractive benchmark; CNN/DM [32] covers news sourced from CNN and The Daily Mail with human-written summa

[Paper](https://openreview.net/forum?id=w1Y7RZC3QT)

Classification / 分类：Corporate Finance & Accounting / 公司金融与会计 → Earnings & Corporate Disclosures / 盈利与公司披露 → General / 综合

## Abstract / 摘要

Automatic summarization systems have advanced rapidly with large language models (LLMs), yet they still lack reliable guarantees on inclusion of critical content in high-stakes domains like healthcare, law, and finance. In this work, we introduce Conformal Importance Summarization, the first framework for importance-preserving summary generation which uses conformal prediction to provide rigorous, distribution-free coverage guarantees. By calibrating thresholds on sentence-level importance scores, we enable extractive document summarization with user-specified coverage and recall rates over critical content. Our method is model-agnostic, requires only a small calibration set, and seamlessly integrates with existing black-box LLMs. Experiments on established summarization benchmarks demonstrate that Conformal Importance Summarization achieves the theoretically assured information coverage rate. Our work suggests that Conformal Importance Summarization can be combined with existing techniques to achieve reliable, controllable automatic summarization, paving the way for safer deployment of AI summarization tools in critical applications. Code is available at github.com/layer6ai-labs/conformal-importance-summarization.
