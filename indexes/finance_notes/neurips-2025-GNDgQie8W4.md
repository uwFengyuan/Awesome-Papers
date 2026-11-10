# ElliCE: Efficient and Provably Robust Algorithmic Recourse via the Rashomon Sets

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：her methods that produce robust counterfactuals. Please see Appendix B for additional details and results. Datasets. We consider nine datasets from high-stakes decision domains such as lending (Aus- tralian Credit [53], FICO [20], German Credit [27], Banknote [44]), healthcare (Parkinson’s [60], Diabetes [58]), and recidivism (COMPAS [2]), as well as benchmark datasets (Wine Quality [13], Extended Iris [3]). Please see Table 3 for detailed dataset descriptions and preprocessing notes. We used datasets with predominantly categorical features (FICO, Australian Credit, C

[Paper](https://openreview.net/forum?id=GNDgQie8W4)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Machine learning models now influence decisions that directly affect people’s lives, making it important to understand not only their predictions, but also how individuals could act to obtain better results. Algorithmic recourse provides actionable input modifications to achieve more favorable outcomes, typically relying on counterfactual explanations to suggest such changes. However, when the Rashomon set - the set of near-optimal models - is large, standard counterfactual explanations can become unreliable, as a recourse action valid for one model may fail under another. We introduce ElliCE, a novel framework for robust algorithmic recourse that optimizes counterfactuals over an ellipsoidal approximation of the Rashomon set. The resulting explanations are provably valid over this ellipsoid, with theoretical guarantees on uniqueness, stability, and alignment with key feature directions. Empirically, ElliCE generates counterfactuals that are not only more robust but also more flexible, adapting to user-specified features constraints  while being substantially faster than existing baselines. This provides a principled and practical solution for reliable recourse under model uncertainty, ensuring stable recommendations for users even as models evolve.
