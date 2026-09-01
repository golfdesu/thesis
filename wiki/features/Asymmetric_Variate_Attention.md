---
type: feature
name: "Asymmetric Variate Attention"
category: feature
tags: [feature, attention, multivariate, cross-variate]
---

# Asymmetric Variate Attention

## Overview
A grouped cross-channel attention masking mechanism that allows target queries to attend to all covariate channels while preventing future-covariate queries from reading target keys to enforce strict causality.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Variate mixer mechanism in TiRex-2 to integrate future covariates without target leakage.
