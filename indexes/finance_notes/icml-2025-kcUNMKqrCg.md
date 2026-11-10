# Conditional Diffusion Model with Nonlinear Data Transformation for Time Series Forecasting

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：tricity. Results of all baselines are from (Shen et al., 2024) Method NorPool Caiso Traffic Electricity Weather Exchange ETTh1 ETTm1 Wind Rank Ours 0.531(1) 0.094(1) 0.374(2) 0.145(1) 0.296(1) 0.016(1) 0.405(1) 0.340(2) 0.988(5) 1.7 mr-Diff 0.645(3) 0.127(4) 0.474(7) 0.155(4) 0.296(1) 0.016(1) 0.411(4) 0.340(2) 0.881(1) 3.0 TimeDiff 0.665(5) 0.136(7) 0.564(8) 0.193(6) 0.311(3) 0.018(7)

[Paper](https://openreview.net/forum?id=kcUNMKqrCg)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time-series forecasting finds application across domains such as finance, climate science, and energy systems. We introduce the Conditional Diffusion  with Nonlinear Data Transformation Model (CN-Diff), a generative framework that employs novel nonlinear transformations and learnable conditions in the forward process for time series forecasting. A new loss formulation for training is proposed, along with a detailed derivation of both forward and reverse process. The new additions improve the diffusion model's capacity to capture complex time series patterns, thus simplifying the reverse process. Our novel condition facilitates learning an efficient prior distribution. This also reduces the gap between the true negative log-likelihood and its variational approximation. CN-Diff is shown to perform better than other leading time series models on nine real-world datasets. Ablation studies are conducted to elucidate the role of each component of CN-Diff.
