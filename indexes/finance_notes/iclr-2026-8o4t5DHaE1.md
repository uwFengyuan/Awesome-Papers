# Lost in the Non-convex Loss Landscape: How to Fine-tune the Large Time Series Model?

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：100% Methods SFF FF TFS SFF FF TFS SFF FF TFS SFF FF TFS Exchange 0.0805 0.0865 0.1441 0.0802 0.0891 0.114 0.0802 0.0914 0.1026 0.08 0.091 0.0981 Standard deviation ±4.5e-4 ±1.9e-4 ±2.0e-3 ±5.4e-4 ±2.3e-3 ±9.9e-4 ±1.2e-3 ±1.6e-3 ±8.8e-4 ±7.6e-4 ±1.3e-4 ±1.2e-3 ETTh1 0.3506 0.355 0.3788 0.3494 0.3573 0.367 0.3493 0.358 0.3593 0.3547 0.3709 0.36 ETTh2 0.271 0.2866 0.2891 0.273 0.2905 0.2775

[Paper](https://openreview.net/forum?id=8o4t5DHaE1)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Foundation models / 基础模型

## Abstract / 摘要

Recently, large time series models (LTSMs) have gained increasing attention due to their similarities to large language models, including flexible context length, scalability, and task generality, outperforming advanced task-specific models. However, prior studies indicate that pre-trained LTSMs may exhibit a poorly conditioned non-convex loss landscape, leading to limited trainability. As a result, direct fine-tuning tends to cause overfitting and suboptimal performance, sometimes even worse than training from scratch, substantially diminishing the benefits of pre-training. To overcome this limitation, we propose Smoothed Full Fine-tuning (SFF), a novel fine-tuning technology. Specifically, we construct an auxiliary LTSM via random initialization to obtain a smoother loss landscape, and then linearly interpolate its weights with those of the pre-trained model to smooth the original landscape. This process improves trainability while preserving pre-trained knowledge, thereby enabling more effective downstream fine-tuning. From an optimization perspective, SFF perturbs sharp minima without significantly harming flat regions, facilitating escape from poor local basins toward smoother and more generalizable solutions. Extensive experiments on benchmark datasets demonstrate consistent improvements across eight representative LTSMs, including Timer, TimesFM, MOMENT, UniTS, MOIRAI, Chronos, TTMs, and Sundial, on diverse downstream tasks. The code is available at the link: \url{https://github.com/Meteor-Stars/SFF}.
