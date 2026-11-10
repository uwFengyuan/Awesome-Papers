# TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second

ICLR 2023 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.8141 0.8323 0.8227 0.8311 0.8242 0.8322 0.8346 0.8321 pc1 0.8321 0.86 0.8489 0.8527 0.8578 0.877 0.8761 0.8739 banknote-authentic.. 1 1 1 1 1 1 1 1 blood-transfusion-.. 0.7144 0.7403 0.7312 0.7504 0.7364 0.753 0.7549 0.7469 ilpd 0.6917 0.7279 0.7171 0.7212 0.723 0.7412 0.7379 0.7326 qsar-biodeg 0.91

[Paper](https://openreview.net/forum?id=cp5PvcI6w8_)

Classification / 分类：Fraud & AML / 欺诈检测与反洗钱 → Banknote Authentication / 钞票真伪识别 → General / 综合

## Abstract / 摘要

We present TabPFN, a trained Transformer that can do supervised classification for small tabular datasets in less than a second, needs no hyperparameter tuning and is competitive with state-of-the-art classification methods.TabPFN is fully entailed in the weights of our network, which accepts training and test samples as a set-valued input and yields predictions for the entire test set in a single forward pass.TabPFN is a Prior-Data Fitted Network (PFN) and is trained offline once, to approximate Bayesian inference on synthetic datasets drawn from our prior.This prior incorporates ideas from causal reasoning: It entails a large space of structural causal models with a preference for simple structures.On the $18$ datasets in the OpenML-CC18 suite that contain up to 1000 training data points, up to 100 purely numerical features without missing values, and up to 10 classes, we show that our method clearly outperforms boosted trees and performs on par with complex state-of-the-art AutoML systems with up to $230\times$ speedup.This increases to a $5\,700\times$ speedup when using a GPU. We also validate these results on an additional 67 small numerical datasets from OpenML.We provide all our code, the trained TabPFN, an interactive browser demo and a Colab notebook at https://github.com/automl/TabPFN.
