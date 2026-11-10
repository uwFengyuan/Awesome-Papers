# Private Rate-Constrained Optimization with Applications to Fair Learning

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：trong privacy guarantees; (iii) scales to a large number of constraints, and (iv) is computationally efficient. Setup. We evaluate RaCO-DP on three constraint types: demographic parity (on Adult (Becker & Kohavi, 1996), Credit-Card (Yeh, 2009), Parkinsons Little (2007), ACSEmployment (Ding et al., 2021), CelebA (Liu et al., 2015)), false negative rate (on Adult, Heart Alex Teboul), and equalized odds (on Credit-Card). We benchmark against DP-FERMI (Lowy et al., 2023), Tran et al. (2021), and Jagielski et al. (2019), reporting their results from Lowy et al. (2023) where avail

[Paper](https://openreview.net/forum?id=mex3rvs2KX)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

Many problems in trustworthy ML can be expressed as constraints on prediction rates across subpopulations, including group fairness constraints (demographic parity, equalized odds, etc.). In this work, we study such constrained minimization problems under differential privacy (DP). Standard DP optimization techniques like DP-SGD rely on objectives that decompose over individual examples, enabling per-example gradient clipping and noise addition. Rate constraints, however, depend on aggregate statistics across groups, creating inter-sample dependencies that violate this decomposability. To address this, we develop RaCO-DP, a DP variant of Stochastic Gradient Descent-Ascent (SGDA) that solves the Lagrangian formulation of rate constraint problems. We show that the additional privacy cost of incorporating these constraints reduces to privately estimating a histogram over the mini-batch at each step. We prove convergence of our algorithm through a novel analysis of SGDA that leverages the linear structure of the dual parameter. Empirical results show that our method Pareto-dominates existing private learning approaches under group fairness constraints and also achieves strong privacy–utility–fairness performance on neural networks.
