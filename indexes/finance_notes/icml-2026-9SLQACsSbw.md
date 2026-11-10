# Differentiable Optimization Layers for Guaranteed Fairness in Deep Learning

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：in all other directions are unaffected. This ensures that backpropagation never encourages the 5.2. Loan Default Prediction model to move in directions that would violate active fair- This first experimental setting concerns loan default pre- ness constraints, while allowing learning to proceed freely dictions for small businesses. Note for any given random in all feasible directions. train, validation, and test split, the dataset sizes are relatively small. Therefore, we repeat the entire experiment (includ- 5. Numerical Experiments ing λ selection for penalty models) 25 times, each with a new, random dataset split to reduce the impact of any given We conduct numerical experiments across four distinct random data split on t

[Paper](https://openreview.net/forum?id=9SLQACsSbw)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Differentiable optimization layers are traditionally integrated in predict-then-optimize frameworks where a neural model estimates parameters that subsequently serve as fixed inputs to downstream decision-making optimization problems. In this work, we introduce the concept of a "fairness layer": a differentiable optimization layer appended to a model's output layer that guarantees a chosen notion of output parity is satisfied when integrated into a neural network. Additionally, we introduce an online primal-dual inference algorithm that provides provable aggregate fairness guarantees for streaming predictions with arbitrarily small batch sizes, where traditional per-batch constraints become overly restrictive. Numerical experiments demonstrate the effectiveness of the fairness layer and associated algorithm, and theoretical analysis characterizes the layer's differentiability and stability properties during model training and backpropagation. Our code for these experiments is publicly available on GitHub: https://github.com/dtroxell19/FairDL-ICML-2026.git and our public Python package documentation can be found online: https://dtroxell19.github.io/fairness_training/.
