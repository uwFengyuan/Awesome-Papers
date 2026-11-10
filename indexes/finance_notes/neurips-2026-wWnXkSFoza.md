# Inadvertent Context Leakage in Language Models

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：For LLM agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. / We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent at 100% success.

[Paper](https://openreview.net/forum?id=wWnXkSFoza)

Classification / 分类：Financial Safety & Compliance / 金融安全与合规 → Financial Privacy & Security / 金融隐私与信息安全 → General / 综合

## Abstract / 摘要

For LLM agents to be useful beyond simple chat, they must hold sensitive user context such as calendars, credentials, health records, and financial data. We study whether the mere presence of such secrets in a model's context window introduces hidden correlations into the model's benign outputs, allowing reconstruction even when the model correctly refuses direct extraction. We further study whether an adversary can actively engineer prompts that amplify this effect, using the model as a covert carrier to transmit secrets through seemingly innocuous text. In both cases, this limited leakage is exploited using a novel _adaptive_ attack that assumes black-box access to the underlying model.  In controlled experiments across eight proprietary models, we find that 2-digit in-context secrets are reconstructed with near-perfect accuracy and 4-digit secrets at 82% exact match, all from outputs the model produces in response to ordinary, non-adversarial requests. More capable models leak more: stronger instruction-following amplifies sensitivity to in-context secrets, making leakage a byproduct of capability rather than a bug to be patched. We show this leakage enables two practical attacks: (1) a trained classifier that infers semantic predicates about user memories (e.g., health conditions, financial events) from routine natural-language outputs, and (2) an RL-trained adversary that extracts full Social Security Numbers from a production-style agent at 100% success.
