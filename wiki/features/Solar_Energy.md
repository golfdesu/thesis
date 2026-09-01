---
type: feature
name: "Solar Energy / Irradiance"
category: Stub (auto-generated)
status: needs-review
tags:
  - feature
  - solar_energy
---

## Overview
Solar radiation or photovoltaic generation covariate; exogenous driver in energy load forecasting benchmarks (e.g. [[Electricity_ECL]], LSTNet-era datasets).

| Property | Description |
|----------|-------------|
| Unit | W/m² or normalized PV output |
| Source | Weather stations, satellite reanalysis, or measured PV output |
| Related | [[Temperature]], [[Wind_Speed]], [[Weather_Traffic]] |

## Usage in EV / Load Forecasting
Used as an input feature in solar-aware and multi-energy forecasting models; rooftop PV output also shapes net-load profiles that EV charging adds to.

## References
- [[2019_LogSparse_Enhancing_Locality_Transformer]]
- [[2021_TimeGrad_Diffusion_Forecasting]]
