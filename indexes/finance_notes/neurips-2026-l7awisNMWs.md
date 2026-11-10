# B$^3$-PWL: GPU-Batched Branch-and-Bound for Piecewise-Linear Optimization with SOS2 Constraints

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ferences in solver behavior across families reflect coupling structure rather than curve shape. G.1 Portfolio Benchmark with Piecewise-Linear Transaction Costs Problem Formulation. We consider a portfolio optimization benchmark with separable PWL transaction-cost penalties. This problem models capital allocation across N assets under a global budget, sparse factor-risk limits, and sector exposure caps. The objective balances expected return against a per-asset transaction penalty. For each asset j ∈ {1, . . . , N }, let wj ≥ 0 denote the dollar holding and let zj denote the transaction- cost penalty associated with wj . The objective is N X N X min − µj wj + γ zj , (13) w,z j=1 j=1 where µj is the expected return of asset j, and γ > 0 controls the tra

[Paper](https://openreview.net/forum?id=l7awisNMWs)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

Piecewise-linear (PWL) optimization problems arise in many mixed-integer programming (MIP) optimization applications, including portfolio optimization, workforce scheduling, and resource allocation. But solving them to global optimality remains computationally expensive because branch-and-bound repeatedly solves LP relaxation subproblems. Existing solvers are largely CPU-centric, leaving the scalability of modern GPUs underutilized. Few prior GPU-accelerated branch-and-bound either targets neural network which is not suitable for general PWL optimization, or accelerates only auxiliary subroutines such as strong branching heuristics within CPU-centric MIP solvers. To bridge this gap, we propose $\textbf{\texttt{B$^{3}$-PWL}}$, a GPU-centric batched branch-and-bound framework for piecewise-linear optimization with Special Ordered Set of type 2 (SOS2) constraints. Our method solves batches of LP relaxation subproblems concurrently on the GPU using a first-order primal-dual solver, enabled by a specialized batched block-tiled sparse matrix kernel. To complement bound computation, we further introduce a unified feasibility search module that combines an SOS2 repair primal heuristic with a batched feasibility pump to rapidly obtain feasible incumbents and improve pruning efficiency. On a benchmark of 43 PWL-MIP instances, $\textbf{\texttt{B$^{3}$-PWL}}$ achieves a 9.25$\times$ geometric-mean speedup over NVIDIA cuOpt while reaching high-quality feasible incumbents on every tested instance, demonstrating the potential of first-order LP methods as the central engine of GPU-accelerated branch-and-bound.
