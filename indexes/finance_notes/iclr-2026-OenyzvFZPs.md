# Adaptive Mamba Neural Operators

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：In several challenging benchmark PDE problems in the fields of fluid physics, solid physics, and finance on point clouds, structured meshes, regular grids, and irregular domains, AMO consistently outperforms state-of-the-art solvers in terms of relative $L^2$ error.

[Paper](https://openreview.net/forum?id=OenyzvFZPs)

Classification / 分类：Financial Models & Benchmarks / 金融模型与评测资源 → Numerical Finance / 计算金融与数值方法 → General / 综合

## Abstract / 摘要

Accurately solving partial differential equations (PDEs) on arbitrary geometries and a variety of meshes is an important task in science and engineering applications. In this paper, we propose Adaptive Mamba Neural Operators (AMO), which integrates reproducing kernels for state-space models (SSMs) rather than the kernel integral formulation of SSMs. This is achieved by constructing Takenaka-Malmquist systems for the PDEs. AMO offers new representations that align well with the adaptive Fourier decomposition (AFD) theory and can approximate the solution manifold of PDEs on a wide range of geometries and meshes. In several challenging benchmark PDE problems in the fields of fluid physics, solid physics, and finance on point clouds, structured meshes, regular grids, and irregular domains, AMO consistently outperforms state-of-the-art solvers in terms of relative $L^2$ error. Overall, this work presents a new paradigm for designing explainable neural operator frameworks. The code is available at https://github.com/checlams/AMO.
