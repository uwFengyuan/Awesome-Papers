# Reinforcement Learning with Imperfect Transition Predictions: A Bellman-Jensen Approach

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：In many real-world applications, such as energy management and stock investment, agents can access multi-step predictions of future states, which provide additional advantages for decision making.

[Paper](https://openreview.net/forum?id=DYuPwwDy9n)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → Stock Movement & Returns / 股价方向与收益预测 → General / 综合

## Abstract / 摘要

Traditional reinforcement learning (RL) assumes the agents make decisions based on Markov decision processes (MDPs) with one-step transition models. In many real-world applications, such as energy management and stock investment, agents can access multi-step predictions of future states, which provide additional advantages for decision making. However, multi-step predictions are inherently high-dimensional: naively embedding these predictions into an MDP leads to an exponential blow-up in state space and the curse of dimensionality. Moreover, existing RL theory provides few tools to analyze prediction-augmented MDPs, as it typically works on one-step transition kernels and cannot accommodate multi-step predictions with errors or partial action-coverage. We address these challenges with three key innovations: First, we propose the \emph{Bayesian value function} to characterize the optimal prediction-aware policy tractably. Second, we develop a novel \emph{Bellman–Jensen Gap} analysis on the Bayesian value function, which enables characterizing the value of imperfect predictions. Third, we introduce BOLA (Bayesian Offline Learning with Online Adaptation), a two-stage model-based RL algorithm that separates offline Bayesian value learning from lightweight online adaptation to real-time predictions. We prove that BOLA remains sample-efficient even under imperfect predictions. We validate our theory and algorithm on synthetic MDPs and a real-world wind energy storage control problem.
