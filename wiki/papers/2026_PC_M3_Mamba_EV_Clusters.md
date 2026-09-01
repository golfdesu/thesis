---
type: paper
title: "A Mamba State-Space Sequence Model for AI-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management"
authors: [Jinyi Tang, Xuan Zhou, Qin Yan]
year: 2026
journal_conference: "Electronics (MDPI), vol. 15, art. 2380"
doi_url: "https://doi.org/10.3390/electronics15112380"
models_used: ["[[PC-M3]]", "[[Mamba-3]]", "[[Routing_Mamba]]", "[[PowerMamba]]", "[[Informer]]", "[[Mamba_SSM]]", "[[TD3]]", "[[MPC]]"]
datasets_used: ["[[Caltech_ACN]]", "[[ACN-Sim]]", "[[ElaadNL]]", "[[NREL_dsgrid_TEMPO]]", "[[NHTS_2009]]"]
features_used: ["[[State_of_Charge]]", "[[Charging_Power]]", "[[Arrival_Departure_Time]]", "[[Arrival_Departure_Time]]", "[[Energy_Requirement]]", "[[Battery_Capacity]]", "[[Pilot_Signal]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[RMSE]]", "[[Hausdorff_Distance]]", "[[Polytope_Feasibility]]", "[[Inference_Latency]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Mamba State-Space Sequence Model for AI-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management

## 🎯 Main Objective & Contribution
- Real-time [[Energy_Management_System|EMS]] for large EV clusters needs both fast aggregate flexibility estimation and executable per-vehicle dispatch. Exact [[Minkowski_Sum|Minkowski-sum]] aggregation of per-vehicle feasibility polytopes scales super-polynomially in $N$; LP/MILP/MPC solve times explode online; learning-based aggregators treat constraints as soft penalties (3–15% session violations observed).
- Proposes **PC-M3** (Physics-Constrained Mamba-3 MIMO Aggregator): an amortized, constraint-aware sequence model combining (i) a vehicle-as-channel [[Mamba-3]] MIMO backbone, (ii) a history-dependent differentiable feasibility projection fused *inside* the recurrent state update, (iii) a sparse [[Routing_Mamba]] mixture-of-experts layer, and (iv) a consistency-trained aggregation–disaggregation closed loop. Scales AI-EMS from one battery to ten-thousand-vehicle clusters in one forward pass.

## 🧠 Methodology & Model Architecture
- **Problem setup**: cluster of $N$ EVs over horizon $t \in \{1,\dots,T\}$ ($T=96$, $\Delta t = 15$ min); vehicle $i$ has arrival $a_i$, departure $d_i$, initial SoC $s_i^0$, energy requirement $E_i^{\text{req}}$, capacity $C_i$, rate limits $[\underline{p}_i, \bar{p}_i]$; SoC dynamics $s_{i,t+1} = s_{i,t} + (\eta_i p_{i,t}\Delta t)/C_i$. Output: envelope $[\underline{P}_t,\bar{P}_t]$ + per-vehicle dispatch tracking grid command $r_t^{\text{grid}}$.
- **Per-vehicle feasibility polytope**:
$$ \mathcal{P}_i = \left\{ \mathbf{p}_i \in \mathbb{R}^T : \underline{p}_i \le p_{i,t} \le \bar{p}_i,\ \underline{s}_i \le s_{i,t}(\mathbf{p}_i) \le \bar{s}_i,\ \sum_{t=a_i}^{d_i} \eta_i p_{i,t}\Delta t \ge E_i^{\text{req}},\ p_{i,t}=0 \text{ outside } [a_i,d_i] \right\} \tag{1} $$
- **Exact cluster flexibility set (Minkowski sum)**:
$$ \mathcal{P}_\Sigma = \mathcal{P}_1 \oplus \mathcal{P}_2 \oplus \cdots \oplus \mathcal{P}_N = \left\{ \sum_{i=1}^{N} \mathbf{p}_i : \mathbf{p}_i \in \mathcal{P}_i,\ \forall i \right\} \tag{2} $$
- **Mamba-3 MIMO recurrence** (vehicle-as-channel; hidden state $h_t \in \mathbb{C}^{D\times R}$):
$$ h_t = A_t h_{t-1} + B_t u_t^\top, \qquad y_t = C_t h_t \tag{3} $$
with trapezoidal discretisation
$$ A_t = \exp(\Delta t A), \qquad B_t = A^{-1}(A_t - I)B \tag{4} $$
($A$ complex-valued, block-diagonal; input $u_t \in \mathbb{R}^N$ carries every vehicle's status; complexity $O(TD^2 + TND)$ time, $O(D^2+ND)$ memory).
- **Differentiable in-loop feasibility projection** (Proposition A1: reduces to clamp onto interval $[p^{\min}_{i,t}, p^{\max}_{i,t}]$ given fixed past):
$$ \tilde{y}_t = \Pi_{\mathcal{P}^{(t)}}(C_t h_t), \qquad h_t \leftarrow h_t + K_t(\tilde{y}_t - C_t h_t) \tag{5} $$
where $K_t$ is a learned Kalman-like gain; the interval intersects the power box, upper/lower SoC bounds and a forward-looking "must-charge-now" bound guaranteeing $E_i^{\text{req}}$ by departure.
- **Routing-Mamba expert layer**: router $g_\phi(x_i)$ gives sparse gating over $E=8$ experts, effective projection $B_i = \sum_e g_\phi(x_i)_e B^{(e)}$, top-$k=2$ routing (~23% fewer FLOPs than dense).
- **Training objective** (weighted sum):
$$ \mathcal{L} = \lambda_{\text{env}}\mathcal{L}_{\text{env}} + \lambda_{\text{ind}}\mathcal{L}_{\text{ind}} + \lambda_{\text{cons}}\mathcal{L}_{\text{cons}} + \lambda_{\text{route}}\mathcal{L}_{\text{route}}, \quad (\lambda = 1.0, 0.5, 0.25, 0.01) \tag{6} $$
- **Envelope loss**, exact regime ($N \le 1024$, rail-wise MSE against exact Minkowski rails):
$$ \mathcal{L}^{\text{exact}}_{\text{env}} = \frac{1}{T}\sum_{t=1}^{T}\left[(\hat{\underline{P}}_t - \underline{P}^\star_t)^2 + (\hat{\bar{P}}_t - \bar{P}^\star_t)^2\right] \tag{7} $$
and band regime ($N > 1024$, zero-penalty inside certified inner–outer sandwich):
$$ \mathcal{L}^{\text{band}}_{\text{env}} = \frac{1}{T}\sum_{t=1}^{T}\left[\text{dist}_{\text{band}}(\hat{\underline{P}}_t, \underline{P}^{\text{out}}_t, \underline{P}^{\text{in}}_t)^2 + \text{dist}_{\text{band}}(\hat{\bar{P}}_t, \bar{P}^{\text{in}}_t, \bar{P}^{\text{out}}_t)^2\right] \tag{8} $$
with $\text{dist}_{\text{band}}(x,a,b)=\max(0,a-x)+\max(0,x-b)$; piecewise selection:
$$ \mathcal{L}_{\text{env}} = \begin{cases} \mathcal{L}^{\text{exact}}_{\text{env}}, & N \le 1024 \\ \mathcal{L}^{\text{band}}_{\text{env}}, & N > 1024 \end{cases} \tag{9} $$
- Implementation: PyTorch 2.2, $D=256$, 6 Mamba blocks, 12.4M params, AdamW lr $3\times10^{-4}$ cosine, 120 epochs, batch 32, single A100 40GB; compiled to $N_{\max}=10{,}240$ channels with masked dummy channels; permutation-equivariant.

## 📊 Dataset & Input Features
- **[[Caltech_ACN]]** (Caltech Adaptive Charging Network): 114,503 real workplace sessions, 25 Apr 2018–28 Feb 2024, Caltech (54 EVSE ports) + JPL (50 ports) + office site; minute-resolution current/pilot signals resampled to 15 min; chronological split (train ≤30 Jun 2022: 78,642 sessions; val Jul–Dec 2022; test CY2023: 20,214). Mean energy 9.12 kWh/session, median stay 5.42 h. URL: https://ev.caltech.edu/dataset ; simulator [[ACN-Sim]]: https://github.com/zach401/acnportal
- **[[ElaadNL]]** Open Datasets (2020 release): 10,397 anonymised public-charging transactions across 1812 Dutch public points, calendar year 2019; mean energy 10.72 kWh, median stay 3.08 h; used strictly for zero-shot cross-regional transfer. URL: https://platform.elaad.io/analyses/
- **[[NREL_dsgrid_TEMPO]]** v2022: county-resolved hourly light-duty EV charging profiles, contiguous US, 2018–2050, three scenarios; used 2030 All-EV-Sales-by-2035 LA County profile to calibrate a synthetic 10,000-vehicle cluster bootstrapped from ACN-Data-conditioned distributions (V2G capability share imposed by scenario; not native). URL: https://data.openei.org/submissions/5958
- Auxiliary: 2022 [[NHTS_2009]] for synthetic disconnection-period states only.
- Per-vehicle parameters ($C_i$, SoC bounds $[0.10,0.95]$, $s_i^0$, $\eta_i = 0.92$) imputed since datasets don't expose battery capacity/SoC; all feasibility numbers are relative to specified/imputed polytopes; ±15% sensitivity analysis confirms robustness.
- Data availability statement: all datasets public (accessed 19 May 2026).

## 📈 Performance & Results
- **Envelope approximation** ([[Hausdorff_Distance]], % width-normalised, ACN-Data / ElaadNL zero-shot): PC-M3 **3.4 / 4.1** vs PowerMamba 9.7/11.2, Informer 11.8/14.6, Mamba-2+proj 10.4/12.1, Zonotope 13.2/15.9, LP outer bound 21.6/24.2. Envelope width 92.4% of true vs 118.3% (PowerMamba), 131.4% (Zonotope).
- **10k-vehicle dsgrid-TEMPO stress test**: PC-M3 3.8% vs sandwich reference vs PowerMamba 10.6%, Informer 13.5%.
- **Closed-loop tracking on [[ACN-Sim]]** (500 simulated days, 6200 sessions): tracking [[RMSE]] 0.82 MW (PC-M3) vs MPC 1.45 MW, TD3 1.78 MW, PowerMamba+proj 1.18 MW, uncoordinated 3.12 MW → 43% reduction vs strongest control baseline; **zero polytope violations** (structural, via in-loop clamp) across all evaluated sessions (0/20,214 test, 0/10,397 ElaadNL, 0/6200 closed loop).
- **Scalability**: 0.34 s inference for 10,000 EVs at $T=96$ on one A100 (3.8 GB peak memory) vs PowerMamba 0.81 s and Informer 6.20 s (18× faster); ~39× faster than LP-MPC at $N=512$ (0.08 s vs 3.10 s); LP/MILP timeout (>120 s) at $N \ge 5000$; measured linear scaling ~32 µs/vehicle. RTX 4090: 0.71 s; RTX 3060: 2.36 s; CPU: 18.7 s at N=10,000.
- **Ablations** (ACN-Data): removing projection → Hnorm 9.1%, 13.6% violations, no convergence within 120 epochs; removing Routing-Mamba → 4.6%, 0.66 s @10k; removing A-DA loop → 4.8%, RMSE 1.29 MW; removing all → 11.4%, 17.1% violations. In-loop projection reaches Hnorm<5% in 38 epochs vs 92 (post-hoc) with lower gradient norms (0.74 vs 1.05/1.39).
- Case study (Caltech peak day 25 Jul 2023): holds 0.89 MW during 16:00–20:00 peak-shave window, peak-to-peak tracking error 0.04 MW vs MPC 0.28, TD3 0.39; SoC delivery MAE 0.32% vs MPC 1.91%, TD3 3.04%.

## 💡 Limitations & Identified Research Gaps
- Differentiable projection relies on separable per-vehicle polytopes (one intertemporal energy constraint); shared-infrastructure coupling (DC fast-charging hubs) is an open problem.
- Assumes arrival time and requested energy known at connection; mid-session revisions require re-running the projection.
- Vehicle-as-channel use of Mamba-3 MIMO is far beyond validated rank range ($R \in \{4,8,16\}$ originally); no quality guarantees inherited at $N \gg 16$; claims limited to $N \le 10{,}000$; 100k-vehicle regime would need hierarchical routing/sparse MIMO decomposition.
- Feasibility certified only relative to imputed polytopes (no true BMS data in ACN-Data/ElaadNL); validation on true vehicle-side measurements is next step.
- Bidirectional V2G/G2V exercised only on synthetic dsgrid-TEMPO stress test (real corpora charge-only); future work: degradation co-optimisation head.

## 📚 BibTeX & Citation Reference
```bibtex
@article{tang2026pcm3,
  author  = {Tang, Jinyi and Zhou, Xuan and Yan, Qin},
  title   = {A {M}amba State-Space Sequence Model for {AI}-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management},
  journal = {Electronics},
  volume  = {15},
  pages   = {2380},
  year    = {2026},
  doi     = {10.3390/electronics15112380}
}
```

## 🔗 Key References & Citation Graph
- [[2026_Mamba_3_Sequence_Modeling]] — Mamba-3 MIMO recurrence backbone [9]
- [[Routing_Mamba]] (Zhan et al., arXiv:2506.18145) — MoE expert layer [10]
- [[PowerMamba]] (Menati et al., arXiv:2412.06112) — closest SSM baseline [11]
- [[2017_Attention_Is_All_You_Need]]-lineage Transformers: [[Informer]] (AAAI 2021) [8], Autoformer (NeurIPS 2021) [20]
- [[Mamba_SSM]] (Gu & Dao, arXiv:2312.00752) [22], [[Mamba_SSM]]/Structured State-Space Duality (ICML 2024) [23], S4 (Gu et al., ICLR 2022) [21]
- [[OptNet]] differentiable optimization layers (Amos & Kolter, ICML 2017) [24]; safe-exploration projection layers (Dalal et al.) [25]
- Switch Transformer load-balance loss (Fedus et al., JMLR 2022) [35]; TD3 (Fujimoto et al., ICML 2018) [28]; SAC [29]
- Aggregate flexibility geometry: Nazir & Hiskens inner-box CDC 2018 [5]; Zhao et al. zonotope IEEE TPWRS 2017 [6]; Müller et al. IEEE TSG 2019 [3]; Barot & Taylor 2017 [4]
- [[Caltech_ACN]] (Lee et al., ACM e-Energy 2019) [2]; [[ACN-Sim]] (Lee et al., IEEE TSG 2021) [12]
- PINN soft-constraint contrast: Raissi et al. 2019 [37]; Cuomo et al. 2022 [38]
