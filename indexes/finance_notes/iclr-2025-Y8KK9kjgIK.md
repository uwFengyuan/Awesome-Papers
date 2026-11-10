# SigDiffusions: Score-Based Diffusion Models for Time Series via Log-Signature Embeddings

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.551±.028 SigDiffusion (ours) 0.278±.062 0.057±.001 DDO (γ = 1) 0.326±.102 0.094±.004 Exchange Rates Diffusion-TS 0.401±.196 0.120±.016 CSPD-GP (RNN) 0.500±.001 0.273±.100 CSPD-GP (Transformer) 0.500±.000 0.432±.074 SigDiffusion (ours) 0.350±.080 0.168±.001 DDO (γ = 10) 0.356

[Paper](https://openreview.net/forum?id=Y8KK9kjgIK)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Generation / 生成

## Abstract / 摘要

Score-based diffusion models have recently emerged as state-of-the-art generativemodels for a variety of data modalities. Nonetheless, it remains unclear how toadapt these models to generate long multivariate time series. Viewing a timeseries as the discretisation of an underlying continuous process, we introduceSigDiffusion, a novel diffusion model operating on log-signature embeddingsof the data. The forward and backward processes gradually perturb and denoiselog-signatures while preserving their algebraic structure. To recover a signal fromits log-signature, we provide new closed-form inversion formulae expressing thecoefficients obtained by expanding the signal in a given basis (e.g. Fourier ororthogonal polynomials) as explicit polynomial functions of the log-signature.Finally, we show that combining SigDiffusions with these inversion formulaeresults in high-quality long time series generation, competitive with the currentstate-of-the-art on various datasets of synthetic and real-world examples.
