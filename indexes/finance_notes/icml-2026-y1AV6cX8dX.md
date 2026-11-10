# Mining Useful General Data for Low-Resource Domain Adaptation

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Extensive experiments across medical, financial, legal, and psychological domains demonstrate that NTK-Selector consistently outperforms domain-only fine-tuning and existing data selection baselines.

[Paper](https://openreview.net/forum?id=y1AV6cX8dX)

Classification / 分类：Financial Models & Benchmarks / 金融模型与评测资源 → Financial Pretraining & Adaptation / 金融预训练与领域适配 → General / 综合

## Abstract / 摘要

Adapting large language models (LLMs) to low-resource domains remains challenging due to the scarcity of domain-specific data. While in-domain data is limited, there exists a vast amount of general-domain data that shares similar question–answer formats and reasoning patterns with domain tasks. This observation raises an important question: can useful general-domain data be mined to improve low-resource domain adaptation? Our initial findings show that general-domain chain-of-thought data contains useful auxiliary signals for domain adaptation, even without careful selection. This observation motivates a new paradigm for domain adaptation beyond exclusive reliance on domain-specific data. To systematically identify the most beneficial general-domain samples, we propose NTK-Selector, motivated by the Neural Tangent Kernel’s ability to capture alignment in training dynamics. Since directly applying NTK to pretrained LLMs is impractical, we introduce a Jacobian-free NTK approximation and empirically demonstrate stable NTK-like behavior during fine-tuning. Extensive experiments across medical, financial, legal, and psychological domains demonstrate that NTK-Selector consistently outperforms domain-only fine-tuning and existing data selection baselines. In particular, NTK-Selector achieves gains of +8.7 and +5.1 points on Llama3-8B-Instruct and Qwen3-8B, respectively, compared to only +0.8 and +0.9 points from domain-only fine-tuning.
