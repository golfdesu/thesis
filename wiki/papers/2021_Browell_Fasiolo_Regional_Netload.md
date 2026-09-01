---
type: paper
title: "Probabilistic Forecasting of Regional Net-Load With Conditional Extremes and Gridded NWP"
authors: [Jethro Browell, Matteo Fasiolo]
year: 2021
journal_conference: "IEEE Transactions on Smart Grid 12(6):5011-5019"
doi_url: "https://doi.org/10.1109/TSG.2021.3107159"
status: metadata-verified-2026-08
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Produces **probabilistic forecasts of regional net-load** (transmission-level demand minus embedded wind/solar generation) with particular attention to the **tails** of predictive distributions, which drive risk decisions such as reserve procurement.
- Novel combination: best-in-class load forecasting methodology adapted to net-load, plus **conditional Generalised Pareto Distribution (cGPD)** tails whose scale parameter varies smoothly with covariates, plus features derived from **gridded NWP**.

## 🧠 Methodology & Model Architecture
- Additive quantile regression framework (GAMLSS-style) for central quantiles; tails modelled by GPD with log-link scale conditioned on expected net-load, 100 m wind speed and surface solar irradiance; shape parameter held constant.
- Evaluated on Great Britain Grid Supply Point Groups (14 regions), half-hourly metered, five years 2014-2018 — a period when embedded solar grew 3 GW → 13 GW.

## 📈 Performance & Results
- Conditional tails produce calibrated and sharper forecasts than unconditional/static-tail benchmarks.
- In a reserve-setting use case, cGPD reduces upward reserve volume by up to **24.6%** and downward reserve by up to **10.8%** at probability levels 0.01%-0.25%, while correctly identifying high-risk periods missed by static approaches.
- Gridded NWP features added little value within this framework compared with station/NWP-point features.

## 💡 Limitations & Identified Research Gaps
- Tail modelling needs sufficient extremes; shape-parameter constancy may fail under structural change. Reserve-simulation is GB-specific. Extension to joint/net-load-plus-generation distributions is open.

## 📚 BibTeX & Citation Reference
- J. Browell, M. Fasiolo, "Probabilistic Forecasting of Regional Net-Load With Conditional Extremes and Gridded NWP," *IEEE Transactions on Smart Grid*, 12(6):5011-5019, 2021. DOI:10.1109/TSG.2021.3107159; preprint arXiv:2103.10335; data DOI:10.5281/zenodo.4618056
