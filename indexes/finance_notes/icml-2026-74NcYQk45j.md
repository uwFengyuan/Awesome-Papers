# Algorithmic Recourse of In-Context Learning for Tabular Data

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：As predictive models are increasingly deployed in high-stakes settings such as credit approval, there is a growing need for post-hoc methods that provide recourse to affected individuals.

[Paper](https://openreview.net/forum?id=74NcYQk45j)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

As predictive models are increasingly deployed in high-stakes settings such as credit approval, there is a growing need for post-hoc methods that provide recourse to affected individuals. Many such models operate on tabular data, where features correspond to real-world attributes. Recently, in-context learning (ICL) has enabled large language models to perform tabular prediction by conditioning on labeled examples at inference time, without explicit training. However, algorithmic recourse for tabular decision-making under ICL remains largely unexplored. In this work, we present the first study of algorithmic recourse for tabular data under ICL. We carry out a theoretical analysis, showing that recourse remains well-defined and bounded, and we characterize how recourse converges toward classical solutions as the context size increases. In practice, we propose a novel zeroth-order recourse framework, Adaptive Subspace Recourse for In-Context Learning (ASR-ICL), that efficiently generates actionable and sparse recourse for black-box ICL models. The proposed framework naturally extends to multi-class tabular tasks. Experiments across multiple real-world datasets and models demonstrate that ASR-ICL achieves recourse quality comparable to existing methods with fewer queries and empirically confirm the predicted convergence behavior, supporting our theoretical analysis.
