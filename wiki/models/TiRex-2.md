---
type: model
name: "TiRex-2"
category: foundation-model
tags: [model, xlstm, multivariate, streaming, foundation-model]
---

# TiRex-2

## Overview
A recurrent xLSTM-based time series foundation model (82.5M parameters) that extends TiRex to multivariate forecasting with past and future-known covariates. It combines a bidirectional xLSTM time mixer with an asymmetric grouped-attention variate mixer, enabling constant $\mathcal{O}(1)$ inference cost per patch under streaming.

## Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Introduces TiRex-2, achieving SOTA zero-shot multivariate forecasting on fev-bench and GIFT-Eval.
