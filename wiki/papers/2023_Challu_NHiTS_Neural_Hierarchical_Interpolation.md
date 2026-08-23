---
type: paper
title: "N-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting"
authors: [Cristian Challu, Kin G. Olivares, Boris N. Oreshkin, Federico Garza, Max Mergenthaler-Canseco, Artur Dubrawski]
year: 2023
journal_conference: "AAAI 2023"
doi_url: "https://arxiv.org/abs/2201.12886"
models_used: ["[[NHiTS]]", "[[N-BEATS]]", "[[Autoformer]]", "[[Informer]]", "[[FEDformer]]", "[[Reformer]]", "[[LogTrans]]", "[[DilRNN]]", "[[DeepAR]]", "[[Prophet]]", "[[ARIMA]]"]
datasets_used: ["[[ETTm2]]", "[[Exchange_Rate]]", "[[ECL_Dataset]]", "[[TrafficL_PeMS]]", "[[Weather_Jena]]", "[[ILI_CDC]]"]
features_used: ["[[Historical_Load|Univariate lags only (own history y_{t-L:t})]]"]
forecasting_horizon: "[[Long_Term]]"
metrics: ["[[MSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: N-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting

## 🎯 Main Objective & Contribution
- Tackles **long-horizon forecasting** volatility + computational complexity: attention and fully-connected layers scale quadratically in memory/compute with horizon $H$, and forecast errors inflate with $H$.
- Proposes **[[NHiTS]]**, extending [[N-BEATS]] with two complementary techniques: (1) **multi-rate input sampling** (MaxPool subsampling per block) and (2) **hierarchical interpolation** (few forecast coefficients upsampled via temporal interpolation).
- Contributions: multi-rate sampling layers; interpolation-based output synthesis (architecture-agnostic); hierarchically synchronized block specialization into frequency bands; SOTA on six large-scale long-horizon benchmarks — average accuracy improvement of ~20%/14-16% over latest Transformer architectures while reducing compute time by an order of magnitude (~50×).

## 🧠 Methodology & Model Architecture
MLP stacks ($S$ stacks × $B$ blocks) connected via the doubly-residual stacking principle; each block emits a backcast $\tilde{y}_{t-L:t,\ell}$ (subtracted from the next block's input) and a forecast $\hat{y}_{t+1:t+H,\ell}$ (summed).

**Equation 1 — Multi-rate signal sampling (MaxPool with kernel $k_\ell$):**
$$y_{t-L:t,\ell}^{(p)} = \text{MaxPool}(y_{t-L:t,\ell},\, k_\ell)$$
Larger $k_\ell$ removes high-frequency content, forcing the block to focus on large-scale/low-frequency components.

**Equation 2 — Non-linear regression of interpolation coefficients:**
$$h_\ell = \text{MLP}_\ell\left(y_{t-L:t,\ell}^{(p)}\right), \qquad \theta_\ell^f = \text{LINEAR}_f(h_\ell), \qquad \theta_\ell^b = \text{LINEAR}_b(h_\ell)$$

**Equations 3–4 — Hierarchical interpolation** with expressiveness ratio $r_\ell$, $|\theta_\ell^f| = \lceil r_\ell H \rceil \ll H$:
$$\hat{y}_{\tau,\ell} = g(\tau, \theta_\ell^f),\;\forall \tau \in \{t+1,\dots,t+H\}, \qquad \tilde{y}_{\tau,\ell} = g(\tau, \theta_\ell^b),\;\forall \tau \in \{t-L,\dots,t\}$$
Linear interpolator $g \in C^1$ on anchors $\mathcal{T}=\{t+1, t+1+1/r_\ell, \dots, t+H\}$:
$$g(\tau,\theta) = \theta[t_1] + \left(\frac{\theta[t_2]-\theta[t_1]}{t_2-t_1}\right)(\tau-t_1), \quad t_1 = \arg\min_{t\in\mathcal{T}:t\le\tau} \tau-t, \quad t_2 = t_1+1/r_\ell$$

**Hierarchical assembly (Top-Down: low frequencies first):**
$$\hat{y}_{t+1:t+H} = \sum_{l=1}^{L} \hat{y}_{t+1:t+H,\ell}, \qquad y_{t-L:t,\ell+1} = y_{t-L:t,\ell} - \tilde{y}_{t-L:t,\ell}$$
Expressiveness ratios increase exponentially across blocks; blocks near the input have small $r_\ell$/large $k_\ell$ (coarse scales first).

**Equation 5 — Neural Basis Approximation Theorem:** if multi-resolution functions $V_w = \{\phi_{w,h}(\tau)=\phi(2^w(\tau-h))\}$ arbitrarily approximate $L^2([0,1])$ and projections vary smoothly in $y_{t-L:t}$, then for all $\epsilon>0$:
$$\int \left| Y(\tau|y_{t-L:t}) - \sum_{w,h}\hat{\theta}_{w,h}(y_{t-L:t})\phi_{w,h}(\tau) \right| d\tau \le \epsilon$$
(proved via Haar scaling functions + ReLU universal approximation, Eqs. 7–9).

**Equation 6 — Metrics:** $\text{MSE} = \frac{1}{H}\sum_{\tau=t}^{t+H}(y_\tau-\hat{y}_\tau)^2$, $\text{MAE} = \frac{1}{H}\sum_{\tau=t}^{t+H}|y_\tau-\hat{y}_\tau|$.

Appendix interpolators (Eqs. 10–13d): nearest-neighbor $\hat{y}_\tau=\theta[t^*]$; Hermite cubic $\hat{y}_\tau=\theta[t_1]\varphi_1(\tau)+\theta[t_2]\varphi_2(\tau)+\theta'[t_1]\psi_1(\tau)+\theta'[t_2]\psi_2(\tau)$ with $\varphi_1(\tau)=2\tau^3-3\tau^2+1$, etc. Complexity: time/memory scale as $O(H\frac{1-r^B}{1-r})$ vs $O(H^2B)$ for N-BEATSi and $O(H^2)$ Transformers. Training: PyTorch, ADAM, MAE loss, batch 256, lr 1e-3 halved 3×, HyperOpt Bayesian tuning (20 iters), GeForce RTX 2080 / AWS g4dn.2xlarge.

## 📊 Dataset & Input Features
All datasets publicly available (Table A1); normalized by train mean/std; univariate inputs (own history only); splits 70/10/20 (ETTm2 val 20%), rolling-window test evaluation:
- **[[ETTm2]]**: electricity transformer temperature, region of a province in China; oil temp + load variants; Jul 2016–Jul 2018; 15-min; 7 series; 403,200 obs (80,640 test); horizons {96,192,336,720}.
- **[[Exchange_Rate]]**: daily exchange rates of 8 countries vs USD (Australia, UK, Canada, Switzerland, China, Japan, New Zealand, Singapore), 1990–2016; 8 series; 60,704 obs.
- **[[ECL_Dataset]]**: electricity consumption (kWh) of 321 customers, 2012–2014; 15-min aggregated to hourly; 321 series; 8,443,584 obs.
- **[[TrafficL_PeMS]]**: San Francisco Bay Area highway hourly occupancy rates, 862 sensors, California DOT (Caltrans/PeMS), Jan 2015–Dec 2016; 862 series; 15,122,928 obs.
- **[[Weather_Jena]]**: 21 meteorological measures every 10 min, Weather Station of the Max Planck Biogeochemistry Institute, Jena, Germany; year 2020; 21 series; 1,106,595 obs.
- **[[ILI_CDC]]**: weekly influenza-like illness patient ratio, US Centers for Disease Control and Prevention, 2002–2021; 7 series; 6,762 obs; horizons {24,36,48,60}.
- Code/data availability: official implementation https://github.com/Nixtla/neuralforecast ; paper preprint https://arxiv.org/abs/2201.12886 . No other dataset URLs given in text (datasets follow Autoformer/Informer releases).

## 📈 Performance & Results
Multivariate, averaged over 8 runs (Table 1):
- Average relative error decrease vs best baseline: **14% MAE, 16% MSE**; at longest horizon (720/60): **11% MAE, 17% MSE** reduction. Example ECL@96: N-HiTS MSE 0.147 vs N-BEATS 0.145, Autoformer 0.201, Informer 0.274; Exchange@720: 0.798 vs Autoformer 1.447, Informer 2.478; TrafficL@96: 0.402 vs FEDformer 0.562; Weather@720: 0.351 vs FEDformer 0.403; ILI@24: 1.862 vs FEDformer 2.203, Informer 5.764.
- Vs concurrent ETSformer/Preformer (Table A4): still **11% MAE / 9% MSE** better on average (ETSformer wins only short-horizon Exchange).
- **Univariate** (ETTm2, Exchange, Table A5): −17% MAE, −25% MSE vs best alternative (e.g., ETTm2@720 MSE 0.157 vs N-BEATS 0.188, DeepAR 0.332).
- **Efficiency**: 45× faster than [[Autoformer]]; <26% of parameters of second-best model; 1.26× faster than N-BEATS with 54% of its parameters. Train times (Table A10, full benchmark): N-HiTS₁ 1.5 h, N-BEATSg 2.7 h, Informer 62.1 h, Autoformer 92.6 h → cost ≈ USD 22.8 (N-HiTS₂₀) vs USD 70 (Autoformer); N-HiTS₁ gains 17% MSE over Autoformer at 1.6% of its cost.
- **Ablations (Tables 2, A6–A9)**: both components together best (avg MSE @720: N-HiTS 0.484 vs N-BEATSi 0.794); MaxPool beats AvgPool (up to 15% MAE / 15.2% MSE @720); linear ≥ cubic > nearest-neighbor interpolation (linear up to 15.8% better than NN @720); Top-Down frequency ordering beats Bottom-Up (+4.6% MAE, +7.5% MSE); hierarchical interpolation also transfers to [[DilRNN]].

## 💡 Limitations & Identified Research Gaps
- Strictly **univariate** (each variable predicted from own history) — cannot exploit cross-variable dependencies common in EV station networks; authors flag multivariate integration as untapped potential.
- Point forecasts only (MAE loss) — no probabilistic/quantile outputs for downstream uncertainty-aware decisions.
- Interpolation smoothness assumption may limit abrupt regime shifts (e.g., anomalous events, new-station cold start).
- Wavelet/multi-resolution-analysis formulations proposed as future work; combining with Transformer-inspired architectures suggested.
- Gap for thesis: use as efficient long-horizon backbone for day-ahead EV charging demand; combine with [[RevIN]] for non-stationarity and probabilistic heads for planning.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{challu2023nhits,
  title     = {N-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting},
  author    = {Challu, Cristian and Olivares, Kin G. and Oreshkin, Boris N. and Garza, Federico and Mergenthaler-Canseco, Max and Dubrawski, Artur},
  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
  year      = {2023}
}
```

## 🔗 Key References & Citation Graph
- [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]]
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]]
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]]
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]]
- [[2020_DeepAR_Probabilistic_Forecasting_with_Autoregressive_Recurrent_Networks]]
- [[2021_Lim_TFT_Temporal_Fusion_Transformers]]
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]]
- [[2022_Kim_RevIN_Reversible_Instance_Normalization]]
