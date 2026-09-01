---
type: model
name: EnbPI (Ensemble batch Prediction Intervals)
category: Statistical Learning / Conformal Prediction for Time Series
tags:
  - model
  - conformal-prediction
  - ensemble-learning
  - uncertainty-quantification
---

# 🎯 EnbPI

## Overview
EnbPI (Xu & Xie, 2021, *Conformal prediction interval for dynamic time-series*) is a **distribution-free conformal wrapper that turns any ML point forecaster into one with approximately valid prediction intervals** — no retraining of the base model, no distributional assumptions. Mechanics:

1. Fit an **ensemble of B models on bootstrap batches** of the training data.
2. Compute **leave-one-batch-out (LOO) residuals** $\hat{\epsilon}^{\mathrm{LOO}}$ (each point predicted by the sub-ensemble that never saw its batch).
3. Interval = ensemble aggregate ± residual quantile:
$$\widehat{\mathrm{PI}}_{\alpha}(x) \;=\; \hat{F}^{\,\phi}(x) \,\pm\, \mathrm{quantile}_{(1-\alpha)}\!\left(\hat{\epsilon}^{\,\mathrm{LOO}}\right)$$
4. **Sequential aggregation**: as new observations arrive, residuals are updated in a FIFO fashion so intervals track mild non-stationarity.

Coverage is approximate (not exact finite-sample) under β-mixing dependence; crucially the calibration is **static between updates** — it has no covariate-aware or fully-online feedback mechanism, which is exactly where it breaks under hard regime shifts.

## Typical Usage in EV Load Forecasting
- **Input**: any point-forecast features; wrapper only.
- **Strengths**: model-agnostic (trees, deep nets alike); cheap; competitive coverage on load/solar-type series.
- **Weaknesses**: static quantile of past residuals fails under regime change — empirically: EV/PV coverage ≈0.90/0.91 at α=0.1 but **price coverage collapse to 0.60 (0.22 in Autumn)** under the 2021 gas-price shift ([[PICP]] evidence). Adaptive alternatives: [[AS_CQR]] / ACI-style online feedback.

## 📚 Literature Usage
- [[2025_Stochastic_MPC_Conformal_Hub]] — CDC 2025 usage: EnbPI (MAPIE implementation) wraps Scikit-learn GradientBoostingRegressor ([[XGBoost]]-family gradient-boosted trees) forecasters for EV load / PV / price, producing the scenario tree (5th/mean/95th percentiles) consumed by stochastic MPC of a charging energy hub.

## Related Pages
- [[PICP]]
- [[AS_CQR]]
