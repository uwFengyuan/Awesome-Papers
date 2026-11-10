# Performative Validity of Recourse Explanations

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：distributions, we rely on discrete noise distributions with finite support. In addition, we include two real-world settings: College admission (GPA) and credit scoring (Credit). For GPA we assume the causal graph in [Harris et al., 2022] and fit a linear SCM with additive Gaussian noise on the dataset [OpenIntro, 2020]; For Credit we rely on the graph by Chen et al. [2023] and fit a random-forest based, nonlinear SCM with additive Gaussian noise [Yeh, 2009]. The Cred setting has eleven features; all others include one cause and one effect variable. To highlight the differences between methods, we choose the costs such that interventions on effects are more lucrative. Consequently, CE and CR intervene on the effect, while ICR only int

[Paper](https://openreview.net/forum?id=PhoyfQG9Vb)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

When applicants get rejected by a high-stakes algorithmic decision system, recourse explanations provide actionable suggestions for applicants on how to change their input features to get a positive evaluation. A crucial yet overlooked phenomenon is that recourse explanations are *performative*: When many applicants act according to their recommendations, their collective behavior may shift the data distribution and, once the model is refitted, also the decision boundary. Consequently, the recourse algorithm may render its own recommendations *invalid*, such that applicants who make the effort of implementing their recommendations may be rejected again when they reapply. In this work, we formally characterize the conditions under which recourse explanations remain valid under their own performative effects. In particular, we prove that recourse actions may become invalid if they are influenced by or if they intervene on non-causal variables. Based on this analysis, we caution against the use of standard counterfactual explanations and causal recourse methods, and instead advocate for recourse methods that recommend actions exclusively on causal variables.
