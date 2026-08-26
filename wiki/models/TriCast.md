---
type: model
name: TriCast
category: Deep Learning / Tri-Modal Causal Spatio-Temporal-Economic Graph Network
tags:
  - model
  - deep-learning
  - graph-neural-network
  - spatio-temporal
  - causal
---

# 🔺 TriCast

## Overview
TriCast (Wang et al., Pattern Recognition Letters 2026) is a tri-modal forecasting framework that jointly models **spatial, temporal, and economic modalities** for urban EV charging demand prediction on a charging network graph $G=(V,E,A)$. Given a historical window $X \in \mathbb{R}^{P\times N\times C}$ (occupancy, price, context), it predicts $Y \in \mathbb{R}^{Q\times N\times C}$. It targets three deficiencies of prior methods: static proximity-only graphs, temporal information leakage in attention models, and shallow economic modeling. Three purpose-built modules:

- **PEM (Price Elasticity Modulator)** — L-step random-walk propagation $P = \text{RandomWalk}(A,L)$ with row normalization $P_{i,j} = P_{i,j}/\sum_k P_{i,k}$; gated occupancy enhancement and behavior-modulated price:
$$X^*_t = X_t + \sigma(W_X P X_t) \odot f_X(P X_t), \qquad E^*_t = E_t \odot \left(1 + \sigma(W_E \tilde{E}_t) \odot f_E(\tilde{E}_t)\right)$$
with $\tilde{E}_t = P E_t$ the spatially smoothed price vector.
- **SAGE (Semantic-Aware Graph Encoder)** — semantic inducing points $I = \text{TopK}(\text{GCN}(X^*_t, A)) \in \mathbb{R}^{m\times d'}$, $m \ll N$, followed by two-stage Set Transformer induced attention ($H_1 = \text{MAB}_1(I, H_{conv})$, $\hat{H}_1 = \text{MAB}_2(H_{conv}, H_1)$) and hierarchical residual fusion:
$$Z_{out} = (1-\alpha) Z^{(2)} + \alpha[(1-\alpha)Z^{(1)} + \alpha H_{conv}]$$
- **TACT (Temporal Alignment with Causal Transformation)** — dilated causal convolutions $H^{(l)} = \text{CausalConv1D}(Z^{(l-1)}; k, 2^l)$ with causal padding (no future leakage), price-aware gated modulation $\hat{H}^{(l)} = H^{(l)} \odot (1 + \tanh(E_t))$ and gated residual blocks.

Prediction head: MLP over temporally pooled features, trained with MSE loss $\mathcal{L} = \frac{1}{BN}\sum_b\sum_i (\hat{Y}_{b,i} - Y_{b,i})^2$.

## Typical Usage in EV Load Forecasting
- **Input**: zone-level charging occupancy + electricity prices + traffic-zone adjacency graph ([[UrbanEV_Dataset]] Shenzhen, 247 nodes / 1006 edges).
- **Forecasting Horizon**: [[Short_Term]] — 3–12 steps (15–60 min ahead) from a 12-step (1 h) input.
- **Strengths**: avg RMSE 4.71 ×10⁻² and MAPE 15.41 across horizons, −9.8% MAPE vs best prior at 15 min among 16 baselines; robust to inference-time noise; ablation shows SAGE induced attention most critical.
- **Weaknesses**: deterministic point forecasts only (no probabilistic output); single-city/30-day validation; elasticity learning constrained by sparse dynamic-price coverage (57/247 zones); occupancy used as demand proxy.

## Literature Usage
- 2026 — [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] : Original paper — SAGE + TACT + PEM tri-modal framework on [[UrbanEV_Dataset]] (Shenzhen, 5-min resolution); beats VAR/Lasso/KNN/LSTM/GCN/GAT/DCRNN/AST-GAT/FourierGNN/PAG/CityEVCP/PIAST etc., paired t-test p < .01.
