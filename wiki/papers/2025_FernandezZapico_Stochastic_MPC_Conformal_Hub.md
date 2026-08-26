---
type: paper
title: "Stochastic Model Predictive Control of Charging Energy Hubs with Conformal Prediction"
authors: ["Diego Fernandez-Zapico", "Theo Hofman", "Mauro Salazar"]
year: 2025
journal_conference: "IEEE Conference on Decision and Control (CDC 2025)"
doi_url: https://doi.org/10.1109/CDC57313.2025.11311970
arxiv: "arXiv:2504.00685"
models_used: ["[[XGBoost]] (Scikit-learn GradientBoostingRegressor, MAE loss, early stopping)", "[[EnbPI]] conformal wrapper (MAPIE implementation)", "[[Stochastic_MPC]] scenario-based SOCP"]
datasets_used: ["simulated Charging Energy Hub (simulated) w/ publicly available real EV charging demand data (Gholizadeh & Musilek, Data in Brief 2024)", "NREL OpenEI/PVDAQ Farm Solar Array PV data (California)", "ENTSO-E Transparency Platform NL day-ahead prices + CO2", "Open-Meteo.com Weather API (NOAA HRRR historical weather forecasts)"]
features_used: ["historical load/PV/prices (lagged daily sum & std, lagged intraday 6-h sum)", "weather forecasts (direct/diffuse radiation, temperature, wind speed)", "sun position (zenith angle, solar time)", "calendar (month, day-of-week, arrival hour, hour)", "exogenous normalized 24-h differences of national electricity demand and national solar+wind generation"]
forecasting_horizon: "day-ahead 24 h @ 15 min (load/PV, Nwq=96; price 24 h @ 1 h, Nwh=24, upsampled to 15 min) -> [[Day_Ahead_Forecasting]]"
metrics: ["normalized average daily operational cost (% vs Omniscient)", "daily net CO2 emissions (%)", "interval coverage CPI_alpha=0.1 ([[PICP]]-type)", "normalized MAE (nMAE)"]
tags: [paper, ev-load-forecasting, conformal-prediction, mpc, energy-hub]
---

# Stochastic Model Predictive Control of Charging Energy Hubs with Conformal Prediction

**Fernandez-Zapico, Hofman & Salazar — TU/e Control Systems Technology — IEEE CDC 2025** · [DOI](https://doi.org/10.1109/CDC57313.2025.11311970) · [arXiv:2504.00685](https://arxiv.org/abs/2504.00685) · Code: https://github.com/diegofz/ChargingEnergyHubs_MPC

## 🎯 Main Objective & Contribution
Online energy management system (EMS) for an energy hub combining EV charging, on-site PV, battery energy storage (BESS) and grid connection, minimizing operational cost. First published EMS leveraging state-of-the-art ML forecasters with **calibrated distribution-free uncertainty intervals via conformal prediction**: a probabilistic prediction module for 24-h-ahead EV charging load (Pev), PV generation (Ppv) and day-ahead electricity prices (pel) built on Gradient-boosted Trees wrapped by EnbPI, feeding two scenario-based stochastic MPCs evaluated closed-loop over 280 days against deterministic point-forecast and perfect-forecast (omniscient) baselines.

## 🧠 Methodology & Model Architecture
- **Point forecaster**: GBT additive model F(x)=F0(x)+Σ ν·ρm·hm(x) trained on absolute error (linear cost justification, following Lago et al.), early stopping on validation set (Scikit-learn `GradientBoostingRegressor`).
- **Conformal wrapper**: EnbPI produces calibrated distribution-free prediction intervals from any model without uncertainty quantification, using leave-one-out (LOO) ensemble residuals (MAPIE library):
$$\widehat{\mathrm{PI}}_{\alpha}(x) \;=\; \hat{F}^{\,\phi}(x) \,\pm\, \mathrm{quantile}_{(1-\alpha)}\!\left(\hat{\epsilon}^{\,\mathrm{LOO}}\right)$$
*(reconstructed from PDF-extracted Eq. (13): "PIα(x) = F̂φ(x) ± (1−α) quantile(ε̂LOO)", where F̂φ is the mean of LOO estimators and ε̂LOO the absolute LOO residuals |Y − F̂LOO(x)|; hats/subscripts were mangled in extraction.)*
- **Scenario tree**: ns = 3 scenarios per variable (mean F̂φ, 5th, 95th percentiles), nv = 3 variables (Pev, Ppv, pel), assuming **independence between variables** → Ns = 27 equally probable branches (ρs = 1/Ns).
- **Controllers**: scenario-based stochastic MPC solving a **second-order cone program (SOCP)** at every step (quadratic BESS loss relaxed to conic constraint; convex grid-cost relaxation). Two variants: **Stochastic MPC** (control equal across scenarios for whole receding window R={0,…,95}) vs **Recourse MPC** (nonanticipativity relaxed to first step R={0}). Benchmarks: **Deterministic** (point estimate, Ns=1) and **Omniscient** (perfect forecast). Periodic battery constraint Eb,0=Eb,Nep for fair episodes.
- Price treated as a real-time signal (no auction assumption), forecast on 24-h differences with exogenous national demand/generation forecasts.

## 📊 Dataset & Input Features
- Closed-loop simulated hub: peak EV power max(Pev)=160 kW, peak PV max(Ppv)=70 kW, BESS limits 10–90 kWh initialized at 25 kWh; ΔT=0.25 h; episodes Nep=96 steps.
- **Data sources** (all 2021, test set = 70 days/season = 280 evaluation days; both EV & PV sites located in California, USA per text):
	- Pev: public daily EV charging dataset of Gholizadeh & Musilek (Data in Brief, vol. 55, 110587, 2024) [ref 16]
	- Ppv: NREL OpenEI / PVDAQ "Farm Solar Array" site — https://openei.org/wiki/PVDAQ/Sites/Farm Solar Array
	- pel + CO2: ENTSO-E Transparency Platform (Netherlands) — https://transparency.entsoe.eu/
	- Weather forecast features: NOAA High-Resolution Rapid Refresh (HRRR) via Open-Meteo.com Weather API — https://open-meteo.com
- Features: PV — weather forecast vars, sun position, month, lagged daily power sum/std; EV — month/day-of-week/arrival hour, lagged daily sum/std, lagged 6th-hour intraday sum (→ recursive multi-step forecasting); price — calendar, lagged daily std, exogenous normalized 24-h differences of national load Pload and national solar+wind generation Pgen.

## 📈 Performance & Results
- Forecast quality (280-day test): nMAE all-season Pev 0.106, Ppv 0.057, pel 0.098 (price degrades sharply in Autumn: 0.228, blamed on the 2021 gas-price regime change in the day-ahead market).
- Coverage (CPI, α=0.1): Pev 0.90, Ppv 0.91, **pel 0.60 overall (Autumn 0.22)** — price interval badly miscovered late in year, i.e., static calibration fails under regime shift.
- Cost (normalized to Omniscient=100 %): Deterministic 113.65, **Stochastic 112.76, Recourse 112.77** → scenario-based MPCs are **13 % pricier than perfect forecast**, only **~0.9–1 % better than deterministic point-forecast**.
- CO2 (normalized): Deterministic 101.40 % vs Stochastic/Recourse 101.13 % (−0.3 %).
- Runtime: avg per episode Stochastic **0.743 min (< 0.75 min, far below ΔT·96 budget)**, Recourse 0.604, Deterministic 0.321, Omniscient 0.043 min.

## 💡 Limitations & Identified Research Gaps
- **Static EnbPI calibration is not adaptive/covariate-aware**: price coverage collapses to 0.60 (0.22 in Autumn) under the 2021 regime change — motivates online/weighted conformal recalibration.
- **Simulation only**: closed-loop simulated environment, no hardware/real-time deployment; authors suggest future work on jointly optimizing charging power levels and schedules of individual vehicles (vs aggregated demand).
- **Independence assumption between variables** when building the scenario tree (Pev × Ppv × pel cross-correlations ignored); equal scenario probabilities ρs = 1/Ns rather than learned.
- Point estimates already yield acceptable control performance → value of probabilistic forecasts must be argued via downstream control benefit (marginal here).

## 📚 BibTeX
```bibtex
@inproceedings{2025_FernandezZapico_Stochastic_MPC_Conformal_Hub,
  title     = {Stochastic Model Predictive Control of Charging Energy Hubs with Conformal Prediction},
  author    = {Fernandez-Zapico, Diego and Hofman, Theo and Salazar, Mauro},
  booktitle = {IEEE Conference on Decision and Control (CDC)},
  year      = {2025},
  doi       = {10.1109/CDC57313.2025.11311970},
  url       = {https://doi.org/10.1109/CDC57313.2025.11311970},
  note      = {arXiv:2504.00685}
}
```

## 🔗 Key References & Citation Graph
- [[2024_Bampos_EV_Load_Forecasting_DAM]] — cited [7]: systematic day-ahead EV load forecasting review; XGBoost/MLP best performers make no distributional assumptions → motivates GBT base model here.
- Xu & Xie (2021), *Conformal prediction interval for dynamic time-series* (EnbPI), PMLR — methodological foundation ([10]; no dedicated vault page yet, see [[EnbPI]]).
- Lago, Marcjasz, De Schutter & Weron (2021), day-ahead electricity price forecasting review, Applied Energy — feature/best-practice source for pel ([8]).
- Yang, Xia & Mayer (2024), solar power curve tutorial review, Adv. Atmos. Sci. — PV feature engineering ([9]).
- *Note:* [[2021_Stankeviciute_Conformal_Time_Series_Forecasting]] is **not** cited by this paper (linked here only as vault context for conformal time-series lineage).
