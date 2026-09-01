---
type: dataset
name: "Utrecht SmoothEMS Office Parking Lot EV Charging Data"
location: "Utrecht, Netherlands (a.s.r. office parking lot)"
resolution: "15 minutes (aggregated); raw session-level"
access: "open (4TU.ResearchData, CC BY-NC-SA)"
status: metadata-verified-2026-08
tags: [dataset, ev-charging]
---

# Utrecht SmoothEMS Office Parking Lot EV Charging Data

## 📊 Overview
EV charging demand measured at the **ASR office parking lot in Utrecht, Netherlands**, collected within the **SmoothEMS Met GridShield** project. 15-minute discretization; the underlying 4TU release covers ~300 charging points (Aug 2020 – Oct 2024), though the [[2025_Matrone_QR_LSTM_Attention_EV_Load]] paper itself does not disclose station/session counts. Used with [[2025_Matrone_QR_LSTM_Attention_EV_Load]]'s protocol: 96 input steps (= previous full day) → next-day forecast on a rolling horizon refreshed hourly; 80/20 train/test split. Companion weather: KNMI daily meteorological data.

## 🔗 Access Links
- **4TU.ResearchData (public)**: [Electric Vehicle Charging Session Data of Large Office Parking Lot](https://doi.org/10.4121/80ef3824-3f5d-4e45-8794-3b8791efbd13) — session-level records collected **25 Aug 2020 – 2 Oct 2024**; ~300 charging points installed at the a.s.r. living lab by end of the measurement period.
- **KNMI daily weather data**: https://www.knmi.nl/nederland-nu/klimatologie/daggegevens

## 📚 Used By
- [[2025_Matrone_QR_LSTM_Attention_EV_Load]] — QR-LSTM-Attention probabilistic day-ahead forecasting (q20/q50/q80); best CRPS 6.111, PICP 78.60%.
