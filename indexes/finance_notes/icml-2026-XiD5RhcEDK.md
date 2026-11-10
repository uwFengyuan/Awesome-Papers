# Fair Decisions from Calibrated Scores: Achieving Optimal Classification While Satisfying Sufficiency

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：erg et al., 2017). Nevertheless, among classifiers vided in Appendix I. that satisfy sufficiency, the extent to which separation is violated can vary. In this section, we adopt the deviation- 7.1. FICO from-separation measure ∆sep (R) introduced in (Benger & Ligett, 2025), and study classifiers that satisfy predictive FICO scores are used to predict creditworthiness. We use parity while minimizing ∆sep (R). We show that the optimal the aggregate score statistics from Barocas et al. (2023), classifier is attained on the bounda

[Paper](https://openreview.net/forum?id=XiD5RhcEDK)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Binary classification based on predicted probabilities (scores) is a fundamental task in supervised machine learning. While thresholding scores is Bayes-optimal in the unconstrained setting, using a single threshold generally violates statistical group fairness constraints. Under independence (statistical parity) and separation (equalized odds), such thresholding suffices when the scores already satisfy the corresponding criterion. However, this does not extend to sufficiency: even perfectly group-calibrated scores---including true class probabilities---violate predictive parity after thresholding. In this work, we present an exact solution for optimal binary (randomized) classification under sufficiency, assuming finite sets of group-calibrated scores. We provide a geometric characterization of the feasible pairs of positive predictive value (PPV) and false omission rate (FOR) achievable by such classifiers, and use it to derive a simple post-processing algorithm that attains the optimal classifier using only group-calibrated scores and group membership. Finally, since sufficiency and separation are generally incompatible, we identify the classifier that minimizes deviation from separation subject to sufficiency, and show that it can also be obtained by our algorithm, often achieving performance comparable to the optimum.
