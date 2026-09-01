---
type: paper
title: "Additive Models and Robust Aggregation for GEFCom2014 Probabilistic Electric Load and Electricity Price Forecasting"
authors: [Pierre Gaillard, Yannig Goude, Raphaël Nedellec]
year: 2016
journal_conference: "International Journal of Forecasting 32(3):1038-1050"
doi_url: "https://doi.org/10.1016/j.ijforecast.2015.12.001"
status: metadata-verified-2026-08
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Describes **team Tololo's methodology** for both probabilistic tracks (electric load and electricity price) of **GEFCom2014**: semi-parametric quantile GAMs combined with **robust online aggregation of experts**, forming the statistical backbone later reused across EDF forecasting systems.

## 🧠 Methodology & Model Architecture
- **Load track**: two-step scheme — first simulate probabilistic temperature scenarios, then plug them into a **quantile generalized additive model (quantGAM)** with nonlinear weather/calendar effects to yield load quantiles.
- **Price track**: three approaches explored, settling on aggregating 13 heterogeneous expert predictors (AR, TAR, ARX, TARX, spike-preprocessed PAR, GAM, random forests, gradient boosting machines) using **ML-Poly-style robust sequential aggregation** under the quantile loss, with weights allowed to vary over time (extending Nowotarski & Weron 2015).

## 📈 Performance & Results
- Top-tier finishes in both GEFCom2014 tracks; the aggregation consistently improved upon any individual expert, demonstrating the practical value of sequential expert mixing under the pinball loss.

## 💡 Limitations & Identified Research Gaps
- Expert-set design is manual; temperature-scenario simulation drives load-track uncertainty. Direct descendants: the `opera` R package ([[Wintenberger2017_BOA]] theory) and net-load aggregation work by the same group.

## 📚 BibTeX & Citation Reference
- P. Gaillard, Y. Goude, R. Nedellec, "Additive models and robust aggregation for GEFCom2014 probabilistic electric load and electricity price forecasting," *International Journal of Forecasting*, 32(3):1038-1050, 2016. DOI:10.1016/j.ijforecast.2015.12.001
