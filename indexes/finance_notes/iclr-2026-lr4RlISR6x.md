# PHAT: Modeling Period Heterogeneity for Multivariate Time Series Forecasting

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Table 1: Statistics of used datasets. Datasets NN5 Exchange FRED-MD ETTh ETTm AQShunyi AQWan ILI CzeLan ZafNoo NASDAQ NYSE # Samples 791 7,588 728 14,440 57,600 35,064 35,064 966 19,934 19,225 1,244 1,243 # Frequency 1 day 1 day 1 month 1 hour 15 mins 1 hour 1 hour 1 week 30 mins 30 mins 1 day 1 day Split Ration 7:1:2 7:1:2

[Paper](https://openreview.net/forum?id=lr4RlISR6x)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

While existing multivariate time series forecasting models have advanced significantly in modeling periodicity, they largely neglect the periodic heterogeneity common in real-world data, where variables exhibit distinct and dynamically changing periods. To effectively capture this periodic heterogeneity, we propose PHAT (Period Heterogeneity-Aware Transformer). Specifically, PHAT arranges multivariate inputs into a three-dimensional "periodic bucket" tensor, where the dimensions correspond to variable group characteristics with similar periodicity, time steps aligned by phase, and offsets within the period. By restricting interactions within buckets and masking cross-bucket connections, PHAT effectively avoids interference from inconsistent periods. We also propose a positive-negative attention mechanism, which captures periodic dependencies from two perspectives: periodic alignment and periodic deviation. Additionally, the periodic alignment attention scores are decomposed into positive and negative components, with a modulation term encoding periodic priors. This modulation constrains the attention mechanism to more faithfully reflect the underlying periodic trends. A mathematical explanation is provided to support this property. We evaluate PHAT comprehensively on 14 real-world datasets against 18 baselines, and the results show that it significantly outperforms existing methods, achieving highly competitive forecasting performance. Our sources is available at GitHub.
