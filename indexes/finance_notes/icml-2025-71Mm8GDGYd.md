# $K^2$VAE: A Koopman-Kalman Enhanced Variational AutoEncoder for Probabilistic Time Series Forecasting

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：eans and standard errors are based on 5 independent runs of retraining and evaluation. Red: the best, Blue: the 2nd best. Model Metric Exchange-S Solar-S Electricity-S Traffic-S ETTh1-S ETTh2-S ETTm1-S ETTm2-S CRPS 0.012±0.002 0.516±0.011 0.068±0.003 0.298±0.022 0.320±0.017 0.212±0.012 0.193±0.005 0.199±0.003 FITS NMAE 0.017±0.003 0.701±0.014 0.092±0.004 0.392±0.028 0.423±0.033 0.278±0.009 0.249±0.007 0.260±0.011

[Paper](https://openreview.net/forum?id=71Mm8GDGYd)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Probabilistic Time Series Forecasting (PTSF) plays a crucial role in decision-making across various fields, including economics, energy, and transportation. Most existing methods excell at short-term forecasting, while overlooking the hurdles of Long-term Probabilistic Time Series Forecasting (LPTSF). As the forecast horizon extends, the inherent nonlinear dynamics have a significant adverse effect on prediction accuracy, and make generative models inefficient by increasing the cost of each iteration. To overcome these limitations, we introduce $K^2$VAE, an efficient VAE-based generative model that leverages a KoopmanNet to transform nonlinear time series into a linear dynamical system, and devises a KalmanNet to refine predictions and model uncertainty in such linear system, which reduces error accumulation in long-term forecasting. Extensive experiments demonstrate that $K^2$VAE outperforms state-of-the-art methods in both short- and long-term PTSF, providing a more efficient and accurate solution.
