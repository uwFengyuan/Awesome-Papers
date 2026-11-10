# Consistent Counterfactuals for Deep Models

ICLR 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：the generating model (Section 4). Finally, we empirically demonstrate that SNS generates consistent counterfactuals while maintaining a low cost relative to other methods over several tabular datasets, e.g. Seizure and German Credit from UCI database (Dua & Karra Taniskidou, 2017), in Section 5. In summary, our main contributions are: 1) we demonstrate that common counterfactual explanations can have low consistency across nearby deep models, and that cost is an insufficient signal to find consistent counterfactuals (Theorem. 1); 2) to navigate this cost-consistency tradeoff,

[Paper](https://openreview.net/forum?id=St6eyiTEHnG)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Counterfactual examples are one of the most commonly-cited methods for explaining the predictions of machine learning models in key areas such as finance and medical diagnosis. Counterfactuals are often discussed under the assumption that the model on which they will be used is static, but in deployment models may be periodically retrained or fine-tuned. This paper studies the consistency of model prediction on counterfactual examples in deep networks under small changes to initial training conditions, such as weight initialization and leave-one-out variations in data, as often occurs during model deployment. We demonstrate experimentally that counterfactual examples for deep models are often inconsistent across such small changes, and that increasing the cost of the counterfactual, a stability-enhancing mitigation suggested by prior work in the context of simpler models, is not a reliable heuristic in deep networks. Rather, our analysis shows that a model's Lipschitz continuity around the counterfactual, along with confidence of its prediction, is key to its consistency across related models. To this end, we propose Stable Neighbor Search as a way to generate more consistent counterfactual explanations, and illustrate the effectiveness of this approach on several benchmark datasets.
