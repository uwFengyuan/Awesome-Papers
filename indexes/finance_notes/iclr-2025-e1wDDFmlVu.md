# Time-MoE: Billion-Scale Time Series Foundation Models with Mixture of Experts

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：s, high-quality time series data collection named Time-300B for foundation model pre-training. Time-300B comprises a diverse array of publicly available datasets from domains such as energy, retail, healthcare, weather, finance, transportation, and web, augmented with synthetic data to enhance both quantity and diversity. It spans sam- pling frequencies from seconds to yearly intervals and, after processing through our data-cleaning pipeline, includes over 300 billion time points, as summarized in Table 1. 5 Publishe

[Paper](https://openreview.net/forum?id=e1wDDFmlVu)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Foundation models / 基础模型

## Abstract / 摘要

Deep learning for time series forecasting has seen significant advancements over the past decades. However, despite the success of large-scale pre-training in language and vision domains, pre-trained time series models remain limited in scale and operate at a high cost, hindering the development of larger capable forecasting models in real-world applications. In response, we introduce Time-MoE, a scalable and unified architecture designed to pre-train larger, more capable forecasting foundation models while reducing inference costs. By leveraging a sparse mixture-of-experts (MoE) design, Time-MoE enhances computational efficiency by activating only a subset of networks for each prediction, reducing computational load while maintaining high model capacity. This allows Time-MoE to scale effectively without a corresponding increase in inference costs. Time-MoE comprises a family of decoder-only transformer models that operate in an auto-regressive manner and support flexible forecasting horizons with varying input context lengths. We pre-trained these models on our newly introduced large-scale data Time-300B, which spans over 9 domains and encompassing over 300 billion time points. For the first time, we scaled a time series foundation model up to 2.4 billion parameters, achieving significantly improved forecasting precision. Our results validate the applicability of scaling laws for training tokens and model size in the context of time series forecasting. Compared to dense models with the same number of activated parameters or equivalent computation budgets, our models consistently outperform them by large margin. These advancements position Time-MoE as a state-of-the-art solution for tackling real-world time series forecasting challenges with superior capability, efficiency, and flexibility. Code is available at https://github.com/Time-MoE/Time-MoE
