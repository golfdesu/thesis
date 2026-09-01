---
type: paper
title: "Short-term Load Forecasting Considering EV Charging Loads with Prediction Interval Evaluation"
authors: [Naihao Shi, Feixiang Zhang, Zhaoyu Wang, Jason S. MacDonald, Maxime Baudette, Yashen Lin, Venkateswara Motakatla]
year: 2024
journal_conference: "2024 56th North American Power Symposium (NAPS), IEEE"
doi_url: "https://doi.org/10.1109/NAPS61145.2024.10741734"
models_used: ["[[Gaussian_Process_Regression]]", "[[Kernel_Density_Estimation]]"]
datasets_used: ["[[US_Utility_Feeder_Residential_Load]]", "[[Real_World_EV_DC_Charging]]"]
features_used: ["[[Historical_Load]]", "[[Weather_Traffic]]", "[[Calendar_Features]]", "[[Charging_Habit_Probability]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAPE]]", "[[PICP]]", "[[NMPIL]]", "[[CLC]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Short-term Load Forecasting Considering EV Charging Loads with Prediction Interval Evaluation

> **Affiliations (verified from PDF header):** Iowa State University (Shi, Zhang, Wang); Lawrence Berkeley National Laboratory (MacDonald, Baudette); National Renewable Energy Laboratory (Lin, Motakatla).
> **Venue/DOI verified from PDF footer:** "2024 56th North American Power Symposium (NAPS) | 979-8-3315-2103-5/24/$31.00 ©2024 IEEE | DOI: 10.1109/NAPS61145.2024.10741734".
> ⚠️ Distinct from [[2024_Attention_Spatiotemporal_MultiGraph_EV_Load]] (different co-author team/topic).

## 🎯 Main Objective & Contribution
- Probabilistic **day-ahead short-term load forecasting** for a distribution feeder whose load is the sum of residential demand + aggregated **EV charging loads**, using **Gaussian Process Regression (GPR)**.
- Motivation: EV integration raises peak load *and shifts its timing*; deterministic point forecasts are inadequate under EV-induced uncertainty, especially at aggregate (feeder) level, which matters most to system operators.
- Contributions:
	1. A probabilistic (PI-producing) GPR forecaster adapted to day-ahead feeder-level load with integrated EV charging.
	2. Quantitative **prediction interval (PI) evaluation** using metrics covering both interval length (NMPIL) and coverage probability (PICP), combined into a coverage-length-based criterion (CLC) — beyond purely deterministic MAPE/RMSE.
	3. A novel input feature capturing **users' charging habits** (charging probability at time t), shown to greatly improve accuracy when EVs are present.

## 🧠 Methodology & Model Architecture
### A. EV charging load synthesis (data model)
- Starting charging time CT fitted by **kernel density estimation** with Gaussian kernel (Eq. 1):
$$f(CT) = \frac{1}{nV}\sum_{i=1}^{n} K\!\left(\frac{CT - CT_i}{h}\right) \tag{1}$$
where $n$ = number of samples, $h$ = bandwidth, $K(\cdot)$ = kernel function (Gaussian chosen for symmetry).
- Battery capacity $C_0$ ~ Gamma distribution (Eq. 2); initial SOC ~ $\mathcal{N}(0.8, 0.12)$:
$$G(C_0) = \frac{1}{\beta^{\alpha_C}\,\Gamma(\alpha_C)}\, C_0^{\alpha_C - 1}\, e^{-C_0/\beta_C} \tag{2}$$
- Initial battery energy (Eq. 3):
$$E_0^i = C_0^i \times SOC_0^i \tag{3}$$
- Temperature-/speed-dependent energy consumption per km (regression model adopted from [16]) (Eq. 4):
$$e_0 = b + v_1 v + v_2 v^2 + c_e^T P_e + a A + h_e H_e + t_1 T + t_2 T^2 + t_3 T^3 \tag{4}$$
where $e_0$ = energy consumption per km, $v$ = average travel speed, $P_e$ = percentage of link length with gradient, $A$, $H_e$ = AC/heater usage times per km, $T$ = ambient temperature.
- Remaining battery after driving distance $l_i$ (sampled log-normal) (Eq. 5):
$$E_i = E_0^i - e_0^i \times l_i \tag{5}$$
- Charging power with range-anxiety rule (Eq. 6); base power sampled $P_{char}^i \sim U(4.5, 5.5)$ kW [17]; range-anxiety coefficient $a_1^i \in [0.15, 0.3]$:
$$P_{char}^i = \begin{cases} P_{char}^i \text{(kW)} & \text{if } E_i < a_1^i \times C_0^i \\ 0 & \text{otherwise} \end{cases} \tag{6}$$
- Charging duration (battery capped at 0.8 of full capacity) (Eq. 7):
$$T_C^i = \frac{0.8 \times C_0^i - E_i}{P_{char}^i} \tag{7}$$
- Total EV charging load = sum over all $N_{EV}$ vehicles (Eq. 8):
$$P_{EV}(t) = \sum_{i=1}^{N_{EV}} P^i(t) \tag{8}$$

### B. Input features
- $HD(t)$: hour of day ∈ {1,…,24}; $DW(t)$: day of week ∈ {1,…,7}; $DY(t)$: day of year ∈ {1,…,365}; $MY(t)$: month ∈ {1,…,12}.
- $T(t)$: temperature at t (Gaussian noise added to simulate weather-forecast error); $TH(t)$: temperatures of past 24 h $\{T_{t-24},…,T_{t-1}\}$.
- $PH(t)$: historical load of past 24 h $\{p_{t-24},…,p_{t-1}\}$.
- $CH(t)$: **charging-habit feature** — probability of charging at time t (obtainable via questionnaires or historical EV charging data). ← the key novel feature.

### C. Gaussian Process Regression
- Load modeled as a draw from a GP (Eq. 9):
$$p(x) \sim GP(\mu(x_t),\, k(x_t, x_t')) \tag{9}$$
- Squared Exponential covariance kernel (Eq. 10):
$$k(x_t, x_t') = \sigma^2 \exp\!\left(-\frac{\|x_t - x_t'\|^2}{2\lambda^2}\right) \tag{10}$$
- Joint Gaussian over n training points (Eqs. 11–12):
$$P(x) \sim \mathcal{N}(\mu, \Sigma) \tag{11}$$
$$\mu = \begin{bmatrix} \mu(x_1) \\ \vdots \\ \mu(x_n) \end{bmatrix}, \qquad \Sigma = \begin{bmatrix} K(x_1,x_1) & \cdots & K(x_1,x_n) \\ \vdots & \ddots & \vdots \\ K(x_n,x_1) & \cdots & K(x_n,x_n) \end{bmatrix} \tag{12a,b}$$
- Conditioning joint train/test distribution (Eq. 13):
$$\begin{bmatrix} p(x_1) \\ \vdots \\ p(x_n) \\ p(x_t) \end{bmatrix} \sim \mathcal{N}\!\left( \begin{bmatrix} \mu \\ \mu_t \end{bmatrix}, \begin{bmatrix} \Sigma & \Sigma_{Nt} \\ \Sigma_{Nt}^T & \Sigma_{tt} \end{bmatrix} \right) \tag{13}$$
- Posterior predictive via Bayes' theorem (Eq. 14), with $\mu(x_t)=\Sigma_{Nt}^T\Sigma^{-1}P_x$ and $\sigma(x_t) = \Sigma_{tt} - \Sigma_{Nt}^T\Sigma^{-1}\Sigma_{Nt}$:
$$p(x_t)\,|\,P_x \sim \mathcal{N}(\mu(x_t), \sigma(x_t)) \tag{14}$$
- **Day-ahead iterative scheme:** predicted $\hat{p}(x_t)$ is fed back into the input to predict $p(x_{t+1})$, repeated hour-by-hour across the day.

## 📊 Dataset & Input Features
- **Residential load:** real smart-meter data from a **U.S. utility feeder** with **>100 residential customers**; feeder load $P_R(t)$ = sum of customer meters (losses neglected); **EV-free** feeder. History: **3 years**, resolution: **1 hour**.
- **EV charging load:** charging profiles for **30 EVs**, sampled from the KDE/statistical model built on **real-world EV charging load profile data collected from the nearby area** (see Eqs. 1–8). Training split: **22 consecutive months**; testing: following **2 months**.
- Weather information joined by timestamp (used for $T(t)$, $TH(t)$).
- ⚠️ **No public URLs/download links appear anywhere in the PDF text** (data described as real-world/utility-provided; none published).

## 📈 Performance & Results
Three cases (same GPR): **Case 1** = EV-free load forecast (features: time indices, $PH$, $T$, $TH$); **Case 2** = load including EVs, same features; **Case 3** = Case 2 + charging-habit feature $CH(t)$.

**Table I — Deterministic metrics (verified verbatim):**

| Case | MAPE | RMSE |
|---|---|---|
| 1 (no EVs) | 9.0714% | 12.0494 |
| 2 (with EVs, no CH) | 21.3612% | 25.6835 |
| 3 (with EVs + CH(t)) | 9.2057% | 12.5291 |

Key finding: adding EV loads more than doubles MAPE (9.07% → 21.36%); the single $CH(t)$ feature restores accuracy to near EV-free levels (9.21%).

**Fig. 3 — PI quality (read from bar-chart labels in extracted text; grouping by confidence interval inferred from the paper's narrative — treat individual assignments as approximate, extracted from figure annotations):**
- **PICP (%):** CI-68%: 67.8 (Case 1) / 50.4 (Case 2) / 73.6 (Case 3); CI-95%: 90.8 / 84.6 / 93.8; CI-99.7%: 97.5 / 95.5 / 98.5. Ideal values: 68 / 95 / 99.7. Case 3 closest to ideal; Case 2 far below.
- **NMPIL:** CI-68%: 0.24 / 0.4 / 0.27; CI-95%: 0.48 / 0.8 / 0.54; CI-99.7%: 0.71 / 1.2 / 0.81. Case 2 produces the widest intervals yet worst coverage.
- **CLC:** CI-68%: 0.484 / 13.9 / 0.357; CI-95%: 1.57 / 7.24 / 1.21; CI-99.7%: 1.83 / 3.98 / 1.83. Cases 1 & 3 ≪ Case 2 → far more reliable PIs.
- Fig. 2 (one test week, ±2σ PIs, ideal PICP 95%): Case 2 PIs are visibly longer yet cover fewer true points; Case 3 PIs are shorter and encompass most points.

## 💡 Limitations & Identified Research Gaps
- Single feeder, hourly resolution, ~2-month test window — generalization to other feeders/geographies/resolutions untested.
- EV charging loads for only 30 vehicles, synthetically sampled from a statistical (KDE/Gamma/log-normal/uniform) model rather than directly measured per-EV metering.
- GPR scales poorly to large training sets (kernel-matrix inversion); authors do not discuss computational cost or sparse/variational GP variants.
- Day-ahead recursive scheme feeds predictions back as inputs → potential multi-hour error accumulation (not quantified).
- PI construction relies on GP Gaussianity assumption; no comparison against quantile-regression or conformal alternatives; no pinball/Winkler scoring.
- Gap: richer charging-behavior modeling, higher-resolution (sub-hourly) probabilistic forecasting, and benchmarking against QR/deep probabilistic methods (cf. [[2017_QRA_Sister_Forecasts_Probabilistic_Load]], [[2025_QR_LSTM_Attention_EV_Load]], [[2021_Probabilistic_Queuing_EV_Load]]).

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{shi2024short,
  title     = {Short-term Load Forecasting Considering {EV} Charging Loads with Prediction Interval Evaluation},
  author    = {Shi, Naihao and Zhang, Feixiang and Wang, Zhaoyu and MacDonald, Jason S. and Baudette, Maxime and Lin, Yashen and Motakatla, Venkateswara},
  booktitle = {2024 56th North American Power Symposium (NAPS)},
  year      = {2024},
  organization = {IEEE},
  doi       = {10.1109/NAPS61145.2024.10741734}
}
```

## 🔗 Key References & Citation Graph
- **Probabilistic line:** [[2017_QRA_Sister_Forecasts_Probabilistic_Load]] · [[2025_QR_LSTM_Attention_EV_Load]] · [[2021_Probabilistic_Queuing_EV_Load]]
- **Metrics:** [[PICP]] · [[Pinball_Loss]] · [[RMSE]] · [[MAPE]]
- **In-paper citations of interest:** [3] Hong & Fan, probabilistic LF tutorial review (IJF 2016); [8] Wang et al., combining probabilistic forecasts (TSG 2019); [13] Schulz et al., GPR tutorial; [16] Liu et al., EV energy consumption vs temperature (Applied Energy 2018); [17] Zhang et al., daily EV charging profiles (Applied Energy 2020); [18] **Khosravi et al., optimal prediction interval construction (TPWRS 2010)** — source of NMPIL/PICP/CLC framework.
