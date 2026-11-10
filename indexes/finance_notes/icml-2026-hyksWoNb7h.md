# DRL-STAF: A Deep Reinforcement Learning Framework for State-Aware Forecasting of Complex Multivariate Hidden Markov Processes

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：n real-world datasets. SMachine dataset Exchange dataset Traffic dataset Models Accuracy Precision Recall F1 MAE MSE MAE MSE MAE MSE Parallel HMM 76.37% 55.86% 90.95% 69.21% 0.0563 0.0056 8.6701 294.0451 5.5411 59.5501 Parallel HSMM

[Paper](https://openreview.net/forum?id=hyksWoNb7h)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Forecasting multivariate hidden Markov processes is challenging due to nonlinear and nonstationary observations, latent state transitions, and cross-sequence dependencies. While deep learning methods achieve strong predictive accuracy, they typically lack explicit state modeling, whereas Hidden Markov Models (HMMs) provide interpretable latent states but struggle with complex nonlinear emissions and scalability. To address these limitations, we propose DRL-STAF, a **D**eep **R**einforcement **L**earning based **ST**ate-**A**ware **F**orecasting framework that jointly predicts next-step observations and estimates the corresponding hidden states for complex multivariate hidden Markov processes. Specifically, DRL-STAF models complex nonlinear emissions using deep neural networks and estimates discrete hidden states using reinforcement learning, reducing the reliance on predefined transition structures and enabling flexible adaptation to diverse temporal dynamics. In particular, DRL-STAF mitigates the state-space explosion encountered by typical multivariate HMM-based methods. Extensive experiments demonstrate that DRL-STAF outperforms HMM variants, standalone deep learning models, and existing DL-HMM hybrids in most cases, while also providing reliable hidden-state estimates.
