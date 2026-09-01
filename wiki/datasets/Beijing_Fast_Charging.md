---
type: dataset
name: "Beijing Fast Charging Station Dataset"
location: "Beijing, China"
resolution: "15 minutes"
access: "private"
data_type: "DC fast-charging load power (kW), 10 stations, 15-min series"
tags: [dataset, ev-charging]
---

# Beijing Fast Charging Station Dataset

## 📊 Overview
Real-world DC fast-charging load from **10 fast charging stations in Beijing, China**, 25 Jan 2022 – 30 Apr 2022; power recorded every **15 min** (96 points/day/station); nearest inter-station distance 4.69 km. Split: last 63 days train / 18 days validation / remainder test. Covariates selected by maximal information coefficient (MIC ≥ 0.3): historical charging power, temperature, wind speed, humidity, electricity price (MIC(load, price) = 0.92). Missing values filled by linear interpolation.

## 🔗 Access Links
- Not publicly available — no URL/DOI given in the paper (described only as "charging load dataset from Beijing, China", Section IV-A).

## 📚 Used By
- [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] — STMGCN spatio-temporal multi-graph convolution forecasting (MAE 53.29 kW vs 10 baselines).
