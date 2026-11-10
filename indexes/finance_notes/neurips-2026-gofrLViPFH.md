# Learning the Context of Errors: Black-Box Online Adaptation of Time Series Foundation Models

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：% 0.0232 -15.3% 0.0233 -11.4% 0.0231 -10.9% 0.0232 -6.5% -10.6% Vanilla 0.0031 0.0033 0.0035 0.0033 0.0042 Exchange Refined 0.0031 -0.0% 0.0034 2.0% 0.0032 -8.5% 0.0032 -3.1% 0.0037 -10.4% -4.0% Vanilla 0.0477 0.0565 0.0542 0.0497 0.0415 Weather Refined 0.0435 -8.9% 0.0446 -21.2% 0.0463 -14.5% 0.0441 -11.3% 0.0408 -1.7% -11.5% Vanilla 0.0571 0.0576 0.0549 0.0579 0.0484 Electricity Refined 0.0517 -9.5% 0.0522 -9.5% 0.0503

[Paper](https://openreview.net/forum?id=gofrLViPFH)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Foundation models / 基础模型

## Abstract / 摘要

The rapid evolution of Time Series Foundation Models (TSFMs) has advanced zero-shot forecasting across diverse domains. Inspired by the current form of Large Language Models, future TSFMs may be offered as commercialized, closed-source API services. However, many existing online adaptation methods still rely on white-box access for parameter fine-tuning or gradient backpropagation. This paradigm mismatch raises a question: *In black-box online adaptation for TSFMs, what should we learn?* We answer this with an insight: the predictive errors of the base model are conditioned on both the input and output of the base model (i.e., the context of errors). To validate this insight, we propose **ORCA** (Online Residual Contextual Adaptation). We conduct extensive experiments across 5 state-of-the-art TSFMs and 8 datasets to demonstrate the effectiveness of our approach. Furthermore, through ablation studies, we quantitatively analyze the impact of different adapter learning hypotheses on the final adaptation performance in black-box online adaptation. Code available at https://anonymous.4open.science/r/ORCA1/.
