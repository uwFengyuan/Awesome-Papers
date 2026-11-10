# Crowded in B-Space: Calibrating Shared Directions for LoRA Merging

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Across eight different benchmarks from math, coding, finance, and medical domains, Pico improves average accuracy by 3.4-8.3 points over the corresponding base method and achieves the best overall average performance.

[Paper](https://openreview.net/forum?id=PtEkosDXWk)

Classification / 分类：Financial QA & Reasoning / 金融问答与数值推理 → Numerical & Table Reasoning / 数值与表格推理 → General / 综合

## Abstract / 摘要

Merging separately trained LoRA adapters is a practical alternative to joint multi-task training, but it often hurts performance. Existing methods usually treat the LoRA update $\Delta W = BA$ as a single object and do not distinguish the two LoRA matrices. We show that the main source of LoRA merge interference comes from the output-side matrix $B$. Across tasks, $B$ repeatedly uses a small set of shared directions, while $A$ remains much more task-specific. As a result, the merged adapter overemphasizes these shared directions, and task-specific information is lost. We propose Pico (Pre-merge interference calibration in output-space), a data-free method that calibrates $B$ before merge by downscaling over-shared directions and then rescaling the merged update. Pico plugs directly into existing merging methods such as Task Arithmetic, TIES, and TSV-M. Across eight different benchmarks from math, coding, finance, and medical domains, Pico improves average accuracy by 3.4-8.3 points over the corresponding base method and achieves the best overall average performance. Pico also enables merged adapters to outperform the LoRA trained with all task data. These results show that LoRA merging works better when the two LoRA matrices are treated separately.
