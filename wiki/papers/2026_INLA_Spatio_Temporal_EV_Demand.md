---
type: paper
title: "Spatio-Temporal Modelling of Electric Vehicle Charging Demand"
authors: [Kaoutar Bouaachra, Yvenn Amara-Ouali, Yannig Goude, Raphaël Lachieze-Rey]
year: 2026
journal_conference: "arXiv preprint (arXiv:2604.19841)"
doi_url: "https://arxiv.org/abs/2604.19841"
models_used: ["[[INLA_Latent_Gaussian_Model]] (proposed-new; SPDE–RW2 and ICAR–RW2 variants)", "[[XGBoost]] (station-level baseline)", "Poisson GLM (station-level baseline)"]
datasets_used: ["[[ChargePlace_Scotland]] (proposed-new, open benchmark Oct 2022 – Apr 2025)"]
features_used: ["spatial coordinates (lon/lat, British National Grid)", "[[Weather_Traffic|weather covariates]] (temperature splines, humidity, wind speed via riem package)", "[[Electricity_Tariff|tariff status free/paid]] (time-varying)", "charger type (AC vs Rapid/Ultra-Rapid)", "public/private access", "day-of-week"]
forecasting_horizon: "[[Day_Ahead_Forecasting|day-ahead daily session counts]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[MAPE]]", "WAIC/DIC"]
tags: [paper, ev-load-forecasting, bayesian, spatio-temporal, open-dataset]
---

# Summary: Spatio-Temporal Modelling of Electric Vehicle Charging Demand

## 🎯 Main Objective & Contribution
Two-part contribution:
1. **New open benchmark dataset**: large-scale longitudinal EV charging dataset from Scotland (October 2022 – April 2025), released openly via ChargePlace Scotland with a reproducible preprocessing pipeline (cleaning, enrichment, spatial indexing). Explicitly positioned as a **modern replacement for stale legacy benchmarks such as Palo Alto (2020)** that "fail to reflect the scale and behavioral diversity of modern charging networks."
2. **First application of Latent Gaussian Models + INLA to EV charging demand**: spatio-temporal formulation jointly capturing spatial dependence, temporal dynamics, and covariate effects in a unified probabilistic framework — scalable approximate Bayesian inference (vs. prohibitive MCMC), **principled uncertainty quantification**, and interpretable spatial/temporal decompositions for risk-aware infrastructure planning.

## 🧠 Methodology & Model Architecture
**Observation model** (daily session counts $y_{i,t}$ at charge point $i$, day $t$), Poisson likelihood with log link (Eqs. 1–3):
$$y_{i,t} \mid \mu_{i,t} \sim \text{Poisson}(\mu_{i,t})$$
$$\mu_{i,t} = \exp(\eta_{i,t})$$
$$\eta_{i,t} = \alpha + \sum_{k=1}^{K} \beta_k x_k(i,t) + f_{space}(i) + f_{time}(t)$$

- Fixed effects $\beta_k$: charger type, power capacity, public/private access, tariff status, day-of-week, weather (temperature spline, wind speed).
- Both latent effects are sparse-precision GMRFs enabling INLA.

**Temporal effect — RW2** (Eq. 4), intrinsic GMRF of rank 2 (invariant to shift + linear trend), precision matrix banded to 4 neighbours per time point:
$$\Delta^2 f_{time}(t) = f_{time}(t) - 2f_{time}(t+1) + f_{time}(t+2) \sim \mathcal{N}(0, \tau_t^{-1})$$
Prior on log-precision: $\theta_t = \log \tau_t \sim \text{Log-Gamma}(a=1,\ b=5\times10^{-5})$.

**Spatial effect — two alternatives:**
1. *SPDE (continuous)*: Matérn GRF represented as SPDE solution $(\kappa^2 - \Delta)^{\alpha/2}(\tau f(s)) = W(s)$ (reconstructed from garbled Eq. 7), $\alpha=2$ ⇒ smoothness $\nu=1$ in $\mathbb{R}^2$; solved by FEM on a constrained Delaunay triangulated mesh (inner edge 200 m, outer edge 2000 m, cutoff 100 m) with barycentric projection matrix $A$. Complexity drops from $O(n^3)$ to $O(V^{3/2})$.
2. *ICAR (discrete)*: intrinsic conditional autoregressive (Besag) over areal units, precision $Q = \tau(D - W)$, sum-to-zero constraint; neighbourhoods = k-nearest neighbours ($k=4$) on CPID coordinates, isolated nodes bridged to keep one connected component.

**Inference**: R-INLA (Integrated Nested Laplace Approximation) — deterministic Laplace-based approximate Bayesian inference, avoiding MCMC cost at scale.
**Evaluation protocol**: 80/20 temporal train/test split, split date **2024-10-06**; metrics MAE/RMSE/MAPE on test window; fit compared via WAIC/DIC. Baselines: per-CPID Poisson GLM and XGBoost fitted independently (no spatial information sharing) — isolating the benefit of structured spatial pooling.

## 📊 Dataset & Input Features
**Source**: ChargePlace Scotland (CPS) open-access repository (Transport Scotland); monthly session logs enriched with charger metadata from Davies et al. (2024) (CPID → connector specs, postcodes), community-council boundaries from Open Data Scotland, meteorological data via the `riem` package.
> ⚠️ **URL caveat**: the extracted full text contains only hyperlink placeholders ("Git repository.", "Zenodo repository.") for code and data — no literal URLs appear anywhere in the text (ref [15] is citation-only). Exact Zenodo/Git URLs must be recovered from the arXiv HTML/PDF source before citing them.

**Curation**: removed zero-duration / zero-kWh sessions (failed handshakes), sessions exceeding UK mass-market max battery capacity, billed cost above max daily tariff (incl. overstay penalties); inconsistent date formats (DD/MM vs MM/DD) re-parsed; systematic reporting-failure windows removed (Oct 2022, Mar & Jun 2023, early 2024).

**Scotland-wide EDA**: 12 local authorities switched free→paid tariffs during Oct 2022–Apr 2025 → sharp, lasting session declines (e.g., North Lanarkshire, East Renfrewshire) while pre-tariff Dundee City stayed stable; Rapid chargers active 83% of days vs 59% AC; post-tariff drops −46.6% (Rapid) vs −66.1% (AC) ⇒ AC more price-sensitive; weekday > weekend demand, Friday peak, Sunday lowest.

**Spatio-temporal case study — Central Glasgow** (highest session density of all Scottish local authorities): 18 neighbourhoods, **96 CPIDs**, 879 days (Oct 2022–Apr 2025), 43,807 session-day records, **104,041 total sessions**; mean 2.37 sessions/day/CPID (median 2, sd 2.01, max 32); AC 92 (95.8%) vs Rapid 4 (4.2%); public 86 (89.6%) vs private 10 (10.4%); extent lon [−4.313, −4.210], lat [55.843, 55.883]. Seven anomalous CPIDs excluded (62201, 62202, 62203, 62266, 62261, 50433, 62123).

## 📈 Performance & Results
- **Model fit (in-sample)**: ICAR–RW2 slightly better than SPDE–RW2 — ICAR: DIC = 136,562.8, WAIC = 136,509.1; SPDE: DIC = 136,941.3, WAIC = 136,909.1. Posterior fixed effects consistent across both.
- **Key drivers**: Rapid connector strongest positive effect (ICAR $\hat\beta$=0.872, CI [0.599, 1.146]; SPDE 0.914 [0.819, 1.008]); public access (+0.321/+0.350); free charging (+0.146/+0.142); Sunday largest negative day effect (−0.063/−0.066); only temperature spline 1 credibly negative among weather covariates (−0.324 ICAR); humidity & wind negligible.
- **Head-to-head dominance vs station-level baselines** (% of stations where INLA wins):
  - **MAE**: 70.1% (ICAR vs GLM), **77%** (ICAR vs XGBoost), 72.4% (SPDE vs GLM), 73.6% (SPDE vs XGBoost) ⇒ **70–77% dominance**, tighter error distributions.
  - **MAPE**: 67.8–72.4% ("68–72%"), advantage clearest for low-demand stations.
  - **RMSE**: only 52.9–58.6% ("53–59%") ⇒ **near-parity**; spatial pooling reduces average/relative errors but not large individual errors (local demand spikes not captured by the spatial structure).
- **Spatial range**: $\hat\rho$ = **684.4 m** (95% CI [338.9, 1175.1] m) — physically coherent given mean nearest-neighbour CPID distance 113.8 m (max 834.5 m) ⇒ spatial dependence operates at a **sub-kilometre scale** (local land use / amenities).
- **Temporal**: RW2 posterior precision ≈ 1.97×10⁵ absorbs nearly all time-varying signal; latent trend cleanly captures the **early-2023 tariff structural break** then stabilisation.

## 💡 Limitations & Identified Research Gaps
- **Session counts, not kWh load or peak power** — energy/power modelling flagged as future work needing heavier-tailed likelihoods.
- Day-level aggregation; Poisson likelihood imperfect under observed over-/under-dispersion (Negative Binomial suggested).
- Case study limited to dense central Glasgow — generalisation to sparse Scottish regions unclear; CPS network may not represent private/workplace charging.
- **Proposed future directions**: scaling to all of Scotland; hierarchical multi-scale forecasting (CPID → neighbourhood → local authority, coherent across aggregations); **hybrid two-stage INLA–ML pipeline** — XGBoost first stage for nonlinear covariate interactions, INLA second stage on its residuals (following Hu et al. 2026, "XGBoost meets INLA", wildfire forecasting) — directly relevant to thesis hybrid-model discussions.

## 📚 BibTeX
```bibtex
@misc{2026_Bouaachra_INLA_EV,
  author        = {Bouaachra, Kaoutar and Amara-Ouali, Yvenn and Goude, Yannig and Lachieze-Rey, Rapha{\"e}l},
  title         = {Spatio-Temporal Modelling of Electric Vehicle Charging Demand},
  year          = {2026},
  howpublished  = {arXiv preprint arXiv:2604.19841},
  doi           = {10.48550/arXiv.2604.19841},
  url           = {https://arxiv.org/abs/2604.19841}
}
```

## 🔗 Key References & Citation Graph
- Cites **Amara-Ouali et al. (2021), "A review of electric vehicle load open data and models"** (Energies) as ref [12] — the survey line this paper's dataset contribution extends; ⚠️ **no vault page yet** → candidate new paper page.
- Cites [[Graph_WaveNet]] (Wu et al., ref [9]) and spatio-temporal GCNs (Yu et al., STGCN, ref [8]) as the ML spatio-temporal line it positions against → see also [[GCN]], [[2019_Graph_WaveNet_Spatial_Temporal_Modeling]].
- Cites TCN-LSTM EV charging load forecasting (Tian et al. 2025, ref [10]) — related vault concept [[TCN]].
- Future-work anchor: Hu et al. 2026 "XGBoost meets INLA" two-stage spatio-temporal wildfires (ref [26]) — blueprint for the proposed EV hybrid.
- Vault context (not cited by paper, but related): replaces [[Palo_Alto_EV]] as benchmark lineage; Scottish sibling open datasets [[Dundee_EV]] and [[Perth_EV]]; tariff-effect discussion connects to [[Electricity_Tariff]].
