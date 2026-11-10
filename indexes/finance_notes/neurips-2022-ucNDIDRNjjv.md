# Non-stationary Transformers: Exploring the Stationarity in Time Series Forecasting

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：tatistic indicates more stationary dataset. Dataset Variable Number Sampling Frequency Total Observations ADF Test Statistic Exchange 8 1 Day 7,588 -1.889 ILI 7 1 Week 966 -5.406 ETTm2 7 15 Minutes 69,680 -6.225 Electricity 321 1 Hour 26,304 -8.483 Traffic 862 1 Hou

[Paper](https://openreview.net/forum?id=ucNDIDRNjjv)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Transformers have shown great power in time series forecasting due to their global-range modeling ability. However, their performance can degenerate terribly on non-stationary real-world data in which the joint distribution changes over time. Previous studies primarily adopt stationarization to attenuate the non-stationarity of original series for better predictability. But the stationarized series deprived of inherent non-stationarity can be less instructive for real-world bursty events forecasting. This problem, termed over-stationarization in this paper, leads Transformers to generate indistinguishable temporal attentions for different series and impedes the predictive capability of deep models. To tackle the dilemma between series predictability and model capability, we propose Non-stationary Transformers as a generic framework with two interdependent modules: Series Stationarization and De-stationary Attention. Concretely, Series Stationarization unifies the statistics of each input and converts the output with restored statistics for better predictability. To address the over-stationarization problem, De-stationary Attention is devised to recover the intrinsic non-stationary information into temporal dependencies by approximating distinguishable attentions learned from raw series. Our Non-stationary Transformers framework consistently boosts mainstream Transformers by a large margin, which reduces MSE by 49.43% on Transformer, 47.34% on Informer, and 46.89% on Reformer, making them the state-of-the-art in time series forecasting. Code is available at this repository: https://github.com/thuml/Nonstationary_Transformers.
