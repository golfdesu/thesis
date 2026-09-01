---
type: metric
name: "Win_Rate"
tags: [metric]
---

# Win_Rate

## Overview
Win rate — proportion of pairwise wins vs other models; W = 1-(R-1)/(N-1) where R is average rank (Shchur et al. 2025); more interpretable than rank.

## Literature Usage
- [[2025_Chronos_2_Univariate_to_Universal]] — **Win rate** reported on all 3 benchmarks (Tables 3-5); fev-bench SQL 90.7% (Chronos-2) vs TiRex 80.8, TimesFM-2.5 75.9. Interpretable via R=1+(1-W/100)(N-1).
