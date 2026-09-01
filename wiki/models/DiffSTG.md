---
type: model
name: DiffSTG (UGnet)
category: Deep Learning / Denoising Diffusion Probabilistic Model on Spatio-Temporal Graphs
tags:
  - model
  - deep-learning
  - diffusion
  - probabilistic-forecasting
  - spatial-temporal
  - gnn
---

# 🌀 DiffSTG

## Overview
DiffSTG (Wen et al., 2023) is the **first generalization of DDPM to spatio-temporal graphs (STGs)**: a non-autoregressive probabilistic forecasting framework paired with **UGnet**, the first DDPM denoising network dedicated to STGs (Unet-style temporal architecture + GNN spatial modeling). Deterministic STGNNs cannot quantify uncertainty; prior diffusion forecasters ([[TimeGrad]], [[CSDI]]) model single-node temporal dynamics only, miss spatial correlations, and suffer sequential train/inference inefficiency. DiffSTG reduces CRPS by 4–14% and RMSE by 2–7% on three real-world datasets.

- **Conditional reverse process** — history $\boldsymbol{x}_h$ and graph $G$ condition denoising:
$$p_\theta(\boldsymbol{x}_{0:N}^p|\boldsymbol{x}_h,G)=p(\boldsymbol{x}_N^p)\prod_{n=N}^{1}p_\theta(\boldsymbol{x}_{n-1}^p|\boldsymbol{x}_n^p,\boldsymbol{x}_h,G), \quad L(\theta)=\mathbb{E}\big\|\epsilon-\epsilon_\theta(\sqrt{\alpha_n}\boldsymbol{x}_0^p+\sqrt{1-\alpha_n}\epsilon,\,n|\boldsymbol{x}_h,G)\big\|_2^2$$
- **Generalized masked formulation** — history + future unified as $\boldsymbol{x}^{all}=[\boldsymbol{x}_h,\boldsymbol{x}_p]\in\mathbb{R}^{F\times V\times T}$, history represented by masking future steps $\boldsymbol{x}^{all}_{msk}$; unifies STG prediction/generation/interpolation in one framework.
- **UGnet denoiser** $\epsilon_\theta(\boldsymbol{x}^{all}_n, n|\boldsymbol{x}^{all}_{msk}, G)$: temporal concatenation → linear projection → stacked ST-Residual Blocks with Unet down/up-sampling over time, each block combining a **gated causal TCN** ($\Gamma_T(H_i) = P_i \odot \sigma(Q_i)$, the WaveNet-style gate), **vanilla GCN** ($A_{gcn}=D^{-1/2}(A+I)D^{-1/2}$), and transformer positional **noise-level embedding** $e(n)$.
- **Non-autoregressive inference**: one reverse process generates all $T_p$ steps at once (vs TimeGrad's $T_p$ runs); DDIM-style subset sampling of $M<N$ steps plus reusing last-$k$ reverse steps as samples cuts cost from $S\times N$ to $\tilde S\times\tilde N$ — ~40× faster than TimeGrad.

## Typical Usage in EV Load Forecasting
- **Input**: graph signals $\mathbf{x}^t\in R^{F\times V}$ over $T_h=12$ steps + adjacency (road network for PEMS08; station distances for AIR-BJ/GZ).
- **Forecasting Horizon**: [[Spatial_Temporal_Forecasting]] ($T_p = 12$ steps; 5-min traffic / hourly air quality).
- **Strengths**: full predictive distribution per node-step; best MAE/RMSE/CRPS among probabilistic baselines (PEMS08 CRPS 0.06 vs TimeGrad 0.09); massive sampling speed-up enables near-real-time deployment.
- **Weaknesses**: still trails SOTA *deterministic* STGNNs (PEMS08: GMSDR MAE 16.01 vs DiffSTG 17.68) since the variational objective yields an inaccurate posterior with insufficient samples; vanilla GCN only in UGnet; multi-step sampling remains at inference; more parameters than TimeGrad/CSDI.

## Literature Usage
- [[2023_DiffSTG_Probabilistic_ST_Graph_Diffusion]] — Original paper: AIR-BJ/AIR-GZ/PEMS08 CRPS −5.6%/−4.3%/−14.3% vs most competitive baseline; ablations confirm GNN, TCN, and Unet components all essential.
- [[2021_CSDI_Conditional_Diffusion_Forecasting]] — CSDI's masked conditional-training scheme is DiffSTG's direct ancestor; DiffSTG adds spatial conditioning + non-autoregressive generation (CSDI beaten on all three datasets).
- [[2024_DiffPLF_Conditional_Diffusion_EV]] — DiffPLF extends the same conditional-diffusion line specifically to EV charging load via cross-attention conditioning; DiffSTG complements it with the graph/spatial dimension absent in DiffPLF's station-level scope.
- [[2019_Graph_WaveNet_Spatial_Temporal_Modeling]] — UGnet inherits Graph WaveNet's gated dilated causal TCN as its temporal layer (cited as ref [44]), grafting the deterministic WaveNet backbone into a diffusion denoiser.
