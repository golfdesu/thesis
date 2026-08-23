---
type: paper
title: "When Mamba Meets KAN: A Hybrid Learning Network for Electric Vehicle Charging Demand Prediction"
authors: [Meilin Hao, Qianqian Ren]
year: 2026
journal_conference: "ICASSP 2026 (IEEE International Conference on Acoustics, Speech and Signal Processing), pp. 1276-1280"
doi_url: "https://doi.org/10.1109/ICASSP55912.2026.11461366"
models_used: ["[[HyKANet]]", "[[Mamba]]", "[[Mamba-2]]", "[[KAN]]", "[[PAG]]", "[[FourierGNN]]", "[[AST-GAT]]", "[[DCRNN]]", "[[STGCN]]"]
datasets_used: ["[[Real_world_EV_charging_dataset]]"]
features_used: ["[[Historical_Demand]]", "[[Weather]]", "[[Calendar_Features]]", "[[Electricity_Price]]", "[[Dynamic_Adjacency_Matrix]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MAPE]]", "[[RAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: When Mamba Meets KAN: A Hybrid Learning Network for Electric Vehicle Charging Demand Prediction

## 🎯 Main Objective & Contribution
- EV charging demand forecasting must jointly capture (i) local + global spatial dependencies between stations, (ii) multi-scale temporal dynamics, and (iii) heterogeneous contextual signals (weather, calendar, pricing). Prior work either ignores spatial structure ([[LSTM]] with weather/calendar [4]), relies on static graphs (ASTGCN [6]), or underuses recent physics-informed graph learning and Transformer spatiotemporal architectures.
- Proposes **[[HyKANet]]** (Hybrid Mamba-KAN Network): a unified graph-temporal framework with (i) a Graph-aware MambaBlock embedding spatial topology into long-range temporal modeling, (ii) **HydraMamba**, a multi-scale routing module with three parallel Mamba branches (short/medium/long-term) plus dynamic graph learning, (iii) factor-wise external encoding with bidirectional cross-attention fusion, and (iv) a [[KAN]] decoder for expressive nonlinear demand projection.

## 🧠 Methodology & Model Architecture
- **Problem definition**: charging network as undirected graph $\mathcal{G} = (\mathcal{V}, \mathcal{E}, \mathcal{A})$ with $N$ stations; static physical adjacency $A_{\text{phy}} \in \mathbb{R}^{N\times N}$ and learned dynamic adjacency $A_{\text{dyn}}$ from node embeddings; input $X = (X_1,\dots,X_P) \in \mathbb{R}^{P\times N\times C}$, external factors $E_P = \{e^{(1)},\dots,e^{(M)}\}$, price sequence $E \in \mathbb{R}^{P\times 1}$; predict $\hat{Y} = (\hat{Y}_{P+1},\dots,\hat{Y}_{P+Q}) \in \mathbb{R}^{Q\times N\times C}$.
- **Unified structure-aware encoding**: $X_{\text{in}} = \text{Concat}[X; E]$; two complementary representations fused as $Z = H_G + H_T$ ($H_G$: graph convolution spatial, $H_T$: sequence transformation temporal).
- **Multi-scale Mamba branches**:
$$ H^k = \text{Mamba}_k(Z), \quad k \in \{s, m, l\} \tag{1} $$
each Mamba block is dual-branch: an SSM for global memory plus a multi-scale convolutional module for local temporal cues.
- **Fusion / residual aggregation** (reintroduces spatial topology):
$$ H_M = \text{MLP}(\tilde{H}_s + \tilde{H}_m + \tilde{H}_l) + H_G \tag{2} $$
- **Factor-wise external encoding**: each contextual factor projected via shared linear layer then encoded independently:
$$ h^{(i)} = \text{Encoder}(\hat{e}^{(i)}), \qquad H_E = \text{Concat}(h^{(1)}, h^{(2)}, \dots, h^{(M)}) \tag{3,4} $$
- **Bidirectional cross-attention fusion**:
$$ \bar{H}_M = \text{LayerNorm}\big(\text{MHA}(H_M, H_E, H_E) + H_M\big), \quad \bar{H}_E = \text{LayerNorm}\big(\text{MHA}(H_E, H_M, H_M) + H_E\big) \tag{5,6} $$
with adaptive gating:
$$ [\alpha, 1-\alpha] = \text{Softmax}\big(W[\bar{H}_M \parallel \bar{H}_E]\big), \qquad H_F = \alpha \cdot \bar{H}_M + (1-\alpha) \cdot \bar{H}_E \tag{7,8} $$
then $\hat{H} = \text{LayerNorm}(H_F + \text{FFN}(H_F))$.
- **KAN decoder** (Kolmogorov–Arnold Network prediction head):
$$ \hat{Y} = \text{KAN}(\hat{H}) \in \mathbb{R}^{Q \times N \times C} \tag{9} $$
- Training: end-to-end adaptive loss MSE/MAE/Smooth-L1 weighted [0.5, 0.3, 0.2]; Adam lr 0.001, weight decay 1e−5, batch 64, ≤200 epochs, gradient clipping max-norm 5, early stopping patience 20; hidden dim 128, spatiotemporal feature dim 58, external feature dim 6; Mamba state dims [8,16,48] per branch ($d_{\text{conv}}=4$, expand=2); KAN grid size 5, spline order 3; Z-score normalization.

## 📊 Dataset & Input Features
- A single unnamed **real-world EV charging dataset** (no name, station count, session count, or public URL given anywhere in the paper); split 70%/15%/15% train/validation/test.
- Sampling resolution: 5-minute intervals; input length 12 steps (1 hour); horizons 3/6/9/12 steps (15–60 min).
- Features: historical charging demand (spatiotemporal sequence, $C$ features/station), electricity price sequence, and $M$ external factors — 12 meteorological variables (weather processor projection dim 32, outlier threshold 3.0), calendar/holiday indicators, time-of-day effects.
- No data availability statement or dataset URL/DOI appears in the text.

## 📈 Performance & Results
- Best average across 15–60 min horizons: **RMSE 4.67, MAPE 15.33, RAE 17.86, MAE 2.49** (×10² units).
- Per-horizon RMSE: 2.81 (15min), 4.47 (30min), 5.26 (45min), 6.12 (60min). vs best baseline [[PAG]]: 3.02/5.16/6.52/7.21 (avg 5.48) → up to **14.8% RMSE improvement** and 17.3% over [[FourierGNN]] (5.65); **MAE reduced 12.2% on average** (2.49 vs PAG 3.33). MAPE 15.33 vs PAG 16.87.
- Baselines beaten: FCNN (6.37), LSTM (6.70), GCN (6.76), GAT (6.36), GCN-LSTM (5.81), STGCN (6.20), HSTGCN (6.39), DCRNN (5.93), AST-GAT (5.73), FourierGNN (5.65), PAG (5.48) average RMSE.
- Ablations (30-min): removing KAN decoder → MAPE 16.93 (+29.3% relative); removing external encoding → 17.76 (+35.7%); removing short-/medium-/long-term Mamba branch → 19.84/18.37/19.46 (+51.6%/40.4%/48.7%). Full model: MAPE 13.09, RMSE 4.47.
- t-SNE shows progressive feature clustering through cross-attention, multi-scale fusion, and the three Mamba branches; 90% confidence intervals tightly enclose ground truth over six forecast days and a 49-hour rollout; sensitivity optima: fusion α=0.5, KAN grid size 5, $d_{\text{state}}=16$.

## 💡 Limitations & Identified Research Gaps
- Only short-term horizons evaluated (15–60 min); extrapolation of the [[KAN]] decoder to day-ahead horizons untested.
- Dataset not named or released; no comparison against other Mamba/KAN-based forecasting models.
- Dynamic adjacency learning may scale poorly to very large station networks.
- Self-supervised/meta-learning appear only in index terms, not developed in the method.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{hao2026hykanet,
  author    = {Hao, Meilin and Ren, Qianqian},
  title     = {When {M}amba Meets {KAN}: A Hybrid Learning Network for Electric Vehicle Charging Demand Prediction},
  booktitle = {Proc. IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages     = {1276--1280},
  year      = {2026},
  doi       = {10.1109/ICASSP55912.2026.11461366}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] lineage — Transformer spatiotemporal forecasting [9]
- [[Mamba]] selective state spaces (Gu & Dao, arXiv:2312.00752) [10]; [[Mamba-2]] 2D state spaces (Gu et al., 2024) [11]
- [[KAN]] Kolmogorov-Arnold Networks (Liu et al., 2025) [12]
- [[PAG]] physics-informed attention-based graph learning for regional EV demand (Qu et al., IEEE T-ITS 2024) [8]
- AST-GAT attribute-augmented spatiotemporal GCN [21]; [[FourierGNN]] [22]; DCRNN [20]; STGCN [18]; Graph WaveNet [19]; GMAN [17]; GCN (Kipf & Welling) [15]; GAT [16]
- LSTM occupancy prediction (Ma & Faye, Energy 2022) [14]; multivariate LSTM demand forecasting (Sanami et al.) [4]
- Heterogeneous spatio-temporal GCN for EV charging demand (Wang et al., TR-C 2023) [6]; adaptive ST graph recurrent network (Wang et al., Applied Energy 2025) [7]
