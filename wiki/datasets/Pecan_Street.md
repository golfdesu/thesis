---
dataset: Pecan Street Dataport
source: Pecan Street Inc. (University of Texas at Austin)
location: Austin, Texas, USA
charger_type: Residential Level 1 & Level 2
sessions: "~25 million data points (ongoing)"
time_period: "2012–present"
resolution: "1-minute and 15-minute"
last_updated: 2026-08-02
url: "https://www.pecanstreet.org/dataport/"
tags: [dataset, residential-charging, smart-meter, USA, pecan-street]
name: "Pecan Street Dataport"
access: "academic/paid license via Dataport registration"
license: "Proprietary Dataport Data License Agreement (academic free tier / paid commercial); no resale, no sub-license"
commercial_use: prohibited
---

# 📁 Pecan Street Dataport

## 🔗 Access Links & Repositories
- **Pecan Street Dataport**: [Pecan Street Official Portal](https://www.pecanstreet.org/dataport/)

## Overview

The **Pecan Street Dataport** is a large-scale residential energy dataset from **Pecan Street Inc.** (affiliated with University of Texas at Austin). It includes high-resolution smart meter data, home EV charging profiles, solar PV generation, and appliance-level disaggregation for hundreds of homes in Austin, Texas. One of the most comprehensive public residential EV charging datasets available.

## Key Statistics

| Attribute | Value |
|-----------|-------|
| Location | Austin, Texas, USA (primary); New York, California (secondary) |
| Participants | ~1,000 homes (Austin), smaller cohorts in other cities |
| Homes with EVs | ~160 EV-equipped homes with 12+ years of charging records |
| Charger Type | Residential Level 1 (1.4 kW) and Level 2 (6.6 kW) |
| Temporal Resolution | 1-minute and 15-minute intervals; circuit-level data up to 1-second for a subset |
| Data Period | 2012–present (ongoing collection) |
| Features | Smart meter, EV charging, solar PV, appliance-level |
| Access | Academic license via Pecan Street website |

## Available Features

- Per-minute EV charging power draw (kW) — disaggregated from whole-home load
- Solar PV generation (kW)
- Whole-home electricity consumption (kW)
- Appliance-level subcircuit data (HVAC, EV charger, etc.)
- Outdoor temperature (linked weather data)
- Session-level derived features: arrival time, departure time, energy consumed

## Unique Advantages

- **High temporal resolution**: 1-minute granularity (up to 1-second circuit-level for a subset) enables short-term forecasting research.
- **Long time series**: Multi-year records allow seasonal and annual trend analysis.
- **Multi-energy context**: EV load in context of solar, HVAC, and household demand.
- **Socioeconomic diversity**: Homes across different income levels and building types.

## Limitations

- **Residential only**: Behavior patterns differ significantly from public/workplace charging.
- **Access requires academic license**: Not fully open access.
- **Selection bias**: Early adopters tend to have higher income and environmental awareness.
- **No vehicle-level SOC**: Charging behavior inferred from power draw, not direct SOC measurement.

## Papers Using This Dataset

| Paper | How Used |
|-------|----------|
| [[2024_Divide_Conquer_Transformer_EV]] | Smart-meter EV charging event prediction minutes ahead (DCT-EV) |
| [[2024_EV_Load_Forecasting_DAM]] | Included in multi-dataset DAM benchmark evaluation |

## Related Pages

- [[Caltech_ACN]]
- [[Boulder_Colorado]]
- [[ElaadNL]]
- [[Historical_Load]]
- [[State_of_Charge]]
