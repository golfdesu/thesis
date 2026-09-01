---
type: dataset
title: "Influenza-like Illness Dataset"
name: "Influenza-like Illness Dataset"
location: "United States (CDC ILINet surveillance)"
resolution: "weekly"
access: "open (CDC FluView)"
license: "US CDC FluView - US Government work, public domain"
commercial_use: allowed
data_type: "Weekly % of outpatient visits for influenza-like illness (national + HHS regions)"
tags: [dataset, ltsf-benchmark]
---

# Influenza-like Illness Dataset

Long-horizon forecasting benchmark derived from the **US CDC ILINet** (Influenza-like Illness Surveillance Network): weekly percentage of outpatient visits for influenza-like illness, national + regional levels. The benchmark slice covers roughly weekly observations from 2002–2021 (~966 timesteps × 7 features), with horizons {24, 36, 48, 60} weeks.

- **Reference**: [https://github.com/zhouhaoyi/ETDataset](https://github.com/zhouhaoyi/ETDataset)
- **Source surveillance**: CDC FluView / ILINet — https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html
