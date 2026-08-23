---
concept: Spatial-Temporal Network Forecasting
category: forecasting-horizon
time_range: "Multi-station, multi-step"
last_updated: 2026-08-02
tags: [horizon, spatial-temporal, graph-neural-network, multi-station]
---

# 🗺️ Spatial-Temporal Network Forecasting

## Definition

Spatial-temporal EV load forecasting predicts demand across **multiple charging stations simultaneously**, exploiting both temporal patterns and spatial dependencies (geographic proximity, road network topology, shared grid feeder relationships) between stations.

## Spatial Granularity

| Level | Description | Example Papers |
|-------|-------------|----------------|
| Station-level | Forecast each station independently | [[2019_Zhu_EV_Load_Forecasting]] |
| Multi-station graph | Stations as graph nodes with adjacency edges | [[2022_Zhang_GCN_TRN_EV_Availability]], [[2025_Tian_MSSTGAN_City_EV_Load]] |
| Feeder/district | Aggregate at distribution network level | [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] |
| City-wide | All public stations in a metropolitan area | [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] |
| Regional (physics-informed) | Road network + grid topology | [[2024_Qu_Physics_Informed_GAT_EV_Load]] |

## Characteristics & Challenges

- **Spatial correlation**: Nearby stations often share demand peaks due to shared road corridors.
- **Graph construction**: Adjacency matrix design (distance-based Gaussian kernel, road network, feeder topology) significantly impacts model performance.
- **Scalability**: City-level networks may have 100s–1000s of nodes.
- **Data heterogeneity**: Different stations have different utilization rates, connector types, and service areas.
- **Price misinterpretation**: Naive models incorrectly learn positive demand-price correlations during peak pricing (spurious correlation). See [[2024_Qu_Physics_Informed_GAT_EV_Load]].

## Common Model Approaches

| Model | Spatial Component | Temporal Component | Papers |
|-------|------------------|--------------------|--------|
| GCN-TRN | Graph Convolution | Transformer | [[2022_Zhang_GCN_TRN_EV_Availability]] |
| Graph WaveNet | Adaptive-adjacency + bidirectional diffusion GCN | Gated dilated causal TCN | [[2019_Wu_Graph_WaveNet_Spatial_Temporal_Modeling]] |
| DiffSTG / UGnet | Vanilla GCN inside Unet denoiser | Masked DDPM diffusion (non-autoregressive) | [[2023_Wen_DiffSTG_Probabilistic_ST_Graph_Diffusion]] |
| PAG (Physics-Informed) | GAT + PIML | TPA-LSTM | [[2024_Qu_Physics_Informed_GAT_EV_Load]] |
| MSSTGAN | Pyramid Split GAT | Adaptive Gated Fusion | [[2025_Tian_MSSTGAN_City_EV_Load]] |
| EV-STLLM | Graph Transformer | LLM (LoRA) | [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] |
| VFL + EGAT-LSTM | Vertical Federated GAT | LSTM | [[2025_Han_Vertical_Federated_EGAT_LSTM]] |
| Multi-Branch ResTrans | ResNet (spatial) | Transformer | [[2023_Ziyabari_Multi_Branch_ResTrans_Solar]] |
| Multi-View Graph Contrastive | Mask-Attention Graph Transformer | Time encoder | [[2025_Li_Multi_View_Graph_Intrusion_Detection_EV]] |
| EVformer | Semantics-aware Top-K spatial attention (physical topology × cosine semantic similarity, $O(N^2)\to O(K^2)$) | Channel-first global-aggregation temporal attention + Bidirectional Temporal Bridge | [[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]] |

## Citing Literature

- 2019 — [[2019_Wu_Graph_WaveNet_Spatial_Temporal_Modeling]] : Foundational adaptive-adjacency STGNN — learns hidden inter-node dependencies ($\tilde{A}_{adp} = \text{SoftMax}(\text{ReLU}(E_1E_2^T))$) instead of relying on given graphs; SOTA on METR-LA/PEMS-BAY and the backbone reused by EV station GNN forecasters ([[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]], [[2025_Tian_MSSTGAN_City_EV_Load]]).
- 2023 — [[2023_Wen_DiffSTG_Probabilistic_ST_Graph_Diffusion]] : First DDPM generalized to spatio-temporal graphs — probabilistic multi-station forecasting with uncertainty bands (CRPS −4.3% to −14.3% vs TimeGrad/CSDI/MC Dropout), the machinery needed when downstream grid decisions require distributions, not point forecasts.
- 2026 — [[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]] : Decouples temporal from spatial modeling — channel-first global aggregation avoids $O(T^2C)$ time-time attention while semantic Top-K spatial attention cuts $O(N^2)\to O(K^2)$; best MAE/RMSE/MAPE at all 15/30/45-min horizons on Shenzhen ST-EVCDP (247 zones / 18,061 piles), beating GCN/GAT/STGCN/DCRNN/MTGNN/GraphWaveNet/AST-GAT/PAG.

## Hierarchical Coherence Problem

Multi-station forecasts must satisfy the summation constraint:
$$y_t^{\text{total}} = \sum_{s=1}^{S} y_t^{(s)}$$

Without explicit reconciliation, independently generated station-level forecasts violate this constraint. See:
- [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] — Ensemble methodology for hierarchical coherence
- [[2025_Zheng_Coherent_Hierarchical_EV_Load]] — PICNN + DCL for probabilistic coherent reconciliation
- [[2024_Zhou_Conformal_Prediction_DER]] — Distribution-free conformal prediction for DER hierarchies

## Key Input Features

- [[Historical_Load]] (per-station time series)
- [[Weather_Traffic]] (spatial traffic density, road conditions)
- [[Arrival_Departure_Time]] (station-level arrival distributions)
- Spatial adjacency matrix (graph topology)

## Evaluation Metrics

- [[MAE]], [[RMSE]], [[MAPE]] per station and aggregate
- [[V2G_SVE]] for downstream control quality
- Energy Score (multivariate probabilistic)

## Related Pages

- [[Short_Term_Forecasting]]
- [[Day_Ahead_Forecasting]]
