---
type: feature
name: "Missing Value Mask"
category: feature
tags: [feature, mask, missing-values, imputation]
---

# Missing Value Mask

## Overview
Binary presence/absence indicator channels concatenated or embedded alongside input time series to distinguish observed timestamps from missing/unobserved positions.

## Literature Usage
- [[2026_TS_ICL_Time_Indexed_Foundation_Model]] — Used in timestamp-aligned regression to coordinate forecasting and missing-value imputation.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Concatenated to raw input patches in TiRex to enable Contiguous Patch Masking (CPM).
