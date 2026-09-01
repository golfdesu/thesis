---
type: paper
title: "A Scalable Stochastic Model for the Electricity Demand of Electric and Plug-In Hybrid Vehicles"
authors: [Mahnoosh Alizadeh, Anna Scaglione, Jamie Davies, Kenneth S. Kurani]
year: 2014
journal_conference: "IEEE Transactions on Smart Grid, 5(2), 848-860"
doi_url: "https://doi.org/10.1109/TSG.2013.2275988"
models_used: ["[[Queuing_Model]]", "[[Factor_Model]]", "[[ARIMA]]", "[[Kalman_Filter]]", "[[EM_Algorithm]]", "[[Persistence_Model]]"]
datasets_used: ["[[UC_Davis_PH_EV_Center_Data]]", "[[NHTS_2009]]"]
features_used: ["[[EV_Arrival_Rate]]", "[[Charging_Duration]]", "[[Charging_Power]]", "[[Laxity_Slack_Time]]", "[[Daily_Mileage]]", "[[Calendar_Features]]", "[[Submetering_Triplets]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[Absolute_Error_kW]]", "[[Kolmogorov_Smirnov_Test]]", "[[Log_Likelihood]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Scalable Stochastic Model for EV/PHEV Electricity Demand

## 🎯 Main Objective & Contribution
- Proposes a **queueing-theoretic stochastic model** ([[Queuing_Model|M/G/∞ queueing model]]) for aggregate EV/PHEV charging demand that yields: (1) more accurate **short-term forecasts with uncertainty** when real-time sub-metering data is available; (2) a mathematical description of load **plus demand flexibility** at wholesale level, useful for [[Demand_Response]] and dynamic pricing design.
- Answers four essential behavioral questions from real data: when vehicles arrive at chargers, how often parked customers request charge, energy required per charge event, and flexibility (laxity) per request.
- Adds **scalability**: quantized ("digital") sub-metering classifies each charge request into $L\times K$ service classes so only class counts per epoch need storage/communication, independent of vehicle-population size.
- Validates statistics on real PHEV home-charging data and shows the resulting forecasting method beats classical univariate load prediction.

## 🧠 Methodology & Model Architecture
### Uncontrolled load model (Section II)
- $L$ parallel $M_t/G_t/\infty$ service systems (one per charging rate $r$, e.g., 1.1 kW level-1, 3.3/6.6 kW level-2); arrivals are **non-homogeneous Poisson processes** with time-varying rate $\lambda^{(r)}(t)$; service times (charge durations) i.i.d. with CDF $F^{(r)}(t,\tau)$; no queue ever forms.
- **Aggregate Charging Load (Eq. 1)**:
$$P(t) = \sum_{r=1}^{L} \mathcal{P}_r\, n^{(r)}(t)$$
with $\mathcal{P}_r$ the charging power of rate $r$ and $n^{(r)}(t)$ the number of vehicles being served.
- **Expected Number in Service / Poisson Mean (Eq. 2, Mt/G/∞ result from Palm/Khinchin/Eick et al.)**:
$$\mathbb{E}\big[n^{(r)}(t)\big] = \int_{0}^{t} \lambda^{(r)}(\tau)\left(1 - F^{(r)}(t-\tau)\right)d\tau$$
— sums expected arrivals at $\tau$ still receiving service at $t$. Hence day-ahead aggregate load (Eq. 3) is a **sum of scaled Poisson random variables** with time-varying means.
- **Rate-based demand response (Eqs. 4)**: pricing incentives modify arrival rates through an empirically learned mapping $\tilde{\boldsymbol\lambda}(t) = \mathcal{G}(\boldsymbol\lambda(t))$ (possibly nonlinear, with memory); Eqs. 2–3 then map $\tilde\lambda$ to load.
### Real-time forecasting: Observable Arrival Information (OAI) predictor (Section II-C)
- Sub-metering reveals each plugged-in vehicle's $(r_i, t_i, d_i)$ triplet (queue index, arrival time, charge duration) ⇒ remaining service is **deterministic**; only new arrivals between now ($t_0$) and horizon $t$ are uncertain.
- **OAI Predictor (Eq. 5)**: $n^{(r)}(t) = \hat{n}^{(r)}(t_0, t) + \tilde{n}^{(r)}(t)$, where $\tilde{n}$ is Poisson with mean of Eq. 2 (integral truncated at $t_0$), and the deterministic term (Eq. 6):
$$\hat{n}^{(r)}(t_0,t) = \sum_{i:\,a_i < t_0} \mathbb{1}\{a_i + d_i > t\}$$
over observed arrivals $\mathcal{A}_{t_0}$ (unit-step indicator). Real-time load forecast (Eq. 7): $\hat{P}(t)=\sum_r \mathcal{P}_r\big(\hat{n}^{(r)}+\tilde{n}^{(r)}\big)$.
### Learning arrival-rate statistics (Section III)
- Counts are Poisson with time-varying mean ⇒ **variance-stabilizing transform (Eq. 8)**: slightly modified **Anscombe square-root transform** maps counts to approximately Gaussian data with constant variance $1/4$: $y = \sqrt{c + 3/8}$-type transform applied per epoch.
- Day divided into $m$ epochs (quarter/half hours); rate vector per day $\boldsymbol\lambda_d$. **Low-dimensional factor model (Eqs. 9–10)**: transformed rates $\mathbf{x}_d = U\mathbf{z}_d$ (PCA/SVD factors, time-invariant $U$, slow dynamics).
- Each factor follows an **AR(1) with weekly periodic mean (Eqs. 11–12)**:
$$z_{k,d} - \bar{z}_{k,d} = \phi_k\,(z_{k,d-1} - \bar{z}_{k,d-1}) + w_{k,d}$$
white noise uncorrelated across factors; combined into linear-Gaussian **state-space dynamics (Eqs. 13–14)** estimated adaptively by standard **Kalman filter** predict/update steps; parameters learned via **expectation–maximization**, initialized with leading singular vectors, refined by recursive subspace tracking.
- **Intraday updating**: direct estimation of latent factors from realized counts (Eq. 15), plus **penalized updating** (weighted blend of direct estimate and day-ahead forecast) when count data are sparse.
### Quantized submetering & controlled activations (Section IV)
- Classifiers quantize durations into $K$ levels ⇒ classes $(r,k)$; load reconstructed from class-arrival counts with unit pulses (Eqs. 17–18); only $LK$ numbers stored per epoch regardless of population size. Directly-controlled charging modeled by activation function $\beta$ rewriting load (Eq. 19), extensible toward V2G.

## 📊 Dataset & Input Features
- **[[UC_Davis_PH_EV_Center_Data]]** — real-world PHEV level-1 home-charging data from households, provided by the UC Davis PH&EV center (Kurani et al., *Learning from consumers*, Res. Rep. UCD-ITS-RR-10-21 [11]); **620 charging samples** (charge durations & laxity); full charge 4–6 kWh ⇒ 4–5 h at average ≈ 1.1 kW; used for duration/laxity PDFs and a small-scale arrival test.
- **[[NHTS_2009]] (NHTS)** — US DOT/FHWA ICEV daily travel patterns (mode, duration, distance, purpose), mapped into synthetic PHEV charge requests via miles→kWh conversion; **~150,000 derived charging amounts** used to learn arrival-rate statistics and principal components.
  - Data URL stated in the paper: **`http://nhts.ornl.gov`**
- Simulation testbed: substation serving **≈1000 PHEVs**, all level-1 (1.1 kW); **60 simulated days** (30 train / 30 test); peak daily EV charging load ≈ 250 kW.
- Input features: arrival times (5-min-rounded trip ends, dithered with N(0, 2 min²)/N(0,15 min²) noise for multiples of 5/30 min), daily mileage, plug-in decision (Bernoulli, probability increasing in miles driven since last charge; threshold model with 5-mile cutoff), charge rate, charge duration, battery capacity, parking duration, day-of-week periodic mean.
- Other links found in text: IEEE Xplore `http://ieeexplore.ieee.org`; Hadley & Tsvetkova [20] `http://www.sciencedirect.com/science/article/pii/S104061900900267X`; Kalman filter intro [28] `http://www.cs.unc.edu/~welch/media/pdf/kalman_intro.pdf`; paper DOI `10.1109/TSG.2013.2275988`. No public code/data repository for the authors' own dataset.

## 📈 Performance & Results
- **Fitted statistics**: charge duration best fit by a **clipped lognormal distribution (Eq. 20)** with expected value **207 minutes** (clip at 320 min improves q-q fit); laxity bimodal — daytime requests: **exponential, mean 1.089 (hours)**; nighttime: lognormal; duration and laxity acknowledged correlated but joint density not estimable from data.
- **Plug-in behavior**: with mileage-dependent plug-in probability (Eq. 23), a two-sample Kolmogorov–Smirnov test does **not reject** (5% significance) that the 620 real samples and 150,000 NHTS-derived charges share one distribution; constant-probability alternative (geometric $D$, Eq. 24) fitted by maximizing likelihood of the 620 PH&EV samples; naive every-night charging (Eq. 21) yields implausible short durations (~40% very short) — rejected against real data.
- **Poisson validation**: conditional-uniformity (Barnard/Lewis) tests via one-sample KS on normalized arrival times per half-hour interval — null hypothesis never rejected (e.g., Monday 13:30–14:00 q-q plot uniform).
- **Dimensionality**: first **six principal components capture 96% of variance** of weekly arrival-count profiles (96 → 6 features/day); PC1 ≈ weekday pattern, later PCs capture weekend deviations.
- **Forecasting (half-hour ahead)**: OAI1 (non-homogeneous arrivals) absolute error up to **3–4× lower than the classical ARMA baseline**; OAI2 (homogeneous arrivals à la Li & Zhang [9]) clearly inferior to OAI1 ⇒ non-homogeneous arrival modeling necessary. When arrivals become volatile (PH&EV events with persistence rate forecast), the classic predictor degrades far more than the OAI predictor, which retains zero error on already-plugged-in load.

## 💡 Limitations & Identified Research Gaps
- Model valid only for **large populations** (rate-function assumption breaks at single-feeder/few-house scale); suitable for substations and charging stations, not individual dwellings.
- No **geographical/spatial information** (grid topology, transformer limits, location-based CO₂ accounting) — explicitly deferred to future work.
- Arrival statistics could not be learned from the small (620-sample) real dataset — NHTS mapping needed; NHTS entries cover only one travel day per household and cannot encode expectation-of-next-day-travel charging decisions; ICEV-derived behavior may diverge further as EV adoption changes household activity/travel patterns.
- Charge-duration PDF treated stationary though real data suggest non-stationarity (night vs. day); tapering charging power ignored (constant average rate assumed); serial correlation of daily mileage ignored.
- V2G discharge scheduling within the queuing framework sketched but left open; aggregator control functions $\beta$ must be learned from historical data.
- Authors stress all parameter estimates should be re-evaluated as larger multi-day EV datasets emerge — the gap later filled by data-driven deep-learning forecasters.

## 📚 BibTeX & Citation Reference
```bibtex
@article{alizadeh2014scalable,
  title   = {A Scalable Stochastic Model for the Electricity Demand of Electric and Plug-In Hybrid Vehicles},
  author  = {Alizadeh, Mahnoosh and Scaglione, Anna and Davies, Jamie and Kurani, Kenneth S.},
  journal = {IEEE Transactions on Smart Grid},
  volume  = {5},
  number  = {2},
  pages   = {848--860},
  year    = {2014},
  doi     = {10.1109/TSG.2013.2275988}
}
```

## 🔗 Key References & Citation Graph
- Li & Zhang (2012) [9] — homogeneous-Poisson PHEV charging demand model improved upon here (OAI2 baseline)
- Eick, Massey & Whitt (1993) [17], Palm [18], Khinchin [19] — $M_t/G/\infty$ queue theory underpinning Eq. 2
- Brown et al. call-center arrival forecasting [23]; Shen & Huang factor-model interday/intraday updating [24] — source of the PCA + AR(1) + Kalman methodology
- Wu, Aliprantis & Gritzka [7]; Taylor et al. [8] — ICEV-to-synthetic-EV trace mapping emulated for NHTS
- Kurani et al. UCD-ITS-RR-10-21 [11]; Turrentine et al. MINI E study [33] — source of real PHEV behavior data
- Anscombe (1948) [26] — variance-stabilizing transform
- Vault context:
  - [[2021_Zhang_Probabilistic_Queuing_EV_Load]] — deep-learning successor of this queuing approach
  - [[2014_Kingma_Adam_Stochastic_Optimization]] — optimization tooling for the neural models that later replaced analytical arrival models
  - [[2021_VanKriekinge_Day_Ahead_EV_Demand]] — day-ahead EV charging demand forecasting line
  - [[2024_Xu_Day_Ahead_EVCB_EVSC_Parking_Lot]] — day-ahead charging-behavior/schedulable-capacity forecasting

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2014_Alizadeh_Scalable_Stochastic_EV_Demand_refs]]
