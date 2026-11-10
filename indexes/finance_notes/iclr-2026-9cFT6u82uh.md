# Analytica: Soft Propositional Reasoning for Robust and Scalable LLM-Driven Analysis

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Large language model (LLM) agents are increasingly tasked with complex real-world analysis (e.g., in financial forecasting, scientific discovery), yet their reasoning suffers from stochastic instability and lacks a verifiable, compositional structure. / Our theoretical and empirical results on economic, financial, and political forecasting tasks show that Analytica improves 15.84\% accuracy on average over diverse base models, achieving 71.06\% accuracy with the lowest variance of 6.02\% when working with a Deep Research grounder.

[Paper](https://openreview.net/forum?id=9cFT6u82uh)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → Stock Movement & Returns / 股价方向与收益预测 → General / 综合

## Abstract / 摘要

Large language model (LLM) agents are increasingly tasked with complex real-world analysis (e.g., in financial forecasting, scientific discovery), yet their reasoning suffers from stochastic instability and lacks a verifiable, compositional structure. To address this, we introduce **Analytica**, a novel agent architecture built on the principle of **Soft Propositional Reasoning (SPR)**. SPR reframes complex analysis as a structured process of estimating the soft truth values of different outcome propositions, allowing us to formally model and minimize the estimation error in terms of its bias and variance. Analytica operationalizes this through a parallel, divide-and-conquer framework that systematically reduces both sources of error. To reduce bias, problems are first decomposed into a tree of subpropositions, and tool-equipped LLM *grounder agents* are employed —including a novel Jupyter Notebook agent for data-driven analysis—that help to validate and score facts. To reduce variance, Analytica recursively synthesizes these grounded leaves using robust linear models that average out stochastic noise with superior efficiency, scalability, and enable interactive "what-if" scenario analysis. Our theoretical and empirical results on economic, financial, and political forecasting tasks show that Analytica improves 15.84\% accuracy on average over diverse base models, achieving 71.06\% accuracy with the lowest variance of 6.02\% when working with a Deep Research grounder. Our Jupyter Notebook grounder shows strong cost-effectiveness that achieves a close 70.11\% accuracy with 90.35\% less cost and 52.85\% less time. Analytica also exhibits highly noise-resilient and stable performance growth as the analysis depth increases, with a near-linear time complexity, as well as good adaptivity to open-weight LLMs and scientific domains.
