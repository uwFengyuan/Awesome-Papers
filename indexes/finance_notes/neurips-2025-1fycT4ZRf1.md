# Scalable Signature Kernel Computations via Local Neumann Series Expansions

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：As demonstrated in our benchmarks, these advantages make our method particularly well-suited for rough-path-assisted machine learning, financial modeling, and signal processing applications involving very long and highly volatile sequential data.

[Paper](https://openreview.net/forum?id=1fycT4ZRf1)

Classification / 分类：Time Series / 时间序列 → General Time-Series Methods / 综合序列方法 → General / 综合

## Abstract / 摘要

The signature kernel is a recent state-of-the-art tool for analyzing high-dimensional sequential data, valued for its theoretical guarantees and strong empirical performance. In this paper, we present a novel method for efficiently computing the signature kernel of long, high-dimensional time series via adaptively truncated recursive local power series expansions. Building on the characterization of the signature kernel as the solution of a Goursat PDE, our approach employs tilewise Neumann‐series expansions to derive rapidly converging power series approximations of the signature kernel that are locally defined on subdomains and propagated iteratively across the entire domain of the Goursat solution by exploiting the geometry of the time series. Algorithmically, this involves solving a system of interdependent Goursat PDEs via adaptively truncated local power series expansions and recursive propagation of boundary conditions along a directed graph in a topological ordering. This method strikes an effective balance between computational cost and accuracy, achieving substantial performance improvements over state-of-the-art approaches for computing the signature kernel. It offers (a) adjustable and superior accuracy, even for time series with very high roughness; (b) drastically reduced memory requirements; and (c) scalability to efficiently handle very long time series (e.g., with up to one million data points or more) on a single GPU. As demonstrated in our benchmarks, these advantages make our method particularly well-suited for rough-path-assisted machine learning, financial modeling, and signal processing applications involving very long and highly volatile sequential data.
