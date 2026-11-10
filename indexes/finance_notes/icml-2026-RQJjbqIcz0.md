# PlotCraft: Pushing the Limits of LLMs for Complex and Interactive Data Visualization

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：To address this gap, we introduce **PlotCraft**, a new benchmark featuring 1k challenging visualization tasks that cover a wide range of topics, such as finance, scientific research, and sociology.

[Paper](https://openreview.net/forum?id=RQJjbqIcz0)

Classification / 分类：Document AI / 票据、财报与图表理解 → Charts & Visual Understanding / 金融图表与视觉理解 → General / 综合

## Abstract / 摘要

Recent Large Language Models (LLMs) have demonstrated remarkable proficiency in code generation. However, their ability to create complex visualizations for scaled and structured data remains largely unevaluated and underdeveloped. To address this gap, we introduce **PlotCraft**, a new benchmark featuring 1k challenging visualization tasks that cover a wide range of topics, such as finance, scientific research, and sociology. The benchmark is structured around seven high-level visualization tasks and encompasses 48 distinct chart types. Crucially, it is the first to systematically evaluate both single-turn generation and multi-turn refinement across a diverse spectrum of task complexities. Our comprehensive evaluation of 23 leading LLMs on PlotCraft reveals obvious performance deficiencies in handling sophisticated visualization tasks. To bridge this performance gap, we develope **SynthVis-30K**, a large-scale, high-quality dataset of complex visualization code synthesized via a collaborative agent framework. Building upon this dataset, we develope **PlotCraftor**, a novel code generation model that achieves strong capabilities in complex data visualization with a remarkably small size. Across VisEval, PandasPlotBench, and our proposed PlotCraft, PlotCraftor shows performance comparable to that of leading proprietary approaches. Especially, on hard task, Our model achieves over 50\% performance improvement. We will release the benchmark, dataset, and code at \href{https://anonymous.4open.science/r/PlotCraft-E320}{PlotCraft anonymous repository}.
