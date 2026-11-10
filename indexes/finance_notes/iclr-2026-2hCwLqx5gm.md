# Numerion: A Multi-Hypercomplex Model for Time Series Forecasting

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：2 Traffic 0.281 0.468 0.298 0.485 0.298 0.485 0.282 0.428 0.300 0.470 0.340 0.521 0.304 0.481 0.426 0.667 0.336 0.620 0.376 0.610 0.383 0.625 Exchange 0.399 0.358 0.432 0.416 0.453 0.391 0.470 0.519 0.464 0.515 0.414 0.379 0.404 0.367 0.707 0.940 0.443 0.416 0.429 0.519 0.414 0.354 Table 1 showcases the comparison results of our method against other approaches, with all outcomes representing the average across four prediction lengths {96, 192, 336, 720}. The complete experi- mental results are detailed in Appendix C. It is evident that our method achieves

[Paper](https://openreview.net/forum?id=2hCwLqx5gm)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Many methods aim to enhance time series forecasting by decomposing the series through intricate model structures and prior knowledge, yet they are inevitably limited by computational complexity and the robustness of the assumptions. Our research uncovers that in the complex domain and higher-order hypercomplex spaces, the characteristic frequencies of time series naturally decrease. Leveraging this insight, we propose Numerion, a time series forecasting model based on multiple hypercomplex spaces. Specifically, grounded in theoretical support, we generalize linear layers and activation functions to hypercomplex spaces of arbitrary power-of-two dimensions and introduce a novel Real-Hypercomplex-Real Domain Multi-Layer Perceptron (RHR-MLP) architecture. Numerion utilizes multiple RHR-MLPs to map time series into hypercomplex spaces of varying dimensions, naturally decomposing and independently modeling the series, and adaptively fuses the latent patterns exhibited in different spaces through a dynamic fusion mechanism. Experiments validate the model’s performance, achieving state-of-the-art results on multiple public datasets. Visualizations and quantitative analyses comprehensively demonstrate the ability of multi-dimensional RHR-MLPs to naturally decompose time series and reveal the tendency of higher-dimensional hypercomplex spaces to capture lower-frequency features.
