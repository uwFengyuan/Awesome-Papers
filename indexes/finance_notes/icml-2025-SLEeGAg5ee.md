# DANCE: Dual Unbiased Expansion with Group-acquired Alignment for Out-of-distribution Graph Fairness Learning

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：approaches, including MLP (Pal & Mitra, as follows: 1) Credit-Cs is derived from the Credit dataset 1992), GCN (Kipf & Welling, 2016). (B) Fair GNNs: GNNs (Yeh & Lien, 2009), where nodes represent credit card users. designed to improve fairness, including FairVGNN (Wang The task involves classifying users’ credit risk as either high et al., 2022), NIFTY (Agarwal et al., 2021), EDITS (Dong or low, with “age” designated as the sensitive attribute. To et al., 2022), CAF (Guo et al., 2023). (C) Ou

[Paper](https://openreview.net/forum?id=SLEeGAg5ee)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Graph neural networks (GNNs) have shown strong performance in graph fairness learning, which aims to ensure that predictions are unbiased with respect to sensitive attributes. However, existing approaches usually assume that training and test data share the same distribution, which rarely holds in the real world. To tackle this challenge, we propose a novel approach named Dual Unbiased Expansion with Group-acquired Alignment (DANCE) for graph fairness learning under distribution shifts. The core idea of our DANCE is to synthesize challenging yet unbiased virtual graph data in both graph and hidden spaces, simulating distribution shifts from a data-centric view. Specifically, we introduce the unbiased Mixup in the hidden space, prioritizing minor groups to address the potential imbalance of sensitive attributes. Simultaneously, we conduct fairness-aware adversarial learning in the graph space to focus on challenging samples and improve model robustness. To further bridge the domain gap, we propose a group-acquired alignment objective that prioritizes negative pair groups with identical sensitive labels. Additionally, a representation disentanglement objective is adopted to decorrelate sensitive attributes and target representations for enhanced fairness. Extensive experiments demonstrate the superior effectiveness of the proposed DANCE.
