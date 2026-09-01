---
type: model
name: "Chronos Bolt"
category: Stub (auto-generated)
status: needs-review
tags:
  - model
  - chronos-bolt
---

# Chronos Bolt

Faster, patch-based descendant of [[Chronos]] for point and quantile forecasting.

## Referenced in this knowledge base

*(none recorded)*
- [[2025_Chronos_2_Univariate_to_Universal]] — Direct predecessor **Chronos-Bolt** beaten decisively: fev-bench W 60.3% vs 90.7%, S 38.9% vs 47.3%; GIFT-Eval WQL 53.8 vs 81.9; Chronos Bench II 49.4 vs 79.8.

## Literature Usage
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Compared as baseline on GIFT-Eval zero-shot benchmark where FlowState achieves state-of-the-art accuracy with significantly lower parameter counts.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Evaluated as baseline comparison in zero-shot time series benchmark (GiftEval-ZS and Chronos-ZS), where TiRex (35M) outperforms baseline models across short and long horizons.
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
