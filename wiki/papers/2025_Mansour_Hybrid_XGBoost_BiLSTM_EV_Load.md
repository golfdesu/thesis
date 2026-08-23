---
type: paper
title: "Electric vehicles charging stations load forecasting based on hybrid XGBoost-BiLSTM model"
authors: [Hany S. E. Mansour, Amira S. Mohamed, M. Abdel-Aziz]
year: 2025
journal_conference: "Scientific Reports 16:374"
doi_url: "https://doi.org/10.1038/s41598-025-29739-z"
models_used: ["[[XGBoost]]", "[[BiLSTM]]", "[[LightGBM]]", "[[Stacking_Ensemble]]", "[[CNN]]", "[[TCN]]", "[[Transformer]]", "[[SARIMAX]]", "[[Prophet]]"]
datasets_used: ["[[Caltech_ACN_Dataset]]", "[[Synthetic_Cross_Site_EVCS_Dataset]]"]
features_used: ["[[kWhDelivered]]", "[[Charging_Duration_Log]]", "[[Arrival_Departure_Time]]", "[[Hour_Of_Day]]", "[[Day_Of_Week]]", "[[Lag_Features]]", "[[Rolling_Mean_Features]]", "[[Holiday_Indicator]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[MAE]]", "[[MSE]]", "[[RMSE]]", "[[R2_Score]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Electric vehicles charging stations load forecasting based on hybrid XGBoost-BiLSTM model

## 🎯 Main Objective & Contribution
- Short-term, hourly, **station-level** EV charging load forecasting of session energy delivered ([[kWhDelivered]]) for energy management and grid stability.
- Contributions:
  - **Hybrid 3**: a hybrid [[XGBoost]]–[[BiLSTM]] **stacking ensemble** with an XGBoost meta-learner that learns optimal nonlinear combinations of base-learner predictions.
  - Comprehensive benchmarking against **24 baseline models** spanning statistical (Persistence, Seasonal Naïve, SARIMAX, Prophet), ML (XGBoost, LightGBM), DL (CNN, TCN, Transformer, BiLSTM), and ensemble families (boosting/bagging/stacking/weighted), plus two alternative hybrids (Hybrid 1 feature concatenation; Hybrid 2 sequential prediction fusion).
  - Five-fold walk-forward validation, one-way ANOVA significance testing, component-wise ablation, and cross-site external validation on a synthetic ~1.96M-session dataset.

## 🧠 Methodology & Model Architecture
- **Hybrid 3 pipeline**: (1) optimized XGBoost base regressor (Optuna-tuned n_estimators/max_depth/learning_rate) trained on scaled features; (2) BiLSTM with three bidirectional LSTM layers (128, 64, 64 units), L2 = 0.0001, dropout = 0.07, learning rate 0.0005 (AdamW), batch size 128, on 3D reshaped input; (3) their predictions stacked column-wise into meta-feature matrices; (4) XGBoost meta-learner (default params, seed 42) trained on meta-features to produce final prediction.
- **Preprocessing**: IQR outlier capping (Q1−1.5·IQR to Q3+1.5·IQR) on duration, charging_duration, kWhDelivered; 17 engineered features — hour, day_of_week, month, season, is_weekend, is_holiday (Dec/Jan), cyclical hour_sin/hour_cos, day_of_year, week_of_year, duration, charging_duration, **charging_duration_log** (skew 1.24→0.70), interaction terms (hour×charging, weekend×charging), lag features lag_1_log/lag_2_log/lag_3_log and rolling_mean_3_log/rolling_mean_5_log; log-transformed target; 80/20 split without shuffling, seed = 42.
- **Key Equations**:
  - **Eq. 1 — Mean Squared Error**:
    $$ \text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2 $$
  - **Eq. 2 — Root Mean Squared Error**:
    $$ \text{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2} $$
  - **Eq. 3 — Mean Absolute Error**:
    $$ \text{MAE} = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i| $$
  - **Eq. 4 — Coefficient of determination**:
    $$ R^2 = 1 - \frac{\sum_{i=1}^{M}(\hat{y}_i - y_i)^2}{\sum_{i=1}^{M}(y_i - \bar{y})^2} $$
  - **Eq. 5 — ANOVA effect size** ($F$: F-statistic, $k$: number of models, $n$: observations):
    $$ \eta^2 = \frac{F \cdot (k-1)}{F \cdot (k-1) + n} $$
  - Baseline forecast rules: Persistence $\hat{y}_t = y_{t-1}$; Seasonal Naïve $\hat{y}_t = y_{t-24}$; SARIMAX order (1,1,1) seasonal (1,1,1,24); Transformer: 2 multi-head attention layers (4 heads, key dim 64); TCN dilations [1,2,4], 64 filters.
- **Environment**: 2× NVIDIA Tesla T4 (16 GB), CUDA 12.6; TensorFlow/Keras for DL, CPU for tree ensembles.

## 📊 Dataset & Input Features
- **ACN-Caltech** ([Adaptive Charging Network dataset](https://ev.caltech.edu/dataset)): workplace/mixed-use public parking facility at Caltech campus; **55 charging stations**; **1,329 days** from April 25, 2018 to September 13, 2021; **31,424 raw sessions** preprocessed to **14,496 cleaned sessions** (outliers capped, lags aligned). Fields: connectionTime, disconnectTime, doneChargingTime (ISO 8601), kWhDelivered (target), station/space/site/cluster IDs, userInputs.
- **Cross-site synthetic dataset**: **1,965,239 simulated sessions** from a distinct generic EVCS site; kWhDelivered clipped to 0–100 kWh; synthetic meteorology seeded Gaussian: temperature T~N(20 °C, 5), humidity H~N(60%, 15); mean delivered 9.44 kWh (SD 5.70), mean duration 3.80 h.
- **Data availability**: ACN dataset publicly available at https://ev.caltech.edu/dataset ; the synthetic cross-site dataset was generated for validation ("available at" — no URL printed in the text).
- **Features**: temporal (hour, day_of_week, month, season, weekend/holiday flags, sin/cos hour, day/year, week/year), charging dynamics (duration, charging_duration, log variants, interactions), history (3 lags + rolling means on log duration). SHAP confirms **charging_duration_log as dominant predictor (importance 0.376)**.

## 📈 Performance & Results
- **Cleaned data test set (Table 7)**: Hybrid 3 **MAE 2.6870 kWh / RMSE 3.9825 kWh / R² 0.6395** — 3.4% better than standalone BiLSTM (MAE 2.7816, R² 0.5950), ranked 4th overall. Best model: Boosting (XGBoost+BiLSTM+LightGBM) MAE 2.6432 / R² 0.6437; Weighted Blending/Sum (XGB+BiLSTM+LGBM) 2.6438 / R² 0.6445; LightGBM 2.6523 / R² 0.6559; XGBoost 2.6697 / R² 0.6463; CNN 2.6859; SARIMAX 2.8947; Prophet 2.8441; Persistence 6.7029 (R² −0.95); Transformer 4.8141 (R² −0.007).
- **Original (outlier-retained) data (Table 8)**: Hybrid 3 led by test MAE **3.5431 kWh / RMSE 5.9546 / R² 0.5285**, showing robustness to noise; TCN unstable (train MAE 3246 kWh).
- **Walk-forward validation (5 folds)**: Hybrid 3 lowest mean **MAE 2.5351 kWh (SD 1.2885)** and highest mean **R² 0.6289**, but high variability (CV 0.5082); best fold MAE 1.27 kWh / R² 0.91. XGBoost (mean MAE 3.0963, CV 0.1080) and LightGBM (3.1581, CV 0.1226) more stable → preferable for real-time deployment.
- **ANOVA**: F = 1.624, p = 0.2073 (no statistically significant difference among top models), but large effect size η² = 0.2062 → practically relevant.
- **Ablation (Table 14 vs abstract)**: removing meta-learner is most damaging (**MAE 2.687→3.5071, +30.5%**, Cohen's d = 0.22); removing base learners +19.9% (3.2228); removing feature engineering +14.8% (3.0860); all p < 0.001. (Abstract/intro cite +13.7%/+18.8%/+29.2%.)
- **Cross-site transfer (no retraining, n≈1.96M)**: all models degraded ~53% in MAE (paired t-test p < 0.001, Cohen's d = 6.86). Hybrid 3 MAE **4.1587 kWh, R² 0.0129**; best transfer: Bagging ensembles MAE 3.082 / R² 0.357; LightGBM 3.199 / R² 0.322; BiLSTM collapsed (MAE 6.133, R² −1.02).
- **Exogenous adaptation experiment**: retraining only the meta-learner with added synthetic temperature/humidity improved cross-site performance from MAE 4.16 → **2.94 kWh, R² 0.01 → 0.37** (29.3% improvement, p < 0.001) in only 0.02 s.
- **Efficiency**: Hybrid 3 trains in 2.52 s, tests in 0.01 s; LightGBM fastest (0.10 s train); Hybrid 1 slowest (1471 s train).

## 💡 Limitations & Identified Research Gaps
- Single real site (ACN-Caltech) training limits geographic/operational generalization — demonstrated by weak zero-shot cross-site transfer (R² ≈ 0.01); domain adaptation or retraining needed.
- Heavy reliance on accurate charging-duration data, which may be unavailable for long-horizon forecasts; temporal features are overshadowed, so time-of-use/grid-event-driven variation is poorly captured.
- High walk-forward CV (0.51) indicates sensitivity to temporal drift → periodic (e.g., monthly) retraining advised.
- Future work: incorporate weather/electricity prices/demand-response events; reinforcement-learning-based forecast-to-control; adaptive ensemble weighting; lightweight hybrids; enhanced SHAP/attention explainability.

## 📚 BibTeX & Citation Reference
```bibtex
@article{mansour2025hybrid,
  title   = {Electric vehicles charging stations load forecasting based on hybrid XGBoost-BiLSTM model},
  author  = {Mansour, Hany S. E. and Mohamed, Amira S. and Abdel-Aziz, M.},
  journal = {Scientific Reports},
  volume  = {16},
  pages   = {374},
  year    = {2025},
  doi     = {10.1038/s41598-025-29739-z}
}
```

## 🔗 Key References & Citation Graph
- ACN-Data public EV charging dataset — https://ev.caltech.edu/dataset (ref. [27])
- Chen & Guestrin, XGBoost: A Scalable Tree Boosting System, KDD 2016, doi:10.1145/2939672.2939785 (ref. [28])
- Huang, Xu & Yu, Bidirectional LSTM-CRF Models for Sequence Tagging, arXiv:1508.01991 (ref. [29])
- [[2021_Day_Ahead_Forecast_of_Electric_Vehicle_Charging_Demand_with_Deep_Neural_Networks]] — Van Kriekinge et al., day-ahead DNN EV charging demand (refs. [6], [19])
- [[2019_Short_Term_Load_Forecasting_for_Electric_Vehicle_Charging_Stations_Based_on_Deep_Learning_Approaches]] — Zhu et al., deep learning EV station baselines (ref. [17])
