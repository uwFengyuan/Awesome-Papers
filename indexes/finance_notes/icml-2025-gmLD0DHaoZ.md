# Algorithmic Recourse for Long-Term Improvement

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Algorithmic recourse aims to provide a recourse action for altering an unfavorable prediction given by a model into a favorable one (e.g., loan approval). / In practice, it is also desirable to ensure that an action makes the real-world outcome better (e.g., loan repayment).

[Paper](https://openreview.net/forum?id=gmLD0DHaoZ)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Algorithmic recourse aims to provide a recourse action for altering an unfavorable prediction given by a model into a favorable one (e.g., loan approval). In practice, it is also desirable to ensure that an action makes the real-world outcome better (e.g., loan repayment). We call this requirement *improvement*. Unfortunately, existing methods cannot ensure improvement unless we know the true oracle.  To address this issue, we propose a framework for suggesting improvement-oriented actions from a long-term perspective. Specifically, we introduce a new online learning task of assigning actions to a given sequence of instances. We assume that we can observe delayed feedback on whether the past suggested action achieved improvement. Using the feedback, we estimate an action that can achieve improvement for each instance. To solve this task, we propose two approaches based on contextual linear bandit and contextual Bayesian optimization. Experimental results demonstrated that our approaches could assign improvement-oriented actions to more instances than the existing methods.
