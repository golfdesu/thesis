---
type: model
name: RevIN
category: Deep Learning / Reversible Instance Normalization (Normalization Technique)
tags:
  - model
  - normalization
  - distribution-shift
  - plug-in-technique
---

# ♻️ RevIN (Reversible Instance Normalization)

## Overview
RevIN (Kim et al., ICLR 2022) is a simple, model-agnostic, end-to-end trainable **normalization-and-denormalization layer** against the **distribution shift problem**: train/test splits made at a point in time cause mean/variance divergence, degrading forecasts — especially for long horizons. RevIN symmetrically *removes* non-stationary instance statistics at the input and *restores* them at the output, with learnable affine parameters ($2K$ extra parameters only).

Key equations:
- Instance statistics (per variable $k$, instance $i$): $\mathbb{E}_t[x_{kt}^{(i)}] = \frac{1}{T_x}\sum_{j=1}^{T_x} x_{kj}^{(i)}$, $\text{Var}[x_{kt}^{(i)}] = \frac{1}{T_x}\sum_{j}(x_{kj}^{(i)} - \mathbb{E}_t[x_{kt}^{(i)}])^2$
- Normalization with learnable affine transform:
$$\hat{x}_{kt}^{(i)} = \gamma_k \left( \frac{x_{kt}^{(i)} - \mathbb{E}_t[x_{kt}^{(i)}]}{\sqrt{\text{Var}[x_{kt}^{(i)}] + \epsilon}} \right) + \beta_k$$
- Denormalization using the SAME input statistics:
$$\hat{y}_{kt}^{(i)} = \sqrt{\text{Var}[x_{kt}^{(i)}] + \epsilon} \cdot \left( \frac{\tilde{y}_{kt}^{(i)} - \beta_k}{\gamma_k} \right) + \mathbb{E}_t[x_{kt}^{(i)}]$$

Theory: after normalization all instances share $\mathbb{E}=\beta,\ \text{Var}=\gamma^2$ → identical train/test distributions by definition; the denormalized output satisfies $\mathbb{E}[\hat{y}]=\Delta+\mathbb{E}[x]$ and $\text{Var}[\hat{y}]=\lambda\cdot\text{Var}[x]$, so the model only learns the offset $(\Delta,\lambda)$.

> [!note] Technique, not a forecaster
> RevIN is a plug-in layer used *by* forecasters — most prominently [[PatchTST]] (instance normalization before patching) and optionally [[TiDE]] — rather than a standalone prediction model.

## Typical Usage in EV Load Forecasting
- **Input/Output**: wraps any encoder-decoder DNN; input and prediction lengths may differ since normalization is over time.
- **Strengths**: ETTh2@960 N-BEATS MSE 6.408→0.471; Informer 2.972→0.600; beats z-score/batch-norm/RevBN/DAIN normalizations by wide margins; robust when input fixed at 48 steps.
- **Weaknesses**: assumes future-window statistics ≈ input-window statistics plus small offset — may fail under abrupt regime changes longer than the input window; point forecasts only.

## Literature Usage
- [[2022_Kim_RevIN_Reversible_Instance_Normalization]] — Original paper: SOTA on seven large-scale datasets by adding RevIN to Informer/N-BEATS/SCINet; symmetric KL analysis quantifies reduced train/test feature divergence.
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — PatchTST's instance-normalization component (RevIN-style); helps notably on ILI (T=24 MSE 1.522 vs 3.489 without).
- [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]] — Flagged combination: N-HiTS backbone + RevIN for non-stationary EV charging demand as future work.
- [[2023_Ziyabari_Multi_Branch_ResTrans_Solar]] — Related normalization usage in multi-branch residual Transformer solar forecasting.
- [[2024_Das_TiDE_Long_Term_Forecasting]] — Optional reversible instance normalization component in TiDE training.
- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — iTransformer's per-variate-token LayerNorm is related to RevIN/stationarization for inconsistent measurements.
- [[2025_Li_DC_Charging_Profiles_TFT]] — β-VAE anomaly-detection stage of the DC fast-charging workflow uses RevIN layers to handle distributional shift/scale invariance across sessions.
- 2024 — [[2024_He_Robust_MTS_Transitional_Shift]] — JointPGM explicitly critiques RevIN for assuming a **time-invariant transition** between input and output windows and ignoring inter-series dynamics; in Table III (L/H=96/96) JointPGM beats RevIN-augmented backbones in ~92% of comparisons on Exchange/ILI non-stationary benchmarks, positioning PGM-based transitional-shift modeling as the successor to instance normalization.
- 2024 — [[2024_Menati_PowerMamba_Power_Systems_SSM]] — Adopted over Z-score normalization for non-stationary grid series (zonal loads/prices/renewables) as the first stage of PowerMamba's pipeline, ahead of trend–seasonal decomposition and dual-path Mamba blocks.
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Uses RevIN-standard normalization (mean/std of first input patch) for distribution-shift handling.
