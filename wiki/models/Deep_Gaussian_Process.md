---
type: model
name: Deep Gaussian Process (DGP)
category: Machine Learning / Bayesian Nonparametrics
tags:
  - model
  - deep-gaussian-process
  - dgp
  - bayesian
  - uncertainty-quantification
---

# 🧠 Deep Gaussian Process (DGP)

## Overview
Deep Gaussian Process (DGP) is a multi-layer hierarchical generalization of Gaussian Processes (GP). Stacking Sparse GPs via variational inference enables self-tuning covariance functions capable of learning non-linear feature representations without overfitting on small datasets.

## Key Mathematical Equations
- **Evidence Lower Bound (ELBO)**:
  $$\mathcal{L}_{\text{DGP}} = \sum_{i=1}^N \mathbb{E}_{q(f_i^L)} [\log p(y_n | f_n^L)] - \sum_{l=1}^L \text{KL}[ q(U^l) || p(U^l) ]$$
- **Reparameterized Layer Sampling**:
  $$\hat{f}_i^l = m_{\mu^l, Z^{l-1}}(\hat{f}_i^{l-1}) + \xi_i^l \odot \sqrt{S_{\Sigma^l, Z^{l-1}}(\hat{f}_i^{l-1}, \hat{f}_i^{l-1})}$$

## Application in EV / Power Systems Load Forecasting
- Performs exceptionally well under **limited training data** and **anomalous events** (e.g. lockdowns, new charging stations) where deep neural networks overfit ([[2022_Cao_Robust_Deep_Gaussian_Process_Load]]).
- Quantifies epistemic and aleatoric uncertainties via closed-form Prediction Intervals (PIs).

## Literature References
- [[2022_Cao_Robust_Deep_Gaussian_Process_Load]] - Doubly stochastic variational inference DGP for load forecasting under data scarcity.
