# Distributional Equivalence in Linear Non-Gaussian Latent-Variable Cyclic Causal Models: Characterization and Learning

ICLR 2026 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：roperties, Sun Hung Kai Properties, Wharf Holdings), 3 on utilities (CLP Holdings, HK & China Gas, HK Electric), and 3 on commerce (Hutchison, Swire Pacific ’A’, Cathay Pacific Airways). All of them were constituents of Hang Seng Index (HSI), and they were almost the largest companies of the Hong Kong stock market at the time. By applying glvLiNG on this dataset, we recovered an equivalence class of causal graphs containing 2 latent variables. The presentation (see Appendix C.3) of this equivalence class is shown in Figure 8. Here is a summary: the class consists of 19,008

[Paper](https://openreview.net/forum?id=b8TlYh6PN6)

Classification / 分类：Financial QA & Reasoning / 金融问答与数值推理 → Knowledge & Conversational QA / 知识与对话问答 → General / 综合

## Abstract / 摘要

Causal discovery with latent variables is a fundamental task. Yet most existing methods rely on strong structural assumptions, such as enforcing specific indicator patterns for latents or restricting how they can interact with others. We argue that a core obstacle to a general, structural-assumption-free approach is the lack of an equivalence characterization: without knowing what can be identified, one generally cannot design methods for how to identify it. In this work, we aim to close this gap for linear non-Gaussian models. We establish the graphical criterion for when two graphs with arbitrary latent structure and cycles are distributionally equivalent, that is, they induce the same observed distribution set. Key to our approach is a new tool, edge rank constraints, which fills a missing piece in the toolbox for latent-variable causal discovery in even broader settings. We further provide a procedure to traverse the whole equivalence class and develop an algorithm to recover models from data up to such equivalence. To our knowledge, this is the first equivalence characterization with latent variables in any parametric setting without structural assumptions, and hence the first structural-assumption-free discovery method. Code and an interactive demo are available at https://equiv.cc.
