# Aurora: Towards Universal Generative Multimodal Time Series Forecasting

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：1.151 0.763 1.186 0.772 1.251 0.820 1.201 0.783 1.613 0.870 1.478 0.834 - - 1.425 0.848 1.299 0.795 1.337 0.829 NYSE 0.528 0.526 0.880 0.642 - - 0.988 0.704 0.623 0.536 1.129 0.720 - - 1.220 0.820 - - - - st 1 Count 27 21 11 13 3 1 0 0 1 2

[Paper](https://openreview.net/forum?id=VVJ6Ck9JBl)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Cross-domain generalization is very important in Time Series Forecasting because similar historical information may lead to distinct future trends due to the domain-specific characteristics. Recent works focus on building unimodal time series foundation models and end-to-end multimodal supervised models. Since domain-specific knowledge is often contained in modalities like texts, the former lacks the explicit utilization of them, thus hindering the performance. The latter is tailored for end-to-end scenarios and does not support zero-shot inference for cross-domain scenarios. In this work, we introduce Aurora, the first Multimodal Time Series Foundation Model, which supports multimodal inputs and zero-shot inference. Pretrained on Cross-domain Multimodal Time Series Corpus, Aurora can adaptively extract and focus on key domain knowledge contained in corresponding text or image modalities, thus possessing strong cross-domain generalization capability. Through tokenization, encoding, and distillation, Aurora can extract multimodal domain knowledge as guidance and then utilizes a Modality-Guided Multi-head Self-Attention to inject them into the modeling of temporal representations. In the decoding phase, the multimodal representations are used to generate the conditions and prototypes of future tokens, contributing to a novel Prototype-Guided Flow Matching for generative probabilistic forecasting. Comprehensive experiments on 5 well-recognized benchmarks, including TimeMMD, TSFM-Bench, ProbTS, TFB, and EPF, demonstrate the consistent state-of-the-art performance of Aurora on both unimodal and multimodal scenarios.
