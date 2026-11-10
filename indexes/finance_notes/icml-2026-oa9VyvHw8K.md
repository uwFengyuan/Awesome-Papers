# Active Tabular Augmentation via Policy-Guided Diffusion Inpainting

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：57.58±5.70 63.99±2.40 62.84±3.16 68.13±2.75 50 65.29±3.52 67.23±1.92 68.21±1.46 60.43±5.29 66.49±2.07 65.53±4.12 62.79±3.26 67.55±1.89 69.72±0.51 Credit-G 100 67.53±2.43 68.27±1.23 68.65±1.63 67.26±1.68 67.27±1.50 66.09±3.05 64.07±2.19 68.15±2.11 70.73±1.66 200 67.85±3.81 69.33±1.38 69.30±1.52 64.41±2.34 67.22±4.42 66.07±2.90 62.77±5.06 70.13±1.73 71.35±1.67 500 71.17±0.64 71.07±0.74 71.50±0.89 68.06±2.18 69.86±1.15 69.53±1.55 66.25±3.14 72.31±1.62 74.21±0.77

[Paper](https://openreview.net/forum?id=oa9VyvHw8K)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Generative tabular augmentation is appealing in data-scarce domains, yet the prevailing focus on distributional fidelity does not reliably translate into better downstream models. We formalize a *fidelity-utility gap*: common generative objectives prioritize distributional plausibility, whereas augmentation succeeds only when injected samples reduce the current learner's held-out evaluation loss. This gap motivates learning not just how to generate, but what to generate and when to inject as training evolves. We propose TAP (Tabular Augmentation Policy), which couples diffusion inpainting with a lightweight, learner-conditioned policy to steer generation toward high-utility regions and controls safe injection via explicit gating and conservative windowed commitment. Under severe data scarcity, TAP consistently outperforms strong generative baselines on seven real-world datasets, improving classification accuracy by up to 15.6 percentage points and reducing regression RMSE by up to 32%.
