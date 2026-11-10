# Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting

NeurIPS 2021 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：9 2.568 1.238 3.105 1.348 720 0.422 0.419 3.379 1.388 3.048 1.328 2.631 1.242 3.171 1.368 2.720 1.287 3.135 1.354 Exchange Electricity 96 0.201 0.317 0.274 0.368 0.258 0.357 0.312 0.402 0.680 0.645 0.375 0.437 0.985 0.813 192 0.222 0.334 0.296 0.386 0.266 0.368 0.348 0.433 0.725 0.676 0.442 0.473 0.996 0.821 336 0.231 0.338 0.300 0.394 0.280 0.380 0.350 0.433 0.828 0.727 0.439 0.473 1.000 0.824 720

[Paper](https://openreview.net/forum?id=J4gRj6d5Qm)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Extending the forecasting time is a critical demand for real applications, such as extreme weather early warning and long-term energy consumption planning. This paper studies the long-term forecasting problem of time series. Prior Transformer-based models adopt various self-attention mechanisms to discover the long-range dependencies. However, intricate temporal patterns of the long-term future prohibit the model from finding reliable dependencies. Also, Transformers have to adopt the sparse versions of point-wise self-attentions for long series efficiency, resulting in the information utilization bottleneck. Going beyond Transformers, we design Autoformer as a novel decomposition architecture with an Auto-Correlation mechanism. We break with the pre-processing convention of series decomposition and renovate it as a basic inner block of deep models. This design empowers Autoformer with progressive decomposition capacities for complex time series. Further, inspired by the stochastic process theory, we design the Auto-Correlation mechanism based on the series periodicity, which conducts the dependencies discovery and representation aggregation at the sub-series level. Auto-Correlation outperforms self-attention in both efficiency and accuracy. In long-term forecasting, Autoformer yields state-of-the-art accuracy, with a 38% relative improvement on six benchmarks, covering five practical applications: energy, traffic, economics, weather and disease. Code is available at this repository: https://github.com/thuml/Autoformer.
