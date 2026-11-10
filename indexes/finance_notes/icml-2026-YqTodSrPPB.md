# ANCHOR: Automated Alignment Auditing for CLI Agents on Real-World Harm

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：When agents comply, they frequently exceed user requests, autonomously building infrastructure for large-scale harm, including catastrophic risk scenarios such as large-scale financial fraud and bioweapon development.

[Paper](https://openreview.net/forum?id=YqTodSrPPB)

Classification / 分类：Fraud & AML / 欺诈检测与反洗钱 → Payment & Transaction Fraud / 支付与交易欺诈 → General / 综合

## Abstract / 摘要

Autonomous CLI agents can now execute hundreds of actions across multi-hour sessions: writing code, executing shell commands, browsing the web, and managing cloud infrastructure, all with minimal human oversight. Does greater autonomy invite greater risk? We introduce ANCHOR, an automated auditing framework that stress-tests CLI agents on illegal tasks grounded in public US court cases. ANCHOR deploys an auditor agent fine-tuned on dark personality data using supervised and reinforcement fine tuning. This auditor roleplays persistent malicious users who decompose tasks, reframe requests upon refusal, and adapt strategies across multi-turn interactions. Evaluating frontier CLI agents, we find that while they often refuse illegal tasks when prompted directly, compliance reaches 100\% under persistent malicious interaction. When agents comply, they frequently exceed user requests, autonomously building infrastructure for large-scale harm, including catastrophic risk scenarios such as large-scale financial fraud and bioweapon development. These findings demonstrate that current alignment techniques are insufficient for autonomous agents and underscore the need for safety evaluations against persistent, adaptive malicious users.
