# Selective Learning for Deep Time Series Forecasting

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：learning. Full results of ETTh2 and ETTm1 are provided in Appendix G.1. ETTh1 ETTm2 Electricity Exchange Weather ILI Method MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE Informer 1.289 0.917 1.485 0.919 0.342 0.420 1.520 0.985 0.337 0.374 4.953 1.544 +SL 0.538 0.534 0.494 0.527 0.292 0.386 0.814 0.712 0.273 0.299 3.997 1.360 ∆ -58.3% -41.8% -66.8% -42.6% -14.4% -8.21% -46.4% -27.8% -19.1

[Paper](https://openreview.net/forum?id=kgzRy6nD6D)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Benefiting from high capacity for capturing complex temporal patterns, deep learning (DL) has significantly advanced time series forecasting (TSF). However, deep models tend to suffer from severe overfitting due to the inherent vulnerability of time series to noise and anomalies. The prevailing DL paradigm uniformly optimizes all timesteps through the MSE loss and learns those uncertain and anomalous timesteps without difference, ultimately resulting in overfitting. To address this, we propose a novel selective learning strategy for deep TSF. Specifically, selective learning screens a subset of the whole timesteps to calculate the MSE loss in optimization, guiding the model to focus on generalizable timesteps while disregarding non-generalizable ones. Our framework introduces a dual-mask mechanism to target timesteps: (1) an uncertainty mask leveraging residual entropy to filter uncertain timesteps, and (2) an anomaly mask employing residual lower bound estimation to exclude anomalous timesteps. Extensive experiments across eight real-world datasets demonstrate that selective learning can significantly improve the predictive performance for typical state-of-the-art deep models, including 37.4% MSE reduction for Informer, 8.4% for TimesNet, and 6.5% for iTransformer.
