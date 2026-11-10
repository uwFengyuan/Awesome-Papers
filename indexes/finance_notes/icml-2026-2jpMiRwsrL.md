# A Penalty Approach For Differentiation Through Black-box Quadratic Programming Solvers

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We evaluate dXPP on various tasks, including randomly generated QPs, large-scale sparse projection problems, and a real-world multi-period portfolio optimization task.

[Paper](https://openreview.net/forum?id=2jpMiRwsrL)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

Differentiating through the solution of a quadratic program (QP) is a central problem in differentiable optimization. Most existing approaches differentiate through the Karush--Kuhn--Tucker (KKT) system, but their computational cost and numerical robustness can degrade at scale. To address these limitations, we propose dXPP, a penalty-based differentiation framework that decouples QP solving from differentiation. In the solving step (forward pass), dXPP is solver-agnostic and can leverage any black-box QP solver. In the differentiation step (backward pass), we map the solution to a smooth approximate penalty problem and implicitly differentiate through it, requiring only the solution of a much smaller linear system in the primal variables. This approach bypasses the difficulties inherent in explicit KKT differentiation and significantly improves computational efficiency and robustness. We evaluate dXPP on various tasks, including randomly generated QPs, large-scale sparse projection problems, and a real-world multi-period portfolio optimization task. Empirical results demonstrate that dXPP is competitive with KKT-based differentiation methods and achieves substantial speedups on large-scale problems. Our implementation is open source and available at https://github.com/mmmmmmlinghu/dXPP.
