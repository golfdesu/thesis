---
type: model
name: "TFT"
category: Time Series Forecasting
tags: [model, time-series, forecasting]
---

# TFT

## Overview
Temporal Fusion Transformer (Lim et al. 2021) — global deep forecasting model cited as predecessor.

## Literature Usage
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Evaluated as baseline comparison in zero-shot time series benchmark (GiftEval-ZS and Chronos-ZS), where TiRex (35M) outperforms baseline models across short and long horizons.
- [[2025_Chronos_2_Univariate_to_Universal]] — **PatchTST / TFT / DeepAR / N-BEATS** cited as global deep-learning predecessors; patching heritage (Nie et al. 2023) underpins Chronos-2 patching+embedding Eq.3 with REG token and time-index/mask meta features.

## Related Models
- See [[2025_Chronos_2_Univariate_to_Universal]] Table 1/3 for capability comparisons on fev-bench / GIFT-Eval.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — **MOIRAI (Woo et al., ICML 2024)**: Masked Encoder-based Universal Time Series Forecasting Transformer (14M Small, 91M Base, 311M Large). Introduces multi-patch size input/output projections (8..128), Any-variate Attention with binary variate biases and RoPE, and 4-component mixture distribution (Student-t, log-normal, neg-binomial, low-var normal). Pre-trained on LOTSA (27.6B obs across 9 domains) with sequence packing.
