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
- Paper summaries are collected under `papers/`; the master bibliography is [[_all_references]].

## Literature Usage
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Training loss (Eq. 5, MSE over output patches) and ETT reporting (Table 2/5).
