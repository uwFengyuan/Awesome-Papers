# Sundial: A Family of Highly Capable Time Series Foundation Models

ICML 2025 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：k by a small MLP: ECG 5.62% 9.11% 4.65% Finance (t) (t) uθt yi |hi = FM-Net yi , t, hi .   (7) 1.02% IoT

[Paper](https://openreview.net/forum?id=LO7ciRpjI5)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Foundation models / 基础模型

## Abstract / 摘要

We introduce Sundial, a family of native, flexible, and scalable time series foundation models. To predict the next-patch's distribution, we propose a TimeFlow Loss based on flow-matching, which facilitates native pre-training of Transformers on continuous-valued time series without discrete tokenization. Conditioned on arbitrary-length time series, our models are pre-trained without specifying any prior distribution and can generate multiple probable predictions, achieving more flexibility in representation learning than using parametric densities. Towards time series foundation models, we leverage minimal but crucial adaptations of Transformers and curate TimeBench with one trillion time points, comprising mostly real-world datasets and synthetic data. By mitigating mode collapse via TimeFlow Loss, we pre-train a family of Sundial models on TimeBench, which achieve unprecedented model capacity and generalization performance. In addition to excellent scalability, Sundial achieves state-of-the-art results on both point and probabilistic forecasting benchmarks with a just-in-time inference speed, i.e., making zero-shot predictions within a few milliseconds. We believe that Sundial's pioneering generative forecasting capability can improve model reliability in real-world decision-making. Code is available at: https://github.com/thuml/Sundial.
