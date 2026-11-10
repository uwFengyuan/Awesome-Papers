# TimePro: Efficient Multivariate Long-term Time Series Forecasting with Variable- and Time-Aware Hyper-state

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：AE ECL 0.169 0.262 0.170 0.265 0.174 0.264 0.178 0.270 0.189 0.276 0.244 0.334 0.251 0.344 0.192 0.295 0.212 0.300 0.268 0.365 0.193 0.296 Exchange 0.352 0.399 0.367 0.408 0.361 0.402 0.360 0.403 0.367 0.404 0.940 0.707 0.370 0.413 0.416 0.443 0.354 0.414 0.750 0.626 0.461 0.454 Weather 0.251 0.276 0.251 0.276 0.255 0.278 0.258 0.278 0.256 0.279 0.259 0.315 0.271 0.320 0.259 0.287 0.265 0.317 0.292 0.363 0.288 0.314 Solar-Energy 0.232 0.266 0.240 0.273 0.229 0.256 0.233 0.262 0.236 0.266 0.641 0.639 0.347 0.417 0.301 0.319 0.330 0.401 0.282 0.375 0.261

[Paper](https://openreview.net/forum?id=s69Ei2VrIW)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

In long-term time series forecasting, different variables often influence the target variable over distinct time intervals, a challenge known as the multi-delay issue. Traditional models typically process all variables or time points uniformly, which limits their ability to capture complex variable relationships and obtain non-trivial time representations. To address this issue, we propose TimePro, an innovative Mamba-based model that constructs variate- and time-aware hyper-states. Unlike conventional approaches that merely transfer plain states across variable or time dimensions, TimePro preserves the fine-grained temporal features of each variate token and adaptively selects the focused time points to tune the plain state. The reconstructed hyper-state can perceive both variable relationships and salient temporal information, which helps the model make accurate forecasting. In experiments, TimePro performs competitively on eight real-world long-term forecasting benchmarks with satisfactory linear complexity. Code is available at https://github.com/xwmaxwma/TimePro.
