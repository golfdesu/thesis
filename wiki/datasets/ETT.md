---
type: dataset
title: "Electricity Transformer Temperature Dataset"
name: "Electricity Transformer Temperature Dataset"
location: "Electricity transformer depots (Wenzhou & Chaoyang regions), China"
resolution: "15-min raw; hourly (ETTh1/h2) and 15-min (ETTm1/m2) variants"
access: "open (github.com/zhouhaoyi/ETDataset)"
license: "CC BY-ND 4.0 (zhouhaoyi/ETDataset LICENSE) - share verbatim w/ attribution; no modified redistribution"
commercial_use: allowed
data_type: "2 years of transformer oil temperature + 6 power-load features per station"
status: metadata-verified-2026-08
---

# Electricity Transformer Temperature Dataset

Multivariate transformer-temperature benchmark.

- **Reference**: [https://github.com/zhouhaoyi/ETDataset](https://github.com/zhouhaoyi/ETDataset)

## Literature Usage
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Evaluation (not pretraining): ETTh1/ETTh2/ETTm1/ETTm2 (2-year transformer temperature) horizons 96/192, last-window; TimesFM ZS avg MAE 0.36 vs PatchTST 0.37, Informer 0.99.
