---
type: dataset
name: CAISO Load Data (Today's Outlook)
location: California, USA
resolution: Hourly (5-min/10-min live views available)
access: open
data_type: TAC-area / zonal electricity demand for the California ISO
urls:
  - https://www.caiso.com/TodaysOutlook/Pages/default.aspx
tags:
  - dataset
  - power-systems
  - load-forecasting
  - open-data
---

# 📁 CAISO Load Data

## Overview
The California Independent System Operator publishes real-time and historical system/TAC-area demand through its **Today's Outlook** portal. The dataset covers 9 Transmission Access Charge (TAC) areas: PG&E, SCE, SDG&E, VEA, and smaller municipal utilities — California's major investor-owned utilities plus associated service territories.

## Key Features Provided
- Per-region hourly integrated load (MWh); 8,760 steps/year.
- Distinct duck-curve net-load signature (solar-driven) — high renewable-shaping of demand.

## 📚 Used By
- [[2026_Yu_EnergyMamba_Graph_Mamba_ASCQR]] — Year-2024 TAC-area load, 9 regions/zones, hourly, MWh; graph nodes from region centroids (EnergyMamba benchmark, hardest scale: MAE 199.18).

## Related Pages
- [[EIA-930]]
- [[NYISO]]
