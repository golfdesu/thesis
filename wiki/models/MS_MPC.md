---
type: model
name: Multiscenario Stochastic MPC (MS-MPC)
category: Control & Optimization / Model Predictive Control
tags:
  - model
  - ms-mpc
  - stochastic-mpc
  - microgrid-ems
  - scenario-reduction
---

# 🧠 Multiscenario Stochastic MPC (MS-MPC)

## Overview
MS-MPC handles uncertainties in renewable generation and EV arrival/departure by sampling future scenario trees (using Latin Hypercube Sampling) and compressing them via **Two-Stage Simultaneous Backward Scenario Reduction** to solve receding horizon optimization efficiently.

## Key Mathematical Equations
- **Upper Layer Multi-Scenario Objective**:
  $$\min \sum_{j=1}^{N_S} \rho_j \sum_{t=k}^{k+N_u-1} J_T^j(t)$$
- **Lower Layer Individual EV Allocation**:
  $$\min \left| \sum_{i=1}^{n_{\text{EVs}}} p_{\text{EV}}^i(t) - p_{\text{agg,upper}}^{*}(t) \right|$$

## Literature References
- [[2025_Stochastic_MPC_Microgrid_EV]] - Proposed two-layer MS-MPC for V2G microgrid energy management.
