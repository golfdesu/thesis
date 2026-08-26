---
type: model
name: Feature-Enhanced Deep Learning Method (FEDM)
category: Deep Learning / Probabilistic Feature-Selection Architecture
tags:
  - model
  - fedm
  - feature-selection
  - grn
  - glu
  - quantile-loss
---

# 🧠 Feature-Enhanced Deep Learning Method (FEDM)

## Overview
FEDM combines statistical Pearson correlation analysis ($r_{X,Y}$) for prior feature weight initialization with **Gated Residual Networks (GRN)**, **Gated Linear Units (GLU)**, and **Multi-Head Self-Attention** for station-level probabilistic load forecasting.

## Key Mathematical Equations
- **Prior Pearson Reweighting**:
  $$\mu_X = \text{Softmax}\left(\text{GRN}(\tilde{X}, r_X)\right)$$
- **Gated Residual Network**:
  $$\text{GRN}_\omega(Y, X) = \text{Norm}(Y + \text{GLU}_\omega(d_1))$$
  $$\text{GLU}_\omega(d_1) = \sigma\left(W_\omega^{(4)} d_1 + b_\omega^{(4)}\right) \odot \left(W_\omega^{(5)} d_1 + b_\omega^{(5)}\right)$$

## Literature References
- [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] - Proposed FEDM achieving 99.22% Qualified Rate in 15-minute probabilistic EV load forecasting.
