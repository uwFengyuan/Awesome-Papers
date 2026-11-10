# ReNF: Rethinking the Design of Neural Long-Term Time Series Forecasters

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：s Angeles during the spring of 2012, specifically from March to June. This data was collected at an interval of five minutes. The NASDAQ includes the daily NASDAQ index and key economic indicators from 2010 to 2024. The SP500 records daily SP500 index data (e.g., opening price, closing price, and trading volume) from January 1993 to February 2025. CarSales collects daily sales of 10 vehicle brands (e.g., Toyota, Honda) in the U.S. from January 2005 to June 2023. The data are compiled from the Vehicle Sales dataset on Kaggle. Power contains daily wind and solar energy p

[Paper](https://openreview.net/forum?id=emDhH9VFqm)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Neural Forecasters (NFs) have become a cornerstone of Long-term Time Series Forecasting (LTSF). However, recent progress has been hampered by an overemphasis on architectural complexity at the expense of fundamental forecasting structures. In this work, we revisit principled designs of LTSF. We begin by formulating a Variance Reduction Hypothesis (VRH), positing that generating and combining multiple forecasts is essential to reducing the inherent uncertainty of NFs. Guided by this, we propose Boosted Direct Output (BDO), a streamlined paradigm that synergistically hybridizes the causal structure of Auto-Regressive (AR) with the stability of Direct Output (DO), while implicitly realizing the principle of forecast combination within a single network. Furthermore, we mitigate a critical validation-test generalization gap by employing parameter smoothing to stabilize optimization. Extensive experiments demonstrate that these trivial yet principled improvements enable a direct temporal MLP to outperform recent, complex state-of-the-art models in nearly all benchmarks, without relying on intricate inductive biases. Finally, we empirically verify our hypothesis, establishing a dynamic performance bound that highlights promising directions for future research. The code is publicly available at: \url{https://github.com/Luoauoa/ReNF}.
