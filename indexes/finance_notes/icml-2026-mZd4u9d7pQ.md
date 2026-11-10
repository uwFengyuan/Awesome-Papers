# Once-for-All: Scalable Simultaneous Forecasting via Equilibrium State Estimation

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：t red background. commonly used as a benchmark in prediction studies. Here, we use 16 exchange rates relative to the USD, representing Models RMSE MAE Cost (mins) 16 non-USD currencies from the G20, which comprises ESE – 0.248 0.228 0.23 the world’s most significant economies. These currencies No ESE 0.249 0.243 0.09 exhibit mutual influence, while the impact of economie

[Paper](https://openreview.net/forum?id=mZd4u9d7pQ)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → FX & Crypto Forecasts / 汇率与加密资产预测 → General / 综合

## Abstract / 摘要

We introduce Equilibrium State Estimation (ESE), a novel paradigm for simultaneous prediction, where multiple interacting systems require separate yet coordinated forecasts. Such scenarios often arise in real-world such as economics and healthcare modeling.  Unlike existing approaches that predict one system at a time, ESE forecasts all systems in a single pass.  It first estimates the equilibrium state across systems, then generates holistic forecasts based on the difference between the current state and the estimated equilibrium.  Extensive experiments on synthetic and real-world datasets, including currency exchange and COVID-19 spread modeling, demonstrate that ESE is at least as accurate as state-of-the-art (SOTA) methods while being significantly faster.  In addition, ESE integrates seamlessly with conventional predictors, combining their accuracy with its exceptional efficiency and delivering a 10–70× speedup. With linear-time complexity, ESE scales far better than SOTA methods as the number of systems increases. Moreover, it remains accurate under diverse perturbations, establishing ESE as a fast, generalizable, robust, and scalable multi-prediction method.
