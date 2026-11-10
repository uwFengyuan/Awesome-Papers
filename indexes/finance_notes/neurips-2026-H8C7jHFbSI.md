# AlphaPareto: Formulaic Alpha Discovery with LLM-Guided Multi-Objective Reinforcement Learning

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Formulaic alpha discovery is a core challenge in quantitative trading, as identifying alphas that work well together remains difficult.

[Paper](https://openreview.net/forum?id=H8C7jHFbSI)

Classification / 分类：Alpha Mining / 量化因子挖掘 → Alpha Discovery / Alpha与因子发现 → LLM factor discovery / LLM因子发现

## Abstract / 摘要

Formulaic alpha discovery is a core challenge in quantitative trading, as identifying alphas that work well together remains difficult. Recent reinforcement learning (RL) methods formulate this task as a Markov decision process (MDP), but two important issues remain unresolved. First, as the alpha pool evolves, the reward function changes accordingly, making the MDP inherently non-stationary. Second, most existing methods optimize a single objective, typically predictive power, while ignoring other important properties of a high-quality alpha pool. Motivated by these challenges, we propose AlphaPareto, an RL method for formulaic alpha discovery. To address non-stationarity, AlphaPareto augments the state to include both the alpha under construction and the current alpha pool, and applies a large language model (LLM) to encode the pool. This design allows the agent to adapt to the evolving search environment. To overcome the limitation of single-objective reward design, AlphaPareto replaces the scalar reward with a multi-objective vector-valued reward that simultaneously captures predictive power, temporal stability, perturbation robustness, and diversity, and optimizes these objectives through a Pareto-regularized learning procedure. Empirical applications to real-world datasets show that our AlphaPareto method outperforms its competitors.
