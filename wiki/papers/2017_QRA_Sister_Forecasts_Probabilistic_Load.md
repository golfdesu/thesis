---
type: paper
title: "Probabilistic Load Forecasting via Quantile Regression Averaging on Sister Forecasts"
authors: [Bidong Liu, Jakub Nowotarski, Tao Hong, Rafał Weron]
year: 2017
journal_conference: "IEEE Transactions on Smart Grid, vol. 8, no. 2, pp. 730-737"
doi_url: "https://doi.org/10.1109/TSG.2015.2437877"
models_used: ["[[QRA]]", "[[Quantile_Regression]]", "[[Recency_Effect_Regression]]", "[[Taos_Vanilla_Benchmark]]"]
datasets_used: ["[[GEFCom2014]]"]
features_used: ["[[Sister_Point_Forecasts]]", "[[Temperature]]", "[[Calendar_Features]]", "[[Calendar_Features]]", "[[Calendar_Features]]", "[[Temperature]]", "[[Temperature]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[Pinball_Loss]]", "[[Winkler_Score]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Probabilistic Load Forecasting via Quantile Regression Averaging on Sister Forecasts

## 🎯 Main Objective & Contribution
- First formal study of **forecast-combination-based probabilistic load forecasting**: applies **[[QRA|Quantile Regression Averaging (QRA)]]** — previously used only for electricity *price* forecasting and by a top GEFCom2014 price-track entry — to a set of **sister point forecasts** to produce prediction intervals (PIs).
- **Sister forecasts** = point forecasts from the same family of models ("sister models") differing only in variable-selection choices (training-set length 2 vs. 3 years, calibration/partition scheme, number of lagged temperature terms). Much easier to generate than independent expert forecasts and transparent to manage.
- Practical value: QRA leverages decades of point load forecasting literature as direct input (no need for high-quality expert forecasts), and the case study uses fully public data so results are reproducible.
- Dominantly outperforms two naïve benchmarks and nine advanced empirical benchmarks on both the pinball loss function and Winkler scores.

## 🧠 Methodology & Model Architecture
Two-step methodology: (1) generate sister point forecasts, (2) run quantile regression on them.

**Step 1 — Sister models.** Base model is Tao's Vanilla benchmark (Equation 1):
$$\hat{y} = \beta_0 + \beta_1 M_t + \beta_2 W_t + \beta_3 H_t + \beta_4 W_t H_t + f(T_t) \tag{1}$$
with piecewise temperature response (Equation 2):
$$f(T_t) = \beta_5 T_t + \beta_6 T_t^2 + \beta_7 T_t^3 + \beta_8 T_t M_t + \beta_9 T_t^2 M_t + \beta_{10} T_t^3 M_t + \beta_{11} T_t H_t + \beta_{12} T_t^2 H_t + \beta_{13} T_t^3 H_t \tag{2}$$
where $M_t, W_t, H_t$ are month-of-the-year, day-of-the-week, hour-of-the-day dummies; $T_t$ is temperature. Daily moving average temperature of the $d$th previous day (Equation 3):
$$\tilde{T}_{t,d} = \frac{1}{24}\sum_{lag=24d-23}^{24d} T_{t-lag} \tag{3}$$
The family of sister recency-effect models adds sums over lagged temperatures and lagged daily moving averages (Equation 4):
$$\hat{y}_t = \beta_0 + \beta_1 M_t + \beta_2 W_t + \beta_3 H_t + \beta_4 W_t H_t + f(T_t) + \sum_d f\big(\tilde{T}_{t,d}\big) + \sum_{lag} f\big(\tilde{T}_{t-lag}\big) \tag{4}$$

**Step 2 — QRA.** Standard quantile regression with the $m$ sister point forecasts as regressors (Equation 5):
$$Q_y(q \mid X_t) = X_t \beta_q \tag{5}$$
Parameters estimated by minimizing the check loss (Equation 6):
$$\min_{\beta_q}\left[\sum_{\{t:\, y_t \geq X_t \beta_q\}} q \left| y_t - X_t\beta_q \right| + \sum_{\{t:\, y_t < X_t \beta_q\}} (1-q)\left| y_t - X_t \beta_q \right|\right] = \min_{\beta_q} \sum_t \big(q - \mathbb{1}_{y_t < X_t\beta_q}\big)\big(y_t - X_t \beta_q\big)$$
where $X_t = [1, \hat{y}_{1,t}, \dots, \hat{y}_{m,t}]$. All data are log-transformed before fitting quantiles (inverse-transformed after); PIs computed at 99 quantiles ($q = 0.01,\dots,0.99$).

**Scoring rules.** Pinball loss (Equation 7):
$$\text{Pinball}\big(\hat{y}_{t,q}, y_t, q\big) = \begin{cases} (1-q)\big(\hat{y}_{t,q}-y_t\big) & y_t < \hat{y}_{t,q} \\ q\big(y_t - \hat{y}_{t,q}\big) & y_t \geq \hat{y}_{t,q} \end{cases} \tag{7}$$
Winkler score for a central $(1-\alpha)\times100\%$ PI with bounds $L_t, U_t$ and width $\delta_t = U_t - L_t$ (Equation 8):
$$\text{Winkler} = \begin{cases} \delta, & L \leq y_t \leq U \\ \delta + 2(L_t - y_t)/\alpha, & y_t < L_t \\ \delta + 2(y_t - U_t)/\alpha, & y_t > U_t \end{cases} \tag{8}$$

**Model selection:** rolling daily recalibration over four calibration windows $L \in \{91, 122, 183, 365\}$ days; seven $\mathrm{QRA}(m)$ variants using the $m = 2,\dots,8$ best-in-window (BI, by MAE) sisters; validation on year 2010 selects the best "(S,L)" pair per score.

## 📊 Dataset & Input Features
- **[[GEFCom2014]] probabilistic load forecasting track** (public): 7 years of hourly load history (2005–2011) plus 11 years of hourly weather (2001–2011) from **25 weather stations**; the simple average of all 25 stations serves as a virtual territory-wide weather station.
- Case study uses the last six years (2006–2011): first three years calibrate the sister models only, last three for validation/testing. Eight sister forecasts built from Ind1–Ind4 (2-year training 2007–2008) and Ind5–Ind8 (3-year training 2006–2008); year 2009 (later 2010) as validation for selecting average-lag/d-lag pairs; eight sister **24-h ahead day-ahead forecasts generated on a rolling basis**, re-estimated each day.
- Actual future temperatures used as a proxy for temperature forecasts (common industry practice, per [30]).
- Features: sister point forecasts, temperature and its lags/moving averages, calendar class variables ($M_t$, $W_t$, $H_t$), interaction $W_tH_t$.
- **Data availability / links found in text**: IEEE DOI https://doi.org/10.1109/TSG.2015.2437877; color figures at http://ieeexplore.ieee.org; article repository http://www.drhongtao.com/articles (refs [2] and [26]); price-averaging code reference http://ideas.repec.org/s/wuu/hscode.html (ref [22]); GEFCom2014 competition data described in ref [21].

## 📈 Performance & Results
- **Validation period (2010)**: for every one of the three scores (pinball, 50% Winkler, 90% Winkler) and every window length, the **worst QRA model still beat the best individual sister model and the BI model** — dominance across all configurations.
- Selected pairs: pinball → QRA(8) with 183-day calibration, i.e., $(S,L)=(8,183)$ vs. Ind(1,91) and BI(–,365).
- **Test period (2011)**: QRA(8,183) PIs are consistently narrower than individual-model PIs at similar coverage (90% PI shown for winter/summer weeks); QRA is dominantly better than **all eleven benchmarks** (Vanilla, Direct, nine residual-based advanced benchmarks) on all three scores.
- Notable margins: largest gains over the equal-weight `Direct` benchmark occur on the **90% Winkler score** (the industrially critical high-percentile interval); the scenario-based `Vanilla` benchmark is much worse since it is a genuine ex-ante forecast while others use actual temperatures ex-post.
- Interpretation: combination beats any single forecast even under probabilistic scoring rules; QRA weights vary with quantile and produce time-varying interval widths (wider at peak loads after inverse log-transform), unlike constant-width empirical PIs.

## 💡 Limitations & Identified Research Gaps
- Linear QRA weights must be re-estimated in a rolling scheme; performance relies on calibration windows that track non-stationary forecast-error distributions.
- Ex-post evaluation uses actual observed temperatures rather than operational temperature forecasts (gap shrinks only as horizon grows).
- Extensions proposed by authors: apply QRA to independent expert forecasts; generate sister forecasts from other techniques ([[ANN]], [[SVM]], fuzzy regression, holiday-effect models); extend beyond short-term to long-term point forecasts; optimize sister generation and (S,L) selection on **daily peak** errors instead of all-hours scores.
- Future-work direction relevant to this vault: probabilistic forecasting of renewable generation and EV charging demand via QRA-style combination (cf. [[2025_QR_LSTM_Attention_EV_Load]]).

## 📚 BibTeX & Citation Reference
```bibtex
@article{liu2017probabilistic,
  title={Probabilistic Load Forecasting via Quantile Regression Averaging on Sister Forecasts},
  author={Liu, Bidong and Nowotarski, Jakub and Hong, Tao and Weron, Rafa{\l}},
  journal={IEEE Transactions on Smart Grid},
  volume={8},
  number={2},
  pages={730--737},
  year={2017},
  publisher={IEEE},
  doi={10.1109/TSG.2015.2437877}
}
```

## 🔗 Key References & Citation Graph
- Probabilistic scoring lineage feeding EV-charging PIs: [[2021_Probabilistic_Queuing_EV_Load]], [[2021_Hierarchical_Probabilistic_EV_Load]], [[2025_QR_LSTM_Attention_EV_Load]]
- Deep-learning successors to regression averaging: [[2020_DeepAR_Probabilistic_Forecasting]], [[2019_Deep_Probabilistic_Scheduling_Power_Markets]]
