---
type: model
name: TiDE
category: Deep Learning / Dense MLP Encoder-Decoder Forecaster
tags:
  - model
  - deep-learning
  - mlp
---

# TiDE

## Literature Usage
- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — Compared as supervised/point-forecasting baseline in GIFT-Eval (e.g., PatchTST MASE 0.762, N-BEATS 21.38 rank).
- [[2024_TiDE_Long_Term_Forecasting]]: Dense residual MLP encoder-decoder blocks encode historical series and covariates, then decode the horizon using future covariates with linear scaling in context and horizon length.
- 2024 — [[2024_iTransformer_Inverted_Transformers_Effective_Time_Series]] : TiDE appears among the benchmarked models; inverted iTransformer posts avg ECL MSE 0.178/MAE 0.270 and Traffic 0.428/0.282, with the inversion itself cutting vanilla Transformer MSE 35.6–86.1%.
- [[2024_TimesFM_Decoder_Only_Foundation_Model]] — Same first author (Das) — residual-block design reused in TimesFM Input/Output blocks (cf. [[2024_TiDE_Long_Term_Forecasting]]).
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — **MOIRAI (Woo et al., ICML 2024)**: Masked Encoder-based Universal Time Series Forecasting Transformer (14M Small, 91M Base, 311M Large). Introduces multi-patch size input/output projections (8..128), Any-variate Attention with binary variate biases and RoPE, and 4-component mixture distribution (Student-t, log-normal, neg-binomial, low-var normal). Pre-trained on LOTSA (27.6B obs across 9 domains) with sequence packing.
