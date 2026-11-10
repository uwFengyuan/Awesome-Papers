# DynFrs: An Efficient Framework for Machine Unlearning in Random Forest

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：±.000 .7911±.001 .7934±.002 Adult .8628±.001 .8428±.001 .8637±.000 .8503±.000 .8633±.001 .8650±.001 Bank .9420±.000 .9350±.000 .9414±.001 .9436±.000 .9417±.000 .9436±.000 Heart .7344±.001 .7195±.001 .7342±.001 .7301±.000 .7358±.002 .7366±.000 Diabetes .6443±.001 .6190±.000 .6435±.001 .6462±.000 .6453±.001 .6470±.002 NoShow .7361±.001 .7170±.000 .7387±.000 .7269±.000 .7335±.001 .7356±.000 Synthetic .9451±.000 / .9441±.000 .9309±.000 .9424±.000 .9454±.000 Higgs .7441±.000 / .7434±.000 .7255±.000 .7431±.000 .7475±.000 Effect of q on Predictive Accuracy Unlearning v.s. Retraining .866 .86 Accuracy Accuracy .863 .84 Adult .860 .82 Unlearned DYNFRS .857 Adult .80 Retrained DYNFRS .854 .648 .65 .64 Accuracy Accuracy .645 .642 .

[Paper](https://openreview.net/forum?id=nsCOeCLR8e)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Banking Data Applications / 银行业务数据应用 → General / 综合

## Abstract / 摘要

Random Forests are widely recognized for establishing efficacy in classification and regression tasks, standing out in various domains such as medical diagnosis, finance, and personalized recommendations. These domains, however, are inherently sensitive to privacy concerns, as personal and confidential data are involved. With increasing demand for the right to be forgotten, particularly under regulations such as GDPR and CCPA, the ability to perform machine unlearning has become crucial for Random Forests. However, insufficient attention was paid to this topic, and existing approaches face difficulties in being applied to real-world scenarios. Addressing this gap, we propose the DynFrs framework designed to enable efficient machine unlearning in Random Forests while preserving predictive accuracy. Dynfrs leverages subsampling method Occ(q) and a lazy tag strategy Lzy, and is still adaptable to any Random Forest variant. In essence, Occ(q) ensures that each sample in the training set occurs only in a proportion of trees so that the impact of deleting samples is limited, and Lzy delays the reconstruction of a tree node until necessary, thereby avoiding unnecessary modifications on tree structures. In experiments, applying Dynfrs on Extremely Randomized Trees yields substantial improvements, achieving orders of magnitude faster unlearning performance and better predictive accuracy than existing machine unlearning methods for Random Forests.
