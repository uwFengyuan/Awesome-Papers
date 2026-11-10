# Mitigating Label Shift in Tabular In-Context Learning via Test-Time Posterior Adjustment

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：100 stratify True 42 1 1055 2 0 356 PizzaCutter3 38 1 1043 2 0 127 rmftsa sleepdata 3 1 1024 4 0 94 credit-g 21 14 1000 2 0 300 dummy 7 1 1000 2 0 273 xd6 10 10 973 2 0 322 tokyo1 45 3 959 2 0 346 tic-tac-toe 10 10 958 2 0 332 Tour-and-Travels-Customer-Churn-Prediction 7 5 954 2 60 224 stock 10 1 950 2 0 462 vehicle 19 1 846 4 0 199 vehicle reproduced 19 1 846 4 0 199 analcatdata authorship 71 1 841 4 0 55 analcatdata dmft 5 5 797 6 0 123 diabetes 9 1 768 2 0 268 blood-transfusion-service-center 5 1 748 2 0 178 blood-transfusion-service-center seed 0 nrows 2000 nclasses 10 ncols 100 stratify True 5 1 748 2 0 178 doa bwin balanced 14 3 708 2 0 354 PieChart1 38 1 705 2 0 61 breast-w 10 1 699 2 16 241 credit-approval 16 10 6

[Paper](https://openreview.net/forum?id=8N2kUoknvy)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

TabPFN has recently gained attention as a foundation model for tabular datasets, achieving strong performance by leveraging in-context learning on synthetic data. However, we find that TabPFN is vulnerable to label shift, often overfitting to the majority class in the training dataset. To address this limitation, we propose DistPFN, the first test-time posterior adjustment method designed for tabular foundation models. DistPFN rescales predicted class probabilities by downweighting the influence of the training prior (i.e., the class distribution of the context) and emphasizing the contribution of the model’s predicted posterior, without architectural modification or additional training. We further introduce DistPFN-T, which incorporates temperature scaling to adaptively control the adjustment strength based on the discrepancy between prior and posterior. We evaluate our methods on over 250 OpenML datasets, demonstrating substantial improvements for various TabPFN-based models in classification tasks under label shift, while maintaining strong performance in standard settings without label shift. Code is available at this repository: https://github.com/seunghan96/DistPFN.
