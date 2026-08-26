---
type: dataset
name: "Utrecht SmoothEMS Office Parking Lot EV Charging Data"
location: "Utrecht, Netherlands (ASR office parking lot)"
resolution: "15 minutes"
access: "on-request"
tags: [dataset, ev-charging]
---

# Utrecht SmoothEMS Office Parking Lot EV Charging Data

## 📊 Overview
EV charging demand measured at the **ASR office parking lot in Utrecht, Netherlands**, collected within the **SmoothEMS Met GridShield** project. 15-minute discretization; station/session counts not disclosed in the paper. Used with [[2025_Matrone_QR_LSTM_Attention_EV_Load]]'s protocol: 96 input steps (= previous full day) → next-day forecast on a rolling horizon refreshed hourly; 80/20 train/test split. Companion weather: KNMI daily meteorological data.

## 🔗 Access Links
- Not publicly available as a download; obtained via the SmoothEMS Met GridShield project.
- **KNMI daily weather data**: https://www.knmi.nl/nederland-nu/klimatologie/daggegevens

## 📚 Used By
- [[2025_Matrone_QR_LSTM_Attention_EV_Load]] — QR-LSTM-Attention probabilistic day-ahead forecasting (q20/q50/q80); best CRPS 6.111, PICP 78.60%.
