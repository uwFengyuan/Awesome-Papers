# Cost-efficient Collaboration between On-device and Cloud Language Models

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We investigate an emerging setup in which a small, on-device language model (LM) with access to local data collaborates with a frontier, cloud-hosted LM to solve real-world tasks involving financial, medical, and scientific reasoning over long documents.

[Paper](https://openreview.net/forum?id=qGDlzt3dKz)

Classification / 分类：Financial Models & Benchmarks / 金融模型与评测资源 → Cross-Task Financial Evaluation / 跨任务金融综合评测 → General / 综合

## Abstract / 摘要

We investigate an emerging setup in which a small, on-device language model (LM) with access to local data collaborates with a frontier, cloud-hosted LM to solve real-world tasks involving financial, medical, and scientific reasoning over long documents. *Can a local-remote collaboration reduce cloud inference costs while preserving quality?*First, we consider a naïve collaboration protocol, coined MINION, where the local and remote models simply chat back and forth. Because only the local model ingests the full context, this protocol reduces cloud costs by 30.4x, but recovers only 87% of the performance of the frontier model.We identify two key limitations of this protocol: the local model struggles to (1) follow the remote model's multi-step instructions and (2) reason over long contexts. Motivated by these observations, we propose MINIONS, a protocol in which the remote model decomposes the task into easier subtasks over shorter chunks of the document, that are executed locally in parallel. MINIONS reduces costs by 5.7× on average while recovering 97.9% of the remote-only performance. Our analysis reveals several key design choices that influence the trade-off between cost and performance in local-remote systems.
