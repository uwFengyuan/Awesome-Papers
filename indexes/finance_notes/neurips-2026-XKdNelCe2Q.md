# FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：1.042 0.733 1.186 0.772 1.292 0.836 1.251 0.820 1.201 0.783 1.478 0.834 - - 1.337 0.829 1.299 0.795 NYSE 0.527 0.553 0.442 0.430 0.529 0.507 0.880 0.642 0.620 0.626 - - 0.988 0.704 1.129 0.720 - - - - 0.492 0.441 1st Count 8 8 6 4 15 9

[Paper](https://openreview.net/forum?id=XKdNelCe2Q)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

In this work, we introduce FLAME, a family of extremely lightweight and capable Time Series Foundation Models, which support versatile forecasting tasks via generative probabilistic modeling, while ensuring both efficiency and robustness. FLAME utilizes the Legendre Memory for strong generalization capabilities. Through adapting variants of Legendre Memory, i.e., translated Legendre (LegT) and scaled Legendre (LegS), in the Encoding and Decoding phases, FLAME can effectively capture the inherent inductive bias within data and make efficient long-range inferences. To enhance the accuracy of probabilistic forecasting while keeping efficient, FLAME adopts a Normalizing Flow based forecasting head, which can model the arbitrarily intricate distributions over the forecasting horizon in a generative manner. Comprehensive experiments on four well-recognized benchmarks, including TSFM-Bench, ProbTS, TFB, and GIFT-EVAL, demonstrate that FLAME is a strong out-of-the-box tool of decision intelligence.
