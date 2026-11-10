# CTSyn: A Foundation Model for Cross Tabular Data Generation

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：1 0080 BNG(vote) 100000 17 0 1375 MAGIC-Gamma-Telescope-Dataset 19020 1 10 0063 BNG(credit-g,nominal,1000000) 100000 21 0 1431 Beijing-Multi-Site-Air-Quality 100000 2 16 bodyPerformance 13393 2 10 term deposit subscribed33 31647 9 8 1465 credit 16714 0 11 0077 BNG(heart

[Paper](https://openreview.net/forum?id=Sh4FOyZRpv)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Generative Foundation Models (GFMs) have achieved remarkable success in producing high-quality synthetic data for images and text. However, their application to tabular data presents significant challenges due to the heterogeneous nature of table features. Current cross-table learning frameworks struggle because they lack a generative model backbone and an effective mechanism to decode heterogeneous feature values. To address these challenges, we propose the Cross-Table Synthesizer (CTSyn), a diffusion-based generative foundation model for tabular data generation. CTSyn comprises two key components. The first is an autoencoder network that consolidates diverse tables into a unified latent space. It dynamically reconstructs table values using a table schema embedding, allowing adaptation to heterogeneous datasets. The second is a conditional latent diffusion model that generates samples from the learned latent space, conditioned on the table schema. Through large-scale pre-training, CTSyn outperforms existing table synthesizers on standard benchmarks in both utility and diversity.  These results position CTSyn as a promising framework for synthetic table generation and lay the groundwork for developing large-scale tabular foundation models.
