---
type: dataset
name: Florida Census Block Group Smart Meter Data
location: Leon County (Tallahassee), Florida, USA
resolution: 30-minute smart-meter readings aggregated to Census Block Groups
access: restricted (NDA — utility-partner data, not public)
data_type: CBG-level aggregate electricity consumption (kWh), 201 CBGs × 17,520 steps/year
urls: []
tags:
  - dataset
  - smart-meter
  - energy-consumption
  - restricted-data
---

# 📁 Florida CBG Smart Meter Data

## Overview
Household-level electricity consumption from **60k+ smart meters** of a municipal utility in Leon County, FL, automatically recorded every 30 minutes and aggregated to **201 Census Block Groups (CBGs)**. Two annual slices are used in the literature:
- **Florida 1**: calendar year 2018 (17,520 steps) — includes **Hurricane Michael** (Oct 2018) extreme-event shift.
- **Florida 2**: calendar year 2019 (17,520 steps) — record heat waves.

Missing readings (~0.3%) imputed by linear interpolation; IQR-based outlier screening retains genuine extreme values; log-normalization $X'=\ln(X+1)$ applied.

> [!WARNING] Not public
> The raw data is utility-partner data under an NDA — no public portal exists. Access requires agreement with the provider.

## 📚 Used By
- [[2026_EnergyMamba_Graph_Mamba_ASCQR]] — Primary benchmark for GE-Mamba/[[AS_CQR]] (Florida 1 MAE 36.57 / IS 231.86 vs best baseline ST-LLM 38.49 / 246.66); graph adjacency from CBG centroid distances.

## Related Pages
- [[NYISO]]
- [[CAISO]]
