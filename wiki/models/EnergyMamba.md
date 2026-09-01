---
type: model
name: GE-Mamba (EnergyMamba)
category: Deep Learning / Graph-Enhanced Selective State-Space Model
tags:
  - model
  - mamba
  - ssm
  - gcn
  - spatiotemporal
  - probabilistic-forecasting
---

# ⚡ GE-Mamba (EnergyMamba)

## Overview
GE-Mamba (Yu et al., KDD '26) reformulates energy-consumption prediction as an **uncertainty-aware spatiotemporal** task: a per-time-step [[GCN]] extracts spatial context over a grid-topology graph (Census Block Groups / ISO zones) and **injects it into the selective-scan dynamics** of a bidirectional [[Mamba_SSM]], organized in a U-Net encoder–decoder for multi-scale temporal modeling. Three linear heads output median/lower/upper quantiles; the [[AS_CQR]] wrapper calibrates the resulting intervals online.

Key mechanism — spatial context conditions input-dependent SSM selectivity:
$$Z_t=\mathrm{GCN}(H_t,A)=\mathrm{GELU}\!\left(\tilde{D}^{-\frac12}\tilde{A}\tilde{D}^{-\frac12}H_tW_{\text{gcn}}\right),\quad \tilde{A}=A+I_N$$
$$B_t=W_B[h_t\,\|\,z_t],\quad C_t=W_C[h_t\,\|\,z_t],\quad \Delta_t=\mathrm{Softplus}\!\left(W_\Delta[h_t\,\|\,z_t]+b_\Delta\right)$$
Bidirectional processing $\mathrm{BIP}(H,Z)=\mathrm{Mamba}_{\rightarrow}(H,Z)+\mathrm{Mamba}_{\leftarrow}(\mathrm{Flip}(H),\mathrm{Flip}(Z))$; blocks stacked in a U-Net (S=2 stages, K=2 blocks/stage, D=64, state dim 16) with skip connections preserving spikes. Adjacency uses Gaussian-kernel geographic distances with sparsity thresholding $A_{ij}=\exp(-d_{ij}^2/\sigma^2)\cdot\mathbb{1}\{\cdot\ge\epsilon\}$ — the authors flag physical-topology edges + adaptive graph learning as future work.

Trained end-to-end with pinball loss at $\tau\in\{\alpha/2, 0.5, 1-\alpha/2\}$; log-normalization $X'=\ln(X+1)$ preprocessing.

## Typical Usage in EV Load Forecasting
- **Input**: univariate historical consumption per node ([[Historical_Load]]) + learnable temporal position embedding; graph from centroid distances. No exogenous covariates.
- **Forecasting Horizon**: [[Short_Term_Forecasting]] (30-min / 1-h steps).
- **Strengths**: beats 15 SOTA baselines by ~5% MAE / ~6% Interval Score; ≥90% target coverage everywhere; tiny footprint (312.8K params, 2.78 s inference) vs LLM baselines (67M+).
- **Weaknesses**: regional/building-aggregate granularity (CBGs/zones), not station-level EV loads; geographic-proxy graphs (no true topology); marginal long-run coverage guarantee only, not per-step conditional coverage; no monotonicity structure à la [[PICNN]].

## 📚 Literature Usage
- [[2026_EnergyMamba_Graph_Mamba_ASCQR]] — Original KDD '26 paper: GCN-conditioned bidirectional selective SSM in U-Net + [[AS_CQR]]; evaluated on [[Florida_CBG_Smart_Meter]], [[NYISO]], [[CAISO]] ([[MAE]]/[[RMSE]]/[[MPIW]]/[[Interval_Score]]/[[PICP]]).

## Related Pages
- [[Mamba_SSM]]
- [[GCN]]
- [[AS_CQR]]
