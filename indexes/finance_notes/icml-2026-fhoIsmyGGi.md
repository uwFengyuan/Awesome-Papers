# Decomposition-Based Modular Conformal Prediction for Two-Stage Modeling

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that our approach improves coverage under structural, stage-wise shifts compared to standard conformal methods, while identifying stage-wise error contribution.

[Paper](https://openreview.net/forum?id=fhoIsmyGGi)

Classification / 分类：Time Series / 时间序列 → Financial Stochastic Processes / 金融随机过程 → Foundation models / 基础模型

## Abstract / 摘要

Conformal prediction offers finite-sample coverage guarantees under minimal assumptions. However, existing methods treat the entire modeling process as a black box, overlooking opportunities to exploit and understand modular  structure. We introduce a conformal prediction framework for two-stage sequential models, where an upstream predictor generates intermediate representations for a downstream model. By decomposing the overall prediction residual into stage-specific components, our method enables practitioners to attribute uncertainty to specific pipeline stages. We develop a risk-controlled parameter selection procedure using family-wise error rate (FWER) control to calibrate stage-wise scaling parameters, and introduce an adaptive extension for non-stationary settings. Experiments on synthetic distribution shifts, as well as real-world supply chain and stock market data, demonstrate that our approach improves coverage under structural, stage-wise shifts compared to standard conformal methods, while identifying stage-wise error contribution. This framework offers diagnostic advantages and robust coverage that standard conformal methods lack.
