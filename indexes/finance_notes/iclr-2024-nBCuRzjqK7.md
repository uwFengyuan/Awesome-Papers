# Self-Supervised Contrastive Learning for Long-term Forecasting

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.178 0.054 0.181 0.068 0.197 0.049 0.170 0.052 0.173 0.054 0.178 0.059 0.184 Exchange 360 0.448 0.527 0.479 0.532 0.459 0.536 0.548 0.573 0.485 0.531 0.492 0.534 0.493 0.541 0.528 0.556 720 1.067 0.794 1.239 0.856 1.383 0.927 1.264 0.859 1.718 1.024 1.291 0.864 1.358 0.894 1.381 0.903

[Paper](https://openreview.net/forum?id=nBCuRzjqK7)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Forecasting / 预测

## Abstract / 摘要

Long-term forecasting presents unique challenges due to the time and memorycomplexity of handling long sequences. Existing methods, which rely on sliding windows to process long sequences, struggle to effectively capture long-term variations that are partially caught within the short window (i.e., outer-window variations). In this paper, we introduce a novel approach that overcomes this limitation by employing contrastive learning and enhanced decomposition architecture,specifically designed to focus on long-term variations. To this end, our contrastiveloss incorporates global autocorrelation held in the whole time series, which facilitates the construction of positive and negative pairs in a self-supervised manner. When combined with our decomposition networks, our constrative learning significantly improves long-term forecasting performance. Extensive experiments demonstrate that our approach outperforms 14 baseline models on well-establishednine long-term benchmarks, especially in challenging scenarios that require a significantly long output for forecasting. This paper not only presents a novel direction for long-term forecasting but also offers a more reliable method for effectively integrating long-term variations into time-series representation learning.
