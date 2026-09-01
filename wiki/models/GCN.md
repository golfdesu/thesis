---
type: model
name: Graph Convolutional Network (GCN)
category: Deep Learning / Graph Neural Networks
tags:
  - model
  - gcn
  - graph-neural-network
  - spatial-features
---

# 🧠 Graph Convolutional Network (GCN)

## Overview
GCN is a neural network architecture designed for non-Euclidean graph-structured data. It aggregates neighbor node features using a normalized graph Laplacian and adjacency matrix ($A$).

## Key Mathematical Equations
- **1st-Order Chebyshev Graph Convolution Layer**:
  $$H^{l+1} = \sigma\left( \tilde{D}^{-\frac{1}{2}} \tilde{A} \tilde{D}^{-\frac{1}{2}} H^l W^l \right)$$
  Where $\tilde{A} = A + I_N$ and $\tilde{D}$ is the diagonal degree matrix.
- **Gaussian Distance Adjacency Matrix**:
  $$A_{ij} = \exp\left( -\frac{\text{dist}(v_i, v_j)^2}{\sigma^2} \right) \quad \text{for } \text{dist} \le K$$

## Application in EV Charging Systems
- Extracts spatial dependencies across interconnected charging station networks in urban road grids.
- Combined with Transformers (GCN-TRN) or GRUs (GCN-GRU) for spatial-temporal load and availability forecasting ([[2022_GCN_TRN_EV_Availability]]).

## Literature References
- [[2022_GCN_TRN_EV_Availability]] - GCN-TRN model for EV charging station availability in Dundee City.
- [[2024_Physics_Informed_GAT_EV_Load]] - PAG couples GAT-based graph embedding (over 247 Shenzhen zones) with TPA-LSTM decoding and physics-informed meta-learning pre-training; RMSE 0.0548, ~6.73% average improvement over SOTA spatiotemporal baselines including GCN-LSTM.
- [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]] - STMGCN fuses distance- and similarity-based graphs in a multi-graph convolutional layer with spatiotemporal attention + gated TCN for Beijing fast-charging load: MAE 53.287 kW, RMSE 78.831 kW, beating 10 baselines.
- [[2025_EV_STLLM_Spatio_Temporal_LLM]] - GCN used as spatial baseline for Shenzhen charging-volume forecasting; the proposed spatio-temporal LLM cuts RMSE by 44–52% vs GCN across datasets/horizons.
- [[2025_Multi_View_Graph_Intrusion_Detection_EV]] - GCN encoder ablated against a mask-attention Graph Transformer in multi-view contrastive intrusion detection for EV charging stations; GCN clearly worse in self-supervised settings.
- [[2025_Meta_Learning_Physics_Informed_GACN_Power_System]] - Meta-PIGACN embeds the nodal admittance matrix as physics-informed edge weighting into graph attention convolution for distribution system state estimation; reduces voltage-magnitude MAE by 85.05% vs GCN on IEEE 33-node.
- [[2019_Graph_WaveNet_Spatial_Temporal_Modeling]] - Graph WaveNet generalizes GCN diffusion convolution ($Z = \sum_k P_f^k X W_{k1} + P_b^k X W_{k2} + \tilde{A}_{adp}^k X W_{k3}$) with a **self-adaptive adjacency** $\tilde{A}_{adp} = \text{SoftMax}(\text{ReLU}(E_1 E_2^T))$ learned from node embeddings, capturing hidden spatial dependencies with no prior graph (adaptive-only mode ≈ matches forward-diffusion on METR-LA); SOTA MAE/RMSE/MAPE on METR-LA/PEMS-BAY at lowest inference cost.
- 2026 — [[2026_EVformer_Spatio_Temporal_Decoupled_Citywide]] — Static vanilla GCN among the weakest baselines for Shenzhen citywide load (RMSE 4.41/6.65/8.10 ×10⁻², MAPE 40–49% vs EVformer 8.90% at 15 min); EVformer's ablation confirms the gap is architectural — replacing its semantic Top-K spatial attention with a static GCN costs +7.2% RMSE / +13.9% MAPE.
- 2026 — [[2026_EnergyMamba_Graph_Mamba_ASCQR]] — GCN as a learnable neural surrogate of power-flow/Kirchhoff propagation: its output feeds Mamba state transitions (conditions B/C/Δ of the selective scan) in GE-Mamba — removing it costs 36.57→47.82 MAE on Florida CBG data; the graph-conditioned architecture nets ~5% MAE gain over best baselines (see [[EnergyMamba]]).
