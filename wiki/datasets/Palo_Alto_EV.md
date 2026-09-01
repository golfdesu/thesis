---
type: dataset
name: City of Palo Alto EV Charging Station Usage Dataset
location: Palo Alto, California, USA
resolution: Session-level (start/end timestamps, kWh); hourly aggregates derived in papers
access: open
data_type: Session-level public EV charging station usage records (July 2011 - Dec 2020+)
urls:
  - https://data.cityofpaloalto.org/datasets/194693/electric-vehicle-charging-station-usage-july-2011-dec-2020/
  - https://data.cityofpaloalto.org/dataviews/241685/ELECT-VEHIC-CHARG-STATI-USAGE-JULY/
tags:
  - dataset
  - ev-charging
  - palo-alto
  - open-data
  - public-ev-charging
status: needs-review # legacy data.cityofpaloalto.org dataview URL dead; portal moved to data.paloalto.gov (checked 2026-08-26)
license: "City of Palo Alto Open Data portal (open government data)"
commercial_use: allowed
---

# 📁 City of Palo Alto EV Charging Station Usage Dataset

## Overview
The **Palo Alto EV Dataset** is a widely used benchmark dataset provided by the City of Palo Alto Open Data Portal. It contains detailed transaction records of public EV charging station usage across Palo Alto, California from July 2011 to December 2020 (and updated continuously).

## 🔗 Access Links & Open Data Portals
- **City Data Portal (verified 2026-08-23)**: [Electric Vehicle Charging Station Usage (July 2011 - Dec 2020)](https://data.cityofpaloalto.org/datasets/194693/electric-vehicle-charging-station-usage-july-2011-dec-2020/)
- **Data View API**: [Palo Alto EV Dataview API](https://data.cityofpaloalto.org/dataviews/241685/ELECT-VEHIC-CHARG-STATI-USAGE-JULY/)
- **Kaggle mirror (used by DiffPLF)**: [EV Charging Station Usage of California City](https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-usage-of-california-city)

## Key Features Provided
- `Station Name` & `Address`: Geographical location of public charging stations.
- `Start Time` & `End Time`: Plug-in and plug-out timestamps.
- `Total Duration (hh:mm:ss)` & `Charging Time`: Connection duration vs active charging duration.
- `Energy (kWh)`: Total electricity consumed per session.
- `Port Type` & `Plugin Category`: Level 2 / DC Fast Charger types.

## Literature References (Papers in Vault Using Palo Alto Dataset)
- `[[2023_MetaProbformer_EV_Load]]` - Huang et al. (2023): Used Palo Alto dataset for few-shot meta-learning (Reptile + Informer).
- `[[2024_DiffPLF_Conditional_Diffusion_EV]]` - Li et al. (2024): Used Palo Alto dataset with Meteostat weather data for conditional diffusion probabilistic forecasting (DiffPLF).
- `[[2024_EV_Load_Forecasting_DAM]]` - Bampos et al. (2024): Benchmark on Palo Alto EV dataset for Day-Ahead Market (DAM) participation.
- `[[2025_MSSTGAN_City_EV_Load]]` - Tian et al. (2025): Multi-Scale Spatial-Temporal Graph Attention Network benchmarked on Palo Alto, Boulder, Dundee, and Perth.
- `[[2026_Decomposition_Stacked_Meta_Learning_EV_Load]]` - Ullah et al. (2026): Benchmark on ACN, Palo Alto, Perth, and Paris (Belib) datasets.
- `[[2026_TFT_Conformal_Environmental_EV_Load]]` - Moghadam Dost et al. (2026): TFT + CQR conformal calibration with Open-Meteo environmental covariates on 2018–2022 hourly data (RMSE 1.2687 kWh, PICP 96.2%).
- `[[2026_MetaLearning_Informer_Probabilistic_EV]]` - Singh et al. (2026): MAML-Informer point + probabilistic benchmark (39,915 records; best RMSE50 0.168, CRPS 1.012).
- `[[2026_ML_Geographical_Transferability_EV]]` - Wang et al. (2026): Palo Alto one of 12 cities in the six-model ML/DL transferability benchmark (7 stations, 17.9 events/day/station).
- `[[2026_DualDirection_Transformer_EV_Charging]]` - Zhang et al. (2026): USDT probabilistic dual-direction transformer on ~5 months / 3114 hourly points (PALO).
- `[[2026_ML_Comparison_EV_Charging_Forecasting]]` - Kyriakopoulos & Theodoridis (2026): Palo Alto one of four cities (47 stations, 259,415 sessions, Jul 2011–Dec 2020); Transformer best at region/city short- and mid-term (city MAE 12.84→12.77), XGBoost best at station level.
- `[[2026_INLA_Spatio_Temporal_EV_Demand]]` - Bouaachra et al. (2026): names Palo Alto a **stale legacy benchmark** (2020-era) that fails to reflect the scale and behavioral diversity of modern charging networks; proposes [[ChargePlace_Scotland]] (Oct 2022–Apr 2025) as the modern open replacement.
