# Adaptive Conformal Inference Under Distribution Shift

NeurIPS 2021 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：Time Figure 1: Local coverage frequencies for adaptive conformal (blue), a non-adaptive method that holds ↵t = ↵ fixed (red), and an i.i.d. Bernoulli(0.1) sequence (grey) for the prediction of stock market volatility. The coloured dotted lines mark the average coverage obtained across all time points, while the black line indicates the target level of 1 ↵ = 0.9. Daily open prices were obtained from publicly available datasets published by The Wall Street Journal. The realized local coverage frequencies for the non-adaptive and adaptive conformal m

[Paper](https://openreview.net/forum?id=6vaActvpcp3)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → Stock Movement & Returns / 股价方向与收益预测 → General / 综合

## Abstract / 摘要

We develop methods for forming prediction sets in an online setting where the data generating distribution is allowed to vary over time in an unknown fashion. Our framework builds on ideas from conformal inference to provide a general wrapper that can be combined with any black box method that produces point predictions of the unseen label or estimated quantiles of its distribution. While previous conformal inference methods rely on the assumption that the data are exchangeable, our adaptive approach provably achieves the desired coverage frequency over long-time intervals irrespective of the true data generating process. We accomplish this by modelling the distribution shift as a learning problem in a single parameter whose optimal value is varying over time and must be continuously re-estimated. We test our method, adaptive conformal inference, on two real world datasets and find that its predictions are robust to visible and significant distribution shifts.
