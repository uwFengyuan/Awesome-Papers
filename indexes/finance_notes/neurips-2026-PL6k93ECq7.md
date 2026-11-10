# Combating Camouflage and Forgetting: Spatio-Temporal Dual Denoising for Money Laundering Detection

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：Money laundering detection on financial transaction graphs is critical but challenging. / Laundering activities often conceal illicit fund flows within dense legitimate transaction neighborhoods and disperse suspicious behaviors over extended time spans. / In this paper, we propose a spatio-temporal dual denoising framework for money laundering detection on evolving graphs, named EvoDen. / For spatial denoising, instead of relying on passive neighborhood aggregation, we design a risk-potential guided walk mechanism to extract denoised and suspicion-biased transaction sequences, enabling the model to isolate anomalous fund flows from noisy local neighborhoods. / We conduct experiments on three transaction datasets, and the results show that EvoDen outperforms state-of-the-art baselines in accurately identifying concealed money laundering entities.

[Paper](https://openreview.net/forum?id=PL6k93ECq7)

Classification / 分类：Fraud & AML / 欺诈检测与反洗钱 → Payment & Transaction Fraud / 支付与交易欺诈 → General / 综合

## Abstract / 摘要

Money laundering detection on financial transaction graphs is critical but challenging. Laundering activities often conceal illicit fund flows within dense legitimate transaction neighborhoods and disperse suspicious behaviors over extended time spans. These patterns cause weak illicit signals to be spatially diluted and temporally forgotten, limiting the effectiveness of standard graph learning methods in AML scenarios. In this paper, we propose a spatio-temporal dual denoising framework for money laundering detection on evolving graphs, named EvoDen. For spatial denoising, instead of relying on passive neighborhood aggregation, we design a risk-potential guided walk mechanism to extract denoised and suspicion-biased transaction sequences, enabling the model to isolate anomalous fund flows from noisy local neighborhoods. For temporal denoising, we propose a continual Transformer-based sequence learning method driven by a reconstruction objective, which learns denoised sequence representations while enabling latent-space replay of historical knowledge to mitigate representation drift. We conduct experiments on three transaction datasets, and the results show that EvoDen outperforms state-of-the-art baselines in accurately identifying concealed money laundering entities.
