# How Realistic Is Your Synthetic Data? Constraining Deep Generative Models for Tabular Data

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：5 Published as a conference paper at ICLR 2024 Table 1: Constraint violation rate for each model and dataset. Model/Dataset URL WiDS LCLD Heloc FSP News WGAN 11.1±1.6 98.2±0.2 100.0±0.0 57.0±13.0 70.7±8.3 45.6±9.6 TableGAN 4.9±1.4 96.4±2.4 6.1±0.9 45.6±16.3 71.6±8.7 72.6±5.3 CTGAN 3.1±2.6 99.9±0.0 11.8±2.7 41.6±12.1 74.3±5.2 54.3±10.1 TVAE

[Paper](https://openreview.net/forum?id=tBROYsEz9G)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Deep Generative Models (DGMs) have been shown to be powerful tools for generating tabular data, as they have been increasingly able to capture the complex distributions that characterize them. However, to generate realistic synthetic data, it is often not enough to have a good approximation of their distribution, as it also requires compliance with constraints that encode essential background knowledge on the problem at hand. In this paper, we address this limitation and show how DGMs for tabular data can be transformed into Constrained Deep Generative Models (C-DGMs), whose generated samples are guaranteed to be compliant with the given constraints. This is achieved by automatically parsing the constraints and transforming them into a Constraint Layer (CL) seamlessly integrated with the DGM. Our extensive experimental analysis with various DGMs and tasks reveals that standard DGMs often violate constraints, some exceeding 95% non-compliance, while their corresponding C-DGMs are never non-compliant. Then, we quantitatively demonstrate that, at training time, C-DGMs are able to exploit the background knowledge expressed by the constraints to outperform their standard counterparts with up to 4.5% improvement in utility and detection. Further, we show how our CL does not necessarily need to be integrated at training time, as it can be also used as a guardrail at inference time, still producing some improvements in the overall performance of the models. Finally, we show that our CL does not hinder the sample generation time of the models.
