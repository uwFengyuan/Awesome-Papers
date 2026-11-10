# Self-Jailbreaking: Language Models Can Reason Themselves Out of Safety Alignment After Benign Reasoning Training

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：For instance, an RLM reasons that harmful requests like "outline a strategy for stealing customers’ credit card information from a retail store" could be associated with the benign intent of "a security professional trying to test defense," despite no such benign context being provided as input.

[Paper](https://openreview.net/forum?id=akbtPEZnDZ)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

We discover a novel and surprising phenomenon of unintentional misalignment in reasoning language models (RLMs), which we call **self-jailbreaking**. Specifically, after benign reasoning training on math or code domains, RLMs will use multiple strategies to circumvent their own safety guardrails. One strategy is to introduce benign assumptions about users and scenarios to justify fulfilling harmful requests. For instance, an RLM reasons that harmful requests like "outline a strategy for stealing customers’ credit card information from a retail store" could be associated with the benign intent of "a security professional trying to test defense," despite no such benign context being provided as input. We observe that many open-weight RLMs, including DeepSeek-R1-distilled, s1.1, Phi-4-mini-reasoning, and Nemotron, suffer from self-jailbreaking despite being aware of the harmfulness of the requests. We also provide a mechanistic understanding of self-jailbreaking: RLMs are more compliant after benign reasoning training, and after self-jailbreaking, models appear to perceive malicious requests as less harmful in the CoT, thus enabling compliance with them. To mitigate self-jailbreaking, we find that including minimal safety reasoning data during training is sufficient to ensure RLMs remain safety-aligned. Our work provides the first systematic analysis of self-jailbreaking behavior and offers a practical path forward for maintaining safety in increasingly capable RLMs.
