# Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：In November 2024, this risk materialized when a developer reportedly lost 2,500 USD after ChatGPT generated an otherwise routine cryptocurrency trading script containing a live phishing URL.

[Paper](https://openreview.net/forum?id=jEQQBE30m1)

Classification / 分类：Fraud & AML / 欺诈检测与反洗钱 → Scams & Financial Misinformation / 诈骗与金融虚假信息 → General / 综合

## Abstract / 摘要

The insatiable demand for web-scale training data has exposed LLMs to a subtle but consequential threat: the absorption of malicious scam content into model weights and its subsequent reproduction during inference. In November 2024, this risk materialized when a developer reportedly lost 2,500 USD after ChatGPT generated an otherwise routine cryptocurrency trading script containing a live phishing URL. To systematically investigate this problem, we introduce Scam2Prompt, an automated auditing framework that crawls known scam websites, infers their functional intent, and synthesizes innocuous developer-style prompts — the kind of legitimate coding requests a programmer might naturally submit — to evaluate whether LLMs reproduce the underlying scam endpoints. Importantly, our approach requires neither jailbreaking nor adversarial prompting; all 1,377 prompts in our benchmark, Innoc2Scam-bench, which is automatically constructed by Scam2Prompt, were human-validated as benign coding tasks. Evaluation of seven production LLMs released in 2025 on Innoc2Scam-bench shows that the vulnerability proves both persistent and severe: malicious code generation rates range from 12.9% to 47.3% across the evaluated models, and no tested model proves immune. State-of-the-art guardrails and RAG-based agents offer only limited protection, underscoring an urgent need for explicit URL validation in LLM-assisted software development pipelines.
