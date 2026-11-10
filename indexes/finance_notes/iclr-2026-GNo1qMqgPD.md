# VoxPrivacy: A Benchmark for Evaluating Interactional Privacy of Speech Language Models

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ollowing: •Personally Identifiable Information: Name, address, Social Security number, passport number, driver's license number, email address, and phone number •Financial Records: Financial account numbers, credit card details, and any other data related to personal finances … Some Examples: •I applied for a bank card a few days ago, and my password is 123456. •Tony applied for a mortgage today. The total amount appears to be $800,000, with an interest rate of 4.2%. •The mobile phone number associated with my PayPal account is 138xxxx5678.

[Paper](https://openreview.net/forum?id=GNo1qMqgPD)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

As Speech Language Models (SLMs) transition from personal devices to shared, multi-user environments such as smart homes, a new challenge emerges: the model is expected to distinguish between users to manage information flow appropriately. Without this capability, an SLM could reveal one user’s confidential schedule to another—a privacy failure we term **interactional privacy**. Thus, the ability to generate speaker-aware responses becomes essential for SLM safe deployment. Current SLM benchmarks test dialogue ability but overlook speaker identity. Multi-speaker benchmarks check who said what without assessing whether SLMs adapt their responses. Privacy benchmarks focus on globally sensitive data (e.g., bank passwords) while neglecting contextually sensitive information (e.g., a user’s private appointment). To address this gap, we introduce **VoxPrivacy**, the first benchmark designed to evaluate interactional privacy in SLMs. VoxPrivacy spans three tiers of increasing difficulty, from following direct secrecy commands to proactively protecting privacy. Our evaluation of nine SLMs on a 32-hour bilingual dataset reveals a widespread vulnerability: most open-source models perform close to random chance (around 50\% accuracy) on conditional privacy decisions, while even strong closed-source systems still fall short on proactive privacy inference. We further validate these findings on Real-VoxPrivacy, a human-recorded subset, confirming that the failures observed on synthetic data persist in real speech. We also demonstrate a viable path forward: by fine-tuning on a new 4,000-hour training set, we improve the model’s privacy-preserving capabilities while achieving fair robustness. To support future work, we are releasing the VoxPrivacy benchmark, the large-scale training set, and the fine-tuned model to help the development of safer and more context-aware SLMs.
