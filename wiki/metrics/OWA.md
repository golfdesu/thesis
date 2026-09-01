---
type: metric
name: "OWA (Overall Weighted Average)"
category: point-forecast-metric
formula: "OWA = 0.5 · (MASE / MASE_naive) + 0.5 · (sMAPE / sMAPE_naive)"
unit: Dimensionless (relative to naive benchmark)
last_updated: 2026-08-26
tags:
  - metric
  - owa
  - benchmark
  - point-forecast
---

# OWA (Overall Weighted Average)

## Definition

**OWA**, introduced for the M4 forecasting competition, aggregates accuracy relative to the seasonal naive benchmark:

$$\text{OWA} = \frac{1}{2}\left(\frac{\text{MASE}}{\text{MASE}_{\text{naive}}} + \frac{\text{sMAPE}}{\text{sMAPE}_{\text{naive}}}\right)$$

where [[MASE]] and [[sMAPE]] of the model are divided by the same metrics computed for the naive benchmark method on the same data. OWA < 1 means the model beats the naive benchmark on both error families combined.

| Property | Description |
|----------|-------------|
| **Unit** | Dimensionless |
| **Lower is better** | ✅ Yes (< 1 beats naive) |
| **Scale-free** | ✅ Comparable across series/competitions |

## Referenced in this knowledge base

[[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]], [[2023_Wu_TimesNet_Temporal_2D_Variation_Modeling]]
- [[2026_Khwaja_Toto_2_Scaling_Era]] — Ensemble training target: OWA_f,j = 1/2 (MASE_f,j/MASE_sNaive + CRPS_f,j/CRPS_sNaive) (Eq.8, Makridakis et al. 2020) — FFORMA-style XGBoost meta-learner over 10-model pool; 20 heads by frequency*horizon.
