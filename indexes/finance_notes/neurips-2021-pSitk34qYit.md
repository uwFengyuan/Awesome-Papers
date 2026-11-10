# Risk Bounds and Calibration for a Smart Predict-then-Optimize Method

NeurIPS 2021 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We perform experiments to empirically demonstrate the strength of the SPO+ surrogate, as compared to standard $\ell_1$ and squared $\ell_2$ prediction error losses, on portfolio allocation and cost-sensitive multi-class classification problems.

[Paper](https://openreview.net/forum?id=pSitk34qYit)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

The predict-then-optimize framework is fundamental in practical stochastic decision-making problems:  first predict unknown parameters of an optimization model, then solve the problem using the predicted values. A natural loss function in this setting is defined by measuring the decision error induced by the predicted parameters, which was named the Smart Predict-then-Optimize (SPO) loss by Elmachtoub and Grigas [2021]. Since the SPO loss is typically nonconvex and possibly discontinuous, Elmachtoub and Grigas [2021] introduced a convex surrogate, called the SPO+ loss, that importantly accounts for the underlying structure of the optimization model. In this paper, we greatly expand upon the consistency results for the SPO+ loss provided by Elmachtoub and Grigas [2021]. We develop risk bounds and uniform calibration results for the SPO+ loss relative to the SPO loss, which provide a quantitative way to transfer the excess surrogate risk to excess true risk. By combining our risk bounds with generalization bounds, we show that the empirical minimizer of the SPO+ loss achieves low excess true risk with high probability. We first demonstrate these results in the case when the feasible region of the underlying optimization problem is a polyhedron, and then we show that the results can be strengthened substantially when the feasible region is a level set of a strongly convex function. We perform experiments to empirically demonstrate the strength of the SPO+ surrogate, as compared to standard $\ell_1$ and squared $\ell_2$ prediction error losses, on portfolio allocation and cost-sensitive multi-class classification problems.
