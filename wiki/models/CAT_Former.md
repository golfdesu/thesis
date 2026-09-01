---
type: model
name: Context-Aware Temporal Transformer (CAT-Former)
category: Deep Learning / Context-Aware Attention Architecture
tags:
  - model
  - cat-former
  - context-aware
  - spatial-temporal
  - self-attention
---

# 🧠 Context-Aware Temporal Transformer (CAT-Former)

## Overview
CAT-Former fuses **Temporal Features** ($h, dw, dt, dm, sd$) with **Contextual Features** ($S_{\text{lat}}, S_{\text{long}}, W_{\text{temp}}, W_{\text{precip}}, W_{\text{wind}}$) into a unified positional-encoded Transformer self-attention block for short-term EV load forecasting.

## Key Mathematical Equations
- **Input Vector Fusion**:
  $$Z_t = [X_{\text{temporal}, t}, X_{\text{context}, t}], \quad Z'_t = Z_t + P_t$$
- **Attention Output**:
  $$\text{Output}_t = \text{Linear}\left( \text{MultiHead}(Q, K, V) \right)$$

## Literature References
- [[2025_CAT_Former_Short_Term_EV]] - Proposed CAT-Former for 1-hour and 1-day short-term EV station demand forecasting.
