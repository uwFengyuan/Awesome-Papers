# TimeBase: The Power of Minimalism in Efficient Long-term Time Series Forecasting

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：et al., 2018), Wind (Li et al., 2022), , METR-LA (Li et al., G = X⊤ basis Xbasis (5) 2017), Exchange Rate (Lai et al., 2018), ZafNoo (Poy- atos et al., 2020) and CzeLan (Poyatos et al., 2020), 2 AQShunyi (Zhang et al., 2017), AQWan (Zhang et al., 2017), Lorth = ∥G − diag(G)∥F (6) and 4 very large datasets: CA (4.52B), GLA (2.02B), GBA

[Paper](https://openreview.net/forum?id=GhTdNOMfOD)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Long-term time series forecasting (LTSF) has traditionally relied on  large parameters to capture extended temporal dependencies, resulting in substantial computational costs and inefficiencies in both memory usage and processing time. However, time series data, unlike high-dimensional images or text, often exhibit temporal pattern similarity and  low-rank structures, especially in long-term horizons.  By leveraging this structure, models can be guided to focus on more essential, concise temporal data, improving both accuracy and computational efficiency. In this paper, we introduce TimeBase, an ultra-lightweight network  to harness the power of minimalism in LTSF.  TimeBase 1) extracts core basis temporal components and 2) transforms traditional point-level forecasting into efficient segment-level forecasting, achieving optimal utilization of both data and parameters. Extensive experiments on diverse  real-world datasets show that TimeBase achieves remarkable efficiency and secures competitive forecasting performance. Additionally, TimeBase can also serve as a very effective plug-and-play complexity reducer for any patch-based forecasting models. Code is available at \url{https://github.com/hqh0728/TimeBase}.
