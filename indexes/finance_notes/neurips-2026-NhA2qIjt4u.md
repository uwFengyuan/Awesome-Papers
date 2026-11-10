# Kairos: Toward Adaptive and Parameter-Efficient Time Series Foundation Models

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：291,336,704 Wiki Daily (100k) Web D 100,000 274,100,000 Wind Farms (Daily) Energy D 337 119,549 Exchange Rate Finance D 8 60,704 Table 19: Detailed descriptions of weekly datasets. Dataset Domain Frequency # Time Series # Time points CDC Fluview ILINet Healthcare W 375 319,515 CDC Fluview WHO NREVSS Healthcare W 296 16

[Paper](https://openreview.net/forum?id=NhA2qIjt4u)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Foundation models / 基础模型

## Abstract / 摘要

Inherent temporal heterogeneity, such as varying sampling densities and periodic structures, has posed substantial challenges in zero-shot generalization for Time Series Foundation Models (TSFMs). Existing TSFMs predominantly rely on massive parameterization to absorb such heterogeneity, as their static tokenization and positional encoding schemes entangle diverse temporal patterns into a fixed representation space, encouraging memorization rather than adaptation. To address this limitation, we propose Kairos, a flexible and parameter-efficient TSFM dedicated to forecasting tasks, which decouples temporal heterogeneity from model capacity through a novel tokenization perspective. Kairos introduces a dynamic patching tokenizer and a mixture-of-size encoding that adapt observational granularity to local information density, enabling fine-grained temporal abstraction without increasing model width or depth. In addition, we design a multi-granularity positional embedding based on dynamic rotary encodings, which conditions on instance-level spectral features and temporal structure induced by dynamic patching tokenization, allowing robust modeling of diverse temporal dependencies. Trained on a novel Predictability-Stratified Time-Series (PreSTS) corpus, Kairos achieves superior zero-shot performance with substantially fewer parameters on two mainstream benchmarks, GIFT-Eval and Time-Series-Library.
