# Density-Guided Robust Counterfactual Explanations on Tabular Data under Model Multiplicity

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.8579 (.001) black-box ensemble M. As shown in the results, Densi- Compas 7214 9 0.6753 (.003) tyFlow consistently achieves high validity while maintain- HELOC 10459 23 0.7106 (.002) Blood 748 4 0.7994 (.004) ing competitive costs. Specifically, on real-world tabular datasets such as Adult and Compas, our method

[Paper](https://openreview.net/forum?id=oAiq3HWlI6)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Counterfactual explanations (CEs) are essential for actionable recourse, yet their reliability is often compromised in low-density regions, where classifiers exhibit high variance. Unlike existing methods that rely on expensive ensemble intersections to define stability, we propose DensityFlow, a generative framework that constructs robust CEs by adhering to the high-confidence data manifold. Specifically, we model the counterfactual generation as continuous-time dynamics parameterized by Neural ODE, guided by a differentiable density score to actively avoid uncertain, low-density areas. This density score is learned via Noise Contrastive Estimation, effectively leveraging a $(K{+}1)$-way discriminator to estimate density ratios. For black-box settings, we introduce a local proxy distillation mechanism that aligns a lightweight surrogate with the target model strictly within the trajectory of CE generation, enabling efficient gradient-based optimization with minimal queries. Experiments demonstrate that \textit{DensityFlow} achieves superior validity under model multiplicity while significantly reducing query costs compared to ensemble-based baselines. Our implementation is available at \url{https://github.com/G-AILab/DensityFlow}.
