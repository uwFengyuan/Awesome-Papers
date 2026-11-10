# From Similarity to Vulnerability: Key Collision Attack on LLM Semantic Caching

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：A case study on a financial agent further illustrates the real-world impact.

[Paper](https://openreview.net/forum?id=BQfNL1wahQ)

Classification / 分类：Financial Agents / 金融Agent与决策 → Investment & Financial Research Agents / 投研与金融决策Agent → General / 综合

## Abstract / 摘要

Semantic caching has emerged as a pivotal technique for scaling LLM applications, widely adopted by providers including AWS and Microsoft. By utilizing embedding vectors as cache keys, this mechanism effectively minimizes latency and redundant computation for semantically similar queries. In this work, we conceptualize semantic cache keys as a form of fuzzy hashes. We demonstrate that the locality required to maximize cache hit rates fundamentally conflicts with the cryptographic avalanche effect necessary for collision resistance.  Our conceptual analysis formalizes this inherent trade-off between performance (locality) and security (collision resilience), revealing that semantic caching is inherently vulnerable to key collision attacks. While prior research has focused on side-channel and privacy risks, we present the first systematic study of integrity risks arising from cache collisions. We introduce CacheAttack, an automated framework for launching black-box collision attacks.  We evaluate CacheAttack in security-critical tasks and agentic workflows. It achieves a hit rate of 86\% in LLM response hijacking and can induce malicious behaviors in LLM agent, while preserving strong transferability across different embedding models.  A case study on a financial agent further illustrates the real-world impact.  Finally, we discuss mitigation strategies, highlighting a persistent trade-off between cache efficiency and robustness.
