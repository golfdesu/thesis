---
title: Historical Charging Load
type: feature
name: "Historical Charging Load"
feature: Historical Charging Load
category: temporal-feature
data_type: continuous time series (kW or kWh)
last_updated: 2026-08-02
tags: [feature, time-series, load, historical]
---

# 📊 Historical Charging Load

## Definition

**Historical charging load** refers to the past observed power demand (kW) or energy consumption (kWh) time series at an EV charging station or network. It is the most universally used input feature across all EV load forecasting models — the direct autoregressive signal.

## Forms & Representations

| Form | Unit | Typical Window |
|------|------|---------------|
| Raw power series | kW (instantaneous) | 15-min to 1-week lookback |
| Energy per interval | kWh per 15-min slot | 24–96 steps |
| Session energy total | kWh per session | Session-level aggregation |
| Normalized load | 0–1 (Min-Max scaled) | Model-dependent |
| Decomposed (trend + residual) | Dimensionless | See [[2024_Bampos_EV_Load_Forecasting_DAM]] |

## Importance Across Models

Almost every paper in this wiki uses historical load as the primary input:

| Paper | Lookback Window | Resolution |
|-------|----------------|------------|
| [[2019_Zhu_EV_Load_Forecasting]] | 1 hour | 1-minute |
| [[2021_VanKriekinge_Day_Ahead_EV_Demand]] | 7 days | 15-minute |
| [[2024_Bampos_EV_Load_Forecasting_DAM]] | Trend decomposed | 1-hour |
| [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] | 96 steps | 15-minute |
| [[2025_Weqar_LTLM_LSTM_EV_Load]] | 200 days | Daily |

## Preprocessing Techniques

- **Min-Max Normalization**: $\hat{x} = \frac{x - x_{\min}}{x_{\max} - x_{\min}}$ — Standard across LSTM/GRU papers.
- **Z-score Standardization**: $\hat{x} = \frac{x - \mu}{\sigma}$ — Used in Transformer-based models.
- **Outlier Detection & Interpolation**: Threshold-based detection + linear interpolation ([[2019_Zhu_EV_Load_Forecasting]]).
- **Multiplicative Decomposition**: Separate annual trend from residual seasonality ([[2024_Bampos_EV_Load_Forecasting_DAM]]).
- **Wavelet Decomposition**: DWT noise reduction before model input ([[2025_Bao_ResMMoT_Informer_Time_Series]]).
- **VMD (Variational Mode Decomposition)**: Adaptive signal decomposition ([[2023_Cheng_VMD_Prophet_LSTM]]).

## Autocorrelation Patterns

EV charging load exhibits:
- **Intraday periodicity**: Morning and evening peaks corresponding to commuting behavior.
- **Weekly seasonality**: Weekday vs. weekend usage patterns.
- **Annual trend**: Growing baseline due to EV fleet expansion.

## Citing Literature

- 2015 — [[2015_Raza_Review_AI_Load_Demand]] : Review identifies lagged load as the dominant input across ANN/fuzzy/wavelet AI forecasting approaches.
- 2019 — [[2019_Li_LogSparse_Enhancing_Locality_Transformer]] : LogSparse Transformer consumes raw historical load windows with time-based covariates for self-attention.
- 2019 — [[2019_Zhu_ApplSci_EV_Load_Forecasting]] : Multi-dimensional feature GRU comparison on Liuyue charging-station load series.
- 2020 — [[2020_Huang_Ensemble_EV_Load]] : Ensemble of LR/ANN/RNN/LSTM on hourly-aggregated Boulder load.
- 2021 — [[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]] : Historical load drives RL state in Q-learning-based EV load estimation.
- 2021 — [[2021_Rasul_TimeGrad_Diffusion_Forecasting]] : Autoregressive conditioning on scaled history (mean-scaling normalization) for diffusion forecasting.
- 2022 — [[2022_Cao_Robust_Deep_Gaussian_Process_Load]] : Lagged load + mobility/COVID features feed robust deep GP city load models.
- 2022 — [[2022_Kim_RevIN_Reversible_Instance_Normalization]] : RevIN normalizes each input load window with instance statistics (μ, σ) to handle distribution shift.
- 2023 — [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]] : NHiTS compresses long historical inputs via multi-rate hierarchical interpolation blocks.
- 2023 — [[2023_Cheng_VMD_Prophet_LSTM]] : Load series decomposed via VMD into intrinsic mode functions before Prophet-LSTM forecasting.
- 2023 — [[2023_Huang_MetaProbformer_EV_Load]] : Past load is core input for meta-trained probabilistic Informer across charging sites.
- 2023 — [[2023_Koohfar_Transformer_EV_Demand]] : Transformer day-ahead benchmark conditioned on past demand + NOAA weather.
- 2024 — [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] : MQ-TCN transfer learning reuses source-site load patterns (ACN/NREL workplace charging).
- 2024 — [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] : Per-station Beijing fast-charging load histories as multigraph node signals.
- 2024 — [[2024_Zhong_V2G_SVE_Evaluation_Metric]] : Base electrical load + fleet profiles underlie V2G-SVE scheduling-value evaluation.
- 2025 — [[2025_Zhu_Personalized_Federated_Learning]] : Last observed power anchor personalizes federated household/EV forecasts.
- 2026 — [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] : STL decomposition splits load into trend/seasonal/residual streams for stacked meta-learning.
- 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] : Lagged load + rolling 3/7/14-day energy sums as TFT past inputs; rolling 14-day energy tops encoder variable importance on Palo Alto data.
- 2026 — [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] : 5-min charging occupancy history is the core node signal, enhanced by price-modulated gated attention in TriCast.
- 2026 — [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] : Historical load curves drive ShapeDTW similarity; loads at forecast hours of the 35 optimal similar days become forecaster inputs.
- 2026 — [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] : 96-step (24-h @15-min) historical load sequences are the primary Informer input across three datasets.
- 2026 — [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] : Strictly univariate setting — only past 12 h of hourly demand counts via sliding window; still enough for near-optimal accuracy after ~72 h of training data.
- 2024 — [[2024_Huo_Data_Driven_EVCS_Demand_Forecasting]] : Purely autoregressive 24-hour hourly window $H_t = \{h_{t-1}, \ldots, h_{t-24}\}$ suffices for Rao-1-tuned ANN one-step station forecasting (JPL RMSE 6.93 kW, R² 0.974) — no exogenous variables.
- 2024 — [[2024_Li_TOU_Price_Meteorology_EV_Charging_Load]] : Lagged-load screening via Pearson autocorrelation — same-time lags of past 2 h and past 18 days both correlate >0.6; input vector concatenates the last 24 moments with discontinuous lags t−48/t−72/t−168 plus current exogenous data.
- 2026 — [[2026_Hong_SSM_Transformer_LSTM_Grid_Benchmark]] : Grid-level hourly historical load (L=240 h lookback) is the sole autoregressive input in a five-architecture US benchmark — load-only rankings (PatchTST first) reverse entirely once weather covariates join, so architecture choice should follow input availability.

## Related Pages

- [[Cyclical_Encodings]]
- [[Arrival_Departure_Time]]
- [[State_of_Charge]]
- [[Electricity_Tariff]]
- [[Weather_Traffic]]

## Literature Usage
- [[2025_Liu_Sundial_Highly_Capable_Time_Series_Foundation_Models]]
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Pure univariate input only; no covariates during pretraining (Eq. 1); date-feature extension Eq. 8 discussed as future work.
- [[2026_Khwaja_Toto_2_Scaling_Era]] — Pure univariate input y_{1:L} + missingness mask b_{1:N}; 32 variates/sample in training; no exogenous covariates (weather/tariff/SoC all future work).
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — Past target values Y_{1:T} as core input (V, U) together with optional covariates; univariate mode ignores covariates and still beats Toto-1.0 on multivariate subset.
