---
type: paper
title: "EVformer: A Spatio-Temporal Decoupled Transformer for Citywide EV Charging Load Forecasting"
authors: [Mengxin Jia, Bo Yang]
year: 2026
journal_conference: "World Electric Vehicle Journal (MDPI), Vol. 17"
doi_url: "https://doi.org/10.3390/wevj17020071"
models_used: ["[[EVformer]]", "[[Multi_Head_Attention]]", "[[Gated_Fusion]]", "[[Top-K_Spatial_Attention]]", "[[STGCN]]", "[[DCRNN]]", "[[MTGNN]]", "[[Graph_WaveNet]]", "[[Graph_Attention_Networks|GAT]]", "[[AST-GAT]]", "[[PAG]]"]
datasets_used: ["[[ST-EVCDP]]"]
features_used: ["[[Charging_Demand]]", "[[Charging_Duration]]", "[[Pile_Utilization_Rate]]", "[[Pricing_Mechanism]] (fixed/dynamic)", "[[Regional_Functional_Type]] (residential/commercial/industrial)", "[[Charging_Pile_Density]]", "[[Temperature]]", "[[Time_of_Day]]", "[[Spatio_Temporal_Embedding]]"]
forecasting_horizon: "[[Spatial_Temporal_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MAPE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: EVformer: A Spatio-Temporal Decoupled Transformer for Citywide EV Charging Load Forecasting

**Paper**: Mengxin Jia & Bo Yang (School of Computer Science, Xi'an Polytechnic University, Xi'an 710600, China). *World Electr. Veh. J.* 2026, 17, 71. https://doi.org/10.3390/wevj17020071
**Related wiki line**: [[2025_MSSTGAN_City_EV_Load]], [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]], [[2025_EV_STLLM_Spatio_Temporal_LLM]], [[2024_Physics_Informed_GAT_EV_Load]]

## 🎯 Main Objective & Contribution
- Citywide EV charging demand forecasting suffers from (i) quadratic self-attention cost in long-sequence temporal modeling, (ii) quadratic spatial attention cost w.r.t. number of stations $N$, and (iii) tightly coupled architectures lacking modular flexibility.
- Proposes **[[EVformer]]**, a **modular encoder–decoder framework that explicitly decouples temporal sequence modeling from spatial dependency learning**:
  - **Temporal module**: a *global aggregation mechanism* compresses multi-station/multi-channel time-series into a shared latent global context used as attention query → avoids $O(T^2 C)$ time–time self-attention.
  - **Spatial module**: a *dynamic semantics-aware Top-K spatial attention* combining physical graph topology with data-driven neighbor selection → reduces complexity from $O(N^2)$ to $O(K^2)$.
  - **Bidirectional Temporal Bridge (BTB)** maps historical context to future steps bidirectionally to reduce error propagation/drift in multi-horizon decoding; plus a **Multi-Horizon Decoder (MHD)** and **Gated Fusion Unit** that adaptively balances temporal vs. spatial contributions per horizon/node/time-step.
- Validated on Shenzhen dataset (18,061 public charging piles); beats VAR/Lasso/KNN/FCNN/LSTM/GCN/GAT/STGCN/DCRNN/MTGNN/GraphWaveNet/AST-GAT/PAG on MAE, RMSE, MAPE at 15/30/45 min horizons.

## 🧠 Methodology & Model Architecture
### Problem Formulation
Station set (**Eq. 3 — station set**): $\mathcal{S} = \{s_1, s_2, \ldots, s_N\}$
(**Eq. 4 — feature matrix per step**): $X_t \in \mathbb{R}^{N \times D}$ ($D$ observed features: charging indicators + external factors)
(**Eq. 5 — history window**): $X_{1:T} = \{X_1, X_2, ..., X_T\} \in \mathbb{R}^{T \times N \times D}$
(**Eq. 6 — mapping**): $\mathcal{F}(\cdot) : X_{1:T} \rightarrow Y_{1:\tau}$
(**Eq. 7 — output**): $Y_{1:\tau} \in \mathbb{R}^{\tau \times N \times D'}$ (e.g., predicted load and occupancy rate)
(**Eq. 8 — objective (L2 form)**):
$$ \min_{\mathcal{F}} \; \mathcal{L}(Y_{1:\tau}, \hat{Y}_{1:\tau}) = \frac{1}{\tau N}\sum_{t=1}^{\tau}\sum_{i=1}^{N} \left\lVert y_{i,t} - \hat{y}_{i,t} \right\rVert_2^2 $$

### Background: standard attention cost
(**Eq. 1 — scaled dot-product attention**):
$$ \text{Attn}(Q,K,V) = \text{Softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right)V $$
(**Eq. 2 — multi-head self-attention**):
$$ \text{MSA}(X) = \text{Concat}(\text{Attn}_1, \text{Attn}_2, \ldots, \text{Attn}_H)W_O $$

### Overall Framework
Pipeline: **STE embedding** → stacked **Temporal-Spatial Modeling blocks** (encoder + decoder) joined by **Bidirectional Temporal Bridge (BTB)**; each block = temporal attention + spatial attention + gated fusion; FC heads output the multi-step forecast.

### Spatio-Temporal Embedding (STE)
(**Eq. 9 — temporal embedding**): $TE_t = [\sin(\omega t), \cos(\omega t)] + e_t$ (sinusoidal + learnable $e_t$)
(**Eq. 10 — spatial embedding**): $SE = [SE_1, SE_2, \ldots, SE_N]^\top \in \mathbb{R}^{N \times D}$
(**Eq. 11 — feature fusion**): $H_t = \text{MLP}\left([X_t; TE_t; SE]\right)$
(**Eq. 12 — embedded sequence**): $H_{1:T} = [H_1, H_2, \ldots, H_T] \in \mathbb{R}^{T \times N \times D}$

### Temporal Attention — two-stage channel-first strategy
Stage 1 (**Eq. 13 — channel-wise global aggregation**, per node $v_i$ with multi-variable sequence $S_i = H^{(l-1)}_{:,i,:} \in \mathbb{R}^{T\times C}$):
$$ o^{(i)}_t = \text{Pool}\left(S_i[t,:]\right) \in \mathbb{R}^{d_g}, \quad O^{(i)} = [o^{(i)}_1, \ldots, o^{(i)}_T] \in \mathbb{R}^{T \times d_g} $$
Stage 2 (**Eq. 14 — projections with global queries**):
$$ q^{(i)}_{t_j} = W_q o^{(i)}_{t_j}, \quad k^{(i)}_t = W_k S_i[t,:], \quad v^{(i)}_t = W_v S_i[t,:] $$
(**Eq. 15 — causal cross-time scores & softmax**):
$$ u^{(k)}_{t_j,t} = \frac{\left\langle f^{(k)}_1(q^{(i)}_{t_j}), f^{(k)}_2(k^{(i)}_t)\right\rangle}{\sqrt{d}}, \qquad \alpha^{(k)}_{t_j,t} = \frac{\exp(u^{(k)}_{t_j,t})}{\sum_{t_r \in \mathcal{N}_{t_j}} \exp(u^{(k)}_{t_j,t_r})} $$
(**Eq. 16 — updated temporal representation**):
$$ h^{temp\,(l)}_{i,t_j} = \sum_{k=1}^{K}\left(\sum_{t \in \mathcal{N}_{t_j}} \alpha^{(k)}_{t_j,t} f^{(k)}_3(v^{(i)}_t)\right) $$
Causal mask (optionally sliding window) prevents future leakage; avoids $O(T^2C)$ pairwise time–time/cross-channel coupling.

### Spatial Attention — semantics-aware Top-K
Physical adjacency $A \in \mathbb{R}^{N\times N}$ from urban topology ($A_{ij}=1$ if geographically connected). Semantic embeddings $s_i \in \mathbb{R}^{d_s}$ encode land-use type, charging policy, charger density.
(**Eq. 17 — semantic similarity**):
$$ sim(i,j) = \cos(s_i, s_j) = \frac{s_i^\top s_j}{\lVert s_i \rVert \lVert s_j \rVert} $$
(**Eq. 18 — hybrid Top-K neighbor selection** within structural neighborhood $\mathcal{N}^A_i = \{v_j \mid A_{ij}=1\}$):
$$ \mathcal{N}^{top}_i = \text{TopK}\left(sim(i,j)\right), \quad j \in \mathcal{N}^A_i $$
(**Eq. 19 — attention with learnable semantic bias $b_{ij}$**):
$$ \alpha^{(k)}_{ij} = \frac{\exp\left((q_i W_q^{(k)})(k_j W_k^{(k)})^\top + b_{ij}\right)}{\sum_{m \in \mathcal{N}^{top}_i} \exp\left((q_i W_q^{(k)})(k_m W_k^{(k)})^\top + b_{im}\right)} $$
(**Eq. 20 — spatial output**):
$$ h^{spat\,(l)}_{i,t} = \sum_{k=1}^{K}\left(\sum_{j \in \mathcal{N}^{top}_i} \alpha^{(k)}_{ij} W_v^{(k)} h^{(l-1)}_{j,t}\right) $$
Complexity reduced from $O(N^2)$ to $O(K^2)$ while preserving structural + semantic relations.

### Gated Fusion Unit (within block)
(**Eq. 21 / Eq. 28 — gated fusion**):
$$ H^{(l)} = z \odot H^{(l)}_{spat} + (1-z) \odot H^{(l)}_{temp} $$
(**Eq. 22 — gating coefficient (additive form)**): $z = \sigma\left(H^{(l)}_{spat}W_{z,1} + H^{(l)}_{temp}W_{z,2} + b_z\right)$
(**Eq. 29 — gating coefficient (concatenated form)**): $z = \sigma(W_z[H^{(l)}_{spat}; H^{(l)}_{temp}] + b_z)$

### Bidirectional Temporal Bridge (BTB)
Given encoder output $H^{enc} \in \mathbb{R}^{T \times N \times C}$ and future-step embeddings $E^{query} \in \mathbb{R}^{\tau \times C}$:
(**Eq. 23 — forward mapping**): $Z^{fwd} = \text{MultiHeadAttn}\left(E^{query}, H^{enc}, H^{enc}\right) \in \mathbb{R}^{\tau \times N \times C}$
(**Eq. 24 — reverse refinement**): $H^{rev} = \text{MultiHeadAttn}\left(H^{enc}, Z^{fwd}, Z^{fwd}\right)$
(**Eq. 25 — gated fusion of both directions**):
$$ H^{bridge} = \lambda H^{rev} + (1-\lambda)H^{enc}, \qquad \lambda = \sigma\left(W[H^{enc}; Z^{fwd}] + b\right) $$

### Multi-Horizon Decoder (MHD)
Horizon split into short/mid/long-term ranges, each with an independent decoder layer:
(**Eq. 26 — per-range decode**): $Y^{(k)} = \text{Decoder}_k(H^{bridge}), \quad k \in \{1, 2, 3\}$
(**Eq. 27 — adaptive fusion**): $\hat{Y} = \sum_{k=1}^{3} \alpha_k Y^{(k)}, \quad \sum_{k=1}^{3}\alpha_k = 1$ (learnable $\alpha_k$)

### Prediction Mapping & Training Objective
(**Eq. 30 — prediction head**): $\hat{Y}_{1:\tau} = \text{MLP}(H^{(L)})$
(**Eq. 31 — MAE training loss**):
$$ \mathcal{L} = \frac{1}{\tau N}\sum_{t=1}^{\tau}\sum_{i=1}^{N} \left\lvert \hat{Y}_{t,i} - Y_{t,i} \right\rvert $$
End-to-end backpropagation over encoder + BTB + decoder + gated fusion; MAE loss chosen for outlier robustness.

## 📊 Dataset & Input Features
- **[[ST-EVCDP]]** (public mobile-app dataset of real-time public charging pile availability):
  - Location: **Shenzhen, China**; Period: **19 June – 18 July 2022** (~30 days, single season).
  - Scale: **18,061 public charging piles**; sampling interval: **minimum 5 min**.
  - URL: https://github.com/IntelligentSystemsLab/ST-EVCDP (accessed 20 January 2025).
- Spatial partitioning: city divided into **247 regional nodes**; graph with **1006 edges** built from centroid distances between regions.
- Node features: charging demand, charging duration, pile utilization rate, pricing mechanism (fixed/dynamic), regional functional type (residential/commercial/industrial), charging pile density; external factors mentioned: temperature, time of day.
- Preprocessing: chronological train/val/test split **7:1:2**; missing values via linear interpolation + forward filling (none occurred); Z-score normalization (**Eq. 32**): $\bar{x} = \frac{x-\mu}{\sigma}$.
- Settings: PyTorch 2.60, NVIDIA RTX 4090 48 GB, CUDA 12.4; Adam LR 0.001 + cosine annealing; batch 64; up to 80 epochs; early stopping patience 10; input window $T=12$ (past 1 h @ 5 min); horizons $\tau = 3, 6, 9$ (=15/30/45 min); hidden dim $d=64$; 8 attention heads; Top-$K=20$; encoder/decoder depth $N=3$ layers each.

## 📈 Performance & Results
Table 1 metrics ×10⁻² (RMSE/MAE as reported; MAPE in %):

| Model | RMSE 15m | RMSE 30m | RMSE 45m | MAE 15m | MAE 30m | MAE 45m | MAPE 15m | MAPE 30m | MAPE 45m |
|---|---|---|---|---|---|---|---|---|---|
| VAR | 5.55 | 8.51 | 11.25 | 8.11 | 10.04 | 10.98 | 53.57 | 64.02 | 65.93 |
| Lasso | 4.33 | 6.32 | 7.98 | 2.51 | 3.75 | 4.66 | 12.28 | 19.43 | 25.64 |
| KNN | 4.58 | 6.48 | 7.94 | 2.49 | 3.68 | 4.53 | 11.56 | 16.60 | 20.79 |
| FCNN | 3.37 | 5.75 | 7.45 | 1.92 | 3.26 | 4.31 | 9.74 | 15.86 | 22.37 |
| LSTM | 3.59 | 6.64 | 7.50 | 1.88 | 3.25 | 4.75 | 8.91 | 14.91 | 21.01 |
| GCN | 4.41 | 6.65 | 8.10 | 6.30 | 7.34 | 8.06 | 40.26 | 46.17 | 49.40 |
| GAT | 3.62 | 5.78 | 7.44 | 2.06 | 3.34 | 4.35 | 10.26 | 16.77 | 23.65 |
| STGCN | 3.58 | 5.57 | 6.88 | 4.93 | 5.65 | 6.60 | 31.42 | 32.59 | 43.05 |
| DCRNN | 3.75 | 5.41 | 6.75 | 2.25 | 3.35 | 4.23 | 11.32 | 16.08 | 19.94 |
| MTGNN | 3.54 | 5.39 | 6.60 | 2.21 | 3.32 | 4.11 | 11.15 | 16.02 | 18.77 |
| GraphWaveNet | 3.49 | 5.41 | 6.67 | 2.18 | 3.33 | 4.17 | 10.86 | 15.95 | 19.21 |
| AST-GAT | 3.44 | 5.38 | 6.57 | 2.05 | 3.38 | 3.96 | 9.94 | 18.04 | 17.83 |
| PAG | 3.15 | 5.15 | 6.52 | 1.88 | 3.15 | 3.94 | 9.34 | 14.57 | 17.55 |
| **EVformer** | **3.06** | **4.98** | **6.45** | **1.78** | **3.05** | **3.93** | **8.90** | **12.49** | **17.49** |

- EVformer best on ALL metrics/horizons; at 30 min beats best baseline PAG by **3.8% RMSE / 2.1% MAE / 3.1% MAPE**; ~**1–6% relative RMSE reduction** vs. graph-based SOTA at 45 min and up to **~13% improvement at 15 min** (conclusions section).

### Ablation (30-min task; RMSE / MAPE ×10⁻²)
| Interval | Full | w/o Temporal | w/o Spatial | w/o BTB | w/o Gating |
|---|---|---|---|---|---|
| 15 min | 3.06 / 8.90 | 3.32 / 10.42 | 3.28 / 10.15 | 3.18 / 9.55 | 3.14 / 9.38 |
| 30 min | 4.98 / 12.49 | 5.42 / 14.02 | 5.46 / 14.31 | 5.16 / 13.21 | 5.28 / 12.98 |
| 45 min | 6.45 / 17.49 | 7.01 / 19.82 | 6.96 / 19.55 | 6.72 / 18.63 | 6.60 / 18.15 |

- w/o Spatial (replaced by static GCN): RMSE +7.2%, MAPE +13.9% at 15 min; w/o BTB: RMSE +3.9%, MAPE +7.3%; w/o Gating (simple concat): RMSE +2.6%, MAPE +5.4%.

### Sensitivity analysis
- Top-K neighbors: $K=5$ too few; $K=20$ optimal; $K=30$ redundant neighbors degrade performance. Depth: $N=2$ underfits, $N=3$ optimal, $N=4$ marginal, $N=5$ error rises (overfitting). Optimal config (**Eq. 33**): $K=20,\; N=3$.

### Efficiency (Table 3)
| Model | Params (M) | Train Time/Epoch (s) | Inference Time/Step (ms) |
|---|---|---|---|
| STGCN | 2.3 | 35 | 4.2 |
| DCRNN | 3.8 | 52 | 6.1 |
| GMAN | 5.6 | 68 | 7.3 |
| PAG | 4.9 | 61 | 6.9 |
| **EVformer (Ours)** | 3.9 | 46 | 5.7 |

- Theoretical: temporal avoids $O(T^2 d)$ full attention; spatial reduced from $O(N^2 d)$ to $O(K^2 d)$.

## 💡 Limitations & Identified Research Gaps
- Dataset covers only ~1 month (single season, summer Shenzhen); authors state reaching ~1% RMSE would require **longer-term, multi-season datasets**, **exogenous variables (weather conditions, traffic flow)**, and finer temporal resolution.
- Future work: incorporate external data sources (weather, traffic flow); develop lighter-weight models for real-time scheduling and edge computing; extend evaluation to seasonal effects and cross-seasonal generalization.
- Evaluation limited to very short horizons (≤45 min) with 247 aggregated region nodes rather than individual stations; no probabilistic/uncertainty quantification; GMAN appears in efficiency Table 3 but not in accuracy Table 1 (baseline list inconsistency).

## 📚 BibTeX & Citation Reference
```bibtex
@article{jia2026evformer,
  title   = {EVformer: A Spatio-Temporal Decoupled Transformer for Citywide EV Charging Load Forecasting},
  author  = {Jia, Mengxin and Yang, Bo},
  journal = {World Electric Vehicle Journal},
  volume  = {17},
  number  = {2},
  pages   = {71},
  year    = {2026},
  doi     = {10.3390/wevj17020071}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — Transformer foundation (ref [6]).
- [[2021_Informer_Beyond_Efficient_Transformer]] (ref [13]) & [[2021_Autoformer_Decomposition_Transformers_AutoCorrelation]] (ref [14]) — efficient-attention line the temporal module departs from.
- [[2023_Crossformer_Cross_Dimension_Dependency]] (cited as CrossFormer, ref [7]) and [[2024_iTransformer_Inverted_Transformers_Effective_Time_Series]] (ref [8]) — recent variable-wise/channel-first Transformers motivating the global-aggregation design.
- [[2019_Graph_WaveNet_Spatial_Temporal_Modeling]] (ref [23]) and MTGNN (ref [22]) — coupled spatio-temporal graph baselines.
- STGCN (ref [15]), DCRNN (ref [16]) — classic graph-based spatio-temporal baselines; GCN [[2022_GCN_TRN_EV_Availability]]-style baselines.
- AST-GAT (ref [25]) — adaptive spatial-temporal graph attention; PAG (ref [26]) — physics-aware attention (strongest baseline).
- Wang et al., "Short-term electric vehicle charging demand prediction: A deep learning approach," Appl. Energy 2023 (ref [17]) — problem-formulation source.
- **Wiki links**: [[2025_MSSTGAN_City_EV_Load]] (city-level EV load w/ STE + gated fusion + transform attention — closest architectural sibling), [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]] (multi-graph attention EV load), [[2025_EV_STLLM_Spatio_Temporal_LLM]] (LLM-based spatio-temporal EV forecasting), [[2024_Physics_Informed_GAT_EV_Load]] (physics-informed GAT EV load).
