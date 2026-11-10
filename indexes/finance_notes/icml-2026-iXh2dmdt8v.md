# Towards a Unified Generative Model for Scarce Time Series with Domain Experts

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：sets ues to benefit from increased available data and outperforms (Gonen et al., 2025; Gao et al., 2024) spanning 10 do- advanced methods. Notably, TimeMoDE fine-tuned with mains—healthcare, finance, energy, traffic, cloud, human only 5% of dataset even surpasses state-of-the-art models activity, machine sensors, physics, space, and nature—and such as ImagenTime trained on full dataset. It highlights the covering 5 tasks: forecasting, simulation, anomaly detec- effectiveness of transferring knowledge

[Paper](https://openreview.net/forum?id=iXh2dmdt8v)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Generation / 生成

## Abstract / 摘要

Synthesizing realistic time series with generative models has wide-ranging applications in real-world scenarios. Despite recent progress, most existing methods are trained under the assumption of abundant training data, which substantially limits their effectiveness in data-scarce settings. In this paper, we propose TimeMoDE, a novel framework that integrates Diffusion Transformers with Mixture-of-Experts to exploit both domain adaptability and diffusion-stage awareness for time series generation under data scarcity. It is pre-trained on a large-scale collection of multi-domain datasets to extract domain-agnostic temporal representations and domain-specific information benefiting generalization during fine-tuning. We propose Domain Prompts to condition expert assignment for indistinguishable noised tokens, mitigating the limitations of capturing inter-dataset relationships. Moreover, we incorporate diffusion timestep signals to equip the experts with awareness of time series degradation variations, facilitating adaptive calibrate to stage-dependent denoising requirements. Extensive experiments demonstrate that TimeMoDE outperforms existing methods under diverse low-data settings. It establishes an innovative paradigm for advanced time series few-shot generation.
