---
type: dataset
name: "fev-bench"
benchmark: true
tasks: 100
tags: [dataset, benchmark, multivariate, covariates]
---

# fev-bench

## Overview
Realistic benchmark for universal forecasting (Shchur et al. 2025) — 100 tasks covering univariate (32), multivariate (26), and covariate-informed (42, past-only + known). Primary benchmark for universal ICL.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated on multivariate zero-shot forecasting benchmark with past and future covariates.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Evaluated on zero-shot forecasting and imputation benchmarks.
- [[2025_Chronos_2_Univariate_to_Universal]] — Primary evaluation (Table 3, Fig. 2-5): Chronos-2 SOTA SQL W 90.7% S 47.3%, 3.6s median, 0% leakage, 0 failures; significant over TiRex 80.8/42.6, TimesFM-2.5 75.9/42.3, Toto-1.0 66.6/40.7. ICL gains largest on covariates subset (40.0->47.0 skill). Energy (16 tasks) and retail (17 tasks) case studies from this benchmark (Fig.6-7: EPF-DE, Rossmann).

## Data Availability
- Paper: Shchur et al. 2025 (arXiv fev-bench).
