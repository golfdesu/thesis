---
type: metric
name: "ND (Normalized Deviation)"
category: point-forecast-metric
formula: "ND = Σ|y − ŷ| / Σ|y|"
unit: Dimensionless
last_updated: 2026-08-26
tags:
  - metric
  - nd
  - normalized-deviation
  - point-forecast
---

# ND (Normalized Deviation)

## Definition

**ND** is the sum of absolute errors normalized by the sum of absolute actual values (standard in GluonTS / DeepAR-style evaluations):

$$\text{ND} = \frac{\sum_{i=1}^{N} |y_i - \hat{y}_i|}{\sum_{i=1}^{N} |y_i|}$$

It equals [[MAE]] normalized by the mean absolute level of the series; ND = 0 is a perfect forecast. Closely related to [[NMAE]] (which may use a different normalizer such as capacity or range).

| Property | Description |
|----------|-------------|
| **Unit** | Dimensionless (%) |
| **Lower is better** | ✅ Yes |
| **Scale-free** | ✅ Comparable across stations with different load levels |

## Referenced in this knowledge base

[[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]], [[2020_Salinas_DeepAR_Probabilistic_Forecasting]], [[2024_Ali_MQ_TCN_Transfer_Learning_EV]]
