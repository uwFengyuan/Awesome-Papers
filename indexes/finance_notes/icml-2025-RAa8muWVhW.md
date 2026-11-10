# Advancing Constrained Monotonic Neural Networks: Achieving Universal Approximation Beyond Bounded Activations

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Beyond Bounded Activations Table 1. Test metrics across different datasets. The best-performing architecture per dataset is bolded. COMPAS Blog Feedback Loan Defaulter AutoMPG Heart Disease Method (Test Accuracy) (Test RMSE) (Test Accuracy) (Test MSE) (Test Accuracy) XGBoost 68.5% ± 0.1% 0.176 ± 0.005 63.7% ± 0.1% - - Certified 68.8% ± 0.2% 0.159

[Paper](https://openreview.net/forum?id=RAa8muWVhW)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Imposing input-output constraints in multi-layer perceptrons (MLPs) plays a pivotal role in many real world applications. Monotonicity in particular is a common requirement in applications that need transparent and robust machine learning models. Conventional techniques for imposing monotonicity in MLPs by construction involve the use of non-negative weight constraints and bounded activation functions, which poses well known optimization challenges.  In this work, we generalize previous theoretical results, showing that MLPs with non-negative weight constraint and activations that saturate on alternating sides are universal approximators for monotonic functions.  Additionally, we show an equivalence between saturation side in the activations and sign of the weight constraint. This connection allows us to prove that MLPs with convex monotone activations and non-positive constrained weights also qualify as universal approximators, in contrast to their non-negative constrained counterparts.  This results provide theoretical grounding to the empirical effectiveness observed in previous works, while leading to possible architectural simplification.  Moreover, to further alleviate the optimization difficulties, we propose an alternative formulation that allows the network to adjust its activations according to the sign of the weights. This eliminates the requirement for weight reparameterization, easing initialization and improving training stability.  Experimental evaluation reinforce the validity of the theoretical results, showing that our novel approach compares favorably to traditional monotonic architectures.
