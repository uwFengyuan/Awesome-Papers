# Partially Performative Prediction

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：rticular the processed version from [29]. The dataset contains demographic and socioeconomic features xi ∈ R16 , including age, education, and credit history, and labels yi indicating whether a person defaulted on their credit card payment, for 30, 000 individuals. The learner aims to predict the individuals’ creditworthiness by minimizing a regularized logistic loss over an ℓ2 ball in d = 17 dimensions (one dimension corresponding to the intercept), after standardizing the features. The performative feedback is modeled as coming from strategic responses: an individual i res

[Paper](https://openreview.net/forum?id=OJ3tHPcSRq)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Financial Risk / 金融风险管理 → General / 综合

## Abstract / 摘要

Performative prediction studies feedback loops that arise when predictive models are deployed in consequential domains. In these settings, model updates can shape the population whose patterns they aim to predict, inducing a distribution shift that is *endogenous* to the learning system. This perspective departs from classical treatments of distribution shift, where shifts are typically modeled as *exogenous* changes in the data-generating process. Yet, in practice, distribution shift is rarely one or the other. Predictive models may influence future data through the decisions they support, while the world itself continues to drift for reasons beyond the learner’s control. We study *partially performative prediction*, a framework that captures both endogenous and exogenous sources of distribution shift. The framework generalizes performative prediction by allowing the data distribution to evolve both in response to the deployed model and according to an external, time-varying process. We extend the central notions of performative stability and performative optimality to this setting by defining online analogues that measure performance relative to the evolving partially performative environment. We analyze practical learning heuristics, including repeated retraining, and characterize when they successfully adapt to partially performative environments.
