# From Token to Token Pair: Efficient Prompt Compression for Large Language Models in Clinical Prediction

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Furthermore, MedTPE demonstrates robustness across different input context lengths and generalisability to scientific and financial domains and different languages.

[Paper](https://openreview.net/forum?id=SRGpmDQjJM)

Classification / 分类：Financial Models & Benchmarks / 金融模型与评测资源 → Cross-Task Financial Evaluation / 跨任务金融综合评测 → General / 综合

## Abstract / 摘要

By processing electronic health records (EHRs) as natural language sequences, large language models (LLMs) have shown potential in clinical prediction tasks such as mortality prediction and phenotyping. However, longitudinal or highly frequent EHRs often yield excessively long token sequences that result in high computational costs and even reduced performance. Existing solutions either add modules for compression or remove less important tokens, which introduce additional inference latency or risk losing clinical information. To achieve lossless compression of token sequences without additional cost or loss of performance, we propose Medical Token-Pair Encoding (MedTPE), a layered method that extends standard tokenisation for EHR sequences. MedTPE merges frequently co-occurring medical token pairs into composite tokens, providing lossless compression while preserving the computational complexity through a dependency-aware replacement strategy. Only the embeddings of the newly introduced tokens of merely 0.5-1.0\% of the LLM’s parameters are fine-tuned via self-supervised learning. Experiments on real-world datasets for two clinical scenarios demonstrate that MedTPE reduces input token length by up to 31\% and inference latency by 34-63\%, while maintaining or even improving both predictive performance and output format compliance across multiple LLMs and four clinical prediction tasks. Furthermore, MedTPE demonstrates robustness across different input context lengths and generalisability to scientific and financial domains and different languages. The code is available in the GitHub repository.
