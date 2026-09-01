---
title: R-squared (Coefficient of Determination, R²)
type: metric
metric: R-squared (Coefficient of Determination, R²)
category: point-forecast-metric
formula: "R² = 1 − Σ(y−ŷ)² / Σ(y−ȳ)²"
unit: Dimensionless (typically 0–1; can be negative)
last_updated: 2026-08-23
tags: [metric, r-squared, r2, goodness-of-fit, point-forecast]
---

# 📐 R-squared (R²)

## Definition

**R²** expresses the proportion of variance in the target explained by the forecast:

$$R^2 = 1 - \frac{\sum_{i=1}^{n}(y_i - \hat{y}_i)^2}{\sum_{i=1}^{n}(y_i - \bar{y})^2}$$

$R^2 = 1$ is a perfect forecast; $R^2 = 0$ matches the mean baseline; negative values mean the model is worse than predicting the mean.

## Properties

| Property | Description |
|----------|-------------|
| **Unit** | Dimensionless — comparable across stations/scales |
| **Higher is better** | ✅ Yes (≤ 1) |
| **Outlier sensitivity** | High (squared terms) — related to [[RMSE]] behavior |
| **Caution for sparse EV load** | ⚠️ Inflated by variance of the series itself; report with [[MAE]]/[[MAPE]] |

## Usage in EV / Load Forecasting Papers

| Paper | Result |
|-------|--------|
| 2019 — [[2019_Zhu_EV_Load_Forecasting]] | R² reported for minute-level BiLSTM/SAE EV load forecasting. |
| 2022 — [[2022_Zhang_GCN_TRN_EV_Availability]] | GCN-TRN evaluated with R² alongside Accuracy Index and Explained Variance Score. |
| 2023 — [[2023_Cheng_VMD_Prophet_LSTM]] | VMD enables Prophet-LSTM to handle volatile sequences — raw Prophet alone collapses to R² ≈ 0.49. |
| 2023 — [[2023_Ziyabari_Multi_Branch_ResTrans_Solar]] | ResTrans reached $R^2 = 97\%$ for solar irradiance spatial-temporal forecasting. |
| 2024 — [[2024_Bampos_EV_Load_Forecasting_DAM]] | R² among benchmark metrics for day-ahead market EV load forecasting. |
| 2025 — [[2025_Alghamdi_REST_Network_Port_EV]] | RESTNet outperformed SVR/RF/CNN/VGGNet/DeepSigRNet on R² plus MAPE/RMSE. |
| 2025 — [[2025_Han_Vertical_Federated_EGAT_LSTM]] | VFL EGAT-LSTM evaluation on IEEE-33/69 test systems includes R². |
| 2025 — [[2026_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] | Hybrid 3 test R² 0.6395 vs BiLSTM 0.5950; walk-forward mean R² 0.6289; Transformer negative (R² −0.007). |
| 2025 — [[2025_Zheng_BWO_ICEEMDAN_iTransformer]] | BWO-tuned pipeline on Singapore Energy Market data reports R². |
| 2025 — [[2025_Zhu_Personalized_Federated_Learning]] | Personalized federated learning evaluated with R² on REFIT appliance-level data. |
| 2026 — [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] | CNN-LSTM-Attention R² 0.89 at 1 h (+3.49% vs GRU); degrades to 0.66–0.70 at 24–48 h. |
| 2026 — [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] | STL-Hybrid ablation: removing seasonality costs ΔR² −0.059 — seasonality is the dominant component. |
| 2024 — [[2024_Huo_Data_Driven_EVCS_Demand_Forecasting]] | Rao-1-tuned ANN R² = **0.974** at JPL (Caltech 0.885) for hourly station demand vs persistence 0.855/0.745. |

## Related Pages

- [[MAE]]
- [[RMSE]]
- [[MAPE]]
