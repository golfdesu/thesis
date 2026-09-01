---
type: model
name: Multi-Scale Spatial-Temporal Graph Attention Network (MSSTGAN)
category: Deep Learning / Spatio-Temporal Graph Neural Network
tags:
  - model
  - msstgan
  - graph-attention
  - pyramid-split-attention
  - spatio-temporal
---

# 🧠 Multi-Scale Spatial-Temporal Graph Attention Network (MSSTGAN)

## Overview
MSSTGAN combines **Pyramid Split Attention (PSA)** for multi-scale temporal resolution with **Graph Attention Networks (GAT)** and **Adaptive Gated Fusion** for city-wide multi-station load forecasting.

## Key Mathematical Equations
- **Pyramid Split Spatial Attention**:
  $$S_i = \text{split}(\text{AveragePooling}(H^{(l-1)}))$$
  $$H_S^{(l)} = \text{Softmax}\left(\frac{X_q X_k^T}{\sqrt{D}}\right) X_v$$
- **Adaptive Gated Fusion**:
  $$H^{(l)} = z \odot H_S^{(l)} + (1-z) \odot H_T^{(l)}, \quad z = \text{Sigmoid}(H_S^{(l)} W_{z,1} + H_T^{(l)} W_{z,2} + b_z)$$

## Literature References
- [[2025_MSSTGAN_City_EV_Load]] - Proposed MSSTGAN for city-level EV charging station network load forecasting.
