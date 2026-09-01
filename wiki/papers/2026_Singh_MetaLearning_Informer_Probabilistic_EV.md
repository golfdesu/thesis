---
type: paper
title: "Probabilistic computing forecasting approach for EV charging load forecasting using meta-learning enhanced informer"
authors: [Arpana Singh, Uma Nangia, M. Rizwan]
year: 2026
journal_conference: "Applied Soft Computing"
doi_url: "https://doi.org/10.1016/j.asoc.2026.115869"
models_used: ["[[MAML-Informer]]", "[[Informer]]", "[[MAML]]", "[[Transformer]]", "[[LSTM]]", "[[SVR]]", "[[Reptile]]", "[[LSTM-Informer]]", "[[LSTM_Transformer]]"]
datasets_used: ["[[Caltech_ACN]]", "[[Boulder_Colorado]]", "[[Palo_Alto_EV]]"]
features_used: ["[[Historical_Load]]", "[[Weather_Features]]", "[[Calendar_Features]]", "[[Token_Embeddings]]", "[[ProbSparse_Attention]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MSE]]", "[[CRPS]]", "[[PICP]]", "[[MPIW]]", "[[Pinball_Loss]]", "[[Winkler_Score]]", "[[Pinball_Loss]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Probabilistic Computing Forecasting Approach for EV Charging Load Forecasting Using Meta-Learning Enhanced Informer

> Arpana Singh, Uma Nangia, M. Rizwan — Department of Electrical Engineering, Delhi Technological University, Delhi 110042, India. Applied Soft Computing 202 (2026) 115869. Received 11 Nov 2025; revised 27 Apr 2026; accepted 29 Jun 2026; online 30 Jun 2026. DOI: https://doi.org/10.1016/j.asoc.2026.115869

## 🎯 Main Objective & Contribution
Propose **[[MAML-Informer]]**: a [[MAML]] ([[MAML]])-enhanced [[Informer]] for **multi-horizon point + probabilistic** EV charging load forecasting under sparse, heterogeneous, non-stationary data (e.g., newly commissioned stations). Each charging station is treated as a meta-learning task; the model first learns common charging-demand patterns across station clusters, then adapts quickly with few gradient steps.
Contributions:
1. MAML-Informer framework handling data-scarce, spatially heterogeneous stations with cross-station generalization + meta-adaptivity (Table 1 positions it as the only surveyed 2024–2026 method combining probabilistic forecasting ✓, cross-station generalization ✓, meta-learning adaptability ✓).
2. Unified quantile-driven pipeline producing deterministic and probabilistic outputs evaluated via RMSE/MAE/quantile-RMSE/PICP/CRPS.
3. Benchmarking against SVR, LSTM, Transformer, Informer, and LSTM hybrids on ACN, Palo Alto, Boulder datasets.
4. Computational-efficiency analysis (training time, inference latency, memory).
5. Ablation/sensitivity on inner-loop adaptation steps $K$, meta-learning rates $\alpha$, sequence lengths under few-shot (10% data) conditions.

Research gap addressed: prior probabilistic EV studies are mostly LSTM/hybrid-LSTM based, lack extended-horizon evaluation in data-scarce settings, and existing energy meta-learning targets only average accuracy without calibrated uncertainty.

## 🧠 Methodology & Model Architecture
**Problem formulation** — net load series per station $i$ (Eq. 1): $\{P_{i,t}\},\ t=1,\dots,T$. Training set (Eq. 2): $\mathcal{T} = \{\Theta_t, y_{t+1}\}_{t=1}^{T}$ where $\Theta_t$ is the input feature vector (historical load + meteorological data + temporal indices). Mapping (Eq. 3): $y_{t+1} = g(\Theta_t)$. Dual-dataset design: primary set $\mathcal{T}$ trains the deterministic model; auxiliary set $\mathcal{T}_r$ drives meta-learning adaptation and probabilistic calibration.

**Informer backbone** — inputs decomposed into historical load $H_t \in \mathbb{R}^{L_1 \times d_{model}}$ and auxiliary variables $S_t \in \mathbb{R}^{L_2 \times d_{model}}$. Query/Key/Value projections (Eq. 4):
$$Q = W^Q_i S_t,\quad K = W^K_i H_t,\quad V = W^V_i H_t$$
with $W^Q_i, W^K_i, W^V_i \in \mathbb{R}^{d_{model}\times d_k}$, $d_k = d_{model}/h$. Scaled dot-product attention (Eq. 5):
$$\text{Attention}(Q,K,V) = V \cdot \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)$$
Multi-head output (Eq. 6):
$$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1,\dots,\text{head}_h)\,W^O, \quad W^O \in \mathbb{R}^{hd_k\times d_{model}}$$
Feed-forward block (Eq. 7):
$$\text{FFN}(x) = \text{ReLU}(xW_1+b_1)W_2+b_2$$
A causal mask $M_{ij}$ ($j \le i$) is applied to encoder ProbSparse self-attention so support/query splits from sequential charging data remain causally valid — key adaptation vs. the vanilla Informer. Benefits retained: ProbSparse complexity reduced from $O(L^2)$ to $O(L \log L)$; self-attention distilling; generative one-pass multi-step decoding avoiding autoregressive error accumulation.

**MAML layer** — bi-level objective (Eq. 8, MAML Meta-Objective):
$$\theta^* = \arg\min_{\theta} \sum_{\mathcal{T}_i \in \mathcal{T}} \mathcal{L}_{\mathcal{T}_i}(\theta - \alpha \nabla_\theta \mathcal{L}_{\mathcal{T}_i}(\theta))$$
Inner-loop task update (Eq. 9): $\theta'_i = \theta - \alpha\nabla_\theta \mathcal{L}_{\mathcal{T}_i}(\theta)$; outer-loop meta-update (Eq. 10):
$$\theta \leftarrow \theta - \beta \nabla_\theta \sum_{\mathcal{T}_i\in\mathcal{T}} \mathcal{L}_{\mathcal{T}_i}(\theta'_i)$$

**Probabilistic head** — Gaussian likelihood over aggregated load (justified as approximately continuous/unimodal on daily horizons); chosen over quantile regression to avoid training multiple quantile models and quantile crossing under sparse data (Eq. 11, Gaussian Probabilistic Loss):
$$\mathcal{L}_{probabilistic} = \frac{1}{N}\sum_{t=1}^{N}\left((y_t - \mu_t)^2 + \log(\sigma^2_t) + \frac{(y_t-\mu_t)^2}{\sigma^2_t}\right)$$
with predicted mean $\mu_t$, variance $\sigma^2_t$. Quantile outputs Q50/Q90 derived for evaluation (Pinball/PICP/CRPS verify calibration beyond the Gaussian assumption).

**Pipeline**: token embedding → Conv1D → dropout → masked ProbSparse Informer encoder (conv layers + layer norm) → decoder → point forecasts (MAE/RMSE) + probabilistic forecasts (Q50/Q90). Offline meta-training across stations; online adaptation with few gradient updates on sliding windows; streaming deployment.

**Hyperparameters (Table 2)**: batch 32, dropout 0.2, GELU, 4 attention heads, embedding dim 512, 3 encoder / 2 decoder layers, FFN 1024; LSTM hidden 128, lr $10^{-3}$; meta inner-loop $\alpha=10^{-3}$, outer $\beta=10^{-3}$, $K=3$ inner steps, support–query split 70:30; input length 96 timesteps (24 h @15-min), prediction horizon 24 timesteps (6-h ahead); epochs ≤30 w/ early stopping; selected by validation RMSE$_{50}$ + CRPS stability.

## 📊 Dataset & Input Features
Three public real-world EV charging datasets (Sec. 4, Table 3), all min–max normalized; short gaps forward-fill interpolated, long gaps excluded; >3σ outliers kept only if genuine peak events:
| Metric | ACN | Boulder | Palo Alto |
|---|---|---|---|
| Data points | 2170 | 29,396 | 39,915 |
| Total energy (kWh) | 26,001.91 | 252,719.21 | 336,664.02 |
| Avg load (kW) | 11.98 | 8.60 | 8.43 |
| Peak load (kW) | 77.70 | 92.25 | 77.83 |
| Load std (kW) | 12.39 | 8.94 | 6.96 |
| Non-zero charging hour ratio | 23.54% | 19.95% | 72.07% |
| Unique charging days | 222 | 852 | 365 |
| Peak hour | 08:00 | 22:00 | 22:00 |
| Raw records cited in text | 2939 events | 148,136 records | 259,415 records |

Sources & access (as stated in paper):
- **[[Caltech_ACN]]** — Adaptive Charging Network data portal, ACN website ("available on the ACN website's data portal"): https://ev.caltech.edu/dataset (ACN-Data portal)
- **[[Boulder_Colorado]]** — City of Boulder Open Data platform (public-station charging; timestamps, kWh, charging times, GHG-savings metrics)
- **[[Palo_Alto_EV]]** — open data repository, referenced via [42] Amara-Ouali et al., "A review of electric vehicle load open data and models," Energies 14(8) 2021:2233, https://doi.org/10.3390/en14082233
Paper-level **Data availability statement: "Data will be made available on request."**

Features: historical charging-load sequences (96-step lookback @15-min), auxiliary variables — meteorological data and temporal indices; embedding module (token embedding + Conv1D + dropout).

Two evaluation scenarios: (1) one year of history → single-step next-day point forecast; (2) multi-step probabilistic forecast over several days ahead (24-timestep/6-h horizon in experiments).

## 📈 Performance & Results
**Point forecasting (Table 4)** — MAML-Informer lowest RMSE & MAE on all three datasets:
| Model | ACN RMSE/MAE | Boulder RMSE/MAE | Palo Alto RMSE/MAE |
|---|---|---|---|
| SVM/SVR | 5.212 / 7.372* | 16.976 / 14.81 | 9.847 / 7.815 |
| LSTM | 6.004 / 4.046 | 8.561 / 5.374 | 6.359 / 5.308 |
| Transformer | 7.587 / 5.015 | 8.672 / 6.178 | 6.594 / 5.108 |
| Informer | 7.437 / 4.862 | 8.791 / 4.593 | 7.158 / 5.479 |
| LSTM-Informer | 7.789 / 4.901 | 7.711 / 4.196 | 6.819 / 5.212 |
| LSTM-Transformer | 8.727 / 5.114 | 7.722 / 3.820 | 7.377 / 5.629 |
| Reptile-Informer | 5.684 / 3.891 | 7.412 / 3.982 | 5.972 / 4.437 |
| **MAML-Informer** | **5.212 / 3.372*** | **7.095 / 3.676** | **5.545 / 4.122** |
(*ACN SVM row prints MAE/RMSE columns swapped in source table; best overall reported as MSE 0.009, RMSE 0.095.)

**Probabilistic forecasting (Table 5)**:
| Model | ACN PICP/MPIW/CRPS/RMSE50/RMSE90 | Boulder | Palo Alto |
|---|---|---|---|
| SVR | 85.48 / 0.1639 / 1.625 / 0.310 / 0.812 | 83.48 / 0.1601 / 1.925 / 0.414 / 0.869 | 81.20 / 0.1585 / 1.621 / 0.209 / 0.851 |
| LSTM | 89.21 / 0.1642 / 1.330 / 0.366 / 0.811 | 89.21 / 0.1588 / 1.920 / 0.320 / 0.814 | 83.21 / 0.1582 / 1.990 / 0.192 / 0.862 |
| Transformer | 86.86 / 0.1640 / 1.610 / 0.274 / 0.869 | 86.86 / 0.1590 / 1.650 / 0.389 / 0.798 | 82.86 / 0.1589 / 1.630 / 0.203 / 0.850 |
| Informer | 84.24 / 0.1645 / 1.722 / 0.285 / 0.892 | 84.24 / 0.1597 / 1.170 / 0.301 / 0.828 | 89.24 / 0.1578 / 1.770 / 0.292 / 0.818 |
| LSTM-Informer | 92.14 / 0.1633 / 1.350 / 0.213 / 0.798 | 97.22 / 0.1582 / 1.013 / 0.398 / 0.807 | 96.82 / 0.1577 / 1.130 / 0.195 / 0.791 |
| **MAML-Informer** | **99.82 / 0.1602 / 1.140 / 0.181 / 0.783** | 91.88 / **0.1485** / **1.001** / 0.202 / 0.852 | 94.88 / 0.1511 / 1.012 / **0.168** / **0.754** |

- Headline gains: up to **51.21% lower RMSE$_{Q50}$** (vs SVR, Boulder), **12.53–12.98% lower RMSE$_{Q90}$**, up to **48% CRPS reduction**, ~17% PICP rise; PICP ≈100% (ACN 99.82%) with narrow MPIW ≈0.148–0.164 kWh; CRPS 0.065 (ACN), 0.023 (Boulder), 0.025 (Palo Alto) in Fig. 10 reporting.
- **Few-shot ablation (10% training data)** vs vanilla Informer: RMSE$_{Q50}$ cut by **36.5% (ACN), 48.1% (Boulder), 42.4% (Palo Alto)** plus consistently lower CRPS → gains stem from meta-learned initialization, not capacity.
- **Stress test** (sudden demand spikes ×1.5 / ×2.0, unchanged model): MAE 0.2195% / 0.4391%; RMSE 1.2576% / 2.5153%.
- **Computational cost (Table 8)**: train time/epoch 0.657 s (~30% above Informer's 0.511 s); total time 1.982 s; inference 1.083 ms (near-real-time). Sensitivity: RMSE/CRPS stabilize at $K=3$, $\alpha=10^{-3}$; saturation/degradation beyond.
- **Statistical significance** (10 runs, vs Informer): paired t-test p = 1.52×10⁻¹² (RMSE), 4.57×10⁻¹² (MAE); Wilcoxon p = 1.95×10⁻³ both.

## 💡 Limitations & Identified Research Gaps
- Authors explicitly scope the work as methodological integration + empirical validation: **no formal convergence analysis of MAML optimization** nor theoretical treatment of Informer sparsity.
- Gaussian likelihood assumption may misfit multimodal/spiky charging distributions (quantile metrics used as robustness check).
- Meta-training adds ~30% training-time overhead; future work: reducing meta-training complexity, event-aware forecasting strategies.
- Absolute MAE/RMSE margins over strong baselines are modest; superiority argued primarily through probabilistic metrics and few-shot ablations.
- Experiments in MATLAB R2022b on CPU (i7-13700, 32 GB RAM); distributed/high-performance claims not benchmarked on GPU-scale hardware in detail.

## 📚 BibTeX & Citation Reference
```bibtex
@article{singh2026mamlinformer,
  title   = {Probabilistic computing forecasting approach for EV charging load forecasting using meta-learning enhanced informer},
  author  = {Singh, Arpana and Nangia, Uma and Rizwan, M.},
  journal = {Applied Soft Computing},
  volume  = {202},
  pages   = {115869},
  year    = {2026},
  doi     = {10.1016/j.asoc.2026.115869}
}
```

## 🔗 Key References & Citation Graph
Vault papers this work builds directly on:
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — base Informer architecture, ProbSparse attention, generative decoder (ref. [8])
- [[2017_Finn_MAML_Model_Agnostic_Meta_Learning]] — MAML bi-level optimization (ref. [26])
- [[2018_Nichol_Reptile_First_Order_Meta_Learning]] — Reptile baseline (Reptile-Informer in Table 4)
- [[2017_Attention_Is_All_You_Need]] — scaled dot-product/multi-head attention (refs. [7])
- [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — probabilistic deep forecasting context (ref. [20])
- [[2021_Lim_TFT_Temporal_Fusion_Transformers]] — TFT probabilistic multi-horizon baseline family (ref. [6])
- Related vault EV probabilistic/meta-learning work: [[2023_Huang_MetaProbformer_EV_Load]], [[2025_Matrone_QR_LSTM_Attention_EV_Load]] (QR+LSTM probabilistic EV forecasting, ref. [34]), [[2024_Li_DiffPLF_Conditional_Diffusion_EV]], [[2025_Wu_Meta_Learning_Physics_Informed_GACN_Power_System]], [[2024_Ali_MQ_TCN_Transfer_Learning_EV]]
- Dataset-overlapping vault papers: [[2025_Hussain_Hybrid_LSTM_Transformer_Demand]] ([[Caltech_ACN]]), [[2020_Huang_Ensemble_EV_Load]] & [[2024_Helmy_Autoformer_EV_Charging]] ([[Boulder_Colorado]]), [[2024_Bampos_EV_Load_Forecasting_DAM]] ([[Palo_Alto_EV]])
