# Beyond Suspicious Steps: Ontological Trust in Long-Horizon Agents

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We construct a cross-domain trajectory corpus from OSWorld, FinanceBench, and EICU-AC, covering benign executions, prefix-paired drift, and pseudo-consistency failures.

[Paper](https://openreview.net/forum?id=Skjgiw2yTJ)

Classification / 分类：Financial QA & Reasoning / 金融问答与数值推理 → Knowledge & Conversational QA / 知识与对话问答 → General / 综合

## Abstract / 摘要

Long-horizon agents increasingly operate across many steps, tools, and observations. In this setting, the relevant oversight question is not only whether each action is locally valid, but whether the evolving trajectory still corresponds to the task the user authorized. Drift can accumulate quietly: an agent may call the right tool with plausible arguments at every step, while its prefix moves toward a broader role, an adjacent objective, or evidence the user never supplied. Existing monitors mostly check local compliance, deliver final-trace verdicts, or score generic risk; they do not directly estimate this prefix-level relation. We introduce ontological trust, a task-conditioned property of trajectory prefixes, and instantiate it as RGE, an online monitor that decomposes trust along Role, Goal, and Evidence. RGE uses LLMs only to derive structured representations. State updates, projections, and intervention decisions are deterministic, so the output is a replayable and auditable trust trajectory rather than a single end-to-end judge verdict. We construct a cross-domain trajectory corpus from OSWorld, FinanceBench, and EICU-AC, covering benign executions, prefix-paired drift, and pseudo-consistency failures. On this corpus, RGE outperforms adapted rule-, judge-, and shield-style baselines on prefix-paired drift detection. With the two larger estimator models, it exceeds 93\% Drift F1 on every benchmark while keeping benign coverage at or above 95.8\%. Pseudo-consistency is harder: detection depends on whether task completion is externally visible, a structural limit we characterize empirically.
