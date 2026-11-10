# LETS Forecast: Learning Embedology for Time Series Forecasting

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：48 0.042 0.142 0.042 0.143 0.128 0.271 0.045 0.147 0.044 0.144 0.045 0.148 0.044 0.144 0.043 0.143 0.043 0.145 0.054 0.180 0.117 0.248 0.042 0.139 Exchange 96 0.088 0.205 0.083 0.207 0.294 0.394 0.093 0.213 0.089 0.209 0.095 0.219 0.085 0.204 0.084 0.203 0.084 0.220 0.113 0.261 0.108 0.251 0.081 0.196 144 0.133 0.255 0.130 0.261 0.597 0.578 0.151 0.274 0.144 0.267 0.154 0.283 0.132 0.260 0.146 0.270 0.132 0.253 0.133 0.258 0.152 0.301 0.122 0.244 192 0.178 0.301 0.184 0.309 0.654 0.595 0.205 0.323 0.207 0.322 0.212 0.334 0.174 0

[Paper](https://openreview.net/forum?id=LLk1qYQatJ)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Real-world time series are often governed by complex nonlinear dynamics. Understanding these underlying dynamics is crucial for precise future prediction. While deep learning has achieved major success in time series forecasting, many existing approaches do not explicitly model the dynamics. To bridge this gap, we introduce DeepEDM, a framework that integrates nonlinear dynamical systems modeling with deep neural networks. Inspired by empirical dynamic modeling (EDM) and rooted in Takens' theorem, DeepEDM presents a novel deep model that learns a latent space from time-delayed embeddings, and employs kernel regression to approximate the underlying dynamics, while leveraging efficient implementation of softmax attention and allowing for accurate prediction of future time steps. To evaluate our method, we conduct comprehensive experiments on synthetic data of nonlinear dynamical systems as well as real-world time series across domains. Our results show that DeepEDM is robust to input noise, and outperforms state-of-the-art methods in forecasting accuracy. Our code is available at: https://abrarmajeedi.github.io/deep_edm.
