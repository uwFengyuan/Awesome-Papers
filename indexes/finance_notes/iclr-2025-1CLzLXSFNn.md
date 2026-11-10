# TimeMixer++: A General Time Series Pattern Machine for Universal Predictive Analysis

ICLR 2025 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：ly 1 6 (23000, 0, 23000) Yearly 0.43 Demographic M4-Quarterly 1 8 (24000, 0, 24000) Quarterly 0.47 Finance M4-Monthly 1 18 (48000, 0, 48000) Monthly 0.44 Industry M4-Weakly 1 13 (359, 0, 359) Weakly 0.43 Macro M4-Daily 1 14 (4227, 0, 4227) Daily 0

[Paper](https://openreview.net/forum?id=1CLzLXSFNn)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series analysis plays a critical role in numerous applications, supporting tasks such as forecasting, classification, anomaly detection, and imputation. In this work, we present the time series pattern machine (TSPM), a model designed to excel in a broad range of time series tasks through powerful representation and pattern extraction capabilities. Traditional time series models often struggle to capture universal patterns, limiting their effectiveness across diverse tasks. To address this, we define multiple scales in the time domain and various resolutions in the frequency domain, employing various mixing strategies to extract intricate, task-adaptive time series patterns. Specifically, we introduce TimeMixer++, a general-purpose TSPM that processes multi-scale time series using (1) multi-resolution time imaging (MRTI), (2) time image decomposition (TID), (3) multi-scale mixing (MCM), and (4) multi-resolution mixing (MRM) to extract comprehensive temporal patterns. MRTI transforms multi-scale time series into multi-resolution time images, capturing patterns across both temporal and frequency domains. TID leverages dual-axis attention to extract seasonal and trend patterns, while MCM hierarchically aggregates these patterns across scales. MRM adaptively integrates all representations across resolutions. TimeMixer++ achieves state-of-the-art performance across 8 time series analytical tasks, consistently surpassing both general-purpose and task-specific models. Our work marks a promising step toward the next generation of TSPMs, paving the way for further advancements in time series analysis.
