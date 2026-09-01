---
type: model
name: VMD-Prophet-LSTM
category: Hybrid Decomposition / VMD + Prophet + LSTM Combined Model
tags:
  - model
  - hybrid-model
  - decomposition
  - vmd
  - ev-load-forecasting
---

# 🧩 VMD-Prophet-LSTM

## Overview
VMD-Prophet-LSTM (Cheng et al., Frontiers in Energy Research 2023) is a decomposition-based hybrid for EV charging-load prediction: [[VMD]] decomposes the load into $k$ Intrinsic Mode Functions (IMFs); IMFs are split by **zero-crossing rate** into low-frequency (stable, periodic) and high-frequency (volatile) reconstructed sequences; [[Prophet]] forecasts the low-frequency part while [[LSTM]] handles the high-frequency part; outputs are summed.

Pipeline equations:
- VMD constrained variational problem:
$$ \min_{\{u_i\},\{\omega_i\}} \left\{ \sum_{i=1}^{k} \left\| \partial_t \left[ \left( \delta(t) + \frac{j}{\pi t} \right) * u_i(t) \right] e^{-j\omega_i t} \right\|_2^2 \right\}, \quad s.t.\ \sum_{i=1}^{k} u_i = f $$
solved by ADMM-style Fourier-domain updates with augmented Lagrangian ($\alpha = 8000$; mode count via energy-jump criterion, $k=6$).
- Zero-crossing split (threshold 0.05): $P_{sZC} = n_{ZC}/N$ — >0.05 → high-frequency (→LSTM), <0.05 → low-frequency (→Prophet).
- Prophet additive model: $y(t) = g(t) + h(t) + s(t) + \varepsilon(t)$ with logistic growth $g(t) = C/(1+e^{-k(t-m)})$ and holiday term $h(t)=Z(t)\kappa$.
- LSTM gates: standard forget/input/output cell ($f_t, i_t, o_t$), 96-dim input → 2 LSTM layers → FC layers (128/64/32/16).

Reported average absolute-error reductions: **7.57% vs ARIMA**, **8.73% vs LSTM**, **46.02% vs Prophet**.

## Typical Usage in EV Load Forecasting
- **Input**: univariate historical charging-power series (15-min resolution, 96 steps/week); no exogenous covariates.
- **Forecasting Horizon**: [[Short_Term_Forecasting]].
- **Strengths**: component-aware modeling — VMD even rescues volatile sequences that collapse raw Prophet (R² 0.49→part of a 0.84 combined fit); simple, interpretable pipeline on modest hardware (GTX 1050Ti).
- **Weaknesses**: fixed zero-crossing threshold heuristic; empirical k-selection; single-station case study; point forecast only — motivates quantile/distributional and federated extensions.

## Literature Usage
- [[2023_Cheng_VMD_Prophet_LSTM]] — Original paper: MAE 109.22 kW / R² 0.8411 vs ARIMA 118.16, LSTM 119.67, Prophet 202.32 on Fujian station data.
- [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] — Related VMD(+ICEEMDAN) multi-frequency decomposition preprocessing line for spatio-temporal LLM-based EV charging-volume forecasting.
- [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] — Related decomposition-first hybrid lineage for EV load forecasting benchmarking.
