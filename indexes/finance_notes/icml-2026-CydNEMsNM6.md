# Learning the ESG Geometry with Domain Aware Language Models

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Current ESG solutions cannot model high-dimensional, multi-modal time series capturing the joint evolution of ESG risks, financial returns, news, and sentiment, even though this domain requires jointly reasoning over distinct numerical signals where both numerical proximity and semantic type must be preserved. / Trained on ESG, returns, news, and sentiment, the domain-aware LLM learns a representation space that enables accurate ESG forecasting, trajectory-based grouping, and latent-space search for superior asset selection and downstream application like portfolio rebalancing

[Paper](https://openreview.net/forum?id=CydNEMsNM6)

Classification / 分类：ESG & Sustainable Finance / ESG与可持续金融 → ESG Disclosure & Greenwashing / ESG披露与漂绿 → General / 综合

## Abstract / 摘要

Responsible investing aims to generate positive impact across Environment (E), Society (S), and Governance (G), and rating companies along these dimensions is now widespread, making ESG scores highly popular. Allocating retail capital with sustainability in mind could be transformational, yet it remains unclear how individual investors can do so in practice. Current ESG solutions cannot model high-dimensional, multi-modal time series capturing the joint evolution of ESG risks, financial returns, news, and sentiment, even though this domain requires jointly reasoning over distinct numerical signals where both numerical proximity and semantic type must be preserved. To bridge this gap, we introduce a novel domain-aware $\textbf{representation learning framework}$ that learns geometry-preserving representations for heterogeneous time series using value-aware tokens with block-wise $\textbf{orthogonal embeddings}$. To capture trajectory-level structure, we introduce $\textbf{FACET}$ tokens and train the model using a geometry-preserving loss. The resulting model jointly learns to forecast future values and to organize entities in a representation space that reflects their temporal evolution. Trained on ESG, returns, news, and sentiment, the domain-aware LLM learns a representation space that enables accurate ESG forecasting, trajectory-based grouping, and latent-space search for superior asset selection and downstream application like portfolio rebalancing
