---
type: metric
name: "Hausdorff Distance"
category: geometric-distance-metric
formula: "d_H(A,B) = max( max_a min_b ‖a−b‖ , max_b min_a ‖a−b‖ )"
unit: Same as the embedding space metric (per set pair)
last_updated: 2026-08-26
tags:
  - metric
  - hausdorff_distance
  - set-distance
---

# Hausdorff Distance

## Definition

**Hausdorff distance** measures the worst-case mismatch between two point sets $A, B$ in a metric space:

$$d_H(A, B) = \max\Big\{ \sup_{a \in A} \inf_{b \in B} \|a-b\|,\; \sup_{b \in B} \inf_{a \in A} \|a-b\| \Big\}$$

The two inner terms ($h(A,B)$, directed distances) capture how far each set is from being contained in the other; the outer max makes it symmetric. In EV-cluster forecasting ([[2026_Tang_PC_M3_Mamba_EV_Clusters]]) it scores how closely a forecast feasibility *envelope* hugs the true polytope boundary — small $d_H$ means every predicted boundary point lies near a true one and vice versa.

| Property | Description |
|----------|-------------|
| **Lower is better** | ✅ Yes (0 = identical sets) |
| **Sensitive to outliers** | ⚠️ Worst-case — one stray point dominates; use the mean variant (modified Hausdorff) if that is undesirable |

## Referenced in this knowledge base

[[2026_Tang_PC_M3_Mamba_EV_Clusters]]
