# Statistical Guarantees in the Search for Less Discriminatory Algorithms

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Recent scholarship argues that this doctrine has direct implications for algorithmic decision-making in high-stakes domains such as employment, lending, and housing, potentially obligating firms to search for “less discriminatory algorithms” (Black et al., 2024). / We also show how stronger distributional assumptions over the model space can yield tighter bounds, and we validate the approach on real-world credit and housing datasets.

[Paper](https://openreview.net/forum?id=n8FKO0DIl8)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

U.S. discrimination law can impose liability on firms that fail to adopt a less discriminatory alternative (LDA), defined as a decision policy that achieves the same business objectives while reducing disparate impact on legally protected groups. Recent scholarship argues that this doctrine has direct implications for algorithmic decision-making in high-stakes domains such as employment, lending, and housing, potentially obligating firms to search for “less discriminatory algorithms” (Black et al., 2024). Regulators have at times encouraged proactive LDA searches, reinforcing the expectation of a good-faith effort to identify equally performant models with lower disparate impact. Model multiplicity makes such searches plausible: retraining with different random seeds can yield models with comparable predictive performance but materially different disparate impacts. Yet firms cannot retrain indefinitely, raising a central question: when is the search sufficient to demonstrate good faith? We formalize LDA search under multiplicity as an optimal stopping problem in which a developer seeks to produce evidence that further search is unlikely to yield meaningful improvements. Our main contribution is an adaptive stopping algorithm that provides a high-probability upper bound on the best disparate-impact gains attainable through continued retraining, enabling developers to certify (e.g., to a court) that additional search is unlikely to help. We also show how stronger distributional assumptions over the model space can yield tighter bounds, and we validate the approach on real-world credit and housing datasets.
