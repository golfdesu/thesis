---
type: feature
name: Cyclical Trigonometric Encodings (Sin/Cos)
category: Feature Engineering / Time Encoding
tags:
  - feature
  - cyclical-encoding
  - sine-cosine
  - time-series
---

# 📊 Cyclical Trigonometric Encodings (Sin/Cos)

## Mathematical Formulation
To map cyclical periodic time variables (e.g., quarter-hour $t \in [0, N-1]$ or day of week $d \in [0, 6]$) into continuous 2D space where step $N-1$ is close to step $0$:
$$x_{\sin} = \sin\left(x \times 2\pi \times \frac{1}{N}\right), \quad x_{\cos} = \cos\left(x \times 2\pi \times \frac{1}{N}\right)$$

## Application in EV Charging Load Forecasting
- **Quarter-Hour Encoding ($N=96$)**: Maps 15-minute time intervals across 24 hours.
- **Day-of-Week Encoding ($N=7$)**: Maps weekly continuity (Sunday $d=6$ smoothly transitions to Monday $d=0$).

## Literature References
- [[2021_VanKriekinge_Day_Ahead_EV_Demand]] - Demonstrated that adding cyclical Sin/Cos encodings reduced day-ahead forecast MAE by 23.2% and RMSE by 19.22%.
- 2024 — [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] : Sine/cosine time encoding of transfer-learned MQ-TCN inputs alongside station-ID embeddings.
- 2024 — [[2024_Bampos_EV_Load_Forecasting_DAM]] : Cyclical time features (incl. week-of-year) in the XGBoost/MLP DAM forecasting pipeline.
- 2025 — [[2025_Matrone_QR_LSTM_Attention_EV_Load]] : Calendar features (month/day/hour/minute) fed to QR-LSTM with attention on Utrecht parking-lot data.
- 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] : Sine/cosine cyclic encoding of hour/day/month plus derived flags (is_morning/is_evening/is_peak_hour); hour_cos and is_evening dominate TFT encoder importance.
