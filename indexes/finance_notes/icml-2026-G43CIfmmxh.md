# The Label Horizon Paradox: Rethinking Supervision Targets in Financial Forecasting

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：While deep learning has revolutionized financial forecasting through sophisticated architectures, the design of the supervision signal itself is rarely scrutinized. / Extensive experiments on large-scale financial datasets demonstrate consistent improvements over conventional baselines, thereby opening new avenues for label-centric research in financial forecasting.

[Paper](https://openreview.net/forum?id=G43CIfmmxh)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → Stock Movement & Returns / 股价方向与收益预测 → General / 综合

## Abstract / 摘要

While deep learning has revolutionized financial forecasting through sophisticated architectures, the design of the supervision signal itself is rarely scrutinized. We challenge the canonical assumption that training labels must strictly mirror inference targets, uncovering the Label Horizon Paradox: the optimal supervision signal often deviates from the prediction goal, shifting across intermediate horizons governed by market dynamics. We theoretically ground this phenomenon in a dynamic signal-noise trade-off, demonstrating that generalization hinges on the competition between marginal signal realization and noise accumulation. To operationalize this insight, we propose a bi-level optimization framework that autonomously identifies the optimal proxy label within a single training run. Extensive experiments on large-scale financial datasets demonstrate consistent improvements over conventional baselines, thereby opening new avenues for label-centric research in financial forecasting.
