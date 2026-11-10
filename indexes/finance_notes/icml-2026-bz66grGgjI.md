# Dynamic Relational Priming Improves Transformer in Multivariate Time Series

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ETTh2 Avg. 0.377 0.404 0.386 0.411 0.382 0.405 0.386 0.408 0.450 0.459 Exchange Avg. 0.339 0.392 0.357 0.401 0.341 0.397 0.356 0.403 0.613 0.539 Weather Avg. 0.254 0.277 0.259 0.280 0.258 0.281 0.260 0.282 0.338 0.382 ECL Avg. 0.175 0.266 0.173 0.265 - - 0.193 0.278 0.227 0.338 Traffic

[Paper](https://openreview.net/forum?id=bz66grGgjI)

Classification / 分类：Time Series / 时间序列 → General Time-Series Methods / 综合序列方法 → Forecasting / 预测

## Abstract / 摘要

Standard attention mechanisms in transformers employ static token representations that remain unchanged across all pair-wise computations in each layer. This limits their representational alignment with the potentially diverse dynamics of each token-pair interaction. While they excel in domains with relatively homogeneous relationships, standard attention may be inadequate in capturing heterogeneous inter-channel dependencies of multivariate time series (MTS) data where different channel-pair interactions within a single system may be governed by entirely different physical laws or temporal dynamics. To better align the attention mechanism for such domain phenomena, we propose attention with dynamic relational priming (prime attention). Prime attention modulates token representations for each token-pair, optimizing each pair-wise interaction for that specific relationship. Our results demonstrate that prime attention consistently outperforms standard attention across benchmarks, achieving up to 6.5\% improvement in forecasting accuracy. In addition, prime attention achieves comparable performance using up to 40\% less sequence length compared to standard attention, demonstrating its superior relational modeling capabilities and potential for data efficiency.
