# When Tabular Foundation Models Meet Strategic Tabular Data: A Prior Alignment Approach

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：that do not involve fea- sion rules. Formal definitions and details are included in ture manipulation, such as Bank-Marketing and Phishing. Appendix H.4. Detailed dataset descriptions are provided in Appendix H.1. Methods. We compare the proposed SPN against two broad classes of tabular learning approaches. First, we consider

[Paper](https://openreview.net/forum?id=jlQeiq1azU)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Bank Marketing & Churn / 银行营销与客户流失 → General / 综合

## Abstract / 摘要

Tabular foundation models based on pretrained prior-data fitted networks (PFNs) have shown strong generalization on diverse tabular tasks, but they are typically designed for non-strategic settings where data distributions are independent of deployed classifiers. In many real-world decision scenarios, however, individuals may strategically modify their features after deployment to obtain favorable outcomes, inducing a post-deployment distribution shift. This paper studies whether PFN-style tabular foundation models can generalize to such strategic tabular data. We show that strategic manipulation creates a fundamental mismatch between the non-strategic prior learned during pretraining and the post-manipulation strategic prior encountered at deployment, which leads to an irreducible structural prediction bias. To address this issue, we propose the Strategic Prior-data Fitted Network (SPN), an inference-time strategy-aware framework that adapts tabular foundation models to strategic environments without retraining or architectural modification. SPN constructs strategic in-context examples to approximate post-manipulation inputs and aligns PFN predictions with the induced strategic distribution via in-context learning, with theoretical guarantees on bias reduction. Experiments on real-world and synthetic tabular datasets show that SPN consistently improves robustness and predictive performance under strategic manipulation compared with both tabular foundation models and classical tabular methods.
