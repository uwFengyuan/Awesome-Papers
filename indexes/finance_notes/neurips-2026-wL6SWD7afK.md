# CounterFlowNet: From Minimal Changes to Meaningful Counterfactual Explanations

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：valid domain V (d). Upon Method Spars.(%)↑ Div.(%)↑ H. Mean(%)↑ Val.(%)↑ Cov.(%)↑ Unary(%)↑ reaching a terminal state x′ , we compute the composite re- German Credit (Logistic Regression) ward R(x′ | x0 , y ′ ) (Equation (7)). The policy parameters L2C 61.35 37.31 46.39 100.00 100.00 99.06 θ and flow estimator parameters ψ are updated jointly via DICE-R 88.23 15.29 26.06 100.00 100.00 90.81

[Paper](https://openreview.net/forum?id=wL6SWD7afK)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Counterfactual explanations (CFs) provide human-interpretable insights into model's predictions by identifying minimal changes to input features that would alter the model's output. However, existing methods struggle to generate multiple high-quality explanations that (1) affect only a small portion of the features, (2) can be applied to tabular data with heterogeneous features, and (3) are consistent with the user-defined constraints. We proposeCounterFlowNet, a generative approach that formulates CF generation as sequential feature modification using conditional Generative Flow Networks (GFlowNet). CounterFlowNet is trained to sample CFs proportionally to a user-specified reward function that can encode key CF desiderata: validity, sparsity, proximity and plausibility, encouraging high-quality explanations. The sequential formulation yields highly sparse edits, while a unified action space seamlessly supports continuous and categorical features. Moreover, actionability constraints, such as immutability and monotonicity of features, can be enforced at inference time via action masking, without retraining. Experiments on eight datasets under two evaluation protocols demonstrate that CounterFlowNet achieves superior trade-offs between validity, sparsity, plausibility, and diversity with full satisfaction of the given constraints.
