---
type: paper
title: "Adaptive Methods for Short-Term Electricity Load Forecasting During COVID-19 Lockdown in France"
authors: [Dustin Obst, Jacob Vilmarest, Yannig Goude]
year: 2021
journal_conference: "IEEE Transactions on Power Systems 36(6):5359-5370"
doi_url: "https://arxiv.org/abs/2101.05845"
status: metadata-verified-2026-08
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Addresses the collapse of standard short-term load forecasting models during the **COVID-19 lockdown in France** (spring 2020), when consumption patterns shifted abruptly (~15% demand drop with strong regional heterogeneity).
- Compares and combines **adaptive methods**: exponential smoothing variants, Kalman-filter-based state-space adaptation of GAMs and machine-learning models, and online aggregation of experts — providing practical guidance for forecasting through regime change.

## 🧠 Methodology & Model Architecture
- Baseline GAM with weather/calendar decomposition (the industrial EDF-style model) is linearised and embedded in a **linear-Gaussian state-space model**, so its coefficients are tracked over time by Kalman filtering with break/forget settings tuned to adapt faster than classical smoothing.
- The same adaptation wrapper is applied to other learners (e.g., random forests retrained incrementally), and experts are aggregated sequentially for robustness.

## 📈 Performance & Results
- On French national/regional load spanning the lockdown, adaptive state-space versions recover forecast accuracy far faster than non-adaptive benchmarks; Kalman-adapted GAM is among the strongest single models, and expert aggregation stabilises performance across regions and periods.

## 💡 Limitations & Identified Research Gaps
- Break detection/adaptation speeds are hand-set; the approach reacts after a regime shift begins rather than anticipating it. Follow-up work (VIKING variance tracking; the post-COVID competition win) directly extends this paper — see [[2022_Vilmarest_Goude_State_Space_PostCOVID]].

## 📚 BibTeX & Citation Reference
- D. Obst, J. de Vilmarest, Y. Goude, "Adaptive Methods for Short-Term Electricity Load Forecasting During COVID-19 Lockdown in France," *IEEE Transactions on Power Systems*, 36(6), 2021. Preprint arXiv:2101.05845
