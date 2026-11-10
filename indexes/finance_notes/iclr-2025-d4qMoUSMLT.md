# Efficient Training of Neural Stochastic Differential Equations by Matching Finite Dimensional Distributions

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：FDM (ours) .003, 1.51 .001, 0.428 .001, 0.410 .001, 0.349 .002, 0.522 the U.S. stock indices dataset are presented in Figures 4, 5, 6, 7, 8, 9, 10, 11, 12, and 13. Results for the exchange rates data are presented in Figure 14. Results for the energy price data are shown in Figures 15, 16, 17, 18, 19, and 20. Finally, results for the bonds data are presented in Figures 21, 22, and 23. We present additional qualitative results comparing real and generated sample paths. Results for the exchange rates data are presented in Figures 24 and 25. Similarly, Figures 26 through 30 show the sample paths for five featu

[Paper](https://openreview.net/forum?id=d4qMoUSMLT)

Classification / 分类：Time Series / 时间序列 → Causality & Dynamics / 序列因果与动力学 → Generation / 生成

## Abstract / 摘要

Neural Stochastic Differential Equations (Neural SDEs) have emerged as powerful mesh-free generative models for continuous stochastic processes, with critical applications in fields such as finance, physics, and biology. Previous state-of-the-art methods have relied on adversarial training, such as GANs, or on minimizing distance measures between processes using signature kernels. However, GANs suffer from issues like instability, mode collapse, and the need for specialized training techniques, while signature kernel-based methods require solving linear PDEs and backpropagating gradients through the solver, whose computational complexity scales quadratically with the discretization steps. In this paper, we identify a novel class of strictly proper scoring rules for comparing continuous Markov processes. This theoretical finding naturally leads to a novel approach called Finite Dimensional Matching (FDM) for training Neural SDEs. Our method leverages the Markov property of SDEs to provide a computationally efficient training objective. This scoring rule allows us to bypass the computational overhead associated with signature kernels and reduces the training complexity from $O(D^2)$ to $O(D)$ per epoch, where $D$ represents the number of discretization steps of the process. We demonstrate that FDM achieves superior performance, consistently outperforming existing methods in terms of both computational efficiency and generative quality.
