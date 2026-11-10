# Cooperative Bargaining Games Without Utilities: Mediated Solutions from Direction Oracles

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Finally, we conduct experiments in two domains, multi-agent formation assignment and mediated stock portfolio allocation, which validate these theoretical results.

[Paper](https://openreview.net/forum?id=DcpUkPHRJw)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

Cooperative bargaining games are widely used to model resource allocation and conflict resolution. Traditional solutions assume the mediator can access agents’ utility function values and gradients. However, there is an increasing number of settings, such as human-AI interactions, where utility values may be inaccessible or incomparable due to unknown, nonaffine transformations. To model such settings, we consider that the mediator has access only to agents' $\textit{most preferred directions}-$normalized utility gradients in the decision space. To this end, we propose a cooperative bargaining algorithm where a mediator has access to only the direction oracle of each agent.  We prove that unlike popular approaches such as the Nash and Kalai-Smorodinsky bargaining solutions, our approach is invariant to monotonic nonaffine transformations, and that under strong convexity and smoothness assumptions, this approach enjoys global asymptotic convergence to Pareto stationary solutions. Moreover, we show that the bargaining solutions found by our algorithm also satisfy the axioms of symmetry and (under slightly stronger conditions) independence of irrelevant alternatives, which are popular in the literature. Finally, we conduct experiments in two domains, multi-agent formation assignment and mediated stock portfolio allocation, which validate these theoretical results.
