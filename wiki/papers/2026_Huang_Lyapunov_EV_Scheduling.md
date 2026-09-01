---
type: paper
title: "Forecast-Enhanced Lyapunov Optimization for Real-Time EV Charging Scheduling"
authors: [Shihan Huang, Yue Chen, Richard Chen, Adam Wierman]
year: 2026
journal_conference: "arXiv preprint arXiv:2604.16873 [math.OC]"
doi_url: "https://arxiv.org/abs/2604.16873"
models_used: ["[[Lyapunov_Optimization|Forecast-Enhanced Lyapunov Optimization]]", "[[MPC|RHC]]", "[[Queuing_Model]]", "[[Linear_Programming]]", "[[MPC]] (benchmark)"]
datasets_used: ["[[Shanghai_EV_Arrival_Data]]", "[[CAISO]]"]
features_used: ["[[EV_Arrival_Rate]]", "[[Electricity_Tariff]]", "[[Arrival_Departure_Time]]", "[[EV_Charging_Demand]]", "[[Charging_Power]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[Total_Cost]]", "[[Unit_Cost_USD_per_kWh]]", "[[Maximum_Charging_Delay]]", "[[Optimality_Gap]]", "[[Computational_Time]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Forecast-Enhanced Lyapunov Optimization for Real-Time EV Charging Scheduling

## 🎯 Main Objective & Contribution
- **First work to incorporate short-term forecasts into the Lyapunov optimization framework** for online EV charging scheduling, overcoming the myopia of prediction-free Lyapunov methods while retaining rigorous theoretical guarantees.
- Novel **forecast-integrated virtual queue design** ($q_g$, $z_g$) embedded in a [[MPC]] framework; extended with **heterogeneous penalty parameters** $V_g$ per EV group to shrink the optimality gap.
- Proves charging delay upper bound $O(w)$ and optimality gap bound $O(1/(wV))$ — both improving with lookahead window length $w$.
- Case study (100 EVs, real Shanghai arrivals + CAISO prices): A1 reaches within **1% of offline optimal cost**, vs 46% for homogeneous-penalty A2; both beat MPC and greedy.

## 🧠 Methodology & Model Architecture

### 1. Offline Problem (P1)
Available charging window $U_v \triangleq \{T_v^a,\dots,T_v^d-1\}$; instantaneous cost:
$$f(t) \triangleq \pi(t) \sum_{v\in S} p_v(t)$$
$$\text{P1:} \quad \min \frac{1}{T}\sum_{t=1}^{T} f(t) \quad \text{s.t. } 0\le p_v(t)\le P_v\ (\forall t\in U_v),\; p_v(t)=0\ (\forall t\notin U_v),\; E_v^{req}\le \eta\Delta t \sum_{t=1}^T p_v(t)\le E_v^{max}$$

### 2. Equivalent Aggregation by Parking Time (P3)
EVs grouped so $|U_v|=R_g$; aggregate power $x_g(t)=\sum_{v\in S_g}p_v(t)$. Equivalence to P1 enforced over every duration $U\subseteq\{1,\dots,T\}$:
$$X_g^U = \sum_{v\in S_g}\max\{0,\; E_v^{req}/(\eta\Delta t) - P_v|U_v\setminus U|\}, \qquad X_g^{\bar U} = \sum_{v\in S_g}\min\{E_v^{max}/(\eta\Delta t),\; P_v|U_v\cap U|\}$$
$$X_g^U \le \sum_{t\in U} x_g(t) \le X_g^{\bar U}, \quad \forall U \;\text{(Proposition 1: equivalent aggregation, proven via Hoffman's circulation theorem)}$$

### 3. Stochastic Relaxation (P4)
Aggregate demand arrival (with $T_v^{min}=\lceil E_v^{req}/(P_v\eta)\rceil$):
$$a_v(t)=\begin{cases} P_v, & T_v^a \le t \le T_v^a+T_v^{min}\\ E_v^{req}/\eta - T_v^{min}P_v, & t = T_v^a+T_v^{min}+1\\ 0, & \text{otherwise}\end{cases}$$
Objective: $\inf \lim_{T\to\infty}\frac1T\sum_t E[f(t)]$ s.t. mean-rate stability $\lim_{T\to\infty}\frac1T\sum_t E[a_g(t)-x_g(t)]\le0$. Optimality gap of relaxation bounded by price fluctuation:
$$f_2^* - f_3^* \le \frac{1}{\eta T\Delta t}\sum_{v\in S}\left(E_v^{req}\max_{t_1,t_2\in U_v}(\pi(t_1)-\pi(t_2))\right) \tag{Claim 1}$$

### 4. Forecast-Enhanced Virtual Queues
Demand backlog queue integrating a $w$-slot lookahead forecast:
$$q_g(t+w) = \max\left(q_g(t) + \sum_{\tau=0}^{w-1}(a_g(t+\tau)-x_g(t+\tau)),\; 0\right) \tag{Forecast-Lookahead Queue}$$
Delay-aware virtual queue ($I_g(t)=1$ iff $q_g(t)>0$):
$$z_g(t+w) = \max\left(z_g(t) - \sum_{\tau=0}^{w-1}x_g(t+\tau) + \frac{\alpha_g}{R_g}I_g(t),\; 0\right) \tag{Delay-Aware Queue}$$
FIFO processing ⇒ maximum charging delay $D_g < wR_g(Q_g+Z_g)/\alpha_g$ (Proposition 2).

### 5. Drift-Plus-Penalty Algorithm
Lyapunov function and drift-plus-penalty term:
$$L(\Theta(t)) \triangleq \frac12\sum_{g=1}^G (q_g^2(t)+z_g^2(t)), \qquad \Delta(\Theta(t)) + V E\!\left[\frac1w\sum_{\tau=0}^{w-1} f(t+\tau)\,\Big|\,\Theta(t)\right]$$
Drift upper bound (constants $B_{g1}$, $B_{g2}=(\alpha_g/R_g)^2+(wX_g)^2+2Z_g\alpha_g/R_g$):
$$\Delta(\Theta(t)) \le B - \sum_{g=1}^G (q_g(t)+z_g(t))\sum_{\tau=0}^{w-1}x_g(t+\tau)$$
Online LP (P5), solved each slot with standard solvers:
$$\min_{x_g(t+\tau)} \; V\sum_{\tau=0}^{w-1}f(t+\tau) - \sum_{g=1}^G (q_g(t)+z_g(t))\sum_{\tau=0}^{w-1}x_g(t+\tau) \quad \text{s.t. } 0\le x_g(t+\tau)\le \sum_{v\in S_g^{act}(t+\tau)}\min\{P_v, E_v^{max}/(\eta\Delta t)\}$$

### 6. Buffered Average Policy & Guarantees
Implemented policy averages the last $w$ LP solutions:
$$x_g(t) = \frac1w\sum_{\tau=0}^{w-1}\hat{x}_g^{(t-\tau)}(t)$$
Uniform queue bounds: $q_g(t)\le Q_g=V\pi_{\max}+2wX_g$, $z_g(t)\le Z_g=V\pi_{\max}+2\alpha_g/R_g$; hence:
$$D_g < \frac{wR_g}{\alpha_g}\left(2V\pi_{\max} + 2wX_g + \frac{2\alpha_g}{R_g}\right) = O(w) \tag{Corollary 1: Delay Bound}$$
$$0 \le f^{\text{ONL}} - f^{\text{OFL}} \le \frac{B}{wV} = O\!\left(\frac{1}{wV}\right) \tag{Proposition 3: Optimality Gap}$$
Heterogeneous penalties (P5′): objective $\sum_{\tau=0}^{w-1}(\pi(t+\tau)V - q(t)-z(t))^\top x(t+\tau)$ with vector $V=(V_g)$, gap $\le B/(wV_{\min})$ where $V_{\min}=\min_g V_g$ (Proposition 5).

## 📊 Dataset & Input Features
- **[[Shanghai_EV_Arrival_Data]]**: real-world EV arrival/departure times in Shanghai ([23] Du et al., Applied Energy, vol. 383, p. 125302, Apr. 2025); typical working day — most EVs arrive ~8:00 am, leave ~6:00 pm. **100 EVs**, 24-h horizon, **5-min time slots** ($\Delta t$); initial SOC 25–80%, max charging power 150–350 kW, target SOC ≥ 80%, efficiency $\eta=0.95$.
- **[[CAISO]]**: California ISO electricity prices obtained via Grid Status.
  - Data URL: https://www.gridstatus.io/
- Features fed as forecasts into the LP: short-term EV arrival/demand $a_g(t)$, electricity price $\pi(t)$ within window $w$; system state: virtual-queue backlogs $q_g,z_g$.
- No public code/data repository stated; simulation in MATLAB on Intel Core i5-10505, 16 GB RAM.

## 📈 Performance & Results
Cost & delay comparison (Table II, 100 EVs, MPC at $w=12$):

| Algorithm | Total Cost | Relative | Unit Cost | Avg Delay | Max Delay |
| :-- | :--: | :--: | :--: | :--: | :--: |
| Offline optimal | $0.99M | 100% | $28.5/kWh | 7.36 h | 9.67 h |
| **A1 (heterogeneous)** | **$1.01M** | **101%** | $28.9 | 7.43 h | 9.67 h |
| A2 (homogeneous) | $1.44M | 146% | $41.5 | 2.91 h | 7.83 h |
| MPC | $1.81M | 182% | $51.8 | 9.46 h | 12.6 h |
| Greedy | $1.80M | 182% | $51.7 | 0.18 h | 0.42 h |

- A1 cost gap only **1%** vs offline; A2 gap **46%**; both below theoretical bounds.
- MPC cannot guarantee charging-demand satisfaction when the lookahead window is small (demand enters window too late) — proposed method does not suffer this.
- Delay bounds validated empirically for $w=1,2,5,8,12$: e.g., average max delay grows 1.19→2.63 h (all under bound (18)).
- Parametrics: cost falls with $V$ until tasks risk failure ($V>11$ infeasible at $w=8,12$); larger $w$ smooths cost traces and simplifies $V$ tuning ($V\in[8,10]$ works for any $w\ge5$); larger $\alpha_g$ trades higher cost for lower delay.
- Scalability: compute time 21.6 s (50 EVs) → 22.8 s (200 EVs), only +1.2 s (+6%) — near-flat scaling for real-time use.
- Robustness: with price prediction MAPE ≈ 4% ($\tilde\pi=(1+0.05Y)\pi$, $Y\sim\mathcal N(0,1)$), A2 remains robust and still beats MPC; A1 becomes sensitive (may miss charging demand since each group is tuned to its limit).

## 💡 Limitations & Identified Research Gaps
- Assumes i.i.d. prices/arrivals/energy demands for P4; forecasts assumed accurate inside window (only Gaussian-noise robustness test).
- Grouping by parking time is an aggregation approximation; per-EV disaggregation via FIFO may be suboptimal.
- Single-station scope; no network constraints, transformer limits, or renewable co-optimization; V2G explicitly left to future work.
- Heterogeneous penalty (A1) requires careful per-group tuning of $V_g$ and degrades under forecast error.
- Gap for thesis: the framework consumes generic short-term load/price forecasts — coupling probabilistic forecasters ([[TimeGrad]], [[Temporal_Fusion_Transformer]]) with uncertainty-aware Lyapunov control is unexplored.

## 📚 BibTeX & Citation Reference
```bibtex
@article{huang2026forecast,
  title={Forecast-Enhanced Lyapunov Optimization for Real-Time EV Charging Scheduling},
  author={Huang, Shihan and Chen, Yue and Chen, Richard and Wierman, Adam},
  journal={arXiv preprint arXiv:2604.16873},
  year={2026}
}
```

## 🔗 Key References & Citation Graph
- Foundation: Neely, *Stochastic Network Optimization with Application to Communication and Queueing Systems* (2010) — standard Lyapunov drift-plus-penalty [12].
- Data sources: [[Shanghai_EV_Arrival_Data]] (Du et al. 2025), [[CAISO]] via Grid Status (https://www.gridstatus.io/).
- Related vault concepts: [[MPC]], [[Queuing_Model]], [[Lyapunov_Optimization]], [[Short_Term_Forecasting]]
- Contrast baselines: [[MPC]], greedy scheduling; related RL-based alternatives ([[Q_Learning]]) lack hard-constraint safety guarantees.
