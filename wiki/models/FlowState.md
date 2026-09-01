---
type: model
name: "FlowState"
category: Stub (auto-generated)
status: needs-review
tags: [model, flowstate]
---

# FlowState

Sampling-rate invariant TSFM (Graf et al. 2025, NeurIPS 2025) — dynamic forecasting horizons.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated as baseline comparison on fev-bench and GIFT-Eval where TiRex-2 achieves SOTA zero-shot accuracy in multivariate and covariate-aware settings.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Introduces FlowState, an 18.6M continuous-time foundation model pairing an S5 SSM encoder with a Functional Basis Decoder (FBD), achieving SOTA MASE 0.706 on GIFT-Eval and zero-shot sampling-rate equivariance.
- [[2026_Toto_2_Scaling_Era]] — GIFT-Eval competitor (CRPS rank 25.6) and TIME/BOMM baseline behind Toto 2.0; in FnF ensemble pool.
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
