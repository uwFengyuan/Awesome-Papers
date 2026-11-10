# Conformal Risk Training: End-to-End Optimization of Conformal Risk Control

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Our method achieves provable risk guarantees while demonstrating significantly improved average-case performance over post-hoc approaches on applications to controlling classifiers' false negative rate and controlling financial risk in battery storage operation.

[Paper](https://openreview.net/forum?id=uBEiZd2P0K)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Financial Risk / 金融风险管理 → General / 综合

## Abstract / 摘要

While deep learning models often achieve high predictive accuracy, their predictions typically do not come with any provable guarantees on risk or reliability, which are critical for deployment in high-stakes applications. The framework of conformal risk control (CRC) provides a distribution-free, finite-sample method for controlling the expected value of any bounded monotone loss function and can be conveniently applied post-hoc to any pre-trained deep learning model. However, many real-world applications are sensitive to tail risks, as opposed to just expected loss. In this work, we develop a method for controlling the general class of Optimized Certainty-Equivalent (OCE) risks, a broad class of risk measures which includes as special cases the expected loss (generalizing the original CRC method) and common tail risks like the conditional value-at-risk (CVaR). Furthermore, standard post-hoc CRC can degrade average-case performance due to its lack of feedback to the model. To address this, we introduce "conformal risk training," an end-to-end approach that differentiates through conformal OCE risk control _during model training or fine-tuning_. Our method achieves provable risk guarantees while demonstrating significantly improved average-case performance over post-hoc approaches on applications to controlling classifiers' false negative rate and controlling financial risk in battery storage operation.
