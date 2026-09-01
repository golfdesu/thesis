---
type: paper
title: "Data-driven Short-term Electric Vehicle Charging Station Demand Forecasting"
authors: [Meiyi Huo, Songling Pang, Hao Bai, Wei Li, Min Xu, Tong Liu]
year: 2024
journal_conference: "2024 IEEE 7th International Electrical and Energy Conference (CIEEC)"
doi_url: "https://doi.org/10.1109/CIEEC60922.2024.10583059"
models_used: ["[[MLP]]", "[[SVR]]", "[[XGBoost]]"]
datasets_used: ["[[Caltech_ACN]]"]
features_used: ["[[Historical_Load]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[R_squared]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Data-driven Short-term Electric Vehicle Charging Station Demand Forecasting

## 🎯 Main Objective & Contribution
- Proposes a **data-driven framework** for short-term (one-step-ahead, hourly) demand forecasting at EV charging stations (EVCS), motivated by grid-operation challenges posed by surging EV charging demand (IEA: ~10 million EVs worldwide by end of 2020, +41% registrations in 2020).
- Builds three ML forecasting models of different families — **Artificial Neural Network ([[MLP]])**, **Support Vector Regression (SVR)**, and **Boosted Regression Trees (BRT)** — and systematically compares them.
- Key contribution: a **hyperparameter optimization method based on the parameter-free [[Rao-1]] evolutionary algorithm**, avoiding the algorithm-self-hyperparameter problem of GA/swarm methods.
- Verified on real public ACN data from two stations (JPL, Caltech); all ML models beat the persistence baseline; ANN/BRT outperform SVR.

## 🧠 Methodology & Model Architecture
Pipeline: data cleaning + feature selection → train/test split → ML model trained on training set → hyperparameters tuned by Rao-1 evolutionary computation → error evaluated on test set.

**Input definition (Eq. 1 – Historical load window)**: one-step prediction using hourly load within 24 h before forecast time:
$$H_t = \{h_{t-1}, h_{t-2}, \cdots, h_{t-24}\}$$

**Generic model form (Eq. 2)**:
$$h_t = f(H_t) + e_t$$
where $f$ is the machine learning algorithm and $e_t$ the model error. Given $D=\{(x_i,y_i)\mid i=1,2,\cdots,N\}$, $f$ minimizes the difference between $f(x)$ and $y$.

**Boosted Regression Trees (Eqs. 3–6)** — ensemble of $M$ weak tree learners $T_m(x,\theta_m)$ (square loss $L(y,f(x))=(y-f(x))^2$, solved by gradient boosting in forward step-wise manner):
$$f(x) = \sum_{m=1}^{M} T_m(x,\theta_m)$$
$$\{\theta_m\}_{m=1}^{M} = \arg\min_{\{\theta'_m\}_{m=1}^{M}} \sum_{i=1}^{N} L\Bigl(y_i,\ \sum_{m=1}^{M} T_m(x,\theta'_m)\Bigr)$$
$$\theta_m = \arg\min_{\theta}\ \sum_{i=1}^{N} L\bigl(y_i,\ f_{m-1}(x_i) + T_m(x_i,\theta)\bigr)$$
$$f_m(x) = f_{m-1}(x) + \lambda T(x_m,\theta_m)$$
with learning rate $\lambda$; each $T_m$ fits the current residual $y-f_{m-1}(x)$.

**ε-Support Vector Regression (Eqs. 7–10)** — ε-SVM with radial basis kernel:
$$f(x) = w\phi(x) + b$$
$$\min\ \frac{1}{2}\|w\|^2 + C\sum_{i=1}^{N}(\xi+\xi^*)\quad \text{s.t.}\quad \begin{cases} y_i - w\phi(x_i) - b \le \epsilon + \xi_i \\ w\phi(x_i) + b - y_i \le \epsilon + \xi_i \\ \xi_i, \xi_i^* \ge 0 \end{cases}$$
$$f(x) = \sum_{i=1}^{N} (\alpha_i - \alpha_i^*)K(x_i,x) + b$$
$$K(x_i,x_j) = \exp\left(\frac{-\|x_i-x_j\|^2}{2\sigma^2}\right)$$
($C$ penalty factor, $\epsilon$ insensitivity coefficient, $\alpha_i,\alpha_i^*$ Lagrange multipliers, $\sigma$ kernel control coefficient.)

**ANN / MLP (Eq. 11 – tanh hidden activation)**: single-hidden-layer MLP, tanh hidden activation (as printed, OCR-degraded; reconstructed standard form), linear output, weights optimized by the Levenberg–Marquardt algorithm:
$$\mathrm{tansig}(u) = \frac{2}{1+\exp(-2u)} - 1$$

**Rao-1 hyperparameter optimization (Eqs. 12–13)**: hyperparameters tuned are BRT {number of weak learners $M$, learning rate $\lambda$, max splits $p$}; SVR {$\epsilon$, $C$, $\sigma$}; ANN {number of hidden neurons $Q$}.
$$\min_{\phi}\ L(y, f(x|\phi))$$
$$\phi'_{i,j,k} = \phi_{i,j,k} + r_{i,k}\bigl(\phi_{i,best,k} - \phi_{i,worst,k}\bigr)$$
where $\phi_{i,best,k}$/$\phi_{i,worst,k}$ are elements of best/worst candidate solutions of generation $i$, and $r_{i,k}$ random values in $[0,1]$. Rao-1's stated advantage: simple and **parameter-free** (no meta-hyperparameters unlike GA/PSO).

## 📊 Dataset & Input Features
- **[[Caltech_ACN]] ACN-Data** (Lee, Li & Low, ACM e-Energy 2019): public open EV charging session dataset covering two workplace stations at the **California Institute of Technology (Caltech)** and the **Jet Propulsion Laboratory (JPL)**.
  - Period used: **all records from January 3, 2019 to March 19, 2020**.
  - Raw granularity: individual charging-session records (start time, energy consumed, user info). Preprocessing: sessions converted to **1-minute resolution time series**, then **hourly average charging power** computed as forecast target.
  - Access status: **publicly available** (open dataset; paper cites ref. [17], URL not printed in PDF text; hosted at ev.caltech.edu). No utility/company restriction.
- **Input feature**: historical load only — the 24 hourly loads preceding the forecast hour ($H_t$); no weather/calendar exogenous variables.
- **Split**: chronological 7:3 — training = Jan 3 – Nov 8, 2019 (**310 days**); test = Nov 9, 2019 – Mar 19, 2020 (**132 days**).
- Load series exhibits clear daily periodicity (shown for JPL in Fig. 2).

## 📈 Performance & Results
Metrics: MAE, RMSE, R² (Eqs. 14–16). Baseline: **persistence model (PER)**, $\hat{h}_t = h_{t-1}$.

**JPL station (Table II)**:

| Model | MAE (kW) | RMSE (kW) | R² |
|---|---|---|---|
| PER | 8.28 | 16.34 | 0.855 |
| BRT | 4.15 | 7.30 | 0.971 |
| SVR (SVM) | 5.30 | 10.39 | 0.941 |
| ANN | **4.19** | **6.93** | **0.974** |

**Caltech station (Table III)**:

| Model | MAE (kW) | RMSE (kW) | R² |
|---|---|---|---|
| PER | 3.47 | 6.69 | 0.745 |
| BRT | **2.83** | 4.76 | 0.871 |
| SVR (SVM) | 3.14 | 5.76 | 0.811 |
| ANN | 3.00 | **4.50** | **0.885** |

Findings:
- All ML models substantially beat persistence (e.g., JPL RMSE 6.93 kW ANN vs 16.34 kW PER, ≈58% reduction).
- BRT and ANN clearly better than SVR. By MAE, BRT < ANN at both sites; by RMSE/R², ANN < BRT. Box plots show BRT more prone to larger absolute errors — since RMSE/R² penalize squared errors, ANN wins those metrics despite slightly higher MAE.
- Both BRT and ANN track load variations well (Figs. 6–7).

## 💡 Limitations & Identified Research Gaps
- Only **univariate autoregressive** inputs ($H_t$, past 24 h): no calendar, weather, TOU price, or traffic features (contrast [[2024_TOU_Price_Meteorology_EV_Charging_Load]] which adds TOU price/meteorology, and [[2024_LASSO_BPNN_Mid_Term_EV_Load]] which adds socio-economic indicators).
- One-step (1 h ahead) only; no multi-step or day-ahead horizons.
- Two workplace stations only (same ACN source); no cross-station/cross-region generalization testing.
- No uncertainty/probabilistic forecasts; point predictions only.
- Hyperparameter search cost of wrapping Rao-1 around retraining not quantified in detail.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{huo2024datadriven,
  author    = {Huo, Meiyi and Pang, Songling and Bai, Hao and Li, Wei and Xu, Min and Liu, Tong},
  title     = {Data-driven Short-term Electric Vehicle Charging Station Demand Forecasting},
  booktitle = {2024 IEEE 7th International Electrical and Energy Conference (CIEEC)},
  year      = {2024},
  pages     = {--},
  address   = {Hainan/Guangdong, China},
  doi       = {10.1109/CIEEC60922.2024.10583059}
}
```
Note: page numbers not extractable from the provided text. Author order follows the numbered IEEE header: Huo (1st), Pang (2nd), Bai (3rd), Li (4th, corresponding), Xu (5th), Liu (6th). Funded by China Southern Power Grid Corporation Technology Project 073000KK52220001.

## 🔗 Key References & Citation Graph
- **[17] Lee, Li, Low — "ACN-Data: Analysis and Applications of an Open EV Charging Dataset"** (ACM e-Energy 2019): the data source → see [[Caltech_ACN]].
- **[18] Döpke et al., Int. J. Forecasting 2017** — boosted regression trees methodology source.
- **[19] Smola & Schölkopf 2004** — SVR tutorial basis.
- **[20] Moré 1978** — Levenberg–Marquardt algorithm (ANN weight optimization).
- **[14] Huang, Wu, Boulet, IEEE EPEC 2020** — ensemble ANN+RNN+LSTM for next-hour station load (related aggregation-level approach; cf. [[2020_Ensemble_EV_Load]]).
- **[12] Arias & Bae, Applied Energy 2016**; **[13] Yi et al. 2021** (LSTM regional monthly EV load); **[15][16]** SVM/KNN predecessors.
- Related vault papers: [[2024_TOU_Price_Meteorology_EV_Charging_Load]] (adds TOU price/weather exogenous features to short-term station forecasting), [[2024_LASSO_BPNN_Mid_Term_EV_Load]] (feature selection + MLP-family model, mid-term horizon), [[2021_Day_Ahead_EV_Demand]] (day-ahead station-level forecasting with calendar features absent here).
