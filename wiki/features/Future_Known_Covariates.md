---
type: feature
name: "Future Known Covariates"
category: feature
tags: [feature, covariates, exogenous-variables, future-known]
---

# Future Known Covariates

## Overview
Exogenous time series that are known ahead of time over the forecasting horizon (e.g., weather forecasts, calendar features, day-ahead electricity prices, scheduled events).

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — TiRex-2 processes future-known covariates via bidirectional xLSTM and fuses them with strictly causal target series using asymmetric attention masks.
