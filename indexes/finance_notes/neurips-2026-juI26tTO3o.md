# BALTO: Balanced Token-Level Policy Optimization for Hallucination Mitigation

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Experiments on ConFiQA, RAGTruth, and FinLLM-Eval show that BALTO achieves the highest faithfulness across all six model--benchmark settings and consistently outperforms existing post-training baselines in Q-Score, demonstrating a stronger faithfulness--informativeness trade-off.

[Paper](https://openreview.net/forum?id=juI26tTO3o)

Classification / 分类：Financial Safety & Compliance / 金融安全与合规 → Financial Regulation / 金融监管与业务规则 → General / 综合

## Abstract / 摘要

Hallucinations remain a major obstacle to deploying large language models (LLMs) in knowledge-intensive settings, where generated responses must be faithfully grounded in provided evidence.  Reinforcement learning (RL) is a promising direction for hallucination mitigation, but response-level faithfulness rewards suffer from a granularity mismatch: localized hallucinations can cause supported content to receive spurious penalties. Although recent work introduces fine-grained feedback such as claim-level verification and token-level rewards, unbalanced credit assignment can still induce length, verbosity, or optimization-noise biases. We propose $\textbf{BALTO}$, a $\textbf{Bal}$anced $\textbf{T}$oken-level Policy $\textbf{O}$ptimization framework for hallucination mitigation. BALTO extracts checkable factual claims, verifies them against the reference context, and projects claim-level judgments to token-level labels. A balanced token-level credit assignment mechanism is introduced into the framework. This design redistributes probability mass from unsupported content toward faithful content, rather than suppressing the entire response. We systematically analyze the limitations of response-level rewards from a theoretical standpoint, and prove BALTO’s advantages in training stability and optimization efficiency for hallucination mitigation.  Experiments on ConFiQA, RAGTruth, and FinLLM-Eval show that BALTO achieves the highest faithfulness across all six model--benchmark settings and consistently outperforms existing post-training baselines in Q-Score, demonstrating a stronger faithfulness--informativeness trade-off.
