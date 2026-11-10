# RobustTSF: Towards Theory and Design of Robust Time Series Forecasting with Anomalies

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：we report best epoch MAE for each setting ETT-h1 with Anomaly Position Exchange with Anomaly Position Anomaly Type front middle back front middle back Clean 0.051 0.051 0.051 0.047 0.047 0.047 Const. (η = 0.1) 0.051 0.051 0.052

[Paper](https://openreview.net/forum?id=ltZ9ianMth)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting is an important and forefront task whose techniques have been applied to electricity forecasting, trajectory prediction, labor planning, etc. However, most of time series forecasting techniques assume that the training data is clean without anomalies. This assumption is unrealistic since the collected time series data can be contaminated in practice. The forecasting model will be inferior if it is directly trained by time series with anomalies. Thus it is essential to develop methods to automatically learn a robust forecasting model from the contaminated data. In this paper, we first statistically define three types of anomalies, then theoretically and experimentally analyze the loss robustness and sample robustness when these anomalies exist. Based on our analyses, we propose a simple and efficient algorithm to learn a robust forecasting model. Extensive experiments show that our method is highly robust and outperforms all existing approaches. The code is available at https://github.com/haochenglouis/RobustTSF.
