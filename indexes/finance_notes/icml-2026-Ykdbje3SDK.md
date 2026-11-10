# Long-term Fairness with Selective Labels

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：However, in scenarios such as hiring or lending, the labels (e.g., ability to repay the loan) are _selective labels_ as they are only revealed based on positive decisions (e.g., when a loan is granted).

[Paper](https://openreview.net/forum?id=Ykdbje3SDK)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

Long-term fairness algorithms aim to satisfy fairness beyond static and short-term notions by accounting for the dynamics between decision-making policies and population behavior. Most previous approaches evaluate performance and fairness measures from observable features and a label, which is assumed to be fully observed. However, in scenarios such as hiring or lending, the labels (e.g., ability to repay the loan) are _selective labels_ as they are only revealed based on positive decisions (e.g., when a loan is granted). In this paper, we study long-term fairness in the selective labels setting and analytically show that naive solutions do not guarantee fairness. To address this gap, we then introduce a novel framework that leverages both the observed data and a label predictor model to estimate the true fairness measure value by decomposing it into the observed fairness and bias from label predictions. This allows us to derive  sufficient conditions to satisfy true fairness from observable quantities by using the confidence in the predictor model.  Finally,  we rely on our theoretical results to propose a novel reinforcement learning algorithm for effective long-term fair decision-making with selective labels. In semisynthetic environments, the proposed algorithm reached comparable fairness and performance to an agent with oracle access to the true labels.
