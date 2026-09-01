---
type: dataset
name: "Chronos Corpus"
tags: [dataset, pretraining, univariate]
---

# Chronos Corpus

## Overview
Pretraining corpus from Ansari et al. 2024 (Chronos) — select datasets (Table 6 of [[2025_Chronos_2_Univariate_to_Universal]]) reused in Chronos-2 real-univariate mix along with GIFT-Eval pretraining corpus and synthetic generators.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated on multivariate zero-shot forecasting benchmark with past and future covariates.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Evaluated on zero-shot multi-frequency benchmarks within GIFT-Eval test suite.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Incorporates 30 million real time series from `autogluon/chronos_datasets` augmented with z-score TsMixup ($K_{max}=4, \alpha=1.5$).
- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — 94B-point subset of TimeBench (9.11%) — see TimeBench composition.
- [[2025_Chronos_2_Univariate_to_Universal]] — Real univariate component of Chronos-2 pretraining (Table 6 lists Electricity, M4, Solar, Traffic, Wiki, Buildings 900K, etc. with frequencies and series counts).

## Data Availability
- Ansari et al. 2024; HuggingFace.
- [[2026_Moirai_2_When_Less_Is_More]] — Used as pretraining/evaluation data (Moirai 2.0): see paper §4 & Fig. 2–5, Table 1–2. GIFT-Eval 97 tasks (55 datasets) for evaluation; GIFT-Eval Pretrain (3.25M/230B) as pretrain foundation; Chronos-Mixup (30M/63B) & KernelSynth (1M/1.02B) as synthetic augmentation; internal Salesforce telemetry (2.15M/1.48B daily) as proprietary source. Normalized MASE/CRPS via gift-eval replication code.
