---
type: model
name: "xLSTM"
category: Stub (auto-generated)
status: needs-review
tags: [model, xlstm]
---

# xLSTM

Extended LSTM (Beck et al. 2024) — SSM alternative where CPM was originally designed.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated as baseline comparison on fev-bench and GIFT-Eval where TiRex-2 achieves SOTA zero-shot accuracy in multivariate and covariate-aware settings.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Uses sLSTM modules (scalar LSTM with exponential gating and normalizer state) as the core sequence-mixing backbone in TiRex, demonstrating that recurrent state-tracking beats Transformers on long-horizon zero-shot forecasting.
- [[2026_Toto_2_Scaling_Era]] — CPM designed for xLSTM (Auer et al. 2025); Toto 2.0 shows CPM pays off more on Transformer (one call vs |M| on SSM).
