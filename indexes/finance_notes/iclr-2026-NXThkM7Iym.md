# PaAno: Patch-Based Representation Learning for Time-Series Anomaly Detection

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0038 0.8660±0.0011 0.5164±0.0032 CATSv2 5 17 0.0690±0.0072 0.6881±0.0088 0.1381±0.0127 0.0744±0.0117 0.6813±0.0105 0.1285±0.0145 CreditCard 1 29 0.0343±0.0182 0.5558±0.0757 0.0351±0.0179 0.0068±0.0039 0.5652±0.0875 0.0416±0.0151 Daphnet 1 9 0.2706±0.0489 0.8925±0.0192 0.3117±0.0440 0.2564±0.0551 0.9052±0.0200 0.4189±0.0413 Exathlon 25 20.16 0.7769±0.0248 0.9545±0.0072 0.6045±0.0287 0.7482±0.0257 0.9518±0.0075 0.8357±0.01

[Paper](https://openreview.net/forum?id=NXThkM7Iym)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Foundation models / 基础模型

## Abstract / 摘要

Although recent studies on time-series anomaly detection have increasingly adopted ever-larger neural network architectures such as transformers and foundation models, they incur high computational costs and memory usage, making them impractical for real-time and resource-constrained scenarios. Moreover, they often fail to demonstrate significant performance gains over simpler methods under rigorous evaluation protocols. In this study, we propose Patch-based representation learning for time-series Anomaly detection (PaAno), a lightweight yet effective method for fast and efficient time-series anomaly detection. PaAno extracts short temporal patches from time-series training data and uses a 1D convolutional neural network to embed each patch into a vector representation. The model is trained using a combination of triplet loss and pretext loss to ensure the embeddings capture informative temporal patterns from input patches. During inference, the anomaly score at each time step is computed by comparing the embeddings of its surrounding patches to those of normal patches extracted from the training time-series. Evaluated on the TSB-AD benchmark, PaAno achieved state-of-the-art performance, significantly outperforming existing methods, including those based on heavy architectures, on both univariate and multivariate time-series anomaly detection across various range-wise and point-wise performance measures.
