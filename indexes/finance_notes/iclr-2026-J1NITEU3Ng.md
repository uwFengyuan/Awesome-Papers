# ATEX-CF: Attack-Informed Counterfactual Explanations for Graph Neural Networks

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：strate the limitations Alice Alice of existing counterfactual methods, consider a scenario from the Loan-Decision dataset 6 6 4 (Ma et al., 2025). Loan approval is granted when both conditions are met: income > 5 and degree > 3. Applicant Alice has 4 3 5 4 3 5 income 6 (satisfies condition) but degree 3 (fails). The model predicts rejection. Classi- Figure 1: Illustration of counterfactual limitations cal deletion-based counterfactual methods fail in the Loan Decision dataset. here–removing edges further reduces degree. Unconstrained edge additions (e.g., linking to a billionaire) succeed but can be implausible. Our method ATEX-CF identifies a feasible peer connection that serves as an actionable update and flips the prediction. Wh

[Paper](https://openreview.net/forum?id=J1NITEU3Ng)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Counterfactual explanations offer an intuitive way to interpret graph neural networks (GNNs) by identifying minimal changes that alter a model’s prediction, thereby answering “what must differ for a different outcome?”. In this work, we propose a novel framework, ATEX-CF that unifies adversarial attack techniques with counterfactual explanation generation—a connection made feasible by theirshared goal of flipping a node’s prediction, yet differing in perturbation strategy:adversarial attacks often rely on edge additions, while counterfactual methods typically use deletions. Unlike traditional approaches that treat explanation and attack separately, our method efficiently integrates both edge additions and deletions, grounded in theory, leveraging adversarial insights to explore impactful counterfactuals. In addition, by jointly optimizing fidelity, sparsity, and plausibility under a constrained perturbation budget, our method produces instance-level explanations that are both informative and realistic. Experiments on synthetic and real-world node classification benchmarks demonstrate that ATEX-CF generates faithful, concise, and plausible explanations, highlighting the effectiveness of integrating adversarial insights into counterfactual reasoning for GNNs.
