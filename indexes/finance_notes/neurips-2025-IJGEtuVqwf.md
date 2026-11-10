# Robust Reinforcement Learning in Finance:  Modeling Market Impact with Elliptic Uncertainty Sets

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：In financial applications, reinforcement learning (RL) agents are commonly trained on historical data, where their actions do not influence prices. / However, during deployment, these agents trade in live markets where their own transactions can shift asset prices, a phenomenon known as market impact. / Experiments on single-asset and multi-asset trading tasks demonstrate that our method achieves superior Sharpe ratio and remains robust under increasing trade volumes, offering a more faithful and scalable approach to RL in financial markets.

[Paper](https://openreview.net/forum?id=IJGEtuVqwf)

Classification / 分类：Trading & Microstructure / 交易与市场微观结构 → Trading & Execution / 交易策略与执行 → General / 综合

## Abstract / 摘要

In financial applications, reinforcement learning (RL) agents are commonly trained on historical data, where their actions do not influence prices. However, during deployment, these agents trade in live markets where their own transactions can shift asset prices, a phenomenon known as market impact. This mismatch between training and deployment environments can significantly degrade performance.  Traditional robust RL approaches address this model misspecification by optimizing the worst-case performance over a set of uncertainties, but typically rely on symmetric structures that fail to capture the directional nature of market impact. To address this issue, we develop a novel class of elliptic uncertainty sets. We establish both implicit and explicit closed-form solutions for the worst-case uncertainty under these sets, enabling efficient and tractable robust policy evaluation. Experiments on single-asset and multi-asset trading tasks demonstrate that our method achieves superior Sharpe ratio and remains robust under increasing trade volumes, offering a more faithful and scalable approach to RL in financial markets.
