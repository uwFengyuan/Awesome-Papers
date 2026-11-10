# AutoDiscovery: Open-ended Scientific Discovery via Bayesian Surprise

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We evaluate AutoDiscovery in the setting of data-driven discovery across 21 real-world datasets spanning domains such as biology, economics, finance, and behavioral science.

[Paper](https://openreview.net/forum?id=kJqTkj2HhF)

Classification / 分类：Financial Agents / 金融Agent与决策 → Investment & Financial Research Agents / 投研与金融决策Agent → General / 综合

## Abstract / 摘要

The promise of autonomous scientific discovery (ASD) hinges not only on answering questions, but also on knowing which questions to ask. Most recent works in ASD explore the use of large language models (LLMs) in goal-driven settings, relying on human-specified research questions to guide hypothesis generation. However, scientific discovery may be accelerated further by allowing the AI system to drive exploration by its own criteria. The few existing approaches in open-ended ASD select hypotheses based on diversity heuristics or subjective proxies for human interestingness, but the former struggles to meaningfully navigate the typically vast hypothesis space, and the latter suffers from imprecise definitions. This paper presents AutoDiscovery—a method for open-ended ASD that instead drives scientific exploration using Bayesian surprise. Here, we quantify the epistemic shift from the LLM’s prior beliefs about a hypothesis to its posterior beliefs after gathering experimental results. To efficiently explore the space of nested hypotheses, our method employs a Monte Carlo tree search (MCTS) strategy with progressive widening using surprisal as the reward function. We evaluate AutoDiscovery in the setting of data-driven discovery across 21 real-world datasets spanning domains such as biology, economics, finance, and behavioral science. Our results demonstrate that under a fixed budget, AutoDiscovery substantially outperforms competitors by producing 5-29% more discoveries deemed surprising by the LLM. Our human evaluation further reveals that two-thirds of discoveries made by our system are surprising to domain experts as well, suggesting this is an important step towards building open-ended ASD systems.
