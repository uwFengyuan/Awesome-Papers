# New Insight of Variance reduce in Zero-Order Hard-Thresholding: Mitigating Gradient Error and Expansivity Contradictions

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Finally, we illustrate the utility of our method on a portfolio optimization problem as well as black-box adversarial attacks.

[Paper](https://openreview.net/forum?id=fjf3YenThE)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

Hard-thresholding is an important type of algorithm in machine learning that is used to solve $\ell_0$ constrained optimization problems. However,  the true gradient of the objective function can be difficult to access in certain scenarios, which normally can be approximated by zeroth-order (ZO) methods. SZOHT algorithm is the only algorithm tackling $\ell_0$ sparsity constraints with zeroth-order gradients so far. Unfortunately,  SZOHT  has a notable limitation on the number of random directions due to the inherent conflict between the deviation of ZO gradients and the expansivity of the hard-thresholding operator. This paper approaches this problem by considering the role of variance and provides a new insight into variance reduction: mitigating the unique conflicts between ZO gradients and hard-thresholding.  Under this perspective, we propose a generalized variance reduced ZO hard-thresholding algorithm as well as the generalized convergence analysis under standard assumptions. The theoretical results demonstrate the new algorithm eliminates the restrictions on the number of random directions, leading to improved convergence rates and broader applicability compared with SZOHT.  Finally, we illustrate the utility of our method on a portfolio optimization problem as well as black-box adversarial attacks.
