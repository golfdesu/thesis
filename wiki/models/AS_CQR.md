---
type: model
name: AS-CQR (Adaptive Sequential Conformalized Quantile Regression)
category: Statistical Learning / Adaptive Conformal Uncertainty Quantification
tags:
  - model
  - conformal-prediction
  - quantile-regression
  - uncertainty-quantification
  - distribution-shift
---

# 🎯 AS-CQR (Adaptive Sequential Conformalized Quantile Regression)

## Overview
AS-CQR (Yu et al., KDD '26) wraps a quantile-regression forecaster with a **conformal calibration layer that adapts online** to distribution shift. Two ingredients distinguish it from static CQR:

1. **Width-normalized signed nonconformity score** — scale-invariant across heteroscedastic high/low-load regions (motivated by measured r=0.94 correlation between load level and residual std):
$$\epsilon_t=\frac{\max\bigl(\hat{q}_{\text{lo}}(X_t)-Y_t,\; Y_t-\hat{q}_{\text{up}}(X_t)\bigr)}{\hat{q}_{\text{up}}(X_t)-\hat{q}_{\text{lo}}(X_t)+\delta},\qquad\delta\approx10^{-6}$$
2. **Online feedback of the effective miscoverage level** (ACI-style, $\tilde{\alpha}_0=\alpha$, $\gamma=0.005$), computed over a sliding window of $m=100$ scores:
$$Q_t=\mathrm{Quantile}_{1-\tilde{\alpha}_t}(E_t),\qquad \tilde{\alpha}_{t+1}=\tilde{\alpha}_t+\gamma\bigl(\alpha-\mathbb{I}\{Y_t\notin\hat{C}(X_t)\}\bigr)$$
The calibrated interval multiplicatively rescales the raw quantile width $w_t=\hat{q}_{\text{up}}-\hat{q}_{\text{lo}}$: $\hat{C}(X_t)=[\hat{q}_{\text{lo}}-Q_t w_t,\;\hat{q}_{\text{up}}+Q_t w_t]$.

## Lineage: CQR → ACI → AS-CQR
| Method | Mechanism | Guarantee |
|--------|-----------|-----------|
| **CQR** (Romano et al., NeurIPS 2019) | Static conformal correction of quantile heads | Finite-sample marginal coverage *only under exchangeability* — fails under regime shift |
| **ACI** (Gibbs & Candès, NeurIPS 2021) | Online update $\tilde{\alpha}_t$ from recent misses | Long-run coverage under arbitrary shift |
| **AS-CQR** (Yu et al., KDD '26) | CQR quantile base + width-normalized scores + ACI feedback | $\lim_{T\to\infty}\frac1T\sum_t\mathbb{I}\{Y_t\in\hat{C}(X_t)\}=1-\alpha$ |

Static CQR is exactly what fails in Yu's ablation (w/o AS-CQR: MAE 36.57→44.12 *and* target coverage missed); AS-CQR restores coverage online but only via scalar feedback — window $m$ and step size $\gamma$ are fixed hyperparameters with no per-region/per-horizon adaptivity. This adaptive-calibration-under-shift problem is the thesis **Gap P-3** hook. Contrast [[PICNN]]: AS-CQR adds no convexity/monotonicity structure, so quantile crossing remains possible; and note EnbPI ([[EnbPI]]) shows the same static-calibration failure mode empirically on price series.

## 📚 Literature Usage
- [[2026_Yu_EnergyMamba_Graph_Mamba_ASCQR]] — Original paper: AS-CQR wraps GE-Mamba's three-head quantile output; ~6% Interval-Score gain and ≥90% coverage across [[Florida_CBG_Smart_Meter]]/[[NYISO]]/[[CAISO]].
- Related vault anchors: [[2021_Stankeviciute_Conformal_Time_Series_Forecasting]], [[2024_Zhou_Conformal_Prediction_DER]], [[2025_FernandezZapico_Stochastic_MPC_Conformal_Hub]] (static-wrapper failure motivating adaptivity).

## Related Pages
- [[EnergyMamba]]
- [[PICNN]]
- [[PICP]]
- [[Interval_Score]]
