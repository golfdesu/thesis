---
type: dataset
name: "Google Trends Time Series"
location: "Global (Google Search queries)"
resolution: "hourly / daily / weekly / monthly"
access: "open (https://trends.google.com)"
---

# Google Trends Time Series

Search-interest time series for ~22k head queries (Jan 2007-Dec 2021 daily/weekly/monthly; Jan 2018-Dec 2019 hourly), ~0.5B points. Differentially private, >50% sparsity filter. Used as pretraining ingredient in [[2024_TimesFM_Decoder_Only_Foundation_Model]] (TimesFM) and related foundation models.

## Literature Usage
- [[2024_TimesFM_Decoder_Only_Foundation_Model]] — Core pretraining source (hourly 393M, daily 123M, weekly 16.6M, monthly 3.8M points; Table 1).
