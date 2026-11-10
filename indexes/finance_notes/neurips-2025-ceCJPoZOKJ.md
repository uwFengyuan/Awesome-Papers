# In-Context Learning of Stochastic Differential Equations with Foundation Inference Models

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We demonstrate that FIM-SDE achieves robust *in-context* function estimation across a wide range of synthetic and real-world processes --- from canonical SDE systems (*e.g*., double-well dynamics or weakly perturbed Lorenz attractors) to stock price recordings and oil-price and wind-speed fluctuations --- while matching the performance of symbolic, Gaussian process and Neural SDE baselines trained on the target datasets.

[Paper](https://openreview.net/forum?id=ceCJPoZOKJ)

Classification / 分类：Time Series / 时间序列 → Causality & Dynamics / 序列因果与动力学 → Foundation models / 基础模型

## Abstract / 摘要

Stochastic differential equations (SDEs) describe dynamical systems where deterministic flows, governed by a drift function, are superimposed with random fluctuations, dictated by a diffusion function. The accurate estimation (*or discovery*) of these functions from data is a central problem in machine learning, with wide application across the natural and social sciences. Yet current solutions either rely heavily on prior knowledge of the dynamics or involve intricate training procedures. We introduce FIM-SDE (Foundation Inference Model for SDEs), a pretrained recognition model that delivers accurate *in-context* (or zero-shot) estimation of the drift and diffusion functions of *low-dimensional* SDEs, from noisy time series data, and allows rapid *finetuning* to target datasets. Leveraging concepts from amortized inference and neural operators, we (pre)train FIM-SDE in a supervised fashion to map a large set of noisy, discretely observed SDE paths onto the space of drift and diffusion functions. We demonstrate that FIM-SDE achieves robust *in-context* function estimation across a wide range of synthetic and real-world processes --- from canonical SDE systems (*e.g*., double-well dynamics or weakly perturbed Lorenz attractors) to stock price recordings and oil-price and wind-speed fluctuations --- while matching the performance of symbolic, Gaussian process and Neural SDE baselines trained on the target datasets. When *finetuned* to the target processes, we show that FIM-SDE consistently outperforms all these baselines.
