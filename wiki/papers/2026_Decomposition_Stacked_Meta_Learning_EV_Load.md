---
type: paper
title: "Decomposition and Stacked Meta-Learning for Short-Term Electric Vehicle Load Forecasting"
authors: [Syed Sajid Ullah, Gang Li, Muhammad Zunair Zamir, Abdul Malik, Saeed Mian Qaisar, Mudassar Riaz]
year: 2026
journal_conference: "IEEE Transactions on Smart Grid"
doi_url: "https://doi.org/10.1109/TSG.2026.3677496"
models_used: ["[[STL_Hybrid]]", "[[STL]]", "[[Ridge_Regression]]", "[[XGBoost]]", "[[Random_Forest]]", "[[Gradient_Boosting_Regressor]]", "[[Prophet]]", "[[CatBoost]]", "[[Informer]]", "[[CNN-LSTM-AM]]", "[[DeepBoost]]"]
datasets_used: ["[[Caltech_ACN]]", "[[ChargePlace_Scotland]]", "[[Palo_Alto_EV]]", "[[Paris_Belib_EV]]"]
features_used: ["[[Historical_Load]]", "[[Lag_Features]]", "[[Calendar_Features]]", "[[Trend_Component]]", "[[Seasonal_Component]]", "[[Residual_Component]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[MAPE]]", "[[R_squared]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Decomposition and Stacked Meta-Learning for Short-Term Electric Vehicle Load Forecasting

## 🎯 Main Objective & Contribution
- Short-term EV load forecasting (STLF) must jointly capture **multi-scale temporal structure** (diurnal/weekly/annual cycles + adoption trend), **nonlinear interactions**, and **cross-dataset heterogeneity**; existing statistical/ensemble/DL models rely on implicit sequence learning, uniform learners across decomposed components, or simple linear fusion.
- Contributions:
  1. A decomposition-driven hybrid framework integrating **STL** with a stacked ensemble architecture that explicitly disentangles multi-scale temporal structures before fusion.
  2. **Component-specific modeling**: Ridge regression → smooth trend; [[XGBoost]] → nonlinear seasonal patterns; [[Random_Forest]] → stochastic residual fluctuations.
  3. Stacked fusion via a **Gradient Boosting Regressor (GBR) meta-learner** (adaptive nonlinear weighting instead of fixed averaging).
  4. Evaluation on four real-world EV charging datasets of varying scale/variability, plus ablation and runtime analyses.

## 🧠 Methodology & Model Architecture
- **STL decomposition** ("additive decomposition"):
  $$ y_t = T_t + S_t + R_t $$
  computed iteratively via Loess local regression ("Loess smoothing equations"):
  $$ S_t = Loess(y_t, w_S), \qquad T_t = Loess(y_t - S_t, w_T), \qquad R_t = y_t - T_t - S_t $$
  ($w_S$, $w_T$ seasonal/trend smoothing windows; robust-weight refinement pass).
- **Ridge regression for the trend** ("ridge objective"):
  $$ \hat{\beta} = \arg\min_\beta \sum_{t=1}^{n}\left(T_t - x_t^\top\beta\right)^2 + \lambda\|\beta\|_2^2 $$
  ($\alpha=1.0$ after grid search).
- **XGBoost for the seasonal component** ("XGBoost objective"):
  $$ L(\phi) = \sum_i l\left(y_i,\ \hat{y}_i^{(t-1)} + f_t(x_i)\right) + \Omega(f_t) $$
  (n_estimators=300, max_depth=6, lr=0.1, subsample=0.9, colsample_bytree=0.9).
- **Random Forest for the residual component** ("RF averaging"):
  $$ \hat{y} = \frac{1}{B}\sum_{b=1}^{B} T_b(x) $$
  (n_estimators=300, max_depth=10, min_samples_split=2, min_samples_leaf=1).
- **Meta-learning formulation** ("expected task loss"): $\theta^* = \arg\min_\theta E_{T\sim p(T)}[L_T(f_\theta(D^{train}_T), D^{test}_T)]$; metric-based prototype classification $\hat{y}=\arg\min_c \sum_{x_i\in S_c} d_\phi(x,x_i)$; MAML-style adaptation $\theta'_T = \theta_0 - \alpha\nabla_\theta L_T(f_\theta(D^{train}_T))$.
- **Unified optimization objective** — per-component empirical risk minimization ("component learner loss"):
  $$ \min_{\theta_c} \frac{1}{n}\sum_{i=1}^n L(y_i^c, \hat{y}_i^c) + \Omega(\theta_c), \quad c\in\{T,S,R\} $$
  meta-stage GBR fusion ("stacked meta-fusion objective"):
  $$ \min_\phi \frac{1}{n}\sum_{i=1}^n \left(y_i - F_\phi(\hat{T}_i, \hat{S}_i, \hat{R}_i)\right)^2 $$
- Component prediction ("component forecast"): $\hat{y}^c(t) = f_c(X_t)$; final forecast ("ensemble output"):
  $$ \hat{y}(t) = F_{meta}\left(\hat{y}_{trend}(t), \hat{y}_{seasonal}(t), \hat{y}_{residual}(t)\right) $$
- Metrics ("MAE / RMSE / MAPE"):
  $$ MAE = \frac{1}{n}\sum_{i=1}^n |y_i-\hat{y}_i|, \quad RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i-\hat{y}_i)^2}, \quad MAPE = \frac{1}{n}\sum_{i=1}^n \left|\frac{y_i-\hat{y}_i}{y_i+10^{-10}}\right|\times 100 $$
- Setup: 80:20 chronological split per component; time-series cross-validation with early stopping (patience=10); PyTorch 1.10/CUDA 11.3/Python 3.8 on RTX 3090; Adam, batch 32, lr 0.001.

## 📊 Dataset & Input Features
- Four real-world public EV charging datasets (hourly energy delivered, kWh; Table II):

| Dataset | Period | Samples | Sampling | Train/Test | Mean±Std (kWh), CV |
|---|---|---|---|---|---|
| [[Caltech_ACN]] (Caltech ACN-Portal) | 2015–2021 | 56,949 | 1 h | 45,559/11,390 | 5.844±7.645, CV 1.308 |
| [[ChargePlace_Scotland]] | 2016–2021 | 63,936 | 1 h | 51,149/12,787 | 3.048±7.599, CV 2.493 |
| [[Palo_Alto_EV]] | 2011–2020 | 259,352 | 1 h | 207,482/51,870 | 4.071±4.181, CV 1.027 |
| [[Paris_Belib_EV]] | 2015–2021 | 5,780 | 1 h | 4,624/1,156 | 0.213±0.470, CV 2.202 |

- Preprocessing: data cleaning (remove incomplete/corrupt records), noise reduction/outlier filtering, normalization. Features: load-intrinsic lag-based and time-aware features feeding both base learners and the meta-learner; no exogenous variables.
- **Dataset URLs** (from references):
  - ACN: https://ev.caltech.edu/dataset (accessed 2025-08-27)
  - Perth & Kinross Council / ChargePlace Scotland: https://data.pkc.gov.uk/datasets/perth-kinross::electric-vehicle-charging-points
  - Palo Alto Open Data: https://data.paloalto.gov/datasets/194693/electric-vehicle-charging-station-usage-july-2011-dec-2020/
  - Paris (Belib'): https://opendata.paris.fr/explore/dataset/belib-points-de-recharge-pour-vehicules-electriques-disponibilite-temps-reel/
- IEA/BNEF context links: https://www.iea.org/reports/net-zero-by-2050 , https://www.iea.org/reports/renewables-2023 , https://about.bnef.com/electric-vehicle-outlook/
- **Data availability statement**: "The datasets used in this study are available from the corresponding author upon reasonable request."

## 📈 Performance & Results
- **ACN dataset (Table VIII)**: Proposed STL-Hybrid **MAE 0.614, RMSE 0.797, MAPE 12.71%** vs Informer (4.667/8.734/74.17%), CatBoost (5.126/7.586/85.88%), Prophet (10.392/23.911/121.37%), CNN-LSTM-AM (7.071/9.819/166.58%), DeepBoost (7.146/9.884/168.86%) → **>90% RMSE and >88% MAPE reduction vs strongest benchmark (Informer)**.
- **Other datasets**: Palo Alto — proposed 1.302/1.646/14.51% vs CatBoost 2.628/3.542/40.18%; Perth — 1.206/1.531/11.32% vs CatBoost 5.038/7.291/156.7%; Paris — 0.993/1.336/12.45% vs CatBoost 3.928/6.272/142.06%. Consistent wins across scales from 259,352 samples down to 5,780 samples.
- **Robustness (Table VI)**: 5-fold time-series CV mean MAE/RMSE/MAPE = 0.614/0.797/12.71% with tiny stds (0.021/0.035/0.84); hyperparameter perturbations (trees ±20%, depth ±2, LR ±0.02) change MAE by at most ~0.02 — low tuning sensitivity.
- **Ablation (Table VII)**: removing seasonality is worst (∆MAPE +3.2%, ∆R² −0.059); removing trend costs +1.5% MAPE, −0.027 R²; removing residual costs +0.7% MAPE, −0.011 R² — all three components justified, seasonality dominant.
- **Runtime (Table IX, ACN)**: proposed trains in **0.108 s** and infers in **0.004 s** — faster than Prophet (0.486 s), CNN-LSTM-AM (1.207 s), DeepBoost (2.347 s), CatBoost (3.056 s), Informer (1.372 s).

## 💡 Limitations & Identified Research Gaps
- Relies only on load-intrinsic features; **no exogenous variables** (temperature, precipitation) yet — weather-aware features are planned future work.
- No probabilistic/uncertainty-quantified forecasts (deterministic point predictions only); probabilistic extension planned.
- No adaptive online learning mechanism for evolving charging environments; scalability/real-time adaptation left open.
- STL assumes additive structure; strong nonstationarity or multiplicative seasonality may require alternative decompositions.

## 📚 BibTeX & Citation Reference
```bibtex
@article{ullah2026decomposition,
  title   = {Decomposition and Stacked Meta-Learning for Short-Term Electric Vehicle Load Forecasting},
  author  = {Ullah, Syed Sajid and Li, Gang and Zamir, Muhammad Zunair and Malik, Abdul and Qaisar, Saeed Mian and Riaz, Mudassar},
  journal = {IEEE Transactions on Smart Grid},
  year    = {2026},
  doi     = {10.1109/TSG.2026.3677496}
}
```

## 🔗 Key References & Citation Graph
- [[2021_Informer_Beyond_Efficient_Transformer]] — Informer baseline
- [[2020_NBEATS_Interpretable_Time_Series_Forecasting]] — interpretable decomposition-style forecasting lineage
- Related vault papers: [[2025_BWO_ICEEMDAN_iTransformer]], [[2023_VMD_Prophet_LSTM]], [[2026_Hybrid_XGBoost_BiLSTM_EV_Load]], [[2019_EV_Load_Forecasting]], [[2023_DLinear_Are_Transformers_Effective_LTSF]]
