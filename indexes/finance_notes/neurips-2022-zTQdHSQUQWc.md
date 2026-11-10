# FiLM: Frequency improved Legendre Memory Model for Long-term Time Series Forecasting

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：96 0.086 0.204 0.086 0.208 0.087 0.210 Exchange 192 0.188 0.292 0.187 0.318 0.207 0.340 336 0.356 0.433 0.358 0.437 0.353 0.461 720 0.727 0.669 0.788 0.680 0.748 0.674

[Paper](https://openreview.net/forum?id=zTQdHSQUQWc)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Recent studies have shown that deep learning models such as RNNs and Transformers have brought significant performance gains for long-term forecasting of time series because they effectively utilize historical information. We found, however, that there is still great room for improvement in how to preserve historical information in neural networks while avoiding overfitting to noise present in the history. Addressing this allows better utilization of the capabilities of deep learning models. To this end, we design a Frequency improved Legendre Memory model, or FiLM: it applies Legendre polynomial projections to approximate historical information, uses Fourier projection to remove noise, and adds a low-rank approximation to speed up computation. Our empirical studies show that the proposed FiLM significantly improves the accuracy of state-of-the-art models in multivariate and univariate long-term forecasting by (19.2%, 22.6%), respectively. We also demonstrate that the representation module developed in this work can be used as a general plugin to improve the long-term prediction performance of other deep learning modules. Code is available at  https://github.com/tianzhou2011/FiLM/.
