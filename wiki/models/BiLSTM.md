---
type: model
name: "Bidirectional LSTM (BiLSTM)"
category: Stub (auto-generated)
status: needs-review
tags:
  - model
  - bilstm
---

## Overview
[[LSTM]] variant that processes the sequence in both forward and backward directions and concatenates the hidden states, giving each time step access to past and future context.

## Role in EV / Load Forecasting
Used in hybrid models (e.g. Transformer+BiLSTM) where full-sequence context is available at inference.
