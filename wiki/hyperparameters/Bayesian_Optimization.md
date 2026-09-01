---
type: hyperparameter
name: Bayesian Optimization
category: Sequential Model-Based Optimization (SMBO)
tags:
  - hyperparameter
  - bayesian-optimization
  - gaussian-process
---

# ⚙️ Bayesian Optimization

## Overview
Bayesian Optimization constructs a probabilistic surrogate model (typically a Gaussian Process) to approximate the objective function (e.g., validation loss/RMSE) and uses an acquisition function (such as Expected Improvement or Upper Confidence Bound) to balance exploration and exploitation.

## Key Advantages
- **Sample Efficiency**: Significantly reduces the number of expensive training iterations compared to [[Grid_Search]].
- **Continuous & Discrete Search**: Effective for continuous hyperparameters like learning rate, weight decay, and kernel bandwidths.

## Papers Utilizing Bayesian Optimization
- [[2022_Robust_Deep_Gaussian_Process_Load]] - Variational hyperparameter inference for Deep Gaussian Processes.
- [[2024_MQ_TCN_Transfer_Learning_EV]] - Optimized Multi-Quantile Temporal Convolutional Network (MQ-TCN) dilation factors and loss weights.
