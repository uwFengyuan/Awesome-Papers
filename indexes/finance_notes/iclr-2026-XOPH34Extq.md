# TabStruct: Measuring Structural Fidelity of Tabular Data

ICLR 2026 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：,132 3,430 Characters Images OpenML 1459 10,218 8 1277.25 7 1 10 600 1,416 Credit-g Economics OpenML 46378 1,000 21 47.62 7 14 2 300 700 Electricity Economics OpenML 151 45,312 9 5034.67 7 2 2 19,237 26,075 Higgs Physics OpenML 4532 98,050 29 3381.03

[Paper](https://openreview.net/forum?id=XOPH34Extq)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Evaluating tabular generators remains a challenging problem, as the unique causal structural prior of heterogeneous tabular data does not lend itself to intuitive human inspection. Recent work has introduced structural fidelity as a tabular-specific evaluation dimension to assess whether synthetic data complies with the causal structures of real data. However, existing benchmarks often neglect the interplay between structural fidelity and conventional evaluation dimensions, thus failing to provide a holistic understanding of model performance. Moreover, they are typically limited to toy datasets, as quantifying existing structural fidelity metrics requires access to ground-truth causal structures, which are rarely available for real-world datasets. In this paper, we propose a novel evaluation framework that jointly considers structural fidelity and conventional evaluation dimensions. We introduce a new evaluation metric, global utility, which enables the assessment of structural fidelity even in the absence of ground-truth causal structures. In addition, we present TabStruct, a comprehensive evaluation benchmark offering large-scale quantitative analysis on 13 tabular generators from nine distinct categories, across 29 datasets. Our results demonstrate that global utility provides a task-independent, domain-agnostic lens for tabular generator performance. We release the TabStruct benchmark suite, including all datasets, evaluation pipelines, and raw results. Code is available at https://github.com/SilenceX12138/TabStruct.
