---
type: paper
title: "Adaptive Conformal Predictions for Time Series"
authors: [Margaux Zaffran, Olivier Féron, Yannig Goude, Julie Josse, Aymeric Dieuleveut]
year: 2022
journal_conference: "ICML 2022; arXiv:2202.07282"
doi_url: "https://arxiv.org/abs/2202.07282"
status: metadata-verified-2026-08
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Brings **conformal prediction** to non-exchangeable time series: proposes **AgACI (Aggregated Adaptive Conformal Inference)**, combining multiple online conformal interval controllers (building on Gibbs & Candès' ACI) so the miscoverage rate tracks a target level automatically under distribution shift.
- Adds a practical contribution for realistic pipelines: an imputation-aware variant handling **missing values** in the target series without breaking validity.

## 🧠 Methodology & Model Architecture
- Base point forecasters (e.g., sequential GAM/ML models) produce point predictions; ACI-style controllers adjust the interval radius online via feedback on recent coverage errors; AgACI runs several controllers with different learning rates and aggregates them with online expert aggregation (BOA-flavoured).
- Theory: validity guarantee maintained step-by-step even under arbitrary distribution drift, given only exchangeability-free coverage accounting.

## 📈 Performance & Results
- Experiments on French electricity demand (industrial-scale, incl. the COVID-19 disruption period) show AgACI maintains near-nominal coverage where static conformal intervals under-cover, while keeping intervals competitive in width; the missing-data variant remains valid on gappy real smart-meter streams.

## 💡 Limitations & Identified Research Gaps
- Adaptation speed vs stability trade-off controlled by controller learning rates; conditional coverage (per-time-step guarantees) beyond marginal validity remains open — connects to CQR/conformalized quantile regression lines (cf. [[Conformal_Prediction]]).

## 📚 BibTeX & Citation Reference
- M. Zaffran, O. Féron, Y. Goude, J. Josse, A. Dieuleveut, "Adaptive Conformal Predictions for Time Series," ICML 2022; arXiv:2202.07282. Code: github.com/mzaffran/adaptiveconformaltimeseries
