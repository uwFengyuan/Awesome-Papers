# Generalizing Multi-Scale Time-Series Modeling with a Single Operator

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：298 0.194 0.294 0.298 0.390 Traffic 0.458 0.302 0.546 0.344 0.497 0.329 0.527 0.343 0.501 0.318 0.654 0.384 0.543 0.320 0.627 0.334 0.685 0.384 Exchange 0.353 0.400 0.358 0.401 0.387 0.419 0.376 0.408 0.384 0.414 0.431 0.446 0.345 0.424 0.416 0.443 1.181 0.854 ETTh1 0.443 0.433 0.447 0.434 0.443 0.440 0.451 0.442 0.455 0.444 0.459 0.458 0.572 0.531 0.480 0.468 0.879 0.731 ETTh2 0.376 0.402 0.376 0.400 0.379 0.406 0.390 0.410 0.389 0.410 0.402 0.421 0.582 0.527 0.410 0.424 4.086 1.621 ETTm1 0.383 0.397 0.395 0.399 0.385 0.400 0.385 0.397 0.385 0.

[Paper](https://openreview.net/forum?id=hxNN3xhuS9)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Multi-scale modeling has emerged as an effective design principle for time-series forecasting by capturing temporal dynamics at multiple resolutions. As no principled foundation has been established in the literature, we unify existing scaling methods into a scaling operator family, revealing a fundamental limitation of existing approaches: reliance on fixed and discrete scaling. To address this limitation, we propose SiGMA (Single Generalized Multi-scale Architecture), which enables distance-aware scaling via the learnable discrete Gaussian (LDG) kernel grounded in scale-space theory. We evaluate SiGMA comprehensively on long- and short-term forecasting benchmarks against state-of-the-art multi-scale baselines. SiGMA outperforms all competitors on both tasks, especially achieving the best performance in 13 out of 16 long-term evaluation settings. Beyond accuracy, SiGMA significantly improves training speed by up to 5.3 times and reduces memory consumption by up to 3.8 times over the strongest competitors. Code is available at https://github.com/cheonwoolee/SiGMA.
