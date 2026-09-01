---
type: dataset
title: "Weather Time-Series Dataset"
name: "Weather Time-Series Dataset"
location: "Weather Station, Max Planck Institute for Biogeochemistry, Jena, Germany"
resolution: "10 minutes"
access: "open (hosted in zhouhaoyi/ETDataset)"
license: "No formal license on benchmark redistribution (Max Planck Jena station data via Autoformer/Informer mirrors)"
commercial_use: unknown
tags: [dataset, ltsf-benchmark]
---

# Weather Time-Series Dataset

Standard long-horizon forecasting benchmark: **21 meteorological measurements** (temperature, humidity, pressure, wind speed/direction, etc.) recorded every **10 minutes** at the Max Planck Biogeochemistry Institute weather station in Jena, Germany (the 2020 annual slice used by the Informer/Autoformer lineage; the full Jena Climate record goes back to 2009). 52,696 timesteps; standard 7/1/2 train/val/test split with horizons {96, 192, 336, 720}.

Note: distinct from the older 14-feature Jena Climate Keras variant.

- **Reference**: [https://github.com/zhouhaoyi/ETDataset](https://github.com/zhouhaoyi/ETDataset)

## Literature Usage
- [[2025_Liu_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — TSLib Weather zero-shot; Sundial-S 0.233/0.271 competitive (Timer-XL 0.256/0.294).
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Pretraining ingredient: 10-min Weather (42 variates, 2.2M points) from Informer benchmark [ZZP+21].
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — Weatherbench 225280 series etc. (Table 6) in Chronos-2 real-univariate mix.
