# Sketching the Readout of Large Language Models for Scalable Data Attribution and Valuation

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We validate RISE on three tasks: Howdy backdoor data detection, Finance-Medical domain separation, and Brain Rot high-quality data selection.

[Paper](https://openreview.net/forum?id=DFNRxCD5mZ)

Classification / 分类：Financial Safety & Compliance / 金融安全与合规 → Adversarial Robustness in Finance / 金融应用中的攻击与防御 → General / 综合

## Abstract / 摘要

Data attribution and valuation are critical for understanding data-model synergy for Large Language Models (LLMs), yet existing gradient-based methods suffer from scalability challenges on LLMs. Inspired by human cognition, where decision making relies on a focused readout of relevant memories rather than replaying all pathways, we introduce **RISE (Readout Influence Sketching Estimator)**. Instead of computing and indexing gradients across the entire LLM, RISE focuses on influence hotspots at the output layer, where influence signals concentrate, and the gradient admits a decomposed outer-product form. This enables a dual-channel representation combining a lexical residual channel (RH) and a semantic projected-error channel (GH). Applying CountSketch projections to these channels achieves strong compression while maintaining accurate attribution. Across the OLMo (1B–32B) and Pythia (14M–6.9B) families, RISE reduces index storage by up to 112$\times$ compared to RapidIn and scales to 32B parameters LLM, where gradient-based baselines such as RapidIn and ZO-Inf become memory-infeasible. We evaluate RISE on two paradigms: (1) retrospective attribution, retrieving influential training examples for specific predictions, and (2) prospective valuation, scoring candidate data utility zero-shot. We validate RISE on three tasks: Howdy backdoor data detection, Finance-Medical domain separation, and Brain Rot high-quality data selection. In a closed-loop Brain Rot study, continued pretraining on RISE-selected data yields consistent downstream improvements. Overall, RISE provides a practical and scalable primitive for influence analysis and training-data selection in modern large language models.
