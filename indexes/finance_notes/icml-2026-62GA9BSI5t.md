# Primal-Spectral Generative Modeling: Fast Analytical Generation via Pseudoinverse Lévy Inversion

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We test our PriSpecNet in two applications: for time series, it unifies generation and forecasting, outperforming state-of-the-art (SOTA) baselines with Context-FID reductions of 50.0\%, 41.5\%, 80.6\%, and 63.1\% on Sines, Solar, ETTh, and Stock benchmarks, respectively, also decreasing forecasting MSE by 29.8\% on Solar and 23.8\% on Stock.

[Paper](https://openreview.net/forum?id=62GA9BSI5t)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → Stock Movement & Returns / 股价方向与收益预测 → General / 综合

## Abstract / 摘要

A probability distribution $\mathbb{P}$ is a measure on a $\sigma$-algebra, assigning mass to sets rather than points, which poses a challenge for the training of neural networks that often struggle to reconstruct the global topology of continuous manifolds from sparse samples. We mitigate this issue by transforming $\mathbb{P}$ into a continuous function via spectral methods, providing theoretical guarantees for the convergence of the learned distribution to the true distribution. Specifically, we introduce a network, PriSpecNet, with a single-function evaluation (1-NFE) Pseudoinverse L\'evy Inversion (PiLI) solver that regards generation as a fast analytical problem, eliminating the need for iterative numerical integration while maintaining full compatibility with the stochastic interpolants. We test our PriSpecNet in two applications: for time series, it unifies generation and forecasting, outperforming state-of-the-art (SOTA) baselines with Context-FID reductions of 50.0\%, 41.5\%, 80.6\%, and 63.1\% on Sines, Solar, ETTh, and Stock benchmarks, respectively, also decreasing forecasting MSE by 29.8\% on Solar and 23.8\% on Stock. For ImageNet $256 \times 256$, 1-NFE PiLI achieves a competitive FID of **1.66** using only **26** Gflops, representing a **170$\times$** reduction in total Gflops compared to the 4,436 Gflops required by the 25-NFE DPM-Solver++.
