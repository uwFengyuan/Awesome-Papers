# Harpoon: Generalised Manifold Guidance for Conditional Tabular Diffusion

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：, c) = wT ∈ TQt (xt ) M0 17 Published as a conference paper at ICLR 2026 C DATASETS We used eight widely adopted benchmark datasets: Adult2 , Default of Credit Card Clients3 , Magic Gamma Telescope4 , Online Shoppers Purchasing Intention5 , Gesture Phase Segmentation6 , Letter Recognition7 , and Dry Bean8 . Additionally, we included the California Housing dataset from Kaggle9 . The statistics of these datasets are presented in Table 8, each of which is partitioned using a random 70-30 train-test split. Prior

[Paper](https://openreview.net/forum?id=G5g6tDg1ZE)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Generating tabular data under conditions is critical to applications requiring precise control over the generative process. Existing methods rely on training-time strategies that do not generalise to unseen constraints during inference, and struggle to handle conditional tasks beyond tabular imputation. While manifold theory offers a principled way to guide generation, current formulations are tied to specific inference-time objectives and are limited to continuous domains. We extend manifold theory to tabular data and expand its scope to handle diverse inference-time objectives. On this foundation, we introduce Harpoon, a  tabular diffusion method that guides unconstrained samples along the manifold geometry to satisfy diverse tabular conditions at inference. We validate our theoretical contributions empirically on tasks such as imputation and enforcing inequality constraints, demonstrating Harpoon's strong performance across diverse datasets and the practical benefits of manifold-aware guidance for tabular data. Code URL: https://github.com/adis98/Harpoon
