---
type: model
name: Transformer-BiLSTM Hybrid
category: Deep Learning / Hybrid Attention-Recurrent Architecture
tags:
  - model
  - transformer-bilstm
  - bi-lstm
  - self-attention
  - price-forecasting
---

# 🧠 Transformer-BiLSTM Hybrid Architecture

## Overview
Transformer-BiLSTM combines a **Transformer Encoder** (using multi-head self-attention for parallel global context) with a **Bidirectional LSTM (BiLSTM)** layer (capturing forward and backward local sequential dependencies).

## Key Mathematical Equations
- **BiLSTM Concatenation**:
  $$h_t = [\vec{h}_t \,;\, \overleftarrow{h}_t], \quad \vec{h}_t = \text{LSTM}(x_t, \vec{h}_{t-1}, \vec{C}_{t-1}), \quad \overleftarrow{h}_t = \text{LSTM}(x_t, \overleftarrow{h}_{t+1}, \overleftarrow{C}_{t+1})$$
- **Transformer Encoder Output**:
  $$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \dots, \text{head}_N) W^O$$

## Application in EV Systems
- Outperformed standalone Transformer, BiLSTM, and XGBoost models in Day-Ahead Electricity Price Forecasting (DA EPF) for V2G market bidding ([[2025_Transformer_BiLSTM_Price_Forecasting]]).

## Literature References
- [[2025_Transformer_BiLSTM_Price_Forecasting]] - Day-ahead electricity market price forecasting using Transformer-BiLSTM.
