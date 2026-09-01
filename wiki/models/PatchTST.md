---
type: model
name: PatchTST
category: Deep Learning / Patched Channel-Independent Transformer
tags:
  - model
  - deep-learning
  - transformer
  - long-term-forecasting
  - self-supervised
---

# 🩹 PatchTST

## Overview
PatchTST ("A Time Series is Worth 64 Words", Nie et al., ICLR 2023) answers the [[DLinear]] challenge by showing a vanilla-attention Transformer **can** win at long-term forecasting if designed properly. Two core designs:

1. **Patching**: subseries-level patches (length $P=16$, stride $S=8$) become input tokens instead of single points — retaining local semantic information and quadratically reducing attention compute ($N \approx L/S$ tokens):
$$N = \left\lfloor \frac{L-P}{S} \right\rfloor + 2, \qquad x_d^{(i)} = W_p x_p^{(i)} + W_{pos}$$
2. **Channel-independence (CI)**: each univariate channel is processed separately through shared embedding + Transformer weights.

Standard multi-head scaled dot-product attention per channel; encoder uses BatchNorm (superior to LayerNorm for TS Transformers); instance normalization ([[RevIN]]-style) normalizes each window before patching and adds statistics back. Variants: PatchTST/42 ($L=336$) and PatchTST/64 ($L=512$). Also demonstrates strong masked self-supervised pretraining (40% patches masked) and cross-dataset transfer learning.

MSE loss: $\mathcal{L} = \mathbb{E}_x \frac{1}{M}\sum_{i=1}^{M} \left\| \hat{x}_{L+1:L+T}^{(i)} - x_{L+1:L+T}^{(i)} \right\|_2^2$

## Typical Usage in EV Load Forecasting
- **Input**: long look-back windows (up to $L=512$) of multivariate load series, treated channel-wise.
- **Forecasting Horizon**: [[Long_Term_Forecasting]] ($T \in \{96,...,720\}$).
- **Strengths**: overall −21.0% MSE / −16.7% MAE vs best Transformer baselines; ×19–22 patching speedups at $L=336$; benefits monotonically from longer look-backs (unlike prior Transformers).
- **Weaknesses**: channel-independence ignores explicit cross-channel correlations (GNN extension suggested); point forecasts only (no uncertainty); memory-heavy for very long inputs (OOMs ≥ L=1440).

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated as baseline comparison on fev-bench and GIFT-Eval where TiRex-2 achieves SOTA zero-shot accuracy in multivariate and covariate-aware settings.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Compared as baseline on GIFT-Eval zero-shot benchmark where FlowState achieves state-of-the-art accuracy with significantly lower parameter counts.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Evaluated as baseline comparison in zero-shot time series benchmark (GiftEval-ZS and Chronos-ZS), where TiRex (35M) outperforms baseline models across short and long horizons.
- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — Compared as supervised/point-forecasting baseline in GIFT-Eval (e.g., PatchTST MASE 0.762, N-BEATS 21.38 rank).
- [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] — Original paper: patching + CI + RevIN-style normalization; Electricity T=96 MSE 0.129 vs DLinear 0.140; self-supervised fine-tuning further improves to 0.126.
- [[2023_DLinear_Are_Transformers_Effective_LTSF]] — The linear-model critique PatchTST directly answers and whose numbers it supplies/beats.
- [[2024_TiDE_Long_Term_Forecasting]] — Strongest baseline: TiDE is >10× faster in training / 5× faster inference; PatchTST OOMs at L≥1440; PatchTST still wins Weather 96–336 and M5-without-covariates comparisons differ.
- [[2024_Divide_Conquer_Transformer_EV]] — DCT-EV home-charging Transformer inspired by PatchTST's sub-sequence "patch" partitioning idea.
- [[2024_iTransformer_Inverted_Transformers_Effective_Time_Series]] — Prior SOTA baseline framed as "extreme patching"; iTransformer beats PatchTST on ECL (0.178 vs 0.205 avg MSE), Traffic, Solar; PatchTST fails on fluctuating PEMS.
- [[2025_ResMMoT_Informer_Time_Series]] — PatchTST baseline on NASDAQ100 beaten by ResMMoT-Informer (~30–40%); noted as weak at long-term dependencies.
- [[2025_Benchmark_Foundation_Models]] — Best trained-from-scratch baseline for household STLF (MAE_h 0.494–0.535); ranks best at input size 24 but overtaken by foundation models at 96/168.
- 2026 — [[2026_SSM_Transformer_LSTM_Grid_Benchmark]] — Best load-only model in the controlled six-ISO EIA-930 benchmark (avg 5.59% MAPE, 15/30 grid-wins, 7.53 MSE%) but weakest weather utilization of all architectures (ΔMAPE only −0.52 pp vs iTransformer's −1.62) — channel independence caps covariate benefit; still wins rhythmic tasks (solar 23.1%, ancillary nMAE).
- [[2025_Chronos_2_Univariate_to_Universal]] — **PatchTST / TFT / DeepAR / N-BEATS** cited as global deep-learning predecessors; patching heritage (Nie et al. 2023) underpins Chronos-2 patching+embedding Eq.3 with REG token and time-index/mask meta features.
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — **MOIRAI (Woo et al., ICML 2024)**: Masked Encoder-based Universal Time Series Forecasting Transformer (14M Small, 91M Base, 311M Large). Introduces multi-patch size input/output projections (8..128), Any-variate Attention with binary variate biases and RoPE, and 4-component mixture distribution (Student-t, log-normal, neg-binomial, low-var normal). Pre-trained on LOTSA (27.6B obs across 9 domains) with sequence packing.
