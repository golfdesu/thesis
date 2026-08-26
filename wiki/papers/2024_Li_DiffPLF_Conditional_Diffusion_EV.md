---
type: paper
title: "DiffPLF: A Conditional Diffusion Model for Probabilistic Forecasting of EV Charging Load"
authors: [Siyang Li, Hui Xiong, Yize Chen]
year: 2024
journal_conference: "23rd Power Systems Computation Conference (PSCC 2024), Paris, France, June 4-7 2024"
doi_url: "https://arxiv.org/abs/2402.13548"
models_used: ["[[DiffPLF]]", "[[DDPM]]", "[[TimeGrad]]", "[[CSDI]]", "Quantile Regression", "[[LSTM]]"]
datasets_used: ["[[Palo_Alto_EV]]", "[[Weather]]"]
features_used: ["[[Historical_Load]]", "[[Temperature_Forecast]]", "[[Humidity]]", "[[Calendar_Features]]", "[[EV_Number]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[MAE]]", "[[CRPS]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: DiffPLF: A Conditional Diffusion Model for Probabilistic Forecasting of EV Charging Load

## 🎯 Main Objective & Contribution
- Probabilistic [[EV_Charging_Demand]]: explicitly approximate the predictive distribution $q(x_0|p,r)$ of future charging load profiles conditioned on historical demand and covariates, instead of point forecasts or quantile regression (which struggles with the extreme volatility and conditioning information of EV charging).
- Proposes **[[DiffPLF]]**: a conditional denoising diffusion model ([[DDPM]]) with a **cross-attention conditioning mechanism** (from latent diffusion / text-to-image models) entangling perturbed load series with conditions; plus a **task-informed fine-tuning** stage via a 50%-quantile deviation minimization (QDM) loss that sharpens prediction intervals (~40% improvement vs standard quantile regression training).
- Results: **39.58% MAE and 49.87% CRPS improvement** over conventional quantile regression; supports controllable generation conditioned on EV number and flexible horizons (24/12/6/4/1 h). Code public: https://github.com/LSY-Cython/DiffPLF

## 🧠 Methodology & Model Architecture
Problem: context window $\omega$ of past charging demand $p_i \in \mathbb{R}, i\in[s-\omega,s]$; covariate set known in advance over horizon $\tau$: weather forecasts (temperature $u\in\mathbb{R}^\tau$, humidity $v\in\mathbb{R}^\tau$), one-hot day-of-week $d\in\mathbb{R}^7$, EV number $e$; i.e., $r=\{u,v,d,e\}$. Goal: sample plausible future profiles from $q(x_0|p,r)$.

### Conditional Denoising Diffusion
Forward Markov noising process (**Eq. 1**):
$$q(x_t|x_{t-1}) = \mathcal{N}\left(x_t;\ \sqrt{1-\beta_t}\,x_{t-1},\ \beta_t I\right)$$
Closed-form arbitrary-step noising (**Eqs. 2a-2b**, $\bar{\alpha}_t = \prod_{s=1}^t(1-\beta_s)$):
$$q(x_t|x_0) = \mathcal{N}(x_t;\sqrt{\bar{\alpha}_t}x_0,(1-\bar{\alpha}_t)I); \qquad x_t = \sqrt{\bar{\alpha}_t}x_0 + \sqrt{1-\bar{\alpha}_t}\,\epsilon,\quad \epsilon\sim\mathcal{N}(0,I)$$
Learnable Gaussian reverse transition (**Eq. 3**), trained via variational bound on negative log-likelihood (**Eq. 4**) yielding the ε-prediction objective (**Eq. 5**):
$$p_\theta(x_{t-1}|x_t)=\mathcal{N}(x_{t-1};\mu_\theta(x_t,t),\Sigma_\theta(x_t,t)); \qquad -\log p_\theta(x_0)\le \mathbb{E}_{q(x_{1:T}|x_0)}\left[-\log\frac{p_\theta(x_{0:T})}{q(x_{1:T}|x_0)}\right]$$
$$L_{t-1} = \mathbb{E}_{x_0,\epsilon,t}\left[\|\epsilon - \epsilon_\theta(\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha}_t}\epsilon,\ t)\|_2^2\right]$$
Conditional reverse transition with fixed variance $\tilde{\beta}_t = \frac{1-\bar{\alpha}_{t-1}}{1-\bar{\alpha}_t}\beta_t$ (**Eq. 6**) and conditional training objective (**Eq. 7**):
$$p_\theta(x_{t-1}|x_t,c) = \mathcal{N}(x_{t-1};\mu_\theta(x_t,c,t),\tilde{\beta}_t I); \qquad L_{t-1} = \mathbb{E}_{x_0,c,\epsilon,t}\left[\|\epsilon-\epsilon_\theta(\sqrt{\bar{\alpha}_t}x_0+\sqrt{1-\bar{\alpha}_t}\epsilon,\ c,\ t)\|_2^2\right]$$
Stochastic step-wise denoising sampler (**Eq. 8**, $z\sim\mathcal{N}(0,I)$):
$$x_{t-1} = \frac{1}{\sqrt{1-\beta_t}}\left(x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}}\epsilon_\theta(x_t,c,t)\right) + \sqrt{\tilde{\beta}_t}\,z$$

### Denoising Network (4 components)
1. **Perturbation encoder** $f_\phi$: LSTM on $x_t$ + linear layer on $t$, fused by self-attention (unconditional noise-prediction path).
2. **Condition encoder** $h_\phi$: concatenates temporal data $\{p,u,v\}$ → LSTM; calendar vector $d$ and EV number $e$ → linear layer; self-attention fusion.
3. **Cross-attention mechanism** conditioning $x_t,t$ on $c$ (**Eq. 9**, $Q=h_\phi(p,r)W_Q$, $K=f_\phi(x_t,t)W_K$, $V=f_\phi(x_t,t)W_V$, hidden dim $d$):
$$\text{Attention}(Q,K,V) = \text{softmax}\!\left(\frac{QK^T}{\sqrt{d}}\right)V$$
4. **Forecast network**: self-attention + linear projection → predicted noise ε.

### Task-Informed Fine-Tuning (QDM)
Goal: make the median $m_0\in\mathbb{R}^\tau$ of $N=1000$ generated profiles close to ground truth ($\min \|m_0-x_0\|_2^2$). Since sampling is iterative/non-differentiable end-to-end, use alternative objective on corrupted versions of $m_0$ and $x_0$ with the same noise (**Eq. 10**):
$$L_{\text{QDM}} = \|\epsilon_\theta(m_t,c,t)-\epsilon_\theta(x_t,c,t)\|_2^2$$
Total refinement loss with prior preservation (**Eq. 11**, weight λ):
$$L_{\text{ref}} = L_{t-1} + \lambda L_{\text{QDM}}$$
Algorithm: Stage 1 pre-train $\epsilon_\theta$ via Eq. 7 → Stage 2 generate samples, compute median, refine θ via Eq. 11 → Stage 3 inference by iterating Eq. 8 T times.

### Implementation Details
Hidden dims of LSTM/cross-attention/self-attention all 32; attention heads 4; quadratic noise schedule β₁=0.0001, β_T=0.5, **T=200 diffusion steps**; context = past 5 days; PyTorch, Linux, 48 GB Nvidia A40 GPU; Adam, batch size 16; lr 0.001 (pre-training, 200 epochs) / 0.0002 (fine-tuning, 100 epochs); best QDM weight λ=0.001; 1000 trajectories generated per test case. Avg epoch time: 2.0174 s (pre-training) vs 2.5514 s (fine-tuning); mean inference time per test case 5.7511 s.

## 📊 Dataset & Input Features
- **[[Palo_Alto_EV]]** ("EV Charging Station Usage of California City"): real-world daily charging session details of individual stations in Palo Alto, California — charging durations and delivered energy per session; aggregated to total city charging load at **15-min resolution** using the transformation method of Arias & Bae. Train/fine-tune: 2016–2018; test: 2019. URL: https://www.kaggle.com/datasets/venkatsairo4899/ev-charging-station-usage-of-california-city
- **[[Weather]]**: Palo Alto weather forecasts (temperature, humidity — identified as the two most influential weather factors). URL: https://dev.meteostat.net/
- Covariates: historical aggregate demand (5-day look-back), temperature/humidity forecasts, one-hot weekday vector, number of charged EVs in forecast window.
- Context: US projection of 30–42 M EVs served by 26–35 M charging piles by 2030 (NREL report https://www.nrel.gov/docs/fy23osti/85970.pdf).

## 📈 Performance & Results
Day-ahead forecasting (24 h horizon, past-5-days context), median-of-1000 as point forecast:

| Variant | MAE | CRPS |
| :--- | :---: | :---: |
| Quantile Regression (pinball loss, 5/25/75/95%) | 11.852 ± 3.936 | 10.107 ± 2.124 |
| DiffPLF w/o covariates | 7.842 ± 2.065 | 5.592 ± 1.570 |
| w/o cross-attention (latent addition fusion) | 7.333 ± 1.559 | 5.192 ± 1.099 |
| w/o fine-tuning | 7.227 ± 1.489 | 5.111 ± 1.041 |
| whole-model fine-tuning | 7.200 ± 1.607 | 5.089 ± 1.122 |
| **DiffPLF (full)** | **7.161 ± 1.557** | **5.067 ± 1.094** |

- vs quantile regression: **−39.58% MAE, −49.87% CRPS**.
- Covariates contribute 9.5%/10.4% on MAE/CRPS; cross-attention beats latent feature-fusion by >0.12 on both metrics; partial fine-tuning (denoising front only, freezing cross-attention/encoder weights) beats whole-model fine-tuning.
- Diffusion-step sensitivity (**Table II**): best at T=200 (7.227/5.111 pre-trained); worse at T=100 (9.127/6.458), T=150 (7.313/5.177), T=250 (9.569/6.780), T=300 (9.503/6.742).
- Horizon scaling: retraining-free horizon reduction (fix measured prefix in LQDM input); sharp reliable PIs at 12/6/4/1 h with consistent MAE/CRPS across lengths.
- Controllable generation: varying input EV count e produces cumulative-energy curves with distinct magnitudes/trends; robust to ±5% and mostly ±10% errors in assumed EV number (modest drop at −10%).

## 💡 Limitations & Identified Research Gaps
- Requires a separate task-informed fine-tuning stage for accuracy — authors target a more efficient **end-to-end diffusion model** specialized for probabilistic load forecasting.
- Performance sensitive to diffusion steps T; principled selection of T per scenario left as future work.
- Univariate/station-level scope; extension to **multivariate diffusion** generative models for EV charging and general energy time-series is future work.
- Long-term (multi-day) forecasting for charging-infrastructure planning not yet addressed; benchmarking across different EV charging dataset patterns suggested.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{li2024diffplf,
  author    = {Li, Siyang and Xiong, Hui and Chen, Yize},
  title     = {{DiffPLF}: A Conditional Diffusion Model for Probabilistic Forecasting of {EV} Charging Load},
  booktitle = {23rd Power Systems Computation Conference (PSCC)},
  year      = {2024},
  address   = {Paris, France},
  note      = {arXiv:2402.13548},
  url       = {https://arxiv.org/abs/2402.13548}
}
```

## 🔗 Key References & Citation Graph
- Ho, Jain & Abbeel, NeurIPS 2020 — Denoising Diffusion Probabilistic Models ([[DDPM]] foundation) [20]
- Rombach et al., CVPR 2022 — Latent diffusion / cross-attention conditioning source [21]
- [[2021_Rasul_TimeGrad_Diffusion_Forecasting]] — TimeGrad: autoregressive diffusion TS forecasting baseline (concatenation-style conditioning contrasted) [16]
- Rasul et al., ICLR 2021 — conditioned normalizing flows forecasting [17]
- [[2021_Tashiro_CSDI_Conditional_Diffusion_Forecasting]] — CSDI: score-based diffusion imputation; variance scheduling scheme adopted [18]
- Nichol & Dhariwal, ICML 2021 — improved DDPM; analysis of diffusion-step effects [28]
- Song et al. 2020 — score-based SDE generative modeling (diffusion theory) [25]
- [[2023_Huang_MetaProbformer_EV_Load]] — meta-learning probabilistic charging-load baseline [14]
- [[2021_Zhang_Probabilistic_Queuing_EV_Load]] — queuing-model probabilistic EV forecasting baseline [13]
- [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] — hierarchical ensemble quantile probabilistic EV forecasting baseline [11]
- Dabbaghjamanesh, Moeini & Kavousi-Fard 2021 — RL-based Q-learning charging-load forecasting baseline [6] ([[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]])
- Arias & Bae, Appl. Energy 2016 — big-data charging-demand aggregation method used for the Palo Alto data [7]
