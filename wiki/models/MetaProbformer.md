---
type: model
name: MetaProbformer (Reptile + Probformer)
category: Machine Learning / Meta-Learning & Transformers
tags:
  - model
  - meta-learning
  - reptile
  - informer
  - probabilistic-forecasting
---

# 🧠 MetaProbformer (Reptile + Probformer)

## Overview
MetaProbformer combines an Informer-adapted probabilistic model (**Probformer**) with the **Reptile Meta-Learning Framework**. It solves the problem of few-shot EV load forecasting at new charging stations with scarce historical data.

## Key Mathematical Equations
- **Reptile Meta-Update Rule**:
  $$\theta \leftarrow \theta + \beta \frac{1}{J} \sum_{j=1}^J (\theta_j' - \theta)$$
- **ProbSparse Self-Attention Sparsity**:
  $$\bar{S}(q_l, K) = \max_m \left\{ \frac{q_l k_m^T}{\sqrt{d}} \right\} - \frac{1}{d_k} \sum_{m=1}^{d_k} \frac{q_l k_m^T}{\sqrt{d}}$$

## Literature References
- [[2023_MetaProbformer_EV_Load]] - Proposed MetaProbformer for probabilistic EV load forecasting across multiple datasets.
