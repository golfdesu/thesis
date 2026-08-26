---
type: dataset
name: ERCOT GridSet
location: Electric Reliability Council of Texas (ERCOT), USA
resolution: Hourly, 5-year span (2019–2023)
access: open (released with PowerMamba toolbox)
data_type: Multivariate power-system time series: 22 core channels; extended 262-channel version with external forecasts
urls:
  - https://github.com/alimenati/PowerMamba
tags:
  - dataset
  - power-systems
  - ercot
  - electricity-prices
  - renewables
---

# 📁 ERCOT GridSet

## Overview
**GridSet** is a five-year hourly benchmark dataset for electric power systems released alongside [[PowerMamba]]: **43,824 hours (1,826 days), 2019–2023**, capturing Texas's rapid renewable/storage/flexible-load growth. Train = first 4 years; test = final year.

## Channels (22 core)
| Group | Count | Detail |
|-------|-------|--------|
| Zonal loads | 8 | One per weather zone (mean 5,797.93 MW, σ 1,446.52) |
| Day-ahead prices | 8 | Zonal settlement-point prices (mean $67.06/MWh, σ 422.15) |
| Ancillary-service prices | 4 | Reg-Up, Reg-Down, RRS, Non-Spin (mean $52.41, σ 662.53) |
| Renewables | 2 | Wind + solar generation (mean 6,363.30 MW, σ 4,438.36) |

**Extended version**: + ERCOT external forecasts (8 zonal-load + 2 renewable columns × 24-h rolling window updated hourly, up to one week ahead) → **262 channels**. No external price forecasts exist.

Companion: six-year PJM ISO dataset (2019–2024) in the paper appendix confirms cross-ISO generalization.

## 📚 Used By
- [[2024_Menati_PowerMamba_Power_Systems_SSM]] — Native benchmark (GridSet W=24 MSE 0.129/MAE 0.166; external-forecast module cuts MSE to 0.074); toolbox + data at https://github.com/alimenati/PowerMamba .

## Related Pages
- [[PowerMamba]]
- [[EIA-930]]
