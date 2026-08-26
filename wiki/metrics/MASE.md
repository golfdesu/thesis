---
type: metric
name: "Mean Absolute Scaled Error (MASE)"
category: Stub (auto-generated)
status: needs-review
tags:
  - metric
  - mase
---

## Definition
$$\mathrm{MASE} = \frac{\mathrm{MAE}}{\mathrm{MAE}_{\text{naive}}}$$

[[MAE]] scaled by the in-sample MAE of a naive seasonal forecast; values < 1 beat the naive baseline. Scale-independent.

## Usage in EV / Load Forecasting
Used in benchmark studies (N-BEATS lineage, TimesNet) for scale-comparable comparison.
