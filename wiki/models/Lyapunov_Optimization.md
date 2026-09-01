---
type: model
name: Lyapunov Optimization & Virtual Queueing
category: Real-Time Control & Optimization
tags:
  - model
  - lyapunov-optimization
  - virtual-queues
  - stochastic-control
---

# 🧠 Lyapunov Optimization & Virtual Queueing

## Overview
Lyapunov Optimization uses virtual queues ($q(t), z(t)$) to convert time-average constraints (e.g., energy requirements, delay bounds) into queue stability conditions. Minimizing the **Drift-Plus-Penalty** function balances operational cost minimization with system stability.

## Key Mathematical Equations
- **Drift-Plus-Penalty Minimization**:
  $$\min \frac{1}{w} \Delta(\mathbf{\Theta}(t)) + V f(t)$$
- **Demand & Delay Virtual Queues**:
  $$q_g(t+w) = \max\left( q_g(t) + \sum (a_g - x_g), 0 \right)$$
  $$z_g(t+w) = \max\left( z_g(t) - \sum x_g + \frac{\alpha_g}{R_g} \mathbb{I}_g(t), 0 \right)$$

## Application in EV Charging Systems
- Converts short-term EV load forecasts into optimal real-time power dispatch commands.
- Guarantees bounded charging delay $O(w)$ and achieves a cost gap within 1% of offline global optimal ([[2026_Lyapunov_EV_Scheduling]]).

## Literature References
- [[2026_Lyapunov_EV_Scheduling]] - Forecast-Enhanced Lyapunov Optimization for real-time EV charging scheduling.
