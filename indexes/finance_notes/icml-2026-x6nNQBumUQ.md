# Towards Professional-Grade Financial Agents: Benchmarking, Tooling, and Structured Reasoning

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：While Large Language Model (LLM) agents have shown encouraging progress in financial reasoning, their effectiveness in realistic financial workflows is severely hindered by the lack of holistic benchmarks and the fragility of unstructured reasoning. / To address this gap, we introduce ProFinR, the first Professional Finance Reasoning benchmark, covering four financial domain tasks and comprising 528 expert-designed problems. / To solve these complex financial reasoning questions, we construct the Financial Tool Universe, a tool library containing 53 domain-specific tools organized into 13 categories.

[Paper](https://openreview.net/forum?id=x6nNQBumUQ)

Classification / 分类：Financial Agents / 金融Agent与决策 → Investment & Financial Research Agents / 投研与金融决策Agent → General / 综合

## Abstract / 摘要

While Large Language Model (LLM) agents have shown encouraging progress in financial reasoning, their effectiveness in realistic financial workflows is severely hindered by the lack of holistic benchmarks and the fragility of unstructured reasoning. To address this gap, we introduce ProFinR, the first Professional Finance Reasoning benchmark, covering four financial domain tasks and comprising 528 expert-designed problems. To solve these complex financial reasoning questions, we construct the Financial Tool Universe, a tool library containing 53 domain-specific tools organized into 13 categories. Building on the tool library, we introduce ProFinAgent, a structured agent framework based on Directed Acyclic Graph (DAG) and Case-Based Memory (CBM). Compared with strictly sequential workflows, ProFinAgent coordinates tool execution through a DAG planner for parallel efficiency and uses CBM to retrieve prior cases for more reliable decision-making. Experimental results demonstrate that ProFinAgent achieves a 49.81% performance gain over state-of-the-art baselines with a 47.1% reduction in inference latency. Our code is available at https://github.com/tsinghua-fib-lab/ProFinAgent.
