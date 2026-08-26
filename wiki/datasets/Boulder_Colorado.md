---
dataset: Boulder Colorado EV Dataset
source: City of Boulder, Colorado (Open Data)
location: Boulder, Colorado, USA
charger_type: Public Level 2 AC
sessions: 20562
time_period: "2018–2021"
resolution: Session-level
last_updated: 2026-08-02
url: "https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0/explore"
tags: [dataset, public-charging, level-2, USA]
---

# 📁 Boulder Colorado EV Dataset

## 🔗 Access Links & Repositories
- **City of Boulder Open Data Portal**: [https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0/explore](https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0/explore)
- **Direct dataset link (verified 2026-08-23)**: [https://bouldercolorado.gov/open-data/electric-vehicle-charging-stations](https://bouldercolorado.gov/open-data/electric-vehicle-charging-stations)
- **Direct ArcGIS view**: [https://opendata.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0](https://opendata.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0)
- **Data Dictionary (CSV)**: [https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary.csv](https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary.csv)

## Overview

A public EV charging session dataset from **City of Boulder, Colorado** open data portal. Contains **20,562 EV charging transactions** from city-owned public Level 2 AC charging stations. Widely used as a benchmark for day-ahead and short-term EV load forecasting.

## Key Statistics

| Attribute | Value |
|-----------|-------|
| Total Sessions | 20,562 |
| Location | Boulder, Colorado, USA |
| Charger Type | Level 2 AC (public) |
| Data Period | 2018–2021 |
| Temporal Resolution | Session-level (start time, end time, energy delivered) |
| Access | Open data (City of Boulder portal) |

## Available Features

- Session start/end timestamps
- Energy delivered per session (kWh)
- Station ID and location
- Connector type
- User anonymized ID (in some versions)

## Limitations

- **No real-time power profiles**: Only session-level energy totals, not per-minute load curves.
- **Level 2 only**: Does not include DC fast charging behavior.
- **Missing SOC data**: No information on initial or final battery state of charge.
- **No vehicle type**: Cannot distinguish between BEV and PHEV.

## Papers Using This Dataset

| Paper | How Used |
|-------|----------|
| [[2020_Huang_Ensemble_EV_Load]] | Ensemble learning benchmark; 20,562 transactions 2018–2020 aggregated hourly |
| [[2023_Huang_MetaProbformer_EV_Load]] | One of four meta-learning benchmark stations (with Palo Alto, ElaadNL, Perth) |
| [[2023_Koohfar_Transformer_EV_Demand]] | Transformer-based demand prediction with NOAA weather covariates |
| [[2024_Bampos_EV_Load_Forecasting_DAM]] | 36-hour rolling DAM benchmark across 4 public datasets |
| [[2024_Helmy_Autoformer_EV_Charging]] | Autoformer-based charging-load forecasting on the direct open-data export |
| [[2025_Tian_MSSTGAN_City_EV_Load]] | MSSTGAN city-scale spatio-temporal benchmark (Boulder/Palo Alto/Dundee/Perth) |
| [[2025_Hussain_CAT_Former_Short_Term_EV]] | CAT-Former short-term forecasting with Boulder weather covariates |
| [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] | MAML-Informer benchmark (29,396 points): best RMSE50 0.202, CRPS 1.001, MPIW 0.1485 |
| [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] | Boulder one of 12 cities in the ML/DL transferability benchmark (19 stations, 5.5 events/day/station) |
| [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] | USDT probabilistic forecasting on 31 months / 22,632 hourly points |
| [[2023_Xiong_Combined_Deep_Learning_EV_Station_STLF]] | CNN-LSTM-Transformer STLF on the BOULDER/BASELINE ST1 station (2020, 15-min resolution); RMSE 0.300 / MAE 0.120 |
| [[2025_Zhou_MixerInformer_Transfer_Learning_New_EV_Stations]] | MIK-TST two-stage transfer learning: stations 0–20 as source domain, stations 21–25 as data-scarce targets; MAE 0.4450 (−4% vs PatchTST) |
| [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]] | One of four cities in the ML benchmark (27 stations, 24,081 sessions, Jan 2018–Mar 2021); Transformer best short-term and long-term, LSTM best city mid-term |

## Related Pages

- [[Caltech_ACN]]
- [[Pecan_Street]]
- [[ElaadNL]]
- [[Historical_Load]]
- [[Arrival_Departure_Time]]
