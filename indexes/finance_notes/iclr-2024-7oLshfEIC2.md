# TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：622,5622) 5min 0.58 Transportation Short-term PEMS08 170 12 (10690,3548,265) 5min 0.52 Transportation Forecasting M4-Yearly 1 6 (23000, 0, 23000) Yearly 0.43 Demographic M4-Quarterly 1 8 (24000, 0, 24000) Quarterly 0.47 Finance M4-Monthly 1 18 (48000, 0, 48000) Monthly 0.44 Industry M4-Weakly 1 13 (359, 0,

[Paper](https://openreview.net/forum?id=7oLshfEIC2)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting is widely used in extensive applications, such as traffic planning and weather forecasting. However, real-world time series usually present intricate temporal variations, making forecasting extremely challenging. Going beyond the mainstream paradigms of plain decomposition and multiperiodicity analysis, we analyze temporal variations in a novel view of multiscale-mixing, where time series present distinct patterns in different sampling scales. Specifically, the microscopic and the macroscopic information are reflected in fine and coarse scales, respectively, and thereby complex variations are inherently disentangled. Based on this observation, we propose TimeMixer as a fully MLP-based architecture with Past-Decomposable-Mixing (PDM) and Future-Multipredictor-Mixing (FMM) blocks to take full advantage of disentangled multiscale series in both past extraction and future prediction phases. Concretely, PDM applies the decomposition to multiscale series and further mixes the decomposed seasonal and trend components in fine-to-coarse and coarse-to-fine directions separately, which successively aggregates the microscopic seasonal and macroscopic trend information. FMM further ensembles multiple predictors to utilize complementary forecasting capabilities in multiscale observations. Consequently, our proposed TimeMixer is able to achieve consistent state-of-the-art performances in both long-term and short-term forecasting tasks with favorable run-time efficiency.
