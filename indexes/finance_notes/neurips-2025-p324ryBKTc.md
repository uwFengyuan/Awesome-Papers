# Time Series Generation Under Data Scarcity: A Unified Generative Modeling Approach

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：, encouraging the learning of transferable representations that are useful in data-scarce settings. Specifi- cally, we utilize the datasets: Stocks, Energy [6], ETTh1 [68], Exchange [35], MSL [27], SMAP [27], PSM [1], SMD [57], ECG5000 [21], NonInvasiveFetalECGThorax1 [53], SelfRegulationSCP2 [2], Blink [11], ElectricDevices [37], Trace [52], FordB [15], UWaveGestureLibrary [40], EMOPain [18], Chinatown [15], and SharePriceIncrease [42]. These datasets combine commonly used collections from various tasks in UniTS [20] with datasets from generative modeling research [44, 67]. In our approach, all of these datasets are jointly employed during the pre-training phase, encompassing approximately 300,000 time series in total. During pre-train

[Paper](https://openreview.net/forum?id=p324ryBKTc)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Generation / 生成

## Abstract / 摘要

Generative modeling of time series is a central challenge in time series analysis, particularly under data-scarce conditions. Despite recent advances in generative modeling, a comprehensive understanding of how state-of-the-art generative models perform under limited supervision remains lacking. In this work, we conduct the first large-scale study evaluating leading generative models in data-scarce settings, revealing a substantial performance gap between full-data and data-scarce regimes. To close this gap, we propose a unified diffusion-based generative framework that can synthesize high-fidelity time series across diverse domains using just a few examples. Our model is pretrained on a large, heterogeneous collection of time series datasets, enabling it to learn generalizable temporal representations. It further incorporates architectural innovations such as dynamic convolutional layers for flexible channel adaptation and dataset token conditioning for domain-aware generation. Without requiring abundant supervision, our unified model achieves state-of-the-art performance in few-shot settings—outperforming domain-specific baselines across a wide range of subset sizes. Remarkably, it also surpasses all baselines even when tested on full datasets benchmarks, highlighting the strength of pretraining and cross-domain generalization. We hope this work encourages the community to revisit few-shot generative modeling as a key problem in time series research and pursue unified solutions that scale efficiently across domains.  Code is available at https://github.com/azencot-group/ImagenFew.
