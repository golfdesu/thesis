---
type: dataset
name: Norway Hourly EV Charging Load Dataset
location: Large residential area, Norway
resolution: 1 hour
access: open
data_type: Hourly aggregated residential EV charging load with weather & traffic covariates
code_url: "https://github.com/shivkumarjadon6/Hourly_EV"
tags:
  - dataset
  - ev-charging
  - hourly-ev
  - time-series
---

# 📁 Norway Hourly EV Charging Load Dataset

> [!INFO] Canonical vault page for this dataset. Also referenced as `Hourly_EV_Load` and "Norway_Residential_EV_Charging_Dataset" — do not create duplicate pages.

## 📊 Overview
Hourly aggregated real-world EV charging load from a **large residential area in Norway**, released as the data companion of Liu et al. (2026). Station/session counts are not disclosed; only a GitHub mirror is provided. The paper pairs the load series with **14 external features**: 9 daily weather variables (T_max/T_min/T_mean, W_max/W_mean, precipitation, humidity, sunshine index, snowfall) and 5 hourly traffic-density features from zones surrounding the station.

## 🔗 Access Links
- **GitHub Repository (data availability statement)**: [shivkumarjadon6/Hourly_EV](https://github.com/shivkumarjadon6/Hourly_EV)
- Paper DOI: [10.1038/s41598-026-38562-z](https://doi.org/10.1038/s41598-026-38562-z)

## Key Features Provided
- Hourly charging load sequence (24 h history → 24/48/72/96 h forecasts).
- Daily weather features; hourly zonal traffic density Z1–Z5.
- Strongest correlations: sunshine index −0.239, mean humidity +0.131.

## 📚 Used By
- [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] — Multi-scale Fusion Transformer (3M scale masks + FAM/MFM feature fusion) benchmark vs Transformer/BiLSTM/LSTM/GRU at 24–96 h horizons.
