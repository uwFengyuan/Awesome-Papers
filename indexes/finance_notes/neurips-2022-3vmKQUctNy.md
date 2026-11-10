# Washing The Unwashable : On The (Im)possibility of Fairwashing Detection

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：on trees as interpretable models with respect to black-box Deep Neural Networks, AdaBoost [24], Gradient Boosted Decision Trees [17] and Random Forests [13] on three benchmark datasets: COMPAS [5], Adult Income [22] and Bank Marketing [34]. We evaluate the strength of our detector in the presence of an informed adversary representing an informed dishonest entity with knowledge of FRAUD-Detect that seeks to fairwash and bypass detection by constraining the divergence over subpopulation-wise confusion matrices. Our empirical experiments quantify the capacity of this informed adve

[Paper](https://openreview.net/forum?id=3vmKQUctNy)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Bank Marketing & Churn / 银行营销与客户流失 → General / 综合

## Abstract / 摘要

The use of black-box models (e.g., deep neural networks) in high-stakes decision-making systems, whose internal logic is complex, raises the need for providing explanations about their decisions. Model explanation techniques mitigate this problem by generating an interpretable and high-fidelity surrogate model (e.g., a logistic regressor or decision tree) to explain the logic of black-box models. In this work, we investigate the issue of fairwashing, in which model explanation techniques are manipulated to rationalize decisions taken by an unfair black-box model using deceptive surrogate models. More precisely, we theoretically characterize and analyze fairwashing, proving that this phenomenon is difficult to avoid due to an irreducible factor---the unfairness of the black-box model. Based on the theory developed, we propose a novel technique, called FRAUD-Detect (FaiRness AUDit Detection), to detect fairwashed models by measuring a divergence over subpopulation-wise fidelity measures of the interpretable model. We empirically demonstrate that this divergence is significantly larger in purposefully fairwashed interpretable models than in honest ones. Furthermore, we show that our detector is robust to an informed adversary trying to bypass our detector. The code implementing FRAUD-Detect is available at https://github.com/cleverhans-lab/FRAUD-Detect.
