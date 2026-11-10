# TS-RAG: Retrieval-Augmented Generation based Time Series Foundation Models are Stronger Zero-Shot Forecaster

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：.1711 0.1912 — — 0.1897 0.2107 Electricity 0.1120 0.2002 0.1132 0.2004 0.1967 0.3028 0.1715 0.2643 0.1832 0.2814 — — 0.1460 0.2237 Exchange rate 0.0627 0.1718 0.0673 0.1780 0.0979 0.2059 0.0657 0.1725 0.0663 0.1720 0.0695 0.1802 0.0831 0.1879 of 5 million data points to construct the multi-domain retrieval knowledge base. To facilitate efficient indexing and retrieval, both the pretraining dataset and the retrieval knowledge base are segmented using a predefined context window. This process results in a total of 26 mill

[Paper](https://openreview.net/forum?id=PymOnHw4Ty)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Large Language Models (LLMs) and Foundation Models (FMs) have recently become prevalent for time series forecasting tasks. While fine-tuning LLMs enables domain adaptation, they often struggle to generalize across diverse and unseen datasets. Moreover, existing Time Series Foundation Models (TSFMs) still face challenges in handling non-stationary dynamics and distribution shifts, largely due to the lack of effective mechanisms for adaptation. To this end, we present TS-RAG, a retrieval-augmented generation framework for time series forecasting that enhances the generalization and interpretability of TSFMs. Specifically, TS-RAG leverages pre-trained time series encoders to retrieve semantically relevant segments from a dedicated knowledge base, enriching the contextual representation of the input query. Furthermore, we propose an Adaptive Retrieval Mixer (ARM) module that dynamically fuses the retrieved patterns with the TSFM's internal representation, improving forecasting accuracy without requiring task-specific fine-tuning. Thorough empirical studies on seven public benchmark datasets demonstrate that TS-RAG achieves state-of-the-art zero-shot forecasting performance, outperforming the existing TSFMs by up to 6.84\% across diverse domains while also providing desirable interpretability. Our code and data are available at: https://github.com/UConn-DSIS/TS-RAG.
