---
type: paper
title: "Data-Driven Long-Term Learning Model for EV Charging Load Prediction"
authors: [Bushra Weqar, Ahteshamul Haque, Shabana Mehfuz, Azra Malik]
year: 2025
journal_conference: "2025 IEEE DELCON - International Conference on Recent Smart Technologies in Engineering for Sustainable Development"
doi_url: "https://doi.org/10.1109/DELCON68055.2025.11400364"
models_used: ["[[LTLM]]", "[[LSTM]]"]
datasets_used: ["[[LA_Charging_Station_Dataset]]"]
features_used: ["[[Historical_Load]]", "[[Daily_Weekly_Cycles]]", "[[Seasonal_Trends]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: []
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Data-Driven Long-Term Learning Model for EV Charging Load Prediction

## 🎯 Main Objective & Contribution
- **Problem**: EV charging station (EVCS) load forecasting has focused on short-term horizons (30 min–24 h); long-term load forecasting (LTLF, 1–10 years) and medium-term (MTLF, 1 day–1 year) are needed for infrastructure planning, substation/circuit sizing, renewable integration, maintenance cycles, and investment decisions. Statistical/non-learning models fail under nonlinearity, rapid EV adoption growth, price volatility, and renewable integration.
- **Contribution**: A **[[LTLM]] (Long-Term Load Memory)** framework built on [[LSTM]] networks that captures both short-term fluctuations (daily/weekly cycles) and long-term trends (monthly/seasonal variation, sectoral growth) in EVCS demand over extended horizons.
- Also provides structured taxonomies: comparison of ANN-based learning methods (FNN/ANN, RBFNN, hybrid ANN+fuzzy/wavelet) and deep-learning limitations (RNN vanishing gradients, CNN locality-only, ARIMA/SARIMA linearity assumption, GRU less expressive than LSTM for very long sequences).

## 🧠 Methodology & Model Architecture
- **No explicit mathematical equations are presented in the paper**; the LTLM model is described architecturally:
  - Pipeline (Fig. 5): historical EV data → processing → memory cell (LTLM) → prediction layer → long-term load forecast.
  - LSTM gating mechanisms (input/forget/output gates + memory cell) retain historical information over long horizons to learn weekly/monthly/seasonal patterns — cited to Hochreiter & Schmidhuber [34].
  - Motivated capabilities: long-term dependency capture, nonlinear relationship modeling (user behavior, traffic, weather, renewables), robustness to noisy/volatile data with spikes, joint short+long-term pattern learning, adaptive re-training.
- **Training setup**: batch size tested at 16/32/64 (lower batches fit better but cost more resources/time); max 150 epochs with early stopping — convergence typically by epochs 27–31.
- **Forecast protocol**: 12H sample interval; lookback = 400 time units (200 days); next-horizon forecast = 200 time units (100 days ahead).

## 📊 Dataset & Input Features
- **[[LA_Charging_Station_Dataset]]** — described only as "a publicly accessible dataset which records actual EV charging patterns and behaviour in a variety of locations":
  - Real data from **1 local charging station in Los Angeles, USA**, spanning ~6 months, plus synthetic data based on local US charging stations.
  - Real data **extrapolated to 1000 days** to create long-term series; trained on 6-month epochs, forecasting a 3-month period.
  - Sampling resolution: **12-hour** intervals; univariate load in kW.
- No station count/session count, DOI, URL, GitHub link, or formal data availability statement is given anywhere in the text.
- Features: historical charging load only; weather/climatic influence, traffic intensity, and vacation effects acknowledged as future additions, not included.

## 📈 Performance & Results
- **Qualitative only** — no numerical error metrics (MAE/RMSE/etc.) are reported anywhere in the paper.
- Next-horizon forecast (Fig. 7): 100-day prediction from a 200-day lookback follows the actual trend closely.
- Actual vs predicted (Fig. 8): predicted curve tracks trend and typical values accurately but **flattens peak loads** — attributed to averaging over long periods, biasing corrections, and omitted exogenous factors.
- Model judged accurate for short-term data forecasting; less well-fitted for long-term value precision while remaining stable and spike-aware.
- Claimed operational benefits of LTLM: grid management/load balancing, dynamic pricing & scheduling, infrastructure siting/sizing, renewable-alignment of charging, and maintenance planning.

## 💡 Limitations & Identified Research Gaps
- Peak underestimation/flattening due to long-period averaging — a core accuracy deficit for capacity-planning use cases.
- Single-station, partially synthetic, extrapolated dataset (~6 months real stretched to 1000 days) — weak evidence base for genuine multi-year LTLF claims.
- No quantitative benchmarking against baselines (ARIMA, GRU, SVR, Transformer), no reported error metrics, and no ablations.
- Exogenous drivers absent: weather (cloudy/rainy/stormy/clear), vacations/usage patterns deferred to future work.
- Authors' own improvement roadmap: hyperparameter tuning (epochs, batch size, lr, dropout), GRU/Transformer alternatives, recursive multi-step forecasting, hybrid LSTM+ARIMA, continuous re-training via real-time API service.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{weqar2025datadriven,
  author    = {Weqar, Bushra and Haque, Ahteshamul and Mehfuz, Shabana and Malik, Azra},
  title     = {Data-Driven Long-Term Learning Model for {EV} Charging Load Prediction},
  booktitle = {2025 IEEE DELCON - International Conference on Recent Smart Technologies in Engineering for Sustainable Development},
  year      = {2025},
  doi       = {10.1109/DELCON68055.2025.11400364}
}
```

## 🔗 Key References & Citation Graph
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM foundation [34]
- Related vault papers on long/multi-month EV horizon forecasting: [[2025_Hussain_Hybrid_LSTM_Transformer_Demand]] (120/240-day ACN forecasts), [[2024_Ali_MQ_TCN_Transfer_Learning_EV]], [[2015_Raza_Review_AI_Load_Demand]] (STLF/MTLF/LTLF taxonomy context)
- Hybrid spatial-temporal deep learning precedent cited [17]: related to [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]]
