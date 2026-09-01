---
type: model
name: Crossformer
category: Deep Learning / Cross-Dimension Dependency Transformer
tags:
  - model
  - deep-learning
  - transformer
  - multivariate-forecasting
---

# 🔀 Crossformer

## Overview
Crossformer (Zhang & Yan, ICLR 2023) is among the first Transformers to explicitly exploit **cross-dimension (cross-variate) dependency** for multivariate forecasting — critical when series are associated (e.g., temperature ↔ wind speed; correlated EV charging stations). Existing Transformers embed all dimensions at one time step into a single vector and model only cross-time dependency. Three components:

1. **Dimension-Segment-Wise (DSW) embedding**: each dimension partitioned into segments of length $L_{seg}$, embedded as a 2D vector array (time × dimension):
$$h_{i,d} = E x^{(s)}_{i,d} + E^{(pos)}_{i,d}, \quad E \in \mathbb{R}^{d_{model}\times L_{seg}}$$
2. **Two-Stage Attention (TSA)** layer — *cross-time* MSA within each dimension, then *cross-dimension* stage with a **router mechanism**: $c \ll D$ learnable routers aggregate from all dimensions then distribute back, reducing complexity from $O(D^2L)$ to $O(DL)$; overall TSA complexity $O(DL^2)$:
$$B_{i,:} = \text{MSA}^{dim}_1(R_{i,:}, Z^{time}_{i,:}, Z^{time}_{i,:}), \qquad Z^{dim}_{i,:} = \text{MSA}^{dim}_2(Z^{time}_{i,:}, B_{i,:}, B_{i,:})$$
3. **Hierarchical Encoder-Decoder (HED)**: segment merging every two adjacent time vectors per layer + TSA at coarser scales; decoder consumes each encoder scale with cross-attention; multi-scale predictions summed over layers.

## Typical Usage in EV Load Forecasting
- **Input**: past window of correlated multivariate series only (baselines additionally use timestamp covariates).
- **Forecasting Horizon**: [[Long_Term_Forecasting]] ($\tau$ up to 720; per-horizon look-back searched in {24,...,720}).
- **Strengths**: top-1 in 36/58, top-2 in 51/58 benchmark settings; router enables linear scaling in D (handles D=300 where no-router OOMs); lowest memory/fastest runtime among five tested Transformers.
- **Weaknesses**: all-to-all routing introduces noise on high-dimensional data; outperformed by [[DLinear]] on several datasets (ETTm1 long horizons, ECL, Traffic) — order-preservation flagged as future work; straightforward covariate embedding does not help.

## Literature Usage
- [[2023_Crossformer_Cross_Dimension_Dependency]] — Original paper: DSW + TSA + HED; ETTh1 τ=168 MSE 0.410 vs FEDformer 0.412 / Autoformer 0.493; ECL τ=48 0.156 vs FEDformer 0.229.
- [[2024_iTransformer_Inverted_Transformers_Effective_Time_Series]] — Cross-dimension alternative that underperforms iTransformer (Traffic efficiency: 9.74 GB/702 ms vs iTransformer's variate-token attention).
- [[2025_Multi_View_Graph_Intrusion_Detection_EV]] — Related cross-feature dependency modeling line for EV charging-station security.
