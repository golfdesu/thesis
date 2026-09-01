---
type: paper
title: "A Reliable Evaluation Metric for Electrical Load Forecasts in V2G Scheduling Considering Statistical Features of EV Charging"
authors: [Jiahao Zhong, Xiang Lei, Ziyun Shao, Linni Jian]
year: 2024
journal_conference: "IEEE Transactions on Smart Grid, vol. 15, no. 5, pp. 4917-4930"
doi_url: "https://doi.org/10.1109/TSG.2024.3392910"
models_used: ["[[V2G-SVE]]", "[[Aggregate_EV_Fleet_Model]]", "MLP", "MLR", "Simple Average (SA)", "1-same-day persistence"]
datasets_used: ["[[ASU_Campus_Metabolism_Dataset]]", "[[Ausgrid_Zone_Substation_Dataset]]"]
features_used: ["[[Base_Electrical_Load]]", "[[Arrival_Departure_Time]]", "[[State_of_Charge]]", "[[Battery_Capacity]]", "[[Calendar_Features]]", "[[Historical_Load]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[V2G-SVE]]", "SPDR", "[[MAPE]]", "[[RMSE]]", "[[MAE]]", "[[Pearson_Correlation_Coefficient]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Reliable Evaluation Metric for Electrical Load Forecasts in V2G Scheduling Considering Statistical Features of EV Charging

## 🎯 Main Objective & Contribution
- Shows that prevailing **forecast quality metrics** ([[MAPE]], [[RMSE]], [[MAE]]) fail to predict how a forecast will perform when fed into downstream **[[V2G]]** optimization — the relation between forecast *quality* and forecast *value* is not monotonic.
- Proposes **V2G-SVE (V2G Scheduling Value Error)**: a value-oriented metric scoring a forecast by the relative degradation rate of load-variance-minimization scheduling performance caused by using it instead of actual load.
- Builds an **aggregate model of the EV fleet** parameterized by statistical features of EV charging so V2G-SVE computes in constant time (~0.20 s) regardless of fleet size, avoiding the curse of dimensionality of per-EV quadratic programming.
- Derives and experimentally verifies **three key findings** linking forecast errors to V2G scheduling degradation, with guidance for future forecasting loss design.

## 🧠 Methodology & Model Architecture

### V2G Scheduling Formulation (per-EV)
Objective: minimize daily load variance (**Eq. 1**) with average load (**Eq. 2**):
$$\min \frac{1}{T}\sum_{t=1}^{T}\left(\sum_{n=1}^{N}P^{\text{cha}}_{n,t} + \sum_{n=1}^{N}P^{\text{dis}}_{n,t} + P^{\text{con}}_t - P^{\text{ave}}\right)^2, \qquad P^{\text{ave}} = \frac{1}{T}\sum_{t=1}^{T}\left(\sum_{n=1}^{N}P^{\text{cha}}_{n,t} + \sum_{n=1}^{N}P^{\text{dis}}_{n,t} + P^{\text{con}}_t\right)$$
Constraints (**Eqs. 3-9**, energy requirement, SOC limits $SOC_{\max}=0.9$, $SOC_{\min}=0.1$, power limits, no simultaneous charge/discharge):
$$\eta^{\text{cha}}_n \sum_{t=t^{\text{arr}}_n}^{t^{\text{dep}}_n} P^{\text{cha}}_{n,t} + \frac{1}{\eta^{\text{dis}}_n}\sum_{t=t^{\text{arr}}_n}^{t^{\text{dep}}_n} P^{\text{dis}}_{n,t} = \left(SOC^{\text{dep}}_n - SOC^{\text{arr}}_n\right)\times B_n$$
$$\eta^{\text{cha}}_n \sum_{t=t^{\text{arr}}_n}^{t'} P^{\text{cha}}_{n,t} + \frac{1}{\eta^{\text{dis}}_n}\sum_{t=t^{\text{arr}}_n}^{t'} P^{\text{dis}}_{n,t} \le \left(SOC_{\max}-SOC^{\text{arr}}_n\right)\times B_n, \qquad -\eta^{\text{cha}}_n \sum_{t=t^{\text{arr}}_n}^{t'} P^{\text{cha}}_{n,t} - \frac{1}{\eta^{\text{dis}}_n}\sum_{t=t^{\text{arr}}_n}^{t'} P^{\text{dis}}_{n,t} \le -\left(SOC_{\min}-SOC^{\text{arr}}_n\right)\times B_n$$
$$t'\in[t^{\text{arr}}_n, t^{\text{dep}}_n], \quad 0\le P^{\text{cha}}_{n,t}\le P^{\text{cha},\max}_n, \quad P^{\text{dis},\max}_n \le P^{\text{dis}}_{n,t}\le 0, \quad P^{\text{cha}}_{n,t}\times P^{\text{dis}}_{n,t}=0 \;\; \forall n,\forall t$$

### Forecast Quality Metric Baselines (**Eqs. 10-12**)
$$\text{MAPE} = \frac{1}{T}\sum_{i=1}^{T}\left|\frac{y_i-\hat{y}_i}{y_i}\right|\times 100\%, \qquad \text{RMSE} = \sqrt{\frac{1}{T}\sum_{i=1}^{T}(y_i-\hat{y}_i)^2}, \qquad \text{MAE} = \frac{1}{T}\sum_{i=1}^{T}|y_i-\hat{y}_i|$$

### Three Key Findings + Mathematical Proof
Simplified 3-slot convex QP with unit efficiencies (**Eqs. 13-16**):
$$\min_{x_1,x_2,x_3} f(x) = \frac{1}{3}\left(x_1^2+x_2^2+x_3^2+2ax_1+2bx_2+2cx_3\right), \quad a,b,c = P^{\text{con}}_1-P^{\text{ave}}, P^{\text{con}}_2-P^{\text{ave}}, P^{\text{con}}_3-P^{\text{ave}}$$
$$f(\mathbf{x}) = \frac{1}{2}\mathbf{x}^T H\mathbf{x} + \mathbf{c}^T X \;(H \text{ positive definite}), \qquad x_1+x_2+x_3=E, \quad P^- \le x_1 \le P^+$$
Lagrangian + [[KKT_conditions]] (**Eq. 19-20**) yield analytic optimal charging powers (**Eq. 21**); with forecast errors $\{\varepsilon_1,\varepsilon_2,\varepsilon_3\}$ the realized power is (**Eq. 22**):
$$x_1 = \frac{-2(P^{\text{con}}_1+\varepsilon_1)+(P^{\text{con}}_2+\varepsilon_2)+(P^{\text{con}}_3+\varepsilon_3)-3\mu_1+3\mu_2+E}{3} = \frac{-2\varepsilon_1+\varepsilon_2+\varepsilon_3}{3} + x^*_1$$
With $I = (-2\varepsilon_1+\varepsilon_2+\varepsilon_3)/3$: uniform errors in magnitude and direction leave inter-period load differentials unchanged → $I=0$ and realized schedule equals optimal (**Finding 3 proved**). Piecewise analysis of $x_1 - x^*_1$ (**Eqs. 24-26**, bounded by $[0, P^+-P^-]$) proves errors matter more in dense-EV periods (**Finding 1**) and that error-direction impact is asymmetric and not always positively correlated with magnitude (**Finding 2**).

### Aggregate Model of EV Fleet
EVs split into uncoordinated (charge at max power until departure) vs coordinated; max energy acquired/released (**Eqs. 27-28**):
$$e^{\text{cha}}_n = \left(SOC^{\max}_n - SOC^{\text{arr}}_n\right)\times B_n, \qquad e^{\text{dis}}_n = \left(SOC^{\min}_n - SOC^{\text{arr}}_n\right)\times B_n$$
Average battery capacity from sales-share weighting over $C$ models (**Eq. 29**):
$$B_{\text{ave}} = \sum_{c=1}^{C}\left( S_c \Big/ \sum_{c=1}^{C} S_c \times B_c\right)$$
Fleet energy requirement, uncoordinated ($N'$) + coordinated ($N''$) EVs (**Eqs. 30-31**):
$$E_{\text{need}} = \sum_{n'=1}^{N'}\left(t^{\text{dep}}_{n'}-t^{\text{arr}}_{n'}\right)\times \eta_{n'}\times t\times P^{\text{cha},\max}_{n'} + \sum_{n''=1}^{N''}\left(SOC^{\text{dep}}_{n''}-SOC^{\text{arr}}_{n''}\right)\times B_{n''}, \quad N'+N''=N$$
Aggregate scheduling problem (**Eqs. 32-38**, $\eta^{\text{cha}}=\eta^{\text{dis}}=0.95$):
$$\min \frac{1}{T}\sum_{t=1}^{T}\left(P^{\text{cha}}_t+P^{\text{dis}}_t+P^{\text{con}}_t-P^{\text{ave}}\right)^2$$
s.t. $\eta^{\text{cha}}\sum_t P^{\text{cha}}_t + \frac{1}{\eta^{\text{dis}}}\sum_t P^{\text{dis}}_t = E_{\text{need}}$; cumulative energy bounds $E^-_{t'} \le \eta^{\text{cha}}\sum^{t'} P^{\text{cha}}_t + \frac{1}{\eta^{\text{dis}}}\sum^{t'} P^{\text{dis}}_t \le E^+_{t'}$; $0\le P^{\text{cha}}_t\le P^+_t$, $P^-_t\le P^{\text{dis}}_t\le 0$, $P^{\text{cha}}_t P^{\text{dis}}_t=0$. Each arrival-departure period pair contributes one synthetic EV (fleet treated as 4656 aggregated EVs = sum 1..96), with $SOC^{\text{arr}}=0.35$, $SOC^{\text{dep}}=0.65$.

### V2G-SVE Calculation (**Eqs. 39-40**)
4 steps: build aggregate constraints from statistical features → solve with actual load to get optimal variance $V_1$ → solve plan with forecasted load but evaluate on actual load:
$$V_2 = \frac{1}{T}\sum_{t=1}^{T}\left(P^{\text{cha}}_t+P^{\text{dis}}_t+P^{\text{act}}_t-P^{\text{ave}}\right)^2, \qquad \boxed{\text{V2G-SVE} = \frac{V_2-V_1}{V_1}\times 100\%}$$
Lower score = better forecast. Companion ground-truth metric for specific datasets (**Eq. 41**):
$$\text{SPDR} = \frac{Var^{\text{fore}} - Var^{\text{act}}}{Var^{\text{act}}}\times 100\%$$

## 📊 Dataset & Input Features
- **[[ASU_Campus_Metabolism_Dataset]]**: electrical load of Arizona State University's Tempe campus, **15-minute resolution** (T=96 periods/day), via interactive web tool "Campus Metabolism System". Base load Jan 15, 2022 fluctuating 11,000–17,000 kW (main experiments); Oct 15, 2022 used for generalization tests (also at 1-hour resolution). URL: https://cm.asu.edu (accessed Sep 15, 2023).
- **[[Ausgrid_Zone_Substation_Dataset]]**: real-world large-scale load from Ausgrid (>180 zone substations, NSW, Australia); five substations' consumption aggregated, workdays June 1 – Aug 27, 2021, 15-min resolution; first 54 days train / last 10 days test. URL: https://www.ausgrid.com.au/Industry/Our-Research/Data-to-share/Distribution-zone-substation-data (accessed Jan 31, 2024).
- **Synthetic EV charging data** generated from statistical features: category 1 (70%): arrival ~ Normal($\mu$=6:00, $\sigma$=60 min), departure ~ Normal($\mu$=18:00, $\sigma$=120 min); category 2 (30%): $t^{\text{arr}}\sim U(1,T)$, $t^{\text{dep}}\sim U(t^{\text{arr}},T)$; $SOC^{\text{arr}}\sim U[0.2,0.5]$, $SOC^{\text{dep}}\sim U[0.5,0.8]$; battery capacity/rated power sampled from nine best-selling US EV models proportional to market sales share (per https://insideevs.com/news/631099/us-bev-dominated-us-made-models/); #EVs ~ Normal($N$, 5%·$N$), N ∈ {50, 100, 150, 200}. No public code/data repository stated in the text.
- Forecasting inputs for MLR/MLP: historical load (same periods previous week) + calendar information.

## 📈 Performance & Results
- **Quality metrics are unreliable**: 6 experimental groups (+200/+500/+1000 kW and −200/−500/−1000 kW single-period errors, base load 110–170 MW-scale, schedulable power 0–1150 kW at N=100) show identical RMSE/MAE scores can produce substantially different scheduling results; MAPE contradicts scheduling impact in low-load windows (7:30–9:00, after 20:00); all three ignore error direction.
- **Metric reliability**: 100 synthetic forecasts (MAPE 0.1%→10%). Pearson correlation between metric scores and actual scheduling performance: **V2G-SVE > 0.99 across all three experiments (N = 100, 95, 105), significantly surpassing MAPE, RMSE, MAE**. Scheduling performance loses monotonicity vs MAPE once MAPE > 2%; V2G-SVE tracks it throughout.
- **Generalizability**: on Oct 15, 2022 base load with modified arrival/departure distributions (μ=8:00 σ=120 min arrivals; μ=20:00 σ=60 min departures), V2G-SVE ≈ SPDR along the diagonal for 50/100/150/200 EVs; robust under 1-hour time resolution too (errors hurt more at coarser resolution).
- **Model selection reversal (Ausgrid case study)**:

| Day-ahead forecaster | Best by quality? | Avg SPDR |
| :--- | :--- | :---: |
| MLP (97-192-96 neurons, 3 layers) | No | **0.30% (best value)** |
| SA (simple average) | No | 0.35% |
| MLR | **Yes (lowest MAPE/RMSE/MAE)** | 0.36% |
| 1-same-day persistence | — | worse |

  Best quality ≠ best value: choosing by MAPE/RMSE would pick MLR, but MLP gives best V2G scheduling; V2G-SVE ranks match SPDR per day. Worst SPDR on test day 6 for all models — forecasts misidentified peak periods as valleys (consistent with Finding 3).
- **Online vs offline**: basic online scheduling achieves avg SPDR = **5.61%**, far worse than forecast-based day-ahead scheduling (~0.30–0.36%) — forecasts are worth using; V2G-SVE helps select them.
- **Computation**: V2G-SVE solving time constant ≈ **0.20 s** regardless of EV count; direct per-EV SPDR grows exponentially, fitted by cubic (**Eq. 42**) and infeasible beyond 200 EVs on a 64 GB RAM workstation:
$$y_t = 0.0002N^3 + 0.0228N^2 - 0.6102N + 2.5844$$

## 💡 Limitations & Identified Research Gaps
- V2G-SVE reliability presupposes actual EV charging behavior follows the predefined statistical features; impractical when few EVs or statistically irregular behavior.
- Metric tied to the load-variance-minimization objective; may not transfer to other V2G scheduling objectives (different stakeholders/objectives need re-derived value metrics).
- Non-uniformity: metric built on aggregate model while ground-truth performance solved directly per-EV; conventional solvers hit resource limits at scale.
- Future directions: custom differentiable loss functions weighting dense-EV periods more heavily; using inter-period **load differences** as forecasting inputs rather than raw historical loads; integrating forecasting and optimization (predict-and-optimize); advanced scheduling algorithms could improve both metric construction and validation.

## 📚 BibTeX & Citation Reference
```bibtex
@article{zhong2024v2gsve,
  author  = {Zhong, Jiahao and Lei, Xiang and Shao, Ziyun and Jian, Linni},
  title   = {A Reliable Evaluation Metric for Electrical Load Forecasts in {V2G} Scheduling Considering Statistical Features of {EV} Charging},
  journal = {IEEE Transactions on Smart Grid},
  year    = {2024},
  volume  = {15},
  number  = {5},
  pages   = {4917--4930},
  doi     = {10.1109/TSG.2024.3392910}
}
```

## 🔗 Key References & Citation Graph
- Murphy 1993, "What is a good forecast?" — origin of forecast quality vs value concepts [12]
- Zhang, Hu, Xu & Song, IEEE Trans. Power Syst. 2017 — aggregate PEV model for achievable V2G capacity (basis of the fleet aggregate model) [35]
- Zhang, Wang & Hug 2022, "Cost-oriented load forecasting" — differentiable cost loss function inspiration [41]
- Haben et al. 2014 — alternative error measure for household-level forecasts [16]
- Chen, Yang, Liu & Wu 2022 — forecast value via unit commitment dispatch costs [19]
- Jian et al., IEEE Trans. Ind. Electron. 2013 — regulated charging minimizing load variance (15-min period setting) [27]
- Koufakis et al., IEEE TITS 2020 — offline/online EV charging scheduling with V2V [39]
- Stratigakos et al. 2022 — prescriptive trees for integrated forecasting and optimization [43]
- Zhao, Wan & Song 2022 — cost-oriented prediction intervals bridging forecasting and decision [44]
- Sortomme et al., IEEE Trans. Smart Grid 2011 — coordinated charging to minimize distribution losses [21]

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2024_V2G_SVE_Evaluation_Metric_refs]]
