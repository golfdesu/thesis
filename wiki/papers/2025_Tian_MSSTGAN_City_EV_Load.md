---
type: paper
title: "Multi-Scale Spatial-Temporal Graph Attention Network for Charging Station Load Prediction"
authors: [Ran Tian, Jinshi Wang, Zhihui Sun, Jiarui Wu, Xin Lu, Longlong Chang]
year: 2025
journal_conference: "IEEE Access, Vol. 13, pp. 29000-29017"
doi_url: "https://doi.org/10.1109/ACCESS.2025.3541118"
models_used: ["[[MSSTGAN|Multi-Scale Spatial-Temporal Graph Attention Network (MSSTGAN)]]", "[[Pyramid_Split_Attention|Pyramid Split Attention (PSA)]]", "[[Multi_Head_Attention]]", "[[Gated_Fusion]]", "[[Transform_Attention|Transform Attention (TA)]]", "[[ST-GAT]]", "[[T-GCN]]", "[[STSGCN]]", "[[STFGNN]]", "[[Informer]]", "[[LDformer]]"]
datasets_used: ["[[Palo_Alto_EV_Charging_Dataset]]", "[[Boulder_EV_Charging_Dataset]]", "[[Dundee_EV_Charging_Dataset]]", "[[Perth_EV_Charging_Dataset]]"]
features_used: ["[[Adjacency_Matrix]] $A \\in \\mathbb{R}^{N\\times N}$", "[[Spatio_Temporal_Embedding]] $X_{STE}$", "[[Temporal_Features]] (week/day)", "[[Charging_Energy_kWh]]"]
forecasting_horizon: "[[Spatial_Temporal|City-Level Multi-Station Forecasting: Task 7-1 (7 days → 1 day) & Task 30-7 (30 days → 7 days)]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[MAPE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Multi-Scale Spatial-Temporal Graph Attention Network for Charging Station Load Prediction

## 🎯 Main Objective & Contribution
- Targets two under-addressed problems in **city-level** EV charging station network forecasting:
  1. **Low spatial resolution**: sparse data across geographically dispersed stations → solved by a **[[Pyramid_Split_Attention]] (split-pyramid)** module enabling multi-scale feature extraction.
  2. **Spatial heterogeneity**: regional demand differences (station type, surroundings, usage patterns) → solved by **Spatio-Temporal Embedding (STE)** with graph attention that learns intrinsic spatial structure.
- Proposes **[[MSSTGAN]]**: encoder–decoder architecture where encoder/decoder each stack $L$ **Pyramid Multi-Head Attention Blocks (PMAB)** joined by a **Transform Attention (TA)** layer; parallel multi-scale input branches are merged into the final forecast.
- Evaluated on **4 real-world datasets** over tasks **7-1** and **30-7**, outperforming LSTM/CNN/RNN/BiGRU, [[T-GCN]], [[STSGCN]], [[STFGNN]], ConvLSTM+BiLSTM, [[ST-GAT]], [[Informer]], [[LDformer]].

## 🧠 Methodology & Model Architecture
### Problem Formulation
Charging station network $\mathcal{G}=(V,E,A)$, signal $X \in \mathbb{R}^{T\times N\times C}$. (**Eq. 1 — forecasting map**):
$$ h(\{X_{t_1}, X_{t_2}, \cdots, X_{t_P}\}, \mathcal{G}) = \{X_{t_{P+1}}, X_{t_{P+2}}, \cdots, X_{t_{P+Q}}\} $$

### Spatio-Temporal Embedding (STE)
(**Eq. 2 — neighbor aggregation**): $v' = W\sum_{u\in\mathcal{N}(v)} h_u$
(**Eq. 3 — spatial embedding**): $X_{SE} = \text{FCs}(\text{unsqueeze}(X'_{SE}))$, dims $(P+Q)\times N\times D$
(**Eq. 4 — temporal embedding**): $X_{TE} = \text{FCs}(\text{Conv}(\text{FCs}(d)))$ for temporal features $d=(d_1,\dots,d_P,\dots,d_{P+Q})$
(**Eq. 5 — fusion**): $X_{STE} = X_{SE} + X_{TE}$, split into $STE'$ ($P\times N\times D$, encoder) and $STE''$ ($Q\times N\times D$, decoder).

### Pyramid Multi-Head Attention Block (PMAB)
**Pyramid Split (spatial) Attention**: average-pooled features split into $M$ multi-scale channels:
(**Eq. 6**): $S_i = \text{split}(\text{AveragePooling}(H^{(l-1)}))$
(**Eqs. 7–9**): $X_q = \sum_{i=1}^M \text{FCs}(S_i)\cdot W_q$, $X_k = \sum_{i=1}^M \text{FCs}(S_i)\cdot W_k$, $X_v = \sum_{i=1}^M \text{FCs}(S_i)\cdot W_v$
(**Eq. 10 — scaled dot-product spatial output**): $H_S^{(l)} = \text{softmax}\left(\frac{X_q X_k^T}{\sqrt{D}}\right) X_v$

**Temporal Multi-Head Attention**:
(**Eq. 11**): $W_i = \text{FCs}(H^{(l-1)})$, $i \in (1,\dots,c)$
(**Eq. 12**): $\text{Attention}(Q_i,K_i,V_i) = \text{softmax}\left(\frac{Q_i K_i^T}{\sqrt{D}}\right)V_i$
(**Eq. 13**): $H_T^{(l)} = \sum_{i=1}^{c} \text{Attention}(Q_i,K_i,V_i)$

**Adaptive Gated Fusion**:
(**Eq. 14**): $H^{(l)} = z\odot H_S^{(l)} + (1-z)\odot H_T^{(l)}$
(**Eq. 15**): $z = \text{Sigmoid}(H_S^l W_{z,1} + H_T^l W_{z,2} + b_z)$

### Transform Attention (TA)
Links every future time step $t_j$ to every historical step $t$ via STE projections to prevent error accumulation between encoder and decoder:
(**Eq. 16**): $m_{t_j,t}^{(k)} = \frac{f_{tr,1}^{(k)}(STE''_{v_i,t_j})\cdot f_{tr,2}^{(k)}(STE'_{v_i,t})}{\sqrt{d}}$
(**Eq. 17**): $n_{t_j,t}^{(k)} = \frac{\exp(m_{t_j,t}^{(k)})}{\sum_t \exp(m_{t_j,t}^{(k)})}$
(**Eq. 18**): $h^{(l)}_{v_i,t_j} = \|_{k=1}^{K}\left[\sum_{t=t_1}^{t_P} n_{t_j,t}^{(k)} \odot f_{tr,3}^{(k)}(h^{(l-1)}_{v_i,t})\right]$

### Encoder–Decoder Pipeline
$X \in \mathbb{R}^{P\times N\times C}$ → FC → $H^{(0)}$ → $L$ PMABs → $H^{(L)}$ → TA → decoder with $L$ PMABs → FC → predictions $Y \in \mathbb{R}^{Q\times N\times D}$; all layers output $D$ dims for residual connections; multi-scale inputs $(X, X_{P/2\dots P}, X_{P/4\dots P})$ processed in parallel then merged.
**Hyperparameters**: PyTorch 1.8.0, NVIDIA RTX 3090 (24 GB), Adam, LR 0.001, batch size 16, embedding dim $D=64$, 8 attention heads, scale divisor $n=2$, $L=1$ PMAB, 80/20 train/test split, early stopping.

### Error Metrics
(**Eqs. 19–21**): standard [[MAE]], [[RMSE]], [[MAPE]] definitions over horizon length $C \in \{1,7\}$.

## 📊 Dataset & Input Features
| Dataset | Location | Sites | Period | Resolution |
| :--- | :--- | :---: | :--- | :--- |
| [[Palo_Alto_EV_Charging_Dataset]] | Palo Alto, CA, USA | **47 stations** | 2011–2013 (3,443 timesteps) | minute-level charging energy (kWh) aggregated to daily sums per site |
| [[Boulder_EV_Charging_Dataset]] | Boulder, CO, USA | **27 public stations** (city facilities, entertainment centers, downtown parking) | Jan 2018 – Nov 2021 (1,150 timesteps) | daily energy |
| [[Dundee_EV_Charging_Dataset]] | Dundee, Scotland, UK | **33 stations** | 2017–2018 (370 timesteps) | session records (IDs, transaction IDs, dates/times, kWh) |
| [[Perth_EV_Charging_Dataset]] | Perth, Australia | **21 stations** | Jan 2016 – Dec 2019 (1,094 timesteps) | anonymized per-session data |

- Preprocessing: cleaning of duplicates/corrupted points, distribution-based imputation of missing values, Min-Max normalization to [0,1].
- Node correlation analysis (cosine similarity between all station pairs) confirmed significant spatial correlations motivating graph modeling.
- **Data availability (verbatim URLs)**:
  - Palo Alto: https://github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand/tree/main/data/Palo_Alto
  - Boulder: https://github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand/tree/main/data/Boulder
  - Dundee: https://github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand/tree/main/data/Dundee
  - Perth: https://github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand/tree/main/data/Perth
  - (All four hosted in the fbohu *Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand* repo, companion code of Hüttel et al., arXiv:2106.10940.)

## 📈 Performance & Results
### Task 7-1 (Tables 2; values as reported)
| Dataset | Model | MAE | RMSE | MAPE (%) |
| :--- | :--- | :---: | :---: | :---: |
| Palo Alto | **MSSTGAN** | **0.0117** | **0.0500** | **0.0663** |
| | ST-GAT | 0.0721 | 0.5141 | 0.4329 |
| | T-GCN | 0.1403 | 0.6966 | 0.8598 |
| | ConvLSTM+BiLSTM | 0.1898 | 0.9701 | 1.1809 |
| Boulder | **MSSTGAN** | **0.0256** | **0.0472** | **0.1274** |
| | ST-GAT | 0.0623 | 0.4177 | 0.7117 |
| Dundee | **MSSTGAN** | **0.0314** | **0.1448** | **0.6519** |
| Perth | **MSSTGAN** | **0.0286** | **0.1193** | **0.4434** |

### Task 30-7 (Table 3; values as reported)
- Palo Alto: MSSTGAN MAE **0.0332**, RMSE **0.1654**, MAPE **0.2014%** vs ST-GAT MAE 0.0697 / RMSE 0.4861 / MAPE 0.4386%.
- MSSTGAN best overall on MAPE across all four datasets on both tasks; authors concede ST-GAT was comparable or better on parts of Boulder, attributed to dataset-specific spatio-temporal characteristics.

### Ablations (Boulder + Perth, avg over both tasks)
Variants: **MSSTGAN-NM** (single-scale), **MSSTGAN-NT** (no TA), **MSSTGAN-NP** (PSA→multi-head attention), **MSSTGAN-NF** (fewer FC layers), **MSSTGAN-HGNN** (PSA→HGNN). All degrade performance; PSA replacement causes the largest MAPE drop — pyramid split attention and TA are the most critical components.

### Efficiency & Robustness
- Training time scales sub-linearly with size: Palo Alto 3,443 steps → 1,869 s; Boulder 1,150 → 1,531 s; Perth 1,094 → 1,426 s; Dundee 370 → 927 s (RTX 3090).
- Robust to Gaussian noise (minor degradation), artificial missing data (moderate), and injected outliers (largest impact yet still low error).
- Parameter study: best at LR 0.001, 1 PMAB block, scale divisor $n=2$.

## 💡 Limitations & Identified Research Gaps
- Authors explicitly acknowledge insufficient explanation of cross-dataset performance variation (esp. Boulder vs ST-GAT).
- No exogenous covariates used — future work plans integration of **weather conditions and traffic flow**.
- Computational efficiency optimization targeted for future real-time deployment.
- Daily aggregation discards intra-day load shape; transferability to other spatio-temporal domains (renewables, urban traffic) left untested.
- Thesis gap: multi-scale pyramid attention is a candidate module for handling sparse station networks; deterministic point forecasts only (no uncertainty quantification).

## 📚 BibTeX & Citation Reference
```bibtex
@article{tian2025msstgan,
  title   = {Multi-Scale Spatial-Temporal Graph Attention Network for Charging Station Load Prediction},
  author  = {Tian, Ran and Wang, Jinshi and Sun, Zhihui and Wu, Jiarui and Lu, Xin and Chang, Longlong},
  journal = {IEEE Access},
  volume  = {13},
  pages   = {29000--29017},
  year    = {2025},
  doi     = {10.1109/ACCESS.2025.3541118}
}
```

## 🔗 Key References & Citation Graph
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — Informer baseline for long-sequence forecasting (ref [33]).
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — related decomposition Transformer lineage.
- Li & Zhu (2021), *Spatial-temporal fusion graph neural networks* (AAAI) — [[STFGNN]] baseline, ref [4].
- Huang et al. (2020), *Spatial-temporal graph attention networks* (SPIE) — [[ST-GAT]] baseline, ref [31].
- Hüttel et al. (2021), arXiv:2106.10940 — [[T-GCN]] baseline and source of the four public city datasets, ref [30].
- Mohammad et al. (2023), IEEE Access — ConvLSTM/BiConvLSTM architectures baseline, ref [29].
- Tian et al. (2023), *LDformer: A parallel neural network model for long-term power forecasting* (FITEE) — prior work by same first author, ref [34].
