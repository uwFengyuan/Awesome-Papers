# Decision Trees with Short Explainable Rules

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：n size, our algorithm is at least as good as CART for all datasets, and for 9 of them (bold-faced on columns 4 and 5) it improves the explavg by at least 25%. For the explwc the gain is also clear. For all datasets, but Banknote, our algorithm is at least as good as CART. Moreover, for 3 of them (bold-faced on columns 6 and 7), it provides a gain of at least 25%. Boxplots for the experiments in Table 1 are provided in Section E.5 of the appendix. In Appendix E we compare CART and SER-DT in terms of depthavg and depthwc . For depthavg , SER-DT performs better than CART whi

[Paper](https://openreview.net/forum?id=Lp-QFq2QRXA)

Classification / 分类：Fraud & AML / 欺诈检测与反洗钱 → Banknote Authentication / 钞票真伪识别 → General / 综合

## Abstract / 摘要

Decision trees are widely used in many settings where interpretable models are preferred or required. As confirmed by recent empirical studies,  the interpretability/explanability of a decision tree critically depends on some of its structural parameters, like size and the  average/maximum depth of its leaves. There is indeed a vast literature on the design and analysis of decision tree algorithms that aim at optimizing these parameters.This paper contributes to this important line of research: we propose as a novel criterion of measuring the interpretability of a decision tree, the sparsity of the set of attributes that are (on average) required to explain the classification of the examples. We give a tight characterization of the best possible guarantees achievable by a decision tree built to optimize both our newmeasure (which we call the {\em explanation size})  and the more classical measures of worst-case and average depth. In particular, we give an algorithm that guarantees $O(\ln n )$-approximation (hence optimal if $P \neq NP$) for the minimization of both the average/worst-case explanation size and the average/worst-case depth. In addition to our theoretical contributions, experiments with 20 real datasets show that our algorithm has accuracy competitive with CART while producing trees that allow for much simpler explanations.
