---
type: dataset
title: "Electricity Transformer Temperature Dataset"
name: "Electricity Transformer Temperature Dataset"
location: "Electricity transformer depots (Wenzhou & Chaoyang regions), China"
resolution: "15-min raw; hourly (ETTh1/h2) and 15-min (ETTm1/m2) variants"
access: "open (github.com/zhouhaoyi/ETDataset)"
license: "CC BY-ND 4.0 (zhouhaoyi/ETDataset LICENSE) - share verbatim w/ attribution; no modified redistribution"
commercial_use: allowed
data_type: "2 years of transformer oil temperature + 6 power-load features per station"
status: metadata-verified-2026-08
---

# Electricity Transformer Temperature Dataset

Multivariate transformer-temperature benchmark.

- **Reference**: [https://github.com/zhouhaoyi/ETDataset](https://github.com/zhouhaoyi/ETDataset)

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated on multivariate zero-shot forecasting benchmark with past and future covariates.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Evaluated on zero-shot forecasting and imputation benchmarks.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Evaluated on zero-shot multi-frequency benchmarks within GIFT-Eval test suite.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Evaluated under zero-shot forecasting setting within GiftEval / Chronos-ZS benchmarks.
- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — TSLib evaluation: ETTh1/ETTh2/ETTm1/ETTm2 horizons 96/192/336/720, context 2880; Sundial-L best on 4/6 sets (e.g., ETTm1 MSE 0.331 vs Time-MoE 0.356, Chronos-L 0.555).
- [[2024_TimesFM_Decoder_Only_Foundation_Model]] — Evaluation (not pretraining): ETTh1/ETTh2/ETTm1/ETTm2 (2-year transformer temperature) horizons 96/192, last-window; TimesFM ZS avg MAE 0.36 vs PatchTST 0.37, Informer 0.99.
