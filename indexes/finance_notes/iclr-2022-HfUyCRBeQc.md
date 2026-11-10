# Selective Ensembles for Consistent Predictions

ICLR 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ility that models of similar objective quality may still have arbitrarily different gradients. In Section 5.2, we demonstrate that this outcome is not only possible, but that it occurs in real models—for example, on the German Credit dataset predicting credit risk, on average, individual models with similar accuracy agree on less than two out of the five most important features influencing their decision. 4 SELECTIVE ENSEMBLING The results of Section 3 suggests that models that are retrained and redeployed, may exhibit substantially different behavior from their pre

[Paper](https://openreview.net/forum?id=HfUyCRBeQc)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Recent work has shown that models trained to the same objective, and which achieve similar measures of accuracy on consistent test data, may nonetheless behave very differently on individual predictions. This inconsistency is undesirable in high-stakes contexts, such as medical diagnosis and finance. We show that this duplicitous behavior extends beyond predictions to feature attributions, which may likewise have negative implications for the intelligibility of a model, and one's ability to find recourse for subjects. We then introduce selective ensembles to mitigate such inconsistencies by applying hypothesis testing to the predictions of a set of models trained using randomly-selected starting conditions; importantly, selective ensembles can abstain in cases where a consistent outcome cannot be achieved up to a specified confidence level. We prove that that prediction disagreement between selective ensembles is bounded, and empirically demonstrate that selective ensembles achieve consistent predictions and feature attributions while maintaining low abstention rates. On several benchmark datasets, selective ensembles reach zero inconsistently predicted points, with abstention rates as low as 1.5%.
