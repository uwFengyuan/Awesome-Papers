# Desirable Effort Fairness and Optimality Trade-offs in Strategic Learning

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：, we additionally compare realized losses with the theoretical bounds in Table 1. Setup. We use the TAIWAN credit-default dataset, which contains financial and demographic in- formation about clients and is commonly used to predict whether a client is likely to default on repayment. We study three population partitions based on age, education, and marital status. Each partition induces a corresponding pair of projection matrices, Π1 , Π2 . Similarly to the previ- ous experiment, we compute the β-fair equilibrium for various cost matrices, A1 , A2 and desirable feature sets ΠD . A full description of the setup can be found in Section A.5. Results. Figure 4 compares the realized losses with the theoretical upper bounds from Table 1. The main

[Paper](https://openreview.net/forum?id=GdqrQ75Gg8)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Strategic classification examines how decision rules interact with agents who strategically adapt their features. Most existing models focus on maximizing predictive performance, assuming agents best respond to the learned classifier. However, real decision-making systems are rarely optimized solely for accuracy: ethical, economic, and institutional considerations often make some feature changes more desirable than others. At the same time, principals may wish to incentivize these changes fairly across heterogeneous agents. While prior work has studied causal structure between features, notions of desirability, and information disparities in isolation, this work initiates a unified treatment of these components within a single framework. We frame the problem as a constrained optimization problem that captures the trade-offs between optimality, desirability, and fairness. We provide theoretical guarantees on the principal's optimality loss constrained to a particular desirability fairness tolerance for multiple broad classes of fairness measures. Finally, through experiments on real datasets, we show the explicit tradeoff between maximizing accuracy and fairness in desirability effort.
