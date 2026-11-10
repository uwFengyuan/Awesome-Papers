# Maximum Entropy Flow Networks

ICLR 2017 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Simulation results demonstrate the effectiveness of our method, and applications to finance and computer vision show the flexibility and accuracy of using maximum entropy flow networks.

[Paper](https://openreview.net/forum?id=H1acq85gx)

Classification / 分类：Derivatives & Hedging / 衍生品定价与对冲 → Option Pricing & PDEs / 期权定价与PDE → General / 综合

## Abstract / 摘要

Maximum entropy modeling is a flexible and popular framework for formulating statistical models given partial knowledge. In this paper, rather than the traditional method of optimizing over the continuous density directly, we learn a smooth and invertible transformation that maps a simple distribution to the desired maximum entropy distribution. Doing so is nontrivial in that the objective being maximized (entropy) is a function of the density itself.  By exploiting recent developments in normalizing flow networks, we cast the maximum entropy problem into a finite-dimensional constrained optimization, and solve the problem by combining stochastic optimization with the augmented Lagrangian method. Simulation results demonstrate the effectiveness of our method, and applications to finance and computer vision show the flexibility and accuracy of using maximum entropy flow networks.
