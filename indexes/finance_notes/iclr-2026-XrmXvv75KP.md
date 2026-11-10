# SwiftTS: A Swift Selection Framework for Time Series Pre-trained Models via Multi-task Meta-Learning

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：-0.284 0.251 H=192 -0.040 -0.597 -0.414 0.246 0.152 0.154 -0.273 0.252 Exchange H=336 -0.112 -0.536 -0.306 0.148 0.250 0.230 -0.143 0.233 H=720 -0.210 -0.617 -0.444 -0.024 0.536 0.322 0.126 -0.386 H=96 -0.117 0.058 -0.148 0.113 -0.153 0.511 -0.384 0.656 H=192 -0.285 -0.235 -0.274 -0

[Paper](https://openreview.net/forum?id=XrmXvv75KP)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Foundation models / 基础模型

## Abstract / 摘要

Pre-trained models exhibit strong generalization to various downstream tasks. However, given the numerous models available in the model hub, identifying the most suitable one by individually fine-tuning is time-consuming. In this paper, we propose \textbf{SwiftTS}, a swift selection framework for time series pre-trained models. To avoid expensive forward propagation through all candidates, SwiftTS adopts a learning-guided approach that leverages historical dataset-model performance pairs across diverse horizons to predict model performance on unseen datasets. It employs a lightweight dual-encoder architecture that embeds time series and candidate models with rich characteristics, computing patchwise compatibility scores between data and model embeddings for efficient selection. To further enhance the generalization across datasets and horizons, we introduce a horizon-adaptive expert composition module that dynamically adjusts expert weights, and the transferable cross-task learning with cross-dataset and cross-horizon task sampling to enhance out-of-distribution (OOD) robustness. Extensive experiments on 14 downstream datasets and 8 pre-trained models demonstrate that SwiftTS achieves state-of-the-art performance in time series pre-trained model selection. The code and datasets are available at \href{}{https://github.com/decisionintelligence/SwiftTS}.
