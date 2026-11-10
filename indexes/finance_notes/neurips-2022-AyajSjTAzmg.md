# SCINet: Time Series Modeling and Forecasting with Sample Convolution and Interaction

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.9787 0.0400 0.9458 0.1392 0.9473 0.0689 0.9759 0.0217 0.9693 0.0202 0.9712 0.0226 0.9735 0.0174 0.979 1.72% Exchange 6 0.0240 0.9704 0.0481 0.9197 0.1548 0.9207 0.0806 0.9671 0.0263 0.9633 0.0257 0.9628 0.0280 0.9658 0.0241 0.9709 0.41% Rate 12 0.0331 0.9553 0.0638 0.9054 0.1793 0.8817 0.0893 0.9476 0.0393 0.9531 0.0352 0.9501 0.0356 0.9511 0.0341 0.9564 2.93% 24 0.0436 0.9396 0.0651 0.8952 0.1998 0.7715 0.1

[Paper](https://openreview.net/forum?id=AyajSjTAzmg)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

One unique property of time series is that the temporal relations are largely preserved after downsampling into two sub-sequences. By taking advantage of this property, we propose a novel neural network architecture that conducts sample convolution and interaction for temporal modeling and forecasting, named SCINet. Specifically, SCINet is a recursive downsample-convolve-interact architecture. In each layer, we use multiple convolutional filters to extract distinct yet valuable temporal features from the downsampled sub-sequences or features. By combining these rich features aggregated from multiple resolutions, SCINet effectively models time series with complex temporal dynamics. Experimental results show that SCINet achieves significant forecasting accuracy improvements over both existing convolutional models and Transformer-based solutions across various real-world time series forecasting datasets. Our codes and data are available at https://github.com/cure-lab/SCINet.
