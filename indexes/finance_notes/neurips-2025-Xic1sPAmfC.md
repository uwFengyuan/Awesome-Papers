# Neural MJD: Neural Non-Stationary Merton Jump Diffusion for Time Series Prediction

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：models like DDPM [45], EDM [84], and flow matching (FM) [47]. We include recent neural ODE or SDE based learning methods such as NeuralCDE [33] and LatentSDE [59] for comparisons. NJ-ODE [85] was further included on the S&P 500 dataset. We also design a baseline model, Neural BS, which shares the same architecture as Neural MJD but omits the jump component. For DDPM, EDM, FM, Neural BS, and Neural MJD, we share the same transformer-based backbone to ensure a fair comparison. Since some datasets contain graph-structured data as seen in the following section, we incorporat

[Paper](https://openreview.net/forum?id=Xic1sPAmfC)

Classification / 分类：Time Series / 时间序列 → Causality & Dynamics / 序列因果与动力学 → Forecasting / 预测

## Abstract / 摘要

While deep learning methods have achieved strong performance in time series prediction, their black-box nature and inability to explicitly model underlying stochastic processes often limit their robustness handling non-stationary data, especially in the presence of abrupt changes. In this work, we introduce Neural MJD, a neural network based non-stationary Merton jump diffusion (MJD) model. Our model explicitly formulates forecasting as a stochastic differential equation (SDE) simulation problem, combining a time-inhomogeneous Itô diffusion to capture non-stationary stochastic dynamics with a time-inhomogeneous compound Poisson process to model abrupt jumps. To enable tractable learning, we introduce a likelihood truncation mechanism that caps the number of jumps within small time intervals and provide a theoretical error bound for this approximation. Additionally, we propose an Euler-Maruyama with restart solver, which achieves a provably lower error bound in estimating expected states and reduced variance compared to the standard solver. Experiments on both synthetic and real-world datasets demonstrate that Neural MJD consistently outperforms state-of-the-art deep learning and statistical learning methods. Our code is available at https://github.com/DSL-Lab/neural-MJD.
