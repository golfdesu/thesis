---
type: dataset
name: "Shenzhen ST-EVCDP Charging Pile Dataset"
location: "Shenzhen, China"
resolution: "5 minutes"
access: "open"
tags: [dataset, ev-charging]
license: "MIT License (IntelligentSystemsLab/ST-EVCDP GitHub)"
commercial_use: allowed
---

# Shenzhen ST-EVCDP Charging Pile Dataset

## 📊 Overview
City-scale public EV charging demand dataset from the ST-EVCDP release (Intelligent Systems Lab). Real-time pile availability was scraped from a public mobile app covering **18,061 public charging piles in Shenzhen**, aggregated to **247 traffic zones** (per the 6th Residential Travel Survey of Shenzhen; graph = 247 nodes / 1006 edges). Period: **19 June – 18 July 2022 (30 days, 8,640 timestamps at 5-min resolution)**. Targets: per-zone pile occupancy demand and charging price (57 zones time-of-use priced, rest fixed). Train/val/test = 6:2:2 chronological.

## 🔗 Access Links
- **GitHub (code + data)**: https://github.com/IntelligentSystemsLab/ST-EVCDP

## 📚 Used By
- [[2024_Qu_Physics_Informed_GAT_EV_Load]] — Physics-informed attention graph (PAG) regional demand prediction with price-elasticity priors.
- [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] — Listed as Shenzhen EV charging data source for spatio-temporal LLM forecasting.
- 2026 — [[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]] : EVformer spatio-temporal decoupled Transformer on the 247-zone graph (7:1:2 split, T=12 @ 5-min input, τ=3/6/9-step horizons); best MAE/RMSE/MAPE at all horizons vs 13 baselines.

> [!note] TriCast provenance
> [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] (TriCast) evaluates on what is effectively this same Shenzhen release (247 zones / 1006 edges / 19 Jun–18 Jul 2022 / 18k+ piles) but catalogs it under [[UrbanEV_Dataset]]; see that page for its entry.
