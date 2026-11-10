# Individual Fairness In Strategic Classification

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：7 6 Experiment Dataset and Implementation. In this section, we conduct experiments on two real-world datasets to evaluate the effectiveness of our proposed methods. The first dataset is the FICO dataset, pre- processed by [15]. This dataset provides the cumulative distribution of credit scores across different racial groups. In our experiments, we generate 5,000 data points according to the distributions for the racial groups Black and Non-Hispanic White. Each feature vector is defined as x := [κ, a], where κ denotes the credit score and

[Paper](https://openreview.net/forum?id=sGY0TisiMB)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Strategic classification, where individuals modify their features to influence machine learning (ML) decisions, presents critical fairness challenges. While group fairness in this setting has been widely studied, individual fairness remains underexplored. We analyze threshold-based classifiers and prove that deterministic thresholds violate individual fairness. Then, we investigate the possibility of using a randomized classifier to achieve individual fairness. We introduce conditions under which a randomized classifier ensures individual fairness and leverage these conditions to find an optimal and individually fair randomized classifier through a linear programming problem. Additionally, we demonstrate that our approach can be extended to group fairness notions. Experiments on real-world datasets confirm that our method effectively mitigates unfairness and improves the fairness-accuracy trade-off.
