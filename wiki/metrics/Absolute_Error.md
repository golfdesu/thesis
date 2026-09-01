---
type: metric
name: "Absolute Error"
category: point-forecast-metric
formula: "AE = |ŷ − y|"
unit: Same as target variable (kW or kWh)
last_updated: 2026-08-26
tags:
  - metric
  - absolute_error
  - point-forecast
---

# Absolute Error

## Definition

**Absolute error** is the per-sample distance between a forecast and its observation:

$$\text{AE}_i = |\hat{y}_i - y_i|$$

It is the elementary quantity aggregated by [[MAE]] (mean), [[NMAE]]/[[ND]] (normalized), and summed in the [[Pinball_Loss]] branches. Reported per-sample or as a time series when the distribution of errors matters more than their average.

## Referenced in this knowledge base

[[1997_Hochreiter_Long_Short_Term_Memory]]
