# Cost Efficient Fairness Audit Under Partial Feedback

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We study the problem of auditing the fairness of a given classifier under partial feedback, where true labels are available only for positively classified individuals (e.g., loan repayment outcomes are observed only for approved applicants). / We introduce a novel cost model for acquiring additional labeled data, designed to more accurately reflect real-world costs such as credit assessment, loan processing, and potential defaults.

[Paper](https://openreview.net/forum?id=M86rt803hI)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

We study the problem of auditing the fairness of a given classifier under partial feedback, where true labels are available only for positively classified individuals (e.g., loan repayment outcomes are observed only for approved applicants). We introduce a novel cost model for acquiring additional labeled data, designed to more accurately reflect real-world costs such as credit assessment, loan processing, and potential defaults. Our goal is to find optimal fairness audit algorithms that are more cost-effective than random exploration and natural baselines.  In our work, we consider two audit settings: a black-box model with no assumptions on the data distribution, and a mixture model, where features and true labels follow a mixture of exponential family distributions. In the black-box setting, we propose a near-optimal auditing algorithm and show that a natural baseline can be strictly suboptimal. In the mixture model case, we design a novel algorithm that achieves significantly lower audit cost than the black-box case under mild assumptions. Our approach develops novel connections between partial feedback and learning from truncated samples. We also extend known results on maximum-a-posteriori oracles for spherical Gaussian mixtures to handle exponential family mixtures, which may be of independent interest. Moreover, our algorithms apply to popular fairness metrics including demographic parity, equal opportunity, and equalized odds. Empirically, we demonstrate strong performance of our algorithms on real-world fair classification datasets like Adult Income and Law School, consistently outperforming natural baselines by around 50% in terms of audit cost.
