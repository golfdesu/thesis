---
type: model
name: EV Scheduling Feasible Domain (EVSFD)
category: Optimization / Feasible Space Modeling
tags:
  - model
  - evsfd
  - feasible-domain
  - schedulable-capacity
---

# 🧠 EV Scheduling Feasible Domain (EVSFD)

## Overview
EV Scheduling Feasible Domain (EVSFD) defines the multi-dimensional feasible state space $A_n$ of EV battery state-of-charge ($S_{n,t}$) and charging/discharging power ($p_{n,t}$) bounded by physical constraints, battery SOC boundaries, and user departure energy requirements.

## Key Mathematical Equations
- **SOC Boundaries**: $S_n^{\min} \le S_{n,t} \le S_n^{\max}$
- **Power Boundaries**: $p_n^{\min} \le p_{n,t} \le p_n^{\max}$
- **User Energy Demand Constraint**: $S_{n, t_n^d} \ge S_{n, t_n^d}^{\text{target}}$
- **EV Schedulable Capacity (EVSC)**:
  $$p_{n,t}^{sc} = [p_{n,t} - p_n^{\min}, p_n^{\max} - p_{n,t}]$$

## Literature References
- [[2024_Day_Ahead_EVCB_EVSC_Parking_Lot]] - Derived EVSFD for EV parking lots participating in day-ahead energy markets.
