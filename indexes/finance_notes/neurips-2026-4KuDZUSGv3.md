# Performative Prediction with Selective Labels

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Experiments in a lending application with fairness regularization show that our robust optimization approach closely matches the performance of RRM with complete label access.

[Paper](https://openreview.net/forum?id=4KuDZUSGv3)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

Many social applications of machine learning exhibit performative effects: population behavior changes in response to deployed models. Performative prediction studies this interaction through a distribution map that relates each model to the population distribution it induces. One of the main results in this framework showed that repeated risk minimization (RRM), which updates models by retraining on the most recent data, can converge to a stable model that minimizes risk on its own induced distribution. However, existing analyses typically assume access to the complete distributions of features and labels after model deployment, ignoring the possibility of _selective labels_: observing labels only for the accepted subset of the population. In this work, we formalize performative prediction with selective labels and show that retraining only on observed data can misguide the retraining procedure and undermine the guarantees of convergence to a stable solution. We then propose a worst-case objective based on knowledge of a confidence interval on the probability of a positive label. Applying RRM to this objective permits us to remain within a bounded distance to the true stable point. Under a sensitivity assumption on the conditional label distribution, we further show how previously accepted data can tighten these confidence intervals over time. Experiments in a lending application with fairness regularization show that our robust optimization approach closely matches the performance of RRM with complete label access.
