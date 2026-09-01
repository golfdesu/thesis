---
type: paper
title: "An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations"
authors: [Lubos Buzna, Pasquale De Falco, Gabriella Ferruzzi, Shahab Khormali, Daniela Proto, Nazir Refa, Milan Straka, Gijs van der Poel]
year: 2021
journal_conference: "Applied Energy, 283, 116337"
doi_url: "https://doi.org/10.1016/j.apenergy.2020.116337"
models_used: ["[[GBRT]]", "[[QRF]]", "[[QRNN]]", "[[PLQR]]", "[[PCA]]"]
datasets_used: ["[[ElaadNL]]", "[[Weather]]", "[[COROP_Regions]]"]
features_used: ["[[Historical_Load]]", "[[Weather_Forecast]]", "[[Super_User_Features]]", "[[Calendar_Features]]", "[[PCA]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[Pinball_Loss]]", "[[AACE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: An Ensemble Methodology for Hierarchical Probabilistic EV Load Forecasting at Regular Charging Stations

## 🎯 Main Objective & Contribution
- First application ever of a **hierarchical approach to probabilistic EV load forecasting (PEVLF)**: forecast EV energy consumption of a high-level geographic region by exploiting baseline probabilistic forecasts of its constituent low-level regions.
- Contributions: (i) hierarchical probabilistic forecasting framework; (ii) evaluation of **PCA dimensionality reduction** in preprocessing; (iii) comparative proof that hierarchy beats direct non-hierarchical forecasting regardless of the underlying model; (iv) extensive validation on real multi-year charging data.
- Result: hierarchical approaches increase the skill of probabilistic forecasts by **up to 9.5%** vs non-hierarchical ones.

## 🧠 Methodology & Model Architecture
Three units: input pre-processing (incl. PCA) → baseline probabilistic models per low-level region → l1-penalized linear quantile regression ([[PLQR]]) ensemble at the high level. Forecasts are Q = 9 quantiles at coverages α = 0.1,…,0.9; hourly resolution.

### GBRT (Gradient Boosted Regression Tree)
Function estimation $P_i = f_i(x_i)$ minimized via a proper score (**Loss Minimization**):
$$\hat{f}_i(x_i) = \arg\min_{f_i(x_i)} \Psi(P_i, f_i(x_i)) \tag{2}$$
Initialization at constant value:
$$\hat{\rho}^{\langle 0\rangle}_i = \arg\min_\rho \sum_{n\in\Omega^{\langle B\rangle}_{tra}} \Psi(P_{i,n}, \rho) \tag{3}$$
Negative gradient (pseudo-residual) at iteration $m$:
$$g_{i,n}(x_{i,n}) = -\left[\frac{\partial\, \Psi(P_{i,n}, f^{\langle m-1\rangle}_i(x_{i,n}))}{\partial f^{\langle m-1\rangle}_i(x_{i,n})}\right]_{f^{\langle m-1\rangle}_i = \hat{f}^{\langle m-1\rangle}_i} \tag{4}$$
Weak learner (regression tree) prediction over $S$ leaves:
$$\hat{g}_{i,n}(x_{i,n}) = \sum_{s=1}^{S} g^{\langle s\rangle}_i \cdot I\{x_{i,n}\in R_{l^{\langle s\rangle}}\} \tag{5}$$
Per-leaf step size and update with shrinkage $\upsilon$:
$$\hat{\rho}^{\langle m,s\rangle}_i = \arg\min_\rho \sum_{n\in\Omega^{\langle B\rangle}_{tra}: x_{i,n}\in R_{l^{\langle s\rangle}}} \Psi(P_{i,n}, \hat{f}^{\langle m-1\rangle}_i(x_{i,n}) + \rho) \tag{7}$$
$$\hat{f}^{\langle m\rangle}_i(x_i) = \hat{f}^{\langle m-1\rangle}_i(x_i) + \upsilon\cdot\sum_{s=1}^{S}\hat{\rho}^{\langle m,s\rangle}_i \cdot I\{x_{i,n}\in R_{l^{\langle s\rangle}}\} \tag{8}$$
Forecast: $\hat{P}_{i,h} = \hat{f}^{\langle m\rangle}_i(x_{i,h})$ (Eq. 9). Loss is the Pinball Score (**PS / Quantile Score**):
$$\Psi(P_{i,n}, \hat{P}^{\langle\alpha_q\rangle}_{i,n}) = (P_{i,n} - \hat{P}^{\langle\alpha_q\rangle}_{i,n})\cdot(\alpha_q - I\{P_{i,n}\leq\hat{P}^{\langle\alpha_q\rangle}_{i,n}\}) \tag{10}$$

### QRF (Quantile Regression Forest)
Weighted empirical conditional CDF (Meinshausen weights, Eqs. 11–12), then quantile extraction:
$$\hat{F}(P_{i,h}\leq P^* \mid x_{i,h}) = \sum_{n\in\Omega^{\langle B\rangle}_{tra}}\left[\omega_n(x_{i,h})\cdot I\{P_{i,n}\leq P^*\}\right] \tag{11}$$
$$\hat{P}^{\langle\alpha_q\rangle}_{i,h} = \inf\{P^* : \hat{F}(P_{i,h}\leq P^* \mid x_{i,h}) \geq \alpha_q\} \tag{13}$$

### QRNN (monotone Quantile Regression Neural Network)
Single-hidden-layer MLP ($J$ neurons, tanh activation Φ) with monotonicity constraints on predictor subset $\Xi_1$ (**Monotone QRNN Quantile Equation**):
$$\hat{P}^{\langle\alpha_q\rangle}_{i,h} = \sum_{j=1}^{J}\left[\Phi\!\left(\sum_{c\in\Xi_1} x^{(i,h)}_c \hat{w}^{\langle\alpha_q\rangle}_{c,j} + \sum_{c\in\Xi_2} x^{(i,h)}_c \hat{w}^{\langle\alpha_q\rangle}_{c,j} + \hat{\tau}^{\langle\alpha_q\rangle}_j\right)\cdot\hat{\delta}^{\langle\alpha_q\rangle}_j\right] + \hat{\varepsilon}^{\langle\alpha_q\rangle} \tag{14}$$
Parameters estimated by constrained PS minimization (Eq. 15), s.t. $\partial\hat{P}^{\langle\alpha_q\rangle}/\partial x_c \geq 0,\ \forall c\in\Xi_1$.

### Hierarchical PLQR ensemble (high-level region)
Predictors $x^{\langle H\rangle}_h$: all R low-level regions' baseline quantile forecasts plus lagged high-level loads (up to 24-h, 48-h, 168-h). Linear quantile combination (**PLQR Quantile Equation**):
$$\hat{P}^{\langle\alpha_q\rangle}_h = x^{\langle H\rangle}_h \cdot \hat{\beta}^{\langle\alpha_q\rangle} \tag{16}$$
l1-penalized estimation (lasso-style, robust to outliers, performs embedded variable selection; λ tuned by 10-fold CV) (**Penalized PS Minimization**):
$$\hat{\beta}^{\langle\alpha_q\rangle} = \arg\min_{\beta^{\langle\alpha_q\rangle}} \frac{1}{\dim(\Omega^{\langle H\rangle}_{tra})}\sum_{n\in\Omega^{\langle H\rangle}_{tra}}\left[\Psi(P_n, \hat{P}^{\langle\alpha_q\rangle}_n)\right] + \lambda\sum_{b=1}^{B}|\beta^{\langle\alpha_q\rangle}_b| \tag{17}$$

### Benchmarks
Low-level: same models without PCA ("no PCA"), persistence BPersB ($\hat{P}_{i,h}=P_{i,h-1}$ hour-ahead Eq. 18; $P_{i,h-24}$ day-ahead Eq. 19). High-level: direct GBRT/QRF/QRNN on high-level series, Sum-and-Sort (SaS) of homologous quantiles, non-penalized NPLQR (λ=0), PLQR without recency lags, HPersB persistence.

## 📊 Dataset & Input Features
- **[[ElaadNL]]** provided by ElaadNL (Dutch smart-charging knowledge centre): two tables — "Transactions" with **1,822,884 rows** (unique charging events: station/charge-point IDs, lat/long, meter start/end, max power, hashed RFID card, UTC start/end); "Meter readings" with **52,294,851 rows** recorded every **15 min** during each transaction (UTC timestamp, transferred energy, meter value). Coverage: **Jan 1, 2012 – June 30, 2018**; analysis restricted to transactions ending after June 30, 2015.
  - Data availability/source URLs found: ElaadNL website https://www.elaad.nl ; transfer of stations to municipalities https://www.evnet.nl/nieuws/meer-dan-de-helft-van-publieke-laadpalen-van-pionier-evnetnl-gaat-over-naar-gemeenten/
- Study period: **July 1, 2015 – June 30, 2018** (hourly resolution); only stations active throughout the whole period. Cleaning: 565 transactions lacking meter readings removed.
- Spatial aggregation into **[[COROP_Regions]]** (40 Dutch statistical regions; https://www.regioatlas.nl/indelingen/indelingen_indeling/t/corop_regio_s); four highest-consumption COROP regions used as low-level regions: Zuidoost-Noord-Brabant (**104 stations**), Rijnmond (**91**), Noordoost-Noord-Brabant (**71**), Utrecht (**40**) → high-level region = sum of the four (~306 stations).
- Weather: real + forecast meteorological data (precipitation [m], snowfall [m water eq.], temperature [°C], wind speed [m/s]) from **[[Weather]]** (https://www.ecmwf.int/) on 0.1°×0.1° grids; day-ahead predictions issued at midnight D−1, hourly resolution.
- Predictors (219 total): weather forecasts per grid square; **super-user predictors** (# users and aggregated consumption of top 100/300/500 users, at 1-h/24-h/48-h/168-h lags); calendar features (working/non-working-day dummy `hol`, hour-of-day integer `hod`). PCA retains **4 principal components** for weather+super-user blocks; calendar variables passed through directly.
- Splits: baseline training Jul 2015–Dec 2016 (~50%, 13,200 points), hierarchical PLQR training year 2017 (~30%, 8,760 pts), test first half of 2018 (~20%, 4,344 pts).

## 📈 Performance & Results
Metrics: averaged **PS** (kWh, negatively oriented; Eq. 20) and **AACE%** reliability (100/Q · Σ|αq − α̂q|; Eq. 21–22), Q = 9 quantiles.
- Hour-ahead baselines (PS kWh): GBRT best on average — Noordoost 18.07, Rijnmond 22.30, Utrecht 14.47, Zuidoost 17.51 vs BPersB 28.34/38.84/22.85/30.75 (36–43% improvement). PCA improves PS by ~1–11% in 3 of 4 regions and cuts training time by >78%.
- Hour-ahead hierarchical (high-level, test set): **PLQR proposal PS 41.35–42.13 kWh** depending on base model (GBRT: 41.57/AACE 1.07%; QRF: 41.35/0.36%; QRNN: 42.13/1.75%) vs Direct 42.91–45.29, SaS 44.92–48.92 (AACE >7%), NPLQR 42.68–44.18, HPersB 89.87 → **~54% better than persistence**, **3.5–8% better than direct**.
- Day-ahead baselines: GBRT 20.65–32.25 kWh vs BPersB 33.86–52.73 (39–40% improvement); PCA gains up to 9.5%, training time −75%.
- Day-ahead hierarchical: **PLQR 69.64–70.47 kWh** (GBRT 69.64/1.32%; QRF 69.88/1.38%; QRNN 70.47/1.54%) vs Direct 74.44–77.82, SaS 74.43–77.42, HPersB 114.85 → **6.5–9.5% better than direct** (max 9.5% gain), **~39% better than persistence**.
- Reliability diagrams near ideal bisector for both levels; SaS highly unreliable. l1-penalization consistently outperforms NPLQR and no-recency variants.

## 💡 Limitations & Identified Research Gaps
- Short-term focus: time-varying predictors such as number of circulating EVs or # stations excluded (limited short-term impact; relevant at medium term).
- Single-model baseline per region; authors propose extending to **multi-model ensemble frameworks** in future work.
- Future work: apply the hierarchical PEVLF system to optimal distribution grid operation (bi-level optimization, market participation).
- Hierarchical merging is generally a nonlinear non-convex problem without global optimality guarantees (motivating their simple penalized-linear approach).

## 📚 BibTeX & Citation Reference
```bibtex
@article{buzna2021ensemble,
  title   = {An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations},
  author  = {Buzna, Lubos and De Falco, Pasquale and Ferruzzi, Gabriella and Khormali, Shahab and Proto, Daniela and Refa, Nazir and Straka, Milan and van der Poel, Gijs},
  journal = {Applied Energy},
  volume  = {283},
  pages   = {116337},
  year    = {2021},
  doi     = {10.1016/j.apenergy.2020.116337}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load]] — quantile-based probabilistic load forecasting lineage
- [[2019_Zhu_EV_Load_Forecasting]] — comparative deep learning study cited as motivation that PEVLF is underexplored
- [[2021_VanKriekinge_Day_Ahead_EV_Demand]] — related day-ahead EV demand deep learning forecasting
- Koenker & Bassett (1978) regression quantiles; Meinshausen (2006) QRF; Cannon (2018) monotone QRNN; Friedman (2002) stochastic gradient boosting; Hastie et al. (2015) lasso; Gneiting & Raftery (2007) strictly proper scoring rules; Hong et al. (2019) GEFCom2017 hierarchical probabilistic load forecasting; Wang et al. (2019) combining probabilistic load forecasts

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2021_Buzna_Hierarchical_Probabilistic_EV_Load_refs]]
