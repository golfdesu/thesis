---
type: dataset
name: "Darts Time Series Collection"
location: "Multi-domain (8 series)"
resolution: "varies per series"
access: "open (https://github.com/unit8/darts)"
---

# Darts Time Series Collection

8 univariate series with seasonalities and additive+multiplicative trends (Herzen et al. 2022 [HLP+22]): AirPassengers, AusBeer, GasRateCO2, MonthlyMilk, Sunspots, Wine, Wooly, HeartRate.

## Literature Usage
- [[2024_TimesFM_Decoder_Only_Foundation_Model]] — Zero-shot evaluation (Table 3): TimesFM GM 0.5767 / AM 0.6829, within significance of best (ARIMA 0.5219 GM, LLMTime 0.4882 GM) on n=8; wide CIs.
