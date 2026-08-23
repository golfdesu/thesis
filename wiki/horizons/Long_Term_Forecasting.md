---
concept: Long-Term Load Forecasting
category: forecasting-horizon
time_range: "Days – months ahead"
last_updated: 2026-08-23
tags: [horizon, long-term, LTSF, planning]
---

# 📆 Long-Term Load Forecasting

## Definition

Long-term load forecasting covers prediction horizons from **several days to months ahead**, typically at hourly or daily resolution. For EV charging this includes monthly demand growth tracking for infrastructure planning and capacity expansion; in the broader time-series literature it corresponds to the Long-Term Series Forecasting (LTSF) benchmark setting (96–720 step horizons).

## Temporal Resolution

| Resolution | Horizon | Primary Use Case |
|------------|---------|-----------------|
| Daily | 1–4 weeks | Demand trend monitoring, maintenance planning |
| Hourly | 30/60/90 days | Charging network capacity planning |
| Multi-step (96–720 steps) | Months | Infrastructure investment, fleet-growth scenarios |

## Characteristics & Challenges

- **Non-stationarity**: Annual EV adoption growth creates a persistent upward trend that must be decomposed or normalized.
- **Weak short-lag autocorrelation**: Value shifts from recent lags to seasonal/aggregated patterns.
- **Distribution shift**: Input-window statistics drift over months — motivates instance normalization ([[2022_Kim_RevIN_Reversible_Instance_Normalization]]).
- **Error accumulation**: Direct multi-step strategies generally outperform recursive rollout at these horizons.

## Common Model Approaches

| Model | Papers |
|-------|--------|
| LSTM foundations | [[1997_Hochreiter_Long_Short_Term_Memory]] |
| N-BEATS (basis expansion) | [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]] |
| Decomposition Transformers (Autoformer / Informer) | [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]], [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] |
| Linear LTSF baselines (DLinear) | [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] |
| Patch/channel-independent Transformers | [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]], [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] |
| Multi-layer perceptrons (TiDE) & NHiTS | [[2024_Das_TiDE_Long_Term_Forecasting]], [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]] |
| Selective SSM / Mamba (TimeMachine, Bi-Mamba+) | [[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]], [[2024_Liang_BiMamba_Bidirectional_Mamba_Forecasting]] |
| KAN decoder (learnable spline edges) | [[2024_Liu_KAN_Kolmogorov_Arnold_Networks]] |

## Citing Literature

- 2021 — [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] : ProbSparse attention + distilling enable long-sequence forecasting beyond O(L²).
- 2022 — [[2022_Kim_RevIN_Reversible_Instance_Normalization]] : Reversible instance normalization mitigates distribution shift in long-horizon forecasting.
- 2023 — [[2023_Koohfar_Transformer_EV_Demand]] : Transformer EV demand benchmarked on extended multi-step horizons vs SARIMA.
- 2023 — [[2023_Wu_TimesNet_Temporal_2D_Variation_Modeling]] : 2D variation modeling captures intra-period and inter-period structure for LTSF.
- 2023 — [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]] : Cross-dimension attention exploits multivariate dependencies at long horizons.
- 2024 — [[2024_Helmy_Autoformer_EV_Charging]] : EV charging demand at **30/60/90-day horizons** — Autoformer RMSE ≈ 0.21 kWh/h flat vs LSTM degrading ~60% by day 90.
- 2024 — [[2024_Zhou_Conformal_Prediction_DER]] : Long-range DER adoption forecasting with hierarchical conformal coverage guarantees.
- 2025 — [[2025_Bao_ResMMoT_Informer_Time_Series]] : Residual multi-scale Mixture-of-Experts Informer for extended multi-step horizons.
- 2025 — [[2025_Hussain_Hybrid_LSTM_Transformer_Demand]] : Hybrid LSTM-Transformer evaluated across extended prediction lengths on ACN/JPL data.
- 2025 — [[2025_Weqar_LTLM_LSTM_EV_Load]] : LTLM uses ~200-day historical load windows at daily resolution for long-term station forecasting.
- 2025 — [[2025_Meyer_Benchmark_Foundation_Models]] : Zero-shot foundation models (Chronos-Bolt, TimesFM 2.0, Moirai) benchmarked on long-horizon energy tasks.
- 2026 — [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] : MFT fuses multi-scale temporal features for up to 96-hour-ahead EV charging forecasting.
- 2024 — [[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]] : Quadruple-Mamba LTSF with linear scalability — Electricity T=720 MSE 0.207 vs iTransformer 0.225; benefits monotonically from look-back up to L=720 (Electricity T=96: 0.142→0.133).
- 2024 — [[2024_Liang_BiMamba_Bidirectional_Mamba_Forecasting]] : Bidirectional forget-gated Mamba+ encoder + Spearman-based channel-strategy decider; −4.72% avg MSE vs iTransformer across T ∈ {96,192,336,720}, linear memory on Traffic where attention grows quadratically.
- 2024 — [[2024_Liu_KAN_Kolmogorov_Arnold_Networks]] : KANs offer dimension-independent approximation scaling ($G^{-k-1}$) and grid extension for capacity growth — motivates KOLMOGOROV-ARNOLD decoders in long-horizon EV forecasters ([[2026_Hao_Mamba_KAN_HyKANet_EV]]), though 10× slower training than MLPs favors hybrid rather than pure-KAN stacks.
- 2024 — [[2024_He_Robust_MTS_Transitional_Shift]] : JointPGM probabilistic graphical model targets the LTSF setting (H ∈ {96,192,336,720}) under intra-/inter-series transitional shift — avg −15.3% MAE / −37.9% MSE vs nine baselines (Exchange H=96 MSE 0.076 vs iTransformer 0.086) and −9.3% MSE vs Koopa, with 77.6% training-time reduction; directly addresses the distribution-shift challenge that plagues multi-month EV horizons.
- 2024 — [[2024_Li_TOU_Price_Meteorology_EV_Charging_Load]] : CNN-GRU multi-horizon forecasting out to **168 h** — lowest MAE/RMSE at all of 4/24/72/168 h with small degradation (RMSE 46.42→71.50), showing stable long-window accuracy on TOU/weather-conditioned mall-station load.
- 2024 — [[2024_Ma_LASSO_BPNN_Mid_Term_EV_Load]] : Monthly mid-term LASSO-BPNN across four Qingpu (Shanghai) station types from only ~13 monthly points — best test MAPE 8.64% (Residential) vs LASSO-SVR/XGBoost/RF, with tree baselines overfitting.

## Key Input Features

- [[Historical_Load]] (long lookback windows, often decomposed)
- Calendar/seasonality encodings — see [[Cyclical_Encodings]]
- Trend-seasonality decomposition (moving-average or STL)

## Evaluation Metrics

- [[MAE]], [[MSE]], [[RMSE]] averaged per horizon length
- [[NRMSE]] for cross-station comparability
- [[R_squared]] for trend capture quality

## Related Pages

- [[Day_Ahead_Forecasting]]
- [[Short_Term_Forecasting]]
