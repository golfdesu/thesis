---
type: dataset
name: "Electricity (ECL) Dataset"
category: Stub (auto-generated)
status: needs-review
tags:
  - dataset
  - electricity_ecl
---

## Overview
UCI Electricity Load Diagrams / Electricity Consumption Label (ECL): hourly electricity consumption of 321 clients from 2012–2014, a standard long-term forecasting benchmark.

access: open
resolution: hourly

## Usage in EV / Load Forecasting
Standard benchmark in LTSF papers ([[Informer]], [[Autoformer]], [[PatchTST]], [[DLinear]], [[TimesNet]]) alongside [[ETT]] and [[Weather]].

## Literature Usage
- [[2025_Liu_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — TSLib ECL (hourly, 321 clients) zero-shot; Sundial-L 0.166/0.262 vs Timer-XL 0.174/0.278, Chronos-L 0.204/0.273.
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — 370 series (Table 6) in Chronos-2 real-univariate pretraining mix (Electricity).
