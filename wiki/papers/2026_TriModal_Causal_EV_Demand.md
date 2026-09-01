---
type: paper
title: "Tri-modal causal learning for forecasting EV charging demand"
authors: [Xiaoping Wang, Qianqian Ren, Hezhe Wang, Zhijuan Li]
year: 2026
journal_conference: "Pattern Recognition Letters, Vol. 206, pp. 8–14 (Elsevier)"
doi_url: "https://doi.org/10.1016/j.patrec.2026.04.028"
models_used: ["[[TriCast]]", "[[SAGE_Semantic_Aware_Graph_Encoder]]", "[[TACT_Causal_Temporal_Alignment]]", "[[Price_Elasticity_Modulator]]", "[[Causal_Dilated_Convolution]]", "[[Set_Transformer_Induced_Attention]]"]
datasets_used: ["[[UrbanEV_Dataset]]"]
features_used: ["[[Station_Occupancy]]", "[[Electricity_Tariff]]", "[[Traffic_Zone_Adjacency]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MAPE]]", "[[RAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Tri-modal causal learning for forecasting EV charging demand

> Xiaoping Wang, Qianqian Ren*, Hezhe Wang*, Zhijuan Li — Dept. of Computer Science and Technology, Heilongjiang University, Harbin 150080, China. Editor: Yonghuai Liu. Received 1 Nov 2025; revised 2 Feb 2026; accepted 24 Apr 2026; online 30 Apr 2026. © 2026 Elsevier B.V.

## 🎯 Main Objective & Contribution

Proposes **TriCast**, a tri-modal forecasting framework that jointly models **spatial, temporal, and economic modalities** for urban [[EV_Charging_Demand|EV charging demand]] prediction. Targets three core deficiencies of prior methods:

1. **Static spatial graphs** based only on geographic proximity miss latent functional similarity between regions → poor generalization to unseen zones.
2. **Temporal information leakage** in attention-based models (future inputs influencing current predictions) → instability under distribution shift.
3. **Shallow economic modeling** — electricity pricing treated as auxiliary input rather than a core modeling signal.

Contributions: (1) unified tri-modal framework integrating spatial semantics + temporal causality + economic responsiveness; (2) three purpose-built modules — SAGE (generalization), TACT (temporal robustness), PEM (behavioral elasticity); (3) experiments on a large-scale dataset with >18,000 charging stations showing up to **9.8 % MAPE reduction** over 16 baselines with robustness across cities/pricing regimes.

## 🧠 Methodology & Model Architecture

**Problem definition**: charging network as graph $G=(V,E,A)$, $N=|V|$ stations, adjacency $A \in \mathbb{R}^{N\times N}$; node features $x_{t,i} \in \mathbb{R}^C$ (occupancy, electricity pricing, contextual signals). Given historical window $X = (X_{t-P+1},\dots,X_t) \in \mathbb{R}^{P\times N\times C}$, predict $Y = (X_{t+1},\dots,X_{t+Q}) \in \mathbb{R}^{Q\times N\times C}$.

### Module 1: Price Elasticity Modulator (PEM)
- **L-step random-walk propagation** (Eq. 1, Normalized Transition Matrix):
$$P = \text{RandomWalk}(A,L), \qquad P_{i,j} = \frac{P_{i,j}}{\sum_k P_{i,k}}$$
- **Occupancy feature enhancement via gated attention** (Eq. 2):
$$X^*_t = X_t + \sigma(W_X P X_t) \odot f_X(P X_t)$$
with gating $\sigma(\cdot)$ and learnable transform $f_X(\cdot)$.
- **Price spatial smoothing** (Eq. 3): $\tilde{E}_t = P E_t$, where $E_t \in \mathbb{R}^N$ is the price vector.
- **Behavior-aware modulated price** (Eq. 4):
$$E^*_t = E_t \odot \left(1 + \sigma(W_E \tilde{E}_t) \odot f_E(\tilde{E}_t)\right)$$
- **Enhanced sequences** (Eq. 5): $X^* = (X^*_{t-P+1},\dots,X^*_t)$, $E^* = (E^*_{t-P+1},\dots,E^*_t)$ forwarded to SAGE and TACT.

### Module 2: Semantic-Aware Graph Encoder (SAGE)
- **Multimodal encoding** (Eq. 6): $H_0 = [X^*_t \| E^*_t] \in \mathbb{R}^{N\times(d+1)}$.
- **Local pattern extraction** (Eq. 7): $H_{conv} = \text{Conv2D}(H_0)$.
- **Semantic inducing points** (Eq. 8): $I = \text{TopK}(\text{GCN}(X^*_t, A)) \in \mathbb{R}^{m\times d'}$, $m \ll N$ — semantic anchors for graph-level abstraction.
- **Induced attention** (two-stage, following Set Transformer):
  - Stage 1 (Eq. 9): $H_1 = \text{MAB}_1(I, H_{conv})$
  - Stage 2 (Eq. 10): $\hat{H}_1 = \text{MAB}_2(H_{conv}, H_1)$
- **Cascaded refinement** (Eqs. 11–12): $Z^{(1)} = \sigma(W^{(1)}_{trans}\hat{H}_1 + b^{(1)})$, $Z^{(2)} = \sigma(W^{(2)}_{trans}\hat{H}_2 + b^{(2)})$.
- **Hierarchical residual fusion** (Eq. 13):
$$Z_{out} = (1-\alpha) Z^{(2)} + \alpha[(1-\alpha)Z^{(1)} + \alpha H_{conv}]$$
where $\alpha \in [0,1]$ controls fusion strength.

### Module 3: Temporal Alignment with Causal Transformation (TACT)
- **Dilated causal convolution** (Eq. 14):
$$H^{(l)} = \text{CausalConv1D}(Z^{(l-1)}; k, d_l), \qquad d_l = 2^l$$
causal padding ensures outputs at time $t$ depend only on inputs $\le t$.
- **Price projection** (Eq. 15): $E_t = \text{ReLU}(W_{ep} E + b_{ep}) \in \mathbb{R}^{P\times N\times d}$ from historical price sequence $E \in \mathbb{R}^{P\times N}$.
- **Price-aware gated modulation** (Eq. 16):
$$\hat{H}^{(l)} = H^{(l)} \odot (1 + \tanh(E_t))$$
- **Gated residual block** (Eq. 17):
$$Z^{(l)} = Z^{(l-1)} + \text{Dropout}\left(\tanh(\hat{H}^{(l)}) \odot \sigma(\hat{H}^{(l)})\right)$$
- **Temporal encoding** (Eq. 18): $H_{TACT} = Z^{(L)} \in \mathbb{R}^{P\times N\times d}$.
- **Temporal average pooling** (Eqs. 19–20): $\tilde{Z}_t = \frac{1}{P}\sum_{p=1}^{P} H_{TACT}[p] \in \mathbb{R}^{N\times d}$.

### Prediction head & objective
- **MLP forecasting head** (Eq. 21): $\hat{Y} = \text{MLP}(\tilde{Z}_t) \in \mathbb{R}^{N\times Q\times C}$.
- **Training loss — MSE** (Eq. 22):
$$\mathcal{L} = \frac{1}{BN}\sum_{b=1}^{B}\sum_{i=1}^{N}\left(\hat{Y}_{b,i} - Y_{b,i}\right)^2$$

**Implementation**: PyTorch on Intel i7-11700 + NVIDIA RTX 3090; Adam optimizer (lr 0.001, weight decay $1\times10^{-5}$); batch size 64; up to 1200 epochs; gradient clipping max norm 5; early stopping patience 20; input sequence length 12 (1 h); horizons of 3–12 steps (15–60 min). Results averaged over five runs.

## 📊 Dataset & Input Features

- **[[UrbanEV_Dataset]]** (Shenzhen subset) — large-scale open benchmark for EV charging demand prediction (Li H., Qu H., Tan X., You L., Zhu R., Fan W., "UrbanEV: an open benchmark dataset for urban electric vehicle charging demand prediction", *Scientific Data* 12(1):523, 2025 — ref [10]; no direct URL/DOI given in the paper text).
  - **Location**: Shenzhen, China; **scale**: >18,000 public charging stations across **247 traffic zones**; **period**: 30 days (**June 19 – July 18, 2022**); **resolution**: **5-minute interval** charging occupancy (proxy for demand) and electricity pricing.
  - Pricing regime: 57 zones adopt dynamic pricing, the rest fixed rates.
  - **Graph construction**: 247 nodes, **1006 edges** based on inter-zone connectivity from Shenzhen's Sixth Residential Travel Survey [11].
  - **Split** (following Qu et al./[1]): chronological 60 % train / 20 % validation / 20 % test.
  - Data availability: *"Data will be made available on request"*; source code *"available from the authors upon reasonable request."*

Features: station/zone occupancy, electricity price (dynamic vs fixed), zone-level connectivity graph.

## 📈 Performance & Results

Evaluated at horizons 15/30/45/60 min (3/6/9/12 steps) vs **16 baselines**: traditional — VAR, Lasso, KNN; deep learning — FCNN, LSTM, GCN, GAT, GCN-LSTM, STGCN, HSTGCN, DCRNN, AST-GAT, FourierGNN, PAG, CityEVCP, PIAST. Metrics reported ×10² (Table 1):

| Model | RMSE avg | MAPE avg | MAE avg |
|---|---|---|---|
| VAR | 9.44 | 62.64 | 9.99 |
| Lasso | 7.00 | 22.23 | 4.15 |
| KNN | 7.02 | 18.40 | 4.02 |
| FCNN | 6.37 | 19.08 | 3.72 |
| LSTM | 6.70 | 17.25 | 4.06 |
| GCN-LSTM | 5.81 | 19.32 | 4.87 |
| STGCN | 6.20 | 39.17 | 6.14 |
| DCRNN | 5.93 | 18.00 | 3.75 |
| AST-GAT | 5.73 | 18.82 | 3.49 |
| FourierGNN | 5.32 | 18.37 | 2.93 |
| PAG | 5.56 | 18.20 | 3.00 |
| CityEVCP | 4.83 | 17.26 | 2.86 |
| PIAST | 4.91 | 15.79 | 2.54 |
| **TriCast** | **4.71** | **15.41** | **2.53** |

Horizon detail (RMSE 15/30/45/60 min): TriCast **2.92 / 4.39 / 5.37 / 6.26** vs PIAST 3.01 / 4.33 / 5.60 / 6.49 and CityEVCP 3.25 / 4.52 / 5.37 / 6.18. Improvements vs best prior: RMSE +2.99 % (15 min), +2.48 % avg; MAPE +9.80 % (15 min), +2.41 % avg; RAE avg 18.19 (+0.82 %); MAE avg 2.53 (+0.39 %). TriCast is slightly behind at some individual cells (e.g., −1.38 % RMSE at 30 min, −2.98 % MAPE at 60 min vs PIAST/CityEVCP).

**Ablation (MAE 15/30/45/60; MAPE 15/30/45/60)**: Full TriCast 1.37/2.25/2.90/3.51 and 7.82/12.86/17.66/22.49; w/o PEM 1.40/…, MAPE 8.01/13.09/…; w/o SAGE-Attn 1.48/2.37/3.01/3.60, MAPE 8.22/13.58/18.20/22.71 (**largest drop** → induced attention most critical); w/o TACT (GRU replacement) 1.44/2.29/…, MAPE 8.85/13.32/….

**Robustness**: Gaussian noise injection (1 %, 5 %, 10 %) into occupancy/price at inference — stable under mild noise, moderate degradation at higher levels; low std across runs. **Parameter sensitivity**: stable across dropout rates 0.2–0.7; metrics improve consistently up to ~1000 training epochs. **Statistical significance**: paired t-tests, p < .01 vs PAG and FourierGNN (10-run variance analysis). **Qualitative**: tight zero-centered residuals vs wider LSTM/GCN-LSTM spreads; predicted occupancy covers realistic range 0.0–0.4 without mode collapse; accurate tracking of sharp CBD-node peaks (nodes 217, 223) and step transitions in Non-CBD nodes (124, 235).

## 💡 Limitations & Identified Research Gaps

- Short 30-day record and single city (Shenzhen) in the main experiments; cross-city transfer claimed as design motivation ("transferable") but quantitative cross-city results are limited to robustness/stability claims under distribution shift.
- Occupancy used as a proxy for demand rather than measured energy.
- Deterministic MSE-trained point forecasts only — no probabilistic/interval outputs.
- Only 57/247 zones have dynamic pricing; elasticity learning is constrained by sparse dynamic-price coverage.
- Conclusion text inconsistently states "outperforms 14 baselines" vs 16 baselines compared in Section 3.2/Table 1.
- Data/code availability by request only — reproducibility depends on authors.

## 📚 BibTeX & Citation Reference
```bibtex
@article{Wang2026TriCast,
  author  = {Wang, Xiaoping and Ren, Qianqian and Wang, Hezhe and Li, Zhijuan},
  title   = {Tri-modal causal learning for forecasting EV charging demand},
  journal = {Pattern Recognition Letters},
  volume  = {206},
  pages   = {8--14},
  year    = {2026},
  doi     = {10.1016/j.patrec.2026.04.028}
}
```

## 🔗 Key References & Citation Graph

- [[2025_EV_STLLM_Spatio_Temporal_LLM]] — other vault paper using the [[UrbanEV_Dataset]] benchmark.
- [[2024_Physics_Informed_GAT_EV_Load]] — PAG baseline (ref [1], physics-informed attention-based graph learning for regional EV charging demand).
- [[2026_Mamba_KAN_HyKANet_EV]] — shares baselines FourierGNN, AST-GAT, DCRNN, STGCN, PAG.
- [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]] — related spatiotemporal graph EV load forecasting lineage.
- [[2025_MSSTGAN_City_EV_Load]] — citywide EV charging demand GNN with spatial-temporal attention (related CityEVCP-style line, ref [6] Kuang et al.).
- [[2019_EV_Load_Forecasting]] — earlier LSTM-based EV charging load forecasting (sequence-model baseline context).
