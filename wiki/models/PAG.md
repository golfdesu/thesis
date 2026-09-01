---
type: model
name: PAG (Physics-Informed Attention Graph)
category: Deep Learning / Physics-Informed Graph Learning
tags:
  - model
  - pag
  - physics-informed
  - gat
  - tpa-lstm
  - price-elasticity
---

# 🧠 PAG (Physics-Informed Attention Graph)

## Overview
PAG integrates **Physics-Informed Meta-Learning (PIML)** pre-training with a **Graph Attention Network (GAT)** spatial module and a **TPA-LSTM** temporal decoder to solve price misinterpretation in regional EV charging load forecasting.

## Key Mathematical Equations
- **Price Elasticity Pseudo-Sampling**:
  $$\Delta y_i = -1.48 \left(\frac{\Delta p_i}{p_i}\right) y_i, \quad \Delta y_j = -\frac{1}{N} \Delta y_i$$
- **FOMAML Meta-Pre-Training**:
  $$\phi_{e+1} = \phi_e - \lambda \frac{\nabla_\phi L(\phi)}{S}$$
- **GAT Momentum Residuals**:
  $$\mathbf{x}_i'' = \parallel_{m=1}^M \left[ (1-\beta)\mathbf{x}_i'^m + \beta \mathbf{x}_i'^{m-1} \right]$$

## Literature References
- [[2024_Physics_Informed_GAT_EV_Load]] - Proposed PAG framework evaluated on 18,061 charging piles across 247 traffic zones in Shenzhen.

## 📚 Literature Usage
- 2024 — [[2024_Physics_Informed_GAT_EV_Load]] : Proposed PAG; strongest baseline in later work — average RMSE 5.48 across 15–60 min horizons, MAPE 16.87 on Shenzhen charging demand.
- 2026 — [[2026_Mamba_KAN_HyKANet_EV]] : PAG was the best baseline that HyKANet surpassed — avg RMSE cut from 5.48 to 4.67 (up to 14.8% improvement), MAE 3.33 → 2.49 (−12.2%), MAPE 16.87 → 15.33.
