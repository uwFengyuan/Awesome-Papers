# Latent Laplace Diffusion for Irregular Multivariate Time Series

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：orology features include temperature, dew point, sea-level pressure, wind speed, and precipitation. We construct the finance datasets (Crypto and US Equity) from Google Finance daily market data. Crypto spans 2019-01-01 to 2024-12-31 with the top 118 (volume and market cap) most actively traded currencies selected; US Equity spans 2017-01-01 to 2024-12-31 with the top 222 (volume and market cap) most actively traded equities selected from NYSE and NASDAQ. Finance features include open, high, low, close, volume, daily returns (percent; adjacent trading days), gapped returns, a market index feature, 20-day rolling close, high–low ratio, dividends, and sinusoidal calendar features (day-of-week, day-of-month, month-of-year). Table 9. Dataset stati

[Paper](https://openreview.net/forum?id=t73XUJvyQr)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Imputation / 缺失处理

## Abstract / 摘要

Irregular multivariate time series pose a fundamental trade-off for long-horizon forecasting: discrete methods can distort temporal structure via re-gridding, while continuous-time models often rely on sequential numerical solvers that are prone to drift. To bridge this gap, we present the Latent Laplace Diffusion (LLapDiff), a generative framework that models the target as a low-dimensional latent trajectory, enabling horizon-wide generation without step-by-step integration over physical time. We guide the reverse process using a stable modal parameterization motivated by stochastic port-Hamiltonian dynamics, and parameterize its mean evolution in the Laplace domain via learnable complex-conjugate poles, allowing for direct evaluation over irregular timestamps. Moreover, we link continuous dynamics to irregular observations through renewal-averaging analysis, which maps sampling gaps to effective event-domain poles and theoretically motivates a gap-aware history summarizer for conditioning. Extensive experiments demonstrate that LLapDiff consistently outperforms baselines in long-horizon forecasting, and its continuous-time generative nature also supports missing-value imputation by querying the same model at historical timestamps.
