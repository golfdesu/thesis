---
type: model
name: "TiRex"
category: Stub (auto-generated)
status: needs-review
tags: [model, tirex]
---

# TiRex

Zero-shot TSFM with enhanced in-context learning (Auer et al. 2025) — CPM origin for xLSTM.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated as baseline comparison on fev-bench and GIFT-Eval where TiRex-2 achieves SOTA zero-shot accuracy in multivariate and covariate-aware settings.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Evaluated on fm-impute-bench and fev-bench zero-shot benchmarks for forecasting and missing-value imputation.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Compared as baseline on GIFT-Eval zero-shot benchmark where FlowState achieves state-of-the-art accuracy with significantly lower parameter counts.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Introduces TiRex, a 35M decoder-only foundation model based on 12 sLSTM blocks trained with Contiguous Patch Masking (CPM) on a 47.5M time series corpus, achieving SOTA zero-shot forecasting on GiftEval-ZS (CRPS 0.411) and Chronos-ZS (WQL 0.592).
- [[2026_Toto_2_Scaling_Era]] — CPM scheme borrowed and extended (cmax 16/pmax 0.4 vs TiRex 5/0.25); GIFT-Eval CRPS rank 23.9 behind Toto 2.0 top-3.
- [[2025_Chronos_2_Univariate_to_Universal]] — **TiRex (Auer et al. NeurIPS 2025)** 2nd on fev-bench beaten with significance: W 80.8/S 42.6 vs 90.7/47.3 SQL; GIFT-Eval WQL 76.5/50.2 vs 81.9/51.4; 1.4s median vs 3.6s.
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
