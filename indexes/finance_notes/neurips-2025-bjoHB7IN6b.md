# Seeing is Believing? Mitigating OCR Hallucinations in Multimodal Large Language Models

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：This dataset includes test samples spanning identity cards, invoices, and prescriptions, with simulated real-world degradations and pixel-level annotations for OCR reliability.

[Paper](https://openreview.net/forum?id=bjoHB7IN6b)

Classification / 分类：Document AI / 票据、财报与图表理解 → Receipts, Invoices & OCR / 票据发票与OCR → General / 综合

## Abstract / 摘要

Recent advancements in multimodal large language models (MLLMs) have enhanced document understanding by integrating textual and visual information. However, existing models exhibit incompleteness within their paradigm in real-world scenarios, particularly under visual degradation (e.g., blur, occlusion, low contrast). In such conditions, the current response paradigm often fails to adequately perceive visual degradation and ambiguity, leading to overreliance on linguistic priors or misaligned visual-textual reasoning. This difficulty in recognizing uncertainty frequently results in the generation of hallucinatory content, especially when a precise answer is not feasible. To better demonstrate and analyze this phenomenon and problem, we propose KIE-HVQA, the first benchmark dedicated to evaluating OCR hallucination in degraded document understanding. This dataset includes test samples spanning identity cards, invoices, and prescriptions, with simulated real-world degradations and pixel-level annotations for OCR reliability. This setup allows for evaluating models' capacity, under degraded input, to distinguish reliable visual information and answer accordingly, thereby highlighting the challenge of avoiding hallucination on uncertain data. To achieve vision-faithful reasoning and thereby avoid the aforementioned issues, we further introduce a Group Relative Policy Optimization (GRPO)-based framework featuring a novel reward mechanism. By incorporating a self-awareness of visual uncertainty and an analysis method that initiates refusal to answer to increase task difficulty within our supervised fine-tuning and reinforcement learning framework, we successfully mitigated hallucinations in ambiguous regions. Experiments on Qwen2.5-VL demonstrate that our 7B-parameter model achieves a ~28% absolute improvement in hallucination-free accuracy over GPT-4o on KIE-HVQA and there is no significant performance drop in standard tasks, highlighting both effectiveness and robustness. This work advances the development of reliable MLLMs for real-world document analysis by addressing critical challenges in visual-linguistic alignment under degradation.
