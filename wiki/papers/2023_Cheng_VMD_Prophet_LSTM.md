---
type: paper
title: "Electric vehicle charging load prediction based on variational mode decomposition and Prophet-LSTM"
authors: [Nuo Cheng, Peng Zheng, Xiaofei Ruan, Zhenshan Zhu]
year: 2023
journal_conference: "Frontiers in Energy Research, Vol. 11, Article 1297849"
doi_url: "https://doi.org/10.3389/fenrg.2023.1297849"
models_used: ["[[VMD]]", "[[Prophet]]", "[[LSTM]]", "[[Prophet-LSTM]]"]
datasets_used: ["[[Fujian_Province_EV_Charging_Station_Data]]"]
features_used: ["[[Historical_Load]]", "[[VMD]]", "[[Zero_Crossing_Rate]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[R_squared]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Electric Vehicle Charging Load Prediction Based on Variational Mode Decomposition and Prophet-LSTM

> [!note] Renamed from `2025_Cheng_VMD_Prophet_LSTM_Federated`: the source PDF filename mentions "Federated Learning" but the actual paper (Cheng et al. 2023) contains **no federated learning** — it is a centralized VMD + Prophet-LSTM hybrid decomposition forecasting study.

## 🎯 Main Objective & Contribution
- Accurate [[EV charging load]] prediction is a prerequisite for grid planning and economic operation; real loads are highly volatile due to electricity prices, temperature, dates, etc.
- Proposes a **VMD-Prophet-LSTM combined model**: [[VMD]] decomposes the charging load into $k$ Intrinsic Mode Functions (IMFs); IMFs are split by over-zero (zero-crossing) rate into **low-frequency** (stable, periodic) and **high-frequency** (volatile) reconstructed sequences; [[Prophet]] forecasts the low-frequency part while [[LSTM]] forecasts the high-frequency part; results are summed to the final forecast.
- Reported average absolute error reductions of **7.57% vs ARIMA**, **8.73% vs LSTM**, and **46.02% vs Prophet**.
- Motivation vs prior work: single-model deep predictors ignore component characteristics; prior VMD hybrids ([[GRU]]+TCN (Cai et al. 2022), GRU+ARIMA (Yu et al. 2022)) either use complex ARIMA tuning or one model for all components — Prophet avoids ARIMA's missing-data handling and parameter-tuning burden for medium-scale series.

## 🧠 Methodology & Model Architecture
### 1. VMD Decomposition (Dragomiretskiy & Zosso)
Constrained variational problem (**Eq. 1 — VMD variational problem**):
$$ \min_{\{u_i\},\{\omega_i\}} \left\{ \sum_{i=1}^{k} \left\| \partial_t \left[ \left( \delta(t) + \frac{j}{\pi t} \right) * u_i(t) \right] e^{-j\omega_i t} \right\|_2^2 \right\}, \quad s.t.\ \sum_{i=1}^{k} u_i = f $$
where $\delta(t)$ is the Dirac function and $*$ convolution.

Number of modes selected via energy criterion (**Eq. 2 — IMF energy**):
$$ E_k = \sum_{i=1}^{k} \sqrt{\frac{\sum_{j=1}^{len} I_i^2(j)}{len}} $$
(**Eq. 3 — relative energy change**): $\theta_k = \dfrac{|E_{k+1} - E_k|}{E_k}$ — optimal $k$ where $\theta_k$ jumps abruptly after decreasing ($k=6$ here).

Augmented Lagrangian with quadratic penalty factor $\alpha$ (**Eq. 4**):
$$ L(\{u_k\},\{\omega_k\},\lambda) = \alpha \sum_{i=1}^{k} \left\| \partial_t \left[ \left(\delta(t)+\frac{j}{\pi t}\right) * u_i(t) \right] e^{-j\omega_i t} \right\|_2^2 + \left\| f(t) - \sum_{i=1}^{k} u_i(t) \right\|_2^2 + \left\langle \lambda(t), f(t) - \sum_{i=1}^{k} u_i(t) \right\rangle $$

ADMM-style alternating updates in Fourier domain (**Eqs. 5–7**):
$$ \hat{u}_k^{n+1}(\omega) \leftarrow \frac{\hat{f}(\omega) - \sum_{i \neq k} \hat{u}_i(\omega) + \frac{\hat{\lambda}(\omega)}{2}}{1 + 2\alpha(\omega - \omega_k)^2} $$
$$ \omega_k^{n+1} \leftarrow \frac{\int_0^\infty \omega |\hat{u}_k^{n+1}(\omega)|^2 d\omega}{\int_0^\infty |\hat{u}_k^{n+1}(\omega)|^2 d\omega} $$
$$ \hat{\lambda}^{n+1}(\omega) \leftarrow \hat{\lambda}^n(\omega) + \gamma \left( \hat{f}(\omega) - \sum_k \hat{u}_k^{n+1}(\omega) \right) $$
where $\gamma$ is the noise margin (fidelity parameter).

### 2. High/Low-Frequency Split
Over-zero rate criterion (**Eq. 8 — zero-crossing rate**):
$$ P_{sZC} = \frac{n_{ZC}}{N} $$
with threshold **0.05**: IMF zero-crossing rate > 0.05 → high-frequency sequence (→ LSTM); < 0.05 → low-frequency sequence (→ Prophet).

### 3. Prophet Model (Taylor & Letham)
(**Eq. 9 — Prophet additive model**):
$$ y(t) = g(t) + h(t) + s(t) + \varepsilon(t) $$
Logistic growth trend term (**Eq. 10**):
$$ g(t) = \frac{C}{1 + e^{-k(t-m)}} $$
where $C$ = load capacity, $k$ = growth rate, $m$ = offset parameter.
Holiday effect (**Eq. 11**):
$$ h(t) = Z(t)\kappa, \quad Z(t) = [\mathbb{1}\{T \in D_1\}, \dots, \mathbb{1}\{T \in D_L\}], \quad \kappa \sim Normal(0, v^2) $$

### 4. LSTM Network
Standard gated cell (**Eq. 12 — LSTM gates**):
$$ f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f), \quad i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i) $$
$$ \tilde{c}_t = \tanh(W_c \cdot [h_{t-1}, x_t] + b_c), \quad c_t = f_t * c_{t-1} + i_t * \tilde{c}_t $$
$$ o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o), \quad h_t = o_t * \tanh(c_t) $$
Architecture: **96-dimensional input layer, 1-dimensional output, 2 LSTM layers, 4 fully connected layers (128, 64, 32, 16 neurons)**, tanh activations, [[Adam]] optimizer. Implemented in Python 3.9 / TensorFlow / Keras / Prophet framework on an Intel i5-8300H + NVIDIA GTX 1050Ti (16 GB RAM).

### 5. Error Metrics
(**Eq. 13 — MAE**): $X_{MAE} = \frac{1}{l}\sum_{n=1}^{l} |\hat{y}_n - y_n|$; (**Eq. 14 — R²**): $R^2 = 1 - \frac{\sum_{n=1}^{l}(\hat{y}_n - y_n)^2}{\sum_{n=1}^{l}(\bar{y} - y_n)^2}$.

## 📊 Dataset & Input Features
- **[[Fujian_Province_EV_Charging_Station_Data]]**: EV charging data from one charging station in Fujian Province, China.
  - Period: **January – April 2022**
  - Sampling resolution: **15 min** (96 time steps defined as 1 week at this granularity)
  - Size: #sessions/#stations not disclosed; only aggregate station-level charging power (kW) curve.
- **Features**: historical load time series only (charging power, kW); no exogenous covariates used as model inputs.
- VMD parameters: fidelity balance $\alpha = 8000$, tau $= 0$, DC flag = False, init = 0, tol $= 10^{-7}$; $k = 6$ IMFs (zero-crossing rates: IMF1 0 → IMF6 0.125).
- **Data availability statement**: "The original contributions presented in the study are included in the article/Supplementary material, further inquiries can be directed to the corresponding author." (zszhu@whu.edu.cn). No public URL/repo.
- Funding: State Grid Fujian Electric Power Co., Ltd. (No. 52130N220012); author PZ employed by State Grid Fujian Electric Power.

## 📈 Performance & Results
| Forecasting method | MAE (kW) | R² |
| :--- | :---: | :---: |
| **VMD-Prophet-LSTM (proposed)** | **109.22** | **0.8411** |
| ARIMA | 118.16 | 0.8227 |
| LSTM | 119.67 | 0.8202 |
| Prophet | 202.32 | 0.4936 |

- Average absolute error lower than ARIMA by **7.57%**, LSTM by **8.73%**, Prophet by **46.02%**.
- $R^2 = 0.8411 > 0.8$ indicates a good fit; proposed curve tracks real load best, especially through volatile segments.
- Ablation insight: VMD enables Prophet to handle volatile sequences (raw Prophet alone collapses to R² ≈ 0.49).

## 💡 Limitations & Identified Research Gaps
- Only univariate historical load; no explicit integration of external drivers (electricity prices, temperature, weather) into Prophet/LSTM inputs.
- Single-station case study; no spatial/multi-station or transfer evaluation; no probabilistic/uncertainty quantification.
- Fixed zero-crossing threshold (0.05) heuristic; k-selection via energy-jump rule is empirical.
- Future work stated by authors: extend combined method to other domains (e.g., photovoltaic power prediction) to verify generalization.
- Gap for thesis: deterministic point forecast only — motivates quantile/distributional hybrids and federated extensions across stations.

## 📚 BibTeX & Citation Reference
```bibtex
@article{cheng2023electric,
  title   = {Electric vehicle charging load prediction based on variational mode decomposition and {Prophet}-{LSTM}},
  author  = {Cheng, Nuo and Zheng, Peng and Ruan, Xiaofei and Zhu, Zhenshan},
  journal = {Frontiers in Energy Research},
  volume  = {11},
  pages   = {1297849},
  year    = {2023},
  doi     = {10.3389/fenrg.2023.1297849}
}
```

## 🔗 Key References & Citation Graph
- [[1997_Hochreiter_Long_Short_Term_Memory]] — foundational [[LSTM]] gating architecture used for high-frequency IMF forecasting.
- [[2014_Adam_A_Method_for_Stochastic_Optimization]] — optimizer used to train the [[LSTM]] network.
- Dragomiretskiy & Zosso (2014), *Variational Mode Decomposition*, IEEE Trans. Signal Process. — source of [[VMD]], doi:10.1109/tsp.2013.2288675.
- Taylor & Letham (2018), *Forecasting at Scale* — source of [[Prophet]], doi:10.1080/00031305.2017.1380080.
- Cai et al. (2022) VMD+GRU-TCN hybrid, doi:10.3390/app12136647; Yu et al. (2022) GRU+ARIMA frequency-split scheme — direct baselines inspiring the high/low-frequency division strategy.
