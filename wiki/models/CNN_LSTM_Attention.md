---
type: model
name: CNN-LSTM-Attention
category: Deep Learning / Hybrid Convolutional-Recurrent Attention Architecture
tags:
  - model
  - cnn-lstm-attention
  - fast-charging
  - single-head-attention
---

# 🧠 CNN-LSTM-Attention Architecture

## Overview
CNN-LSTM-Attention combines 1D Convolutional layers for spatial/local feature extraction, stacked LSTM layers for sequential memory, and a Single-Head Attention (SHA) layer to dynamically weight recent observations for single-step short-term forecasts.

## Key Mathematical Equations
- **Single-Head Attention Weighting**:
  $$\text{score}(Q, K) = Q^T K, \quad \alpha_m = \frac{\exp(e_m)}{\sum_{k=1}^n \exp(e_k)}, \quad \text{Attention}(Q, K, V) = \sum_{m=1}^n \alpha_m h_m$$

## Literature References
- [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] - Proposed CNN-LSTM-Attention for 1-hour fast-charging load forecasting (MAE=2.98 kW, latency=0.742ms).
