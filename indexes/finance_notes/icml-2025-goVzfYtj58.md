# Exploring Representations and Interventions in Time Series Foundation Models

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：18 0.107 0.178 0.076 0.220 0.112 Electricity 0.372 0.250 0.446 0.342 0.716 0.757 0.428 0.327 0.727 0.819 Exchange rate 0.125 0.034 0.124 0.032 0.170 0.061 0.111 0.027 0.174 0.067 Illness 0.393 0.421 0.448 0.502 0.547 0.669 0.423 0.446 0.552 0.648 Traffic 0.492 0.790 0.552 0.906 0.861 1.562 0.606 0.940 0.878 1.633 Weather 0.129 0.079

[Paper](https://openreview.net/forum?id=goVzfYtj58)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Foundation models / 基础模型

## Abstract / 摘要

Time series foundation models (TSFMs) promise to be powerful tools for a wide range of applications. However, their internal representations and learned concepts are still not well understood. In this study, we investigate the structure and redundancy of representations across various TSFMs, examining the self-similarity of model layers within and across different model sizes. This analysis reveals block-like redundancy in the representations, which can be utilized for informed pruning to improve inference speed and efficiency. We also explore the concepts learned by these models, such as periodicity and trends. We demonstrate how conceptual priors can be derived from TSFM representations and leveraged to steer its outputs toward concept-informed predictions. Our work bridges representational analysis from language and vision models to TSFMs, offering new methods for building more computationally efficient and transparent TSFMs.
