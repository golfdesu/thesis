---
type: model
name: N-BEATS
category: Deep Learning / Residual Basis-Expansion MLP Ensemble
tags:
  - model
  - deep-learning
  - mlp
---

# N-BEATS

## Literature Usage
- [[2020_NBEATS_Interpretable_Time_Series_Forecasting]]: A deep stack of fully connected residual blocks produces backcasts and forecasts through learned basis expansions; an interpretable trend/seasonality configuration is also evaluated.
- 2021 — [[2021_Autoformer_Decomposition_Transformers_AutoCorrelation]] : N-BEATS used as univariate baseline; Autoformer cuts Exchange predict-336 MSE 17% (0.508 vs N-BEATS 0.611) and ETT-336 to 0.154 vs 0.226.
- 2022 — [[2022_RevIN_Reversible_Instance_Normalization]] : RevIN normalization slashes N-BEATS ETTh2 @960 MSE from 6.408 to 0.471 and ECL @960 from 0.399 to 0.325 under distribution shift.
- 2023 — [[2023_NHiTS_Neural_Hierarchical_Interpolation]] : N-HiTS beats its N-BEATS ancestor — ETTm2@720 univariate MSE 0.157 vs 0.188, 1.26x faster with 54% of its parameters.
- 2024 — [[2024_Feature_Enhanced_Probabilistic_EV_Load]] : N-BEATS benchmark for day-ahead EV probabilistic forecasting; FEDM reaches QR 99.22%/WS −0.4323 vs N-BEATS QR 96.88%/WS −0.6606.
- [[2024_TimesFM_Decoder_Only_Foundation_Model]] — Strongest Monash supervised baseline (GM 0.7005 vs TimesFM 0.6846); TimesFM within significance of N-BEATS despite zero-shot.
