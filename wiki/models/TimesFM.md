---
type: model
name: "TimesFM"
category: Stub (auto-generated)
status: needs-review
tags:
  - model
  - timesfm
---

# TimesFM

Google's decoder-only patched time-series foundation model for zero-shot point forecasting.

## Referenced in this knowledge base

*(none recorded)*
- [[2025_Chronos_2_Univariate_to_Universal]] — **TimesFM-2.5** baseline beaten: fev-bench W 75.9/S 42.3 vs 90.7/47.3 SQL; GIFT-Eval WQL 77.5/51.0 vs 81.9/51.4; capability matrix Table 1: no multivariate/covariate support.

- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]]

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated as baseline comparison on fev-bench and GIFT-Eval where TiRex-2 achieves SOTA zero-shot accuracy in multivariate and covariate-aware settings.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Evaluated on fm-impute-bench and fev-bench zero-shot benchmarks for forecasting and missing-value imputation.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Compared as baseline on GIFT-Eval zero-shot benchmark where FlowState achieves state-of-the-art accuracy with significantly lower parameter counts.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Evaluated as baseline comparison in zero-shot time series benchmark (GiftEval-ZS and Chronos-ZS), where TiRex (35M) outperforms baseline models across short and long horizons.
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — **MOIRAI (Woo et al., ICML 2024)**: Masked Encoder-based Universal Time Series Forecasting Transformer (14M Small, 91M Base, 311M Large). Introduces multi-patch size input/output projections (8..128), Any-variate Attention with binary variate biases and RoPE, and 4-component mixture distribution (Student-t, log-normal, neg-binomial, low-var normal). Pre-trained on LOTSA (27.6B obs across 9 domains) with sequence packing.
