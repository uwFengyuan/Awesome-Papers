# LangTime: A Language-Guided Unified Model for Time Series Forecasting with Proximal Policy Optimization

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.201 0.118 0.246 0.087 0.202 0.083 0.203 0.087 0.208 0.084 0.201 0.088 0.205 0.107 0.234 Exchange 192 0.175 0.300 0.218 0.338 0.253 0.357 0.175 0.298 0.212 0.332 0.178 0.298 0.178 0.299 0.178 0.302 0.178 0.299 0.176 0.299 0.226 0.344 336 0.329 0.412 0.367 0.443 0.390 0.452 0.329 0.409 0.360 0.438 0.329 0.413 0.328 0.415 0.338

[Paper](https://openreview.net/forum?id=VfoKOD65Zq)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Recent research has shown an increasing interest in utilizing pre-trained large language models (LLMs) for a variety of time series applications. However, there are three main challenges when using LLMs as foundational models for time series forecasting: (1) Cross-domain generalization. (2) Cross-modality alignment. (3) Error accumulation in autoregressive frameworks. To address these challenges, we proposed **LangTime**, a **lan**guage-**g**uided unified model for **time** series forecasting that incorporates cross-domain pre-training with reinforcement learning-based fine-tuning. Specifically, LangTime constructs Temporal Comprehension Prompts (TCPs), which include dataset-wise and channel-wise instructions, to facilitate domain adaptation and condense time series into a single token, enabling LLMs to understand better and align temporal data. To improve autoregressive forecasting, we introduce TimePPO, a reinforcement learning-based fine-tuning algorithm. TimePPO mitigates error accumulation by leveraging a multidimensional rewards function tailored for time series and a repeat-based value estimation strategy. Extensive experiments demonstrate that LangTime achieves state-of-the-art cross-domain forecasting performance, while TimePPO fine-tuning effectively enhances the stability and accuracy of autoregressive forecasting.
