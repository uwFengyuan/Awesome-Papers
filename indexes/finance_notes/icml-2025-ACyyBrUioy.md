# Near-Optimal Decision Trees in a SPLIT Second

ICML 2025 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：930 takes merely a second in most cases. This is the regime Netherlands 4255 216 0.932 most relevant to our algorithms. HELOC 5564 337 0.979 • When the optimal objective is high and the tree is super- HIV 9273 388 0.959 sparse (right side of each plot), SPLIT and Lickety- Bike 14330 194 0.999 SPLIT have small overhead costs and can be slower, Table 1. Table summarizing the advantages of RESPLIT. The because we need to train a greedy tree for each sub- first 2 columns show the time taken to compute all bootstrapped problem encountered at the loo

[Paper](https://openreview.net/forum?id=ACyyBrUioy)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Decision tree optimization is fundamental to interpretable machine learning. The most popular approach is to greedily search for the best feature at every decision point, which is fast but provably suboptimal. Recent approaches find the global optimum using branch and bound with dynamic programming, showing substantial improvements in accuracy and sparsity at great cost to scalability. An ideal solution would have the accuracy of an optimal method and the scalability of a greedy method. We introduce a family of algorithms called SPLIT (SParse Lookahead for Interpretable Trees) that moves us significantly forward in achieving this ideal balance. We demonstrate that not all sub-problems need to be solved to optimality to find high quality trees; greediness suffices near the leaves. Since each depth adds an exponential number of possible trees, this change makes our algorithms orders of magnitude faster than existing optimal methods, with negligible loss in performance. We extend this algorithm to allow scalable computation of sets of near-optimal trees (i.e., the Rashomon set).
