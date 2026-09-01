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
- [[2025_Liu_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — Compared as supervised/point-forecasting baseline in GIFT-Eval (e.g., PatchTST MASE 0.762, N-BEATS 21.38 rank).
- [[2024_Das_TiDE_Long_Term_Forecasting]]: Dense residual MLP encoder-decoder blocks encode historical series and covariates, then decode the horizon using future covariates with linear scaling in context and horizon length.
- 2024 — [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] : TiDE appears among the benchmarked models; inverted iTransformer posts avg ECL MSE 0.178/MAE 0.270 and Traffic 0.428/0.282, with the inversion itself cutting vanilla Transformer MSE 35.6–86.1%.
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Same first author (Das) — residual-block design reused in TimesFM Input/Output blocks (cf. [[2024_Das_TiDE_Long_Term_Forecasting]]).
