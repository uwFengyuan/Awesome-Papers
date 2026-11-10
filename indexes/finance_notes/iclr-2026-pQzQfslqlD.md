# Bridging Past and Future: Distribution-Aware Alignment for Time Series Forecasting

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：23 Published as a conference paper at ICLR 2026 Figure 7: Effect of alignment loss weight across ETTh2, ETTm1, ECL and Traffic. (NASDAQ and NYSE) released by TFB (Qiu et al., 2024). As shown in Tab. 10, TimeAlign consis- tently achieves the best forecasting performance, outperforming all baselines across all prediction Models iTransformer +TimeAlign DLinear +TimeAlign Metric MSE

[Paper](https://openreview.net/forum?id=pQzQfslqlD)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Although contrastive and other representation-learning methods have long been explored in vision and NLP, their adoption in modern time series forecasters remains limited. We believe they hold strong promise for this domain. To unlock this potential, we explicitly align past and future representations, thereby bridging the distributional gap between input histories and future targets. To this end, we introduce TimaAlign, a lightweight, plug-and-play framework that establishes a new representation paradigm, distinct from contrastive learning, by aligning auxiliary features via a simple reconstruction task and feeding them back into any base forecaster. Extensive experiments across eight benchmarks verify its superior performance. Further studies indicate that the gains arise primarily from correcting frequency mismatches between historical inputs and future outputs. Additionally, we provide two theoretical justifications for how reconstruction improves forecasting generalization and how alignment increases the mutual information between learned representations and predicted targets. Code is in available at https://github.com/TROUBADOUR000/TimeAlign.
