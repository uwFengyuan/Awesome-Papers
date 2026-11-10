# SurvivalPFN: Amortizing Survival Prediction via In-Context Bayesian Inference

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：[95]. • kidney_transplant: The kidney_transplant dataset records post-transplant death times with recipient age, gender, and race [49]. • credit: The PySurvival [19] credit-risk dataset adapts the German Credit data to model the time until a loan is fully repaid. • PDM: The PySurvival [19] predictive-maintenance (PDM) dataset models the time until an industrial machine breaks. • COVID: The COVID-19 Asian discharge dataset models time to hospital discharge for patients with COVID-19 diagnosis [52]. • WHAS: T

[Paper](https://openreview.net/forum?id=bJ348fNOVg)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Survival analysis provides a powerful statistical framework for modeling time-to-event outcomes in the presence of censoring. However, selecting an appropriate estimator from the many specialized survival approaches often requires substantial methodological and domain expertise. We introduce SurvivalPFN, a prior-data fitted network that amortizes Bayesian inference for censored observations through in-context learning. SurvivalPFN is pretrained on a diverse family of synthetic, identifiable, and right-censored data-generating processes, enabling it to amortize survival analysis in a single forward pass during inference. As a result, the model adapts to the effective complexity of each dataset without task-specific training or hyperparameter tuning, avoids restrictive parametric assumptions, and produces calibrated survival distributions. In a large-scale benchmark spanning 61 survival datasets, 21 methods, and 5 evaluation metrics, SurvivalPFN achieves strong predictive performance and often improves upon established survival models. These results suggest that SurvivalPFN offers a principled and practical foundation model for survival analysis, with potential applications in high-impact domains such as healthcare, finance, and engineering.
