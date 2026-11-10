# Distributionally Robust Recourse Action

ICLR 2023 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ances for which the recourse is valid with respect to the original classifier. Results on real-world data. We use three real-world datasets which capture different data distri- bution shifts (Dua & Graff, 2017): (i) the German credit dataset, which captures a correction shift. (ii) the Small Business Administration (SBA) dataset, which captures a temporal shift. (iii) the Stu- dent performance dataset, which captures a geospatial shift. Each dataset contains original data and shifted data. We normalize all continuous features to [0, 1]. Similar to Mothilal et al. (2020), we us

[Paper](https://openreview.net/forum?id=E3ip6qBLF7)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

A recourse action aims to explain a particular algorithmic decision by showing one specific way in which the instance could be modified to receive an alternate outcome. Existing recourse generation methods often assume that the machine learning model does not change over time. However, this assumption does not always hold in practice because of data distribution shifts, and in this case, the recourse action may become invalid. To redress this shortcoming, we propose the Distributionally Robust Recourse Action (DiRRAc) framework, which generates a recourse action that has high probability of being valid under a mixture of model shifts. We first formulate the robustified recourse setup as a min-max optimization problem, where the max problem is specified by Gelbrich distance over an ambiguity set around the distribution of model parameters. Then we suggest a projected gradient descent algorithm to find a robust recourse according to the min-max objective. We also show that our DiRRAc framework can be extended to hedge against the misspecification of the mixture weights. Numerical experiments with both synthetic and three real-world datasets demonstrate the benefits of our proposed framework over the state-of-the-art recourse methods, which generate robust recourses.
