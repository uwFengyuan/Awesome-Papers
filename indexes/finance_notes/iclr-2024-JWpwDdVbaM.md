# ARM: Refining Multivariate Forecasting with Adaptive Temporal-Contextual Learning

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：95 Traffic (720) 0.425 0.294 0.432 0.286 0.466 0.315 0.626 0.382 0.660 0.408 0.864 0.472 2.811 1.097 Exchange (96) 0.078 0.197 0.087 0.207 0.081 0.203 0.148 0.278 0.197 0.323 0.847 0.752 0.081 0.196 Exchange (192) 0.150 0.280 0.194 0.316 0.157 0.293 0.271 0.380 0.300 0.369 1.204 0.895 0.167 0.289 Exchange (336) 0.252 0.367 0.351 0.432 0.305 0.414 0.460 0.500 0.509 0.524 1.672 1.036 0.305 0.396 Exchan

[Paper](https://openreview.net/forum?id=JWpwDdVbaM)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Long-term time series forecasting (LTSF) is important for various domains but is confronted by challenges in handling the complex temporal-contextual relationships. As multivariate input models underperforming some recent univariate counterparts, we posit that the issue lies in the inefficiency of existing multivariate LTSF Transformers to model series-wise relationships: the characteristic differences between series are often captured incorrectly. To address this, we introduce ARM: a multivariate temporal-contextual adaptive learning method, which is an enhanced architecture specifically designed for multivariate LTSF modelling. ARM employs Adaptive Univariate Effect Learning (**A**UEL), Random Dropping (**R**D) training strategy, and Multi-kernel Local Smoothing (**M**KLS), to better handle individual series temporal patterns and correctly learn inter-series dependencies. ARM demonstrates superior performance on multiple benchmarks without significantly increasing computational costs compared to vanilla Transformer, thereby advancing the state-of-the-art in LTSF. ARM is also generally applicable to other LTSF architecture beyond vanilla Transformer.
