# TACTiS-2: Better, Faster, Simpler Attentional Copulas for Multivariate Time Series

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：994) estimator. Average ranks report the average ranking of methods across all evaluation windows and datasets. Lower is better and the best results are in bold. Model electricity fred-md kdd-cup solar-10min traffic Avg. Rank Auto-ARIMA 0.077 ± 0.016 0.043 ± 0.005 0.625 ± 0.066 0.994 ± 0.216 0.222 ± 0.005 6.2 ± 0.3 ETS 0.059 ± 0.011 0.037 ± 0.010 0.408 ± 0.030 0.678 ± 0.097 0.353 ± 0.011 6.0 ± 0.2 TempFlow 0.075 ± 0.024 0.095 ± 0.004 0.250 ± 0.010

[Paper](https://openreview.net/forum?id=xtOydkE1Ku)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

We introduce a new model for multivariate probabilistic time series prediction, designed to flexibly address a range of tasks including forecasting, interpolation, and their combinations. Building on copula theory, we propose a simplified objective for the recently-introduced transformer-based attentional copulas (TACTiS), wherein the number of distributional parameters now scales linearly with the number of variables instead of factorially. The new objective requires the introduction of a training curriculum, which goes hand-in-hand with necessary changes to the original architecture. We show that the resulting model has significantly better training dynamics and achieves state-of-the-art performance across diverse real-world forecasting tasks, while maintaining the flexibility of prior work, such as seamless handling of unaligned and unevenly-sampled time series. Code is made available at https://github.com/ServiceNow/TACTiS.
