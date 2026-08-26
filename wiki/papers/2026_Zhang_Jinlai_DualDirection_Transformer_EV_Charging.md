---
type: paper
title: "Dynamic charging load prediction using uncertainty-scale dual-direction transformer"
authors: [Jinlai Zhang, Liuqi Tan, Hancheng Xie, Kai Gao, Wenzheng Liu, Jie Su, Wenhao Zhu, Lin Hu]
year: 2026
journal_conference: "Sustainable Energy, Grids and Networks"
doi_url: "https://doi.org/10.1016/j.segan.2026.102428"
models_used: ["[[USDT]]", "[[SMAN]]", "[[DDI]]", "[[Informer]]", "[[Probformer]]", "[[Transformer]]", "[[DeepAR]]", "[[LSTM]]", "[[ARIMA]]", "[[Prophet]]", "[[SVR]]", "[[FEDM]]", "[[PICCN]]"]
datasets_used: ["[[EVnetNL_ElaadNL_Dataset]]", "[[Perth_EV_Charging_Dataset]]", "[[Boulder_EV_Charging_Dataset]]", "[[Palo_Alto_EV_Charging_Dataset]]"]
features_used: ["[[Charging_Load_Sequence]]", "[[Temporal_Feature_Encoding]]", "[[Calendar_Covariates]]"]
forecasting_horizon: "[[Long_Term]]"
metrics: ["[[RMSE]]", "[[MSE]]", "[[MAE]]", "[[R2_Score]]", "[[ACE]]", "[[CRPS]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Dynamic charging load prediction using uncertainty-scale dual-direction transformer

## 🎯 Main Objective & Contribution
- **Problem:** Conventional EV charging load forecasting struggles with (i) intricate temporal dependencies and spatial characteristics and (ii) uncertainty in load fluctuations.
- **Proposal:** **USDT — Uncertainty-Scale Dual-Direction Transformer**, a probabilistic charging-load forecasting model on an [[Informer]]/[[Probformer]] backbone with two new modules:
	- **SMAN (Scalable Multi-Scale Linear Attention Network):** captures load variation across multiple temporal/spatial scales using convolutional projections + query sparsity.
	- **DDI (Dual-Direction Interaction module):** bidirectional attention (horizontal = cross-station patterns, vertical = within-station temporal dynamics) for local spatial relationships.
- Probabilistic output $\mathcal{N}(\mu_t,\sigma_t^2)$ per step; **>10% improvement** in [[RMSE]] on [[EVnetNL_ElaadNL_Dataset]] vs existing methods.

## 🧠 Methodology & Model Architecture
### Preliminaries
$N$ interrelated univariate series; conditioning range Seq$(1,t_0)$, prediction range Seq$(t_0+1,t_0+\tau)$; known covariate matrix $X$ (time-independent e.g. station IDs and/or time-dependent e.g. month).

**Historical sequence (Eq. 3.1):**
$$y_{i,1:t_0} = \begin{cases} y_{i,1} & t=1 \\ y_{i,2} & t=2 \\ \vdots & \\ y_{i,t_0} & t=t_0 \end{cases} \tag{3.1}$$

**Covariate matrix (Eq. 3.2):**
$$X=\begin{pmatrix} X_1 \\ X_2 \\ \vdots \\ X_{t_0+\tau} \end{pmatrix} \tag{3.2}$$

**Q/K/V projection (Eq. 3.3):**
$$Q = XW_Q, \quad K = XW_K, \quad V = XW_V \tag{3.3}$$

**Scaled dot-product attention (Eq. 3.4):**
$$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right)V \tag{3.4}$$

**Sinusoidal positional encoding (Eq. 3.5):**
$$PE(pos, 2i) = \sin\!\left(\frac{pos}{10{,}000^{2i/d_{model}}}\right), \qquad PE(pos, 2i+1) = \cos\!\left(\frac{pos}{10{,}000^{2i/d_{model}}}\right) \tag{3.5}$$

**Sequence likelihood loss (Eq. 3.6):**
$$\mathcal{L} = -\sum_{t=1}^{m} \log P(y_t \mid y_{<t}, X) \tag{3.6}$$

### USDT framework
Encoder: embeddings → SMAN → DDI → MHPSA → SAD → MHPSA. Decoder: truncated history + target sequences → MMHPSA + MHA → fully connected layer → predictive PDF → sampling. MHPSA/SAD/MMHPSA/MHA/FCL/PDF modules inherited from [[Informer]] [34] and [[Probformer]]/MetaProbformer [26].

### SMAN equations
Convolutional Q/K/V generation embedding spatial-temporal neighborhood structure (Eq. 4.1):
$$Q = \text{Conv}_Q(X), \quad K = \text{Conv}_K(X), \quad V = \text{Conv}_V(X) \tag{4.1}$$
Multi-scale processing captures fast spikes + slow diurnal/weekly cycles. Query sparsity via KL-divergence-style max–mean gap (Eq. 4.2):
$$S(q_l, K) = \max_j \left\{ q_l k_j^\top \right\} - \frac{1}{L_K}\sum_{j=1}^{L_K} q_l k_j^\top \tag{4.2}$$
where $q_l$, $k_j$ are rows of $Q$/$K$, $L_K$ = key length; only "active" (top-scoring) queries get full attention. Algorithm 1 SMAN pipeline: 2DConv×2 → ReLU → BatchNorm → Multi-scale → ReLuLinearAttention → LayerNorm → ReLu6.

### DDI equations
Horizontal (cross-station co-movement) attention (Eq. 4.3):
$$\text{Output}_h = \text{softmax}\!\left(\frac{Q_h K_h^\top}{\sqrt{d_k}}\right)V_h \tag{4.3}$$
Vertical (within-station temporal) attention (Eq. 4.4):
$$\text{Output}_v = \text{softmax}\!\left(\frac{Q_v K_v^\top}{\sqrt{d_k}}\right)V_v \tag{4.4}$$
Residual fusion preserving station-specific baselines (Eq. 4.5):
$$\text{Final Output} = X + \text{Output}_h + \text{Output}_v \tag{4.5}$$

### Training objective
Future load assumed Gaussian $\mathcal{N}(\mu_t,\sigma_t^2)$; decoder FCL bifurcates into mean head $\mu_t$ and std head $\sigma_t$ (Softplus); optimized with **Negative Log-Likelihood (NLL)** loss instead of MSE; intervals from standard-normal quantiles of $(\mu,\sigma)$. *(Note: Table 1 lists "Loss function: MSE" while §5.2 states NLL optimization — internal inconsistency in the text.)*

### Configuration (Table 1)
Input length 96 h, label length 48, prediction length 1 (hourly steps), batch size 32, Adam lr $1\times10^{-4}$, weight decay $1\times10^{-4}$, cosine schedule w/ 5 warmup epochs, grad-norm clip 1.0, 200 epochs, 2 encoder / 1 decoder layers, embedding dim 512, FF dim 2048, dropout 0.05, 8 heads, GELU, early stopping patience 8, task batch 2 / data batch 32, Xavier-uniform init, LayerNorm ε $10^{-5}$, sinusoidal positional encodings. Random search space: layers 1–6, dims 64–2048, heads {1,2,4,8}, dropout 0–0.8, GELU/ReLU, data batch 8–256. Environment: Ubuntu 18.04 LTS, Xeon Gold 6140, Tesla P40, Python 3.8, PyTorch 1.9.1; Python/NumPy/PyTorch seeds fixed at 1995.

## 📊 Dataset & Input Features
Four public charging-session datasets (start/end time + total energy per session), aggregated at strict hourly granularity with temporal features:
- **[[EVnetNL_ElaadNL_Dataset]]** — Netherlands, multiple stations, 12 months, 8760 points. URL: https://platform.elaad.io/analyses/ElaadNL_opendata.php
- **[[Perth_EV_Charging_Dataset]]** — Perth, UK, 4 months, 2953 points. URL: https://data.pkc.gov.uk/dataset/ev-charging-data
- **[[Boulder_EV_Charging_Dataset]]** — Boulder, Colorado, USA, 31 months, 22,632 points. URL: https://open-data.bouldercolorado.gov/datasets/
- **[[Palo_Alto_EV_Charging_Dataset]] (PALO)** — California, USA, ~5 months, 3114 points. URL: https://data.cityofpaloalto.org/dataviews/241685/ELECT-VEHIC-CHARG-STATI-USAGE/
- **Data availability statement:** "Data will be made available upon request."
- Split: chronological 60/20/20 train/validation/test, same global windows across stations, sliding windows within subsets only (input window 96, label window 48). Preprocessing: DatetimeIndex ordering, z-score normalization on training-split statistics only; no imputation/outlier clipping. Univariate setting: load is the sole signal, augmented with cyclical/discrete calendar time encodings as exogenous marks for encoder and decoder.

## 📈 Performance & Results
### Main results (point metrics from mean $\mu_t$)
**EVnetNL (Table 2):**

| Method | RMSE | MSE | MAE |
|---|---|---|---|
| ARIMA | 18.887 | 356.733 | 15.043 |
| LSTM | 13.448 | 180.861 | 10.355 |
| SVR | 12.070 | 145.693 | 9.258 |
| Prophet | 26.310 | 692.129 | 21.177 |
| DeepAR | 29.675 | 880.614 | 25.822 |
| Transformer | 12.264 | 150.403 | 8.862 |
| Informer | 9.866 | 97.734 | 6.733 |
| Probformer | 10.212 | 104.285 | 6.896 |
| FEDM | 12.895 | 166.267 | 10.511 |
| PICCN | 20.842 | 434.415 | 16.943 |
| **USDT** | **8.781** | **77.103** | **6.097** |

vs Informer/Probformer: RMSE −10.99%/−14.01%, MSE −21.11%/−26.07%, MAE −9.45%/−11.59%.

**Perth (Table 3):** USDT RMSE **13.837**, MSE **191.457**, MAE **9.042** vs Informer 14.319/205.021/9.189 and Probformer 14.176/200.959/9.245 (RMSE −3.37%/−2.39%; MSE −6.62%/−4.73%; MAE −1.60%/−2.20%). Other baselines: ARIMA 22.110/488.852/17.109; LSTM 19.202/368.717/15.855; SVR 15.560/242.115/14.083; Prophet 23.843/568.493/28.298; DeepAR 24.170/584.197/25.591; Transformer 23.967/574.417/16.534; FEDM 19.319/373.231/14.878; PICCN 20.610/424.802/16.447.

### Statistical robustness (5 seeds)
EVnetNL RMSE: USDT 9.222 ± 0.181 vs Informer 12.095 ± 0.713; Perth: USDT 12.987 ± 0.083 vs Informer 13.386 ± 0.174. One-sided two-sample t-tests: p < 0.01 (superiority significant at 1% level).

### Cross-domain zero-shot transfer (bi-directional)
| Target | Method | In-domain RMSE | Cross-domain RMSE | Degradation |
|---|---|---|---|---|
| EVnetNL | Informer | 9.866 | 19.971 | +102.4% |
| EVnetNL | USDT | 8.781 | 11.134 | +26.8% |
| Perth | Informer | 14.319 | 20.957 | +46.4% |
| Perth | USDT | 13.837 | 13.559 | −2.0% |

t-tests p < 0.001 both scenarios. Zero-shot USDT on Perth even slightly beats in-domain training (−2.0%).

### Uncertainty quality
CI plots: sharper/narrower intervals off-peak, adaptive widening during peaks (95% CI). PIT histograms near-uniform (well calibrated) vs sloped baseline. Reliability diagrams: USDT Average Calibration Error (**ACE**) = 0.0659 with better sharpness/calibration trade-off; CRPS improvements noted qualitatively.

### Computational cost vs Informer baseline
Model size 63.00 MB (both, 0.0%); peak VRAM 2379.24 → 1509.75 MiB (−36.5%); iteration latency 0.5309 → 1.6627 s/iter (+213.2%); inference 122.22 → 120.92 samples/s (−1.1%; ~0.008 s/sample — negligible vs 15-min dispatch windows).

### Ablation (EVnetNL)
Baseline (Informer) 9.866/97.734/6.733; +SMAN ("+SWAN") 9.452/89.347/6.422; +DDI 9.459/89.463/6.508; full USDT 8.781/77.103/6.097. Removing DDI degrades long-horizon prediction most; module benefits grow with horizon length; USDT uniquely improves with longer input sequences while UDT (no-SMAN variant) declines.

## 💡 Limitations & Identified Research Gaps
- **Short-horizon accuracy:** advantage concentrated at long horizons; short-term gains over strong baselines are modest (inductive biases favor low-frequency components/cross-station co-movements). Future: horizon-aware loss weighting, curriculum fine-tuning on high-variance intervals, lightweight residual correction heads.
- **Computational complexity:** +213% iteration latency from multi-scale pathways, dual-direction interactions and test-time adaptation; pruning, knowledge distillation, low-rank factorization and quantization-aware training planned.
- **Domain shift:** absolute accuracy degrades under pronounced distributional discrepancies (temporal coverage, station configuration, regional usage patterns); domain adaptation / robust normalization protocols needed.
- Text inconsistently attributes robustness to a "meta-learning framework" although no explicit meta-learning algorithm is defined.
- Table 1 loss (MSE) conflicts with stated NLL objective.

## 📚 BibTeX & Citation Reference
```bibtex
@article{Zhang2026USDT,
  author  = {Zhang, Jinlai and Tan, Liuqi and Xie, Hancheng and Gao, Kai and Liu, Wenzheng and Su, Jie and Zhu, Wenhao and Hu, Lin},
  title   = {Dynamic charging load prediction using uncertainty-scale dual-direction transformer},
  journal = {Sustainable Energy, Grids and Networks},
  volume  = {47},
  pages   = {102428},
  year    = {2026},
  doi     = {10.1016/j.segan.2026.102428}
}
```
Affiliation: College of Mechanical and Vehicle Engineering & School of Physics and Electronic Science, Changsha University of Science and Technology, Changsha, Hunan, China. Funding: NSFC 62403076; MOE Humanities & Social Science Fund 24YJCZH416; Hunan Innovative Research Group 2025JJ10006; Hunan HE S&T Innovative Research Team 2023CT02. Received 6 Mar 2026; revised 15 Jun 2026; accepted 15 Jul 2026.

## 🔗 Key References & Citation Graph
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — backbone architecture ([34]); also strongest baseline
- [[2023_Huang_MetaProbformer_EV_Load]] — Probformer/MetaProbformer baseline ([26]) and source of MHPSA/MHA/FCL modules
- [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — probabilistic autoregressive baseline ([21])
- [[2017_Attention_Is_All_You_Need]] — original Transformer ([31])
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]] — related locality-enhancing sparse attention lineage ([33])
- [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] — FEDM probabilistic baseline ([43])
- [[2025_Zheng_Coherent_Hierarchical_EV_Load]] — coherent hierarchical probabilistic forecasting (related PICCN-style convex probabilistic modeling, [44])
- [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] — related vault work on cross-site transfer learning for EV load forecasting
- [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] — related vault meta-learning EV load forecasting
- External citations not yet in vault: DiffPLF conditional diffusion (Electr. Power Syst. Res. 235:110723); Vaswani et al. 2017; Taylor & Letham Prophet (Am. Stat. 72(1):37–45); Sun et al. SVR charging load (IEEE APPEEC 2016)
