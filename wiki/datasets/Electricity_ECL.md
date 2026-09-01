---
type: dataset
name: "Electricity (ECL) Dataset"
category: Stub (auto-generated)
status: needs-review
tags:
  - dataset
  - electricity_ecl
---

## Overview
UCI Electricity Load Diagrams / Electricity Consumption Label (ECL): hourly electricity consumption of 321 clients from 2012–2014, a standard long-term forecasting benchmark.

access: open
resolution: hourly

## Usage in EV / Load Forecasting
Standard benchmark in LTSF papers ([[Informer]], [[Autoformer]], [[PatchTST]], [[DLinear]], [[TimesNet]]) alongside [[ETT]] and [[Weather]].

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated on multivariate zero-shot forecasting benchmark with past and future covariates.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Evaluated on zero-shot forecasting and imputation benchmarks.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Evaluated on zero-shot multi-frequency benchmarks within GIFT-Eval test suite.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Evaluated under zero-shot forecasting setting within GiftEval / Chronos-ZS benchmarks.
- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — TSLib ECL (hourly, 321 clients) zero-shot; Sundial-L 0.166/0.262 vs Timer-XL 0.174/0.278, Chronos-L 0.204/0.273.
- [[2025_Chronos_2_Univariate_to_Universal]] — 370 series (Table 6) in Chronos-2 real-univariate pretraining mix (Electricity).

## Used-by

- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — Pre-training archive / evaluation benchmark for MOIRAI 1.0 (Woo et al., ICML 2024). Part of the 27.6B observation LOTSA archive spanning 9 domains; evaluated on Monash, LSF, and out-of-distribution rolling CRPS/MSIS.
