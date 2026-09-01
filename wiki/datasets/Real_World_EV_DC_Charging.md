---
type: dataset
name: Real-World EV Direct Current (DC) Fast Charging Profiles
location: United Kingdom & Germany (public DC fast charging networks)
resolution: Session-level charging power curves (high-frequency within-session samples)
access: code & pretrained models open (Zenodo); charging-session data by request from authors
data_type: Session-level DC fast charging curves & durations
url: "https://doi.org/10.5281/zenodo.17183022"
code_url: "https://github.com/acse-sl420/ev_charging_ml"
status: metadata-verified-2026-08
tags:
  - dataset
  - ev-charging
  - dc-fast-charging
  - nature-2025
---

# 📁 Real-World EV DC Fast Charging Profiles & Durations

## 📊 Overview
A comprehensive dataset of 909,135 real-world EV DC fast charging sessions collected across public networks in the UK and Germany, analyzed in Nature Communications (2025). Used to train and evaluate Temporal Fusion Transformer (TFT) models predicting high-power DC charging power curves.

## 🔗 Access Links
- **Zenodo Repositories**: [Zenodo 17183022](https://doi.org/10.5281/zenodo.17183022) | [Zenodo 17183746](https://doi.org/10.5281/zenodo.17183746)
- **GitHub Repository**: [acse-sl420/ev_charging_ml](https://github.com/acse-sl420/ev_charging_ml)

## Key Features Provided
- Session start time & initial State of Charge (SOC).
- High-power DC fast charging rate (kW) profiles over time.
- Duration of fast charging sessions and disconnect timestamps.

## 📚 Used By
- [[2025_DC_Charging_Profiles_TFT]] — TFT + beta-VAE forecasting of DC charging power curves, duration, and relative accuracy.
- [[2026_Mamba_KAN_HyKANet_EV]] — cited as a real-world EV charging benchmark for demand prediction (per aggregation pass).
