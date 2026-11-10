# Diffusion-TS: Interpretable Diffusion for General Time Series Generation

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：5 Published as a conference paper at ICLR 2024 4.1 DATASETS We use 4 real-world datasets and 2 simulated datasets in Table 11 to evaluate our method. Stocks is the Google stock price data from 2004 to 2019. Each observation represents one day and has 6 features. ETTh dataset contains the data collected from electricity transformers, including load and oil temperature that are recorded every 15 minutes between July 2016 and July 2018. Energy is a UCI appliance energy prediction dataset with 28 values. fMRI is a benchmark for ca

[Paper](https://openreview.net/forum?id=4h1apFjO99)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Generation / 生成

## Abstract / 摘要

Denoising diffusion probabilistic models (DDPMs) are becoming the leading paradigm for generative models. It has recently shown breakthroughs in audio synthesis, time series imputation and forecasting. In this paper, we propose Diffusion-TS, a novel diffusion-based framework that generates multivariate time series samples of high quality by using an encoder-decoder transformer with disentangled temporal representations, in which the decomposition technique guides Diffusion-TS to capture the semantic meaning of time series while transformers mine detailed sequential information from the noisy model input. Different from existing diffusion-based approaches, we train the model to directly reconstruct the sample instead of the noise in each diffusion step, combining a Fourier-based loss term. Diffusion-TS is expected to generate time series satisfying both interpretablity and realness. In addition, it is shown that the proposed Diffusion-TS can be easily extended to conditional generation tasks, such as forecasting and imputation, without any model changes. This also motivates us to further explore the performance of Diffusion-TS under irregular settings. Finally, through qualitative and quantitative experiments, results show that Diffusion-TS achieves the state-of-the-art results on various realistic analyses of time series.
