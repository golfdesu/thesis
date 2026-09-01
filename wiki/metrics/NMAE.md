---
type: metric
name: "NMAE (Normalized Mean Absolute Error)"
category: point-forecast-metric
formula: "NMAE = MAE / normalizer (mean load, capacity, or max−min)"
unit: Dimensionless
last_updated: 2026-08-26
tags:
  - metric
  - nmae
  - normalized-error
  - point-forecast
---

# NMAE (Normalized Mean Absolute Error)

## Definition

**NMAE** divides the [[MAE]] by a problem-dependent normalizing constant, most commonly the mean observed load:

$$\text{NMAE} = \frac{\frac{1}{N}\sum_{i=1}^{N} |y_i - \hat{y}_i|}{\bar{y}} \quad\text{(mean-load variant)}$$

Other conventions normalize by installed capacity or by $\max(y) - \min(y)$ — always check which one a paper uses before comparing numbers. Related scale-free metrics: [[ND]] (normalizes by $\sum|y|$), [[NRMSE]] (RMSE-based).

## Referenced in this knowledge base

[[2019_Zhu_ApplSci_EV_Load_Forecasting]]
[[2024_Bampos_EV_Load_Forecasting_DAM]]
[[2024_DeVilmarest_Adaptive_Probabilistic_Netload]]
[[Absolute_Error]]
[[ND]]
