# A2ASecBench: A Protocol-Aware Security Benchmark for Agent-to-Agent Multi-Agent Systems

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We empirically validate our framework using official A2A Project demos across three representative high-stakes domains (travel, healthcare, and finance), demonstrating that the identified attacks are both pervasive and highly effective, consistently bypassing default safeguards.

[Paper](https://openreview.net/forum?id=LfdFnakqGJ)

Classification / 分类：Financial Safety & Compliance / 金融安全与合规 → Financial Privacy & Security / 金融隐私与信息安全 → General / 综合

## Abstract / 摘要

Multi-agent systems (MAS) built on large language models (LLMs) increasingly rely on agent-to-agent (A2A) protocols to enable capability discovery, task orchestration, and artifact exchange across heterogeneous stacks. While these protocols promise interoperability, they also introduce new vulnerabilities. In this paper, we present the first comprehensive security evaluation of A2A-MAS. We develop a taxonomy and threat model that categorize risks into supply-chain manipulations and protocol-logic weaknesses, and we detail six concrete attacks spanning all A2A stages and components with impacts on confidentiality, integrity, and availability. Building on this taxonomy, we introduce A2ASecBench, the first A2A-specific security benchmark framework capable of probing diverse and previously unexplored attack vectors. Our framework incorporates a dynamic adapter layer for deployment across heterogeneous agent stacks and downstream workloads, alongside a joint safety–utility evaluation methodology that explicitly measures the trade-off between harmlessness and helpfulness by pairing adversarial trials with benign tasks. We empirically validate our framework using official A2A Project demos across three representative high-stakes domains (travel, healthcare, and finance), demonstrating that the identified attacks are both pervasive and highly effective, consistently bypassing default safeguards. These findings highlight the urgent need for protocol-level defenses and standardized benchmarking to secure the next generation of agentic ecosystems.
