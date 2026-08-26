---
type: model
name: CSDI
category: Deep Learning / Conditional Score-Based Diffusion (Imputation + Forecasting)
tags:
  - model
  - deep-learning
  - diffusion
  - probabilistic-forecasting
  - imputation
---

# 🩺 CSDI

## Overview
CSDI (Tashiro et al., NeurIPS 2021) is a conditional score-based [[DDPM]] trained *directly* on the conditional distribution $q(x^{ta}_0 \mid x^{co}_0)$ for probabilistic time-series imputation — also competitive at interpolation and forecasting. Unlike prior approximations (noising the observations, which destroys information), CSDI models the exact conditional reverse process via a **self-supervised masked-training scheme** inspired by BERT, with a 2D (temporal + feature) Transformer denoiser adapted from DiffWave. Results: CRPS improved **40–65%** over probabilistic imputation baselines; MAE improved **5–20%** over deterministic SOTA.

Key equations:
- Conditional reverse process: $p_\theta(x^{ta}_{0:T}|x^{co}_0) = p(x^{ta}_T)\prod_{t=1}^T p_\theta(x^{ta}_{t-1}|x^{ta}_t, x^{co}_0)$.
- Conditional denoising objective:
$$\min_\theta L(\theta) := \min_\theta E_{x_0,\epsilon,t}\left\|\epsilon - \epsilon_\theta(x^{ta}_t, t \mid x^{co}_0)\right\|_2^2$$
with noisy targets $x^{ta}_t = \sqrt{\alpha_t}x^{ta}_0 + (1-\alpha_t)\epsilon$; at sampling targets = missing values, conditionals = observed.
- Quadratic noise schedule: $\beta_t = \left(\sqrt{\frac{T-t}{T-1}}\sqrt{\beta_1} + \sqrt{\frac{t-1}{T-1}}\sqrt{\beta_T}\right)^2$, $\beta_1=0.0001,\ \beta_T=0.5$, $T=50$.
- Denoiser: temporal Transformer layer (per-feature dependency) + feature Transformer layer (per-timestep cross-feature dependency), each 1-layer/8-head, with diffusion-step and timestamp embeddings.

Target choice strategies: Random / Historical / Mix (+ test-pattern mask for forecasting); masked-training variant handles real missing values.

## Typical Usage in EV Load Forecasting
- **Input**: multivariate series $\in \mathbb{R}^{K\times L}$ with observation mask $M$ and timestamps $s$ (irregular intervals allowed).
- **Forecasting Horizon**: [[Short_Term]] (168→24 on electricity/traffic/solar benchmarks).
- **Strengths**: exact conditional modeling; both temporal AND feature dependencies essential (ablation: healthcare 10% MAE 0.217 vs Bi-RNN 0.272, flatten 0.383); gains already with 5–10 samples.
- **Weaknesses**: iterative reverse diffusion (50 steps) slow for real-time EV deployment (ODE/DDIM acceleration suggested); forecasting advantage smaller than imputation advantage; historical strategy sensitive to train/test pattern mismatch.

## Literature Usage
- [[2021_Tashiro_CSDI_Conditional_Diffusion_Forecasting]] — Original paper: healthcare CRPS 0.238 vs GP-VAE 0.574 at 10% missing; best CRPS-sum on electricity (0.017) and traffic (0.020) forecasting.
- [[2024_Li_DiffPLF_Conditional_Diffusion_EV]] — DiffPLF adopts CSDI's variance scheduling scheme and extends conditional diffusion to EV charging-load forecasting with cross-attention conditioning.
