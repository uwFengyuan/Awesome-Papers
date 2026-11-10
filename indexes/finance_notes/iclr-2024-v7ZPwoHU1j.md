# Statistically Optimal $K$-means Clustering via Nonnegative Low-rank Semidefinite Programming

ICLR 2024 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：constraints, a basic but fundamental difficulty is the need to store and optimize over the n2 individual elements of the matrix. Even a small dataset with n ≈ 1000, such as the banknote authentication 1 Published as a conference paper at ICLR 2024 Computational complexity & Statistical performance trade-off 10 2 CPU time [seconds] 10 0

[Paper](https://openreview.net/forum?id=v7ZPwoHU1j)

Classification / 分类：Fraud & AML / 欺诈检测与反洗钱 → Banknote Authentication / 钞票真伪识别 → General / 综合

## Abstract / 摘要

$K$-means clustering is a widely used machine learning method for identifying patterns in large datasets. Recently, semidefinite programming (SDP) relaxations have been proposed for solving the $K$-means optimization problem, which enjoy strong statistical optimality guarantees. However, the prohibitive cost of implementing an SDP solver renders these guarantees inaccessible to practical datasets. In contrast, nonnegative matrix factorization (NMF) is a simple clustering algorithm widely used by machine learning practitioners, but it lacks a solid statistical underpinning and theoretical guarantees. In this paper, we consider an NMF-like algorithm that solves a nonnegative low-rank restriction of the SDP-relaxed $K$-means formulation using a nonconvex Burer--Monteiro factorization approach. The resulting algorithm is as simple and scalable as state-of-the-art NMF algorithms while also enjoying the same strong statistical optimality guarantees as the SDP. In our experiments, we observe that our algorithm achieves significantly smaller mis-clustering errors compared to the existing state-of-the-art while maintaining scalability.
