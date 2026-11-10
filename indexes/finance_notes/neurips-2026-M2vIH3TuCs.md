# Test-Time Scaling in the Wild: Why Exploitation, Not Exploration, Is the Bottleneck

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine, law, finance, general chat, and creative writing — grounded in a unified framework that decomposes the effectiveness of each method's token budget into exploration and exploitation.

[Paper](https://openreview.net/forum?id=M2vIH3TuCs)

Classification / 分类：Financial Models & Benchmarks / 金融模型与评测资源 → Cross-Task Financial Evaluation / 跨任务金融综合评测 → General / 综合

## Abstract / 摘要

Test-time scaling (TTS) improves language model outputs by spending additional inference compute — generating multiple candidates, searching over partial sequences, or iteratively refining drafts. These techniques yield large gains on mathematics and code, but have been developed and stress-tested almost exclusively on tasks where verification is straightforward. We conduct the first compute-normalised comparison of five TTS families across five open-ended generation benchmarks spanning medicine, law, finance, general chat, and creative writing — grounded in a unified framework that decomposes the effectiveness of each method's token budget into exploration and exploitation. The answer depends on which side of that decomposition you examine. Scaling exploration works: the best candidate in the pool improves steadily with compute across all settings. What breaks is exploitation — the step that converts a rich candidate pool into a final output. With state-of-the-art generators, reward models correlate at only $\hat{\rho}_v$ $\approx$ 0.12 with true quality, rendering selection near-random regardless of budget. Tree search amplifies this failure through diversity collapse. Refinement helps on one of five benchmarks; its apparent gains elsewhere are confounded. Only synthesis across candidates (Fusion) consistently improves over single-sample baselines, yet still recovers only ${\sim}$40% of available quality.The candidate pool is not the bottleneck — choosing from it is.
