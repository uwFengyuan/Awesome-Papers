# Partitioning Message Passing for Graph Fraud Detection

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：90.34±0.80 76.05±0.60 80.84±0.09 97.09±0.16 90.68±0.42 90.78±0.11 PMP 93.97±0.15 81.96±0.56 83.92±1.04 97.57±0.12 92.03±0.79 91.85±0.65 Table 2: Experiment Results on T-Finance and T-Social (40% training ratio). OOM: out of memory; OOT: out of time (running time > 1 day). T-Finance T-Social Method AUC F1-Macro G-Mean AUC F1-Macro G-Mean GCN 93.31±0.75 86.86±0.77

[Paper](https://openreview.net/forum?id=tEgrUrUuwA)

Classification / 分类：Fraud & AML / 欺诈检测与反洗钱 → Payment & Transaction Fraud / 支付与交易欺诈 → General / 综合

## Abstract / 摘要

Label imbalance and homophily-heterophily mixture are the fundamental problems encountered when applying Graph Neural Networks (GNNs) to Graph Fraud Detection (GFD) tasks. Existing GNN-based GFD models are designed to augment graph structure to accommodate the inductive bias of GNNs towards homophily, by excluding heterophilic neighbors during message passing. In our work, we argue that the key to applying GNNs for GFD is not to exclude but to {\em distinguish} neighbors with different labels. Grounded in this perspective, we introduce Partitioning Message Passing (PMP), an intuitive yet effective message passing paradigm expressly crafted for GFD. Specifically, in the neighbor aggregation stage of PMP, neighbors with different classes are aggregated with distinct node-specific aggregation functions. By this means, the center node can adaptively adjust the information aggregated from its heterophilic and homophilic neighbors, thus avoiding the model gradient being dominated by benign nodes which occupy the majority of the population. We theoretically establish a connection between the spatial formulation of PMP and spectral analysis to characterize that PMP operates an adaptive node-specific spectral graph filter, which demonstrates the capability of PMP to handle heterophily-homophily mixed graphs. Extensive experimental results show that PMP can significantly boost the performance on GFD tasks.
