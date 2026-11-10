# Adaptive Test Case Discovery for LLM-Assisted Decision Making in High-Stakes Domains

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We evaluate the method across several LLM-assisted decision-making tasks: bank loan approval, stock prediction from news articles, and disaster resource allocation from tweets and images.

[Paper](https://openreview.net/forum?id=vWITPJYgBo)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Large language models (LLMs) are increasingly used for assistive decision-making in high-stakes domains, yet their outputs can be unreliable and difficult to audit. This necessitates pre-deployment testing, which can be used to identify scenarios where an LLM-assisted pipeline fails to produce satisfactory decisions. Existing testing strategies are often not sample-efficient and struggle to adapt to diverse testing objectives, application domains, and rapidly evolving models. We introduce a sample-efficient scenario design strategy for testing LLM-based decision-making pipelines. Our approach formulates testing as adaptive experimental design, using a flow-based surrogate model to sequentially acquire scenarios that balance optimization to discover challenging test cases with diverse exploration. We evaluate the method across several LLM-assisted decision-making tasks: bank loan approval, stock prediction from news articles, and disaster resource allocation from tweets and images. Our approach consistently discovers challenging scenarios that satisfy the testing objective across all tasks, providing high coverage over scenario space.
