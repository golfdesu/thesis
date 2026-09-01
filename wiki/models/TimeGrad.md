---
type: model
name: TimeGrad
category: Deep Learning / Autoregressive Conditional Diffusion Forecaster
tags:
  - model
  - deep-learning
  - diffusion
  - probabilistic-forecasting
---

# ⏳ TimeGrad

## Overview
TimeGrad (Rasul et al., ICML 2021) is an autoregressive energy-based model sampling from the **full joint multivariate predictive distribution** at each time step via denoising diffusion ([[DDPM]]) — avoiding restrictive parametric emission families (Gaussian / negative binomial / copulas / normalizing flows). A diffusion head conditioned on an [[LSTM]] hidden state estimates the **score** of the data distribution.

Key equations:
- Forward noising with schedule $\beta_1..\beta_N$: $q(x_n|x_{n-1}) = \mathcal{N}(x_n;\sqrt{1-\beta_n}\,x_{n-1},\ \beta_n\mathbf{I})$, closed form $q(x_n|x_0) = \mathcal{N}(x_n;\sqrt{\bar{\alpha}_n}\,x_0,\ (1-\bar{\alpha}_n)\mathbf{I})$.
- Simplified score-matching loss conditioned on RNN state $h_{t-1}$:
$$E_{x^0_t,\epsilon,n}\left[\|\epsilon-\epsilon_\theta(\sqrt{\bar{\alpha}_n}x^0_t+\sqrt{1-\bar{\alpha}_n}\epsilon,\ h_{t-1},\ n)\|^2\right]$$
- Autoregressive factorization: $q_X(x^0_{t_0:T}|\cdot) \approx \prod_{t=t_0}^{T} p_\theta(x^0_t|h_{t-1})$ with $h_t = \text{RNN}_\theta(\text{concat}(x^0_t, c_t), h_{t-1})$.
- Reverse sampling (annealed Langevin-style): $x_{n-1} = \frac{1}{\sqrt{\alpha_n}}(x_n - \frac{\beta_n}{\sqrt{1-\bar{\alpha}_n}}\epsilon_\theta(x_n,n)) + \sqrt{\Sigma_\theta}\,z$.

εθ network: 8 conditional residual blocks of bidirectional dilated 1-D convolutions (WaveNet/DiffWave-style, gated activations). Linear noise schedule $\beta_1=10^{-4}\to\beta_N=0.1$, $N=100$; DeepAR-style mean scaling; $S=100$ sampled trajectories at inference.

## Typical Usage in EV Load Forecasting
- **Input**: multivariate history + time covariates + frequency-specific lag features; context size = prediction length.
- **Forecasting Horizon**: [[Short_Term_Forecasting]] (24–30 steps).
- **Strengths**: SOTA CRPSsum on Traffic/Electricity/Taxi/Wikipedia (~21% lower than Transformer-MAF); calibrated intervals across entities of vastly different scale; flexible non-parametric emissions.
- **Weaknesses**: inference latency — N=100 diffusion steps × S=100 trajectories per autoregressive timestep; RNN conditioning limits very long sequences; no spatial inductive bias between stations.

## Literature Usage
- [[2021_TimeGrad_Diffusion_Forecasting]] — Original paper: LSTM-conditioned DDPM head; new SOTA CRPSsum on five of six benchmarks (Electricity 0.0206, Traffic 0.044).
- [[2021_CSDI_Conditional_Diffusion_Forecasting]] — Direct predecessor: CSDI's joint temporal diffusion beats TimeGrad on electricity forecasting CRPS-sum (0.017 vs 0.021) and traffic (0.020 vs 0.044).
- [[2024_DiffPLF_Conditional_Diffusion_EV]] — Contrast point for EV charging-load diffusion design: DiffPLF replaces concatenation-style conditioning with cross-attention conditioning.
