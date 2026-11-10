# Monitoring Monitorability

ICML 2026 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：. • Memory: We created synthetic scenarios and user memories both with and without certain demographic attributes (e.g., gender) and ask the model for recommendations across a variety of topics (e.g., personal finance, parenting, fitness). The prompts themselves do not contain the synthetic demographic attributes of the user. We evaluate whether the model changes it’s behavior based on these demographic attributes appearing in the user memory, and we ask if this bias is monitorable. • Toy Math/Science: We take multiple-choice math datasets GPQA, D

[Paper](https://openreview.net/forum?id=b82fgbMVpz)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Banking Dialogue & Intent / 银行对话与意图 → General / 综合

## Abstract / 摘要

Safe deployment of increasingly capable AI agents may require visibility into how they make decisions. Chain-of-thought (CoT) monitoring can detect misbehavior in today’s reasoning models, but this “monitorability” may be fragile under different training procedures, data sources, or continued system scaling. We propose three evaluation archetypes (intervention, process, and outcome-property), a new monitorability metric, and a broad evaluation suite. We show CoT monitoring outperforms action-only monitoring in practical settings, and that frontier models are generally—but not perfectly—monitorable. We study scaling trends with pre-training model size and inference-time compute, finding longer CoTs are typically more monitorable. We find that, for a fixed capability level, using a smaller model at higher reasoning effort can yield higher monitorability, at greater inference compute cost. We further find that increasing a weak monitor’s test-time compute when monitoring a strong agent improves monitorability, and giving the monitor access to the CoT both boosts monitorability and steepens the compute–to-monitorability scaling trend. Finally, we show monitorability can be improved by asking follow-up questions and giving the follow-up CoT to the monitor.
