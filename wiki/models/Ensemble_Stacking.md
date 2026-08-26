---
type: model
name: Ensemble Stacking Learning
category: Machine Learning / Ensemble Methods
tags:
  - model
  - ensemble
  - stacking
  - meta-learning
---

# 🧠 Ensemble Stacking Learning

## Overview
Ensemble Stacking is a meta-learning architecture that combines predictions from multiple diverse base models (e.g., ANN, RNN, LSTM) using a meta-learner (e.g., Linear Regression) to compute weighted predictions.

## Key Mathematical Equations
$$\hat{y}_t = w_0 + \sum_{i=1}^M w_i P_t^i$$
Where $P_t^i$ is the forecast output from base model $i$, and weights $\mathbf{w}$ are learned by minimizing error on validation fold data.

## Advantages in EV Load Forecasting
- Reduces prediction variance and avoids relying on a single neural network architecture.
- Outperformed individual ANN, RNN, and LSTM models in EV charging station load forecasting ([[2020_Huang_Ensemble_EV_Load]]).

## Literature References
- [[2020_Huang_Ensemble_EV_Load]] - Applied Linear Regression stacking over ANN, RNN, and LSTM for EV load forecasting in Boulder, Colorado.
- [[2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] - XGBoost-BiLSTM stacking ensemble with an XGBoost meta-learner for hourly station-level EV charging load; removing the meta-learner raised MAE by +30.5% (2.687→3.507 kWh), and it led walk-forward validation with mean MAE 2.535 kWh.
