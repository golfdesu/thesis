---
type: dataset
name: Dundee City Council Public EV Charging Dataset
location: Dundee, Scotland, UK
resolution: Session-level transactions (30-min slot aggregation used in GCN-TRN)
access: open
data_type: Session-level public EV charging transactions
url: "https://data.dundeecity.gov.uk/"
tags:
  - dataset
  - ev-charging
  - dundee
  - open-data
  - uk-ev
---

# 📁 Dundee City Council Public EV Charging Dataset

## 🔗 Access Links & Repositories
- **Dundee Open Data Portal**: [Dundee City Council Open Data Portal](https://data.dundeecity.gov.uk/)
- **4-city preprocessed benchmark repo (Palo Alto/Boulder/Dundee/Perth)**: [github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand](https://github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand)

## Overview
Open dataset provided by Dundee City Council (Scotland, UK) covering extensive public EV charging infrastructure usage across the city of Dundee — one of the UK's densest public charging networks per capita. Session records include timestamps, energy delivered, and charge-point locations; [[2022_Zhang_GCN_TRN_EV_Availability]] aggregates connector occupancy into 30-minute slots for availability forecasting.

## 📚 Used By
- [[2022_Zhang_GCN_TRN_EV_Availability]] — GCN-TRN EV charging-station operating-status/availability prediction on 30-min slots.
- [[2025_Tian_MSSTGAN_City_EV_Load]] — Evaluated MS-STGAN on Dundee alongside Palo Alto, Boulder, and Perth.
- [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] — Dundee one of 12 cities in the ML/DL transferability benchmark (27 stations, 25.5 events/day/station).
- [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]] — One of four cities (67 stations, 52,752 sessions, Jan 2017–Dec 2018); Transformer dominates short-term region/city (city MAE 14.52→13.22) but collapses on sparse daily long-term data (city MAE ≈ 93) where GRU wins (21.48@5d).
