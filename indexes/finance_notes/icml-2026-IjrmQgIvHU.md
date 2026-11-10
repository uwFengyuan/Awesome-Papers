# Identifiable Markov Switching Models with Instantaneous Effects and Exponential Families

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Experiments on synthetic benchmarks and a financial economics dataset demonstrate the effectiveness of our approach to detect latent regimes and discover causal structures from non-stationary time series.

[Paper](https://openreview.net/forum?id=IjrmQgIvHU)

Classification / 分类：Time Series / 时间序列 → Causality & Dynamics / 序列因果与动力学 → General / 综合

## Abstract / 摘要

Temporal systems often exhibit non-stationary behaviour, such as seasonal climate variation or glucose fluctuations in patients with type-1 diabetes.  One way to model non-stationarity is through discrete latent *regimes*, *i.e.*, stationary segments of time.  Such systems induce a *Markov Switching Model* (MSM), a class of Hidden Markov Models with autoregressive dependencies among latent regimes and observed variables.  Identifying latent regimes is challenging in the presence of frequent regime switches and nonlinear and non-Gaussian dynamics, particularly when there are *instantaneous effects* between the variables, *e.g.*, due to slow rates of measurements. In this work, we establish the identifiability of both latent regimes and regime-dependent causal structures under temporal regime dependencies, nonlinear lagged and instantaneous effects, and independent noise from the exponential family. Our identifiability theory subsumes non-temporal mixtures of causal models.  Furthermore, we introduce $\texttt{FlowMSM}$, a regime detection framework that can be paired with any stationary causal discovery method to recover regime-dependent causal structures.  Experiments on synthetic benchmarks and a financial economics dataset demonstrate the effectiveness of our approach to detect latent regimes and discover causal structures from non-stationary time series.
