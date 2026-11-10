# Tackling Time-Series Forecasting Generalization via Mitigating Concept Drift

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：2.0% 7.1% 13.8% 6.5% 96 0.338 0.475 0.102 0.237 0.130 0.265 0.102 0.236 0.135 0.272 0.115 0.255 Exchange 192 0.566 0.622 0.203 0.338 0.247 0.394 0.194 0.332 0.250 0.376 0.209 0.343 336 1.078 0.867 0.407 0.484 0.522 0.557 0.388 0.477 0.450 0.503 0.426 0.495 720 1.292 0.963 1.165 0.813 1.171 0.824 0.995 0.747 1.501 0.941 1.138 0.827 IMP. 53.5% 38.9% 20.9% 12.6% 15.

[Paper](https://openreview.net/forum?id=emkvZ7NanK)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time-series forecasting finds broad applications in real-world scenarios. Due to the dynamic nature of time series data, it is important for time-series forecasting models to handle potential distribution shifts over time. In this paper, we initially identify two types of distribution shifts in time series: concept drift and temporal shift. We acknowledge that while existing studies primarily focus on addressing temporal shift issues in time series forecasting, designing proper concept drift methods for time series forecasting has received comparatively less attention.  Motivated by the need to address potential concept drift, while conventional concept drift methods via invariant learning face certain challenges in time-series forecasting, we propose a soft attention mechanism that finds invariant patterns from both lookback and horizon time series. Additionally, we emphasize the critical importance of mitigating temporal shifts as a preliminary to addressing concept drift. In this context, we introduce ShifTS, a method-agnostic framework designed to tackle temporal shift first and then concept drift within a unified approach. Extensive experiments demonstrate the efficacy of ShifTS in consistently enhancing the forecasting accuracy of agnostic models across multiple datasets, and outperforming existing concept drift, temporal shift, and combined baselines.
