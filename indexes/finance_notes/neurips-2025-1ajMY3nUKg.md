# Tight Lower Bounds and Improved Convergence in Performative Prediction

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ining snapshots. Our theoretical contri- butions include establishing a new upper bound for last-iterate methods, demonstrating the tightness 4 Give me Some Credit Dataset, 2011: https://www.kaggle.com/c/GiveMeSomeCredit 9 of this bound, and surpassing existing lower bounds through the aggregation of historical datasets. We have also presented the first lower bound analysis for Repeated Risk Minimization (RRM) within the class of Affine Risk Minimizers. Our empirical results validate the theoretical findings,

[Paper](https://openreview.net/forum?id=1ajMY3nUKg)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Performative prediction is a framework accounting for the shift in the data distribution induced by the prediction of a model deployed in the real world. Ensuring convergence to a stable solution—one at which the post‑deployment data distribution no longer changes—is crucial in settings where model predictions can influence future data. This paper, for the first time, extends the Repeated Risk Minimization (RRM) algorithm class by utilizing historical datasets from previous retraining snapshots, yielding a class of algorithms that we call Affine Risk Minimizers that converges to a performatively stable point for a broader class of problems. We introduce a new upper bound for methods that use only the final iteration of the dataset and prove for the first time the tightness of both this new bound and the previous existing bounds within the same regime. We also prove that our new algorithm class can surpass the lower bound for standard RRM, thus breaking the prior lower bound, and empirically observe faster convergence to the stable point on various performative prediction benchmarks. We offer at the same time the first lower bound analysis for RRM within the class of Affine Risk Minimizers, quantifying the potential improvements in convergence speed that could be achieved with other variants in our scheme.
