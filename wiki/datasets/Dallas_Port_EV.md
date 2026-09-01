---
type: dataset
name: "Dallas Port EV Logistics Charging Dataset"
location: "Dallas, Texas, USA (artificial port logistics fleet)"
resolution: "1 hour"
access: "open"
data_type: "Hourly EV port-fleet charging load (kW) with fleet/infrastructure/weather/economic covariates"
status: needs-review # Kaggle DOI https://doi.org/10.34740/KAGGLE/DSV/9490653 returns 404 (checked 2026-08-26)
tags: [dataset, ev-charging]
---

# Dallas Port EV Logistics Charging Dataset

## 📊 Overview
EV intelligent port-logistics charging dataset for Dallas, Texas: **65,736 hourly data points** covering January 2017 – June 2024 (abstract states Jan 2020 – Jun 2024). Target is hourly EV fleet charging load (kW), deliberately imbalanced toward peak-hour usage to mirror real port operations. Features span calendar, fleet (size, vehicle types, battery capacity), infrastructure (# stations, power rating), operations (distance driven, loading times), environment (temperature, humidity, precipitation), grid/economics (electricity cost, incentives), and usage-class labels.

## 🔗 Access Links
- **Kaggle DOI**: https://doi.org/10.34740/KAGGLE/DSV/9490653

## 📚 Used By
- [[2025_Alghamdi_REST_Network_Port_EV]] — RESTNet ensemble (ResNet+SENet+Transformer) with PSS balancing and DSRS feature selection; MAPE 6.5%, RMSE 9.8 kW.
