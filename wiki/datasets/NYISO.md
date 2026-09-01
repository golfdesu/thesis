---
type: dataset
name: NYISO Zonal Load Data
location: New York State, USA
resolution: Hourly (5-min/1-h SCADA aggregates available)
access: open
data_type: Zonal system-level electricity load (SCADA), 11 zones
urls:
  - https://www.nyiso.com/load-data
tags:
  - dataset
  - power-systems
  - load-forecasting
  - open-data
---

# 📁 NYISO Load Data

## Overview
The New York Independent System Operator publishes zonal SCADA load data (11 load zones — distinct load pockets with similar electrical characteristics) via its open **Custom Reports / Load Data portal**. Hourly records are the standard granularity for market operations.

## Key Features Provided
- Per-zone hourly integrated load (MWh).
- ~4 years rolling history; 8,760 steps/year at hourly resolution.
- Zone-level aggregation aligns with transmission-level forecasting studies.

## 📚 Used By
- [[2026_Yu_EnergyMamba_Graph_Mamba_ASCQR]] — Year-2024 zonal load, 11 nodes/zones, hourly, MWh; one of four EnergyMamba benchmark datasets (graph built from zone centroid distances).

## Related Pages
- [[EIA-930]]
- [[CAISO]]
