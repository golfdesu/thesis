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
---

# 📁 UrbanEV Dataset

## 🔗 Access Links & Repositories
- **Source publication**: Li H, Qu H, Tan X, You L, Zhu R, Fan W. "UrbanEV: an open benchmark dataset for urban electric vehicle charging demand prediction." *Scientific Data* 12(1):523, 2025.
- **Project GitHub repository** (per [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]], ref. [54]).
- **Access**: "Data will be made available **on request**" per the citing papers' data-availability statements — reproducibility depends on author contact.

## Overview

The **UrbanEV dataset** is a large-scale open benchmark for urban EV charging demand prediction covering the city of **Shenzhen, China**, aggregated to **traffic analysis zones** rather than individual stations. It pairs charging **occupancy** (proxy for demand) with **electricity pricing**, enabling spatio-temporal *and* economic (price-elasticity) modeling.

## Key Statistics

| Attribute | Value |
|-----------|-------|
| Charging stations | >18,000 public stations |
| Traffic analysis zones | 275 total; 247-zone subset used for graph modeling |
| Graph structure | 247 nodes / 1006 edges (inter-zone connectivity from Shenzhen's Sixth Residential Travel Survey) |
| Resolution | 5-minute interval (occupancy & price); hourly variants used by some papers |
| Period | e.g. 30 days Jun 19 – Jul 18 2022 ([[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]]); hourly Sep 1 2022 – Feb 28 2023 ([[2026_Wang_Xu_Similar_Day_Selection_EV_Load]]) |
| Pricing regime | 57/247 zones dynamic pricing, rest fixed rates |
| Access | On request |

## Available Features

- Zone-level charging occupancy time series (5-min / hourly)
- Electricity price per zone (dynamic vs fixed tariff)
- Weather variables (temperature, station/sea-level pressure, humidity, rainfall intensity, dew point)
- Calendar/contextual indicators (weekend/workday/holiday)
- POI functional shares per zone (→ Shannon functional entropy)
- Inter-zone connectivity graph

## 📚 Used By

- [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] — TriCast tri-modal forecasting on the 247-zone graph, 5-min resolution, 60/20/20 chronological split.
- [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] — Hourly day-ahead similar-day selection across zones with ShapeDTW/Multi-DTW similarity and NSGA-II weights.
- [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] — Spatio-temporal LLM benchmark on Shenzhen charging volumes.
- [[2025_Tian_MSSTGAN_City_EV_Load]] — Citywide EV charging demand GAN baseline context (UrbanEV benchmark lineage).

## Related Pages

- [[Shenzhen_ST_EVCDP]]
- [[Palo_Alto_EV]]
- [[Electricity_Tariff]]
- [[Spatial_Temporal_Forecasting]]
