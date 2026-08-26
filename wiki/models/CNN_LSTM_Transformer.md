---
type: model
name: CNN-LSTM-Transformer
category: Deep Learning / Hybrid Convolutional-Recurrent Self-Attention Architecture
tags:
  - model
  - cnn-lstm-transformer
  - fast-charging
  - multi-head-attention
  - multi-step-forecasting
---

# 🧠 CNN-LSTM-Transformer Architecture

## Overview
CNN-LSTM-Transformer combines 1D-CNN feature extraction, LSTM sequential encoding, and a Transformer Encoder with Multi-Head Self-Attention (MHA) and residual MLP normalization for multi-step day-ahead load forecasting (24h to 48h).

## Key Mathematical Equations
- **Transformer Block**:
  $$\hat{H} = \text{Norm}(H + \text{MHA}(Q, K, V)), \quad H' = \text{Norm}(\hat{H} + \text{MLP}(\hat{H}))$$

## Literature References
- [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] - Proposed CNN-LSTM-Transformer for 24h and 48h multi-step fast-charging load forecasting.
- 2023 — [[2023_Xiong_Combined_Deep_Learning_EV_Station_STLF]] : serial CNN→LSTM→Transformer on the Boulder ST1 station (24-h lookback, single-step ahead) achieves RMSE 0.300 / MAE 0.120, beating every pairwise combination; notably LSTM+Transformer *without* CNN is worst (RMSE 0.428), showing CNN local feature extraction is essential before attention.
