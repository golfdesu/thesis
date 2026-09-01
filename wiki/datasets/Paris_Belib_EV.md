---
type: dataset
name: Paris Belib Public EV Charging Network
location: Paris, France
resolution: Session-level / terminal status records (hourly aggregates derived in papers)
access: open
data_type: Real-time & historical public EV charging terminal usage
url: "https://opendata.paris.fr/explore/dataset/belib-points-de-recharge-pour-vehicules-electriques-donnees-statiques"
tags:
  - dataset
  - ev-charging
  - paris-belib
  - open-data
---

# 📁 Paris Belib Public EV Charging Network Dataset

## 📊 Overview
Open Data Paris public dataset containing transaction and status records of Paris's Belib public charging network — several hundred public terminals across the city with mixed power levels. Used for meta-learning and decomposition-based short-term EV load forecasting (Ullah et al., 2026).

## 🔗 Access Links
- **Paris Open Data Portal (static)**: [Belib' Points de Recharge — Données statiques](https://opendata.paris.fr/explore/dataset/belib-points-de-recharge-pour-vehicules-electriques-donnees-statiques)
- **Paris Open Data Portal (real-time availability)**: [Belib' — Disponibilité temps réel](https://opendata.paris.fr/explore/dataset/belib-points-de-recharge-pour-vehicules-electriques-disponibilite-temps-reel)

## Key Features Provided
- Terminal locations, power capacities (kW).
- Charging session durations and occupancy status over time.

## 📚 Used By
- [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] — STL decomposition + stacked meta-learning benchmark on Belib alongside ACN, Palo Alto, and Perth.
