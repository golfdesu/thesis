---
type: dataset
name: UrbanEV Dataset
location: Shenzhen, Guangdong Province, China
resolution: 5-minute occupancy & electricity price (hourly variants derived in papers)
access: on request
data_type: Urban-scale EV charging demand benchmark (occupancy + pricing per traffic zone)
source_publication: "[[UrbanEV_Dataset]] Li et al., Scientific Data 12:523 (2025)"
tags:
  - dataset
  - ev-charging
  - shenzhen
  - urban-benchmark
  - traffic-zones
license: "CC0 1.0 (GitHub + Dryad doi:10.5061/dryad.np5hqc04z)"
commercial_use: allowed
---

# 📁 UrbanEV Dataset

## 🔗 Access Links & Repositories
- **Source publication**: Li H, Qu H, Tan X, You L, Zhu R, Fan W. "UrbanEV: an open benchmark dataset for urban electric vehicle charging demand prediction." *Scientific Data* 12(1):523, 2025.
- **GitHub**: https://github.com/IntelligentSystemsLab/UrbanEV
- **Dryad**: https://doi.org/10.5061/dryad.np5hqc04z (CC0 1.0)
- **Access note**: fully open (CC0). Older citing papers said "on request" only because they predate the 2025 public release.

## Overview

The **UrbanEV dataset** is a large-scale open benchmark for urban EV charging demand prediction covering the city of **Shenzhen, China**, aggregated to **traffic analysis zones** rather than individual stations. It pairs charging **occupancy** (proxy for demand) with **electricity pricing**, enabling spatio-temporal *and* economic (price-elasticity) modeling.

## Key Statistics

| Attribute | Value |
|-----------|-------|
| Charging stations | 1,682 stations / 24,798 piles raw; preprocessed: 1,362 stations / 17,532 piles across 275 traffic zones |
| Traffic analysis zones | 275 total; 247-zone subset used for graph modeling |
| Graph structure | 247 nodes / 1006 edges (inter-zone connectivity from Shenzhen's Sixth Residential Travel Survey) |
| Resolution | 5-minute interval (occupancy & price); hourly variants used by some papers |
| Period | 1 Sep 2022 – 28 Feb 2023 (six months; hourly zone-level, 5-min station-level) |
| Pricing regime | 57/247 zones dynamic pricing, rest fixed rates |
| Access | Open (CC0 1.0 via Dryad + Google Drive) |

## Available Features

- Zone-level charging occupancy time series (5-min / hourly)
- Electricity price per zone (dynamic vs fixed tariff)
- Weather variables (temperature, station/sea-level pressure, humidity, rainfall intensity, dew point)
- Calendar/contextual indicators (weekend/workday/holiday)
- POI functional shares per zone (→ Shannon functional entropy)
- Inter-zone connectivity graph

## 📚 Used By

- [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] — TriCast tri-modal forecasting, 5-min resolution, 60/20/20 chronological split. Note: uses the earlier [[Shenzhen_ST_EVCDP]] release (247 zones / 1006 edges, 19 Jun – 18 Jul 2022), not the six-month UrbanEV corpus.
- [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] — Hourly day-ahead similar-day selection across zones with ShapeDTW/Multi-DTW similarity and NSGA-II weights.
- [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] — Spatio-temporal LLM benchmark on Shenzhen charging volumes.
- [[2025_Tian_MSSTGAN_City_EV_Load]] — Citywide EV charging demand GAN baseline context (UrbanEV benchmark lineage).

## Related Pages

- [[Shenzhen_ST_EVCDP]]
- [[Palo_Alto_EV]]
- [[Electricity_Tariff]]
- [[Spatial_Temporal_Forecasting]]
