---
type: paper
title: "CRPS Learning"
authors: [Jonathan Berrisch, Florian Ziel]
year: 2023
journal_conference: "arXiv preprint (Quantitative Finance lineage)"
doi_url: "https://arxiv.org/abs/2302.03511"
status: needs-review
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Proposes **CRPS learning**: perform online gradient-descent-style learning directly in **CRPS (Continuous Ranked Probability Score) space**, building an adaptive **ensemble of distributional forecasts** (base learners' full predictive distributions) whose combination minimises CRPS rather than pinball losses per quantile.
- Motivation: existing distributional ensembles either aggregate quantiles separately or assume exchangeability; CRPS learning yields one coherent predictive distribution and provable/observed robustness on non-stationary series.

## 🧠 Methodology & Model Architecture
- Base learners produce candidate predictive distributions; an online algorithm updates mixture weights by stochastic (mini-batch) gradient steps on the empirical CRPS risk, with expert-aggregation-style guarantees inherited from online learning under dynamic environments.
- Evaluated against quantile-regression averaging (e.g., QRA) and related distributional aggregation methods.

## 📈 Performance & Results
- On electricity-price/load forecasting case studies (including German market data typical of Ziel's line of work), CRPS learning matches or beats QRA-type benchmarks on CRPS and related scores while adapting faster after distribution shifts.

## 💡 Limitations & Identified Research Gaps
- Requires differentiable CRPS approximation choices; base-learner quality still dominates. Connections to conformal and distribution-free calibration (cf. [[Conformal_Prediction]], [[Zaffran2022_Adaptive_Conformal]]) remain open.

## 📚 BibTeX & Citation Reference
- J. Berrisch, F. Ziel, "CRPS learning," 2023 (arXiv preprint; see also their ProfKriging/QRA line of work). R package `crpslearning`. Status: metadata partially verified — confirm journal version.
