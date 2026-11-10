# Optimizing Conditional Value-At-Risk of Black-Box Functions

NeurIPS 2021 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：aR. We empirically evaluate the performance of both CV-UCB and CV-TS in optimizing CVaR of synthetic benchmark functions, an optimization problem of the residuary resistance per unit weight of displacement of a yacht, a portfolio optimization problem, and a simulated robot task (Sec. 5). Related works. Existing solutions to optimizing a black-box function f (x, W) with an environ- mental random variable W are different in the assumptions about W and the objective function. Other than the aforementioned works of [4, 13] where we adopt the assumptions that the distribution of W is

[Paper](https://openreview.net/forum?id=Tc6Uk03Te7g)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

This paper presents two Bayesian optimization (BO) algorithms with theoretical performance guarantee to maximize the conditional value-at-risk (CVaR) of a black-box function: CV-UCB and CV-TS which are based on the well-established principle of optimism in the face of uncertainty and Thompson sampling, respectively. To achieve this, we develop an upper confidence bound of CVaR and prove the no-regret guarantee of CV-UCB by utilizing an interesting connection between CVaR and value-at-risk (VaR). For CV-TS, though it is straightforwardly performed with Thompson sampling, bounding its Bayesian regret is non-trivial because it requires a tail expectation bound for the distribution of CVaR of a black-box function, which has not been shown in the literature. The performances of both CV-UCB and CV-TS are empirically evaluated in optimizing CVaR of synthetic benchmark functions and simulated real-world optimization problems.
