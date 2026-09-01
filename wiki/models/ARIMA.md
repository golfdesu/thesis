---
type: model
name: "AutoRegressive Integrated Moving Average (ARIMA)"
category: Stub (auto-generated)
status: needs-review
tags:
  - model
  - arima
---

## Overview
Classical linear statistical time-series model combining autoregression, differencing (integration), and moving-average terms.

## Role in EV / Load Forecasting
Traditional baseline for load forecasting; reviewed in [[2001_Hippert_Neural_Networks_STLF_Review]]. Seasonal variants include SARIMA.

## Key References
- [[2001_Hippert_Neural_Networks_STLF_Review]]

## Literature Usage
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Statistical baseline: (DHR-)ARIMA on Monash (GM 0.9449) and ARIMA on Darts (GM 0.5219 best); TimesFM competitive without seasonal tuning.
