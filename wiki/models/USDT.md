---
type: model
name: USDT
category: Deep Learning / Uncertainty-Scale Dual-Direction Probabilistic Transformer
tags:
  - model
  - deep-learning
  - transformer
  - probabilistic-forecasting
  - long-term-forecasting
---

# ⚖️ USDT (Uncertainty-Scale Dual-Direction Transformer)

## Overview
USDT (Zhang et al., Sustainable Energy, Grids and Networks 2026) is a probabilistic EV charging-load forecasting model built on an [[Informer]]/[[MetaProbformer]] backbone, augmented with two new modules for multi-station load:

- **SMAN (Scalable Multi-Scale Linear Attention Network)** — convolutional Q/K/V projections embedding spatial-temporal neighborhood structure, $Q = \text{Conv}_Q(X)$, $K = \text{Conv}_K(X)$, $V = \text{Conv}_V(X)$, with multi-scale processing of fast spikes + slow diurnal/weekly cycles and query sparsity via KL-divergence-style max–mean gap:
$$S(q_l, K) = \max_j \left\{ q_l k_j^\top \right\} - \frac{1}{L_K}\sum_{j=1}^{L_K} q_l k_j^\top$$
only top-scoring "active" queries receive full attention. Pipeline: 2DConv×2 → ReLU → BatchNorm → Multi-scale → ReLuLinearAttention → LayerNorm → ReLU6.
- **DDI (Dual-Direction Interaction module)** — bidirectional attention separating horizontal (cross-station co-movement) and vertical (within-station temporal) dynamics with residual fusion preserving station-specific baselines:
$$\text{Output}_h = \text{softmax}\!\left(\frac{Q_h K_h^\top}{\sqrt{d_k}}\right)V_h, \quad \text{Output}_v = \text{softmax}\!\left(\frac{Q_v K_v^\top}{\sqrt{d_k}}\right)V_v, \quad \text{Final} = X + \text{Output}_h + \text{Output}_v$$

Encoder: embeddings → SMAN → DDI → MHPSA → SAD → MHPSA; decoder adds MMHPSA + MHA + fully connected heads bifurcating into mean $\mu_t$ and std $\sigma_t$ (Softplus), giving a Gaussian predictive PDF $\mathcal{N}(\mu_t,\sigma_t^2)$ per step; intervals from standard-normal quantiles; trained with negative log-likelihood $\mathcal{L} = -\sum_t \log P(y_t \mid y_{<t}, X)$.

## Typical Usage in EV Load Forecasting
- **Input**: univariate hourly station load (96-h input window, 48 label length) + cyclical/discrete calendar encodings; z-score normalization on train-split statistics only.
- **Forecasting Horizon**: [[Long_Term_Forecasting]] — hourly steps; benefits grow with horizon length and input length.
- **Strengths**: EVnetNL RMSE 8.781 vs Informer 9.866 (−10.99%) and MSE −21%; robust across 5 seeds (9.222 ± 0.181); zero-shot cross-domain transfer degrades only +26.8% vs Informer's +102% (on Perth it even beats in-domain training by −2.0%); −36.5% peak VRAM vs Informer; well-calibrated intervals (ACE 0.0659, near-uniform PIT).
- **Weaknesses**: modest short-horizon gains over strong baselines; +213% iteration latency from multi-scale/dual-direction pathways; degrades under pronounced domain shift.

## Literature Usage
- 2026 — [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] : Original paper — USDT on [[ElaadNL|EVnetNL]], [[Perth_EV|Perth]], [[Boulder_Colorado|Boulder]] and [[Palo_Alto_EV|Palo Alto]] data; ablation isolates SMAN (+SWAN) and DDI contributions on the Informer baseline (9.866 → 8.781 RMSE).
