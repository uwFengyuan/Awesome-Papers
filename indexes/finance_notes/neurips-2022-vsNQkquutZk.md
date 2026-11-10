# WaveBound: Dynamic Error Bounds for Stable Time Series Forecasting

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：96 0.153 0.285 0.146 0.274 0.604 0.624 0.615 0.627 0.979 0.791 0.878 0.765 0.483 0.518 0.357 0.432 Exchange 192 0.297 0.397 0.262 0.373 0.982 0.806 0.953 0.797 1.147 0.854 1.136 0.859 0.706 0.646 0.621 0.593 336 0.438 0.490 0.425 0.483 1.264 0.934 1.263 0.944 1.592 1.014 1.461 0.992 1.055 0.800 0.837 0.691 720 1.207 0.860 1.088 0.810 1.663 1.051 1.562 1.016 2.540 1.306 2.496 1.294 2

[Paper](https://openreview.net/forum?id=vsNQkquutZk)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting has become a critical task due to its high practicality in real-world applications such as traffic, energy consumption, economics and finance, and disease analysis. Recent deep-learning-based approaches have shown remarkable success in time series forecasting. Nonetheless, due to the dynamics of time series data, deep networks still suffer from unstable training and overfitting. Inconsistent patterns appearing in real-world data lead the model to be biased to a particular pattern, thus limiting the generalization. In this work, we introduce the dynamic error bounds on training loss to address the overfitting issue in time series forecasting. Consequently, we propose a regularization method called WaveBound which estimates the adequate error bounds of training loss for each time step and feature at each iteration. By allowing the model to focus less on unpredictable data, WaveBound stabilizes the training process, thus significantly improving generalization. With the extensive experiments, we show that WaveBound consistently improves upon the existing models in large margins, including the state-of-the-art model.
