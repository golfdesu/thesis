---
type: paper
title: "Probabilistic Load Forecasting Based on Adaptive Online Learning"
authors: [Verónica Álvarez, Santiago Mazuelas, José A. Lozano]
year: 2021
journal_conference: "IEEE Transactions on Power Systems 36(4):3668-3680"
doi_url: "https://arxiv.org/abs/2011.14721"
status: metadata-verified-2026-08
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Proposes **APLF (Adaptive Probabilistic Load Forecasting)**: probabilistic load forecasts based on **adaptive online learning of hidden Markov models (HMMs)**, explicitly designed for consumption patterns that change over time (renewables integration, EVs, microgrids).
- Key contributions: (1) recursive online updates of HMM parameters with theoretical guarantees; (2) sequential prediction rules producing full predictive distributions from the most recent parameters; (3) efficient implementation with memory complexity $O(CR^2)$, learning $O(LR^3)$, prediction $O(LR)$ — amenable to real-time deployment.

## 🧠 Methodology & Model Architecture
- Load is modelled as an HMM whose emissions are Gaussian with parameters conditioned on a calendar-type covariate vector (time-of-day/season classes), so consumption-pattern drift is captured by evolving the hidden state posterior rather than retraining offline.
- At each time step the model parameters are updated **recursively** (no windowing/retraining), and Gaussian probabilistic forecasts $\mathcal{N}(s_{t+i}, e_{t+i})$ for horizons $i=1..L$ are produced from the latest parameters, giving calibrated prediction intervals.

## 📈 Performance & Results
- Evaluated on multiple regional datasets with assorted time-varying consumption patterns; APLF significantly improves both point error and interval quality versus existing probabilistic baselines (GP, quantile regression) and online point-forecast techniques across a wide range of scenarios.

## 💡 Limitations & Identified Research Gaps
- Gaussian emission assumption limits tail modelling; HMM state count and calendar typing are design choices requiring tuning. Guarantees are asymptotic/online-regret style rather than finite-distribution-free.

## 📚 BibTeX & Citation Reference
- V. Álvarez, S. Mazuelas, J. A. Lozano, "Probabilistic Load Forecasting Based on Adaptive Online Learning," *IEEE Transactions on Power Systems*, 36(4):3668-3680, 2021. Preprint: arXiv:2011.14721. Code: github.com/MachineLearningBCAM/Load-forecasting-IEEE-TPWRS-2020
