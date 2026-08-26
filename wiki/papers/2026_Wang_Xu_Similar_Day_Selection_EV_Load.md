---
type: paper
title: "A similar day selection framework with heterogeneous feature integration for electric vehicle charging load forecasting"
authors: [Xu Wang, Zihan Wang, Fei Ma, Rongjian Dai, Xiaoteng Zhou]
year: 2026
journal_conference: "Applied Energy"
doi_url: "https://doi.org/10.1016/j.apenergy.2026.127731"
models_used: ["[[XGBoost]]", "[[NSGA-II]]", "[[Random_Forest]]", "[[SVR]]", "[[LSTM]]", "[[LightGBM]]", "[[ShapeDTW]]", "[[Multi_Dimensional_DTW]]", "[[Adjacency_Matrix]]"]
datasets_used: ["[[UrbanEV_Dataset]]"]
features_used: ["[[Historical_Load]]", "[[Temperature]]", "[[Air_Pressure]]", "[[Sea_Level_Pressure]]", "[[Humidity]]", "[[Rainfall_Intensity]]", "[[Dew_Point]]", "[[Calendar_Features]]", "[[Holiday_Flag]]", "[[Holiday_Flag]]", "[[POI_Functional_Entropy]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[Precision]]", "[[Recall]]", "[[F1_Score]]", "[[AUC]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Similar Day Selection Framework With Heterogeneous Feature Integration for Electric Vehicle Charging Load Forecasting

> Xu Wang, Zihan Wang, Fei Ma, Rongjian Dai (corresponding, Shandong University, School of Qilu Transportation), Xiaoteng Zhou (Shandong Hi-Speed Group). Applied Energy 413 (2026) 127731. Received 6 Jan 2026; revised 9 Mar 2026; accepted 14 Mar 2026; online 1 Apr 2026. DOI: https://doi.org/10.1016/j.apenergy.2026.127731

## 🎯 Main Objective & Contribution
Improve [[Day_Ahead_Forecasting]] [[EV charging load forecasting]] by optimizing the **training-data structure** rather than the forecaster itself: select a set of historical "similar days" whose load patterns match the target day, then feed them into standard forecasting models. Key contributions:
1. **Hybrid similarity engine** combining [[ShapeDTW]] (load curves), [[Multi_Dimensional_DTW]] (weather vectors), and MAD (contextual labels) — morphological alignment that avoids "pseudo-similar" days caused by point-to-point distance sensitivity to temporal shifts.
2. **Leakage-aware XGBoost surrogate bridge**: an offline-to-online pattern-matching model that maps observable weather/context drivers to latent load-shape similarity so the high-fidelity load-similarity signal can be used **without target-day load** (zero-leakage inference).
3. **Localized adaptive mechanism via [[NSGA-II]]**: zone-specific feature weights and optimal similar-day set size per traffic zone (spatial heterogeneity of feature importance).
4. **Applicability boundaries via POI-based functional entropy**: quantifies how urban behavioral complexity limits gains — accuracy stable when entropy <0.94, significantly constrained above.

Identified gaps addressed: (i) tension between information fidelity (load-shape similarity) and operational validity (data leakage); (ii) point-to-point metrics misaligning shifted patterns; (iii) uniform feature weights ignoring spatial heterogeneity.

## 🧠 Methodology & Model Architecture
Three-stage pipeline (Sec. 2): multi-feature similarity computation → adaptive weight optimization ([[NSGA-II]]) → leakage-free [[XGBoost]] pattern matching.

**Weighted overall similarity score (Eq. 1, Weighted Similarity Score)**:
$$S_{final,e} = \vec{w} \cdot \vec{s}_e = \sum_{k \in \{load,\,weather,\,context\}} w_k \cdot s_{k,e}$$
with $\vec{s}_e = (s_{load,e}, s_{weather,e}, s_{context,e})$ normalized per-feature scores.

**(a) ShapeDTW for load** — local shape descriptors from difference sets within a 5-h neighborhood window $N(i)$, dynamic normalized histogram with $B=8$ bins (Eq. 2–3):
$$\Delta_i = \{\delta_{ij} = x^{lo}_j - x^{lo}_i \mid x^{lo}_j \in N(i)\}$$
$$SC^{lo}_i = (\hat{h}^{lo}_{i1}, \hat{h}^{lo}_{i2}, \dots, \hat{h}^{lo}_{iB}), \quad \hat{h}^{lo}_{ik} = \frac{h^{lo}_{ik}}{\sum_{k=1}^{B} h^{lo}_{ik} + \epsilon}$$
Descriptor-pair Euclidean cost (Eq. 4):
$$d^{lo}(SC^{lo}_{X,i}, SC^{lo}_{Y,j}) = \sqrt{\sum_{k=1}^{B}(\hat{h}^{lo}_{X,ik} - \hat{h}^{lo}_{Y,jk})^2}$$
DTW cumulative-cost recurrence and distance (Eq. 5–6, ShapeDTW Recurrence):
$$D^{lo}(i,j) = d(SC^{lo}_{X,i}, SC^{lo}_{Y,j}) + \min\{D^{lo}(i-1,j),\, D^{lo}(i,j-1),\, D^{lo}(i-1,j-1)\}$$
$$\text{ShapeDTW Distance} = D^{lo}(n,n)$$

**(b) Multi-dimensional DTW for weather** — 6-D weather state vector (Eq. 7), Euclidean point distance (Eq. 8), same DTW recurrence (Eq. 9–10):
$$x^{we}_i = (T_i, P^0_i, P_i, U_i, n_{RAIN,i}, T_{d,i})$$
$$d^{we}(\vec{x}^{we}_i, \vec{y}^{we}_j) = \sqrt{\sum_{k=1}^{d_{we}} (x^{we}_{ik} - y^{we}_{jk})^2}$$

**(c) Mean Absolute Deviation (MAD) for contextual features** — binary weekend/workday/holiday labels are time-rigid, so no warping (Eq. 11–13, Contextual MAD Distance):
$$x^{co} = (\tau^{wk}_i, \tau^{wo}_i, \tau^{hd}_i)$$
$$d_{co} = |x^{co}_{ik} - y^{co}_{ik}|$$
$$D_{co}(X_{context}, Y_{context}) = \frac{1}{n \cdot d_{co}} \sum_{k=1}^{d_{co}} \sum_{i=1}^{n} |x^{co}_{ik} - y^{co}_{ik}|$$

**Two-stage normalization** (Eq. 14–15): Robust Scaler then Min–Max Scaler:
$$a'_i = \frac{a_i - \text{median}(A)}{IQR}, \qquad a''_i = \frac{a'_i - \min(A')}{\max(A') - \min(A')}$$

**NSGA-II bi-objective weight optimization** (non-differentiable ranking process; Dirichlet-sampled initial population satisfying simplex constraint) (Eq. 16–18, NSGA-II Objectives):
$$\text{Minimize } f_1(\vec{w}) = \text{mean}(S_{final}) = \frac{1}{N}\sum_{j=1}^{N}(\vec{w}\cdot\vec{s}_j)$$
$$\text{Minimize } f_2(\vec{w}) = \text{std}(S_{final}) = \sqrt{\frac{1}{N}\sum_{j=1}^{N}\left((\vec{w}\cdot\vec{s}_j) - f_1(\vec{w})\right)^2}$$
$$\sum_k w_k = 1 \;\text{ and }\; w_k \geq 0,\ k \in \{load, weather, context\}$$
Optimal weights $\vec{w}^*_r$ chosen from Pareto front $F_1$ as the solution minimizing score std-dev. Candidate set (Eq. 19–20, Similar-Day Set Selection):
$$S_{final,e} = w^*_{load,r}s_{load,e} + w^*_{weather,r}s_{weather,e} + w^*_{context,r}s_{context,e}$$
$$P_{sim}(r) = \text{argK-smallest}\{S_{final}(r,e)\}$$

**Leakage-free XGBoost pattern matching (Sec. 2.3)** — since $P_{sim}$ uses target-day load, a surrogate model learns mapping from observable context/weather pair similarities to pattern-match labels. Day-pair feature vector (Eq. 21): $S_{pair}(d_t,d_h) = [S_{context}(d_t,d_h), S_{weather}(d_t,d_h)]$. Positive/negative samples (Eq. 22–23): label 1 if $d_h \in P_{sim}(d_t)$, else 0; class imbalance handled with 1:3 random undersampling. Additive tree ensemble (Eq. 24–26, XGBoost Additive Prediction):
$$\hat{y}_i = f_{XGB}(s_i) = \sum_{t=1}^{T} f_t(s_i) = \hat{y}^{(0)}_i + \sum_{t=1}^{T}(\hat{y}^{(t)}_i - \hat{y}^{(t-1)}_i), \quad f_t \in F$$
$$s_i = S_{pair}(d_t, d_h)$$
$$\hat{y}_j = \sum_{t=1}^{T} \eta f_t(S_{pair}(d_t, d_{h_j}))$$
Matching probability via sigmoid (Eq. 27) and final top-M selection (Eq. 28):
$$Score_{fused}(d_t,d_{h_j}) = P(y=1|s_j) = \sigma(\hat{y}_j) = \frac{1}{1+e^{-\hat{y}_j}}$$
$$P_1(d_t,M) = \underset{d_{h_j}\in H}{\operatorname{argmax}}^M \left(Score_{fused}(d_t, d_{h_j})\right)$$

**Similar-day set size optimization** — elbow method on the F1 curve (Eq. 34–36): baseline vector $\vec{L}=(m_\alpha - m_1, F_1(m_\alpha)-F_1(m_1))$; perpendicular distances $d_i$ computed for each point; $n^* = \operatorname*{argmax}_{m_i} d_i$, validated by first-order difference $\Delta F_1(m)$.

**POI functional entropy** (Eq. 37, Shannon Functional Entropy): $H = -\sum_{i=1}^{n} p_i \ln(p_i)$ over POI category proportions per traffic analysis zone.

## 📊 Dataset & Input Features
**Dataset: [[UrbanEV_Dataset]]** — real-world EV charging load dataset from **Shenzhen, Guangdong Province, China**, covering **275 traffic analysis zones** from **September 1, 2022 to February 28, 2023** at **hourly resolution**. Access: project GitHub repository (ref. [54]: Li H, Qu H, Tan X, You L, Zhu R, Fan W. "UrbanEV: an open benchmark dataset for urban electric vehicle charging demand prediction." *Sci Data* 2025;12). Paper-level **Data availability statement: "Data will be made available on request."** Funding: Shandong Provincial Natural Science Foundation (ZR2024LZN011 & ZR2024QG016), NSFC (52402373).

Temporal splits: full period for feature/similarity computation; Sep 1 2022–Jan 5 2023 trains XGBoost matcher (matching for subsequent 55 days); Jan 5–Feb 17 2023 forecasting training; Feb 18–28 2023 test.

Feature categories (Table 1):
- **Historical**: hourly EV charging load time series per region
- **Weather** (6 vars): temperature ($T$), station air pressure ($P_0$), sea level pressure ($P$), relative humidity ($U$), rainfall intensity ($n_{RAIN}$), dew point temperature ($T_d$); plus target-day weather forecasts in the forecasting stage
- **Contextual**: weekend / workday / holiday binary indicators, weekday index
- **Auxiliary**: POI functional shares per zone → Shannon entropy $H$

Forecasting-stage inputs (both schemes): historical load values at the forecast hours of the target day, target-day weather forecasts, calendar info; the *with similar-day* scheme adds loads at forecast hours + mean weather of the 35 optimal similar days.

## 📈 Performance & Results
**Pattern matching quality (Table 2)** — XGBoost beats KNN and LightGBM (LightGBM unstable at small samples); all metrics equal because Precision=Recall=F1 at matched set sizes:
| M | Recall/Precision/F1 | AUC |
|---|---|---|
| 15 | 0.7507 | 0.9324 |
| 25 | 0.8183 | 0.9375 |
| **35 (elbow)** | 0.8531 | 0.9348 |
| 55 | 0.9000 | 0.9365 |
| 70 | 0.9274 | 0.9441 |

AUC >0.93 across all sizes; **M*=35** chosen via elbow method and confirmed by forecasting sensitivity analysis (MAE/RMSE minimum at M=35 for LightGBM and RF; plateau/degradation beyond).

**Load forecasting (Table 3, kW, global average across zones)**:
| Model | MAE no SD / with SD / SSDS | RMSE no SD / with SD / SSDS |
|---|---|---|
| Random Forest | 55.99 / **55.01** / 61.56 | 68.07 / **67.11** / 75.60 |
| LightGBM | 58.08 / **55.47** / 79.34 | 71.54 / **68.31** / 75.60 |
| LSTM | 63.82 / **62.63** / 74.93 | 78.45 / **77.23** / 90.77 |
| SVR | 108.75 / **106.44** / 117.53 | 137.30 / **134.73** / 147.47 |

- Average error reduction ≈ **4.5%** (largest: LightGBM, ~4.5% MAE & RMSE cut); RF and LSTM ≈1.5%; SVR marginal.
- vs. **Standard Similar Day Selection (SSDS)**: proposed framework better for all models — e.g., **30.1% MAE reduction for LightGBM**; SSDS even underperforms the no-similar-day baseline (naive similarity injects noise).
- **Leakage ablation**: intentional data-leakage scenario sets the theoretical minimum; proposed leakage-free method approaches it closely — RF MAE/RMSE increase only by 3.85 kW / 4.40 kW vs. leakage upper bound.
- **Spatial polarization**: top 20% of stations improve >20.24%; bimodal split — 50.9% of stations average +19.09%, 36.7% average −26.79%. Success rate drops from 75.0% (entropy 0.69) to 58.9% (entropy 1.07). High-entropy (>0.94) bottlenecks diagnosed as mapping-fidelity breakdown ("one-to-many" driver→pattern conflict), ~400% higher selection uncertainty, and POI-entropy/feature-set representation deficit.
- Commercial share shows inverted-U relation with entropy peaking near share 0.35; lifestyle-service functions reduce entropy (stabilizing).

## 💡 Limitations & Identified Research Gaps
- Global average improvement modest (~4.5%) due to strong station-level heterogeneity; SDA has intrinsic performance limits in regions with functional entropy >0.94.
- Future work (authors): incorporate socio-demographic variables; hybrid modeling / entropy-adaptive weighting or structural adjustments for mixed-use (high-entropy) areas; validate portability across cities with diverse climates and functional characteristics.
- Methodological caveats: framework tuned/validated on one city and one year of data; similar-day features add inputs requiring re-tuning per zone; POI-based entropy may incompletely capture social dynamics (Tier 3 urban cores).

## 📚 BibTeX & Citation Reference
```bibtex
@article{wang2026similarday,
  title   = {A similar day selection framework with heterogeneous feature integration for electric vehicle charging load forecasting},
  author  = {Wang, Xu and Wang, Zihan and Ma, Fei and Dai, Rongjian and Zhou, Xiaoteng},
  journal = {Applied Energy},
  volume  = {413},
  pages   = {127731},
  year    = {2026},
  doi     = {10.1016/j.apenergy.2026.127731}
}
```

## 🔗 Key References & Citation Graph
Vault papers cited by this study:
- [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] — temperature+humidity predictors for EVCS load (ref. [21])
- [[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]] — historical-load-only RL forecasting (ref. [27])
- [[2023_Huang_MetaProbformer_EV_Load]] — MetaProbformer probabilistic charging-load forecasting (ref. [32])
- [[2024_Bampos_EV_Load_Forecasting_DAM]] — sine–cosine periodic encoding + holiday/weekend indicators (ref. [35])
- [[2025_Tian_MSSTGAN_City_EV_Load]] — also built on the [[UrbanEV_Dataset]]
- Related vault work on decomposition/selection hybrids: [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]]; TCN-LSTM with comprehensive similar-day identification (ref. [22], Tian et al., Appl. Energy 2025) — closest prior SDA baseline, not yet in vault
