---
type: model
name: INLA Latent Gaussian Model (LGM)
category: Statistical Learning / Approximate Bayesian Spatio-Temporal Modelling
tags:
  - model
  - bayesian
  - inla
  - spatio-temporal
  - gmrf
---

# 📈 INLA Latent Gaussian Model

## Overview
A **Latent Gaussian Model** couples a likelihood for the observations with a latent Gaussian field $\eta$ carrying fixed effects plus structured spatial/temporal random effects; because the latent field is a *Gaussian Markov Random Field* (sparse precision), it can be fitted with **Integrated Nested Laplace Approximation** (Rue, Martino & Chopin 2009) — deterministic approximate Bayesian inference that avoids prohibitive MCMC at scale.

Canonical EV-demand formulation (Bouaachra et al. 2026; daily session counts $y_{i,t}$ at charge point $i$):
$$y_{i,t}\mid\mu_{i,t}\sim\text{Poisson}(\mu_{i,t}),\qquad \mu_{i,t}=\exp(\eta_{i,t})$$
$$\eta_{i,t}=\alpha+\sum_k \beta_k x_k(i,t)+f_{space}(i)+f_{time}(t)$$
with fixed effects $\beta_k$ for charger type/power, access, tariff status, weather splines, day-of-week.

## Latent Components
- **Temporal — RW2**: second-order random walk, an intrinsic GMRF of rank 2 (invariant to shift + linear trend):
$$\Delta^2 f_{time}(t)=f_{time}(t)-2f_{time}(t+1)+f_{time}(t+2)\sim\mathcal{N}(0,\tau_t^{-1})$$
Absorbs smooth trend and cleanly captures structural breaks (e.g., tariff introduction).
- **Spatial (continuous) — SPDE–RW2**: Matérn field via the SPDE link $(\kappa^2-\Delta)^{\alpha/2}(\tau f(s))=W(s)$ with $\alpha=2$ ($\nu=1$ smoothness); solved by FEM on a constrained Delaunay triangulated mesh with barycentric projection — complexity drops from $O(n^3)$ to $O(V^{3/2})$.
- **Spatial (discrete) — ICAR–RW2**: Besag intrinsic conditional autoregression $Q=\tau(D-W)$ over areal units with sum-to-zero constraint; neighbourhoods from k-NN on charge-point coordinates.

**Inference & fit comparison**: R-INLA posterior marginals; models compared via WAIC/DIC. Hyperpriors on log-precisions are Log-Gamma.

## Typical Usage in EV Load Forecasting
- **Input**: daily session counts + covariates ([[Electricity_Tariff]] status, charger type, [[Weather_Traffic]] splines).
- **Forecasting Horizon**: [[Day_Ahead_Forecasting]] (daily counts, 80/20 temporal split).
- **Strengths**: principled UQ (posteriors, credible intervals); spatial pooling beats per-station no-pooling baselines on MAE at 70–77% of stations; interpretable spatial range (~684 m in Glasgow) and temporal-break decomposition; orders of magnitude cheaper than MCMC.
- **Weaknesses**: session counts only (not kWh/power); Poisson likelihood strained by over-dispersion; RMSE near-parity with XGBoost (local spikes not captured); proposed extensions: Negative Binomial likelihood, hierarchical multi-scale reconciliation, two-stage XGBoost→INLA hybrid on residuals.

## 📚 Literature Usage
- [[2026_INLA_Spatio_Temporal_EV_Demand]] — First LGM+INLA application to EV charging demand; ICAR–RW2 edges out SPDE–RW2 (DIC 136,563 vs 136,941) on the Glasgow [[ChargePlace_Scotland]] benchmark.

## Related Pages
- [[ChargePlace_Scotland]]
- [[XGBoost]]
