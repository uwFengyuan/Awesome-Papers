# Generating Financial Time Series by Matching Random Convolutional Features

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：Generating realistic financial time series is challenging as training data is often limited to a single historical path. / We show that generators trained by matching random SOCK features consistently outperform signature and diffusion baselines across a wide range of small-sample financial datasets.

[Paper](https://openreview.net/forum?id=tLVW1Y9hBz)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Generation / 生成

## Abstract / 摘要

Generating realistic financial time series is challenging as training data is often limited to a single historical path. With such scarce data, overfitting is hard to avoid, especially under adversarial training where a trained discriminator can memorize the training samples. To mitigate this, recent approaches train generators to minimize the discrepancy between untrained feature representations of real and generated time series. In these works, the feature maps are based on path signatures, which can fail to capture relevant time series properties at tractable truncation depths. In this work, we instead train generators by matching random convolutional features of real and generated time series. Existing random convolutional feature maps, such as Rocket and Hydra, have been shown to provide informative representations of real-world time series, but cannot supervise generative models because they are non-differentiable. We introduce **SOCK** (***SO**ft **C**ompeting **K**ernels*), a fully differentiable random convolutional feature map, suited to train generative time series models. We show that generators trained by matching random SOCK features consistently outperform signature and diffusion baselines across a wide range of small-sample financial datasets. We further demonstrate SOCK's expressiveness on two-sample hypothesis testing and time series classification tasks, where SOCK matches or outperforms existing unsupervised feature maps.
