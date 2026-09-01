---
title: Short-Term Load Forecasting (STLF)
concept: Short-Term Load Forecasting (STLF)
category: forecasting-horizon
time_range: "5 minutes – 6 hours ahead"
last_updated: 2026-08-02
tags: [horizon, short-term, real-time, grid-control]
---

# ⏱️ Short-Term Load Forecasting (STLF)

## Definition

Short-term EV charging load forecasting covers prediction horizons from **5 minutes to a few hours ahead** (typically ≤ 6 hours; some multi-step probabilistic works extend to 24 hours). The primary use cases are real-time grid frequency regulation, dynamic pricing, and demand response activation.

## Temporal Resolution

| Resolution | Horizon | Primary Use Case |
|------------|---------|-----------------|
| 5–15 min   | 30–60 min | Real-time grid balancing, V2G dispatch |
| 15–30 min  | 1–4 hours | Smart charging scheduling |
| 1 hour     | 1–6 hours | Dynamic pricing, demand response |

## Characteristics & Challenges

- **High volatility**: EV arrivals and departures are stochastic and session-level.
- **Non-stationarity**: Intraday patterns are highly irregular compared to residential loads.
- **Low autocorrelation**: Short intervals have weaker temporal dependence than daily/weekly cycles.
- **Sensor latency**: Real-time meter data may have communication delays affecting input freshness.

## Common Model Approaches

| Model | Papers |
|-------|--------|
| LSTM / GRU baseline | [[2019_Zhu_EV_Load_Forecasting]], [[2019_Zhu_ApplSci_EV_Load_Forecasting]] |
| CNN-LSTM-Attention | [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] |
| Context-Aware Transformer | [[2025_Hussain_CAT_Former_Short_Term_EV]] |
| Ensemble Stacking | [[2020_Huang_Ensemble_EV_Load]] |

## Citing Literature

- 2021 — [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] : Short-term probabilistic forecasts of Dutch charging-station load with hierarchical GBRT/QRF/QRNN ensembles (EVnetNL data).
- 2023 — [[2023_Cheng_VMD_Prophet_LSTM]] : VMD decomposition + Prophet-LSTM for short-horizon volatile station load (Fujian province).
- 2023 — [[2023_Huang_MetaProbformer_EV_Load]] : Reptile-meta probabilistic Informer for few-shot short-term forecasting at newly deployed stations.
- 2024 — [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] : STMGCN at 15-min/1-h/2-h horizons — MAE degrades only 53.287 → 55.834 kW across horizons.
- 2024 — [[2024_Qu_Physics_Informed_GAT_EV_Load]] : Physics-informed GAT (PAG) for short-term pile occupancy demand with corrected price elasticity.
- 2025 — [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] : LLM-based spatio-temporal forecaster evaluated at 1–6 step horizons incl. critical-day scenarios.
- 2025 — [[2025_Han_Vertical_Federated_EGAT_LSTM]] : Vertical federated EGAT-LSTM for short-term zonal load without sharing raw grid data.
- 2025 — [[2025_Li_DC_Charging_Profiles_TFT]] : TFT session-profile prediction for DC fast charging with quantile outputs.
- 2025 — [[2026_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] : Walk-forward validated XGBoost/BiLSTM stacking for short-term station demand.
- 2025 — [[2025_Yang_Stochastic_MPC_Microgrid_EV]] : Stochastic MPC couples short-term forecasts with microgrid EV dispatch (operating cost metric).
- 2025 — [[2025_Zheng_BWO_ICEEMDAN_iTransformer]] : BWO + ICEEMDAN preprocessing sharpens iTransformer short-term accuracy on Singapore market data.
- 2026 — [[2026_Hao_Mamba_KAN_HyKANet_EV]] : HyKANet targets 15–60 min horizons explicitly; per-horizon RMSE 2.81 (15 min) → 6.12 (60 min).
- 2026 — [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] : STL decomposition + stacked meta-learning for short-term station-level load.
- 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] : Native multi-horizon TFT at hourly 1–24-h timescale with environmental covariates + CQR conformal calibration (RMSE 1.2687 kWh, PICP 96.2%).
- 2026 — [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] : TriCast tri-modal causal forecaster evaluated at 15/30/45/60-min horizons on UrbanEV Shenzhen (avg RMSE 4.71 ×10⁻²).
- 2026 — [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] : MAML-Informer probabilistic multi-step forecasting (24 steps / 6-h ahead @15-min) across ACN/Boulder/Palo Alto.
- 2026 — [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] : Six ML/DL models benchmarked for strict 1-hour-ahead station-level demand over 12 cities; SGD best overall.

## Key Input Features

- [[Historical_Load]] (past 1–24 hour window)
- [[Cyclical_Encodings]] (time-of-day, day-of-week)
- [[Weather_Traffic]] (temperature, precipitation)
- [[Arrival_Departure_Time]] (session arrival probability)

## Evaluation Metrics

- [[MAE]], [[RMSE]], [[MAPE]] (point forecast accuracy)
- CRPS, Winkler Score (probabilistic coverage)

## Related Pages

- [[Day_Ahead_Forecasting]]
- [[Spatial_Temporal_Forecasting]]

## Literature Usage
- 2024 — [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] : Decoder-only TimesFM zero-shot across Monash/Darts/ETT horizons 32-512 (variable context/horizon/granularity).
- [[2026_Khwaja_Toto_2_Scaling_Era]] — Toto 2.0 zero-shot across BOOM (2048 ctx) / GIFT-Eval (4096 ctx) / TIME (per-task ctx); single-pass stable to ~768 steps, block decoding beyond; 2k-8k stability study (r=0.99 at 2k, 0.818 at 8k for 2.5B).
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — Evaluated on mixed horizons via fev-bench/GIFT-Eval/Chronos Bench II (H dictated by benchmark tasks); 2-stage training extends max output patches and context 2048->8192 to support long-horizon and high-frequency seasonalities without heuristics; energy case hourly day-ahead (EPF-DE) and retail weekly quarter (Rossmann) illustrate short vs longer horizons.
