# TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：9 1.05 1.14 loop_seattle/H/short 0.850 ± 0.005 0.900 0.915 0.832 1.15 0.912 0.945 1.06 1.08 0.926 0.967 m4_daily/D/short 3.15 ± 0.063 3.20 3.19 3.09 3.27 4.31 4.18 5.37 4.40 3.18 3.16 m4_hourly/H/short 0.719 ± 0.026 0.837 0.866 0.596 0.768 0.780 0.886 0.971 2.78 0.693 0.739 m4_monthly/M/short 0.929 ± 0.004 0.949 0.954

[Paper](https://openreview.net/forum?id=v7UqniC9pF)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

In-context learning, the ability of large language models to perform tasks using only examples provided in the prompt, has recently been adapted for time series forecasting.  This paradigm enables zero-shot prediction, where past values serve as context for forecasting future values,  making powerful forecasting tools accessible to non-experts and increasing the performance when training data are scarce. Most existing zero-shot forecasting approaches rely on transformer architectures, which, despite their success in language, often fall short of expectations in time series forecasting, where recurrent models like LSTMs frequently have the edge. Conversely, while LSTMs are well-suited for time series modeling due to their state-tracking capabilities, they lack strong in-context learning abilities. We introduce *TiRex* that closes this gap by leveraging xLSTM, an enhanced LSTM with competitive in-context learning skills. Unlike transformers, state-space models, or parallelizable RNNs such as RWKV, TiRex retains state tracking, a critical property for long-horizon forecasting. To further facilitate its state-tracking ability, we propose a training-time masking strategy called CPM. TiRex sets a new state of the art in zero-shot time series forecasting on the Hugging Face benchmarks *GiftEval* and *Chronos-ZS*, outperforming significantly larger models including *TabPFN-TS* (Prior Labs), *Chronos Bolt* (Amazon), *TimesFM* (Google), and *Moirai* (Salesforce) across both short- and long-term forecasts.
