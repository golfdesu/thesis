---
type: model
name: Graph WaveNet
category: Deep Learning / Adaptive-Adjacency Spatial-Temporal GNN (GCN + Gated Dilated TCN)
tags:
  - model
  - deep-learning
  - gnn
  - spatial-temporal
  - tcn
---

# 🌊 Graph WaveNet

## Overview
Graph WaveNet (Wu et al., IJCAI 2019) is a CNN-based deep spatial-temporal graph model combining (i) a **self-adaptive adjacency matrix** learned end-to-end from node embeddings — capturing *hidden* spatial dependencies without prior graph knowledge — and (ii) **gated dilated causal convolutions** whose receptive field grows exponentially with depth, avoiding RNN-style iterative propagation and gradient explosion.

- **Self-adaptive adjacency (Eq. 5)** — from learnable source/target node embeddings $E_1, E_2 \in \mathbb{R}^{N\times c}$; ReLU eliminates weak connections, SoftMax normalizes so $\tilde{A}_{adp}$ acts as the transition matrix of a hidden diffusion process:
$$\tilde{A}_{adp} = \text{SoftMax}\big(\text{ReLU}(E_1 E_2^T)\big)$$
- **Combined graph convolution (Eq. 6)** — predefined forward/backward diffusion ($P_f = A/\text{rowsum}(A)$, $P_b = A^T/\text{rowsum}(A^T)$) plus hidden dependencies:
$$Z = \sum_{k=0}^{K} P_f^k X W_{k1} + P_b^k X W_{k2} + \tilde{A}_{adp}^k X W_{k3}$$
with adaptive-only mode $Z = \sum_k \tilde{A}_{adp}^k X W_k$ when no graph is given.
- **Gated TCN (Eq. 9)** — two parallel dilated causal convolutions ($x \star f(t) = \sum_{s=0}^{K-1} f(s)\,x(t - d\times s)$), tanh branch ⊙ sigmoid gate:
$$h = g(\Theta_1 \star X + b) \odot \sigma(\Theta_2 \star X + c)$$
- **Framework**: stacked layers of Gated TCN → GCN (separate GCN weights per temporal stage); residual + skip connections; MAE loss; outputs all $T$ horizon steps **in one shot** (non-recursive), eliminating train/test inconsistency.

## Typical Usage in EV Load Forecasting
- **Input**: sensor/station time series $X^{(t)}\in\mathbb{R}^{N\times D}$ over $S$ historical steps + (optionally) distance-based adjacency.
- **Forecasting Horizon**: [[Short_Term_Forecasting]] (12 steps @ 5 min on METR-LA/PEMS-BAY).
- **Strengths**: learns inter-station dependencies where explicit graphs miss them (adaptive-only ≈ matches forward-diffusion on METR-LA; forward-backward-adaptive best at 3.04/6.09/8.23%); one-shot decoding fastest of all baselines (2.27 s total inference vs DCRNN 18.73 s).
- **Weaknesses**: adaptive adjacency is static once trained (dynamic/time-varying dependencies left as future work); point forecasts only, no uncertainty quantification; receptive field must be engineered to equal input length.

## Literature Usage
- [[2019_Graph_WaveNet_Spatial_Temporal_Modeling]] — Original paper: SOTA MAE/RMSE/MAPE on METR-LA (15-min 2.69/5.15/6.90%) and PEMS-BAY (1.30/2.74/2.73%), gains growing with horizon vs GGRU/DCRNN/STGCN.
- [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]] — STMGCN for Beijing fast-charging load inherits the WaveNet-style gated-TCN temporal block inside a multi-graph convolutional layer with spatiotemporal attention (MAE 53.287 kW / RMSE 78.831 kW); TCN-only ablation degrades to 61.145/90.681 kW.
- [[2024_Physics_Informed_GAT_EV_Load]] — Cited as the spatial-temporal backbone lineage for EV-station GNN forecasters where dependency structure must be learned rather than given.
- [[2025_MSSTGAN_City_EV_Load]] — MSSTGAN city-scale EV load generator belongs to the same adaptive-graph + gated-temporal design line for multi-station charging demand.
- [[2023_DiffSTG_Probabilistic_ST_Graph_Diffusion]] — DiffSTG's UGnet denoiser embeds the same gated causal temporal convolution (cites Graph WaveNet as ref [44]) but swaps deterministic regression for masked DDPM sampling, making the WaveNet line probabilistic.
