# Design Linear Constrained Neural Layers with Implicit Convex Optimization

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Experiments on linear programming, as well as two real-world problems: partial graph matching and portfolio allocation which involve other discrete constraints.

[Paper](https://openreview.net/forum?id=LHCQSx0cQV)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

One essential limitation of neural networks is how to enforce (hard) constraints on prediction. We propose a plug-in, differentiable layer, which involves a fast implicit (convex) optimization procedure to enforce the general linear constraint. It aims to minimize a divergence between unconstrained and constrained outputs. Connecting to and beyond existing handcrafted layers, we show that our layer degrades to classic layers like Softmax, Sinkhorn and tanh etc. when the corresponding constraint is enforced by KL-divergence minimization. We further show that by replacing the KL-div with a Euclidean distance, a closed-form solution can be derived for highly-efficient constraint enforcing. We evaluate the above two variants of layers, termed as BLCLayer and GLCLayer, with their corresponding neural solver BLCNet and GLCNet with simple MLP/GNN-like backbone. Experiments on linear programming, as well as two real-world problems: partial graph matching and portfolio allocation which involve other discrete constraints.
