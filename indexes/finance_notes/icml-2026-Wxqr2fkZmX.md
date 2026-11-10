# Building Social World Model with Large Language Models

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：SWM-bench includes over 12k data points for social belief prediction tasks spanning diverse domains such as politics, finance, and cryptocurrency.

[Paper](https://openreview.net/forum?id=Wxqr2fkZmX)

Classification / 分类：Blockchain & Digital Assets / 区块链与数字资产 → Crypto & Blockchain Transactions / 加密资产与链上交易 → General / 综合

## Abstract / 摘要

Understanding and predicting how social beliefs evolve in response to events -- from policy changes to scientific breakthroughs -- remains a fundamental challenge in social science. Given LLMs' commonsense knowledge and social intelligence, we ask: Can LLMs model the dynamics of social beliefs following social events? In this work, we introduce the concept of the Social World Model (SWM), a general framework designed to capture how social beliefs evolve in response to major events. SWM learns state-transition functions for social beliefs by mining temporal patterns in social data and optimizing the evidence lower bound, without the need for explicit human annotations linking events to belief shifts, or for expensive census data. To evaluate SWM, we introduce a benchmark, SWM-bench, derived from real-world prediction markets, specifically Kalshi and Polymarket. SWM-bench includes over 12k data points for social belief prediction tasks spanning diverse domains such as politics, finance, and cryptocurrency. Our experimental results show that SWM significantly outperforms time-series foundation models, achieving state-of-the-art results on Kalshi data and demonstrating competitive performance on Polymarket data, while offering interpretable insights into the underlying mechanisms of social belief dynamics.
