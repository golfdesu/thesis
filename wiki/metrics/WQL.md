---
type: metric
name: "WQL"
tags: [metric]
---

# WQL

## Overview
Weighted Quantile Loss — probabilistic metric weighting by magnitude; used on GIFT-Eval and Chronos Benchmark II.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Multi-patch quantile training objective across 9 quantiles.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Used to calculate pinball quantile loss across predicted basis coefficients.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Weighted Quantile Loss across 9 equidistant quantiles $Q = \{0.1, 0.2, \dots, 0.9\}$ used as the primary training objective (Eq. 2) and Chronos-ZS evaluation (WQL 0.592).
- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]]
- [[2025_Chronos_2_Univariate_to_Universal]] — **WQL** on GIFT-Eval W 81.9 S 51.4 and Chronos Bench II W 79.8 S 46.6 for Chronos-2 (Tables 4-5); 2nd place TimesFM-2.5/TiRex 77.5/51.0 and 70.4/41.7.
- [[2026_Moirai_2_When_Less_Is_More]] — GIFT-Eval normalized MASE/CRPS (geometric mean / seasonal naive, 97 tasks); WQL via 9 quantiles (0.1-0.9). Small: MASE 0.728 / CRPS 0.516 (Table 1); ranks 5th/6th among 37 FMs (Fig. 2); base/large underperform small on same corpus.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — Evaluated zero-shot out-of-distribution across 6 datasets (Electricity, Solar, Walmart, Weather, Istanbul Traffic, Turkey Power) and 9 Monash benchmarks using continuous/discrete quantile approximations.
