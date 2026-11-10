# Retrieval Over Training: Similarity search-based Model Selection for Time Series Anomaly Detection

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：rature Review Time-series anomaly detection (TSAD) has been studied extensively in recent years because of its importance in monitoring, diagnosis, and decision support across domains such as healthcare, manufacturing, finance, energy, and cybersecurity [8, 54]. A central challenge in TSAD is that anomalies may take very different forms, and the statistical properties of time series vary widely across datasets. As a result, the literature has produced a large variety of detectors, each relying on different assumptions about temporal structure, recurrence, noise, and ano

[Paper](https://openreview.net/forum?id=WpZao8pAB7)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Anomaly detection / 异常检测

## Abstract / 摘要

Anomaly detection is a fundamental task for time-series analytics, with important implications for the downstream performance of many applications. Despite the large number of anomaly detection methods proposed in the literature, recent benchmark studies have shown that no single detector performs best across highly heterogeneous time series. Therefore, a practical and scalable solution is to develop a model-selection method that, for a given time series, selects the anomaly detector most likely to perform well. Nevertheless, the model selection approach proposed in the literature suffers from a significant drop in accuracy when applied in Out-of-Distribution (OOD) settings. In this paper, we tackle the aforementioned limitation and propose \textbf{\textsc{RAMSAD}}, a train-free, retrieval-based framework for model selection in time-series anomaly detection. Given a new time series, our method queries a knowledge base of previously observed instances, retrieves the top-${k}$ most similar series, and transfers detector recommendations from their performance profiles. The framework can operate with standard similarity measures as well as embedding-based representations. Overall, we demonstrate that similarity-based retrieval constitutes a strong and efficient foundation for model selection in time-series anomaly detection.
