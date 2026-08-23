---
type: paper
title: "Multi-Branch ResNet-Transformer for Short-Term Spatio-Temporal Solar Irradiance Forecasting"
authors: [Saeedeh Ziyabari, Zhenyu Zhao, Liang Du, Saroj K. Biswas]
year: 2023
journal_conference: "IEEE Transactions on Industry Applications, 59(5), 5293-5303"
doi_url: "https://doi.org/10.1109/TIA.2023.3285202"
models_used: ["[[ResTrans|Multi-Branch ResNet-Transformer (ResTrans)]]", "[[Transformer]]", "[[ResLSTM]]", "[[CNN_LSTM]]", "[[AttLSTM]]", "[[ResNet]]", "[[LSTM]]", "[[CNN]]"]
datasets_used: ["[[NSRDB|NSRDB Philadelphia, USA (18 sites, 2000-2017, 30-min, 3,784,320 observations)]]"]
features_used: ["[[GHI]]", "[[DNI]]", "[[DHI]]", "[[Clearsky_GHI_DNI_DHI|Clear-sky GHI/DHI/DNI]]", "[[Temperature]]", "[[Relative_Humidity]]", "[[Wind_Speed]]", "[[Wind_Direction]]", "[[Pressure]]", "[[Dew_Point]]", "[[Solar_Zenith_Angle]]", "[[Precipitable_Water]]", "[[Cloud_Type]]"]
forecasting_horizon: "[[Spatial_Temporal]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[R2|R² score]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Multi-Branch ResNet-Transformer for Short-Term Spatio-Temporal Solar Irradiance Forecasting

## 🎯 Main Objective & Contribution
- Proposes **multi-branch [[ResTrans]]**, a hybrid spatio-temporal framework combining a **multi-branch deep residual network ([[ResNet]])** for spatial correlation modeling across neighboring solar sites and a modified **[[Transformer]]** (encoder-only + time embedding) for temporal long-sequence modeling.
- Motivations: RNN/LSTM frameworks forget long sequences and are computationally inefficient; CNNs ignore cross-site spatial correlations; single-resolution architectures miss multi-scale patterns; CNN/RNN overfitting is alleviated via shared multi-branch representations.
- First work to combine Transformer with multi-branch ResNets for short-term spatio-temporal solar irradiance forecasting; achieves average RMSE 0.049 W/m², MAE 0.031 W/m², R² = 97%, beating single-branch ResTrans, multi/single-branch ResLSTM and CNN-LSTM.

## 🧠 Methodology & Model Architecture
**Equation 1 — Forecast definition:** $\hat{Y}_{t+\Delta}^{n} = F(X)$, with $F(\cdot)$ implemented by self-attention + ResNet + Transformer over $N$ solar sites.

**Equations 2–4 — Attention over RNN hidden states:** $p_t = \tanh(W_h h_t + b_h)$, $a_t = \frac{\exp(p_t)}{\sum_{i=1}^{t}\exp(p_i)}$, $h_t' = a_t \odot h_t$.

**Equation 5 — Single-head scaled dot-product attention:** $\text{Att}(Q,K,V) = \psi\left(\frac{QK^T}{\sqrt{p_k}}\right)V$, ψ = softmax.

**Equations 6–7 — Multi-head attention:** $\text{Multi-head}(Q,K,V)=\text{Concat}(h_1,\dots,h_n)Z_o$ with $h_i = \text{Att}(QZ_i^Q, KZ_i^K, VZ_i^V)$, $Z_o$ learned projection matrix.

**Equation 8 — Time2Vec-style continuous time embedding** (replaces word/positional encoding):
$$C(\tau)[j] = \begin{cases} \omega_j\tau + \phi_j & j = 0 \\ g(\omega_j\tau + \phi_j) & 0 \le j \le k \end{cases}$$
with periodic feature $g$ and learnable parameters $\omega_j, \phi_j$; time-invariant, captures periodic + non-periodic patterns.

**Temporal model (per site):** encoder-only Transformer — 3 encoder layers × 3 heads; each encoder layer has a multi-head self-attention sub-layer and one **1D-CNN sub-layer (28 kernels, kernel size and stride 1)** replacing the feed-forward sub-layer, with dropout + normalization before/after; then global average pooling → dropout → dense layer. Trained with Adam optimizer, MSE loss, 50 iterations, early stopping (patience 3).

**Equation 9 — Multi-branch ResNet output** ($J$ branches, $I$ residual blocks): 
$$Z_D = Z_0 + \sum_{j=1}^{J}\sum_{i=0}^{I} G(Z_{i,j}, \Phi_{i,j})$$
where $G(\cdot)$ is the residual function and $\Phi_{i,j}$ the block weights.

**Equation 10 — Gradient flow through identity shortcut:** 
$$\frac{\partial \mathcal{L}}{\partial Z_0} = \frac{\partial \mathcal{L}}{\partial Z_D}\left(1 + \frac{\partial}{\partial Z_0}\sum_{j=1}^{J}\sum_{i=0}^{I}G(Z_{i,j},\Phi_{i,j})\right)$$
(the "1" term directly back-propagates gradients, alleviating vanishing gradients).

Pipeline: (1) preprocessing — cleaning, linear interpolation of missing data, min-max normalization per site; (2) per-site temporal Transformer models (dimension reduction); (3) outputs aggregated/rearranged and fed to the multi-branch ResNet (bottleneck conv: 64 kernels size 3 stride 1 → BN → ReLU; two residual blocks; prediction block) for inter-site spatial modeling at multiple resolutions.

## 📊 Dataset & Input Features
- **[[NSRDB]]** (National Solar Radiation Data Base, NREL): **18 sites in Philadelphia, PA, USA**, years **2000–2017** (17 years), **30-minute interval**, **3,784,320 total observations**. Evaluation groups: **12 sites in south Philadelphia** (temporal-model validation) and all 18 sites (6 additional sites ~60 miles away, spatio-temporal validation). Reference [26]: M. Sengupta et al., "The National Solar Radiation Data Base (NSRDB)," Renew. Sustain. Energy Rev., vol. 89, pp. 51–60, 2018.
- Features: historical [[GHI]], [[DNI]], [[DHI]] (W/m²); clear-sky GHI/DHI/DNI; meteorological variables — dew point (°C), solar zenith angle (°), wind speed (m/s), precipitable water (mm), wind direction (°), relative humidity (%), temperature (°C), pressure (mb), cloud type (one-hot encoded).
- Only daylight data 5:00–19:00 modeled (28 points/day at 30-min resolution); sliding window length L=24 (half-day lookahead); splits: train 2000–2010, validation 2011–2013, test 2014–2017; linear interpolation for gaps; min-max normalization:
$$x' = \frac{x - \min(x)}{\max(x) - \min(x)}$$
- No public code or data URL beyond the NSRDB citation is provided; no explicit data availability statement in text.

## 📈 Performance & Results
Temporal models on 12 sites, 12-hour horizon (Table II averages): CNN (RMSE 0.19, MAE 0.13, R² 0.63), LSTM (0.14, 0.09, 0.77), AttLSTM (0.12, 0.07, 0.78), ResNet (0.08, 0.05, 0.84), proposed Transformer (**0.06, 0.04, 0.87**) — beats LSTM by **57.14% RMSE / 55.56% MAE / 12.99% R²**; beats ResNet by 25.00% RMSE / 20.00% MAE despite having 12.24% more parameters (1,106,011 vs 985,361) while training **17.35% faster** (parallelism).

Spatio-temporal models (Tables IV–V):
- **12 sites**: replacing LSTM with Transformer lowers average RMSE by 8.70% (single-branch) and 14.04% (multi-branch); **multi-branch ResTrans best: RMSE ≈ 0.054, MAE ≈ 0.036, R² ≈ 0.90+**; multi-branch vs single-branch ResTrans improves RMSE **22.22%** and MAE **20.51%** (single-resolution models miss multi-scale features); CNN-LSTM weakest.
- **18 sites (incl. distant)**: overall best remains multi-branch ResTrans with **average RMSE 0.049 W/m², average MAE 0.031 W/m², R² = 97%** (abstract); accuracy slightly degrades with distant sites due to lower spatial correlation — e.g., single-branch ResTrans RMSE/MAE rise 6.3%/17.9% vs 12-site case; negative correlation between forecast accuracy and inter-site distance.

## 💡 Limitations & Identified Research Gaps
- Accuracy degrades as distance between sites grows — spatial graph construction / distance-aware attention not addressed.
- Deterministic point forecasts only; no probabilistic uncertainty bands (important for grid integration).
- Fixed sliding window (24 steps, half-day); horizon sensitivity not systematically ablated.
- Solar-specific benchmark — but architecture directly transferable to **spatio-temporal EV charging station load forecasting**, where neighboring stations exhibit similar correlated demand patterns.
- Gap for thesis: combine multi-resolution spatial branches with probabilistic heads (cf. [[2023_Huang_MetaProbformer_EV_Load]]) for charging networks.

## 📚 BibTeX & Citation Reference
```bibtex
@article{ziyabari2023resTrans,
  title   = {Multi-Branch ResNet-Transformer for Short-Term Spatio-Temporal Solar Irradiance Forecasting},
  author  = {Ziyabari, Saeedeh and Zhao, Zhenyu and Du, Liang and Biswas, Saroj K.},
  journal = {IEEE Transactions on Industry Applications},
  volume  = {59},
  number  = {5},
  pages   = {5293--5303},
  year    = {2023},
  doi     = {10.1109/TIA.2023.3285202}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]]
- [[1997_Long_Short_Term_Memory]]
- [[2022_Kim_RevIN_Reversible_Instance_Normalization]]
- [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]]
- [[2023_Huang_MetaProbformer_EV_Load]]
