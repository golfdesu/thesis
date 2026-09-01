---
type: dataset
name: "Monash Time Series Forecasting Archive"
location: "Multi-domain (30 datasets)"
resolution: "minutes to yearly"
access: "open (https://github.com/rakshitha-god/MonashTSForecasting + https://huggingface.co/datasets/monash_tsf)"
---

# Monash Time Series Forecasting Archive

Collection of 30 datasets (Godahewa et al. 2021 [GBW+21]) spanning finance, demand, weather, traffic; minutes to yearly granularities. 18 without missing values used for evaluation in [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] (australian electricity demand, bitcoin, pedestrian counts, weather, nn5 daily/weekly, tourism yearly/quarterly/monthly, cif 2016, covid deaths, fred md, traffic hourly/weekly, saugeenday, us births, hospital, solar weekly).

## Literature Usage
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Primary zero-shot evaluation (18 datasets, naive-scaled MAE): TimesFM GM 0.6846 (best), >25% better than LLMTime (0.9715), within significance of N-BEATS (0.7005).
