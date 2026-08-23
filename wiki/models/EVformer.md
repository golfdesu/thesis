---
type: model
name: EVformer
category: Deep Learning / Spatio-Temporal Decoupled Transformer for Citywide EV Charging Load Forecasting
tags:
  - model
  - deep-learning
  - transformer
  - spatial-temporal
  - ev-load-forecasting
---

# ⚡ EVformer

## Overview
EVformer (Jia & Yang, *World Electric Vehicle Journal* 2026, [[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]]) is a **modular encoder–decoder Transformer that explicitly decouples temporal sequence modeling from spatial dependency learning** for citywide EV charging load forecasting. It targets three bottlenecks of coupled spatio-temporal Transformers: quadratic $O(T^2 C)$ time–time self-attention, quadratic $O(N^2)$ spatial attention over stations, and rigid monolithic architectures. Its distinctive components are:

- **Spatio-Temporal Embedding (STE)**: sinusoidal + learnable temporal embedding $TE_t = [\sin(\omega t), \cos(\omega t)] + e_t$ and per-node spatial embedding $SE$, fused as $H_t = \text{MLP}([X_t; TE_t; SE])$.
- **Two-stage channel-first temporal attention**: a global aggregation $\text{Pool}$ compresses each node's multi-channel sequence into a shared latent query ($o^{(i)}_t = \text{Pool}(S_i[t,:])$), so attention is computed against global queries with causal masking — avoiding pairwise time–time coupling entirely.
- **Semantics-aware Top-K spatial attention**: hybrid neighbor selection combining physical urban topology adjacency $A_{ij}=1$ (geographic connectivity) with cosine similarity of semantic embeddings $s_i$ (land-use type, charging policy, charger density):
$$\mathcal{N}^{top}_i = \text{TopK}\left(\frac{s_i^\top s_j}{\lVert s_i \rVert \lVert s_j \rVert}\right), \quad j \in \mathcal{N}^A_i$$
then multi-head attention restricted to $\mathcal{N}^{top}_i$ with a learnable semantic bias $b_{ij}$ — cutting complexity from $O(N^2 d)$ to $O(K^2 d)$.
- **Bidirectional Temporal Bridge (BTB)**: forward mapping $Z^{fwd} = \text{MultiHeadAttn}(E^{query}, H^{enc}, H^{enc})$ plus reverse refinement $H^{rev} = \text{MultiHeadAttn}(H^{enc}, Z^{fwd}, Z^{fwd})$, gated-fused via $\lambda = \sigma(W[H^{enc}; Z^{fwd}] + b)$ to reduce error propagation in multi-horizon decoding.
- **Gated Fusion Unit**: per block, adaptively balances temporal vs. spatial branches:
$$H^{(l)} = z \odot H^{(l)}_{spat} + (1-z) \odot H^{(l)}_{temp}, \qquad z = \sigma(W_z[H^{(l)}_{spat}; H^{(l)}_{temp}] + b_z)$$
- **Multi-Horizon Decoder (MHD)**: independent decoder layers for short/mid/long horizon ranges, adaptively fused with learnable weights $\hat{Y} = \sum_{k=1}^{3} \alpha_k Y^{(k)}$, $\sum_k \alpha_k = 1$. Trained end-to-end with an MAE loss for outlier robustness.

## Typical Usage in EV Load Forecasting
- **Input**: past 1 h at 5-min resolution ($T=12$) over 247 regional nodes; node features include charging demand, charging duration, pile utilization rate, pricing mechanism (fixed/dynamic), regional functional type, charging pile density.
- **Forecasting Horizon**: very short-term multi-step ([[Spatial_Temporal_Forecasting]]) — τ = 3/6/9 steps = 15/30/45 min.
- **Strengths**: best MAE/RMSE/MAPE on ALL horizons vs 13 baselines on Shenzhen ST-EVCDP (RMSE ×10⁻²: 3.06/4.98/6.45; −3.8% RMSE vs PAG at 30 min, ~13% gain at 15 min); linear-ish spatial scaling ($O(K^2)$); compact (3.9 M params) and fast (5.7 ms inference/step).
- **Weaknesses**: evaluated only on ≤45-min horizons with ~30 days of single-season data (no weather/traffic exogenous features); region-level (247 zones), not individual stations; no probabilistic output.

## Literature Usage
- [[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]] — Original paper: channel-first global-aggregation temporal attention + semantic Top-K spatial attention + BTB/MHD/gated fusion; ablation shows w/o Spatial (static GCN substitute) costs +7.2% RMSE / +13.9% MAPE, w/o BTB +3.9%, w/o Gating +2.6%; optimal config Top-K=20, depth N=3.
