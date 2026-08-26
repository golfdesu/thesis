---
type: model
name: Partial Input Convex Neural Network (PICNN)
category: Deep Learning / Convex Learning Architecture
tags:
  - model
  - picnn
  - convex-learning
  - quantile-crossing
  - probabilistic-forecasting
---

# 🧠 Partial Input Convex Neural Network (PICNN)

## Overview
PICNN is a neural network architecture designed to learn functions that are strictly convex with respect to a subset of input variables (e.g. quantile level $\alpha \in (0, 1)$). Taking the gradient with respect to $\alpha$ guarantees strictly monotonic non-decreasing quantile predictions, completely eliminating the **Quantile Crossing Problem**.

## Key Mathematical Equations
- **Quantile Function Gradient**:
  $$q(\alpha | h) = \nabla_\alpha f(\alpha, h) = \frac{\partial v_k}{\partial \alpha}$$
- **Quantile Monotonicity Condition**:
  $$(q_{Z,t}(\alpha_1) - q_{Z,t}(\alpha_2))(\alpha_1 - \alpha_2) \ge 0, \quad \forall \alpha_{1,2} \in (0, 1)$$

## Literature References
- [[2025_Zheng_Coherent_Hierarchical_EV_Load]] - Applied PICNN to prevent quantile crossing in multi-horizon EV charging demand probabilistic forecasting.
