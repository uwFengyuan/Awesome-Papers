# MOTOR: A Time-to-Event Foundation Model For Structured Medical Records

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：to PhysioNet. (2) We prohibit medical decision making, diagnoses, and other non-research use cases of MOTOR in our DUA and can revoke model access for violations. (3) We do not release our MERATIVE models pretrained on insurance claims data, which may be easier for entities to obtain commercially vs. longitudinal EHR data. Reproducibility Statement The code necessary for reproducing the experiments in this paper can be found in the supplemental materials as a zip file. Our hyperparameter search grids can be found in Appendix A. To aid reproducibility we have performed evaluat

[Paper](https://openreview.net/forum?id=NialiwI2V6)

Classification / 分类：Insurance & Actuarial / 保险与精算 → Insurance & Claims / 承保与理赔 → General / 综合

## Abstract / 摘要

We present a self-supervised, time-to-event (TTE) foundation model called MOTOR (Many Outcome Time Oriented Representations) which is pretrained on timestamped sequences of events in electronic health records (EHR) and health insurance claims. TTE models are used for estimating the probability distribution of the time until a specific event occurs, which is an important task in medical settings. TTE models provide many advantages over classification using fixed time horizons, including naturally handling censored observations, but are challenging to train with limited labeled data. MOTOR addresses this challenge by pretraining on up to 55M patient records (9B clinical events). We evaluate MOTOR's transfer learning performance on 19 tasks, across 3 patient databases (a private EHR system, MIMIC-IV, and Merative claims data). Task-specific models adapted from MOTOR improve time-dependent C statistics by 4.6\% over state-of-the-art, improve label efficiency by up to 95\%, and are more robust to temporal distributional shifts. We further evaluate cross-site portability by adapting our MOTOR foundation model for six prediction tasks on the MIMIC-IV dataset, where it outperforms all baselines. MOTOR is the first foundation model for medical TTE predictions and we release a 143M parameter pretrained model for research use at https://huggingface.co/StanfordShahLab/motor-t-base.
