---
metric: Mean Prediction Interval Width (MPIW)
category: probabilistic-forecast-metric
formula: "MPIW = (1/N) Σ (u_i − l_i)"
unit: Same as target variable (kW / kWh / MWh)
last_updated: 2026-08-23
tags: [metric, mpiw, sharpness, prediction-interval, probabilistic-forecast]
---

# 📐 Mean Prediction Interval Width (MPIW)

## Definition

**MPIW** measures the average width of predicted intervals $[l_i, u_i]$ — a pure **sharpness** metric:

$$\text{MPIW} = \frac{1}{N}\sum_{i=1}^{N}\left(u_i - l_i\right)$$

**Lower is better** — but only meaningful jointly with coverage ([[PICP]]): trivially narrow intervals with bad coverage are worthless, and wide intervals with perfect coverage are useless for downstream decisions. Reporting MPIW together with coverage/Interval Score avoids favoring over-wide intervals.

## Properties

| Property | Description |
|----------|-------------|
| **Unit** | Same as target variable (scale-dependent) |
| **Lower is better** | ✅ Yes, conditional on adequate [[PICP]] |
| **Measures** | Sharpness only (no calibration information) |
| **Pair with** | Coverage ([[PICP]]) or [[Interval_Score]] / [[Winkler_Score]] for joint evaluation |

## Usage in EV / Load Forecasting Papers

| Paper | Result |
|-------|--------|
| 2026 — [[2026_Yu_EnergyMamba_Graph_Mamba_ASCQR]] | EnergyMamba MPIW 122.51 (Florida 1) vs best baseline ST-LLM 134.28; 107.83 (Florida 2); 201.87 (NYISO); 692.05 (CAISO) — sharper *and* ≥90% coverage via [[AS_CQR]]. |
| Related interval-width metrics | [[2024_Zhou_Conformal_Prediction_DER]] (Interval_Size), [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] ([[Winkler_Score]] reveals over-wide intervals despite 96.88% PICP). |

## Related Pages

- [[PICP]]
- [[Interval_Score]]
- [[Winkler_Score]]
