# Shifting Time: Time-series Forecasting with Khatri-Rao Neural Operators

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：series containing the positions of NBA is a collection of 100,000 univariate time series from diverse basketball players. The goal here is to forecast the positions domains such as finance and demographics. This collection of the players. For both datasets, we utilized the same train- comprises six datasets corresponding to different seasonal- ing, validation, and test data as used by Wang et al. (2023). ities, varying from hourly to yearly. On thi

[Paper](https://openreview.net/forum?id=emkdmORaj4)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

We present an operator-theoretic framework for temporal and spatio-temporal forecasting based on learning a *continuous time-shift operator*. Our operator learning paradigm offers a continuous relaxation of the discrete lag factor used in traditional autoregressive models, enabling the history of a system up to a given time to be mapped to its future values. We parametrize the time-shift operator using Khatri-Rao neural operators (KRNOs), a novel architecture based on non-stationary integral transforms with nearly linear computational scaling. Our framework naturally handles irregularly sampled observations and enables forecasting at super-resolution in both space and time. Extensive numerical studies across diverse temporal and spatio-temporal benchmarks demonstrate that our approach achieves state-of-the-art or competitive performance with leading methods.
