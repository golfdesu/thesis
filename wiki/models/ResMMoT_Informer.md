---
type: model
name: ResMMoT-Informer
category: Deep Learning / Sparse MoE Multiscale Architecture
tags:
  - model
  - resmmot-informer
  - moe
  - multiscale-tcn
  - informer
---

# 🧠 ResMMoT-Informer Architecture

## Overview
ResMMoT-Informer integrates a **Residual Multiscale TCN Sparse Mixture of Experts (ResMMoT)** for multiscale local feature extraction with an **Informer Transformer** for long-sequence global dependencies.

## Key Mathematical Equations
- **Top-$K$ Sparse MoE Routing**:
  $$y = \sum_{i \in S} g_i(x) \cdot f_i(x), \quad S = \text{TopK}(\text{Softmax}(W_g x), K)$$
- **Informer ProbSparse Attention**:
  $$\mathcal{A}(Q, K, V) = \text{Softmax}\left(\frac{\bar{Q} K^T}{\sqrt{d}}\right) V$$

## Literature References
- [[2025_Bao_ResMMoT_Informer_Time_Series]] - Proposed ResMMoT-Informer achieving 30-40% error reduction on volatile time series forecasting.
