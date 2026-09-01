---
type: metric
name: "ACE (Average Coverage Error)"
category: probabilistic-interval-metric
formula: "ACE = PICP − PINC"
unit: Percentage points (dimensionless)
last_updated: 2026-08-26
tags:
  - metric
  - ace
  - coverage
  - probabilistic-forecast
---

# ACE (Average Coverage Error)

## Definition

**ACE** measures how far the empirical coverage of prediction intervals deviates from the nominal confidence level (PINC, Prediction Interval Nominal Coverage):

$$\text{ACE} = \text{PICP} - \text{PINC}$$

where [[PICP]] is the fraction of observations falling inside the forecast intervals and PINC is the target coverage (e.g. 90% for a 90% interval). It is often reported as |ACE|, where smaller is better and 0 indicates perfectly calibrated interval width.

| Property | Description |
|----------|-------------|
| **Unit** | Percentage points |
| **Lower \|ACE\| is better** | ✅ Yes (0 = calibrated) |
| **Paired with** | [[PICP]], [[MPIW]], [[Winkler_Score]] — coverage must be judged together with sharpness |

## Referenced in this knowledge base

[[2021_Zhang_Probabilistic_Queuing_EV_Load]], [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]]
