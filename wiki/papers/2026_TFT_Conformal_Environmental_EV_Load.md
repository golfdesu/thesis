---
type: paper
title: "Forecasting EV charging load with a temporal fusion transformer: A multi-horizon and interpretable approach with environmental features"
authors: [Danial Moghadam Dost, Mohsen Kalantar, Aref Eskandari, Mohammadjavad Peyravi]
year: 2026
journal_conference: "Computers and Electrical Engineering, Vol. 135, Art. 111201 (Elsevier)"
doi_url: "https://doi.org/10.1016/j.compeleceng.2026.111201"
models_used: ["[[Temporal_Fusion_Transformer]]", "[[Conformal_Prediction]]", "[[Quantile_Regression]]"]
datasets_used: ["[[Palo_Alto_EV]]", "[[Weather]]"]
features_used: ["[[Temperature]]", "[[Precipitation]]", "[[Solar_Radiation]]", "[[Calendar_Features]]", "[[Calendar_Features]]", "[[Calendar_Features]]", "[[Calendar_Features]]", "[[Cyclical_Encodings]]", "[[Historical_Load]]", "[[Rolling_Energy_Aggregates]]", "[[Session-Level_Statistics]]", "[[Charging_Efficiency_Metrics]]", "[[Charging_Fee_Statistics]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MSE]]", "[[MAPE]]", "[[SMAPE]]", "[[R_squared]]", "[[Pinball_Loss]]", "[[PICP]]", "[[MPIW]]", "[[NPIW]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Forecasting EV charging load with a temporal fusion transformer: A multi-horizon and interpretable approach with environmental features

> Danial Moghadam Dost, Mohsen Kalantar, Aref Eskandari*, Mohammadjavad Peyravi — Dept. of Electrical Engineering, Iran University of Science and Technology (IUST), Tehran, Iran. *Corresponding: aeskandari@iust.ac.ir
> Received 26 Dec 2025; revised 7 Apr 2026; accepted 21 Apr 2026; online 25 Apr 2026. © 2026 Elsevier Ltd.

## 🎯 Main Objective & Contribution

Develop a unified, interpretable, probabilistic framework for [[EV_Charging_Demand|EV charging load forecasting]] using the [[Temporal_Fusion_Transformer]] (TFT), providing **native multi-horizon** predictions at two timescales — **hourly (1–24 h ahead)** and **daily (1–7 days ahead)** — enriched with environmental covariates and calibrated by conformal prediction. Four identified research gaps motivate the work:

- **RG1**: Prior models target a single resolution or rely on recursive/iterative multi-step strategies prone to error accumulation; no unified native dual-timescale architecture existed.
- **RG2**: Environmental variables (temperature, rainfall, solar radiation) are underutilized despite their documented effect on EV user behavior.
- **RG3**: Most DL forecasters are black boxes without actionable feature attribution.
- **RG4**: Literature fragments into point-accuracy work vs. probabilistic pipelines; no single end-to-end DL model delivers both.

Contributions: (C1) first native short-term + medium-term EV load forecaster in one end-to-end TFT; (C2) rich environmental + calendar covariate integration synchronized to high-resolution records; (C3) built-in interpretability via variable selection networks, attention, GRNs; (C4) validation on multi-year real-world [[Palo_Alto_EV|Palo Alto]] data with hybrid imputation and sine–cosine encoding; (C5) quantile-loss training enabling conditional probabilistic forecasts, evaluated by a **dual-track** framework (point metrics + probabilistic metrics) with post-hoc conformal calibration.

## 🧠 Methodology & Model Architecture

TFT processing two input streams: past observed inputs (historical load + rolling stats) and future known inputs (calendar + environmental forecasts). Core mechanisms:

1. **Variable Selection Networks (VSN)** — instance-wise feature selection per time step, separate modules for encoder and decoder inputs.
2. **Temporal processing** — seq2seq LSTM encoder-decoder for local dynamics + masked interpretable multi-head attention for long-range dependencies.
3. **Gated Residual Networks (GRN)** — adaptive nonlinear processing.
4. **Quantile Forecasting Head** — direct quantile outputs {0.1, 0.5, 0.9} instead of MSE point regression; P50 as robust point forecast, [P10, P90] as uncertainty band.
5. **Conformal Prediction (CQR-style) post-hoc calibration** — non-conformity scores computed on validation set (which serves dual purpose: early stopping + calibration); no retraining needed.

**Log-shift normalization** (Eq. 1):
$$X_{norm} = \ln\left(1 + (X - X_{min})\right)$$

**Quantile forecast head** (Eq. 2, Quantile Output Equation):
$$\hat{y}(q,t,\tau) = W_q \psi(t,\tau) + b_q$$
where $\psi(t,\tau)$ is the temporal fusion decoder output and $W_q, b_q$ are learned per-quantile weights/bias.

**Training objective** (Eq. 3, Summed Quantile Loss):
$$L(\Omega, W) = \frac{\sum_{y_t \in \Omega} \sum_{q \in \mathcal{Q}} \sum_{\tau=1}^{\tau_{max}} QL(y_{t+\tau}, \hat{y}_{t+\tau}^{(q)})}{M}$$
with $\mathcal{Q} = \{0.1, 0.5, 0.9\}$, $\Omega$ training domain, $M$ normalization factor.

**Pinball loss** (Eq. 4):
$$QL(y,\hat{y}) = \max\left(q(y-\hat{y}),\ (q-1)(y-\hat{y})\right)$$

**Deterministic metrics**: Eq. 5 MAE $= \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$; Eq. 6 MSE; Eq. 7 RMSE $=\sqrt{\frac{1}{n}\sum_{i=1}^n (y_i-\hat y_i)^2}$; Eq. 8 $R^2 = 1 - \frac{\sum_i (y_i-\hat y_i)^2}{\sum_i (y_i-\bar y)^2}$; Eq. 9 MAPE; Eq. 10 SMAPE (ε-policy $\varepsilon=10^{-6}$ applied).

**Average quantile loss** (Eq. 11):
$$L_q = \frac{1}{n}\sum_{i=1}^n \max\left(q(y_i - \hat{y}_i^{(q)}),\ (q-1)(y_i - \hat{y}_i^{(q)})\right)$$

**Coverage** (Eq. 12, PICP): $PICP = \frac{1}{n}\sum_{i=1}^n \mathbb{I}(\hat{L}_i \le y_i \le \hat{U}_i)$; **sharpness** (Eq. 13, MPIW): $MPIW = \frac{1}{n}\sum_{i=1}^n (\hat U_i - \hat L_i)$; **normalized width** (Eq. 14, NPIW): $NPIW = MPIW / \sigma_y$.

**Training setup**: chronological 70%/15%/15% train/validation/test split; validation doubles as conformal-calibration set. Manual grid search; final hyperparameters (Table 4): learning rate 0.0005 (hourly) / 0.001 (daily); batch size 32 (hourly) / 64 (daily); hidden dim 64; 4 attention heads; dropout 0.1; 1 LSTM layer; horizons 24 h / 7 d; Adam optimizer; early stopping patience 10 epochs; loss = quantile loss. Encoder/horizon windows: $k=72,\ \tau=24$ (hourly); $k=30,\ \tau=7$ (daily). PyTorch (Python 3.10), NVIDIA GPU.

Preprocessing: linear interpolation for gaps <6 h; nearest-valid-neighbor imputation for 6–24 h gaps; discard >24 h gaps; IQR outlier flagging + physical plausibility checks; log1p scaling of all continuous inputs; sine/cosine cyclic encoding of hour/day/month.

## 📊 Dataset & Input Features

- **[[Palo_Alto_EV]]**: public EV charging stations in **Palo Alto, California**, **2018–2022** (multiple years of hourly energy consumption, kWh per record with timestamp). Data availability statement: *"Data will be made available on request."* No explicit public URL given in the text (dataset originates from the City of Palo Alto open data portal per related literature, e.g., Amara-Ouali et al. used the same source).
- **[[Weather]]**: temperature, solar radiation, rainfall retrieved via the **Open-Meteo API** (https://open-meteo.com) for the same location/time; environmental variables interpolated/synchronized to hourly resolution.

Features (Tables 2–3, 10): consumption energy (kWh, time-varying target); known inputs = mean daily temperature (°C), cumulative daily rainfall (mm), total daily solar radiation (Wh/m²), hour/day/month calendar features, weekend indicator. Engineered: cyclical sine/cosine encodings (hour_sin/cos, day_of_week_sin), relative time index, time-of-day binary flags (is_morning/is_evening/is_peak_hour), rolling energy sums over 3/7/14-day windows, min–max normalized total energy, session-level statistics (total/average duration, energy per session, number of sessions), charging efficiency mean/std, charging fee sum/mean, historical lagged load ($y_{t-1}, y_{t-2},\dots$).

Descriptive analysis: demand trough 02:00–05:00, peak 17:00–20:00 aligned with commuting; weekly pattern rising Mon→Thu, dip Fri–Sat.

## 📈 Performance & Results

**Table 5 — proposed TFT (real scale):**

| Scenario | MSE (kWh²) | RMSE (kWh) | MAE (kWh) | MAPE (%) | SMAPE (%) | R² |
|---|---|---|---|---|---|---|
| Hourly (1–24 h) | 1.6096 | 1.2687 | 0.8399 | 16.17 | 8.02 | 0.9871 |
| Daily (1–7 d) | 0.508 | 0.71 | 0.662 | 6.17 | 4.37 | 0.98 |

**Table 6 — daily-scale vs literature baselines:** TFT (MSE 0.508, RMSE 0.71, MAPE 6.17 %, SMAPE 4.37 %, MAE 0.662, R² 0.98) vs ConvLSTM+BiLSTM (MSE 0.878, RMSE 0.71, MAPE 18.31 %), BiConvLSTM+LSTM (MSE 0.87, RMSE 0.73, MAPE 24.58 %), XGBoost_sc (RMSE 2.748, MAE 5.37, R² 0.81), Meta Fusion Regressor (RMSE 2.24, MAE 0.91), TCN-LSTM (MAPE 6.37, MAE 19.97). Best overall.

**Table 7 — weather-integrated daily comparison (normalized scale):** TFT MSE 0.001764, MAPE 1.20 %, MAE 0.02889 vs Transformer (0.02008 / 19.03 / 0.10869), CNN (0.01615 / 16.93 / 0.09394), RNN (0.02162 / 19.61 / 0.11471), XGBoost (0.02484 / 22.74 / 0.12703), LSTM (0.02562 / 23.38 / 0.12577), Prophet (0.02726 / 22.29 / 0.18589), SARIMA (0.02881 / 23.69 / 0.19554). Normalized RMSE 0.04202 vs 0.726 for mRGC-CBi-LSTM [40] (~94 % reduction).

**Table 8 — one-hour-ahead (kWh):** TFT RMSE 1.2687 / MAE 0.8399 / SMAPE 8.02 % vs CNN-LSTM (5.002 / 3.567 / 31.7), LSTM (5.967 / 4.464 / 36.9), GRU (7.307 / 5.015 / 38.6), RNN (8.21 / 5.629 / 38.6). >78 % improvement over LSTM/GRU RMSE.

**Probabilistic results (daily horizon):** raw TFT 80 % intervals were overconfident — PICP = 64.47 %, MPIW = 3.093 kWh. After conformal calibration: **PICP = 96.2 %** (nominal 80 %), MPIW = 9.639 kWh, NPIW ≈ 9.639/13.10 ≈ **0.74** (<1 ⇒ sharp relative to data spread σ_y = 13.10 kWh). Post-calibration deterministic error rose slightly (RMSE 1.056 kWh, MAE 0.765 kWh) — an explicit reliability–accuracy trade-off. Vs probabilistic baselines (Table 9, Amara-Ouali et al.): QGAM coverage 0.79 ("valid but tight"), SARIMA+GMM 0.66 ("poor"), TFT+CQR 0.96 ("conservative & safe").

**Interpretability:** encoder importance dominated by temporal features (hour_cos, is_evening, relative_time_idx) and rolling 14-day energy; decoder dominated by charging_efficiency_std; temporal attention slightly higher weights ~30 days back (≈0.042 at −30 vs ≈0.029 at t≈0) → monthly behavioral cycles (billing/salary cycles).

## 💡 Limitations & Identified Research Gaps

- Environmental/pricing variables showed comparatively **small** VSN importance — demand governed mainly by temporal regularities and recent usage in this dataset.
- Static tariff structure limits behavioral insight; authors hypothesize dynamic pricing would reweight attention toward price features (future work).
- Post-conformal coverage (96.2 %) far exceeds nominal 80 % → conservative/wider intervals; marginal degradation of point accuracy.
- Future work suggested: electricity pricing, traffic density, charging-behavior segmentation, socioeconomic indicators; cross-city/climate generalization tests; real-time/edge deployment; coupling probabilistic outputs with optimization for station/grid management.
- Single-city validation only; no spatial dimension modeled.

## 📚 BibTeX & Citation Reference
```bibtex
@article{MoghadamDost2026TFT,
  author  = {Moghadam Dost, Danial and Kalantar, Mohsen and Eskandari, Aref and Peyravi, Mohammadjavad},
  title   = {Forecasting EV charging load with a temporal fusion transformer: A multi-horizon and interpretable approach with environmental features},
  journal = {Computers and Electrical Engineering},
  volume  = {135},
  pages   = {111201},
  year    = {2026},
  doi     = {10.1016/j.compeleceng.2026.111201}
}
```

## 🔗 Key References & Citation Graph

- [[2021_TFT_Temporal_Fusion_Transformers]] — the underlying TFT architecture (quantile outputs, VSN, GRN, interpretable attention).
- [[2021_Conformal_Time_Series_Forecasting]] — related conformal calibration of deep time-series forecasters.
- [[2024_Conformal_Prediction_DER]] — conformal prediction for distributed energy resources (coverage/interval-size framing).
- [[2024_DiffPLF_Conditional_Diffusion_EV]] — cited diffusion-based probabilistic EV charging forecast (ref [31]).
- [[2025_Hybrid_LSTM_Transformer_Demand]] — LSTM+Transformer hybrid on ACN data (ref [25], identified gap RG1/RG2).
- [[2025_CAT_Former_Short_Term_EV]] — CAT-Former contextual transformer on Boulder data (ref [26], deterministic-only gap).
- [[2026_MFT_Multi_Scale_Fusion_Transformer]] — Multi-scale Fusion Transformer, Norway residential data (ref [27]).
- [[2024_EV_Load_Forecasting_DAM]] — XGBoost_sc day-ahead benchmark (ref [37]) compared in Table 6.
- [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]] — related spatiotemporal EV charging-load line of work (spatial dimension absent here).
- [[2025_QR_LSTM_Attention_EV_Load]] — quantile/LSTM probabilistic EV load forecasting alternative.
- [[2023_Transformer_EV_Demand]] — Boulder EV demand + NOAA weather, related environmental-covariate approach.
- [[2025_Benchmark_Foundation_Models]] — broader probabilistic/point benchmarking context.
