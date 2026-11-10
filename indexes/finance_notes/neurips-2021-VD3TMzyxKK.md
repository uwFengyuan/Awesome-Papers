# Probabilistic Forecasting: A Level-Set Approach

NeurIPS 2021 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：NN-QR electricity [13] 0.0499 0.1478 0.0785 0.0592 0.0601 parts [34] 0.9709 0.7584 0.9617 0.9877 0.7566 m4_daily [24] 0.0148 0.0281 0.0188 0.0239 0.0154 traffic [13] 0.1212 0.1062 0.1289 0.0913 0.1134 wiki10k 0.2926 0.2534 0.3069 0.2421 0.2482 dcrideshare [8] 0.3381 0.3171 0.3929 0.2837 0.2820 Table 3: Mean Weighted Quantile Lo

[Paper](https://openreview.net/forum?id=VD3TMzyxKK)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Large-scale time series panels have become ubiquitous over the last years in areas such as retail, operational metrics, IoT, and medical domain (to name only a few). This has resulted in a need for forecasting techniques that effectively leverage all available data by learning across all time series in each panel. Among the desirable properties of forecasting techniques, being able to generate probabilistic predictions ranks among the top. In this paper, we therefore present Level Set Forecaster (LSF), a simple yet effective general approach to transform a point estimator into a probabilistic one. By recognizing the connection of our algorithm to random forests (RFs) and quantile regression forests (QRFs), we are able to prove consistency guarantees of our approach under mild assumptions on the underlying point estimator. As a byproduct, we prove the first consistency results for QRFs under the CART-splitting criterion. Empirical experiments show that our approach, equipped with tree-based models as the point estimator, rivals state-of-the-art deep learning models in terms of forecasting accuracy.
