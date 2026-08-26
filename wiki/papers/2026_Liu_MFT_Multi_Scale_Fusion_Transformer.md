---
type: paper
title: "Multi-scale fusion transformer for EV charging station load prediction"
authors: [Wanying Liu, Jian Qiao, Wenxuan Wang, Xi Zhao]
year: 2026
journal_conference: "Scientific Reports (Nature Portfolio), vol. 16, art. 8609"
doi_url: "https://doi.org/10.1038/s41598-026-38562-z"
models_used: ["[[MFT]]", "[[Transformer]]", "[[LSTM]]", "[[BiLSTM]]", "[[GRU]]"]
datasets_used: ["[[Norway_Residential_EV_Charging_Dataset]]"]
features_used: ["[[Historical_Load]]", "[[Weather_Features]]", "[[Traffic_Density]]", "[[Scale_Mask]]", "[[Positional_Encoding]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MSE]]", "[[RMSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Multi-scale fusion transformer for EV charging station load prediction

## 🎯 Main Objective & Contribution
- EV charging station load prediction is challenged by stochastic charging behavior and complex external influences (weather, traffic). Existing deep models fail to capture **multi-scale temporal dependency** and underuse the **dynamic influence of external factors**; statistical methods ([[SARIMA]], RF, GBRT, Monte Carlo) miss nonlinear evolution.
- Proposes **[[MFT]]** (Multi-scale Fusion Transformer) combining three modules:
  1. **3M** — Multi-scale Modeling Mechanism: predefined *scale masks* constrain each attention head to model temporal dependency at a distinct granularity in parallel (fine-to-coarse), extending the padding-mask mechanism of multi-head attention.
  2. **FAM** — Feature-correlation Analysis Module: Pearson Correlation Coefficient (PCC) analysis over all training samples assigns a static *base weight* to each of 14 external features.
  3. **MFM** — Multi-variable Fusion Module: cross-attention with load as query converts base weights into sample-level *dynamic weights* for weighted aggregation of external features.
- Up to **25.59% average performance improvement** over competitors, with gains growing monotonically with horizon — strongest for long-term prediction.

## 🧠 Methodology & Model Architecture
- **Input embedding + positional encoding**: load sequence $l \in \mathbb{R}^{T_h\times 1}$ projected by MLP $\eta$ into high-dimensional space; sinusoidal positional encoding:
$$ p_t(2q) = \sin(t/10000^{2q/d_{\text{model}}}), \quad p_t(2q+1) = \cos(t/10000^{2q/d_{\text{model}}}) \tag{2} $$
- **Per-head Q/K/V projections**:
$$ \bar{l} = \eta(l) + \text{Pos}; \quad q_n = \gamma^Q(\bar{l}, W_n^Q),\ k_n = \gamma^K(\bar{l}, W_n^K),\ v_n = \gamma^V(\bar{l}, W_n^V) \tag{1} $$
- **Scale mask** ($m_n \in \mathbb{R}^{T_h\times T_h}$, one per head):
$$ m_n^{a,b} = \begin{cases} 0, & \frac{a-b}{n} \in \mathbb{Z} \\ -\infty, & \text{others} \end{cases} \tag{3} $$
- **Scale-masked attention and fusion** into multi-scale dependency representation $R$:
$$ \alpha_n = q_n(k_n)^\top,\quad \alpha'_n = \alpha_n + M,\quad r_n = \text{softmax}\!\left(\frac{\alpha'_n}{\sqrt{d_k^n}}\right)v_n,\quad R = \eta(\text{concat}(r_1,\dots,r_N)) \tag{4} $$
- **FAM base weights** from PCC between each external feature $X$ and load $Y$:
$$ \rho_{X,Y} = \frac{\text{cov}(X,Y)}{\sigma_X\sigma_Y} = \frac{\mathbb{E}[(X-\mu_X)(Y-\mu_Y)]}{\sigma_X\sigma_Y} \tag{5} $$
$$ W = \text{softmax}(P): \quad w_i = \frac{\exp(\rho_i)}{\sum_{j=1}^{14}\exp(\rho_j)} \tag{6} $$
- **MFM dynamic weighting** via cross-attention (load = query, external features = key/value):
$$ l_Q = \phi^Q(l, W_Q^l),\ x_{k_i} = \phi^K(x_i, W_K^x),\ x_{v_i} = \phi^V(x_i, W_V^x) \tag{7} $$
$$ z_i = l_Q (x_{k_i})^\top,\quad \sigma_i^w = \frac{\exp(z_i)}{\sum_{j=1}^{14}\exp(z_j)},\quad \tilde{w}_i = w_i + \sigma_i^w \tag{8} $$
- **Fusion + LSTM decoder**:
$$ E = \text{LeakyReLU}\Big(\sum_{i\in\{1,\dots,14\}} \tilde{w}_i x_{v_i}\Big), \qquad \hat{l} = \text{Dec}(\text{concat}(R, E)) \tag{9} $$
- Implementation: PyTorch, RTX 3090, batch 64, 50 epochs, Adam lr 0.0005, MSE loss, dropout 0.05 on output layer, min–max normalization to [0,1]; input = 24 h history, predict K ∈ {24, 48, 72, 96} hours. Deployment footprint vs standard Transformer (K=96): 17.12 MB params / 3.29 GFLOPs vs 16.04 MB / 3.05 GFLOPs; single 96-step inference < 100 µs.

## 📊 Dataset & Input Features
- Real-world charging data from a **large residential area in Norway** (hourly charging load); 24-hour historical load used to forecast 24/48/72/96 h ahead.
- **14 external features** (Table 1): 9 weather features at daily resolution — $T_{max}$ (°C), $W_{max}$ (m/s), $T_{min}$ (°C), $P_{mean}$ precipitation (mm), $H_{mean}$ humidity (%), $S_{mean}$ snowfall (cm), $I$ sunshine index (W/m²), $T_{mean}$ (°C), $W_{mean}$ wind speed (m/s); plus 5 hourly traffic-density features $Z_1$–$Z_5$ = number of vehicles in 5 fixed zones surrounding the station (aligned with the hourly load sequence).
- PCC findings: sunshine index strongest negative correlation (−0.239); average temperature −0.137; max temperature −0.126; average humidity +0.131; weak: precipitation +0.004, snowfall −0.029; traffic regions Z4/Z5 mildly positive (+0.066/+0.063).
- Data availability statement: "The data used for implementing the forecasting algorithms are available at **https://github.com/shivkumarjadon6/Hourly_EV**"; other data included within the manuscript. No station count or session count disclosed.

## 📈 Performance & Results
- Metrics ([[MSE]], [[RMSE]], [[MAE]]), MFT vs baselines:
| Horizon | MFT (MSE/RMSE/MAE) | Transformer | BiLSTM | LSTM | GRU |
|---|---|---|---|---|---|
| K=24 | **1.51 / 1.23 / 0.69** | 1.67 / 1.29 / 0.82 | 1.76 / 1.33 / 0.79 | 1.81 / 1.35 / 0.82 | 2.12 / 1.46 / 0.91 |
| K=48 | **1.64 / 1.28 / 0.78** | 1.75 / 1.32 / 0.86 | 1.83 / 1.35 / 0.82 | 2.21 / 1.49 / 0.96 | 2.50 / 1.58 / 1.03 |
| K=72 | **1.75 / 1.32 / 0.81** | 1.92 / 1.38 / 0.92 | 2.01 / 1.42 / 0.91 | 2.61 / 1.62 / 1.06 | 2.74 / 1.66 / 1.09 |
| K=96 | **1.89 / 1.38 / 0.88** | 2.51 / 1.58 / 1.08 | 2.96 / 1.60 / 1.10 | 3.20 / 1.79 / 1.19 | 3.26 / 1.80 / 1.18 |
- Average gains over competitors: 26.54% (GRU), 21.88% (LSTM), 12.85% (BiLSTM), 10.79% (Transformer); by metric: MSE 23.73%, RMSE 12.58%, MAE 17.73%.
- Improvements grow monotonically with horizon (MSE: 17.30%/19.14%/22.69%/**35.78%** at 24/48/72/96 h) — best exactly where baselines degrade most.
- Incremental ablation (TF → MT(+3M) → MFT(+MFM)): 3M yields 6.27%/3.19%/3.86% (MSE/RMSE/MAE); MFM adds 6.42%/3.34%/5.49%. At long horizons (K=72, 96) MFM's contribution exceeds 3M's (e.g., 9.73% vs 3.48% at K=96), indicating weather/traffic dominate long-term behavior.
- Qualitative: flattest error curves; baselines lag at K=72/96 while MFT tracks rhythm and magnitude.

## 💡 Limitations & Identified Research Gaps
- Dataset is a single Norwegian residential area; station/session counts and public provenance are not fully specified (only a GitHub mirror link provided).
- Weather features only at daily resolution (assumed stable within a day) — limits fine-grained weather response modeling.
- Scale masks are predefined rather than learned; number of heads fixes the scale set.
- Authors' future work: incorporate battery-related factors (charging/discharging influenced by battery characteristics) to further improve accuracy.
- Baselines limited to classic RNN/Transformer family; no comparison against modern SSM/Mamba or specialized long-horizon forecasters.

## 📚 BibTeX & Citation Reference
```bibtex
@article{liu2026mft,
  author  = {Liu, Wanying and Qiao, Jian and Wang, Wenxuan and Zhao, Xi},
  title   = {Multi-scale fusion transformer for {EV} charging station load prediction},
  journal = {Scientific Reports},
  volume  = {16},
  pages   = {8609},
  year    = {2026},
  doi     = {10.1038/s41598-026-38562-z}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] (Vaswani et al., NeurIPS 2017) [30] — Transformer backbone
- [[LSTM]] (Hochreiter & Schmidhuber, 1997) [28]; [[BiLSTM]] (Graves & Schmidhuber, 2005) [29]; [[GRU]] (Chung et al., 2014) [27]
- Transformer-based EV demand prediction (Koohfar et al., Sustainability 2023) [22]
- Multi-resolution time-series transformer (Zhang et al., AISTATS 2024) [23]; SDFormer spectral/dynamic attention (IJCAI 2024) [24] — contrasted with 3M
- SARIMA EV forecasting (Buzna et al., SyNERGY MED 2019) [12]; aggregated-station time-series modeling (Louie, EPCS 2017) [13]; Jeju fast-charging LSTM (Chang et al., Sustainability 2021) [19]
- Battery-degradation physics-guided TL-LSTM (Liu et al., J. Energy Storage 2025) [31] — planned future extension
- PyTorch [25]; Adam optimizer (Kingma & Ba) [26]
