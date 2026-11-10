# Bayesian Persuasion for Algorithmic Recourse

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：provide a polynomial-time algorithm to approximate the optimal signaling policy (Section 4). 3. We empirically evaluate our persuasion mechanism on semi-synthetic data based on the Home Equity Line of Credit (HELOC) dataset, and find that the optimal signaling policy performs significantly better than the two natural alternatives across a wide range of instances (Section 5). 1.1 Related work Strategic responses to unknown predictive models. To the best of our knowledge, our work is the first to use tools from persuasion to model the strategic inte

[Paper](https://openreview.net/forum?id=Z6BFQqzwuS4)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

When subjected to automated decision-making, decision subjects may strategically modify their observable features in ways they believe will maximize their chances of receiving a favorable decision. In many practical situations, the underlying assessment rule is deliberately kept secret to avoid gaming and maintain competitive advantage. The resulting opacity forces the decision subjects to rely on incomplete information when making strategic feature modifications. We capture such settings as a game of Bayesian persuasion, in which the decision maker offers a form of recourse to the decision subject by providing them with an action recommendation (or signal) to incentivize them to modify their features in desirable ways. We show that when using persuasion, the decision maker and decision subject are never worse off in expectation, while the decision maker can be significantly better off. While the decision maker’s problem of finding the optimal Bayesian incentive compatible (BIC) signaling policy takes the form of optimization over infinitely many variables, we show that this optimization can be cast as a linear program over finitely-many regions of the space of possible assessment rules. While this reformulation simplifies the problem dramatically, solving the linear program requires reasoning about exponentially-many variables, even in relatively simple cases. Motivated by this observation, we provide a polynomial-time approximation scheme that recovers a near-optimal signaling policy. Finally, our numerical simulations on semi-synthetic data empirically demonstrate the benefits of using persuasion in the algorithmic recourse setting.
