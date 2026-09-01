---
title: Interval Score
type: metric
metric: Interval Score
category: probabilistic-forecast-metric
formula: "IS = (u−l) + (2/α)(l−y)·1{y<l} + (2/α)(y−u)·1{y>u}"
unit: Same as target variable (kW / kWh / MWh)
last_updated: 2026-08-23
tags: [metric, interval-score, winkler, prediction-interval, probabilistic-forecast]
---

# 📐 Interval Score

## Definition

The **(1−α) interval score** (Gneiting & Raftery lineage; identical in form to the [[Winkler_Score]]) jointly rewards **sharpness** and penalizes **misses** of a central prediction interval $[l, u]$:

$$\text{IS} = \frac{1}{N}\sum_{i=1}^{N}\left[(u_i - l_i) + \frac{2}{\alpha}(l_i - y_i)\mathbb{I}(y_i < l_i) + \frac{2}{\alpha}(y_i - u_i)\mathbb{I}(y_i > u_i)\right]$$

Lower is better. The width term dominates when the observation falls inside the interval; misses add distance-proportional penalties scaled by $2/\alpha$, so narrow-but-frequent-miss intervals score badly. Averaged over a dataset it summarizes both calibration and sharpness in one number — more informative than [[PICP]] alone or raw width ([[MPIW]]) alone.

## Properties

| Property | Description |
|----------|-------------|
| **Unit** | Same as target variable |
| **Lower is better** | ✅ Yes |
| **Joint sharpness + calibration** | ✅ Yes — single number per interval level |
| **Relation to Winkler** | Identical functional form ([[Winkler_Score]]); "interval score" is the common forecasting-literature naming |

## Usage in EV / Load Forecasting Papers

| Paper | Result |
|-------|--------|
| 2026 — [[2026_Yu_EnergyMamba_Graph_Mamba_ASCQR]] | Primary UQ metric for EnergyMamba/[[AS_CQR]]: IS 231.86 (Florida 1), 198.23 (Florida 2), 295.42 (NYISO), 1279.17 (CAISO) — ~6% better than the best baseline on average, with ≥90% coverage. |

## Related Pages

- [[Winkler_Score]]
- [[PICP]]
- [[MPIW]]
- [[CRPS]]
