# Synthetic Series-Symbol Data Generation for Time Series Foundation Models

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ETTh1 ETTh2 Weather Electircity Traffic Exchange Average Metrics MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE MSE MAE 0B 0.401 0.409 0.293 0.339 0.487 0.474 0.376 0.412 0.257 0.289 0.193 0.284 0.471 0.310 0.383 0.415 0.358 0.366 1B 0.376 0.398 0.292 0.331 0.461 0.459 0.403 0.419 0.257 0.282 0.199 0.285 0.473 0.303 0.370 0.410 0.354 0.361 10B 0.376 0.393 0.281 0.329 0.444 0.444 0.376 0.408 0.2

[Paper](https://openreview.net/forum?id=xB1ZNgq0Xp)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Foundation models / 基础模型

## Abstract / 摘要

Foundation models for time series analysis (TSA) have attracted significant attention. However, challenges such as training data scarcity and imbalance continue to hinder their development. Inspired by complex dynamic system theories, we design a series-symbol data generation mechanism, enabling the unrestricted creation of high-quality time series data paired with corresponding symbolic expressions. To leverage series-symbol data pairs with strong correlations, we develop SymTime, a pre-trained foundation model for enhancing time series representation using symbolic information. SymTime demonstrates competitive performance across five major TSA tasks when fine-tunes with downstream tasks, rivaling foundation models pre-trained on real-world datasets. This approach underscores the potential of series-symbol data generation and pretraining mechanisms in overcoming data scarcity and enhancing task performance. The code is available at https://github.com/wwhenxuan/SymTime.
