---
type: metric
name: "Mean Squared Error (MSE)"
category: Stub (auto-generated)
status: needs-review
tags:
  - metric
  - mse
---

## Definition
$$\mathrm{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

Mean of squared errors. Units are the square of the target's units; the square root ([[RMSE]]) is usually reported instead.

| Property | Value |
|----------|-------|
| Unit | Squared target units |
| Lower is better | Yes |
| Outlier sensitivity | High (squared terms) |
| Related | [[RMSE]], [[MAE]], [[R_squared]] |

## Usage in EV / Load Forecasting Papers
Commonly reported for point forecasts of EV charging load; penalizes large errors more heavily than [[MAE]].

## References
- See paper summaries in [[Papers & Literature]] tagged with MSE.

- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]]

## Literature Usage
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Mean squared error evaluation metric.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — Evaluated zero-shot out-of-distribution across 6 datasets (Electricity, Solar, Walmart, Weather, Istanbul Traffic, Turkey Power) and 9 Monash benchmarks using continuous/discrete quantile approximations.
