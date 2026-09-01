---
type: dataset
name: FEDQR Feature-Enhanced EV Charging Station Dataset
location: Regional EV Charging Stations (China)
resolution: 15-minute / hourly station-level demand
access: on-request
data_type: Multi-station hourly/15-min EV charging demand with meteorological priors
code_url: "https://github.com/Kenny4everlucky/FEDQR_dataset"
tags:
  - dataset
  - ev-charging
  - feature-enhanced
  - probabilistic-forecasting
---

# 📁 FEDQR Feature-Enhanced EV Charging Station Dataset

## 📊 Overview
Dataset introduced in Applied Energy (2024) for probabilistic EV charging demand forecasting using feature-enhanced deep quantile regression (FEDQR). Incorporates Pearson correlation prior reweighting across temporal and meteorological features.

## 🔗 Access Links
- **GitHub Repository**: [https://github.com/Kenny4everlucky/FEDQR_dataset](https://github.com/Kenny4everlucky/FEDQR_dataset) — data shared on request via the authors' repo (no direct download DOI).

## Key Features Provided
- Station-level EV load time series.
- Ambient temperature, humidity, and weather conditions.
- Calendar indicators and day-of-week feature encodings.

## 📚 Used By
- [[2024_Feature_Enhanced_Probabilistic_EV_Load]] — FEDM/GLU-DeepTCN probabilistic forecasting with Pearson-prior feature enhancement (source paper for the dataset).
