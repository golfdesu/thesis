---
type: paper
title: "GCN-TRN: Efficient Transformer based Electric Vehicle Charging Demand Forecasting System"
authors: [Ruihan Zhang, Virgia Wang]
year: 2022
journal_conference: "2022 5th International Conference on Computer Science and Software Engineering (CSSE 2022), Guilin, China, pp. 527-533"
doi_url: "https://doi.org/10.1145/3569966.3570101"
models_used: ["[[GCN_TRN|GCN-TRN]]", "[[GCN]]", "[[Transformer]]", "[[GRU]]", "[[GCN-GRU]]", "[[SVR]]", "[[Historical_Average|HA]]"]
datasets_used: ["[[Dundee_EV_Charging_Dataset]]"]
features_used: ["[[Gaussian_Kernel_Adjacency|Spatial Adjacency Matrix A_ij (true path distances)]]", "[[Station_Availability|Availability p_n]]", "[[Connector_Occupancy_Time]]", "[[Station_Latitude_Longitude|Latitude/Longitude]]", "[[30_Min_Slot_Aggregation|30-min Occupancy Slots]]"]
forecasting_horizon: "[[Spatial_Temporal]]"
metrics: ["[[Accuracy_Index]]", "[[RMSE]]", "[[MAE]]", "[[R2|R² Score]]", "[[Explained_Variance_Score]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: GCN-TRN: Efficient Transformer based Electric Vehicle Charging Demand Forecasting System

## 🎯 Main Objective & Contribution
- **Core problem**: EV charging station (CS) availability forecasting must capture both **spatial relations** (correlations between neighboring stations via non-Euclidean road topology — ARIMA/SVR/KNN cannot mine spatio-temporal relations; CNN only handles Euclidean data) and **temporal dependence** (rush-hour-like charging periodicity). RNNs lose spatial info; GNNs can't process time series; Transformers aggregate poorly local/spatial information.
- **Primary contribution**: **[[GCN_TRN|GCN-TRN]]** — combines a [[GCN]] (spatial extraction from station graph $G=(V,E,A)$) with a [[Transformer]] (global-view temporal modeling, no sequential information loss) for long-term multi-step EV CS availability prediction.
- Result: >80% accuracy at 30- and 60-min horizons on the Dundee City dataset; beats all baselines including vanilla Transformer (+14.3% accuracy at 30 min).

## 🧠 Methodology & Model Architecture
- Input: historical availability $X_s = \{x_{s-L-1},\ldots,x_s\} \in \mathbb{R}^{N\times L}$ plus station locations/connectivity; output $y_{s+W}$ = predicted availability $W$ steps ahead.
- **Gaussian Kernel Spatial Adjacency Matrix** (Eq. 1) built on true path distances $\text{dist}(v_i,v_j)$ between stations:
$$A_{ij} = \begin{cases} \exp\left(-\frac{\text{dist}(v_i,v_j)^2}{\sigma^2}\right) & \text{if } \text{dist}(v_i,v_j) \le K \\ 0 & \text{otherwise} \end{cases}$$
where $\sigma$ is the distance standard deviation and $K$ the threshold filtering negligible elements.
- **Spectral graph convolution** (Eq. 2): $g_\theta * x = U g_\theta U^\top x = U g_\theta'(\Lambda)U^\top x$, with $U$ eigenvectors of normalized Laplacian $L$, $\Lambda$ diagonal eigenvalue matrix.
- **Chebyshev polynomial approximation** (Eq. 3): $g_\theta * x \approx \sum_{K=0}^{K}\theta_k T_k \tilde{\Lambda}_k = \theta_k T_k L_k$ with $\tilde{L} = L - I_N = -D^{-1/2}AD^{-1/2}$, $\tilde\Lambda = \Lambda * 2/\Lambda_{max} + I_N$.
- **First-order Chebyshev simplification** ($K=1$, $T_0(x)=1$, $T_1(x)=x$, $\theta=\theta_0=-\theta_1$) (Eq. 4):
$$g_\theta * x = \theta\left(L + D^{-\frac{1}{2}}AD^{-\frac{1}{2}}\right)x = \theta\left(\tilde{D}^{-\frac{1}{2}}\tilde{A}\tilde{D}^{-\frac{1}{2}}\right)x$$
with $\tilde{A} = A + I_N$ and $\tilde{D}_{ij} = \sum_j \tilde{A}_{ij}$ the diagonal degree matrix.
- **GCN layer output** (Eq. 5), trained until $H^N$ converges ($H^0$ = historical/current values, output $N\times d$):
$$H^{l+1} = \sigma\left(\tilde{D}^{-\frac{1}{2}}\tilde{A}\tilde{D}^{-\frac{1}{2}} H^l W^l\right)$$
- **Scaled self-attention** (Eqs. 6–7) of stacked encoder/decoder Transformer with multi-head attention + feed-forward sublayers and masked decoder attention:
$$A(q_i,K,V) = \sum_j \frac{k(q_i,k_j)}{\sum_l k(q_i,k_l)} \times v_j, \qquad k(q_i,k_j) = e^{\frac{q_i k_j^\top}{\sqrt{d}}}$$
followed by Softmax($x_i$) = $\exp(x_i)/\sum_j \exp(x_j)$ weighting; $d$ = embedding dimension. GCN output feeds the Transformer for temporal refinement.

## 📊 Dataset & Input Features
- **[[Dundee_EV_Charging_Dataset]]**: Dundee City (Scotland, UK) public EV charging stations, **February 13 – February 28, 2018** (~15 days); **2746 usage records across 23 charging stations**; records contain Connector ID, session start/end times, and station latitude/longitude.
- Preprocessing: sessions aggregated into **30-minute time slots**; per-station availability normalized to [0,1] (0 = all connectors occupied, 1 = all vacant) (Eq. 8):
$$p_n = 1 - \frac{\sum t_n}{30 \cdot M_{\text{Connector},n}}$$
where $\sum t_n$ is accumulated occupancy time and $M_{\text{Connector},n}$ the connector count at station $n$.
- No explicit data URL / DOI / GitHub link or formal data availability statement is given in the paper (Dundee City Council open-data portal is the implicit source); related open EV dataset cited in text: ACN-Data (Lee et al., ACM e-Energy 2019).

## 📈 Performance & Results
Baselines: [[Historical_Average|HA]], [[SVR]], [[GRU]], [[GCN-GRU]], vanilla [[Transformer]]. Predictions for next **30-, 60-, 90-minute** intervals (Table 1):

| Horizon | Metric | HA | SVR | GRU | GCN-GRU | Transformer | **GCN-TRN** |
|---|---|---|---|---|---|---|---|
| 30 min | Accuracy | 0.6875 | 0.7321 | 0.7652 | 0.7816 | 0.7236 | **0.8312** |
| | RMSE | 0.2013 | 0.1375 | 0.1553 | 0.1505 | 0.1801 | **0.1067** |
| | MAE | 0.1301 | 0.0952 | 0.1040 | 0.1090 | 0.1537 | **0.0856** |
| | R² | 0.5483 | 0.8088 | 0.7947 | 0.7755 | 0.7032 | **0.8549** |
| | Var | 0.5512 | 0.8093 | 0.7939 | 0.7756 | 0.7321 | **0.8476** |
| 60 min | Accuracy | 0.6692 | 0.7186 | 0.7082 | 0.7512 | 0.7057 | **0.8006** |
| | RMSE | 0.2256 | 0.1572 | 0.2012 | 0.1715 | 0.1917 | **0.1257** |
| | MAE | 0.1333 | 0.1101 | 0.1324 | 0.1272 | 0.1699 | **0.0917** |
| | R² | 0.5250 | 0.7362 | 0.6523 | 0.7084 | 0.6916 | **0.8136** |
| 90 min | Accuracy | 0.6527 | 0.7103 | 0.6503 | 0.7195 | 0.6953 | **0.7876** |
| | RMSE | 0.2302 | 0.1638 | 0.2361 | 0.1934 | 0.2003 | **0.1410** |
| | MAE | 0.1365 | 0.1301 | 0.1621 | 0.1468 | 0.1856 | **0.1042** |
| | R² | 0.4992 | 0.7326 | 0.5243 | 0.6297 | 0.6779 | **0.7657** |

- GCN-TRN vs vanilla Transformer accuracy gains: **+14.3% (30 min)**, +13.4% (60 min), +13.3% (90 min) → demonstrates necessity of GCN spatial extraction layer.
- GCN-GRU vs GRU accuracy gains: +2.1% (30 min), +6.1% (60 min), +10.6% (90 min).
- GRU beats Transformer at short horizon but loses at long horizons → temporal self-attention better long-term; GCN-TRN suffers least accuracy loss across all intervals.

## 💡 Limitations & Identified Research Gaps
- Very small dataset: single city, ~15 days, 23 stations, 2746 sessions — limited generalization evidence; no train/test split details or hyperparameters reported.
- Only availability magnitude $p_n$ modeled; no exogenous features (weather, POI/events mentioned qualitatively as factors but not included).
- Short horizons only (≤90 min); "long-term" claim modest relative to day-ahead needs.
- Metrics reported as raw numbers without variance/confidence intervals; no probabilistic/uncertainty output.
- Gap for thesis: motivates richer spatial-temporal architectures ([[GCN]] + [[Transformer]]) on larger multi-city datasets with weather/calendar covariates and longer horizons.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{zhang2022gcntrn,
  title={GCN-TRN: Efficient Transformer based Electric Vehicle Charging Demand Forecasting System},
  author={Zhang, Ruihan and Wang, Virgia},
  booktitle={Proceedings of the 2022 5th International Conference on Computer Science and Software Engineering (CSSE 2022)},
  pages={527--533},
  year={2022},
  address={Guilin, China},
  publisher={ACM},
  doi={10.1145/3569966.3570101}
}
```

## 🔗 Key References & Citation Graph
- Vault papers: [[2017_Attention_Is_All_You_Need]] (Transformer base architecture, ref [15]), [[2017_Zhang_DCRNN_Deep_Spatio_Temporal_Residual_Networks|Deep Spatio-Temporal Residual Networks]] (ref [3], citywide crowd flows)
- Cited-in-text foundations: Kipf & Welling GCN (arXiv:1609.02907, ref [14] — source of Eqs. 2–5), T-GCN traffic prediction (Zhao et al. 2019, ref [11]), GMAN graph multi-attention network (Zheng et al. 2020, ref [12]), Spatial-Temporal Transformer Networks (Xu et al. 2020, ref [13]), AST-GCN (Zhu et al. 2021, ref [9]), UK EV charging behavior statistical analysis (Quirós-Tortós et al. 2015, ref [2]), ACN-Data open EV charging dataset (Lee et al. 2019, ref [7]), EV CS availability deep learning (Luo et al. ITSC 2021, ref [16] — source of Eq. 8)
