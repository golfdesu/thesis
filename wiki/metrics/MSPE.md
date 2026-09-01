---
type: metric
name: "MSPE (Mean Squared Percentage Error)"
category: point-forecast-metric
formula: "MSPE = (1/n) · Σ((y − ŷ)/y)²  — often reported as its square root (RMSPE)"
unit: "Percent squared (root form: %)"
last_updated: 2026-08-26
tags:
  - metric
  - mspe
  - percentage-error
  - point-forecast
---

# MSPE (Mean Squared Percentage Error)

## Definition

**MSPE** is the mean of squared relative (percentage) errors:

$$\text{MSPE} = \frac{1}{n}\sum_{i=1}^{n}\left(\frac{y_i - \hat{y}_i}{y_i}\right)^{2}$$

It is the percentage-based analogue of [[MSE]]; its square root (RMSPE) is expressed in percent. MSPE shares the weaknesses of [[MAPE]]: undefined for zero actuals and asymmetric — over-forecasts are penalized more than under-forecasts of the same absolute size. Compare with [[NRMSE]] for scale-sensitive normalized evaluation.

## Referenced in this knowledge base

[[2001_Hippert_Neural_Networks_STLF_Review]]
