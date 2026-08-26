---
metric: Mean Absolute Percentage Error (MAPE)
category: point-forecast-metric
formula: "mean(|y_pred - y_true| / |y_true|) * 100%"
unit: Percentage (%)
last_updated: 2026-08-02
tags: [metric, MAPE, point-forecast, percentage-error]
---

# 📐 Mean Absolute Percentage Error (MAPE)

## Definition

**MAPE** measures the average percentage deviation of predictions from actual values. It expresses forecast accuracy in relative (percentage) terms, making it scale-independent and useful for comparing models across stations with different load magnitudes.

$$\text{MAPE} = \frac{1}{n} \sum_{t=1}^{n} \left| \frac{\hat{y}_t - y_t}{y_t} \right| \times 100\%$$

Where:
- $\hat{y}_t$ = predicted value at time $t$
- $y_t$ = actual value at time $t$
- $n$ = number of prediction steps

## Properties

| Property | Description |
|----------|-------------|
| **Unit** | Percentage (%) — scale-free |
| **Lower is better** | ✅ Yes |
| **Interpretability** | High — directly interpretable as % error |
| **Outlier sensitivity** | Moderate |
| **Zero-crossing problem** | ❌ Undefined when $y_t = 0$ (division by zero) |

## Critical Limitation for EV Load Forecasting

> [!WARNING]
> **Zero-load problem**: EV charging stations frequently have periods of zero load (e.g., overnight at workplace stations). MAPE is mathematically undefined when $y_t = 0$, making it unreliable as a standalone metric for EV load forecasting with sparse demand profiles.
>
> **Workaround**: Use only on non-zero timesteps, or use **SMAPE** (Symmetric MAPE) instead.

## Variants

| Variant | Formula | Advantage |
|---------|---------|-----------|
| **MAPE** | $\frac{|\hat{y} - y|}{|y|}$ | Standard, widely used |
| **SMAPE** | $\frac{2|\hat{y} - y|}{|\hat{y}| + |y|}$ | Handles near-zero values better |
| **NMAE** | $\frac{\sum|\hat{y} - y|}{\sum|y|}$ | Aggregate normalization, avoids per-step division |
| **WMAPE** | Weighted by actual values | Reduces influence of small-load periods |

NMAE (Normalized MAE) used in [[2019_Zhu_ApplSci_EV_Load_Forecasting]]:
$$\text{NMAE} = \frac{\sum_{t=1}^{n} |\hat{y}_t - y_t|}{\sum_{t=1}^{n} |y_t|}$$

## Usage in EV Load Forecasting Papers

| Paper | MAPE / Variant | Result |
|-------|---------------|--------|
| [[2024_Feng_LSTM_Transformer_EV_Consumption]] | MAPE | 4.63% (SOC & range prediction) |
| [[2019_Zhu_ApplSci_EV_Load_Forecasting]] | NMAE | Primary metric for GRU feature comparison |
| [[2024_Bampos_EV_Load_Forecasting_DAM]] | MAPE | Included in DAM benchmark reporting |
| [[2025_Tian_MSSTGAN_City_EV_Load]] | MAPE | City-level spatial-temporal evaluation |
| [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] | MAPE | 96-hour MFT benchmark |
| 2001 — [[2001_Hippert_Neural_Networks_STLF_Review]] | MAPE | Dominant reporting metric across 1990s ANN-based STLF literature reviewed. |
| 2015 — [[2015_Raza_Review_AI_Load_Demand]] | MAPE | Catalogued as standard accuracy measure in AI load-demand forecasting review. |
| 2021 — [[2021_Zhang_Probabilistic_Queuing_EV_Load]] | MAPE | WT-CNN spring MAPE **3.29%** vs BPNN 10.56%, SVM-RBF 8.18%, SAE 9.46%. |
| 2022 — [[2022_Cao_Robust_Deep_Gaussian_Process_Load]] | MAPE | Reported alongside RMSE/MAPE for COVID-disrupted city load with DGP + mobility features. |
| 2024 — [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] | MAPE + SMAPE | Dual percentage metrics; complemented by Qualified/Accuracy Rate, AIW and Winkler score. |
| 2024 — [[2024_Helmy_Autoformer_EV_Charging]] | MAPE | Autoformer ≈35% flat over 30/60/90 days vs LSTM degrading to 75.4% at 90 days. |
| 2024 — [[2024_Qu_Physics_Informed_GAT_EV_Load]] | MAPE | PAG improved MAPE by 13.17% vs LSTM and 8.97% vs SOTA spatiotemporal baselines. |
| 2024 — [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] | MAPE | STMGCN multi-station evaluation alongside MSE/MAE/RMSE. |
| 2025 — [[2025_Alghamdi_REST_Network_Port_EV]] | MAPE | Headline **MAPE = 6.5%** (RMSE 9.8 kW) for port EV charging demand ensemble. |
| 2025 — [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] | MAPE | Data 2 volume MAPE 0.09 — ~50% cut vs ChatEV/GPT4TS (0.12→0.09 / 0.18→0.09). |
| 2025 — [[2025_Khan_Transformer_BiLSTM_Price_Forecasting]] | sMAPE | Symmetric variant used for LMP price forecasting on NYISO/PJM/MISO. |
| 2026 — [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] | MAPE (+ε guard) | Uses $10^{-10}$ denominator guard: STL-Hybrid **12.71%** vs Informer 74.17% (>88% reduction). |
| 2026 — [[2026_Hao_Mamba_KAN_HyKANet_EV]] | MAPE | HyKANet average MAPE 15.33 (×10² units) vs PAG 16.87 across 15–60 min horizons. |
| 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] | MAPE + SMAPE | TFT hourly MAPE 16.17%/SMAPE 8.02% vs LSTM 36.9%; daily-scale MAPE 1.20% with weather covariates (ε-policy guard). |
| 2026 — [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] | MAPE | TriCast avg MAPE 15.41 (×10² units), −9.8% vs best prior at 15-min horizon over 16 baselines on UrbanEV. |
| 2026 — [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] | MAPE | SGD/RF traditional ML best on relative error across 12 cities; applicability generally beats transferability on MAPE. |
| 2024 — [[2024_Shi_Naihao_Prediction_Interval_EV_Loads]] | MAPE | EV-containing feeder MAPE 21.36% → **9.21%** from the single charging-habit feature CH(t) — back to near the EV-free level (9.07%). |
| 2026 — [[2026_Hong_SSM_Transformer_LSTM_Grid_Benchmark]] | MAPE | Primary benchmark metric across six ISOs × W∈{24–168} h: PatchTST avg **5.59%** (15/30 wins), PowerMamba/S-Mamba 5.72/5.80%, iTransformer 6.14%, LSTM 6.83%; weather cuts iTransformer by −1.62 pp. |

## Relationship to Other Metrics

$$\text{MAE} = \bar{y} \times \text{MAPE} \quad \text{(approximately, when errors are small)}$$

- Use **MAPE** when load values are consistently non-zero and you want percentage-relative comparison.
- Use **[[MAE]]** or **[[RMSE]]** for absolute error in original units.
- Use **[[V2G_SVE]]** when downstream scheduling performance is the ultimate objective.

## Related Pages

- [[MAE]]
- [[RMSE]]
- [[V2G_SVE]]
