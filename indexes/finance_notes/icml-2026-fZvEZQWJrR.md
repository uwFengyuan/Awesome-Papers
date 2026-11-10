# Correcting Split Selection in Online Decision Trees via Anytime-Valid Inference

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：g Split Selection in Online Decision Trees via Anytime-Valid Inference Datasets Method rbfm100k airlines creditcard hyper100k elec2 http bike chick fried nzenergy house abalone Inference time (ms, mean ± std) HT 0.124±0.011 0.028±0.008 0.010±0.001 0.066±0.004 0.031±0.004 0.006±0.001 0.024±0.004 0.018±0.004 0.026±0.004 0.041±0.004 0.030±0.003 0.021±0.003 AVTB 0.124±0.013 0.010±0.001 0.008±0.001 0.060±0.006 0.066±0.02

[Paper](https://openreview.net/forum?id=fZvEZQWJrR)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

Bagging-based ensembles, most notably Adaptive Random Forests, are among the strongest performers for learning from data streams. A common denominator across these methods is their reliance on Hoeffding Trees as base learners, which grow incrementally by testing whether a candidate split is significantly better than its alternatives using concentration inequalities. Despite their empirical success, existing Hoeffding Trees variants lack valid statistical guarantees. Current analyses rely on fixed-sample concentration bounds, while split decisions are made using data-dependent stopping rules, which invalidates their guarantees and can drive the probabilty of incorrect splits to one. We introduce a principled alternative based on \emph{anytime-valid inference}. Our method provides: (i) anytime-valid control of false splits under arbitrary data streams, including non-stationary settings; (ii) finite commitment time under a predictive advantage; and (iii) under stationary i.i.d.\ data, risk is monotone decreasing and strictly improves at every split. Empirically, we evaluate both standalone trees and their use within Adaptive Random Forests on non-stationary streams. Our method improves performance while producing substantially smaller trees.
