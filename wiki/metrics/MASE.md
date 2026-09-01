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
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Primary point forecasting metric on fev-bench and GIFT-Eval.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Scaled error metric on fev-bench forecasting benchmark.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Primary point forecasting metric on GIFT-Eval (FlowState-18.6M achieves Rank 1 MASE 0.706).
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Point forecast evaluation metric on GiftEval-ZS (MASE 0.647) and Chronos-ZS (MASE 0.776).
- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]]
- [[2025_Chronos_2_Univariate_to_Universal]] — **MASE** point metric on GIFT-Eval W 83.8 S 30.2 and Chronos Bench II W 81.5 S 26.5 for Chronos-2 (Tables 4b/5b); fev-bench MASE gains in Appendix Fig.9-11.
- [[2026_Moirai_2_When_Less_Is_More]] — GIFT-Eval normalized MASE/CRPS (geometric mean / seasonal naive, 97 tasks); WQL via 9 quantiles (0.1-0.9). Small: MASE 0.728 / CRPS 0.516 (Table 1); ranks 5th/6th among 37 FMs (Fig. 2); base/large underperform small on same corpus.
