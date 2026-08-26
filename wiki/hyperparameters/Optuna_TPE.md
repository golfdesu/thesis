---
type: hyperparameter
name: Optuna TPE (Tree-structured Parzen Estimator)
category: Automated Hyperparameter Optimization / Bayesian Optimization Framework
tags:
  - hyperparameter
  - optuna
  - tpe
  - automated-tuning
---

# ⚙️ Optuna TPE (Tree-structured Parzen Estimator)

## Overview
Optuna is an open-source hyperparameter optimization framework that employs Tree-structured Parzen Estimators (TPE), a Bayesian optimization approach based on kernel density estimators. It efficiently searches continuous, discrete, and categorical hyperparameter spaces (such as layer depth, hidden dimensions, learning rate, and attention heads).

## Key Features & Hyperparameter Search Space
- **Search Strategy**: TPE models $P(x|y)$ using two density distributions for trial values above and below a quantile threshold.
- **Pruning**: Early stopping of unpromising trials (e.g., MedianPruner).
- **Target Parameters**: Learning rate, batch size, LSTM/CNN layer count, dropout rate, number of attention heads.

## Papers Utilizing Optuna TPE
- [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] - Optimized CNN filter size, LSTM hidden units, and Multi-Head Attention heads for 1h, 24h, and 48h DC fast-charging load forecasting.
