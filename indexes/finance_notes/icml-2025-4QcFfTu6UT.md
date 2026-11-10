# Winner-takes-all for Multivariate Probabilistic Time Series Forecasting

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：8 Winner-takes-all for Multivariate Probabilistic Time Series Forecasting Figure 4. Cryptocurrency price forecasting for January 4, 2025 with K = 4 hypotheses. Setup in described in Section 6.4. Legend is the same as in Figure 3. We see that TimeMCL produces at least one hypothesis that closely matches the realized trajectory. We expect each hypothesis to specialize in a distinct market scenario, for example, a trend reversal or a sudden collap

[Paper](https://openreview.net/forum?id=4QcFfTu6UT)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

We introduce $\texttt{TimeMCL}$, a method leveraging the Multiple Choice Learning (MCL) paradigm to forecast multiple plausible time series futures. Our approach employs a neural network with multiple heads and utilizes the Winner-Takes-All (WTA) loss to promote diversity among predictions. MCL has recently gained attention due to its simplicity and ability to address ill-posed and ambiguous tasks. We propose an adaptation of this framework for time-series forecasting, presenting it as an efficient method to predict diverse futures, which we relate to its implicit *quantization* objective. We provide insights into our approach using synthetic data and evaluate it on real-world time series, demonstrating its promising performance at a light computational cost.
