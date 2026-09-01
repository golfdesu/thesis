---
type: dataset
name: "REFIT Smart-Meter Household Dataset"
location: "United Kingdom (20 households, Loughborough area)"
resolution: "1 minute (resampled from 6–8 s raw)"
access: "open"
tags: [dataset, ev-charging]
license: "CC BY 4.0 (Loughborough Univ. doi:10.17028/rd.lboro.2070091 + Strathclyde doi:10.15129/9ab14b0e)"
commercial_use: allowed
---

# REFIT Smart-Meter Household Dataset

## 📊 Overview
REFIT (Murray et al., *Scientific Data* 2017): electrical power consumption of **20 UK households over two years**, with appliance-level sub-metering. Raw sampling at 6–8 s; typical usage cleans records, forward-fills to 1 s and resamples to **1-min resolution**. Zhu et al. (2025) use April 2014 – April 2015 (13 months), 8 frequent appliance types (fridge, washing machine, dishwasher, microwave, kettle, TV site, computer site, dryer) with missing appliances zero-filled. Useful as a household-load proxy for EV-charger disaggregation and federated forecasting research.

## 🔗 Access Links
- Publicly available as the "REFIT smart-meter dataset" (Murray et al. 2017); DOI listed in the paper note of [[2025_Meyer_Benchmark_Foundation_Models]].

## 📚 Used By
- [[2025_Zhu_Personalized_Federated_Learning]] — PF-HoLo personalized federated learning under imbalanced household data (−13.41% MSE / −11.33% MAE vs FedAvg).
- [[2025_Meyer_Benchmark_Foundation_Models]] — Household electricity benchmark for time-series foundation models.
