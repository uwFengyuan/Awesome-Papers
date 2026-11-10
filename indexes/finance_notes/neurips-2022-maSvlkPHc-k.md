# On the Discrimination Risk of Mean Aggregation Feature Imputation in Graphs

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We evaluate the fairness and accuracy of our solution on synthetic and real-world credit networks.

[Paper](https://openreview.net/forum?id=maSvlkPHc-k)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

In human networks, nodes belonging to a marginalized group often have a disproportionate rate of unknown or missing features. This, in conjunction with graph structure and known feature biases, can cause graph feature imputation algorithms to predict values for unknown features that make the marginalized group's feature values more distinct from the the dominant group's feature values than they are in reality. We call this distinction the discrimination risk. We prove that a higher discrimination risk can amplify the unfairness of a machine learning model applied to the imputed data. We then formalize a general graph feature imputation framework called mean aggregation imputation and theoretically and empirically characterize graphs in which applying this framework can yield feature values with a high discrimination risk. We propose a simple algorithm to ensure mean aggregation-imputed features provably have a low discrimination risk, while minimally sacrificing reconstruction error (with respect to the imputation objective). We evaluate the fairness and accuracy of our solution on synthetic and real-world credit networks.
