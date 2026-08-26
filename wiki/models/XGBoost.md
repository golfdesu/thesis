---
type: model
name: Extreme Gradient Boosting (XGBoost)
category: Machine Learning / Gradient Boosted Decision Trees
tags:
  - model
  - xgboost
  - machine-learning
  - decision-trees
---

# 🧠 Extreme Gradient Boosting (XGBoost)

## Overview
XGBoost is an optimized gradient boosting decision tree framework. It builds an ensemble of weak decision trees sequentially using second-order Taylor expansion of the loss function and regularized objective functions.

## Key Mathematical Equations
- **Objective Function at Iteration $t$**:
  $$\mathcal{L}^{(t)} = \sum_{i=1}^N l\left(y_i, \hat{y}_i^{(t-1)} + f_t(x_i)\right) + \Omega(f_t)$$
- **Second-Order Taylor Approximation**:
  $$\mathcal{L}^{(t)} \approx \sum_{i=1}^N \left[ l(y_i, \hat{y}^{(t-1)}) + g_i f_t(x_i) + \frac{1}{2} h_i f_t^2(x_i) \right] + \gamma T + \frac{1}{2} \lambda \sum_{j=1}^T w_j^2$$
  Where $g_i = \partial_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$ and $h_i = \partial^2_{\hat{y}^{(t-1)}} l(y_i, \hat{y}^{(t-1)})$.

## Application in EV Charging Load Forecasting
- Outperformed complex deep learning architectures (CNN-LSTM, TCN) across year-long rolling Day-Ahead Market (DAM) forecasts on the Palo Alto EV dataset ([[2024_Bampos_EV_Load_Forecasting_DAM]]).
- Excellent generalization on tabular feature sets without suffering from deep learning overfitting.

## Literature References
- [[2024_Bampos_EV_Load_Forecasting_DAM]] - Comprehensive 1-year benchmark showing XGBoost achieved top nMAE (5.387%) for day-ahead market bidding.

## 📚 Literature Usage
- 2024 — [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] : XGBoost quantile baseline maxes at 80.21% PICP on target domains vs MQ-TCN's transfer-learned 96.88% (NREL, 2 weeks of data).
- 2024 — [[2024_Ke_Divide_Conquer_Transformer_EV]] : XGBoost F1@.5 = 83.43% for 1–10 min-ahead EV charging-event detection vs DCT-EV 87.35% and Random Forest 22.14%.
- 2025 — [[2025_Khan_Transformer_BiLSTM_Price_Forecasting]] : XGBoost NYISO day-ahead MAE $3.1634/RMSE $7.7484 — beaten by Transformer-BiLSTM at $2.7818/$6.4937 (−12.0% MAE).
- 2025 — [[2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] : standalone XGBoost test MAE 2.6697 kWh (R² 0.6463), most stable model in walk-forward CV (0.1080); core member of the winning boosting ensemble (MAE 2.6432).
- 2026 — [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] : STL decomposition + stacked meta-learning outperforms the gradient-boosting family — ACN MAE 0.614/MAPE 12.71%, trained in 0.108 s.
- 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] : XGBoost badly behind TFT on Palo Alto daily-scale load (RMSE 2.748 vs 0.71; weather-integrated normalized MSE 0.02484 vs 0.001764).
- 2026 — [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] : XGBoost as leakage-free surrogate mapping context/weather day-pair similarity to pattern-match labels (AUC >0.93), beating KNN and LightGBM matchers.
- 2026 — [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]] : XGBoost competitive only at station-level granularity (best Palo Alto short-term station MAE ≈ 0.87, lowest RMSE there and mid-term) but loses consistently to Transformer/GRU/LSTM at region and city aggregation scales.
- 2024 — [[2024_Ma_LASSO_BPNN_Mid_Term_EV_Load]] : LASSO-XGBoost overfits tiny monthly Qingpu data (13 points) — strong training-set fit but poor test accuracy vs LASSO-BPNN, attributed to tree-model complexity vs small sample size.
