---
type: model
name: DLinear
category: Deep Learning / One-Layer Linear Long-Term Forecaster (LTSF-Linear)
tags:
  - model
  - linear-model
  - long-term-forecasting
  - decomposition
---

# 📏 DLinear

## Overview
DLinear (Zeng et al., AAAI 2023, "Are Transformers Effective for Time Series Forecasting?") is part of **LTSF-Linear**: embarrassingly simple one-layer direct-multi-step (DMS) linear models that beat FEDformer/Autoformer/Informer/Pyraformer/LogTrans on all nine LTSF benchmarks, often by **20–50%**. The paper's core argument: self-attention is permutation-invariant and "anti-order", causing temporal information loss positional embeddings cannot repair.

Core formulation — one temporal linear layer shared across variates: $\hat{X}_i = W X_i, \qquad W \in \mathbb{R}^{T \times L}$

**DLinear (Decomposition Linear)** reuses Autoformer-style moving-average decomposition into trend + seasonal, with separate one-layer linear heads summed at output (kernel size 25):
$$\hat{X} = \text{Linear}_{trend}(X_{trend}) + \text{Linear}_{seasonal}(X_{seasonal})$$

Properties: $O(1)$ maximum signal traversing path length, only ~2TL parameters, interpretable weights revealing learned periodicity (daily/weekly cycles in Traffic). Companion model [[NLinear]] subtracts/adds back the last value to combat distribution shift: $\hat{X} = W(X - x_L) + x_L$.

## Typical Usage in EV Load Forecasting
- **Input**: raw look-back window ($L=336$ default), no covariates.
- **Forecasting Horizon**: [[Long_Term]] ($T \in \{96,...,720\}$).
- **Strengths**: near-zero cost (0.04G MACs, 139.7K params, 0.4 ms vs Informer 49.3 ms); improves markedly with longer look-backs; strong baseline that many deep models still fail to beat.
- **Weaknesses**: limited capacity — cannot capture change points; no cross-variate modeling; authors position it as a baseline, not an end model.

## Literature Usage
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — Original paper: Electricity T=96 MSE 0.140 vs FEDformer 0.193 / Informer 0.274; Exchange T=720 0.643 vs FEDformer 1.447; shuffling inputs hurts linear models (27–81%) but not Transformers → order preservation is the differentiator.
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — The rebuttal PatchTST answers: patched CI Transformers beat DLinear on large datasets (Electricity T=96: 0.129 vs 0.140) and ILI.
- [[2023_Wu_TimesNet_Temporal_2D_Variation_Modeling]] — TimesNet beats DLinear in forecasting (40 vs 14 first-place counts) while DLinear collapses on classification/imputation (67.5% accuracy) — fixed temporal parameters cannot learn hierarchical representations.
- [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]] — Concurrent challenger: DLinear beats Crossformer on ETTm1 long horizons, ECL, Traffic (e.g., Traffic τ=24: 0.351 vs 0.491).
- [[2024_Das_TiDE_Long_Term_Forecasting]] — Motivation for TiDE; a pure linear model is a guaranteed subclass via TiDE's global residual connection.
- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — Linear forecaster motivating the inversion reflection; iTransformer restores Transformer dominance over RLinear/DLinear-style baselines.
- [[2001_Hippert_Neural_Networks_STLF_Review]] — Modern echo of the review's "benchmark simple linear models" message for load forecasting.
