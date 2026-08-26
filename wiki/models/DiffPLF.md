---
type: model
name: DiffPLF
category: Deep Learning / Conditional Diffusion for Probabilistic EV Load Forecasting
tags:
  - model
  - deep-learning
  - diffusion
  - probabilistic-forecasting
  - ev-load-forecasting
---

# 🔮 DiffPLF

## Overview
DiffPLF (Li et al., PSCC 2024) is a conditional denoising diffusion model ([[DDPM]]) for **probabilistic EV charging-load forecasting**, explicitly approximating the predictive distribution $q(x_0|p,r)$ conditioned on historical demand $p$ and covariates $r$ (temperature/humidity forecasts, one-hot weekday, number of charged EVs). Two innovations over prior diffusion forecasters ([[TimeGrad]], [[CSDI]]):

1. **Cross-attention conditioning** (from latent diffusion / text-to-image models): conditions are queries, perturbed load series keys/values:
$$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^T}{\sqrt{d}}\right)V, \quad Q=h_\phi(p,r)W_Q,\ K=f_\phi(x_t,t)W_K,\ V=f_\phi(x_t,t)W_V$$
with conditional training objective:
$$L_{t-1} = \mathbb{E}_{x_0,c,\epsilon,t}\left[\|\epsilon-\epsilon_\theta(\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha}_t}\epsilon,\ c,\ t)\|_2^2\right]$$
2. **Task-informed fine-tuning (QDM)**: sharpen prediction intervals by minimizing the deviation of the sampled median $m_0$ from ground truth via the differentiable surrogate $L_{\text{QDM}} = \|\epsilon_\theta(m_t,c,t)-\epsilon_\theta(x_t,c,t)\|_2^2$, total loss $L_{\text{ref}} = L_{t-1} + \lambda L_{\text{QDM}}$ ($\lambda=0.001$).

Denoising network: LSTM perturbation encoder + LSTM condition encoder + cross-attention + self-attention forecast head; quadratic schedule β₁=0.0001 → β_T=0.5, **T=200 diffusion steps**; 1000 trajectories per test case.

## Typical Usage in EV Load Forecasting
- **Input**: past 5 days of aggregate demand (15-min Palo Alto data), weather forecasts, calendar vector, EV count.
- **Forecasting Horizon**: [[Day_Ahead_Forecasting]] (24 h; also retraining-free 12/6/4/1 h).
- **Strengths**: −39.58% MAE and −49.87% CRPS vs quantile regression (MAE 7.161 vs 11.852); controllable generation varying input EV count (robust to ±5–10% errors); sharp reliable intervals at all horizons.
- **Weaknesses**: needs a separate fine-tuning stage for accuracy (end-to-end model left as future work); sensitive to diffusion steps T (worse at T=100/250/300); univariate/station-level scope.

## Literature Usage
- [[2024_Li_DiffPLF_Conditional_Diffusion_EV]] — Original paper: conditional diffusion + cross-attention + QDM fine-tuning on Palo Alto charging data; ablations show covariates contribute ~10%, cross-attention beats latent addition fusion.
