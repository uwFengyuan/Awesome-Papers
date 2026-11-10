# CARD: Channel Aligned Robust Blend Transformer for Time Series Forecasting

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ride model dim FFN dim dropout blend size learning rate warm-up batch size M4 Hourly 16 1 128 512 0.1 2 5e-4 0 128 M4 Weekly 16 1 128 512 0.1 2 5e-4 0 128 M4 Daily 16 1 128 512 0.1 2 5e-4 0 128 M4 Monthly 16 1 128 512 0.1 2 5e-4 0 128 M4 Quarterly 4 1 128 512 0.1 2 5e-4 0 128

[Paper](https://openreview.net/forum?id=MJksrOhurE)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Recent studies have demonstrated the great power of Transformer models for time series forecasting. One of the key elements that lead to the transformer's success is the channel-independent (CI) strategy to improve the training robustness. However, the ignorance of the correlation among different channels in CI would limit the model's forecasting capacity. In this work, we design a special Transformer, i.e., **C**hannel **A**ligned **R**obust Blen**d**  Transformer (CARD for short), that addresses key shortcomings of CI type Transformer in time series forecasting. First, CARD introduces a channel-aligned attention structure that allows it to capture both temporal correlations among signals and dynamical dependence among multiple variables over time. Second, in order to efficiently utilize the multi-scale knowledge, we design a token blend module to generate tokens with different resolutions. Third, we introduce a robust loss function for time series forecasting to alleviate the potential overfitting issue. This new loss function weights the importance of forecasting over a finite horizon based on prediction uncertainties. Our evaluation of multiple long-term and short-term forecasting datasets demonstrates that CARD significantly outperforms state-of-the-art time series forecasting methods. The code is available at the following repository: https://github.com/wxie9/CARD.
