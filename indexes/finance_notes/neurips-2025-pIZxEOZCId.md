# TabDPT: Scaling Tabular Foundation Models on Real Data

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：g. Other or not provided SGEMM_GPU_kernel_ 44069 241600 9 2.4M 0.0 Reg. Computing performance 44089 credit 16714 10 184K 0.0 Class. Financial/demographic 44122 pol 10082 26 272K 0.0 Class. Industrial/operational 44136 wine_quality 6497 11 78K 0.0 Reg. Human behaviour 44137 Ailerons 13750 33 468K 0.0 Reg. Other or not provided 44145 sulfur 10081 6 71K 0.0 Reg. Other science 45020 default-of-credit-card-clients 13272 20 279K 0.0 Class. Financial/demographic 45022 Diabetes130US 71090 7 569K 0.0 Class. Medical/human sensor 45026 heloc 10000 22 230K 0.0 Class. Financial/demographic 45032 yprop_4_1 8885 42 382K 0.0 Reg. Medical/human sensor 45038 road-safety 111762 32 3.7M 0.0 Class. Human behaviour 45039 compas-two-years 4966 1

[Paper](https://openreview.net/forum?id=pIZxEOZCId)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Tabular data is one of the most ubiquitous sources of information worldwide, spanning a wide variety of domains. This inherent heterogeneity has slowed the development of Tabular Foundation Models (TFMs) capable of fast generalization to unseen datasets. In-Context Learning (ICL) has recently emerged as a promising solution for TFMs, enabling dynamic adaptation to new tasks without additional tuning. While many studies have attempted to re-purpose large language models for tabular ICL, they have had limited success, so recent works have focused on developing tabular-specific foundation models. In this work, we propose an approach to combine ICL-based retrieval with self supervised learning to train tabular foundation models. We also investigate the utility of real vs. synthetic data for model pre-training, and show that real data can contain useful signal not easily captured in synthetic training. Specifically, we show that incorporating real data during the pre-training phase can lead to significantly faster training and better downstream generalization to unseen data. Our resulting model, **TabDPT**, achieves strong performance on both regression (CTR23) and classification (CC18) benchmarks. Importantly, we also demonstrate that with our pre-training procedure, scaling both model and data size leads to consistent performance improvements that follow power laws. This echoes scaling laws in LLMs and other foundation models, and suggests that large-scale TFMs can be achievable. We open-source our full pipeline: inference code including trained model weights can be found [here](https://github.com/layer6ai-labs/TabDPT-inference), and the training code to reproduce experiments can be found [here](https://github.com/layer6ai-labs/TabDPT-training).
