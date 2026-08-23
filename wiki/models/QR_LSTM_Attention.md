---
type: model
name: Quantile Regression LSTM-Attention (QR-LSTM-Attention)
category: Deep Learning / Quantile Regression Recurrent Architecture
tags:
  - model
  - qr-lstm-attention
  - quantile-regression
  - lstm-attention
  - crps
---

# 🧠 Quantile Regression LSTM-Attention (QR-LSTM-Attention)

## Overview
QR-LSTM-Attention combines an **LSTM Encoder-Decoder** with an intermediate **Attention Layer** and optimizes quantile-dependent **Pinball Loss** functions to produce probabilistic load interval bounds ($q_{20}, q_{50}, q_{80}$).

## Key Mathematical Equations
- **Pinball Loss Function**:
  $$L_\tau(y, \hat{y}) = \begin{cases} \tau(y - \hat{y}) & y \ge \hat{y} \\ (1 - \tau)(\hat{y} - y) & y < \hat{y} \end{cases}$$
- **Continuous Ranked Probability Score (CRPS)**:
  $$\text{CRPS}(\hat{F}, y) = \sum_{i=1}^N \left( \hat{F}(y_i) - \mathbb{I}_{\{y_i \ge y\}} \right)^2 \Delta y_i$$

## Literature References
- [[2025_Matrone_QR_LSTM_Attention_EV_Load]] - Probabilistic forecasting of EV charging demand using QR-LSTM-Attention (ACM E-Energy 2025).
