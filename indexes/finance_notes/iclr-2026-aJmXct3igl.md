# Type-Compliant Adaptation Cascades

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Gains are particularly pronounced on structured tasks, improving FinQA from $12.0\%$ to $24.7\%$ for a Qwen 3 8B model, MGSM-SymPy from $57.1\%$ to $75.9\%$ for a Gemma 2 27B model, MGSM from $1.6\%$ to $27.3\%$, and MuSR from $36.5\%$ to $62.6\%$ for a Gemma 7B model.

[Paper](https://openreview.net/forum?id=aJmXct3igl)

Classification / 分类：Financial QA & Reasoning / 金融问答与数值推理 → Numerical & Table Reasoning / 数值与表格推理 → General / 综合

## Abstract / 摘要

Reliably composing Large Language Models (LLMs) for complex, multi-step workflows remains a significant challenge. The dominant paradigm---optimizing discrete prompts in a pipeline---is notoriously brittle and struggles to enforce the formal compliance required for structured tasks. We introduce Type-Compliant Adaptation Cascades (TACs), a framework that recasts workflow adaptation as learning typed probabilistic programs. TACs treat the entire workflow, which is composed of parameter-efficiently adapted LLMs and deterministic logic, as an unnormalized joint distribution. This enables principled, gradient-based training even with latent intermediate structures. We provide theoretical justification for our tractable optimization objective, proving that the optimization bias vanishes as the model learns type compliance. Empirically, TACs significantly outperform state-of-the-art prompt-optimization baselines. Gains are particularly pronounced on structured tasks, improving FinQA from $12.0\%$ to $24.7\%$ for a Qwen 3 8B model, MGSM-SymPy from $57.1\%$ to $75.9\%$ for a Gemma 2 27B model, MGSM from $1.6\%$ to $27.3\%$, and MuSR from $36.5\%$ to $62.6\%$ for a Gemma 7B model. TACs offer a robust and theoretically grounded paradigm for developing reliable, task-compliant LLM systems.
