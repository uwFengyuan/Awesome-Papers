# Multivariate Probabilistic Time Series Forecasting via Conditioned Normalizing Flows

ICLR 2021 · main · Long

[Long] [Main] [Spotlight] [Poster] [Finance]

Financial evidence / 金融依据：ind-scaling lowrank-Copula scaling Copula Real-NVP MAF MAF Exchange 0.008±0.001 0.007±0.000 0.009±0.000 0.007±0.000 0.0064±0.003 0.005±0.003 0.005±0.003 Solar 0.391±0.017 0.319±0.011 0.368±0.012 0.337±0.024 0.331±0.02 0.315±0.023 0.301±0.014 Electricity 0.025±0.001 0.064±0.008 0.022±0.000 0.024±0.002 0.024±0.001

[Paper](https://openreview.net/forum?id=WiGQBFuVRv)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting is often fundamental to scientific and engineering problems and enables decision making. With ever increasing data set sizes, a trivial solution to scale up predictions is to assume independence between interacting time series. However, modeling statistical dependencies can improve accuracy and enable analysis of interaction effects. Deep learning methods are well suited for this problem, but multi-variate models often assume a simple parametric distribution and do not scale to high dimensions. In this work we model the multi-variate temporal dynamics of time series via an autoregressive deep learning model, where the data distribution  is represented by a conditioned normalizing flow. This combination retains the power of autoregressive models, such as good performance in extrapolation into the future, with the flexibility of flows as a general purpose high-dimensional distribution model, while remaining computationally tractable. We show that it improves over the state-of-the-art for standard metrics on many real-world data sets with several thousand interacting time-series.
