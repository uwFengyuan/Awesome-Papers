# UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：oken probability distri- and AgentHarm—covering a range of scenarios includ- bution—given the current instruction augmented with ing online shopping, financial tasks, and general agent an initialized adversarial string. manipulation. Our approach ooutperforms all existing (2) Identify Positions for Inserting Noise: We then auto- baselines, and successfully attack a real-world agent. matically pinpoint several optimal positions in the agent’s current reasoning where we can insert some 2. Related Work “noise” (e.g., the name of a target item or a malicious Adversarial Attacks on LLMs. Attacking language mod- tool). Here, the response serve

[Paper](https://openreview.net/forum?id=pRmxQHgjb1)

Classification / 分类：Financial Agents / 金融Agent与决策 → Investment & Financial Research Agents / 投研与金融决策Agent → General / 综合

## Abstract / 摘要

Large Language Model (LLM) agents equipped with external tools have become increasingly powerful for complex tasks such as web shopping, automated email replies, and financial trading. However, these advancements amplify the risks of adversarial attacks, especially when agents can access sensitive external functionalities. Nevertheless, manipulating LLM agents into performing targeted malicious actions or invoking specific tools remains challenging, as these agents extensively reason or plan before executing final actions. In this work, we present UDora, a unified red teaming framework designed for LLM agents that dynamically hijacks the agent's reasoning processes to compel malicious behavior. Specifically, UDora first generates the model’s reasoning trace for the given task, then automatically identifies optimal points within this trace to insert targeted perturbations. The resulting perturbed reasoning is then used as a surrogate response for optimization. By iteratively applying this process, the LLM agent will then be induced to undertake designated malicious actions or to invoke specific malicious tools. Our approach demonstrates superior effectiveness compared to existing methods across three LLM agent datasets. The code is available at https://github.com/AI-secure/UDora.
