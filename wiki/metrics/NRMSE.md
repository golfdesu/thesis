---
metric: Normalized RMSE (NRMSE)
category: point-forecast-metric
formula: "NRMSE = RMSE / (y_max − y_min)"
unit: Percentage (%) or dimensionless
last_updated: 2026-08-23
tags: [metric, nrmse, normalized-error, point-forecast]
---

# 📐 Normalized RMSE (NRMSE)

## Definition

**NRMSE** scales [[RMSE]] by the range of observed values, making error magnitudes comparable across charging stations/sites with different load levels:

$$\text{NRMSE} = \frac{\sqrt{\frac{1}{n}\sum_{t=1}^{n}(\hat{y}_t - y_t)^2}}{y_{\max} - y_{\min}}, \qquad \text{NMAE} = \frac{\frac{1}{n}\sum_{t=1}^{n}|\hat{y}_t - y_t|}{y_{\max} - y_{\min}}$$

Lower is better. The range-normalization makes it sensitive to outliers in $y_{\max}$; CV-RMSE (normalizing by the mean $\bar{y}$) is a common alternative.

## Usage in EV Load Forecasting Papers

| Paper | Result |
|-------|--------|
| 2019 — [[2019_Zhu_ApplSci_EV_Load_Forecasting]] | Primary metric: single-hidden-layer GRU achieved Test-NRMSE **2.89%**, Test-NMAE 0.77% — adding hidden layers degraded both accuracy and training speed. |
| 2024 — [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] | NRMSE used to define the Accuracy Rate AR = (1 − NRMSE) × 100%, alongside Qualified Rate (QR) and SMAPE/R². |
| 2024 — [[2024_Bampos_EV_Load_Forecasting_DAM]] | nRMSE variant reported for day-ahead-market EV load benchmarks across four public datasets. |

## Related Pages

- [[RMSE]]
- [[MAPE]]
- [[MAE]]
