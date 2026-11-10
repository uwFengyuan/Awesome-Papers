# DiffPTS: Rethinking Diffusion ELBO for Probabilistic Time Series Forecasting

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：4 Experiments 4.1 Experiment Setup Datasets. Following previous work [8, 33], we evaluate on nine real-world datasets: ETT {h1, h2, m1, m2}, Electricity (ECL), Influenza-like Illness (ILI), Exchange Rate (EXR), Traffic, and Solar Energy (Solar). All experiments adopt a input sequence length of 168 time steps, ILI uses 32 prediction steps, and other datasets follow 192 prediction steps. Data splits follow domain conventions: ETT datasets use 12/4/4-month partitions for training, validation, and testing; all other datasets employ a chronological 7:1:2 split ratio. We provide dataset details in Appendix B.1. Baselines.

[Paper](https://openreview.net/forum?id=x7OutBc7Vk)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Probabilistic time series forecasting requires modeling and predicting complex and time-varying distributions. Recently, Denoising Diffusion Probabilistic Model~(DDPM)-based approaches have shown promise by equipping the diffusion process with pretrained mean and variance estimators to accommodate distributional shift. However, these methods typically follow the standard DDPM framework and consider only partial components of the evidence lower bound (ELBO), treating the training of estimators as designed regression tasks separate from the variational inference framework.  To address this, we rethink the ELBO under the Location-Scale Noise Model (LSNM) and find that it naturally induces a Gaussian negative log likelihood objective for the estimators and inherently defines a joint training objective that unifies recent the diffusion paradigms for probabilistic forecasting. Building on this principled ELBO reformulation, we propose DiffPTS, a general framework that enables end-to-end optimization of all components within the ELBO. Across multiple benchmarks, DiffPTS consistently outperforms recent models, achieving state-of-the-art performance with an average CRPS/MSE reduction of over 14.53\%/16.55\% compared to existing diffusion-based methods. The code is provided at \url{https://anonymous.4open.science/r/DiffPTS}.
