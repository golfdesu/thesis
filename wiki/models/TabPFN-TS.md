---
type: model
name: "TabPFN-TS"
category: Time Series Forecasting
tags: [model, time-series, forecasting]
---

# TabPFN-TS

## Overview
Tables-to-Time adaptation of TabPFN-v2 for time series (Hoo et al. 2025) — tabular FM with known-covariate support; 2nd on fev-bench covariates.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated as baseline comparison on fev-bench and GIFT-Eval where TiRex-2 achieves SOTA zero-shot accuracy in multivariate and covariate-aware settings.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Evaluated on fm-impute-bench and fev-bench zero-shot benchmarks for forecasting and missing-value imputation.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Evaluated as baseline comparison in zero-shot time series benchmark (GiftEval-ZS and Chronos-ZS), where TiRex (35M) outperforms baseline models across short and long horizons.
- [[2025_Chronos_2_Univariate_to_Universal]] — **TabPFN-TS (Hoo et al. 2025)** tabular-to-TS with known-covariate support; 2nd on covariates subset but still beaten: fev-bench W 59.3/S 39.6 vs 90.7/47.3; very slow 305.5s vs 3.6s.

## Related Models
- See [[2025_Chronos_2_Univariate_to_Universal]] Table 1/3 for capability comparisons on fev-bench / GIFT-Eval.
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
