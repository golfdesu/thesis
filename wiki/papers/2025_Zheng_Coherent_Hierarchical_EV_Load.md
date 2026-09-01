---
type: paper
title: "Coherent Hierarchical Probabilistic Forecasting of Electric Vehicle Charging Demand"
authors: [Kedi Zheng, Hanwei Xu, Zeyang Long, Yi Wang, Qixin Chen]
year: 2025
journal_conference: "IEEE Transactions on Industry Applications, vol. 61, no. 1, pp. 1329-1340"
doi_url: "https://doi.org/10.1109/TIA.2023.3344544"
models_used: ["[[LSTM]]", "[[PICNN]]", "[[DCL]]", "[[DeepAR]]", "[[DeepVAR]]", "[[MLP]]"]
datasets_used: ["[[Caltech_ACN]]"]
features_used: ["[[EV_Charging_Demand]]", "[[Temperature]]", "[[Dew_Point]]", "[[Precipitation]]", "[[Calendar_Features]]", "[[Holiday_Indicator]]", "[[Calendar_Features]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[MASE]]", "[[Pinball_Loss]]", "[[Winkler_Score]]", "[[Energy_Score]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Coherent Hierarchical Probabilistic Forecasting of Electric Vehicle Charging Demand

## 🎯 Main Objective & Contribution
- **Problem**: EV charging station (EVCS) operators manage multiple geographically distributed stations hierarchically; probabilistic forecasting across stations must handle (1) strong stochasticity of user behavior without parametric distribution assumptions, (2) **quantile crossing** in classical quantile regression, and (3) **hierarchical incoherency** — individual station forecasts don't sum to the operator total.
- **Contributions**:
  1. A deep learning framework for hierarchical probabilistic EVCS demand forecasting solving multivariate stochasticity + coherency jointly.
  2. [[PICNN]] (partial input convex neural network) models the joint multi-horizon conditional distribution as the gradient of a convex function w.r.t. quantile levels α → structurally prevents quantile crossing.
  3. [[DCL]] (differentiable convex optimization layers, via Cvxpylayers) reconciles sampled scenarios into coherent ones satisfying $y_t = \mathbf{S}\mathbf{z}_t$; the reconciliation weight matrix Q is **learned end-to-end** instead of fixed heuristically.
- Forecasting engine is modular ([[LSTM]] used in case study); explicitly out of scope to innovate on engines.

## 🧠 Methodology & Model Architecture
- **Quantile function definition**, Eq. (1): $q_Z(\alpha) = F_Z^{-1}(\alpha) = \inf\{z \in \mathbb{R} : \alpha \le F_Z(z)\}$; monotonicity requirement (no quantile crossing), Eqs. (3)–(4): $(q_{Z,t}(\alpha_1) - q_{Z,t}(\alpha_2))(\alpha_1 - \alpha_2) \ge 0,\ \forall \alpha_{1,2} \in (0,1)^\tau$.
- **Hierarchical constraint**, Eq. (5): $y_t = \mathbf{S} z_t$, with $\mathbf{S} = [1, 1, \ldots, 1]$ (total = sum of n bottom-level EVCS series).
- **Classical QP reconciliation**, Eq. (6):
$$x_t^\star = \arg\min_x \|Q_r(\hat{x}_t - x)\|_2^2 = \arg\min_x (\hat{x}_t - x)^\top Q (\hat{x}_t - x) \quad s.t.\ x \in \mathcal{S} \cap \mathbb{R}_+^{n+1}$$
with $Q = Q_r^\top Q_r$; traditionally identity or inverse-error-correlation weighting.
- **LSTM gates**, Eq. (7):
$$i_t = \sigma(W^{(i,x)}x_t + W^{(i,h)}h_{t-1} + b_i),\ f_t = \sigma(W^{(f,x)}x_t + W^{(f,h)}h_{t-1} + b_f),\ o_t = \sigma(W^{(o,x)}x_t + W^{(o,h)}h_{t-1} + b_o)$$
$$c_t = i_t \otimes \tanh(W^{(c,x)}x_t + W^{(c,h)}h_{t-1} + b_c) + f_t \otimes c_{t-1}, \qquad h_t = o_t \otimes \tanh(c_t)$$
- **PICNN layer update**, Eq. (8) (partial convexity in α given non-negative $W_i^{(v)}, W_i^{(\alpha)}$ and convex non-decreasing activations $g_i^{(v)}$; proof by induction):
$$u_{i+1} = g_i^{(u)}(W_i^{(u,u)} u_i + b_i^{(u,u)})$$
$$v_{i+1} = g_i^{(v)}\left(W_i^{(v)}\left(v_i \otimes ReLU(W_i^{(v,u)}u_i + b_i^{(v,u)})\right) + W_i^{(\alpha)}\left(\alpha \otimes ReLU(W_i^{(\alpha,u)}u_i + b_i^{(\alpha,u)})\right) + W_i^{(u)}u_i + b_i^{(v)}\right)$$
- **Quantile via gradient** of the convex output $f(\alpha,h)=v_k$, Eq. (9):
$$q(\alpha|h) = \nabla_\alpha f(\alpha, h) = \frac{\partial v_k}{\partial\alpha}, \qquad q(\alpha|h) = \nabla_\alpha e^\top f(\alpha, h) = \nabla_\alpha e^\top v_k \text{ (vector form)}$$
- **Energy score loss** (multivariate CRPS extension), Eqs. (10)–(11):
$$L_{ES} = \mathbb{E}_{w_1,w_2\in\Omega}\left(-\frac{1}{2}\|w_1-w_2\|_2^\beta + \|w_1-x\|_2^\beta\right), \quad \Omega = \{q(\alpha|h) : \alpha \sim U(0,1)^\tau\},\ \beta\in(0,2)$$
- **DCL principle**: reconciliation QP canonicalized into disciplined parameterized program / conic form, Eq. (12): $\min_x c^\top x\ s.t.\ b - Ax \in \mathcal{K}$; auxiliary-variable second-order-cone reformulation Eq. (13)–(14) makes the solution differentiable w.r.t. $(Q_r, \hat{x})$ so gradients flow through backpropagation. Implemented with CvxpyLayers (https://github.com/cvxgrp/cvxpylayers) + PyTorch.
- **Trainable reconciliation**: only Q is trainable ($\mathcal{S}$ fixed); trained with energy score on chronologically split base-validation data (80/20 train/validation); test set shared with base model.
- Pipeline: LSTM hidden states → PICNN → sample α uniformly → scenario set → DCL reconciliation → coherent scenarios.
- **Features**: weather (air temperature °C, dew point °C, hourly precipitation mm, from Meteostat Python API https://github.com/meteostat/meteostat-python using station lat/long, missing values linearly interpolated) + calendar (US-holiday boolean, weekday boolean, sin/cos of hour-of-day and hour-of-year).
- **Hyperparameters**: Adam lr 0.001, batch 64, max 200 epochs, context length T = 7×24 (168 h); LSTM 2 layers ×100 hidden; PICNN 2 layers ×40 hidden, activation per layer ReLU then Gaussian softplus (best combo in ablation, Table VII); MLP baseline 2–4 layers ×100–250 neurons trained with summed pinball loss over α ∈ {0.05,...,0.95}; DeepAR/DeepVAR 2 LSTM layers ×100. Hardware: 36-core 3 GHz server, RTX 3080, Python 3.8, PyTorch 1.13, Cvxpylayers 0.1.5, CUDA 11.7.

## 📊 Dataset & Input Features
- **[[Caltech_ACN]]** (Lee, Li & Low, "ACN-Data: Analysis and applications of an open EV charging dataset", ACM e-Energy 2019): three California EVCSs — **Caltech**, **JPL** (NASA Jet Propulsion Laboratory), **Office001** (Silicon Valley office building). Records delivered energy (kWh) per anonymous charging session plus start/end time and charging-pile ID; aggregated to **hourly charging demand** per station + Total (3 bottom series + 1 top).
- Period: **Jan 15, 2019 – Mar 15, 2020** (14 months, pre-COVID to avoid lockdown distortion). Splits: first 12 months training / next month validation / final month test; DCL further splits validation 80/20.
- Weather covariates from Meteostat API (NOAA open data): https://github.com/meteostat/meteostat-python
- Code references: PICNN structure from Convex Potential Flows implementation https://github.com/CW-Huang/CP-Flow ; DCL https://github.com/cvxgrp/cvxpylayers
- No explicit data-availability statement beyond use of the open ACN dataset.

## 📈 Performance & Results
- **Point forecasting (test set, Table I)** — proposed LSTM+PICNN vs baselines (MAE; proposed error ≈ 30% of DeepVAR for Total):

| Target | Proposed | DeepVAR | DeepAR | MLP |
|---|---|---|---|---|
| Caltech | 0.7981 | 3.7841 | 3.6892 | 4.9952 |
| JPL | 2.3712 | 5.7988 | 9.6658 | 8.9547 |
| Office001 | 0.1825 | 0.9279 | 1.5436 | 1.3682 |
| Total | 2.1546 | 7.4028 | 9.6734 | 13.4911 |

- **Probabilistic evaluation (Table II)**: best on nearly all metrics/stations (QL at all α levels, Winkler Score), except QL(0.7)/QL(0.8) on Total where DeepVAR slightly better. Quantile performance asymmetric in α — large α harder due to skewed demand distributions.
- **Reconciliation (Tables III–IV)**, energy score on 1,000 sampled scenarios:
  - Original unreconciled: 17.2015 → $Q_{id}$ (identity): 15.3431; $Q_{coef}$ (inverse error correlation): 15.7225; **learned $Q_{DCL}$: 14.2982** (~83% of original, ANOVA-significant improvement).
  - MAE after reconciliation: overall reduced ~14.6% across the four series; dominates all targets except Caltech (negligible difference). $Q_{DCL}$ scenarios visibly more compact and closer to actuals (Fig. 9); $Q_{coef}$/similar to $Q_{id}$ performance.
- **Sensitivity (Tables V–VI)**: at 48/72/96-hour horizons proposed method still significantly best; $Q_{coef}$/$Q_{id}$ can be *worse* than unreconciled scenarios at 72/96 h while $Q_{DCL}$ remains better (diminishing gains with horizon).
- **DCL compute cost**: forward/gradient per epoch 61.97/27.97 s (24 h horizon) → 115.65/33.77 s (96 h) — efficient scaling.

## 💡 Limitations & Identified Research Gaps
- Only a flat two-level hierarchy (3 stations + total) tested; authors state future work on more complicated hierarchical structures (grouped/nested trees).
- Reconciliation applied to sampled scenarios rather than full predictive distributions (linear constraints on random variables induce intractable convolutions of CDFs/PDFs).
- Probabilistic quality degrades at high quantile levels (skewed demand); forecast accuracy declines with longer horizons.
- No exploration of alternative forecasting engines or cross-domain transfer; deterministic single-run case study on one dataset/workplaces only.

## 📚 BibTeX & Citation Reference
```bibtex
@article{zheng2025coherent,
  author  = {Zheng, Kedi and Xu, Hanwei and Long, Zeyang and Wang, Yi and Chen, Qixin},
  title   = {Coherent Hierarchical Probabilistic Forecasting of Electric Vehicle Charging Demand},
  journal = {IEEE Transactions on Industry Applications},
  volume  = {61},
  number  = {1},
  pages   = {1329--1340},
  year    = {2025},
  doi     = {10.1109/TIA.2023.3344544}
}
```

## 🔗 Key References & Citation Graph
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM forecasting engine (Eq. 7)
- [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — autoregressive probabilistic baseline [41]
- DeepVAR (Salinas et al., NeurIPS 2019 low-rank Gaussian copula) — multivariate baseline [42]
- [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] — ensemble hierarchical probabilistic EV load forecasting [23]
- [[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]] — RL-based EVCS load forecasting [20]
- [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]] — related deep multi-horizon architecture lineage
- Related vault papers: [[2023_Huang_MetaProbformer_EV_Load]], [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]], [[2024_Li_DiffPLF_Conditional_Diffusion_EV]], [[2021_Zhang_Probabilistic_Queuing_EV_Load]]
