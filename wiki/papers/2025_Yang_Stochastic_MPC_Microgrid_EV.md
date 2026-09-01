---
type: paper
title: "A Stochastic Model Predictive Control-Based Energy Management Approach for Microgrids With Electric Vehicles"
authors: [Weilin Yang, Haojie Fang, Dezhi Xu, Bin Jiang, Peng Shi]
year: 2025
journal_conference: "IEEE Transactions on Transportation Electrification, Vol. 11, No. 1, pp. 3137-3145"
doi_url: "https://doi.org/10.1109/TTE.2024.3435426"
models_used: ["[[MS_MPC]]", "[[MPC]]", "[[Latin_Hypercube_Sampling]]", "[[Scenario_Reduction]]"]
datasets_used: ["[[ELIA_Belgian_Grid]]", "[[NHTS_2009]]"]
features_used: ["[[Arrival_Departure_Time]]", "[[State_of_Charge]]", "[[Wind_Power]]", "[[Solar_Power]]", "[[Electricity_Tariff]]", "[[Baseload]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[Operating_Cost]]", "[[Unbalance_Deviation]]", "[[Computation_Time]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Stochastic MPC-Based Energy Management Approach for Microgrids With Electric Vehicles

## 🎯 Main Objective & Contribution
- Addresses uncertainties of EVs (arrival/departure times, initial SOC) in V2G microgrid energy management (EMS) coordinating wind turbines (WT), PV, battery energy storage (BES), an EV aggregator, and the main grid.
- Proposes a **two-layer stochastic [[MPC|MPC]] framework**:
  - **Upper layer**: [[MS_MPC]] (multiscenario MPC) with [[Latin_Hypercube_Sampling|LHS]] scenario sampling over EV count + arrival SOC uncertainties, minimizing total operating cost while mitigating prediction error.
  - **Scenario reduction**: a **two-stage simultaneous backward reduction** compresses thousands of sampled scenarios for computational tractability (vs. monolithic single-state EV models or brute-force scenario sets).
  - **Lower layer**: EV aggregator allocation model distributing charging/discharging power to individual EVs (including discharging/V2G, absent from prior two-layer works).
- Simulations confirm high cost-effectiveness at affordable computational burden; unbalanced deviation between EMS operating cost and actual optimum ≈ **3.38%**, better than RBC and deterministic MPC.

## 🧠 Methodology & Model Architecture
**System modeling** (microgrid = WT + PV + BES + EV aggregator + baseload + grid):
- Individual EV (**Eq. 1–5 – EV dynamics & constraints**):
$$e^i_{\text{EV}}(t+1) = e^i_{\text{EV}}(t) + \eta_{\text{EV}} p^i_{\text{EV},c}(t) - \frac{p^i_{\text{EV},d}(t)}{\eta_{\text{EV}}}$$
$$SOC_{\text{EV,min}} c_{\text{EV,bat}} \leq e^i_{\text{EV}}(t) \leq SOC_{\text{EV,max}} c_{\text{EV,bat}}, \quad p^i_{\text{EV}}(t) = \delta_{\text{EV}}(t) p^i_{\text{EV},c}(t) - (1-\delta_{\text{EV}}(t)) p^i_{\text{EV},d}(t)$$
$$0 \leq p^i_{\text{EV},c}(t) \leq \delta_{\text{EV}}(t) p_{\text{EV,ch}}, \quad 0 \leq p^i_{\text{EV},d}(t) \leq (1-\delta_{\text{EV}}(t)) p_{\text{EV,dch}}$$
- Uncertainty distributions (**Eq. 6 – Arrival/departure time Gaussian PDF**, Eq. 7 – daily travel distance log-normal PDF):
$$f_t = \frac{1}{\sqrt{2\pi}\sigma_1}\exp\left(-\frac{(t-\mu_1)^2}{2\sigma_1^2}\right), \qquad f_{d^i_{\text{EV}}} = \frac{1}{d\sigma_2\sqrt{2\pi}}\exp\left(-\frac{(\ln d-\mu_2)^2}{2\sigma_2^2}\right)$$
with arrival battery energy (**Eq. 8**): $e^i_{\text{EV,arr}} = c^i_{\text{EV,bat}} + d^i_{\text{EV}} e_{\text{EV,km}}$.
- EV aggregator (**Eq. 9–13 – Aggregator dynamics**):
$$E_{\text{agg}}(t+1) = \alpha_{\text{agg}} E_{\text{agg}}(t) + \eta_{\text{agg}} p_{\text{agg},c}(t) - \frac{p_{\text{agg},d}(t)}{\eta_{\text{agg}}} + \sum_{i=1}^{n} e^i_{\text{EV,arr}}(t) - \sum_{k=1}^{m} e^k_{\text{EV,lea}}(t)$$
$$0 \leq p_{\text{agg},c}(t) \leq \delta_{\text{agg}}(t) p_{\text{EV,ch}} n_{\text{EVs}}(t), \quad SOC_{\text{EV,min}} c_{\text{EV,bat}} n_{\text{EVs}}(t) \leq E_{\text{agg}}(t) \leq SOC_{\text{EV,max}} c_{\text{EV,bat}} n_{\text{EVs}}(t)$$
- BES model with cyclic DOD tracking (**Eq. 14–20**): $E_{\text{BES}}(t+1) = E_{\text{BES}}(t) + \eta_{\text{BES}} p_{\text{BES},c}(t) - p_{\text{BES},d}(t)/\eta_{\text{BES}}$ plus SOC bounds, binary-mode power limits, and recursive $DOD_{\text{BES},c/d}$ updates.
- **Upper-layer MS-MPC** (**Eq. 21–27 – Scenario-weighted cost minimization**):
$$\min_{p^j_{\text{agg}}, p^j_{\text{BES}}, p^j_{\text{G}}} \sum_{j=1}^{N_S} \rho_j \sum_{t=k}^{k+N_u-1} J_T(t), \quad J_T(t) = J^j_B(t) + J^j_G(t) + J^j_{\text{agg}}(t) + J_{WT}(t) + J_{PV}(t)$$
subject to per-scenario power balance (**Eq. 22**): $p_{WT}(t)+p_{PV}(t)+p^j_G(t) = p^j_{\text{BES}}(t)+p_{LD}(t)+p^j_{\text{agg}}(t)$, with costs:
$$J^j_{\text{agg}}(t) = C_{\text{agg}}\left(p^j_{\text{agg},c}+p^j_{\text{agg},d} + \eta_l E^j_{\text{agg}}(t)\right) \;\text{(Eq. 23 – EV battery degradation)}$$
$$J^j_B(t) = c_{\text{BES,SOC}}(SOC^j_{\text{BES}}-SOC_{\text{ref}})^2 + c_{\text{BES,p}}[(p^j_{\text{BES},c})^2-(p^j_{\text{BES},d})^2] + c_{DOD}[(DOD^j_{c})^2+(DOD^j_{d})^2] \;\text{(Eq. 24 – BES cost)}$$
and linear grid/WT/PV cost terms (**Eq. 25–27**): $J^j_G=c_G p^j_G$, $J_{WT}=c_{WT}p_{WT}$, $J_{PV}=c_{PV}p_{PV}$.
- **Lower-layer allocation** (**Eq. 28 – Individual EV power allocation**):
$$\min_{p^i_{\text{EV}}(t)} f(t) = \left|\sum_{i=1}^{n_{\text{EVs}}(t)} p^i_{\text{EV}}(t) - p_{\text{agg,upper}}^{ref}(t)\right| \quad \text{s.t. (1)-(5)}$$
- Sampling: LHS generates 1000 scenarios of available-EV counts + 1000 of initial SOCs; two-stage simultaneous backward reduction ([Dupacová et al.]) reduces both to 10 each → 100 combined scenarios; prediction horizon $N_u = 8$ steps @ 15 min. Solved in MATLAB with CPLEX via YALMIP.

## 📊 Dataset & Input Features
- Actual + forecast profiles of baseload, renewable generation (WT/PV), and electricity price compiled from the **Belgian Electricity Transmission System operator (Elia)** database.
  - URL/data availability: http://www.elia.be/en (ref [29]).
- EV behavioral statistics (arrival/departure times, stored energy levels) characterized by probability distributions based on the **National Household Travel Survey** driving-pattern analysis (refs [21][22]).
- Fleet size: **100 EVs**; simulation day with 15-min sampling intervals.

## 📈 Performance & Results
- Compared against **RBC** (rule-based, no receding horizon/stochastic optimization), **D-MPC** (single deterministic scenario), and **OS-MPC** (multiscenario without reduction).
- Cost: RBC has highest operating cost; all three MPC variants significantly reduce total EMS operating cost; MS-MPC and OS-MPC further reduce cost vs D-MPC thanks to multiscenario sampling under forecast uncertainty.
- Unbalance deviation between obtained EMS operating cost and actual optimum ≈ **3.38%** for MS-MPC — smaller than RBC and D-MPC, similar to OS-MPC.
- Computation: multiscenario methods need longer per-step time than RBC/D-MPC, but two-stage scenario reduction lets **MS-MPC significantly cut computation time vs OS-MPC** while preserving economic performance.
- Qualitative findings: EV aggregator discharges during high-demand periods (8:00–12:00, 14:00–17:00) to support the microgrid; charging is shifted to low-demand windows (12:30–15:30); strategy achieves peak shaving/load leveling vs unguided random charging that concentrates load in peak-price periods; individual SOC curves track aggregator power, with wide SOC spread at 7:30 converging by 9:00 and dropping during 11:00/16:00 discharge support.

## 💡 Limitations & Identified Research Gaps
- Only EV-related uncertainties are modeled stochastically; WT/PV/baseload/price forecasts treated as given (authors' future work: "more uncertain elements in the microgrid").
- Computational burden still exceeds RBC/D-MPC due to multiscenario sampling.
- No real-world/hardware validation; simulation only, single-day case study, 100-EV fleet.
- Forecasting itself is not learned — EV uncertainty comes from parametric (Gaussian/log-normal) distribution sampling rather than data-driven forecast models; links directly to the thesis question of how EV load forecasting quality propagates into EMS scheduling performance.

## 📚 BibTeX & Citation Reference
```bibtex
@article{yang2025msmpc,
  title   = {A Stochastic Model Predictive Control-Based Energy Management Approach for Microgrids With Electric Vehicles},
  author  = {Yang, Weilin and Fang, Haojie and Xu, Dezhi and Jiang, Bin and Shi, Peng},
  journal = {IEEE Transactions on Transportation Electrification},
  volume  = {11},
  number  = {1},
  pages   = {3137--3145},
  year    = {2025},
  doi     = {10.1109/TTE.2024.3435426}
}
```

## 🔗 Key References & Citation Graph
- [[2021_Huang_Lyapunov_EV_Scheduling]] — related online/real-time EV scheduling optimization in the vault
- [[2014_Alizadeh_Scalable_Stochastic_EV_Demand]] — probabilistic modeling of aggregate EV charging demand underlying aggregation approaches
- [[2021_Zhang_Probabilistic_Queuing_EV_Load]] — probabilistic EV load characterization feeding scheduling decisions
- [[2024_Zhong_V2G_SVE_Evaluation_Metric]] — vault note on evaluating load forecasts specifically in V2G scheduling contexts
- [[PC-M3]] — related physics-constrained real-time energy management of EV clusters
