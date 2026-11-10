# ResCP: Reservoir Conformal Prediction for Time Series Forecasting

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：05 0.0517 0.0492 0.0264±0.0002 .. ... ....±0.0005 Exchange ∆Cov 4.44±0.35 2.98±0.07 -0.57±1.58 0.82±1.89 4.57 3.25 1.46±0.18 PI-Width 0.0255±0.0005 0.0399±0.0001 0.0337±0.0016 0.0365±0.0013 0.0544 0.0509 0.0229±0.0001 Winkler 0.0300±0.0005 0.0479±0.0001 0.0480±0.0009 0.04

[Paper](https://openreview.net/forum?id=WGqibe5H3W)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Conformal prediction offers a powerful framework for building distribution-free prediction intervals for exchangeable data.      Existing methods that extend conformal prediction to sequential data rely on fitting a relatively complex model to capture temporal dependencies.      However, these methods can fail if the sample size is small and often require expensive retraining when the underlying data distribution changes.      To overcome these limitations, we propose Reservoir Conformal Prediction (ResCP), a novel training-free conformal prediction method for time series.      Our approach leverages the efficiency and representation learning capabilities of reservoir computing to dynamically reweight conformity scores.      In particular, we compute similarity scores among reservoir states and use them to adaptively reweight the observed residuals at each step. With this approach, ResCP enables us to account for local temporal dynamics when modeling the error distribution without compromising computational scalability. We prove that, under reasonable assumptions, ResCP achieves asymptotic conditional coverage, and we empirically demonstrate its effectiveness across diverse forecasting tasks.
