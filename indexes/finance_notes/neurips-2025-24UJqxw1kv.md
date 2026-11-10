# Forecasting in Offline Reinforcement Learning for Non-stationary Environments

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Forecast Mean Figure 18: Zero-shot forecasting results with Lag-Llama [10] for first 2 time-series in univariate time-series datasets: real-data-A (Australian-electricity-demand), real-data-E (Exchange Rate), real-data-B (Electricity), real-data-C (Electricity Hourly),real-data-D (Electricity Nips). In all datasets, F ORL outperforms the DQL+L AG-s̄ baseline. F ORL achieves its greatest impact on moderately challenging forecasts (a 56.5% error reduction on real-data-D). Its behavior at the extremes further demonstrates its robustness: • F ORL still refines the best forecast by 10.2% (real-data-C)

[Paper](https://openreview.net/forum?id=24UJqxw1kv)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → FX & Crypto Forecasts / 汇率与加密资产预测 → General / 综合

## Abstract / 摘要

Offline Reinforcement Learning (RL) provides a promising avenue for training policies from pre-collected datasets when gathering additional interaction data is infeasible. However, existing offline RL methods often assume stationarity or only consider synthetic perturbations at test time—assumptions that often fail in real-world scenarios characterized by abrupt, time-varying offsets. These offsets can lead to partial observability, causing agents to misperceive their true state and degrade performance. To overcome this challenge, we introduce Forecasting in Non-stationary Offline RL (FORL), a framework that unifies (i) conditional diffusion-based candidate state generation, trained without presupposing any specific form of future non-stationarity, and (ii) zero-shot time-series foundation models. FORL targets environments prone to unexpected, potentially non-Markovian offsets, requiring robust agent performance from the onset of each episode. Empirical evaluations on offline RL benchmarks, augmented with real-world time-series data to simulate realistic non-stationarity, demonstrate that FORL consistently improves performance compared to competitive baselines. By integrating zero-shot forecasting with the agent’s experience we aim to bridge the gap between offline RL and the complexity of real-world, non-stationary environments.
