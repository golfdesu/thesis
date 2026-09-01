---
type: model
name: "Chronos-2"
category: Time Series Forecasting
tags: [model, time-series, forecasting]
---

# Chronos-2

## Overview
Universal pretrained forecaster (Amazon, arXiv:2510.15821). Encoder-only T5+RoPE with alternating time/group attention enabling zero-shot univariate/multivariate/covariate-informed forecasting via group IDs + future inputs. 120M base (28M small), 21-quantile direct multi-patch head, sinh-asinh scaling, entirely synthetic multivariate/covariate pretraining via multivariatizers, 2048->8192 ctx post-training. SOTA on fev-bench/GIFT-Eval/Chronos Bench II.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated as baseline comparison on fev-bench and GIFT-Eval where TiRex-2 achieves SOTA zero-shot accuracy in multivariate and covariate-aware settings.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Evaluated on fm-impute-bench and fev-bench zero-shot benchmarks for forecasting and missing-value imputation.
- [[2025_Chronos_2_Univariate_to_Universal]] — **Origin paper (Chronos-2, Amazon, 120M base / 28M small)**. Universal encoder-only T5+RoPE with alternating time/group attention, O(V) memory, 21-quantile multi-patch head, sinh-asinh robust scaling (Eq.1-5). SOTA on fev-bench W 90.7% S 47.3% SQL, GIFT-Eval WQL 81.9/51.4 and MASE 83.8/30.2, Chronos Bench II WQL 79.8/46.6 and MASE 81.5/26.5. Statistically significant vs TiRex/TimesFM-2.5/Toto-1.0; 300 series/s on A10G. Ablations: 28M near-parity, synthetic-only close, 2048->8192 ctx helps.

## Related Models
- See [[2025_Chronos_2_Univariate_to_Universal]] Table 1/3 for capability comparisons on fev-bench / GIFT-Eval.
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
