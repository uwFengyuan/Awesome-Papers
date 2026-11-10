# AlphaQCM: Alpha Discovery in Finance with Distributional Reinforcement Learning

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：For researchers and practitioners in finance, finding synergistic formulaic alphas is very important but challenging. / Empirical applications to real-world datasets demonstrate that our AlphaQCM method significantly outperforms its competitors, particularly when dealing with large datasets comprising numerous stocks.

[Paper](https://openreview.net/forum?id=3sXMHlhBSs)

Classification / 分类：Alpha Mining / 量化因子挖掘 → Alpha Discovery / Alpha与因子发现 → RL factor discovery / 强化学习因子发现

## Abstract / 摘要

For researchers and practitioners in finance, finding synergistic formulaic alphas is very important but challenging. In this paper, we reconsider the discovery of synergistic formulaic alphas from the viewpoint of sequential decision-making, and conceptualize the entire alpha discovery process as a non-stationary and reward-sparse Markov decision process. To overcome the challenges of non-stationarity and reward-sparsity, we propose the AlphaQCM method, a novel distributional reinforcement learning method designed to search for synergistic formulaic alphas efficiently. The AlphaQCM method first learns the Q function and quantiles via a Q network and a quantile network, respectively. Then, the AlphaQCM method applies the quantiled conditional moment method to learn unbiased variance from the potentially biased quantiles. Guided by the learned Q function and variance, the AlphaQCM method navigates the non-stationarity and reward-sparsity to explore the vast search space of formulaic alphas with high efficacy. Empirical applications to real-world datasets demonstrate that our AlphaQCM method significantly outperforms its competitors, particularly when dealing with large datasets comprising numerous stocks.
