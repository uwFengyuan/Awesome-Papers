# Joint-Embedding Predictive Learning of Latent Market States in U.S. Equities

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We jointly train a permutation-invariant tokenizer that maps each trading day's unordered per-asset features to a fixed set of learned factor tokens, together with a temporal JEPA using masked prediction to obtain a compact daily market-state embedding.

[Paper](https://openreview.net/forum?id=BZfkxSasd3)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Foundation models / 基础模型

## Abstract / 摘要

We investigate whether Joint-Embedding Predictive Architectures (JEPA) can learn useful representations of U.S. equity markets. We jointly train a permutation-invariant tokenizer that maps each trading day's unordered per-asset features to a fixed set of learned factor tokens, together with a temporal JEPA using masked prediction to obtain a compact daily market-state embedding. Our evaluations show that these embeddings are strongly associated with second-moment market structure (realized volatility, correlation concentration, effective factor dimensionality) and weakly associated with market direction. The embedding helps predict gradual recovery dynamics but not sudden stress onsets. Without any text supervision, latent regimes show statistically significant alignment with news-topic shifts.
