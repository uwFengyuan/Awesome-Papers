# Expanding the Chaos: Neural Operator for Stochastic (Partial) Differential Equations

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Empirically, we achieve competitive accuracy across several tasks, including standard SPDE benchmarks and SDE-based diffusion one-step image sampling, topological graph interpolation, financial extrapolation, parameter estimation, and manifold SDE flood forecasting.

[Paper](https://openreview.net/forum?id=uZWpKAqjEg)

Classification / 分类：Time Series / 时间序列 → Causality & Dynamics / 序列因果与动力学 → Forecasting / 预测

## Abstract / 摘要

Stochastic differential equations (SDEs) and stochastic partial differential equations (SPDEs) are fundamental for modeling stochastic dynamics across the natural sciences and modern machine learning. Learning their solution operators with deep learning models promises fast solvers and new perspectives on classical learning tasks. In this work, we build on Wiener--chaos expansions (WCE) to design neural operator (NO) architectures for SDEs and SPDEs: we project driving noise paths onto orthonormal Wick--Hermite features and use NO backbones to parameterize the corresponding chaos coefficients governed by deterministic equations, enabling reconstruction of S(P)DE solutions from the observed noise trajectories. Empirically, we achieve competitive accuracy across several tasks, including standard SPDE benchmarks and SDE-based diffusion one-step image sampling, topological graph interpolation, financial extrapolation, parameter estimation, and manifold SDE flood forecasting. We further explore a law-matching setting where the Brownian trajectories paired with training solutions are unobserved, and show that the proposed framework remains effective by sampling auxiliary Brownian paths from the prescribed noise prior. These results suggest WCE-based neural operators are a practical and scalable approach to learning SDE/SPDE solution operators across domains. Our source code can be found in https://github.com/EEthanShi/SDENO.
