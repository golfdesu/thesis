---
concept: Day-Ahead Load Forecasting
category: forecasting-horizon
time_range: "24–36 hours ahead"
last_updated: 2026-08-02
tags: [horizon, day-ahead, unit-commitment, energy-market]
---

# 📅 Day-Ahead Load Forecasting

## Definition

Day-ahead EV charging load forecasting covers prediction horizons of **24 to 36 hours ahead**, typically producing hourly or 15-minute resolution output for the next operating day. This is the most operationally critical horizon for energy market participation and grid scheduling.

## Temporal Resolution

| Resolution | Horizon | Primary Use Case |
|------------|---------|-----------------|
| 15 min     | 24 hours | Smart charging scheduling, TOU pricing |
| 1 hour     | 24–36 hours | Day-ahead energy market (DAM) bidding |
| 1 hour     | 36 hours | Unit commitment, reserve procurement |

## Characteristics & Challenges

- **Periodic patterns**: Strong daily and weekly seasonality in EV usage behavior.
- **Weather dependence**: Next-day temperature directly influences EV range and charging frequency.
- **Market coupling**: DAM gate closure (typically D-1 noon) requires forecasts hours before delivery.
- **Trend-seasonality decomposition**: Annual EV adoption growth creates non-stationary long-term trends.

## Common Model Approaches

| Model | Papers |
|-------|--------|
| Transformer (Vanilla) | [[2023_Koohfar_Transformer_EV_Demand]] |
| LSTM Encoder-Decoder | [[2021_VanKriekinge_Day_Ahead_EV_Demand]] |
| XGBoost + MLP (Multiplicative Decomposition) | [[2024_Bampos_EV_Load_Forecasting_DAM]] |
| Multi-Scale Fusion Transformer (MFT) | [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] |
| ADMM Neural Network (EVCB+EVSC) | [[2024_Xu_Day_Ahead_EVCB_EVSC_Parking_Lot]] |
| Meta-Probformer (few-shot) | [[2023_Huang_MetaProbformer_EV_Load]] |
| LSTM-Transformer Hybrid | [[2025_Hussain_Hybrid_LSTM_Transformer_Demand]] |

## Citing Literature

- 2001 — [[2001_Hippert_Neural_Networks_STLF_Review]] : Foundational review of day-ahead ANN load forecasting practice and pitfalls.
- 2017 — [[2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load]] : QRA turns day-ahead point forecasts into calibration-valid probabilistic forecasts (GEFCom2014).
- 2019 — [[2019_Toubeau_Deep_Probabilistic_Scheduling_Power_Markets]] : Day-ahead joint probabilistic forecasting of load/wind/solar/price for market scheduling (Belgian grid).
- 2022 — [[2022_Cao_Robust_Deep_Gaussian_Process_Load]] : Probabilistic deep GP for daily-scale city load with COVID mobility covariates.
- 2024 — [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] : MQ-TCN transfer learning for day-ahead multi-quantile station forecasting (PICP 93.62% JPL).
- 2024 — [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] : Feature-enhanced FEDM network for day-ahead probabilistic EV load.
- 2024 — [[2024_Li_DiffPLF_Conditional_Diffusion_EV]] : Conditional diffusion generates day-ahead scenarios; flexible 24/12/6/4/1-h horizons retraining-free.
- 2024 — [[2024_Zhong_V2G_SVE_Evaluation_Metric]] : V2G-SVE quantifies how day-ahead forecast quality maps to scheduling value loss.
- 2025 — [[2025_Khan_Transformer_BiLSTM_Price_Forecasting]] : Transformer-BiLSTM day-ahead LMP price forecasting on NYISO/PJM/MISO markets.
- 2025 — [[2025_Matrone_QR_LSTM_Attention_EV_Load]] : QR-LSTM day-ahead quantile forecasts (q20/q50/q80) for Utrecht office parking lot.
- 2025 — [[2025_Zheng_Coherent_Hierarchical_EV_Load]] : Coherent hierarchical day-ahead reconciliation via PICNN + DCL on ACN data.
- 2026 — [[2026_Chen_PC_M3_Mamba_EV_Clusters]] : PC-M3 clusters fleet flexibility polytopes to support day-ahead EV scheduling co-optimization.
- 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] : TFT daily-scale branch forecasts 1–7 days ahead on Palo Alto data (RMSE 0.71 kWh) with environmental covariates + conformal calibration.
- 2026 — [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] : Day-ahead similar-day selection framework (ShapeDTW/Multi-DTW + NSGA-II weights + XGBoost surrogate) cuts zone-level error ~4.5% on UrbanEV Shenzhen.
- 2024 — [[2024_Qu_Forwardformer_Day_Ahead_Load]] : Forwardformer (day-as-token encoder-dual-decoder, forward sliding/dilated/global attention) emits the full next-day curve in one inference — best ACC 98.51% (China) / 96.94% (US), SOTA on weekends/holidays via holiday-weighted dual-MSE loss.
- 2024 — [[2024_DeVilmarest_Adaptive_Probabilistic_Netload]] : Day-ahead GB half-hourly net-load (14 GSP groups) via Kalman-adapted GAM + OGD/BOA-adapted quantile regression — ≈10% RMSE reduction vs periodic retraining and >20% RPS gain on US cities during COVID.
- 2024 — [[2024_Shi_Naihao_Prediction_Interval_EV_Loads]] : Day-ahead recursive GPR feeder forecasting with EV charging-habit probability CH(t) — MAPE restored to 9.21% and PI coverage near nominal despite integrated EV loads.
- 2025 — [[2025_FernandezZapico_Stochastic_MPC_Conformal_Hub]] : GBT+EnbPI probabilistic scenarios (24 h @ 15-min load/PV; hourly prices upsampled) feed scenario-based stochastic MPC of a charging energy hub — day-ahead forecast quality valued via downstream control cost (112.76% of omniscient).
- 2026 — [[2026_Bouaachra_INLA_Spatio_Temporal_EV_Demand]] : Day-ahead daily session counts per charge point via Bayesian [[INLA_Latent_Gaussian_Model]] (ICAR/SPDE + RW2), beating per-station no-pooling XGBoost/GLM on MAE at 70–77% of Glasgow stations.

## Key Input Features

- [[Historical_Load]] (past 1–7 day window)
- [[Cyclical_Encodings]] (hour-of-day, day-of-week, month)
- [[Electricity_Tariff]] (TOU price signals for next day)
- [[Weather_Traffic]] (forecast temperature, precipitation)
- [[Arrival_Departure_Time]] (calendar-based arrival distributions)

## Key Insight: Simple Models Can Outperform Deep Learning

> [!IMPORTANT]
> [[2024_Bampos_EV_Load_Forecasting_DAM]] demonstrated that XGBoost and MLP outperform complex deep learning architectures on 36-hour rolling DAM evaluation across 4 public datasets. Multiplicative trend-residual decomposition is key to handling annual EV fleet growth.

## Evaluation Metrics

- [[MAE]], [[RMSE]], [[MAPE]] (point forecast)
- [[V2G_SVE]] (value-oriented, downstream scheduling quality)
- PICP, Winkler Score, CRPS (probabilistic intervals)

## Related Pages

- [[Short_Term_Forecasting]]
- [[Spatial_Temporal_Forecasting]]
