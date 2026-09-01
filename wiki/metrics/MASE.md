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

## Literature Usage
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — **MASE** point metric on GIFT-Eval W 83.8 S 30.2 and Chronos Bench II W 81.5 S 26.5 for Chronos-2 (Tables 4b/5b); fev-bench MASE gains in Appendix Fig.9-11.
