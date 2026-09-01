---
type: dataset
name: "Electricity (ECL) Dataset"
category: Stub (auto-generated)
status: metadata-verified-2026-08
tags:
  - dataset
  - electricity_ecl
location: "Tennessee Valley Authority client footprint, USA (UCI archive)"
resolution: hourly
access: open
license: "CC BY 4.0 (UCI ML Repository, ElectricityLoadDiagrams20112014, doi:10.24432/C58C86)"
commercial_use: allowed
data_type: "Hourly kWh consumption of 321 clients, 2012-2014; standard LTSF benchmark"
---

## Overview
UCI Electricity Load Diagrams / Electricity Consumption Label (ECL): hourly electricity consumption of 321 clients from 2012–2014, a standard long-term forecasting benchmark.

access: open
resolution: hourly

## Usage in EV / Load Forecasting
Standard benchmark in LTSF papers ([[Informer]], [[Autoformer]], [[PatchTST]], [[DLinear]], [[TimesNet]]) alongside [[ETT]] and [[Weather]].

## Literature Usage
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Pretraining ingredient: hourly Electricity (321 clients, 8.4M points) — UCI ElectricityLoadDiagrams20112014.
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — 370 series (Table 6) in Chronos-2 real-univariate pretraining mix (Electricity).
