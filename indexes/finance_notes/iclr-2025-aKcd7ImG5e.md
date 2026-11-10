# Towards a General Time Series Anomaly Detector with Adaptive Bottlenecks and Dual Adversarial Decoders

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：61.59 94.59 74.60 74.31 92.11 82.26 Table 2: Overall results for the NeurIPS-TS datasets. Dataset CICIDS Creditcard GECCO SWAN Metric F1 AUC F1 AUC F1 AUC F1 AUC A.T. 34.71 49.00 65.14 52.55 64.27 51.60 33.67 44.74 DCdetector 40.02 53.95 58.28 42.36 66.18 45.38

[Paper](https://openreview.net/forum?id=aKcd7ImG5e)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Anomaly detection / 异常检测

## Abstract / 摘要

Time series anomaly detection plays a vital role in a wide range of applications. Existing methods require training one specific model for each dataset, which exhibits limited generalization capability across different target datasets, hindering anomaly detection performance in various scenarios with scarce training data. Aiming at this problem, we propose constructing a general time series anomaly detection model, which is pre-trained on extensive multi-domain datasets and can subsequently apply to a multitude of downstream scenarios. The significant divergence of time series data across different domains presents two primary challenges in building such a general model: (1) meeting the diverse requirements of appropriate information bottlenecks tailored to different datasets in one unified model, and (2) enabling distinguishment between multiple normal and abnormal patterns, both are crucial for effective anomaly detection in various target scenarios. To tackle these two challenges, we propose a General time series anomaly Detector with Adaptive Bottlenecks and Dual Adversarial Decoders (DADA), which enables flexible selection of bottlenecks based on different data and explicitly enhances clear differentiation between normal and abnormal series. We conduct extensive experiments on nine target datasets from different domains. After pre-training on multi-domain data, DADA, serving as a zero-shot anomaly detector for these datasets, still achieves competitive or even superior results compared to those models tailored to each specific dataset.
