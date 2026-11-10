# Learning Classifiers That Induce Markets

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：When learning is used to inform decisions about humans, such as for loans, hiring, or admissions, this can incentivize users to strategically modify their features, at a cost, to obtain positive predictions.

[Paper](https://openreview.net/forum?id=GA7JfZyJMw)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

When learning is used to inform decisions about humans, such as for loans, hiring, or admissions, this can incentivize users to strategically modify their features, at a cost, to obtain positive predictions. The common assumption is that the function governing costs is exogenous, fixed, and predetermined. We challenge this assumption, and assert that costs emerge as a *result* of deploying a classifier. Our idea is simple: when users seek positive predictions, this creates demand for important features; and if features are available for purchase, then a market will form, and competition will give rise to prices. We extend the strategic classification framework to support this notion, and study learning in a setting where a classifier can induce a market for features. We present an analysis of the learning task, devise an algorithm for computing market prices, propose a differentiable learning framework, and conduct experiments to explore our novel setting and approach.
