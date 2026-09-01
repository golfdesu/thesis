---
title: Winkler Score
type: metric
metric: Winkler Score
category: probabilistic-forecast-metric
formula: "W = δ + (2/α)(L−y)·1{y<L} + (2/α)(y−U)·1{y>U}"
unit: Same as target variable (kW or kWh)
last_updated: 2026-08-23
tags: [metric, winkler-score, prediction-interval, probabilistic-forecast]
---

# 📐 Winkler Score

## Definition

The **Winkler score** evaluates a central $(1-\alpha) \times 100\%$ prediction interval $[L_t, U_t]$ with width $\delta_t = U_t - L_t$, jointly rewarding **sharpness** (narrow intervals) and penalizing **misses**:

$$\text{Winkler} = \begin{cases} \delta, & L \leq y \leq U \\ \delta + \frac{2}{\alpha}(L - y), & y < L \\ \delta + \frac{2}{\alpha}(y - U), & y > U \end{cases}$$

Lower is better. Misses are penalized in proportion to their distance beyond the interval, so it is more informative than [[PICP]] (coverage alone) or raw interval width.

## Properties

| Property | Description |
|----------|-------------|
| **Unit** | Same as target variable |
| **Lower is better** | ✅ Yes |
| **Joint sharpness + calibration** | ✅ Yes — single number per interval level |
| **Typical levels** | 50% and 90% intervals |

## Usage in EV / Load Forecasting Papers

| Paper | Result |
|-------|--------|
| 2017 — [[2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load]] | Largest QRA gains over the equal-weight benchmark occurred on the **90% Winkler score** (industrially critical high-percentile interval). |
| 2024 — [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] | MQ-TCN JPL WS 21.55, NREL 9.78; authors note high NREL WS despite 96.88% [[PICP]] → wide intervals (over-coverage without sharpness). |
| 2024 — [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] | Winkler score part of the evaluation suite with AIW (average interval width) and Qualified/Accuracy Rate. |
| 2025 — [[2025_Zheng_Coherent_Hierarchical_EV_Load]] | PICNN + DCL best on Winkler Score at nearly all stations in coherent hierarchical ACN evaluation. |

## Related Pages

- [[CRPS]]
- [[Pinball_Loss]]
- [[PICP]]
