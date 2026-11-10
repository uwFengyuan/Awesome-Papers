# A Diffusion Model for Regular Time Series Generation from Irregular Data with Completion and Masking

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ors by filling them with zeros. (v) Ours Without 8 Table 7: Discriminative scores of the ablation study with 30%, 50%, and 70% drop-rate on Energy and Stock datasets for sequence lengths of 24, 96, and 768. 30% 50% 70% Model Energy Stock Energy Stock Energy Stock KoVAE + TST 0.399 0.109 0.407 0.064 0.408 0.037 Len. = 2

[Paper](https://openreview.net/forum?id=M9JmlA6Cgf)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Generation / 生成

## Abstract / 摘要

Generating realistic time series data is critical for applications in healthcare, finance, and climate science. However, irregular sampling and missing values present significant challenges. While prior methods address these irregularities, they often yield suboptimal results and incur high computational costs. Recent advances in regular time series generation, such as the diffusion-based ImagenTime model, demonstrate strong, fast, and scalable generative capabilities by transforming time series into image representations, making them a promising solution. However, extending ImagenTime to irregular sequences using simple masking introduces ``unnatural'' neighborhoods, where missing values replaced by zeros disrupt the learning process. To overcome this, we propose a novel two-step framework: first, a Time Series Transformer completes irregular sequences, creating natural neighborhoods; second, a vision-based diffusion model with masking minimizes dependence on the completed values. This hybrid approach leverages the strengths of both completion and masking, enabling robust and efficient generation of realistic time series. Our method achieves state-of-the-art performance across benchmarks, delivering a relative improvement in discriminative score by 70% and in computational cost by 85%.
