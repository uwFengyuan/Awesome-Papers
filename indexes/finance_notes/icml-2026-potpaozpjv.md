# Reward Shaping Control Variates for Off-Policy Evaluation Under Sparse Rewards

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Empirically, we provide a systematic regime map across synthetic chains, a cancer simulator, 5 single-stock and 1 multi-stock DOW-30 trading environments and an ICU-sepsis benchmark showing that shaping-based OPE consistently outperforms DR in sparse-reward settings, while a hybrid estimator achieves state-of-the-art performance across sparse, noisy, and misspecified environments.

[Paper](https://openreview.net/forum?id=potpaozpjv)

Classification / 分类：Trading & Microstructure / 交易与市场微观结构 → Trading & Execution / 交易策略与执行 → General / 综合

## Abstract / 摘要

Off-policy evaluation (OPE) is essential for deploying reinforcement learning in safety-critical settings, yet existing estimators such as importance sampling and doubly robust (DR) often exhibit prohibitively high variance when rewards are sparse. In this work, we introduce Reward-Shaping Control Variates, a new family of unbiased estimators that leverage potential-based reward shaping to construct additional zero-mean control variates. We prove that shaped estimators always yields valid variance reduction, and that combining shaping-based and Q-based control variates strictly expands the variance-reduction subspace beyond DR and its minimax variant MRDR. Empirically, we provide a systematic regime map across synthetic chains, a cancer simulator, 5 single-stock and 1 multi-stock DOW-30 trading environments and an ICU-sepsis benchmark showing that shaping-based OPE consistently outperforms DR in sparse-reward settings, while a hybrid estimator achieves state-of-the-art performance across sparse, noisy, and misspecified environments. Our results highlight reward shaping as a powerful and interpretable tool for robust OPE, offering both theoretical guarantees and practical improvements in domains where standard estimators fail.
