---
type: paper
title: "BWO–ICEEMDAN–iTransformer: A Short-Term Load Forecasting Model for Power Systems with Parameter Optimization"
authors: [Danqi Zheng, Jiyun Qin, Zhen Liu, Qinglei Zhang, Jianguo Duan, Ying Zhou]
year: 2025
journal_conference: "Algorithms (MDPI), vol. 18, no. 5, art. 243"
doi_url: "https://doi.org/10.3390/a18050243"
models_used: ["[[iTransformer]]", "[[ICEEMDAN]]", "[[BWO]]"]
datasets_used: ["[[Singapore_Energy_Market_Dataset]]"]
features_used: ["[[Electricity_Load]]", "[[Electricity_Tariff]]", "[[Temperature]]", "[[Humidity]]", "[[Historical_Load]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[R_squared]]", "[[MAE]]", "[[RMSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: BWO–ICEEMDAN–iTransformer: A Short-Term Load Forecasting Model for Power Systems with Parameter Optimization

## 🎯 Main Objective & Contribution
- **Problem**: Growing irregularity/non-stationarity of power load data (diverse consumption patterns, distributed microgrids, renewables) makes precise short-term load forecasting difficult; demand-response programs depend on accurate forecasts.
- **Contribution**: A hybrid decomposition–optimization–forecasting pipeline, **BWO–ICEEMDAN–[[iTransformer]]**:
  1. [[BWO]] (Beluga Whale Optimization) optimizes the two ICEEMDAN parameters — noise standard deviation (Nstd) and number of realizations (NR) — using minimum envelope entropy as fitness function.
  2. Optimized [[ICEEMDAN]] decomposes volatile load into IMFs + residual (13 IMFs + 1 residual on all splits).
  3. Each IMF subsequence plus correlated exogenous factors is forecast independently by iTransformer; predictions are integrated into the final forecast.
- Claimed first use of a metaheuristic to tune ICEEMDAN parameters rather than relying on empirical settings.

## 🧠 Methodology & Model Architecture
- **Feature selection**: Spearman Correlation Coefficient (SCC), Eq. (1):
$$\rho = 1 - \frac{6\sum d_i^2}{n(n^2 - 1)}$$
where $d_i$ = rank difference between $x_i$ and $y_i$, $n$ = sample size. Selected temperature (+0.6830), relative humidity (−0.6440), price (+0.5131); rejected wind speed (0.2080), dew point, pressure, wind direction (<0.07).
- **BWO balance factor** (exploration vs exploitation switch), Eq. (2): $B_f = B_0 \cdot (1 - t/2T)$; exploration when $B_f > 0.5$, else exploitation.
- **BWO swimming/exploration position update**, Eq. (3):
$$X_{i,j}^{t+1} = X_{i,p_j}^t + \left(X_{r,p_1}^t - X_{i,p_j}^t\right)(1+r_1)\sin(2\pi r_2),\ j=\text{even}$$
$$X_{i,j}^{t+1} = X_{i,p_j}^t + \left(X_{r,p_1}^t - X_{i,p_j}^t\right)(1+r_1)\cos(2\pi r_2),\ j=\text{odd}$$
- **BWO hunting/exploitation with Lévy flight**, Eq. (4):
$$X_i^{t+1} = r_3 \cdot X_{best}^t - r_4 \cdot X_i^t + C_1 \cdot LF \cdot \left(X_r^t - X_i^t\right)$$
with jump height $C_1 = 2 r_4 (1 - t/T)$ and Lévy random number, Eq. (5)-(6):
$$LF = 0.05 \times u \times \frac{\sigma}{|v|^{1/\beta}}, \quad \sigma = \left(\frac{\Gamma(1+\beta)\sin\left(\frac{\pi\beta}{2}\right)}{\Gamma\left(\frac{1+\beta}{2}\right)\beta \cdot 2^{(\beta-1)/2}}\right)^{1/\beta},\ \beta=1.5$$
- **Whale fall phase**, Eqs. (7)–(10):
$$X_i^{t+1} = r_5 X_i^t - r_6 X_r^t + r_7 X_{step}^t,\qquad X_{step}^t = (ub-lb)\exp\left(-C_2 \frac{t}{T}\right)$$
$$C_2 = 2 W_f N,\qquad W_f = 0.1 - 0.05\frac{t}{T}$$
- **ICEEMDAN steps** (noise addition Eq. 11 → final IMF Eq. 17):
  - White-noise-augmented signal, Eq. (11): $x^i(t) = x(t) + \alpha_0 E_1(\beta^{(i)})$
  - First residual, Eq. (12): $r_1 = M(x^i(t))$ ($M(\cdot)$ = local mean operator)
  - First modal component, Eq. (13): $I_1 = x(t) - r_1$
  - Second stage, Eqs. (14)–(15): $r_2 = M(r_1 + \alpha_1 E_2(\beta^{(i)}))$, $I_2 = r_1 - r_2$
  - General stage, Eqs. (16)–(17): $r_j = M(r_{j-1} + \alpha_{j-1}E_j(\beta^{(i)}))$, $I_j = r_{j-1} - r_j$
  - Stop when residual is monotonic or adjacent-IMF std < 0.2. Decomposition performed separately on train/validation/test splits to avoid leakage.
- **iTransformer architecture** (inverted transformer; each variate's whole series becomes one token):
  - Variate token embedding: $h_n = \text{MLP}(X_{:,n}) \in \mathbb{R}^D$
  - Multivariate attention, Eq. (18):
$$Attention(Q,K,V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
  - LayerNorm, Eq. (19): $LayerNorm(H) = \{(h_n - Mean(h_n))/\sqrt{Var(h_n)},\ n=1,\dots,N\}$
  - Residual attention block, Eq. (20): $H^{l-1} = LayerNorm(H^{l-1} + Self\text{-}Attn(H^{l-1}))$
  - FFN block, Eq. (21): $H^l = LayerNorm(H^{l-1} + Feed\text{-}Forward(H^{l-1}))$
  - Output head, Eq. (22): $\hat{Y} = MLP(H^L)$
- **Metrics** (Eqs. 23–25): MAE, RMSE, R².
- **Preprocessing**: missing values filled with average of same time point ±3 days; anomalies screened via three-sigma rule and treated as missing.
- **Hyperparameters**: population 30, max iterations 30, Nstd ∈ [0.15, 0.6], NR ∈ [10, 600], batch size 72, epochs 10 (patience 3), lr 1e-4, linear layer 512, FFN layer 2048; input length 96, output length 48.

## 📊 Dataset & Input Features
- **Dataset**: [[Singapore_Energy_Market_Dataset]] from the Singapore Energy Market Corporation (EMC) / NEMS platform — 2019–2020 electricity load, price, and weather recorded at **30-min intervals**; split train/validation/test 3:1:1 (test set: 1440 records ≈ 30 days).
- **Features**: electricity load (target, MW), temperature (SCC 0.6830), relative humidity (SCC −0.6440), electricity price (SCC 0.5131); holiday-period correlations confirmed (T 0.5699, RH −0.4473, price 0.4521). Lagged-load correlation supports historical inputs.
- **Data availability**: "All data are presented in the main text." EMC price portal: https://www.nems.emcsg.com/nems-prices (accessed 30 September 2024).
- Not an EV dataset — general system-level power load (relevant as methodology template for EV station forecasting).

## 📈 Performance & Results
- Proposed model (test set): **R² 0.9873, MAE 48.0014, RMSE 66.2221** (note: abstract mislabels MAE/RMSE; Table 4 values used here).
- vs baselines (R² / MAE / RMSE):

| Model | R² | MAE | RMSE |
|---|---|---|---|
| **BWO–ICEEMDAN–iTransformer** | **0.9873** | **48.0014** | **66.2221** |
| GWO–ICEEMDAN–iTransformer | 0.9869 | 48.8129 | 67.3607 |
| CSA–ICEEMDAN–iTransformer | 0.9867 | 49.1543 | 67.7606 |
| DA–ICEEMDAN–iTransformer | 0.9858 | 50.0338 | 69.9737 |
| ICEEMDAN–iTransformer | 0.9738 | 71.1998 | 95.0231 |
| CEEMD–iTransformer | 0.9728 | 72.0094 | 96.9611 |
| EEMD–iTransformer | 0.9686 | 80.4151 | 104.0551 |
| BWO–CEEMD–iTransformer | 0.9767 | 67.1662 | 89.6762 |
| BWO–EEMD–iTransformer | 0.9689 | 78.1639 | 103.5629 |
| iTransformer | 0.9577 | 83.2604 | 120.8423 |
| FEDformer | 0.9316 | 114.4395 | 153.7248 |
| PatchTST | 0.9162 | 118.5022 | 170.0605 |
| FreTS | 0.9029 | 126.8714 | 183.1028 |
| Pyraformer | 0.8888 | 135.9388 | 195.9085 |
| LightTS | 0.8796 | 149.3750 | 203.8944 |
| Koopa | 0.8654 | 158.0816 | 215.6215 |
| Autoformer | 0.8138 | 193.9856 | 253.5933 |

- Decomposition gains over raw iTransformer: ICEEMDAN improved R²/MAE/RMSE by 1.68%/14.49%/21.37%; CEEMD 1.58%/13.51%/19.76%; EEMD 1.14%/3.42%/13.89%.
- Full model improves 1.39% over ICEEMDAN–iTransformer and 3.09% over plain iTransformer; ablation error curves stay smooth while baseline errors reach ~200 MW during daytime peaks.
- BWO converged faster and to better minimum-envelope-entropy fitness than GWO, DA, CSA.

## 💡 Limitations & Identified Research Gaps
- Model fusion (decomposition + optimization + deep forecaster) adds computational burden at training time; acceptable but must be managed for real-time operation.
- Single-country dataset (Singapore), system-level load only — no EV-station or spatio-temporal evaluation; no probabilistic/uncertainty quantification.
- Deterministic point forecasts only; decomposition performed per-split requires care against information leakage in operational deployment.

## 📚 BibTeX & Citation Reference
```bibtex
@article{zheng2025bwoiceemdanitransformer,
  author  = {Zheng, Danqi and Qin, Jiyun and Liu, Zhen and Zhang, Qinglei and Duan, Jianguo and Zhou, Ying},
  title   = {{BWO--ICEEMDAN--iTransformer}: A Short-Term Load Forecasting Model for Power Systems with Parameter Optimization},
  journal = {Algorithms},
  volume  = {18},
  number  = {5},
  pages   = {243},
  year    = {2025},
  doi     = {10.3390/a18050243}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — scaled dot-product attention underpinning iTransformer (ref. [15])
- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — base forecaster, variate-token inversion (ref. [19])
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — baseline decomposition transformer (ref. [28])
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — era context for efficient TS forecasting baselines (FreTS/LightTS lineage)
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — patched-channel baseline (ref. [31])
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]] — long-sequence transformer family context (FEDformer ref. [26])
- Related vault papers on hybrid/decomposition EV forecasting: [[2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]], [[2023_Cheng_VMD_Prophet_LSTM]], [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]]
