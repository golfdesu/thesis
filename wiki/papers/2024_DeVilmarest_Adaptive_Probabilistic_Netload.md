---
type: paper
title: "Adaptive Probabilistic Forecasting of Electricity (Net-)Load"
authors: [Joseph de Vilmarest, Jethro Browell, Matteo Fasiolo, Yannig Goude, Olivier Wintenberger]
year: 2024
journal_conference: "IEEE Transactions on Power Systems, Vol. 39, No. 2, pp. 4154-4163, March 2024"
doi_url: "https://doi.org/10.1109/TPWRS.2023.3310280"
models_used: ["[[GAM]]", "[[Kalman_Filter]]", "[[Quantile_Regression]]", "[[Online_Gradient_Descent]]", "[[Bernstein_Online_Aggregation]]"]
datasets_used: ["[[GB_Regional_Netload]]", "[[US_City_Daily_Load_COVID]]"]
features_used: ["[[Historical_Load]]", "[[Temperature_Forecast]]", "[[Solar_Radiation]]", "[[Wind_Speed]]", "[[Embedded_Generation_Capacity]]", "[[Calendar_Features]]", "[[Holiday_Flag]]", "[[Precipitation]]", "[[Humidity]]", "[[Time_of_Year]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[nRMSE]]", "[[nMAE]]", "[[RPS]]", "[[Pinball_Loss]]", "[[CRPS]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Adaptive Probabilistic Forecasting of Electricity (Net-)Load

## 🎯 Main Objective & Contribution
Address the fact that both demand and supply characteristics evolve over time (COVID crisis, price shocks, growth in EV penetration and intermittent renewables) by making **probabilistic** net-load forecasting **adaptive** (online/streaming). Two main contributions:
1. A new method based on **time-varying quantile regression with online gradient descent (OGD)** on the pinball loss, where the gradient step size is chosen automatically via multiple learning rates combined with **Bernstein Online Aggregation (BOA)**.
2. Application to two case studies — regional net-load in Great Britain (14 regions) and daily demand of seven large US cities — showing substantial improvements over offline and periodically re-trained models, for both point and probabilistic forecasts.

Two-step procedure (Fig. 1): explanatory variables → mean forecast (GAM, adapted via Kalman filter) → quantile forecast (quantile regressions on residuals, adapted via OGD + BOA).

## 🧠 Methodology & Model Architecture
**Offline model (Section II-A):**
1. Gaussian GAM for the conditional mean ("GAM mean decomposition equation"):

$$y_t = \sum_{j=1}^{d} f_j(x_{t,j}) + \varepsilon_t, \qquad \varepsilon_t \sim \mathcal{N}(0,\sigma^2) \tag{1}$$

where nonlinear effects $f_j$ are built from spline bases (cubic regression splines).
2. Quantile regressions on GAM residuals ("offline quantile regression / pinball minimization"), with intermediate covariates $z_t$:

$$\beta_q \in \arg\min_{\beta\in\mathbb{R}^{d_0}} \sum_{t=1}^{n_{\text{train}}} \rho_q(y_t-\hat{y}_t,\; \beta^\top z_t) \tag{2}$$

with the **pinball (quantile) loss**:

$$\rho_q(y,\hat{y}_q) = (\mathbb{1}_{y<\hat{y}_q}-q)(\hat{y}_q-y) \tag{3}$$

Quantile prediction: $\hat{y}_t + \beta_q^\top z_t$. Lemma 1 (Koenker): $Y_q \in \arg\min_{\hat{y}} E[\rho_q(Y,\hat{y})]$.

**Adaptation of the GAM (Section II-B):** freeze nonlinear effects learned in training; standardize them into covariate vector $f(x_t)=(f_1(x_{t,1}),\dots,f_d(x_{t,d}),1)^\top$; fit a linear-Gaussian **state-space model**:

$$\theta_t - \theta_{t-1} \sim \mathcal{N}(0,Q) \tag{4}$$
$$y_t - \theta_t^\top f(x_t) \sim \mathcal{N}(0,\sigma^2) \tag{5}$$

Inference via the **Kalman filter** (Theorem 1, Kalman & Bucy), with posterior $\theta_t|\mathcal{F}_{t-1}\sim\mathcal{N}(\hat{\theta}_t,P_t)$:

$$P_{t|t} = P_t - \frac{P_t f(x_t)f(x_t)^\top P_t}{f(x_t)^\top P_t f(x_t)+\sigma^2} \tag{6}$$
$$\hat{\theta}_{t+1} = \hat{\theta}_t - \frac{P_{t|t}}{\sigma^2}\Big(f(x_t)\big(\hat{\theta}_t^\top f(x_t)-y_t\big)\Big) \tag{7}$$
$$P_{t+1} = P_{t|t} + Q \tag{8}$$

Two variance settings: **Static** ($Q=0$, $\sigma^2=1$; equivalent to annealed gradient descent) and **Dynamic** (variances learned batch-wise by greedy likelihood maximization via the R package `viking`; sparse diagonal $Q$).

**Adaptive quantile forecasts (Section II-C):**
1. *Gaussian posterior from Kalman* ("Kalman predictive distribution"): $\mathcal{L}(y_t|x_t,\mathcal{F}_{t-1})=\mathcal{N}(\hat\theta_t^\top f(x_t),\,f(x_t)^\top P_tf(x_t)+\sigma^2)$ (Eq. 9); q-quantile forecast ("Gaussian adaptive quantile"):

$$\hat{y}_{t,q} = \hat{\theta}_t^\top f(x_t) + N_q\sqrt{f(x_t)^\top P_t f(x_t)+\sigma^2} \tag{10}$$

— often poorly calibrated because variance is fixed.
2. *Offline quantile regressions on Kalman residuals* (Kalman residuals are stationary if the state-space model is well-specified).
3. *OGD on the pinball loss* ("adaptive quantile regression update"):

$$\beta_{t+1,q} = \beta_{t,q} - \alpha\,\frac{\partial\,\rho_q(y_t-\hat{y}_t,\;\beta^\top z_t)}{\partial\beta}\bigg|_{\beta_{t,q}} \tag{12}$$

4. *Step-size selection by BOA*: run OGD with step sizes $(\alpha_k)_{1\le k\le K}$, combine forecasts $\hat{y}_{t,q}=\sum_{k=1}^{K} p^{(k)}_{t,q}\hat{y}^{(k)}_{t,q}$ with weights from Bernstein Online Aggregation (R package `opera`); step sizes in $\{10^i, -8\le i\le 0\}$.

Complexity: single-pass OGD+BOA much cheaper than daily re-fitting of quantile regressions or incremental offline GAM.

## 📊 Dataset & Input Features
**1. Great Britain regional net-load** (extends [[2021_Browell_Fasiolo_Regional_Netload]] dataset from 2014–2018 to **2014–2021**, including COVID):
- Net-load = consumption − embedded generation (mostly wind & solar); 14 Grid Supply Point Groups.
- Half-hourly resolution; one-day data availability delay (day-ahead update at midnight).
- Data/supplementary material: https://doi.org/10.5281/zenodo.7849665 ; original dataset supplementary: https://doi.org/10.5281/zenodo.5031704
- GAM covariates: trend, time of year, time of day, day of week, school holidays, moving average of net-load (1-day delay), temperature at maximum population density (weather forecasts), moving average of that temperature, solar radiation × embedded solar capacity, wind speed × embedded wind capacity, precipitation. Day-ahead electricity price variable removed due to Brexit-related definition change. Region P (North Scotland) frequently has negative net-load.
- Quantile regression covariates: GAM prediction, squared prediction, solar radiation × solar capacity, wind speed, temperature, categorical time-of-day and day-of-week.

**2. US city-wide daily load during COVID** ([22] Ruan et al., Joule 2020 cross-domain COVID dataset):
- Seven US electricity markets' major cities: Boston, Chicago, Houston, Kansas City, Los Angeles, New York City, Philadelphia.
- Daily granularity, no data delay.
- GAM formula ("US city GAM equation"):

$$\text{Load}_t = \sum_{i=1}^{7}\alpha_i\mathbb{1}_{\text{WeekDay}_t=i} + \beta_1\text{BH}_t + \beta_2\text{WB}_t + \beta_3\text{LoadD}_t + f_1(\text{LoadW}_t) + f_2(t) + f_3(\text{Temp}_t) + f_4(\text{Hum}_t) + f_5(\text{Toy}_t) + \varepsilon_t \tag{20}$$

where BH/WB = bank holiday / winter break indicators, LoadD/LoadW = 1-day / 1-week load lags, Temp/Hum = temperature/humidity, Toy = time of year (thin-plate splines for $f_1$–$f_4$, cubic cyclic spline for $f_5$).
- Quantile-regression covariates vector ("US QR covariates"):

$$z_t = \Big(\hat{y}_t,\; \hat{y}_t^2,\; \sum_{i=1}^{7}\alpha_i\mathbb{1}_{\text{WeekDay}_t=i},\; \beta_1\text{BH}_t,\; \beta_2\text{WB}_t,\; \beta_3\text{LoadD}_t,\; f_1(\text{LoadW}_t),\; f_2(t),\; f_3(\text{Temp}_t),\; f_4(\text{Hum}_t),\; f_5(\text{Toy}_t),\; 1\Big)^\top \tag{21}$$

## 📈 Performance & Results
Evaluation metrics ("RMSE / MAE equations"):

$$\text{RMSE} = \sqrt{\frac{1}{|T|}\sum_{t\in T}(y_t-\hat{y}_t)^2}, \qquad \text{MAE} = \frac{1}{|T|}\sum_{t\in T}|y_t-\hat{y}_t| \tag{13,14}$$

Aggregate normalized metrics over $N$ series (unexplained-variance interpretation):

$$\text{nRMSE} = \sqrt{\frac{1}{N}\sum_{1\le i\le N}\frac{\sum_{t\in T}(y_{t,i}-\hat{y}_{t,i})^2}{\sum_{t\in T}(y_{t,i}-\bar{y}_i)^2}}, \qquad \text{nMAE} = \frac{1}{N}\sum_{1\le i\le N}\frac{\sum_{t\in T}|y_{t,i}-\hat{y}_{t,i}|}{\sum_{t\in T}|y_{t,i}-\bar{y}_i|} \tag{15,16}$$

Probabilistic scoring ("CRPS definition" and discrete "RPS approximation"):

$$\text{CRPS}(F,y) = \int_{-\infty}^{+\infty}(F(x)-\mathbb{1}_{y\le x})^2 dx = 2\int_0^1 \rho_q(y,F^{-1}(q))\,dq \tag{17}$$
$$\text{RPS}\big((\hat{y}_{q_1},\dots,\hat{y}_{q_l}),y\big) = \sum_{i=1}^{l}\rho_{q_i}(y,\hat{y}_{q_i})(q_{i+1}-q_{i-1}), \quad q_0=0,\; q_{l+1}=1 \tag{18}$$
$$\text{nRPS} = \frac{1}{N}\sum_{1\le i\le N}\frac{\sum_{t\in T}\text{RPS}((\hat{y}_{t,i,q_1},\dots,\hat{y}_{t,i,q_l}),y_{t,i})}{\sum_{t\in T}|y_{t,i}-\bar{y}_i|} \tag{19}$$

Key results:
- GB point forecasting: dynamic Kalman vs incremental offline GAM reduces nRMSE by ≈**4% in 2019, 7% in 2020, 8% in 2021**, at far lower computational cost per day (exact per-model table values in Tables I–II **not extractable** from text).
- GB probabilistic: adapting the GAM via Kalman + keeping offline QR already gives an important nRPS gain (even for stable 2019); adding OGD-adapted QR gives a tenuous difference; BOA combination **outperforms the best single expert (oracle)**. Reliability diagrams show offline model is not calibrated, Kalman Gaussian much better, adaptive QR best (Tables I–II numeric values **not extractable**).
- Embedded capacities experiment (2019, no COVID): removing solar/wind capacities increases offline nRMSE by **>10%** but **reduces** Kalman-GAM nRMSE by **0.4%**; probabilistically >10% nRPS increase offline vs −0.02% with Kalman + offline QR → adaptation learns embedded generation capacities, reducing dependence on hard-to-obtain covariates.
- US cities: best = dynamic Kalman (mean) + Kalman GAM with **adaptive** quantile regression (probabilistic); offline QR on Kalman residuals behaves poorly here — adapting the QR is crucial. Overall conclusions: adaptation of the mean yields ~**10% RMSE reduction** vs periodic retraining in all case studies; adaptive QR adds marginal benefit for GB but **reduces RPS by over 20%** for US cities (COVID impact stronger in big cities; largest gains in London among GB regions).
- Benchmark comparison against APLF ([[2021_Alvarez_APLF_Adaptive_Probabilistic_Load]]) in supplementary material.

## 💡 Limitations & Identified Research Gaps
- Adaptation of **multivariate probabilistic forecasts** (joint dependency structures) unexplored — how to adapt marginals and dependency structures simultaneously has not been studied.
- Only **non-extreme quantiles** considered; adaptive estimation of extremes (e.g., replacing the generalized-Pareto tail modeling of Browell & Fasiolo) is open and challenging.
- Gaussian Kalman posterior alone poorly calibrated (fixed variance assumption violated) — motivates nonparametric residual quantile correction.
- Gains of adaptive QR depend on regime instability (large under COVID in cities; small in stable periods/regions).
- EV relevance: paper explicitly names expected growth in **electric vehicle penetration** as a driver of changing demand patterns requiring adaptive methods.

## 📚 BibTeX & Citation Reference
```bibtex
@article{deVilmarest2024Adaptive,
  author  = {de Vilmarest, Joseph and Browell, Jethro and Fasiolo, Matteo and Goude, Yannig and Wintenberger, Olivier},
  title   = {Adaptive Probabilistic Forecasting of Electricity (Net-)Load},
  journal = {IEEE Transactions on Power Systems},
  year    = {2024},
  volume  = {39},
  number  = {2},
  pages   = {4154--4163},
  month   = mar,
  doi     = {10.1109/TPWRS.2023.3310280}
}
```

## 🔗 Key References & Citation Graph
- [[2021_Browell_Fasiolo_Regional_Netload]] [21] — base GB regional net-load model (GAM + QR + generalized Pareto tails) extended here to the adaptive setting and to 2021 data.
- [[2021_Stankeviciute_Conformal_Time_Series_Forecasting]] — same conformal/adaptive-calibration research line; the paper's quantile-recalibration approach parallels [[Zaffran2022_Adaptive_Conformal]] [20] (adaptive conformal inference for time series), which motivated using BOA to tune the quantile update online.
- [[2025_Matrone_QR_LSTM_Attention_EV_Load]] — related use of quantile regression on residuals of a mean model for probabilistic load forecasting (here: linear QR on GAM/Kalman residuals; there: QR-LSTM for EV load).
- [[2021_Obst_Vilmarest_Goude_Kalman_COVID_France]] [10] and [[2022_Vilmarest_Goude_State_Space_PostCOVID]] [11] — prior Kalman-filter adaptive point load forecasting that this work extends to probabilistic settings.
- [[2021_Alvarez_APLF_Adaptive_Probabilistic_Load]] [12] — adaptive probabilistic benchmark (hidden Markov models, Gaussian predictive distributions; poor tail calibration here).
- [[Gaillard2016_GEFCOM2014_Aggregation]] [13], [[Wintenberger2017_BOA]] [19], [[Berrisch_Ziel_CRPS_Learning]] [18] — expert aggregation lineage for online quantile forecasting.
- [[Day_Ahead_Forecasting]] — both applications forecast one day ahead (half-hourly GB net-load with 24 h update delay; daily US city load).
