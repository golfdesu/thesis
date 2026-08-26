---
type: paper
title: "Electric vehicles load forecasting for day-ahead market participation using machine and deep learning methods"
authors: [Zafeirios N. Bampos, Vasilis M. Laitsos, Konstantinos D. Afentoulis, Stylianos I. Vagropoulos, Pantelis N. Biskas]
year: 2024
journal_conference: "Applied Energy 360 (2024) 122801"
doi_url: "https://doi.org/10.1016/j.apenergy.2024.122801"
models_used: ["[[XGBoost]]", "[[MLP]]", "[[CNN_Dense]]", "[[CNN_LSTM]]", "[[TCN]]", "[[SARIMA]]", "[[Persistence_Model]]", "[[Holt_Exponential_Smoothing]]"]
datasets_used: ["[[Palo_Alto_EV_Charging]]", "[[Crowdcharge]]", "[[Greenflux]]", "[[ACN_Data]]"]
features_used: ["[[EV_Load_Curve]]", "[[Trend_Residual_Decomposition]]", "[[Cyclical_Time_Features]]", "[[Week_of_Year]]", "[[Holiday_Flag]]", "[[Historical_Lags]]"]
forecasting_horizon: "[[Day_Ahead]]"
metrics: ["[[nMAE]]", "[[nRMSE]]", "[[R2_Score]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Electric Vehicles Load Forecasting for Day-Ahead Market Participation Using Machine and Deep Learning Methods

## 🎯 Main Objective & Contribution
- First-of-its-kind systematic benchmark of **9 EV Load Curve (EVLC) forecasting methods** (statistical, [[ML]], [[DL]]) designed specifically for the operational requirements of **[[Day_Ahead_Market]] (DAM)** participation by EV aggregators/suppliers.
- **36-h ahead hourly horizon** aligned with European DAM gate closure at 12 pm CET (first 12 h omitted → day-ahead 24 h forecast); conservative offline scenario extends to 48 h with 24 h omitted.
- Compares models **with online data ("sc") vs without online data ("wo, sc")**; evaluates over a **full year of rolling daily simulations** to expose seasonal variation.
- Provides a step-by-step methodology for **constructing hourly EVLCs from session-based tabular charging data**.

## 🧠 Methodology & Model Architecture
**Two-component decomposition**: EVLC is split into trend + residual; each is forecast separately and recombined multiplicatively.

1. **EVLC construction from sessions** — assume constant power per session (**Eq. — Charging power**):
$$P_i = \frac{E_i}{t_i}$$
($E_i$ = session energy [kWh], $t_i$ = actual charging duration [h]; plug-in ≠ charging duration). Per-second aggregate power across all $n$ sessions (**Eq. — Aggregated EVLC**):
$$\text{EVLC}_t = \sum_{i=1}^{n} P_{i,t} \quad \forall t$$
built per-second then re-sampled to hourly kW/h (= kWh/h) by averaging.

2. **Multiplicative decomposition** (**Eq. — Residual computation**):
$$\text{EVLC residual}_t = \frac{\text{EVLC}_t}{\text{Average}\left(\text{EVLC trend}_{[t-168,t]}\right)} \quad \forall t$$
Residual approximates white noise; trend captured with **[[Holt_Exponential_Smoothing]]** (fast retraining before each inference).

3. **Nine residual forecasting models** (trend component held fixed for fairness):
   - ML: [[XGBoost]]$_{wo,sc}$ / [[XGBoost]]$_{sc}$ (1250 lags [t−1250,t−1], n_estimators=120, lr=0.14); [[MLP]]$_{wo,sc}$ / [[MLP]]$_{sc}$ (168 lags; Bayesian-optimized FF layer 32–512 neurons, lr=0.001).
   - DL: CNN-Dense$_{sc}$ and CNN-LSTM$_{sc}$ ([[2018_Bai_Empirical_TCN_Sequence_Modeling|conv]] filters 64–128, kernel 4–8, LSTM units 32–128); [[TCN]]$_{sc}$ (filters 128–256, dilations [1,2,4,8,16,32]); all with 168 lags, lr=0.001, early stopping.
   - Statistical: SARIMA$_{sc}$ (24 lags, selected order $(p,d,q)(P,D,Q)_s = (0,0,0)(0,1,0)_{24}$).
   - Baseline: [[Persistence_Model]]$_{wo,sc}$ — target hour = average of corresponding hours from two most recent non-holiday weeks.
   - Monthly retraining for ML/DL, daily for statistical models; tuned via Bayesian Optimization (15 trials).

## 📊 Dataset & Input Features
| Dataset | Period used | Sessions | Stations | Mean/max kWh |
|---|---|---|---|---|
| [[Palo_Alto_EV_Charging]] | 01/2017–12/2018 | **259,415** | 52 | 8.54 / 97.36 |
| [[Crowdcharge]] (Electric Nation, UK) | 03/2017–12/2018 | **71,257** | 301 | 10.39 / 393 |
| [[Greenflux]] (Electric Nation, UK) | 03/2017–12/2018 | **86,256** | 400 | 10.11 / 628.8 |
| [[ACN_Data]] (Caltech, CA) | 04/23–10/23/2018 | **581** | 54 | 17.17 / 69.37 |

- **Data URLs / availability**: Palo Alto Open Data Portal: https://data.cityofpaloalto.org/datasets/194693-electric-vehicle-charging-station-usage-july-2011-dec-2020.download/ ; Electric Nation (Crowdcharge & Greenflux): https://opennetzero.org/dataset/electric-nation ; ACN-Data: https://ev.caltech.edu/dataset . Data availability statement: *"We have used publicly available data. All data reference can be found in the manuscript."*
- Hourly granularity; training/validation = 2017, evaluation = full year 2018 (ACN: Jun–Oct 2018 due to limited history).
- **Input features**: sine/cosine of forecasted hour, sine/cosine of day of year, week of year (categorical 1–52), holiday indicator; online models additionally use historical EVLC lags ([t−168,t−1] or [t−1250,t−1]).
- Session clustering per Develder et al.: datasets dominated by "Near home charging" (Electric Nation) and "Park to charge" behaviors.

## 📈 Performance & Results
Yearly nMAE (%) / nRMSE (%) / R² (baseline = Persistence$_{wo,sc}$):
| Model | Palo Alto | Crowdcharge | Greenflux | ACN |
|---|---|---|---|---|
| XGBoost$_{wo,sc}$ | 5.845 / 8.064 / 0.83 | 9.090 / 13.116 / 0.43 | 6.825 / 9.850 / 0.50 | 7.223 / 9.834 / 0.73 |
| MLP$_{wo,sc}$ | 5.746 / 8.162 / 0.82 | 6.905 / 9.250 / 0.72 | 5.932 / 8.592 / 0.62 | **6.887 / 9.727 / 0.74** |
| XGBoost$_{sc}$ | **5.387 / 7.428 / 0.81** | 8.419 / 11.946 / 0.52 | 6.336 / 8.835 / 0.58 | 8.279 / 11.351 / 0.63 |
| MLP$_{sc}$ | 5.698 / 7.682 / 0.80 | **6.804 / 9.426 / 0.64** | **5.122 / 7.348 / 0.72** | 8.119 / 11.079 / 0.66 |
| CNN-Dense$_{sc}$ | 7.284 / 9.890 / 0.72 | 9.778 / 12.855 / 0.45 | 7.210 / 10.007 / 0.48 | 17.816 / 26.007 / −0.9 |
| CNN-LSTM$_{sc}$ | 6.989 / 9.648 / 0.71 | 10.312 / 13.914 / 0.35 | 6.973 / 9.736 / 0.50 | 13.169 / 17.950 / 0.10 |
| TCN$_{sc}$ | 6.177 / 8.319 / 0.81 | 9.436 / 12.846 / 0.45 | 6.923 / 9.856 / 0.49 | 12.714 / 17.128 / 0.18 |
| SARIMA$_{sc}$ | 9.078 / 13.065 / 0.55 | 10.247 / 13.646 / 0.37 | 7.175 / 10.172 / 0.45 | 10.390 / 15.098 / 0.37 |
| Persistence baseline | 6.445 / 9.211 / 0.78 | 8.511 / 11.373 / 0.57 | 6.036 / 8.703 / 0.60 | 7.560 / 10.353 / 0.70 |

- **Key findings**: simple [[ML]] ([[XGBoost]], [[MLP]]) beats all complex [[DL]] models on nearly every dataset/metric. Best gains vs baseline: XGBoost$_{sc}$ +1.058% nMAE (Palo Alto); MLP$_{sc}$ +1.707% nMAE (Crowdcharge), +0.914% nMAE & +1.355% nMSE (Greenflux); MLP$_{wo,sc}$ +0.673% nMAE (ACN). Only TCN$_{sc}$ beat the baseline on one dataset (+0.268% nMAE, Palo Alto) yet still lost to ML models.
- On the small [[ACN_Data]] set, offline simple models outperformed online ones; DL architectures overfit (CNN-Dense R² = −0.9).
- Online data helps but only marginally (~0.5–1%) → robust DAM forecasting possible without real-time feeds.
- Monthly analysis: top models hold ~5% monthly nMAE; all models struggle in September on Greenflux (peak-load surge); errors rise during peak-load hours regardless of time of day.

## 💡 Limitations & Identified Research Gaps
- No probabilistic/quantile forecasts — point forecasts only, though DAM bidding and risk management need uncertainty quantification.
- Best improvements over persistence are modest (<2%); no model dominates across datasets → no one-size-fits-all approach; performance tied to fleet characteristics (location, size, user habits).
- Bid price strategy explicitly out of scope (quantity-only bidding).
- DL underperformance suggests room for architectures/data regimes that handle small or volatile fleets; September-type anomalous peak events degrade all models.
- Constant-power-per-session assumption in EVLC construction simplifies real charging curves.

## 📚 BibTeX & Citation Reference
```bibtex
@article{bampos2024evdam,
  title   = {Electric vehicles load forecasting for day-ahead market participation using machine and deep learning methods},
  author  = {Bampos, Zafeirios N. and Laitsos, Vasilis M. and Afentoulis, Konstantinos D. and Vagropoulos, Stylianos I. and Biskas, Pantelis N.},
  journal = {Applied Energy},
  volume  = {360},
  pages   = {122801},
  year    = {2024},
  doi     = {10.1016/j.apenergy.2024.122801}
}
```

## 🔗 Key References & Citation Graph
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM within CNN-LSTM hybrid ([43]).
- [[2018_Bai_Empirical_TCN_Sequence_Modeling]] — [[TCN]] basis ([44]).
- [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] — prior hierarchical probabilistic EV forecasting benchmark ([33]).
- Related vault concepts: [[Day_Ahead_Market]], [[EV_Aggregator]], [[XGBoost]], [[MLP]], [[TCN]], [[SARIMA]], [[Persistence_Model]], [[Palo_Alto_EV_Charging]], [[ACN_Data]]
