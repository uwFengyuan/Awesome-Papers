# TANGOS: Regularizing Tabular Neural Networks through Gradient Orthogonalization and Specialization

ICLR 2023 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ion 9 699 Street et al. (1993) Cervical (CE) “00383” Classification 136 858 Fernandes et al. (2017) Credit (CR) “credit-screening” Classification 40 677 Dua et al. (2017) HCV (HC) “00571” Classification 12 615 Hoffmann et al. (2018) Australian (AU) “statlog” Classification 55 690 Quinlan (1987) Tumor (TU) “primary-tumor” Classification 25 339 Michalski et al. (1986) Entrance (EN) “00582” Classification 38 666 Hussain et al. (2018) Thoracic (TH) “00277” Classification 24 470 Zikeba et al. (2013) Soybean (SO) “soybean” Classification 484 683 Fisher & Schlimmer (1988) [1] This dataset has now been removed due to ethical issues. For more information see the following url https://medium.com/@docintangible/racist-data-destructi

[Paper](https://openreview.net/forum?id=n6H86gW8u0d)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Despite their success with unstructured data, deep neural networks are not yet a panacea for structured tabular data. In the tabular domain, their efficiency crucially relies on various forms of regularization to prevent overfitting and provide strong generalization performance. Existing regularization techniques include broad modelling decisions such as choice of architecture, loss functions, and optimization methods. In this work, we introduce Tabular Neural Gradient Orthogonalization and Specialization (TANGOS), a novel framework for regularization in the tabular setting built on latent unit attributions. The gradient attribution of an activation with respect to a given input feature suggests how the neuron attends to that feature, and is often employed to interpret the predictions of deep networks. In TANGOS, we take a different approach and incorporate neuron attributions directly into training to encourage orthogonalization and specialization of latent attributions in a fully-connected network. Our regularizer encourages neurons to focus on sparse, non-overlapping input features and results in a set of diverse and specialized latent units. In the tabular domain, we demonstrate that our approach can lead to improved out-of-sample generalization performance, outperforming other popular regularization methods. We provide insight into why our regularizer is effective and demonstrate that TANGOS can be applied jointly with existing methods to achieve even greater generalization performance.
