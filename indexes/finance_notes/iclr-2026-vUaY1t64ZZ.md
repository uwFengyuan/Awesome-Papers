# Holistic Agent Leaderboard: The Missing Infrastructure for AI Agent Evaluation

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：the benchmark on HuggingFace rather than ac- tually solving the task of interest (Challenge #7); (ii) agents often take actions that would be catastrophic if deployed to real-world products, such as using a wrong credit card to make flight bookings (Challenge #8); (iii) log analysis can help uncover bugs and other shortcomings in agent scaffolds. For example, we uncovered a major bug in a scaffold for the TAU-Bench bench- mark, after we had conducted evaluations that cost a significant amount to run.* ; and (iv) log analysis can help uncover potential impr

[Paper](https://openreview.net/forum?id=vUaY1t64ZZ)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

AI agents have been developed for complex real-world tasks from coding to customer service. But AI agent evaluations suffer from many challenges that undermine our understanding of how well agents really work (Figure 1). We introduce the Holistic Agent Leaderboard (HAL) to address these challenges. We make three main contributions. First, we provide a standardized evaluation harness that orchestrates parallel evaluations across hundreds of VMs, reducing evaluation time from weeks to hours while eliminating common implementation bugs. Second, we conduct three-dimensional analysis spanning models, scaffolds, and benchmarks. We validate the harness by conducting 21,730 agent rollouts across 9 models and 9 benchmarks in coding, web navigation, science, and customer service with a total cost of about $40,000. Our analysis reveals surprising insights, such as higher reasoning effort reducing accuracy in the majority of runs. Third, we use LLM-aided log inspection to uncover previously unreported behaviors, such as searching for the benchmark on HuggingFace instead of solving a task, or misusing credit cards in flight booking tasks. We share all agent logs, comprising 2.5B tokens of language model calls, to incentivize further research into agent behavior. By standardizing how the field evaluates agents and addressing common pitfalls in agent evaluation, we hope to shift the focus from agents that ace benchmarks to agents that work reliably in the real world.
