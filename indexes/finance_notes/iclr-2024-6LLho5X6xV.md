# UniTabE: A Universal Pretraining Protocol for Tabular Foundation  Model in Data Science

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.4 7.7 Investing 1 71K 1B 29.33 0.02 1.58 Time Series 1 65K 1B 6.47 0.02 2.27 Finance 1 52K 773M 37.57 0.04 1.46 Economics 1 47K 488M 40.34 0.01 1.27 Games 1 32K 430M 23.37 0.66 3.66 minimizing it between anchor and negative block. We adopt the overlap bet

[Paper](https://openreview.net/forum?id=6LLho5X6xV)

Classification / 分类：Time Series / 时间序列 → General Time-Series Methods / 综合序列方法 → Foundation models / 基础模型

## Abstract / 摘要

Recent advancements in Natural Language Processing (NLP) have witnessed the groundbreaking impact of pretrained models, yielding impressive outcomes across various tasks. This study seeks to extend the power of pretraining methodologies to facilitating the prediction over tables in data science, a domain traditionally overlooked, yet inherently challenging due to the plethora of table schemas intrinsic to different tasks. The primary research questions underpinning this work revolve around the establishment of a universal pretraining protocol for tables with varied structures, the generalizability and transferability of learned knowledge across tasks, the adaptation to diverse downstream applications, and the incorporation of incremental columns over time. In response to these challenges, we introduce UniTabE, a straightforward yet effective method designed to process tables in a uniform manner, devoid of constraints imposed by specific table structures. UniTabE's core concept relies on representing each basic table element with a module, termed TabUnit. This is subsequently followed by a Transformer encoder to refine the representation. Moreover, our model is designed to facilitate pretraining and finetuning through the utilization of free-form prompts. In order to implement the pretraining phase, we curated an expansive tabular dataset comprising approximately 13 billion samples, meticulously gathered from the Kaggle platform. This research primarily centers on classification and regression tasks involving tabular data, and conducts rigorous experimental testing and analyses to validate the effectiveness of our methodology. The experimental results demonstrate UniTabE's superior performance against several baseline models across a multitude of benchmark datasets. This, therefore, underscores UniTabE's potential to significantly enhance the semantic representation of tabular data, thereby marking a significant stride for tabular data analysis.
