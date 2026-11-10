# Synthesising Counterfactual Explanations via Label-Conditional Gaussian Mixture Variational Autoencoders

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：S ETUP Datasets and classifiers. We run our experiments on datasets which are commonly used in prior work (Karimi et al., 2023) and are advocated in the CE benchmarking library, CARLA (Pawelczyk et al., 2021). They are heloc credit (FICO, 2018), wine quality (Cortez et al., 2009), adult income (Becker & Kohavi, 1996), and compas recidivism (Julia Angwin & Kirchner, 2016). We split each dataset into a train and a test set for training classifiers. To demonstrate the model-agnostic nature of our approach, we train a random forest and a neural network for each dataset, w

[Paper](https://openreview.net/forum?id=zd9R2T4HiX)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Counterfactual explanations (CEs) provide recourse recommendations for individuals affected by algorithmic decisions. A key challenge is generating CEs that are robust against various perturbation types (e.g. input and model perturbations) while simultaneously satisfying other desirable properties. These include plausibility, ensuring CEs reside on the data manifold, and diversity, providing multiple distinct recourse options for single inputs. Existing methods, however, mostly struggle to address these multifaceted requirements in a unified, model-agnostic manner. We address these limitations by proposing a novel generative framework. First, we introduce the Label-conditional Gaussian Mixture Variational Autoencoder (L-GMVAE), a model trained to learn a structured latent space where each class label is represented by a set of Gaussian components with diverse, prototypical centroids. Building on this, we present LAPACE (LAtent PAth Counterfactual Explanations), a model-agnostic algorithm that synthesises entire paths of CE points by interpolating from inputs' latent representations to those learned latent centroids. This approach inherently ensures robustness to input changes, as all paths for a given target class converge to the same fixed centroids. Furthermore, the generated paths provide a spectrum of recourse options, allowing users to navigate the trade-off between proximity and plausibility while also encouraging robustness against model changes. In addition, user-specified actionability constraints can also be easily incorporated via lightweight gradient optimisation through the L-GMVAE's decoder. Comprehensive experiments show that LAPACE is computationally efficient and achieves competitive performance across eight quantitative metrics.
