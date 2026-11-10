# TimeXL: Explainable Multi-modal Time Series Prediction with LLM-in-the-Loop

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：AUROC (AUC) for TimeXL and state-of-the-art baselines on multi- modal time series datasets. Weather Finance Healthcare (TP) Healthcare (MT) Datasets → Methods ↓ F1 AUC F1 AUC F1 AUC F1 AUC DLinear [75] 0.540 0.660 0.255 0.485 0.393 0.500 0.419 0.388 Autoformer [76] 0.546 0.590 0.565 0.747 0.774 0.918 0.683 0.825 Crossformer [77] 0.500 0.594 0.571 0.775 0.924 0.984 0.737 0.913 TimesNet [78] 0.494 0.594 0.538 0.756 0.794 0.867 0.765 0.944 iTransformer [79] 0.541 0.650 0.600 0.783 0.861 0.931 0.791 0.963 TSMixer [80] 0.488 0.534 0.465 0.689 0.770 0.797 0.808 0.931 TimeMixer [81] 0.577 0.658 0.571 0.776 0.822 0.887 0.824 0.935 FreTS [82] 0.623 0.688 0.546 0.737 0.887 0.950 0.751 0.762 PatchTST [5] 0.592 0.675 0.604 0.795 0.841 0.934

[Paper](https://openreview.net/forum?id=WRwr2YZ4zt)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series analysis provides essential insights for real-world system dynamics and informs downstream decision-making, yet most existing methods often overlook the rich contextual signals present in auxiliary modalities. To bridge this gap, we introduce TimeXL, a multi-modal prediction framework that integrates a prototype-based time series encoder with three collaborating Large Language Models (LLMs) to deliver more accurate predictions and interpretable explanations. First, a multi-modal prototype-based encoder processes both time series and textual inputs to generate preliminary forecasts alongside case-based rationales. These outputs then feed into a prediction LLM, which refines the forecasts by reasoning over the encoder's predictions and explanations. Next, a reflection LLM compares the predicted values against the ground truth, identifying textual inconsistencies or noise. Guided by this feedback, a refinement LLM iteratively enhances text quality and triggers encoder retraining. This closed-loop workflow---prediction, critique (reflect), and refinement---continuously boosts the framework's performance and interpretability. Empirical evaluations on four real-world datasets demonstrate that TimeXL achieves up to 8.9\% improvement in AUC and produces human-centric, multi-modal explanations, highlighting the power of LLM-driven reasoning for time series prediction.
