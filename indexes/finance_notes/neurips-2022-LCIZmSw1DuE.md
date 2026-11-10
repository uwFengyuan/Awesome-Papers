# Fair and Optimal Decision Trees: A Dynamic Programming Approach

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：DPF Dataset a |D| |F| d=2 d=2 d=3 d=4 Adult Gender 45222 17 > 1h <1 <1 1012 Bank Marketing Married 45211 46 > 1h <1 2 > 1h Communities & Crime Race 1994 97 > 1h <1 4 1261 COMPAS recid. Race 6172 9 > 1h <1 <1 9 COMPAS viol. recid. Race 4020 9

[Paper](https://openreview.net/forum?id=LCIZmSw1DuE)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Bank Marketing & Churn / 银行营销与客户流失 → General / 综合

## Abstract / 摘要

Interpretable and fair machine learning models are required for many applications, such as credit assessment and in criminal justice. Decision trees offer this interpretability, especially when they are small. Optimal decision trees are of particular interest because they offer the best performance possible for a given size. However, state-of-the-art algorithms for fair and optimal decision trees have scalability issues, often requiring several hours to find such trees even for small datasets. Previous research has shown that dynamic programming (DP) performs well for optimizing decision trees because it can exploit the tree structure. However, adding a global fairness constraint to a DP approach is not straightforward, because the global constraint violates the condition that subproblems should be independent. We show how such a constraint can be incorporated by introducing upper and lower bounds on final fairness values for partial solutions of subproblems, which enables early comparison and pruning. Our results show that our model can find fair and optimal trees several orders of magnitude faster than previous methods, and now also for larger datasets that were previously beyond reach. Moreover, we show that with this substantial improvement our method can find the full Pareto front in the trade-off between accuracy and fairness.
