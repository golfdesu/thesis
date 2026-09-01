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
Optuna is an open-source hyperparameter optimization framework that employs Tree-structured Parzen Estimators (TPE), a [[Bayesian_Optimization]] approach based on kernel density estimators. It efficiently searches continuous, discrete, and categorical hyperparameter spaces (such as layer depth, hidden dimensions, learning rate, and attention heads).

## Key Features & Hyperparameter Search Space
- **Search Strategy**: TPE models $P(x|y)$ using two density distributions for trial values above and below a quantile threshold.
- **Pruning**: Early stopping of unpromising trials (e.g., MedianPruner).
- **Target Parameters**: Learning rate, batch size, LSTM/CNN layer count, dropout rate, number of attention heads.

## Papers Utilizing Optuna TPE
- [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] - Optimized CNN filter size, LSTM hidden units, and Multi-Head Attention heads for 1h, 24h, and 48h DC fast-charging load forecasting.
- [[2026_Khwaja_Toto_2_Scaling_Era]] — 4-round Optuna TPE (Watanabe 2023) structured search on 10M proxy (30k steps, WSD schedule, MASE+CRPS on GIFT-Eval val): R1 architecture (PerDimScale, variate-attn last, cmax 16/pmax 0.4), R2 data simplex (42.5% observability/57.5% synthetic, public 0), R3 optimizer (NorMuon eta 0.652/mu 0.96/beta2 0.999 vs AdamW 0.012/0.91/0.972, warmup 6k/clip 7.0), R4 decay (linear 10.5k). Transfer via u-muP.
