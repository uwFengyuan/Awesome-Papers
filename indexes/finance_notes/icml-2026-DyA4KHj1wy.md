# Universal Redundancies in Time Series Foundation Models

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ast_storage/H/short 0.72 0.72 0.72 0.72 0.72 0.71 0.71 0.71 0.71 0.71 0.71 0.71 0.71 ett1/H/long 0.93 0.93 0.93 0.94 0.93 0.93 0.92 0.92 0.92 0.92 0.92 0.92 0.92 m4_daily/D/short 1.04 1.04 1.04 1.03 1.03 1.03 1.03 1.03 1.03 1.04 1.03 1.02 1.02 20 bitbrain

[Paper](https://openreview.net/forum?id=DyA4KHj1wy)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Foundation models / 基础模型

## Abstract / 摘要

Time Series Foundation Models (TSFMs) leverage extensive pretraining to accurately predict unseen time series during inference, without the need for task-specific fine-tuning. Through large-scale evaluations on standard benchmarks, we find that leading transformer-based TSFMs exhibit redundant components in their intermediate layers. We introduce a set of tools for mechanistic interpretability of TSFMs, including ablations of specific components and direct logit attribution on the residual stream. Our findings are consistent across several leading TSFMs with diverse architectures, and across a diverse set of real-world and synthetic time-series datasets. We discover that all models in our study are robust to ablations of entire layers. Furthermore, we develop a theoretical framework framing transformers as kernel regressors, motivating a purely intrinsic strategy for ablating heads based on the stable rank of the per-head projection matrices. Using this approach, we uncover the specific heads responsible for degenerate phenomena widely observed in TSFMs, such as parroting of motifs from the context and seasonality bias. Our study sheds light on the universal properties of this emerging class of architectures for continuous-time sequence modeling.
