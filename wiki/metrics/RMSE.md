---
title: Root Mean Squared Error (RMSE)
type: metric
metric: Root Mean Squared Error (RMSE)
category: point-forecast-metric
formula: "sqrt(mean((y_pred - y_true)^2))"
unit: Same as target variable (kW or kWh)
last_updated: 2026-08-02
tags: [metric, RMSE, point-forecast, error]
---

# 📐 Root Mean Squared Error (RMSE)

## Definition

**RMSE** measures the square root of the average squared difference between predicted and actual values. It penalizes large errors more heavily than [[MAE]] due to the squaring operation.

$$\text{RMSE} = \sqrt{\frac{1}{n} \sum_{t=1}^{n} (\hat{y}_t - y_t)^2}$$

Where:
- $\hat{y}_t$ = predicted value at time $t$
- $y_t$ = actual value at time $t$
- $n$ = number of prediction steps

## Properties

| Property | Description |
|----------|-------------|
| **Unit** | Same as the target variable (kW, kWh) |
| **Scale** | Sensitive to outliers — penalizes large errors quadratically |
| **Lower is better** | ✅ Yes |
| **Interpretability** | Moderate — represents typical error magnitude in original units |
| **Differentiable** | ✅ Yes (used as training loss in some models) |

## RMSE vs MAE

| Aspect | RMSE | MAE |
|--------|------|-----|
| Outlier sensitivity | High (quadratic penalty) | Low (linear penalty) |
| Interpretability | Lower | Higher |
| Optimization | More stable gradients | Less stable near zero |
| Use case | When large errors are especially undesirable | General-purpose |

## Normalized Variants

- **NRMSE** (Normalized RMSE): $\text{NRMSE} = \frac{\text{RMSE}}{y_{\max} - y_{\min}}$ — allows comparison across stations with different load scales. Used in [[2019_Zhu_ApplSci_EV_Load_Forecasting]].
- **CV-RMSE** (Coefficient of Variation): $\text{CV-RMSE} = \frac{\text{RMSE}}{\bar{y}}$ — normalized by mean load.

## Usage in EV Load Forecasting Papers

| Paper | RMSE Result | Context |
|-------|-------------|---------|
| [[2019_Zhu_EV_Load_Forecasting]] | Reported as primary metric | Minute-level LSTM comparison |
| [[2019_Zhu_ApplSci_EV_Load_Forecasting]] | NRMSE variant | Multi-dimensional GRU features |
| [[2021_VanKriekinge_Day_Ahead_EV_Demand]] | MAE < 1 kW (RMSE secondary) | 15-min day-ahead forecasting |
| [[2023_Ziyabari_Multi_Branch_ResTrans_Solar]] | $R^2 = 97\%$ (RMSE primary) | Solar irradiance spatial-temporal |
| [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] | Primary benchmark metric | 96-hour MFT forecasting |
| [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] | Primary benchmark metric | DC fast-charging 1h/24h |
| 2013 — [[2013_Roberts_Gaussian_Processes_Time_Series]] | Standardized MSER metric | GP time-series review; normalized MSE for comparing covariance structures. |
| 2019 — [[2019_Toubeau_Deep_Probabilistic_Scheduling_Power_Markets]] | BLSTM < LSTM < MLP < RF/SVR < ARIMA | 3-layer BLSTM best RMSE on Belgian wind/load/price; recurrent models beat the TSO tool. |
| 2020 — [[2020_Huang_Ensemble_EV_Load]] | Ensemble 3.83 kWh (−1.79% vs LR) | Stacked Boulder ensemble; still best at lookback = 12 (4.00). |
| 2021 — [[2021_Zhang_Probabilistic_Queuing_EV_Load]] | WT-CNN 118.32 vs BPNN 416.69 | Spring 1-h-ahead deterministic forecast — ~72% reduction. |
| 2022 — [[2022_Zhang_GCN_TRN_EV_Availability]] | GCN-TRN 0.1067 vs baselines ≥ 0.1375 | Station availability, best across all three stations. |
| 2024 — [[2024_Qu_Physics_Informed_GAT_EV_Load]] | −5.29% vs SOTA spatiotemporal | PAG ablation: removing TPA degrades RMSE by 50.84%. |
| 2024 — [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] | STMGCN **78.831 kW** | Best overall test RMSE; noAG (TCN-only) worst at 90.681. |
| 2025 — [[2025_Alghamdi_REST_Network_Port_EV]] | **9.8 kW** headline | RESTNet ensemble vs SVR/RF/CNN/VGGNet/DeepSigRNet. |
| 2025 — [[2026_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] | Hybrid 3: 3.9825 kWh | Persistence 6.70; Transformer unstable (R² ≈ 0). |
| 2025 — [[2025_Zheng_Coherent_Hierarchical_EV_Load]] | Reported with MAE/MASE | Coherent hierarchical probabilistic evaluation on ACN. |
| 2026 — [[2026_Hao_Mamba_KAN_HyKANet_EV]] | Avg 4.67 (×10²), up to −14.8% vs PAG | Per-horizon: 2.81 (15 min) → 6.12 (60 min). |
| 2026 — [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] | STL-Hybrid **0.797** | >90% RMSE reduction vs strongest benchmark Informer (8.734). |
| 2026 — [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] | 1-h: 4.61 (**−13.83% vs GRU**) | CNN-LSTM-Transformer best at 24-h (7.68) / 48-h (8.16). |
| 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] | Hourly RMSE **1.2687 kWh** | TFT + CQR conformal calibration on Palo Alto (1–24 h); daily-scale RMSE 0.71. |
| 2026 — [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] | Avg **4.71** (×10²) | TriCast beats PIAST/FourierGNN/CityEVCP and 13 more baselines at 15–60-min horizons on UrbanEV. |
| 2026 — [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] | LightGBM 71.54 → 68.31 kW | Similar-day selection trims RMSE ~4.5% across four forecasters on UrbanEV Shenzhen. |
| 2026 — [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] | Up to **−51.21% RMSE50** | MAML-Informer probabilistic forecasting across ACN/Boulder/Palo Alto; paired t-test p = 1.52×10⁻¹². |
| 2026 — [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] | Reported via MAE/MAPE | Six-model benchmark: SGD best overall across 12 cities; performance plateaus after 3 days of training data. |
| 2026 — [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] | EVnetNL **8.781** vs Informer 9.866 | USDT dual-direction transformer; zero-shot Perth cross-domain RMSE 13.559 even beats in-domain Informer. |
| 2026 — [[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]] | **3.06 / 4.98 / 6.45** (×10⁻²) at 15/30/45 min | Best at every horizon on Shenzhen ST-EVCDP vs 13 baselines; −3.8% RMSE vs PAG at 30 min, ~13% gain at 15 min. |
| 2026 — [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]] | Normalized-domain MAE/RMSE protocol | Transformer RMSE collapses on sparse daily Dundee data (≈106 vs GRU ≈ 40s) — recursive multi-step error accumulation penalizes high-capacity encoders on short histories. |
| 2024 — [[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]] | MSE-family (squared-error) LTSF eval | TimeMachine quadruple-Mamba: Electricity T=96 MSE 0.142/MAE 0.236 vs iTransformer 0.148/0.240; ETTh1 T=720 MSE 0.458 vs 0.503; longer look-backs cut Traffic T=96 to 0.348. |
| 2024 — [[2024_Liang_BiMamba_Bidirectional_Mamba_Forecasting]] | MSE-family (squared-error) LTSF eval | Bi-Mamba+: Electricity T=96 MSE 0.140/MAE 0.238; Traffic T=96 MSE 0.375/MAE 0.258 vs iTransformer 0.395/0.268 (−4.72% avg MSE); linear memory growth on 862-channel Traffic. |
| 2024 — [[2024_Huo_Data_Driven_EVCS_Demand_Forecasting]] | ANN **6.93 kW** (JPL) / 4.50 kW (Caltech) | Rao-1-tuned one-step hourly station demand vs persistence 16.34/6.69 kW — ≈58% reduction. |
| 2024 — [[2024_Shi_Naihao_Prediction_Interval_EV_Loads]] | 25.68 → **12.53** | Day-ahead feeder RMSE with EV loads restored near the EV-free level (12.05) by the single charging-habit feature CH(t). |
| 2024 — [[2024_DeVilmarest_Adaptive_Probabilistic_Netload]] | ≈**10% nRMSE reduction** | Kalman-adapted GAM vs periodically retrained models across GB 14-GSP half-hourly net-load and US 7-city daily load (up to 8% in COVID year 2021 for GB alone). |

## Relationship to Other Metrics

$$\text{RMSE} \geq \text{MAE} \quad \text{(always, by Cauchy-Schwarz inequality)}$$

When RMSE ≫ MAE, the dataset has significant outlier events (e.g., sudden demand spikes during peak hours).

## Related Pages

- [[MAE]]
- [[MAPE]]
- [[V2G_SVE]]
