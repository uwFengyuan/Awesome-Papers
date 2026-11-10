# Error Propagation in Dynamic Programming: From Stochastic Control to American Option Pricing

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Finally, we illustrate how our analysis naturally applies to a key financial application: the pricing of American options.

[Paper](https://openreview.net/forum?id=FB5LYFzu33)

Classification / 分类：Derivatives & Hedging / 衍生品定价与对冲 → Option Pricing & PDEs / 期权定价与PDE → General / 综合

## Abstract / 摘要

This paper investigates theoretical and methodological foundations for stochastic optimal control (SOC) in discrete time. We start formulating the control problem in a general dynamic programming framework, introducing the mathematical structure needed for a detailed convergence analysis. The associate value function is estimated through a sequence of approximations combining nonparametric regression methods and Monte Carlo subsampling. The regression step is performed within reproducing kernel Hilbert spaces (RKHSs), exploiting the classical KRR algorithm, while Monte Carlo sampling methods are introduced to estimate the continuation value. To assess the accuracy of our value function estimator, we propose a natural error decomposition and rigorously control the resulting error terms at each time step. We then analyze how this error propagates backward in time-from maturity to the initial stage-a relatively underexplored aspect of the SOC literature. Finally, we illustrate how our analysis naturally applies to a key financial application: the pricing of American options.
