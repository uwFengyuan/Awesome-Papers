# GT-GAN: General Purpose Time Series Synthesis with Generative Adversarial Networks

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：phases independently. For each feature, i ∈ {1, ..., 5}, xi (t) = sin(2πfi t + θi ), wherefi ∼ U[0, 1] and θi ∼ U[−π, π]. MuJoCo is multivariate physics simulation time series data with 14 features. Stocks is the Google stock price data from 2004 to 2019. Each observation represents one day and has 6 features. Energy is a UCI appliance energy prediction dataset with 28 values. To create the challenging irregular environments, 30, 50, 70% of observations from each time series sample {(ti , xreal i )}N

[Paper](https://openreview.net/forum?id=ez6VHWvuXEx)

Classification / 分类：Time Series / 时间序列 → Generation & Simulation / 序列生成与仿真 → Generation / 生成

## Abstract / 摘要

Time series synthesis is an important research topic in the field of deep learning, which can be used for data augmentation. Time series data types can be broadly classified into regular or irregular. However, there are no existing generative models that show good performance for both types without any model changes. Therefore, we present a general purpose model capable of synthesizing regular and irregular time series data. To our knowledge, we are the first designing a general purpose time series synthesis model, which is one of the most challenging settings for time series synthesis. To this end, we design a generative adversarial network-based method, where many related techniques are carefully integrated into a single framework, ranging from neural ordinary/controlled differential equations to continuous time-flow processes. Our method outperforms all existing methods.
