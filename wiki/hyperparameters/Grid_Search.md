---
type: hyperparameter
name: Grid Search & Random Search
category: Exhaustive / Random Hyperparameter Search
tags:
  - hyperparameter
  - grid-search
  - random-search
---

# ⚙️ Grid Search & Random Search Optimization

## Overview
Grid Search evaluates model performance across an exhaustive Cartesian product of predefined hyperparameter grids, whereas Random Search samples random combinations from a defined distribution. These methods provide straightforward baselines for selecting parameters such as learning rate, batch size, weight decay, tree depth, and hidden layer dimensions.

## Target Parameters Evaluated
- **Learning Rate ($\eta$)**: e.g., $\{10^{-4}, 10^{-3}, 10^{-2}\}$.
- **Tree Ensembles (XGBoost/LightGBM)**: Max depth, number of estimators, subsampling ratio, colsample_bytree.
- **Neural Networks**: Hidden dimensions $\{32, 64, 128, 256\}$, dropout rate $\{0.1, 0.2, 0.5\}$.

## Papers Utilizing Grid / Random Search
- [[2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] - Used grid search to tune XGBoost max depth, learning rate, and BiLSTM hidden units.
- [[2021_VanKriekinge_Day_Ahead_EV_Demand]] - Grid search over temporal feature encodings, sequence length, and hidden layer counts.
- [[2019_Zhu_ApplSci_EV_Load_Forecasting]] - Tuned GRU/LSTM layer depths and look-back window sizes.
