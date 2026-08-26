---
type: paper
title: "Estimating Treatment Effects in Continuous Time with Hidden Confounders"
authors: [Defu Cao, James Enouen, Yan Liu]
year: 2023
journal_conference: "arXiv:2302.09446 (cs.LG); formatted for ICML (PMLR 162), University of Southern California"
doi_url: "https://doi.org/10.48550/arXiv.2302.09446"
models_used: ["[[LipSCDE]]", "[[Neural_SDE]]", "[[Neural_CDE]]", "[[Lipschitz_RNN]]", "[[LSTM]]", "[[MSM]]", "[[RMSN]]", "[[TSD]]", "[[DTA]]", "[[SeqDec]]"]
datasets_used: ["[[MIMIC-III]]", "[[COVID-19_German_Districts]]", "[[Synthetic_Irregular_Time_Series]]"]
features_used: ["[[Covariates]]", "[[Treatments]]", "[[Hidden_Confounders]]", "[[High_Frequency_Components]]", "[[Low_Frequency_Components]]", "[[Brownian_Motion]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[RMSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Estimating Treatment Effects in Continuous Time with Hidden Confounders

## 🎯 Main Objective & Contribution
Estimates individual/average treatment effects (ITE/ATE) in **continuous-time longitudinal settings with multi-cause hidden confounders** and irregularly sampled observations. Prior deconfounding works (TSD, SeqConf/SeqDec, DTA) either cannot handle irregular/sparse/intermittent time series or impose strong assumptions (e.g., multivariate Gaussian on irregular samples). Contributions:
1. **LipSCDE** — a Lipschitz-bounded neural stochastic controlled differential equation that continuously incorporates ongoing interventions and irregular sampling via controlled differential equations and a continuous-time stochastic factor model.
2. Unbiased estimation via **Lipschitz-bounded convolutional operations** on high-/low-frequency components of observed data to reconstruct hidden confounder substitutes with bounded influence ("hidden confounders boundary").
3. Experiments on MIMIC-III and COVID-19 show improved ITE estimates and better healthcare treatment recommendations.

## 🧠 Methodology & Model Architecture
Two branches:

**(a) Hidden Confounders Boundary Branch**: History trajectories $h_t$ are converted to the frequency domain via the Fourier transform $\mathcal{F}$; Gaussian high-pass filter $G_h$ and low-pass filter $G_l$ extract fast-changing boundary components vs. smooth trend components. Lipschitz-constrained convolutional operators + inverse Fourier transform $\mathcal{F}^{-1}$, followed by a small Lipschitz-regularized MLP, produce the hidden-confounder representation $Z_t$ with bounded influence.

**(b) Synthetic Control Branch**: A continuous-time Lipschitz RNN embeds observations $u_t := h_\theta(H_t) = h_\theta([x_t, a_t, z_t, H_{<t}])$ into an $l$-dimensional latent state; $f_\theta(h,t) = A_\theta h + \sigma(W_\theta h + U_\theta u_t + b)$ with 1-Lipschitz nonlinearity $\sigma(\cdot)$ (Erichson et al., 2020); $g_\theta$ defined similarly. The latent path solves the stochastic controlled differential equation (Eq. 1):

$$u_t = u_{t_0} + \int_{t_0}^{t} f_\theta(u_s, s)\, dH_s + \int_{t_0}^{t} g_\theta(u_s, s)\, dW_s, \quad t \in (t_0, t_m],$$

controlled by historical information $H$ and Brownian motion $W$; forward trajectories computed by any numerical ODE solver, gradients via adjoint-based differentiable training (Kidger et al., 2020/2021).

**Outcome model**: latent representations $U_t = (\hat{u}_{t_1},\dots,\hat{u}_{t_k})$ are decoded by two stacked LSTM CDE layers over padded irregular sequences plus a linear fully-connected head; unbiasedness is enforced through inverse probability of treatment weighting (**IPTW**) when estimating $\mathbb{E}[Y_{a,\ge t}|U_t]$.

**Causal assumptions**: Positivity/Overlap, Consistency, and Assumption 3.1 — sequential single strong ignorability in continuous time: $Y_{a_{\ge t_m}} \perp\!\!\!\perp A_{t_m,j} | X_{t_m}, H_{<t_m}$ for all treatments $j$. ITE defined as $\tau^i_{a,b} = Y^i_{a,t_m} - Y^i_{b,t_m}$; ATE as its population average.

## 📊 Dataset & Input Features
1. **MIMIC-III** — freely accessible critical care database (Johnson et al., 2016); outcomes: blood pressure prediction ("Blo. pre.") and oxygen saturation ("Oxy. sat."). No URL printed in the paper text.
2. **COVID-19 dataset** (Steiger et al., 2020) — observational data from German districts; outcome: covid case prediction; drivers include mobility, awareness, holiday indicators (shown in the architecture figure). Published as medRxiv preprint (no URL in text).
3. **Synthetic irregular time series** — aligned synthetic data with randomly removed observations per unit at missing rates {0%, 15%, 30%} and confounding degrees {0.0, 0.2, 0.4}.

Inputs per patient/unit $i$: irregularly sampled covariates $X^i_t = [x^i_{t_0},\dots,x^i_{t_m}]$ ($x_{t_k}\in\mathbb{R}^d$), treatments $A^i_t$ ($a_{t_k}\in\mathbb{R}^j$), hidden confounders $Z^i_t$, complete history $H_{<t_m} = \{X_{<t_m}, A_{<t_m}, Z_{<t_m}\}$, one-dimensional outcomes $Y_t$, plus Brownian motion $W$ in the SDE.

Training setup: Adam optimizer, learning rate 0.01, 10 epochs with 10 iterations per batch, batch size 16, 80/10/10 train/validation/test split. Baselines share an MSM/IPTW-based outcome model design.

## 📈 Performance & Results
All numbers are RMSE (%) — lower is better.

**Real-world data (Table 1)**:

| Outcome | MSM (Conf.) | DTA | TSD | RMSN (Conf.) | RMSN+DTA | RMSN+TSD | SeqDec | **LipSCDE** |
|---|---|---|---|---|---|---|---|---|
| Blood pressure (MIMIC-III) | 14.54 / 14.46 | 13.31 / 18.33 | 13.57 / 12.11 | — | — | — | 13.74 | **8.82** |
| Oxygen saturation (MIMIC-III) | 4.72 / 4.22 | 4.65 / 4.21 | 4.33 / 4.25 | — | — | — | 4.19 | **4.19** |
| COVID-19 cases | 15.10 / 11.48 | 13.93 / 13.52 | 13.07 / 11.08 | — | — | — | 11.43 | **10.28** |

(DTA/TSD rows reported under both MSM and RMSN outcome-model variants.) LipSCDE outperforms the TSD baseline by **27.2% on blood pressure** and **7.2% on COVID case prediction**; ties SeqDec at 4.19 on oxygen saturation.

**Synthetic irregular data (Table 2)** — RMSE across missing rate M ∈ {0%, 15%, 30%} and confounding degree R ∈ {0, 0.2, 0.4}: LipSCDE wins every setting; e.g., at 0%/0: Conf. 2.5, TSD 2.73, SeqDec 2.17, **LipSCDE 0.60**; at 30%/0.4: Conf. 4.19, TSD 4.06, SeqDec 3.89, **LipSCDE 2.96**. Methods ignoring hidden confounders are consistently worse; CDE-based LipSCDE handles irregular sampling natively while all other baselines require prior interpolation onto a regular grid.

## 💡 Limitations & Identified Research Gaps
- Evaluation is one-step-ahead estimation; long-horizon counterfactual rollout is not addressed.
- Hidden-confounder recovery relies on frequency-domain filtering + Lipschitz bounding heuristics; identifiability of the latent factor model is not formally proven.
- Synthetic experiments are small-scale; only two real-world datasets (both clinical/epidemiological), no public-benchmark treatment-effect suites.
- IPTW outcome correction inherits the usual propensity-weighting variance issues under extreme treatment probabilities.
- **Relevance to EV charging load forecasting**: provides the causal/deconfounding machinery for **price-elasticity modeling of charging demand** — directly complements the PIML price-elasticity line of [[2024_Qu_Physics_Informed_GAT_EV_Load]] and the price-elasticity-mechanism (PEM) module of [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]]; LipSCDE's continuous-time treatment-effect framing maps naturally to modeling tariff changes ("treatments") on charging load ("outcomes") while debiasing unobserved confounders such as fuel prices, local events, or fleet composition.

## 📚 BibTeX & Citation Reference
```bibtex
@article{cao2023estimating,
  title   = {Estimating Treatment Effects in Continuous Time with Hidden Confounders},
  author  = {Cao, Defu and Enouen, James and Liu, Yan},
  journal = {arXiv preprint arXiv:2302.09446},
  year    = {2023},
  note    = {University of Southern California. DOI: 10.48550/arXiv.2302.09446}
}
```

## 🔗 Key References & Citation Graph
- Bica et al. 2019 — Time Series Deconfounder (TSD), arXiv: https://arxiv.org/abs/1902.00450 (key deconfounding baseline).
- Hatt & Feuerriegel 2021 — Sequential Deconfounding (SeqDec), arXiv:2104.09323.
- Kuzmanovic et al. 2021 — Deconfounding Temporal Autoencoder (DTA).
- Lim et al. 2018 — Recurrent Marginal Structural Networks (RMSNs), NeurIPS.
- Robins et al. 2000 — Marginal structural models / IPTW.
- Wang & Blei 2019 — The blessings of multiple causes (static deconfounding framework).
- Chen et al. 2018 — Neural ODEs; Kidger et al. 2020/2021 — Neural CDEs and Neural SDEs (adjoint training).
- Erichson et al. 2020 — Lipschitz RNNs (arXiv:2006.12070); Gouk et al. 2021 — Lipschitz continuity regularization.
- Johnson et al. 2016 — MIMIC-III critical care database; Steiger et al. 2020 — COVID-19 German district observational data (medRxiv).
- **Related wiki notes**: [[2024_Qu_Physics_Informed_GAT_EV_Load]] (PIML price elasticity for EV load), [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] (PEM module for causal EV demand).

