---
type: paper
title: "Reinforcement Learning-Based Load Forecasting of Electric Vehicle Charging Station Using Q-Learning Technique"
authors: [Morteza Dabbaghjamanesh, Amirhossein Moeini, Abdollah Kavousi-Fard]
year: 2021
journal_conference: "IEEE Transactions on Industrial Informatics, Vol. 17, No. 6, pp. 4229-4237"
doi_url: "https://doi.org/10.1109/TII.2020.2990397"
models_used: ["[[Q_Learning|Q-Learning (off-policy RL)]]", "[[ANN]]", "[[RNN]]"]
datasets_used: ["[[Simulated_PHEV_Charging_Data|MATLAB-simulated PHEV charging scenarios (uncoordinated / coordinated / smart)]]"]
features_used: ["[[Historical_Load|Previous 24-h PHEV loads]]", "[[Charging_Start_Time]]", "[[SOC|State of Charge (SOC)]]", "[[Battery_Capacity]]", "[[All_Electric_Range|AER]]", "[[Daily_Driven_Miles]]", "[[Depth_of_Discharge|DOD]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[MSE]]", "[[Training_Epochs]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Reinforcement Learning-Based Load Forecasting of Electric Vehicle Charging Station Using Q-Learning Technique

## 🎯 Main Objective & Contribution
- **First RL-based framework covering all three PHEV charging regimes** — uncoordinated, coordinated, and smart charging — for EV charging station load forecasting.
- Proposes an **off-policy [[Q_Learning]] ensemble selector**: an agent learns hour-by-hour which base model ([[ANN]] vs [[RNN]]) to trust for each of the next 24 hourly steps, using an exponential error-based reward with a randomized exploration factor $\lambda$ around candidate predictions.
- Claims >50% accuracy improvement ([[MSE]] reduction) over standalone ANN/RNN under the hardest regime (smart charging), where price incentives cause sharp non-stationary load shifts.

## 🧠 Methodology & Model Architecture
### 1. PHEV Charging Scenario Modeling (data generation)
Charging start-time PDFs per scenario:
$$f(t_s)=\frac{1}{b-a},\ b=19,\ a=18,\ a\le t_s\le b \quad \text{(Uncoordinated: evening plug-in ~6 PM)}$$
$$f(t_s)=\frac{1}{b-a},\ a=21,\ b=24,\ a\le t_s\le b \quad \text{(Coordinated: off-peak ~9 PM)}$$
$$f(t_s)=\frac{1}{\psi\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{t_s-\mu}{\psi}\right)^2},\ \mu=1,\ \psi=3 \quad \text{(Smart: SOC + price driven)}$$
Daily-driven distance (log-normal):
$$f(m)=\frac{1}{m\psi\sqrt{2\pi}}e^{-\frac{(\ln m-\mu)^2}{2\psi^2}},\ m>0$$
SOC and charging duration:
$$\text{SOC}=\begin{cases}0, & m>\text{AER}\\ \dfrac{\text{AER}-m}{\text{AER}}\times100\%, & m\le\text{AER}\end{cases} \tag{SOC}$$
$$t_D=\frac{C_{BT}\times(1-\text{SOC})\times DOD}{\eta\times J} \tag{Charging Duration}$$
where $C_{BT}$ = battery capacity (kWh), $DOD$ = depth of discharge, $\eta$ = charger efficiency, $J$ = charger rate (kW). Level-1/2 home chargers only (level-3 excluded). Four PHEV classes drawn by discrete market share via normal distribution:
$$\mu_{C_{BT}}=\frac{\text{Min}_{C_{BT}}+\text{Max}_{C_{BT}}}{2}, \qquad \psi_{C_{BT}}=\frac{\text{Max}_{C_{BT}}-\text{Min}_{C_{BT}}}{4}$$

### 2. Base Models
ANN node output (input layer X, two hidden layers H, output Y):
$$O_j^l=\sigma_j^l\left(\sum_{i=0}^{n^{l-1}}(O_i^{l-1}\omega_{ij})+b_j^l\right)$$
RNN cell:
$$a_t=b+Uh_{t-1}+Wx_t,\qquad h_t=g(a_t),\qquad o_t=f(c+Vh_t)$$
Both consume the **previous 24-h load** to predict **1 h ahead** (sliding across days).

### 3. Q-Learning Ensemble Selector
Q-table update (off-policy, Markov decision process):
$$Q^{new}(s_t,a_t)\leftarrow Q(s_t,a_t)+\alpha\left(r_t+\lambda\max_a Q(s_{t+1},a_t)-Q(s_t,a_t)\right)$$
with learning rate $\alpha\in[0,1]$, discount factor $\lambda\in[0,1]$; Q-values initialized to zero. Greedy action selection:
$$a_t=\arg\max_a Q(s_{t+1},a_t)$$
Novel exponential reward comparing candidate prediction against actual load, scaled by a random exploratory factor $\lambda_i\in[0,2]$ to search around optimal points:
$$r_t(\lambda_i)=\frac{1}{\exp\left|(P_t^{\text{Optimal}}-\lambda_i(P_t^{\text{ANN/RNN}}))\right|}$$
Two actions ($i=0$: ANN, $i=1$: RNN) selected per hour → **24 optimal actions per day-ahead horizon**.

## 📊 Dataset & Input Features
- **No real-world dataset**: training/testing data generated via **MATLAB** simulation of the three charging techniques using Eqs (1)–(8) (start-time PDFs, log-normal miles, SOC/duration chain, 4-class battery capacity sampling); simulations implemented in open-source **Keras** (https://keras.io).
- Penetration levels studied: **30% and 50% PHEV load penetration**.
- Inputs: previous 24-h hourly PHEV loads (time-series window); scenario-specific charging windows observed: uncoordinated 6 PM–6 AM, coordinated 8 PM–10 AM.
- Sensitivity configuration space (Table III): hidden layers 2→3, nodes 200→500 for both ANN and RNN base models.
- No public data repository or DOI-linked data availability statement appears anywhere in the text.

## 📈 Performance & Results
MSE comparison across scenarios at 30%/50% penetration (Table IV; best in bold):

| Scenario | Model | Hidden Layers | Nodes | Epochs | MSE |
| :-- | :-- | :--: | :--: | :--: | :--: |
| Uncoordinated (30%) | ANN-3 | 3 | 500 | 1,000 | 0.0023 |
| | RNN-3 | 3 | 500 | 1,000 | 0.0020 |
| | **Q-Learning-3** | 3 | 500 | 1,000 | **0.0020 (best)** |
| Coordinated | ANN-3 | 3 | 500 | 3,000 | 9.42 |
| | RNN-3 | 3 | 500 | 500 | 9.80 |
| | **Q-Learning-3** | 3 | 500 | 10,000 | **7.20 (−23.5%)** |
| Smart (worst case) | ANN-3 | 3 | 500 | 3,000 | 7.22 |
| | RNN-3 | 3 | 500 | 500 | 7.34 |
| | **Q-Learning-3** | 3 | 500 | 10,000 | **4.63** |

- Paper's stated headline result: under the worst scenario (smart charging), Q-learning achieves **more than 50% improvement** over conventional ANN/RNN techniques (Conclusion, Sec. VI).
- Deeper/wider networks improve all models (sensitivity analysis Figs 10–12): 3 hidden layers × 500 nodes outperform 2×200/300/400 for ANN, RNN, and Q-learning alike.
- Higher epoch counts matter: ANN (1000–3000 epochs) beats RNN (500 epochs) on raw accuracy; Q-learning benefits most from 10,000 iterations since it re-scores both base models each hour.
- Qualitative claims: higher speed (pre-trained ANN/RNN feed real-time Q-learning), flexibility (any charging regime trainable), and robust tracking of sharp smart-charging load shifts where single models fail.

## 💡 Limitations & Identified Research Gaps
- **Entirely synthetic evaluation**: loads generated from stylized parametric PDFs; no empirical validation against measured charging-station sessions, no confidence intervals or statistical tests on reported MSEs.
- Action space limited to selecting between only two base models (ANN/RNN) — no richer ensemble, no continuous blending weight, no modern sequence models (LSTM/GRU/TFT variants) as candidates despite being mentioned in the related work.
- Reward requires ground truth during learning — formulation is closer to adaptive model weighting than true online forecasting without labels.
- Only residential level-1/2 charging modeled (public DC fast charging excluded); single aggregation-level station load, no spatial/network dimension.
- Fairness caveat: Q-learning used 10,000 iterations vs 500–3,000 for baselines, so part of the gain is compute rather than methodology.
- Gap for thesis: combining RL model selection with probabilistic forecasts ([[TimeGrad]], [[TFT]]) or applying it as a meta-learner over deep ensembles on real EV session data remains untested.

## 📚 BibTeX & Citation Reference
```bibtex
@article{dabbaghjamanesh2021reinforcement,
  title={Reinforcement Learning-Based Load Forecasting of Electric Vehicle Charging Station Using Q-Learning Technique},
  author={Dabbaghjamanesh, Morteza and Moeini, Amirhossein and Kavousi-Fard, Abdollah},
  journal={IEEE Transactions on Industrial Informatics},
  volume={17},
  number={6},
  pages={4229--4237},
  year={2021},
  doi={10.1109/TII.2020.2990397}
}
```

## 🔗 Key References & Citation Graph
- Foundation: Rummery & Niranjan, *On-line Q(-)learning Using Connectionist Systems* (Cambridge, 1994) [27] — original Q-learning; Zurada (ANN) [25]; Hecht-Nielsen (backpropagation/RNN theory) [26].
- Data-modeling sources: Rostami et al. [22] and Qian et al. [23] (charging levels/start-time models); Li & Zhang [24] (log-normal daily mileage).
- Tooling: Keras — https://keras.io
- Related vault concepts: [[Q_Learning]], [[Ensemble_Learning]], [[Short_Term]], [[MSE]]
- Contrast with vault: forecast-driven control alternatives [[2021_Huang_Lyapunov_EV_Scheduling]]; probabilistic deep forecasters [[2021_Rasul_TimeGrad_Diffusion_Forecasting]], [[2021_Lim_TFT_Temporal_Fusion_Transformers]].
