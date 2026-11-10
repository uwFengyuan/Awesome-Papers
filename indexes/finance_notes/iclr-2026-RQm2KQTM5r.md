# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

ICLR 2026 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：to the claim, followed by a concise summary that clearly states whether the claim is supported or refuted based on the aggregated information. Ensure the reasoning explicitly a data table format that includes stock prices, dividend payouts, and percentage changes over various time intervals such as 5 days, 1 month, year-to-date, 1 year, and 5 years. Outline key indicators that investors typically weigh when making decisions, how to interpret short-term versus long-term performance trends, and suggest strategies or metrics to use when making

[Paper](https://openreview.net/forum?id=RQm2KQTM5r)

Classification / 分类：Financial Models & Benchmarks / 金融模型与评测资源 → Financial Pretraining & Adaptation / 金融预训练与领域适配 → General / 综合

## Abstract / 摘要

Large language models (LLMs) are increasingly adapted to downstream tasks via reinforcement learning (RL) methods like Group Relative Policy Optimization (GRPO), which often require thousands of rollouts to learn new tasks. We argue that the interpretable nature of language often provides a much richer learning medium for LLMs, compared to policy gradients derived from sparse, scalar rewards. To test this, we introduce GEPA (Genetic-Pareto), a prompt optimizer that thoroughly incorporates natural language reflection to learn high-level rules from trial and error.     Given any AI system containing one or more LLM prompts, GEPA samples trajectories (e.g., reasoning, tool calls, and tool outputs) and reflects on them in natural language to diagnose problems, propose and test prompt updates, and combine complementary lessons from the Pareto frontier of its own attempts. As a result of GEPA's design, it can often turn even just a few rollouts into a large quality gain.     Across six tasks, GEPA outperforms GRPO by 6 percentage points on average and by up to 19pp, while using up to 35x fewer rollouts. GEPA also outperforms the leading prompt optimizer, MIPROv2, by over 10 percentage points (e.g., +12pp on AIME-2025), and demonstrates promising results as an inference-time search strategy for code optimization. We release our code at https://github.com/gepa-ai/gepa.
