# TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis

ICLR 2023 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.422 Weather 0.259 0.287 0.271 0.334 0.261 0.312 0.265 0.317 0.309 0.360 0.288 0.314 0.338 0.382 0.946 0.717 0.634 0.548 0.696 0.602 0.803 0.656 Exchange 0.416 0.443 0.410 0.427 0.385 0.447 0.354 0.414 0.519 0.500 0.461 0.454 0.613 0.539 1.913 1.159 1.550 0.998 1.402 0.968 1.280 0.932 ILI 2.139 0.931 2.497 1.004 7.382 2.003 2.616 1.090 2.847 1.144 2.077 0.914 3.006 1.161 7.635 2.050 5.137 1.544 4.839 1.485 4.724 1.445 Table 3: Short-term forecasting task on M4. The prediction lengths are in [6, 48] and results are weighted averaged from several datasets unde

[Paper](https://openreview.net/forum?id=ju_Uqw384Oq)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series analysis is of immense importance in extensive applications, such as weather forecasting, anomaly detection, and action recognition. This paper focuses on temporal variation modeling, which is the common key problem of extensive analysis tasks. Previous methods attempt to accomplish this directly from the 1D time series, which is extremely challenging due to the intricate temporal patterns. Based on the observation of multi-periodicity in time series, we ravel out the complex temporal variations into the multiple intraperiod- and interperiod-variations. To tackle the limitations of 1D time series in representation capability, we extend the analysis of temporal variations into the 2D space by transforming the 1D time series into a set of 2D tensors based on multiple periods. This transformation can embed the intraperiod- and interperiod-variations into the columns and rows of the 2D tensors respectively, making the 2D-variations to be easily modeled by 2D kernels. Technically, we propose the TimesNet with TimesBlock as a task-general backbone for time series analysis. TimesBlock can discover the multi-periodicity adaptively and extract the complex temporal variations from transformed 2D tensors by a parameter-efficient inception block. Our proposed TimesNet achieves consistent state-of-the-art in five mainstream time series analysis tasks, including short- and long-term forecasting, imputation, classification, and anomaly detection. Code is available at this repository: https://github.com/thuml/TimesNet.
