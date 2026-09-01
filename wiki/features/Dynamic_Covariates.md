---
type: feature
name: "Dynamic Covariates"
category: feature
tags: [feature, covariates, exogenous]
---

# Dynamic Covariates

## Overview
Known exogenous features whose values are available across both the historical lookback and the future forecasting horizon (e.g., calendar time-of-day, day-of-week, holidays, planned events, scheduled charging slots).

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Split into past covariates $V_{pcov}$ and future-known covariates $V_{fcov}$ and integrated via asymmetric variate attention.
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Integrated through a dedicated cross-channel attention module ($Z_{agg}$) to model inter-variable dependencies.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Scales continuous SSM state transitions using sampling-rate ratios $s_{\Delta}$.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Encodes missing value and unobserved future steps via concatenated binary indicator mask channel.
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — MOIRAI natively incorporates dynamic covariates alongside target variates via flattened sequence representation with known horizon tokens.
