# Towards Neural Scaling Laws for Time Series Foundation Models

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Weather Climate H 192 1029 M4 Hourly Finance H 48 414 M4 Daily Finance D 14 4227 M4 Weekly Finance W 13 359 20 Published as a conference paper at ICLR 2025 Table 3 continued from previous page Dataset Domain Frequency # Predictio

[Paper](https://openreview.net/forum?id=uCqxDfLYrB)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Foundation models / 基础模型

## Abstract / 摘要

Scaling laws offer valuable insights into the design of time series foundation models (TSFMs). However, previous research has largely focused on the scaling laws of TSFMs for in-distribution (ID) data, leaving their out-of-distribution (OOD) scaling behavior and the influence of model architectures less explored. In this work, we examine two common TSFM architectures—encoder-only and decoder-only Transformers—and investigate their scaling behavior on both ID and OOD data. These models are trained and evaluated across varying parameter counts, compute budgets, and dataset sizes. Our experiments reveal that the log-likelihood loss of TSFMs exhibits similar scaling behavior in both OOD and ID settings. We further compare the scaling properties across different architectures, incorporating two state-of-the-art TSFMs as case studies, showing that model architecture plays a significant role in scaling. The encoder-only Transformers demonstrate better scalability than the decoder-only Transformers, while the architectural enhancements in the two advanced TSFMs primarily improve ID performance but reduce OOD scalability. While scaling up TSFMs is expected to drive performance breakthroughs, the lack of a comprehensive understanding of TSFM scaling laws has hindered the development of a robust framework to guide model scaling. We fill this gap in this work by synthesizing our findings and providing practical guidelines for designing and scaling larger TSFMs with enhanced model capabilities.
