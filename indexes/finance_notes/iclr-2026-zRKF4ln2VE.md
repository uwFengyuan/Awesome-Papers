# AlphaSAGE: Structure-Aware Alpha Mining via GFlowNets for Robust Exploration

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：The automated mining of predictive signals, or alphas, is a central challenge in quantitative finance. / Third, the standard RL objective of maximizing expected returns inherently drives policies towards a single optimal mode, directly contradicting the practical need for a diverse portfolio of non-correlated alphas. / Empirical results demonstrate that AlphaSAGE outperforms existing baselines in mining a more diverse, novel, and highly predictive portfolio of alphas, thereby proposing a new paradigm for automated alpha mining.

[Paper](https://openreview.net/forum?id=zRKF4ln2VE)

Classification / 分类：Alpha Mining / 量化因子挖掘 → Alpha Discovery / Alpha与因子发现 → RL factor discovery / 强化学习因子发现

## Abstract / 摘要

The automated mining of predictive signals, or alphas, is a central challenge in quantitative finance. While Reinforcement Learning (RL) has emerged as a promising paradigm for generating formulaic alphas, existing frameworks are fundamentally hampered by a triad of interconnected issues. First, they suffer from reward sparsity, where meaningful feedback is only available upon the completion of a full formula, leading to inefficient and unstable exploration. Second, they rely on semantically inadequate sequential representations of mathematical expressions, failing to capture the structure that determine an alpha's behavior. Third, the standard RL objective of maximizing expected returns inherently drives policies towards a single optimal mode, directly contradicting the practical need for a diverse portfolio of non-correlated alphas. To overcome these challenges, we introduce **AlphaSAGE** (**S**tructure-**A**ware Alpha Mining via **G**enerative Flow Networks for Robust **E**xploration), a novel framework is built upon three cornerstone innovations: (1) a structure-aware encoder based on Relational Graph Convolutional Network (RGCN); (2) a new framework with Generative Flow Networks (GFlowNets); and (3) a dense, multi-faceted reward structure. Empirical results demonstrate that AlphaSAGE outperforms existing baselines in mining a more diverse, novel, and highly predictive portfolio of alphas, thereby proposing a new paradigm for automated alpha mining. Our code is available at https://anonymous.4open.science/r/AlphaSAGE-3BA9.
