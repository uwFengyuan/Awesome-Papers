# Towards Multimodal Time Series Anomaly Detection with Semantic Alignment and Condensed Interaction

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：m Yahoo EWJ 1 9.96 2658 2009.11.16 - 2020.6.9 Finance and news information collected from various financial MDT 1 11.17 2732 2009.8.6 - 2020.6.12 news websites such as NASDAQ, Bloomberg, and others. A.2 BASELINES We extensively compare MindTS against 19 baselines, including (1) LLM-based methods: LLMMixer (LMixer) (Kowsher et al., 2024), UniTime (UTime) (Liu et al., 2024c), GPT4TS 17 Published as a conference paper at ICLR 202

[Paper](https://openreview.net/forum?id=fNFbGqu6Rg)

Classification / 分类：Time Series / 时间序列 → Anomaly Detection / 序列异常检测 → Anomaly detection / 异常检测

## Abstract / 摘要

Time series anomaly detection plays a critical role in many dynamic systems. Despite its importance, previous approaches have primarily relied on unimodal numerical data, overlooking the importance of complementary information from other modalities. In this paper, we propose a novel multimodal time series anomaly detection model (MindTS) that focuses on addressing two key challenges: (1) how to achieve semantically consistent alignment across heterogeneous multimodal data, and (2) how to filter out redundant modality information to enhance cross-modal interaction effectively. To address the first challenge, we propose Fine-grained Time-text Semantic Alignment. It integrates exogenous and endogenous text information through cross-view text fusion and a multimodal alignment mechanism, achieving semantically consistent alignment between time and text modalities. For the second challenge, we introduce Content Condenser Reconstruction, which filters redundant information within the aligned text modality and performs cross-modal reconstruction to enable interaction. Extensive experiments on six real-world multimodal datasets demonstrate that the proposed MindTS achieves competitive or superior results compared to existing methods. The code is available at: https://github.com/decisionintelligence/MindTS.
