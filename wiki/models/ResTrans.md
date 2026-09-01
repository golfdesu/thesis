---
type: model
name: Multi-Branch ResNet-Transformer (ResTrans)
category: Deep Learning / Spatial-Temporal Architecture
tags:
  - model
  - restrans
  - resnet
  - transformer
  - spatial-temporal
---

# 🧠 Multi-Branch ResNet-Transformer (ResTrans)

## Overview
Multi-Branch ResTrans combines a **Multi-Branch Residual Network (ResNet)** for spatial feature extraction with a **Transformer Encoder Stack (1D CNN sub-layers)** for temporal modeling.

## Key Mathematical Equations
- **Multi-Branch ResNet Feature Aggregation**:
  $$Z_D = Z_0 + \sum_{j=1}^J \sum_{i=0}^I G(Z_{i,j}, \Phi_{i,j})$$
- **Gradient Identity Flow**:
  $$\frac{\partial \mathcal{L}}{\partial Z_0} = \frac{\partial \mathcal{L}}{\partial Z_D} \left( 1 + \frac{\partial}{\partial Z_0} \sum G(Z_{i,j}, \Phi_{i,j}) \right)$$

## Application in Renewable & Power Load Forecasting
- Simultaneously captures multi-resolution spatial correlations across geographically distributed generation/charging sites while processing long-sequence temporal signals in parallel ([[2023_Multi_Branch_ResTrans_Solar]]).

## Literature References
- [[2023_Multi_Branch_ResTrans_Solar]] - Proposed Multi-Branch ResTrans achieving 97% R2 in spatio-temporal solar irradiance forecasting.
