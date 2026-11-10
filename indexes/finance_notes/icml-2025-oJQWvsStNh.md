# Stable Fair Graph Representation Learning with Lipschitz Constraint

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：(a) German (b) Bail (c) Credit Figure 4. Training accuracy curve on German, Bail and Credit datasets. The shaded area represents the rolling standard deviation with a window size of 5, which can be used to measure the stability between epochs. Table 1. Comparison results of SFG with baseline fairness methods. In each row, the best result is indicated in bold, while the runner-up result is marked with an underline.

[Paper](https://openreview.net/forum?id=oJQWvsStNh)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Group fairness based on adversarial training has gained significant attention on graph data, which was implemented by masking sensitive attributes to generate fair feature views. However, existing models suffer from training instability due to uncertainty of the generated masks and the trade-off between fairness and utility. In this work, we propose a stable fair Graph Neural Network (SFG) to maintain training stability while preserving accuracy and fairness performance. Specifically, we first theoretically derive a tight upper Lipschitz bound to control the stability of existing adversarial-based models and employ a stochastic projected subgradient algorithm to constrain the bound, which operates in a block-coordinate manner. Additionally, we construct the uncertainty set to train the model, which can prevent unstable training by dropping some overfitting nodes caused by chasing fairness. Extensive experiments conducted on three real-world datasets demonstrate that SFG is stable and outperforms other state-of-the-art adversarial-based methods in terms of both fairness and utility performance. Codes are available at https://github.com/sh-qiangchen/SFG.
