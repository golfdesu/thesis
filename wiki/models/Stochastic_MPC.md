---
type: model
name: Stochastic Model Predictive Control (Stochastic MPC)
category: Control / Scenario-Based Receding-Horizon Optimization
tags:
  - model
  - mpc
  - stochastic-control
  - energy-management
---

# 🎛️ Stochastic MPC

## Overview
**Scenario-based stochastic MPC** propagates forecast uncertainty into the control loop: at each step, probabilistic forecasts are sampled into a **scenario tree**, and a receding-horizon optimization minimizes expected cost over all branches subject to **nonanticipativity** (one control until uncertainty resolves, or recourse after the first step). In the charging-energy-hub formulation of Fernandez-Zapico et al. (CDC 2025):

- $n_s=3$ scenarios per variable (EnbPI ensemble mean, 5th, 95th percentiles) × $n_v=3$ variables (EV load, PV, price), assuming cross-variable independence → $N_s=27$ equally probable branches $\rho_s=1/N_s$.
- Inner problem is a convex **second-order cone program (SOCP)** (quadratic battery-loss + grid-cost relaxations), solved closed-loop every ΔT=0.25 h over a 96-step day.
- Variants: **Stochastic MPC** (control shared across scenarios for the whole window R={0,…,95}) vs **Recourse MPC** (nonanticipativity relaxed to the first step R={0}); benchmarks: deterministic point-forecast ($N_s$=1) and omniscient perfect-forecast bounds.

## Typical Usage in EV Load Forecasting
- **Input**: probabilistic [[Day_Ahead_Forecasting]] scenarios ([[EnbPI]]-wrapped GBT in the CDC paper).
- **Strengths**: hedges branch outcomes — cost 112.76% of omniscient vs deterministic 113.65%, CO₂ −0.3%; runtime 0.743 min/episode fits the control budget.
- **Weaknesses**: value over deterministic control is small (~0.9–1%) when point forecasts are already good; independence between variables ignores Pev×Ppv×pel correlation; equal scenario probabilities rather than learned; simulation only.

## 📚 Literature Usage
- [[2025_Stochastic_MPC_Conformal_Hub]] — Conformal-prediction scenarios feeding SOCP-based stochastic/recourse MPC of an EV+PV+BESS hub over 280 evaluation days.
- Related microgrid-EV line: [[2025_Stochastic_MPC_Microgrid_EV]]; aggregator flexibility variant: [[MS_MPC]].

## Related Pages
- [[EnbPI]]
- [[Day_Ahead_Forecasting]]
