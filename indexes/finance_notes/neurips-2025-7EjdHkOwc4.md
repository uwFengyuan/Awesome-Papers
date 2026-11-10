# PANGEA: Projection-Based Augmentation with Non-Relevant General Data for Enhanced Domain Adaptation in LLMs

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Our extensive experiments on domain-specific benchmarks, including GSM8K, MedQA, and FinQA, as well as a custom domain-specific language task, validate the effectiveness of our approach.

[Paper](https://openreview.net/forum?id=7EjdHkOwc4)

Classification / 分类：Financial QA & Reasoning / 金融问答与数值推理 → Numerical & Table Reasoning / 数值与表格推理 → General / 综合

## Abstract / 摘要

Modern large language models (LLMs) achieve competitive performance across a wide range of natural language processing tasks through zero-shot or few-shot prompting. However, domain-specific tasks often still require fine-tuning, which is frequently hindered by data scarcity, i.e., collecting sufficient domain-specific data remains a practical challenge. A widely adopted solution is to generate synthetic data using LLMs by augmenting a small set of available domain-specific examples. In this work, we first identify fundamental limitations of such approach in terms of both data diversity and quality, particularly when relying on only a handful of domain-specific examples. We then propose our method, PANGEA, which leverages large-scale, publicly available general-purpose data---entirely unrelated to the target domain---to generate more diverse and higher-quality synthetic data. Our extensive experiments on domain-specific benchmarks, including GSM8K, MedQA, and FinQA, as well as a custom domain-specific language task, validate the effectiveness of our approach.
