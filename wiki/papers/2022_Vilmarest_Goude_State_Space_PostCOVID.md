---
type: paper
title: "State-Space Models for Online Post-COVID Electricity Load Forecasting Competition"
authors: [Joseph de Vilmarest, Yannig Goude]
year: 2022
journal_conference: "IEEE Open Access Journal of Power and Energy (doi:10.17023/yaz3-xp85); preprint arXiv:2110.00334"
doi_url: "https://arxiv.org/abs/2110.00334"
status: metadata-verified-2026-08
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Presents the **winning strategy of the IEEE DataPort competition** "Day-Ahead Electricity Load Forecasting: Post-COVID Paradigm" — day-ahead forecasting of an undisclosed ~1.1 GW region whose consumption regime broke in March 2020.
- Core claim: **state-space adaptation gives the best of both worlds** — autoregressive models are inherently adaptive but miss exogenous structure, while ML models capture exogenous dependence but fail on non-stationary data; wrapping ML features in a state-space recursion fixes both failures at once.

## 🧠 Methodology & Model Architecture
- Pipeline: (1) statistical correction of meteorological variables; (2) base forecasters — GAM, MLP, random forest, autoregressions; (3) **Kalman filter** on linearised learner outputs with break settings; (4) **VIKING** (Variational Bayesian Variance Tracking) to learn observation/state variances adaptively instead of hard-coding breaks; (5) **aggregation of experts** across the resulting forecaster set.
- Final procedure was assembled during the competition's evaluation period; the paper focuses on the clean final version.

## 📈 Performance & Results
- The strategy achieved **first place** in the competition; ablations show each layer (Kalman adaptation, VIKING, aggregation) contributes measurable gains over static and singly-adaptive baselines.

## 💡 Limitations & Identified Research Gaps
- Error propagation across the stacked adaptations (intraday correction → Kalman → VIKING → aggregation) lacks full interpretability; variance tracking assumes approximate Gaussianity. Code: gitlab.com/JosephdeVilmarest/state-space-post-covid-forecasting

## 📚 BibTeX & Citation Reference
- J. de Vilmarest, Y. Goude, "State-Space Models for Online Post-Covid Electricity Load Forecasting Competition," *IEEE Open Access Journal of Power and Energy*, 2022 (DOI:10.17023/yaz3-xp85); preprint arXiv:2110.00334
