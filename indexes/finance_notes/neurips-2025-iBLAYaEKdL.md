# Constrained Posterior Sampling: Time Series Generation with Hard Constraints

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Empirically, CPS outperforms state-of-the-art methods in sample quality and similarity to real time series by around 70\% and 22\%, respectively, on real-world stocks, traffic, and air quality datasets.

[Paper](https://openreview.net/forum?id=iBLAYaEKdL)

Classification / 分类：Time Series / 时间序列 → Generation & Simulation / 序列生成与仿真 → Generation / 生成

## Abstract / 摘要

Generating realistic time series samples is crucial for stress-testing models and protecting user privacy by using synthetic data. In engineering and safety-critical applications, these samples must meet certain hard constraints that are domain-specific or naturally imposed by physics or nature. Consider, for example, generating electricity demand patterns with constraints on peak demand times. This can be used to stress-test the functioning of power grids during adverse weather conditions. Existing approaches for generating constrained time series are either not scalable or degrade sample quality. To address these challenges, we introduce Constrained Posterior Sampling (CPS), a diffusion-based sampling algorithm that aims to project the posterior mean estimate into the constraint set after each denoising update. Notably, CPS scales to a large number of constraints ($\sim100$) without requiring additional training. We provide theoretical justifications highlighting the impact of our projection step on sampling. Empirically, CPS outperforms state-of-the-art methods in sample quality and similarity to real time series by around 70\% and 22\%, respectively, on real-world stocks, traffic, and air quality datasets.
