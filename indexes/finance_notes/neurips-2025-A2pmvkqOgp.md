# Forging Time Series with Language: A Large Language Model Approach to Synthetic Data Generation

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.536 0.686 0.775 0.635 0.754 0.823 ECL 0.809 0.941 0.971 0.991 0.997 0.999 Exchange Rate 0.776 0.907 0.942 0.957 0.982 0.989 NN5 0.336 0.479 0.590 0.719 0.780 0.826 Tourism 0.869 0.954 0.977 0.986 0.995 0.998 Traffic 0.376 0.564 0.697 0.408 0.591 0.714 T

[Paper](https://openreview.net/forum?id=A2pmvkqOgp)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Generation / 生成

## Abstract / 摘要

SDForger is a flexible and efficient framework for generating high-quality multivariate time series using LLMs. Leveraging a compact data representation, SDForger provides synthetic time series generation from a few samples and low-computation fine-tuning of any autoregressive LLM. Specifically, the framework transforms univariate and multivariate signals into tabular embeddings, which are then encoded into text and used to fine-tune the LLM. At inference, new textual embeddings are sampled and decoded into synthetic time series that retain the original data's statistical properties and temporal dynamics. Across a diverse range of datasets, SDForger outperforms existing generative models in many scenarios, both in similarity-based evaluations and downstream forecasting tasks. By enabling textual conditioning in the generation process, SDForger paves the way for multimodal modeling and the streamlined integration of time series with textual information. The model is open-sourced at https://github.com/IBM/fms-dgt/tree/main/fms_dgt/public/databuilders/time_series.
