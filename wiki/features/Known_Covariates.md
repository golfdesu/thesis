---
type: feature
name: "Known_Covariates"
tags: [feature]
---

# Known_Covariates

## Overview
Known (future-observed) covariates whose future values are available at forecast time.

## Literature Usage
- [[2025_Chronos_2_Univariate_to_Universal]] — Group attention handles known covariates (future values in W) within same group as targets; future-known covariates distinguished by mask and W entries x_{T+1:T+H}; ICL on 42-task covariates subset delivers 40.0->47.0 skill SQL.
