---
type: dataset
title: "Traffic Time-Series Dataset"
name: "Traffic Time-Series Dataset"
location: "San Francisco Bay Area (PeMS), California, USA"
resolution: "hourly (both variants: LTSF 862 sensors; DeepAR/LSTNet 963 sensors)"
access: "open"
license: "No formal license; Caltrans PeMS public road-sensor data (California state government)"
commercial_use: allowed
data_type: "Road occupancy rates from 862 freeway sensors; two community variants exist (862-sensor LTSF and PEM-SF)"
status: metadata-verified-2026-08
---

# Traffic Time-Series Dataset

Multivariate road-occupancy series used in forecasting benchmarks.

Two distinct benchmarks share this name:
- **PEM-SF Traffic** (this repo; used by DeepAR/TimeGrad): San Francisco Bay Area freeway occupancy from California PeMS, 963 sensors, hourly resolution.
- **LTSF Traffic** (Informer/Autoformer lineage): 862 sensors from California PeMS (SF Bay Area), hourly, 17,544 timesteps, horizons {96, 192, 336, 720}.

Check which variant a paper means before comparing numbers.

- **Reference**: [https://github.com/laiguokun/multivariate-time-series-data](https://github.com/laiguokun/multivariate-time-series-data)

## Literature Usage
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Pretraining ingredient: hourly Traffic (862 sensors, 15.1M points) and 15-min LibCity traffic (6,159 series, 34.3M) — San Francisco Bay Area PeMS.
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — Traffic-related datasets (Taxi 2428, LargeST 8196, Q-Traffic 45148) in Table 6 of Chronos-2 real-univariate mix.
