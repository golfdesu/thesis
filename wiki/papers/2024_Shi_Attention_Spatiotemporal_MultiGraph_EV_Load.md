---
type: paper
title: "Load Forecasting of Electric Vehicle Charging Stations: Attention Based Spatiotemporal Multi-Graph Convolutional Networks"
authors: [Jinkai Shi, Weige Zhang, Yan Bao, David Wenzhong Gao, Zhihao Wang]
year: 2024
journal_conference: "IEEE Transactions on Smart Grid, Vol. 15, No. 3, pp. 3016-3029"
doi_url: "https://doi.org/10.1109/TSG.2023.3321116"
models_used: ["[[STMGCN]]", "[[TCN]]", "[[GCN]]", "[[Chebyshev_Graph_Convolution]]", "[[Graph_WaveNet]]", "[[STGCN]]", "[[T-GCN]]", "[[LSTM]]", "[[GRU]]", "[[CNN-LSTM]]", "[[ARIMA]]"]
datasets_used: ["[[Beijing_Fast_Charging_Dataset]]"]
features_used: ["[[Historical_Load]]", "[[Temperature]]", "[[Wind_Speed]]", "[[Humidity]]", "[[Electricity_Price]]", "[[Distance_Graph]]", "[[Similarity_Graph]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[MSE]]", "[[MAE]]", "[[MAPE]]", "[[RMSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Load Forecasting of EV Charging Stations: Attention Based Spatiotemporal Multi-Graph Convolutional Networks

## 🎯 Main Objective & Contribution
- EV charging stations couple power and transportation systems; loads are shaped by driver charging behavior plus shared traffic/weather conditions of neighboring stations — yet most prior work uses only temporal (historical load) information with fixed single-graph topologies.
- Proposes **[[STMGCN]]** to **collectively forecast charging load at every station** via three components: gated dilated causal [[TCN]], spatiotemporal attention ([[Temporal_Attention]] + [[Spatial_Attention]]), and a **multi-graph convolutional layer** fusing a physical distance graph and a virtual load-similarity graph.
- Evaluated on real-world Beijing fast-charging data (10 stations); outperforms 10 baselines including statistical, recurrent, and graph models.

## 🧠 Methodology & Model Architecture
Charging-station network modeled as undirected graph $G=(V,E,A)$, $|V|=N$; graph signal $X \in \mathbb{R}^{N\times F\times T}$ over $T$ slices; predict next $T_p$ steps $Y \in \mathbb{R}^{N\times T_p}$.

**Temporal dimension** — dilated causal convolution (**Eq. 1 – Dilated causal convolution**):
$$q(t) * x = \sum_{s=0}^{S-1} q(s)\, x(t - d_s s)$$
with filter $q \in \mathbb{R}^S$ and dilation factor $d_s$. Gating combines two convolutions (**Eq. 2 – Gated TCN**):
$$H_g = \sigma_a(\psi_1 * X) \odot \sigma_b(\psi_2 * X)$$
where $\sigma_a,\sigma_b$ = sigmoid, tanh; $\odot$ element-wise product.

**Temporal attention** (**Eq. 3 – Temporal correlation matrix**, Eq. 4 – Softmax normalization, Eq. 5 – Re-weighted input):
$$E_e = V_e \cdot \sigma_a\!\left( X_h^{r-1\,^\top} U_1 U_2 + U_3 X_h^{r-1} + b_e \right), \quad E'_{i,j} = \frac{\exp(E_{i,j})}{\sum_{j=1}^{T_{r-1}} \exp(E_{i,j})}, \quad \hat{X}_h^{r-1} = (X_1,\dots,X_{T_{r-1}})\, E'_e$$

**Spatial attention** applied on top of adjacency (**Eq. 6 – Spatial correlation matrix**, Eq. 7 – normalization):
$$S_s = V_s \cdot \sigma_a\!\left( (\hat{X}_h^{r-1} K_1)(K_2)^{^\top}(K_3 \hat{X}_h^{r-1})^\top + b_s \right), \quad S'_{i,j} = \frac{\exp(S_{i,j})}{\sum_{j=1}^{N} \exp(S_{i,j})}$$

**Spectral graph convolution** (**Eq. 8 – Graph Fourier convolution**): $g_\theta *_G x = g_\theta(U\Lambda U^\top)x = U g_\theta(\Lambda) U^\top x$ with normalized Laplacian $\mathcal{L} = I_N - D^{-1/2} A D^{-1/2}$; reduced by Chebyshev polynomials (**Eq. 9 – Chebyshev GCN**):
$$g_\theta *_G x = \sum_{k=0}^{K-1} \theta_k T_k(\tilde{\mathcal{L}})\, x, \quad \tilde{\mathcal{L}} = \tfrac{2}{\lambda_{max}}\mathcal{L} - I_N$$
with spatial attention injected per term (**Eq. 10 – Attention-weighted Chebyshev convolution**):
$$g_\theta *_G x = \sum_{k=0}^{K-1} \theta_k \left( T_k(\tilde{\mathcal{L}}) \odot S'_s \right) x, \qquad H_h^{r-1} = \sigma_c(g_\theta *_G \hat{X}_h^{r-1}) \;\text{(Eq. 11)}$$

**Multi-graph generation & fusion**: physical graph via threshold Gaussian kernel on distances (**Eq. 12 – Distance matrix**):
$$a^d_{i,j} = \begin{cases} \exp(-d_{i,j}^2/\sigma_D^2), & i \neq j \text{ and } d_{i,j} \geq \epsilon_d \\ 0, & i=j \text{ or } d_{i,j} < \epsilon_d \end{cases}$$
virtual graph from load-pattern similarity (**Eq. 13 – Euclidean load distance**, Eq. 14 – Similarity matrix):
$$e^s_{i,j} = \sqrt{\sum_{t=1}^{T}(x_{t,i}-x_{t,j})^2}, \qquad a^s_{i,j} = \exp(-\sigma_S \times e^s_{i,j})$$
Fused by softmax-normalized learnable weights (**Eq. 17–18 – Multi-graph fusion**):
$$W'_d, W'_s = \sigma_d(W_d, W_s), \qquad Y_f^{r-1} = W'_d \odot H_{hd}^{r-1} + W'_s \odot H_{hs}^{r-1}$$
Framework: input layer → stacked ST-blocks (gated TCN → temporal/spatial attention → dual-graph Chebyshev GCN) with skip + residual connections → output layer (concatenation, two linear convolutions + ReLU). Trained with [[Adam]], lr 0.0001, batch 32, 200 epochs; 4-layer TCN kernel/dilation {2,1},{2,2},{2,4},{2,8}; Chebyshev degree K=3; RTX 3060 Ti, PyTorch.

## 📊 Dataset & Input Features
- **[[Beijing_Fast_Charging_Dataset]]**: real-world charging load from **10 fast DC charging stations in Beijing, China**, Jan 25 2022 – Apr 30 2022; charging power recorded every **15 min** (96 points/day/station); nearest inter-station distance 4.69 km. Split: last 63 days train / following 18 days validation / remainder test; data cleaned and normalized; missing values/outliers filled by linear interpolation.
- Input features selected via maximal information coefficient (MIC, threshold 0.3; **Eq. 19–20 – Mutual information & MIC**): historical charging power, temperature, wind speed, humidity, electricity price (MIC(load, price)=0.92, MIC(load, time)=0.84).
- Output: charging power of each station at next time step.
- Data availability: no public URL/DOI given in the paper; dataset described only as "charging load dataset from Beijing, China" (Section IV-A).

## 📈 Performance & Results
- Overall test set: **STMGCN MAE = 53.287 kW, RMSE = 78.831 kW** (best); MAE reduced ~2–20 kW vs all baselines. ARIMA best statistical baseline at MAE 72.236 kW; HA unacceptable.
- Per-station: best at station NO. 6 (regular loads): MAE 29.438 kW, RMSE 45.249 kW; hardest at station NO. 10 (highest total load), ~103 kW MAE gap vs others.
- Multistep: STMGCN MAE 53.287 / 54.519 / 55.834 kW at 15 min / 1 h / 2 h vs CNN-LSTM 60.061 / 62.114 / 63.715 kW — slowest degradation with horizon; ARIMA drops dramatically.
- Ablations (MAE/RMSE kW): full STMGCN 53.287/78.831 < noMG (identity graph) 55.056/80.791 < noSA 53.838 < noTA 56.629 < noSTA 57.165 < noAG (TCN-only) 61.145/90.681 → both graphs matter; temporal attention contributes more than spatial.
- Baselines compared: HA, ARIMA, FNN, LSTM, GRU, TCN, CNN-LSTM, T-GCN, STGCN, Graph WaveNet.

## 💡 Limitations & Identified Research Gaps
- Model assumes location correlations exist in historical load series; cannot capture dependencies between distant stations whose loads are uncorrelated.
- Robustness to missing/incorrect values (common in charging datasets) not addressed — flagged as future work.
- Hyperparameters manually tuned; small network scale (10 stations); no probabilistic/uncertainty output.
- Traffic-flow information motivates the coupling but is not an explicit input feature.

## 📚 BibTeX & Citation Reference
```bibtex
@article{shi2024stmgcn,
  title   = {Load Forecasting of Electric Vehicle Charging Stations: Attention Based Spatiotemporal Multi-Graph Convolutional Networks},
  author  = {Shi, Jinkai and Zhang, Weige and Bao, Yan and Gao, David Wenzhong and Wang, Zhihao},
  journal = {IEEE Transactions on Smart Grid},
  volume  = {15},
  number  = {3},
  pages   = {3016--3029},
  year    = {2024},
  doi     = {10.1109/TSG.2023.3321116}
}
```

## 🔗 Key References & Citation Graph
- [[2018_Bai_Empirical_TCN_Sequence_Modeling]] — TCN backbone for temporal extraction (via dilated convolutions, Yu & Koltun 2015)
- [[2017_Attention_Is_All_You_Need]] — attention paradigm underlying the spatiotemporal attention modules (ASTGCN, Guo et al. AAAI 2019)
- [[2022_Zhang_GCN_TRN_EV_Availability]] — related GNN use for EV charging-station operating status prediction
- [[2021_Zhang_Probabilistic_Queuing_EV_Load]] — cited deep probabilistic EV charging load forecasting with queuing model (Zhang et al.)
- [[2024_Qu_Physics_Informed_GAT_EV_Load]] — related graph-attention approach to regional EV charging demand
- [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] — multi-station probabilistic EV load forecasting context (Hüttel et al. T-GCN cited within)
