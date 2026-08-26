---
type: metric
name: V2G Scheduling Value Error (V2G-SVE)
category: Evaluation Metric / Forecast Value
tags:
  - metric
  - v2g-sve
  - forecast-value
  - v2g-scheduling
---

# 📐 V2G Scheduling Value Error (V2G-SVE)

## Definition & Mathematical Formulation
V2G-SVE is a value-oriented metric that quantifies the actual operational performance loss ($V_2 - V_1$) in Vehicle-to-Grid (V2G) load variance minimization caused by forecast errors:
$$\text{V2G-SVE} = \frac{V_2 - V_1}{V_1} \times 100\%$$
Where:
- $V_1$: Minimal load variance achieved under perfect ground-truth load forecast.
- $V_2$: Realized load variance when executing scheduling decisions derived from forecasted load.

## Key Advantages over Conventional Quality Metrics (MAPE/RMSE)
- **High Correlation ($r > 0.999$)**: Accurately reflects downstream V2G scheduling value.
- **Fast Computation ($0.20 \text{ seconds}$)**: Uses an Aggregate EV Fleet Model to eliminate the $O(N^3)$ computational burden of full-scale EV optimization.
- **Weights EV Density**: Assigns higher importance to forecast errors occurring during hours with dense EV connection profiles.

## Literature References
- [[2024_Zhong_V2G_SVE_Evaluation_Metric]] - Proposed V2G-SVE metric published in IEEE Transactions on Smart Grid.
