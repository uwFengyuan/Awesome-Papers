# Language Models are Realistic Tabular Data Generators

ICLR 2023 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：99.28±0.06 94.91±0.06 94.57±0.01 94.57±0.00 97.72±0.10 98.30±0.13 LR 71.80±0.00 71.04±0.00 42.03±0.00 57.72±0.00 70.58±0.00 71.90±0.00 HELOC (↑) DT 81.90±0.02 76.39±0.10 42.36±0.10 61.34±0.09 81.40±0.15 79.10±0.07 RF 83.19±0.21 77.24±0.25 42.35±0.34 62.35±0.35 82.14±0.13 80.93±0.28 LR 85.00±0.00 80.53±0.00 80.61±0.00 83.20±0.00 84.65±0.00 84.77±0.00

[Paper](https://openreview.net/forum?id=cEygmQNOeI)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Tabular data is among the oldest and most ubiquitous forms of data. However, the generation of synthetic samples with the original data’s characteristics remains a significant challenge for tabular data. While many generative models from the computer vision domain, such as variational autoencoders or generative adversarial networks, have been adapted for tabular data generation, less research has been directed towards recent transformer-based large language models (LLMs), which are also generative in nature. To this end, we propose GReaT (Generation of Realistic Tabular data), which exploits an auto-regressive generative LLM to sample synthetic and yet highly realistic tabular data. Furthermore, GReaT can model tabular data distributions by conditioning on any subset of features; the remaining features are sampled without additional overhead. We demonstrate the effectiveness of the proposed approach in a series of experiments that quantify the validity and quality of the produced data samples from multiple angles. We find that GReaT maintains state-of-the-art performance across numerous real-world and synthetic data sets with heterogeneous feature types coming in various sizes.
