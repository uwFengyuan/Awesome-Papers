# Deep FlexQP: Accelerated Nonlinear Programming via Deep Unfolding

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Deep FlexQP outperforms state-of-the-art learned QP solvers on a suite of benchmarks including portfolio optimization, classification, and regression problems, and scales to dense QPs with over 10k variables and constraints via fine-tuning.

[Paper](https://openreview.net/forum?id=HL3TvE4Afm)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

We propose FlexQP, an always-feasible convex quadratic programming (QP) solver based on an $\ell_1$ elastic relaxation of the QP constraints. If the original constraints are feasible, FlexQP provably recovers the optimal solution. If the constraints are infeasible, FlexQP identifies a solution that minimizes the constraint violation while keeping the number of violated constraints sparse. Such infeasibilities arise naturally in sequential quadratic programming (SQP) subproblems due to the linearization of the constraints. We prove the convergence of FlexQP under mild coercivity assumptions, making it robust to both feasible and infeasible QPs. We then apply deep unfolding to learn LSTM-based, dimension-agnostic feedback policies for the algorithm parameters, yielding an accelerated Deep FlexQP. To preserve the exactness guarantees of the relaxation, we propose a normalized training loss that incorporates the Lagrange multipliers. We additionally design a log-scaled loss for PAC-Bayes generalization bounds that yields substantially tighter performance certificates, which we use to construct an accelerated SQP solver with guaranteed QP subproblem performance. Deep FlexQP outperforms state-of-the-art learned QP solvers on a suite of benchmarks including portfolio optimization, classification, and regression problems, and scales to dense QPs with over 10k variables and constraints via fine-tuning. When deployed within SQP, our approach solves nonlinear trajectory optimization problems 4-16x faster than SQP with OSQP while substantially improving success rates. On predictive safety filter problems, Deep FlexQP reduces safety violations by over 70\% and increases task completion by 43\% compared to existing methods.
