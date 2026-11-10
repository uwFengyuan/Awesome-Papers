# Signature-Informed Transformer for Asset Allocation

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We argue this creates a fundamental mismatch where minimizing prediction errors fails to yield robust portfolios. / By directly minimizing the Conditional Value at Risk we ensure the training objective aligns with financial goals.

[Paper](https://openreview.net/forum?id=eBM5ALLJNx)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Asset Allocation / 资产配置 → General / 综合

## Abstract / 摘要

Modern deep learning for asset allocation typically separates forecasting from optimization. We argue this creates a fundamental mismatch where minimizing prediction errors fails to yield robust portfolios. We propose the Signature Informed Transformer to address this by unifying feature extraction and decision making into a single policy. Our model employs path signatures to encode complex path dependencies and introduces a specialized attention mechanism that targets geometric asset relationships. By directly minimizing the Conditional Value at Risk we ensure the training objective aligns with financial goals. We prove that our attention module rigorously amplifies signature derived signals. Experiments across diverse equity universes show our approach significantly outperforms both traditional strategies and advanced forecasting baselines. The code is available at: https://github.com/Yoontae6719/Signature-Informed-Transformer-For-Asset-Allocation
