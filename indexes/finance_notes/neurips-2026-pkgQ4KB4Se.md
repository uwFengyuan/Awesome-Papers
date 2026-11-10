# PAAC: Privacy-Aware Agentic Device-Cloud Collaboration

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We find consistent improvements on 17 additional benchmarks spanning 10 domains, including math, science, and finance.

[Paper](https://openreview.net/forum?id=pkgQ4KB4Se)

Classification / 分类：Financial QA & Reasoning / 金融问答与数值推理 → Numerical & Table Reasoning / 数值与表格推理 → General / 综合

## Abstract / 摘要

Large language model (LLM) agents face a structural tension: cloud agents provide strong reasoning but expose user data, while on-device agents preserve privacy at the cost of overall capability. Existing device-cloud designs treat this boundary as a compute split rather than a trust boundary suited to agentic workloads, and existing sanitizers force a choice between policy flexibility and the structural fidelity tool calls require. In this work, we develop PAAC, a privacy-aware agentic framework that aligns planner--executor decomposition with the device-cloud boundary so that role specialization itself becomes the privacy mechanism. The cloud agent reasons over typed placeholder tokens that preserve each sensitive value's reasoning role while discarding its content, while the on-device agent identifies sensitive spans and distills each step's execution outcome into compact key findings. Sanitization confines the on-device LLM to proposing which spans to mask, while a deterministic registry performs all substitution and reversal, keeping actions directly executable on device. On three agentic benchmarks under strict privacy settings, PAAC dominates the Pareto frontier of privacy and accuracy, improving average accuracy by 15-36\% and reducing average leakage by 2-6$\times$ over state-of-the-art device-cloud baselines, with the largest margins on privacy targets outside fixed entity taxonomies. We find consistent improvements on 17 additional benchmarks spanning 10 domains, including math, science, and finance.
