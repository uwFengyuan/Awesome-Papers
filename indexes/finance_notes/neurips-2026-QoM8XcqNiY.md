# Empowering Time Series Analysis with Large-Scale Multimodal Pretraining

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：HORAI W/O Modality Modality Exchange W/O Router W/O MoE-FFN outperforms GPT4TS by 12.2%, 20.2%, and 22.6% in AUC- ROC, VUS-ROC, and VUS-PR. These results demonstrate Figure 4. Ablation study on the Social Good dataset and the Energy dataset. that pre-training on large-scale, multi-domain data equi

[Paper](https://openreview.net/forum?id=QoM8XcqNiY)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Foundation models / 基础模型

## Abstract / 摘要

While existing time series foundation models primarily rely on large-scale unimodal pretraining, they lack complementary modalities to enhance time series understanding. Building multimodal foundation models is a natural next step, but it faces key challenges: 1) lack of a unified multimodal pretraining paradigm and large-scale multimodal corpora for time series analysis; 2) how to effectively integrate heterogeneous modalities and enhance model generalization. To address these challenges, we take an early step toward multimodal foundation models for time series analysis. We first propose a multimodal pretraining paradigm that leverages time series with endogenous modalities (derived images and text) and exogenous knowledge (news), providing a comprehensive multi-view perspective for time series analysis. To support this, we develop an automated data construction pipeline to curate MM-TS, the first large-scale multimodal time series dataset spanning six domains, with up to one billion points. Then we propose HORAI, a frequency-enhanced multimodal foundation model. It integrates two core components: the Frequency-enhanced Cross-Modality Encoder and the Time-Frequency Decoder, designed to effectively fuse multimodal features and enhance model generalization across modalities and domains. After pretraining on MM-TS, HORAI achieves state-of-the-art zero-shot performance on time series forecasting and anomaly detection tasks, demonstrating strong generalization.
