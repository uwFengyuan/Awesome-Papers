# Retrieval-Augmented Diffusion Modeling for Stochastic Discount Factor Portfolios

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：In this work, we study portfolio optimization under the stochastic discount factor (SDF) framework by learning market state representations that capture the underlying risk structures of financial data. / This is challenging due to several factors: financial markets exhibit non-stationary dynamics with shifting regimes, multimodal inputs such as price and news data often contain stochastic noise, and existing diffusion-based approaches, while effective for modeling stochastic dynamics, rely on assumptions such as isotropic Gaussian noise that fail to capture the state-dependent nature of financial uncertainty.

[Paper](https://openreview.net/forum?id=Dk8yYYJtw0)

Classification / 分类：Asset Pricing / 资产定价 → Pricing Models & Risk Premia / 定价模型与风险溢价 → General / 综合

## Abstract / 摘要

In this work, we study portfolio optimization under the stochastic discount factor (SDF) framework by learning market state representations that capture the underlying risk structures of financial data. This is challenging due to several factors: financial markets exhibit non-stationary dynamics with shifting regimes, multimodal inputs such as price and news data often contain stochastic noise, and existing diffusion-based approaches, while effective for modeling stochastic dynamics, rely on assumptions such as isotropic Gaussian noise that fail to capture the state-dependent nature of financial uncertainty. To address these challenges, we introduce RADAR, a retrieval-augmented diffusion framework that learns market representations by conditioning on similar historical regimes. RADAR leverages retrieval to construct context-dependent noise distributions, applies conditional diffusion to denoise multimodal representations, and initializes the diffusion process using empirical statistics to reflect state-dependent uncertainty. Experiments show that RADAR achieves state-of-the-art performance on key risk-adjusted metrics while producing economically meaningful signals on asset returns and correlations.
