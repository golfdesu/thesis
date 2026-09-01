---
type: paper
title: "Day-ahead Electric Vehicle Charging Behavior Forecasting and Schedulable Capacity Calculation for Electric Vehicle Parking Lot"
authors: [Maosheng Xu, Shan Gao, Junyi Zheng, Xueliang Huang, Chuanshen Wu]
year: 2024
journal_conference: "Energy, vol. 309, 133090"
doi_url: "https://doi.org/10.1016/j.energy.2024.133090"
models_used: ["[[ADMM-NN]]", "[[KMeans_Clustering]]", "[[EVSFD]]", "[[Monte_Carlo_Sampling]]"]
datasets_used: ["[[Suzhou_EVPL_Dataset]]", "[[PJM_Day_Ahead_Tariff]]", "[[NMMV_Platform_Data]]"]
features_used: ["[[EV_Access_Time]]", "[[Access_Duration]]", "[[State_of_Charge]]", "[[State_of_Charge]]", "[[Calendar_Features]]", "[[Holiday_Flag]]", "[[Weather_Conditions]]", "[[Temperature]]", "[[Recent_Access_Pattern]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["Forecast Accuracy", "Charging Cost Reduction"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Day-ahead EV Charging Behavior Forecasting and Schedulable Capacity Calculation for Electric Vehicle Parking Lot

## 🎯 Main Objective & Contribution
- Enables **Electric Vehicle Parking Lots (EVPLs)** to participate in day-ahead energy and ancillary services markets via [[V2G]] by forecasting **EV Charging Behavior (EVCB)** day-ahead and computing **EV Schedulable Capacity (EVSC)** from those forecasts.
- Three contributions: (1) a **day-ahead Time-of-Use (TOU) EVCB forecasting method** combining an [[ADMM-NN]] for hourly EV access numbers with TOU [[KMeans_Clustering]] clustering of historical EVCB into typical behavior sets (376 clusters), minimizing idealized assumptions; (2) classification of EVCB types + construction of the **EV Scheduling Feasible Domain (EVSFD)** under physical constraints; (3) an EVSC calculation method based on the day-ahead planning curve within the EVSFD.
- Contrasts with model-driven Monte Carlo/PDF approaches (require assumptions on EV counts/targets/durations — infeasible when daily EVPL access varies with climate/date/user willingness) and data-driven load-profile methods (only forecast disorderly charging profiles, unusable for V2G scheduling).

## 🧠 Methodology & Model Architecture

### EVCB Model
Each accessed EV is modeled (**Eq. 2-3**) as:
$$EV_n = \{t^a_n,\ t^{ad}_n,\ S_{n,t^a_n},\ S_{n,t^d_n}\}, \qquad t^{ad}_n = t^d_n - t^a_n;\ \ S_{n,t}=S_{n,t^a_n}\ (t=t^a_n);\ \ S_{n,t}\ge S_{n,t^d_n}\ (t=t^d_n)$$
Only slow-charging EVs with long access durations are modeled (fast charging = uncontrollable, zero schedulable potential).

### A. ADNN-trained Neural Network: Day-Ahead EV Access Number Forecast
Day split into 24 one-hour periods; one model per period. Inputs: day-of-week, holiday flag, weather (sunny/cloudy/rainy/snowy), average temperature, recent-days access-number pattern. Architecture: **10 → 200 → 200 → 1** neurons; output (**Eq. 4**):
$$y = W_3 f_2(W_2 f_1(z_1 = W_1 x + b_1) + b_2) + b_3$$
Trained via **[[ADMM]]** instead of SGD to avoid vanishing gradients/local optima. Training problem (**Eqs. 5-6**):
$$\min_{W_l,b_l,z_l,a_l} F(\mathbf{W},\mathbf{b},\mathbf{z},\mathbf{a}) = L(z_3;y) + \sum_{l=1}^{3}R_l(W_l)$$
$$\text{s.t. } z_1 = W_1a_0+b_1,\ a_1=f_1(z_1);\ z_2=W_2a_1+b_2,\ a_2=f_2(z_2);\ z_3=W_3a_2+b_3$$
with loss $L(z_3;y)=\frac{1}{n}\sum_{i=1}^{n}(z^3_i - y_i)^2$. Augmented Lagrangian with $\ell_2$ penalty (**Eq. 7**, tuning parameter $v>0$, dual variable $u$, hyperparameter $\rho>0$):
$$L_\rho(\mathbf{W},\mathbf{b},\mathbf{z},\mathbf{a},u) = L(z_3;y)+\sum_{l=1}^{3}R_l(W_l)+\frac{1}{2v}\sum_{l=1}^{2}\left(\|z_l - W_la_{l-1}-b_l\|_2^2 + \|a_l-f_l(z_l)\|_2^2\right) + u^T(z_3-W_3a_2-b_3) + \frac{\rho}{2}\|z_3-W_3a_2-b_3\|_2^2$$
Layer parameters updated sequentially back-to-front through reciprocal iterations.

### B. TOU K-Means++ Clustering of Typical EVCB
Clustering feature vector per historical record (**Eq. 8**): $\mathbf{EV_i} = [t^a_i,\ t^{ad}_i,\ S_{i,t^a_i},\ S_{i,t^d_i}]$, normalized to [0,1]. Records grouped by access time into 24 periods; K-Means++ (deterministic far-apart seeding; elbow method for K) clusters each period. Typical set per period $t$ (**Eq. 9**) and full set (**Eq. 10**):
$$C_t = \left\{\left((t^a_{t,k},\ t^{ad}_{t,k},\ S_{t,k,t^a_{t,k}},\ S_{t,k,t^d_{t,k}}),\ \varphi_{t,k}\right),\ k\in[1,k_t]\right\}, \qquad C=\{C_t,\ t\in[1,24]\}$$
where $\varphi_{t,k}$ = percentage share of the $k$-th typical EVCB in period $t$.

### C. Day-Ahead EVCB Forecast Process (Algorithm 1)
For each period: forecast $N_t$ via trained NN; then cluster count $N_{t,k} = N_t \times \varphi_{t,k}$; add $N_{t,k}$ copies of each typical EVCB to forecast result $F$.

### D. EVSFD Construction
Feasible domain $A_n$ boundaries: (A) SoC limits $S^{\min}_n \le S_{n,t}\le S^{\max}_n$ (**Eq. 12**); (B) power limits $p^{\min}_n \le p_{n,t}\le p^{\max}_n$ (**Eq. 13**) with effective SoC-rate power (**Eq. 14**) and SoC accumulation (**Eq. 15**):
$$p'_{n,t} = \begin{cases}\eta^{ch}_n p_{n,t} & p_{n,t}\ge 0\\ p_{n,t}/\eta^{dis}_n & p_{n,t}<0\end{cases}, \qquad S_{n,t^\tau_n} = S_{n,t^a_n} + \sum_{t=t^a_n}^{t^\tau_n}\frac{p'_{n,t}}{C_n\Delta t}$$
Boundary **B1** (always max-power charging, Eq. 16) and **B2** (always min-power, Eq. 17):
$$S_{n,t^\tau_n} = S_{n,t^a_n} + \frac{\eta^{ch}_n p^{max}_n}{C_n}(t^\tau_n - t^a_n), \qquad S_{n,t^\tau_n} = S_{n,t^a_n} + \frac{p^{min}_n}{\eta^{dis}_n C_n}(t^\tau_n - t^a_n)$$
(C) User travel-demand boundary at departure (**Eqs. 18-19**): $S_{n,t}\ge S_{n,t^d_n}$ at $t=t^d_n$, giving $S_{n,t^\tau_n} \ge S_{n,t^d_n} - \frac{\eta^{ch}_np^{max}_n}{C_n}(t^d_n-t^\tau_n)$.
Three EVCB cluster classes: **A** (all six boundaries triggered; low SoC, long access), **B** (partial boundaries; short $t^{ad}$, large $S^{ad}$), **C** (no feasible domain — cannot meet energy demand even at max power; EVSC ≡ 0).

### E. Day-Ahead Scheduling & EVSC Calculation
Cost-minimizing schedule against day-ahead tariff $\lambda_t$ (**Eqs. 20-21**):
$$\min_{p_{n,t}} f^{EVA} = \sum_{t=1}^{T}\sum_{n=1}^{N}\lambda_t p_{n,t} \quad \text{s.t. power limits; SoC recursion within } (t,S_{n,t})\in A_n$$
$$S_{n,t+1} = \begin{cases} S_{n,t}+\frac{\eta^{ch}_np_{n,t}}{C_n}\Delta t & p_{n,t}\ge 0\\ S_{n,t}+\frac{p_{n,t}}{\eta^{dis}_nC_n}\Delta t & p_{n,t}<0\end{cases}$$
Per-EV schedulable capacity in non-crossing states (**Eq. 23**) plus three crossing cases (**Eqs. 24-26**), e.g.:
$$p^{sc}_{n,t}=[p_{n,t}-p^{\min}_n,\ p^{\max}_n-p_{n,t}], \qquad p^{sc}_{n,t}=\left[\frac{(S^{\min}_n-S_{n,t})\eta^{dis}_n C_n}{\Delta t}-p_{n,t},\ p^{\max}_n-p_{n,t}\right]$$
Aggregation over process (**Eq. 27**) and fleet (**Eq. 28**):
$$SC_n=\{p^{sc}_{n,t},\ t\in[t^a_n,t^d_n)\}, \qquad EVSC=\left\{\sum_{n=1}^{N}p^{sc}_{n,t},\ t\in[0,24h)\right\}$$

## 📊 Dataset & Input Features
- **[[Suzhou_EVPL_Dataset]]**: actual historical EVCB data from **China's National Monitoring and Management Platform for New Energy Vehicles (NMMV)**, recorded **January 2022 in Suzhou city, China**; **>10,000 historical EVCB records** ($t^a, t^d, S^a, S^d$); test set = 29 January (528 records), rest training. Meteorological data (weather condition, min/max temperature) from publicly available meteorological websites.
- Parameters: battery capacity 48 kWh; max charge/discharge power ±7 kW; $\eta^{ch}=\eta^{dis}=0.98$; minimum scheduling interval **3 minutes**.
- Tariff: **day-ahead hourly PJM electricity market prices as of 29 January 2022**.
- **Data availability statement**: "The data that has been used is confidential." Open-access author version: https://orca.cardiff.ac.uk/id/eprint/172146/ ; publisher page https://doi.org/10.1016/j.energy.2024.133090. No public code/data repository.

## 📈 Performance & Results
- **Case 1 (access number)**: NN forecasts hourly EV access numbers for 29 January with **88.5% average accuracy**; Monte Carlo baseline cannot even produce this forecast since total daily EV count is unknown a priori.
- **Case 2 (clustering)**: **376 typical EVCB clusters** across 24 periods; most accesses/clusters occur evening–late night (peak hour [21,22): 2150 EVs, 32 clusters). Of typical EVCBs, **76.3% have $t^{ad}>2h$** (46.3% >4 h, 32.2% >6 h); **67.6% expect $S^{ad}>40\%$** (35.9% >60%, 9.8% >80%).
- **Case 3 (EVCB forecast)**: forecast distributions closely match actuals, e.g., $S^d$: 87.9% actual vs 88.4% forecast in (80,100] bin; duration distribution: >2 h actual 68.2% vs forecast 73.2%; >6 h 25.0% vs 23.3%.
- **Case 4 (day-ahead plan)**: plan curve built on forecasted EVCB nearly coincides with that built on actual EVCB; ordered charging under PJM tariffs cuts EVPL charging cost by **15.3%** vs disordered charging.
- **Cases 5-6 (EVSC)**: EVSC computed from forecasted vs actual EVCB are close; cheap-price hours (0-8, 12-16) yield max-power charging → minimal upward but large downward SC; expensive hours (9-12, 17-24) yield larger SC for ancillary services. **EVs with $t^{ad}>6$h are only 25% of the fleet but provide 56.2% of total EVSC** (actual; 43.2% forecast); EVs with <2 h (~30% of fleet) contribute <7%.

## 💡 Limitations & Identified Research Gaps
- Only slow-charging EVs modeled; fast-charging loads treated as uncontrollable.
- Real-time scheduling strategy impact on EVSC calculation not analyzed — flagged as future work.
- Further research planned on EVSC mining across different scenarios/EV clusters in EVPLs.
- Cluster-C EVs (no feasible domain) contribute nothing to V2G; incentive design could target longer access durations.

## 📚 BibTeX & Citation Reference
```bibtex
@article{xu2024dayahead,
  author  = {Xu, Maosheng and Gao, Shan and Zheng, Junyi and Huang, Xueliang and Wu, Chuanshen},
  title   = {Day-ahead electric vehicle charging behavior forecasting and schedulable capacity calculation for electric vehicle parking lot},
  journal = {Energy},
  year    = {2024},
  volume  = {309},
  pages   = {133090},
  doi     = {10.1016/j.energy.2024.133090}
}
```

## 🔗 Key References & Citation Graph
- Zhang, Hu, Xu & Song, IEEE Trans. Power Syst. 2017 — aggregate PEV model for achievable V2G capacity [30] (also used by [[2024_Zhong_V2G_SVE_Evaluation_Metric]])
- Taylor et al., ICML 2016 — gradient-free ADMM neural network training [33]
- Wang, Yu, Chen & Zhao, KDD 2019 — ADMM for deep learning with global convergence [35]
- Arthur & Vassilvitskii, SODA 2007 — [[KMeans_Clustering]] careful seeding [37]
- Han, Han & Sezaki, IEEE Trans. Smart Grid 2011 — V2G frequency-regulation capacity estimation [27]
- Yao, Wong & Schober, IEEE Trans. Smart Grid 2018 — aggregate PEV capacity for day-ahead frequency regulation [10]
- Cui, Hu & Luo, IEEE TIA 2020 — day-ahead charging + frequency reserve scheduling under regulation-signal uncertainty [9]
- Mao et al., J. Mod. Power Syst. Clean Energy 2019 — big-data-based schedulable capacity forecasting [31]
- Zhang, Chan et al., IEEE Trans. Cybernetics 2020 — deep-learning probabilistic EV charging load forecasting with queuing model [25] ([[2021_Zhang_Probabilistic_Queuing_EV_Load]])
- Nespoli, Ogliari & Leva, IEEE Access 2023 — user-behavior-clustering EV charging forecast [22]
