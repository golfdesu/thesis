---
type: paper
title: "Mid-Term Load Forecasting for Electric Vehicle Charging Stations Based on LASSO-BPNN"
authors: [Yifan Ma, Zhiyun Yu, Zhizhuo He, Junzhe Zhao]
year: 2024
journal_conference: "2024 IEEE 2nd International Conference on Control, Electronics and Computer Technology (ICCECT)"
doi_url: "https://doi.org/10.1109/ICCECT60629.2024.10546219"
models_used: ["[[MLP]]", "[[XGBoost]]", "[[SVR]]", "[[Random_Forest]]"]
datasets_used: ["[[Qingpu_State_Grid_EV_Stations]]", "[[Shanghai_Qingpu_Statistics_Bureau]]"]
features_used: ["[[Historical_Load]]", "[[Weather_Traffic]]", "[[Economic_Indicators]]", "[[Social_Indicators]]"]
forecasting_horizon: "[[Long_Term]]"
metrics: ["[[RMSE]]", "[[MAPE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Mid-Term Load Forecasting for Electric Vehicle Charging Stations Based on LASSO-BPNN

## 🎯 Main Objective & Contribution
- Proposes **LASSO-BPNN**, a combined model for **mid-term (monthly) load forecasting of EV charging stations**, addressing the gap that most EV charging-load research targets short/super-short-term horizons and considers only weather + time series.
- Contributions: (a) combined LASSO→BPNN pipeline that **selects station-type-specific influencing factors**; (b) a broadened 15-indicator system spanning **environmental, economic, and societal** factors (beyond weather-only prior work); (c) multi-scenario design with four charging-station types (Residential / Office / Attraction / Highway areas) to support State Grid planning decisions in Qingpu District, Shanghai.
- Motivation: stations in the same district share weather yet show divergent load trends → non-weather (economic/social) drivers matter; mid-term forecasts serve the **system planning phase** during rapid charging-infrastructure build-out.

## 🧠 Methodology & Model Architecture
Five-step pipeline: collect load (State Grid) + factor data (statistics bureau monthly reports) → preprocess (missing values, normalization, four areas) → **LASSO** regression per area to screen variables by coefficients → per-area **BPNN** trained on selected variables with **grid search + cross-validation** hyperparameter tuning → evaluation.

### LASSO feature selection
**Eq. 1 – LASSO estimator** (L1 penalty shrinks insignificant coefficients to zero, promoting sparsity; $\lambda$ controls penalty strength):
$$\min_{\beta_0,\beta}\ \frac{1}{2n}\sum_{i=1}^{n}\Bigl(y_i-\beta_0-\sum_{j=1}^{m}\beta_j x_{ij}\Bigr)^2 + \lambda\sum_{j=1}^{m}|\beta_j|$$
(As printed the source shows $\sum^{m}_{i=1}$ subscripts due to typesetting/OCR; standard form given. Small $\lambda$ → fewer coefficients zeroed; large $\lambda$ → fewer variables retained.)

### BP neural network
Single-hidden-layer BPNN (universal approximation justification cited). With input $X=(x_1,\ldots,x_n)$, output $y$, randomized initial weights $w_{ij}=\mathrm{random}(i,j)$, biases $b_{ij}$:
**Eq. 2 – forward pass**: $$\hat{y} = \sum w_{ij}x_i + b_{ij}$$
**Eq. 3 – error**: $$err = \frac{1}{2}\sum(\hat{y}_k - y_k)^2$$
**Eqs. 4–5 – weight/bias update (gradient descent)**:
$$w(k+1) = w(k) - \eta\frac{\partial\, err}{\partial w(k)}\qquad b(k+1) = b(k) - \eta\frac{\partial\, err}{\partial b(k)}$$
Iterated until error within tolerance or max iterations. Grid-searched hyperparameters: learning rate, activation function, solver, hidden layer structure.

### Metrics (as printed)
**Eq. 6 – MAPE** (source prints $1/2$ where $1/n$ is evidently intended): $$\mathrm{MAPE}(y,\hat{y}) = \frac{1}{n}\sum_{i=1}^{n}\left|\frac{\hat{y}_i - y_i}{y_i}\right|$$
**Eq. 7 – RMSE**: $$\mathrm{RMSE}(y,\hat{y}) = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(\hat{y}_i-y_i)^2}$$
where $n$ = sample size (calendar months), $y_i$ real monthly charging loads, $\hat{y}_i$ predictions.

## 📊 Dataset & Input Features
- **Load data — [[Qingpu_State_Grid_EV_Stations]]**: total positive active power of EV charging stations from **State Grid**, Qingpu District, Shanghai, **July 2022 – July 2023** (monthly via differencing). Four representative station types: **Residential Area** (data starts Oct 2022), **Office Area**, **Attraction Area**, **Highway Area**.
  - Access status: **not public** — internal State Grid operational data; no URL/repository.
- **Exogenous data — [[Shanghai_Qingpu_Statistics_Bureau]]**: Monthly Statistical Report of Shanghai Qingpu District Municipal Statistics Bureau — **https://www.shqp.gov.cn/stat/tjzltjyb/** — access status: **public government website**.
- **15-factor indicator system (Table I)**:
  - *Environment*: ENV1 temperature (monthly avg ℃), ENV2 precipitation (mm), ENV3 wind speed (m/s), ENV4 humidity (%), ENV5 AQI good rate (%).
  - *Economic*: ECO1 new-energy industry gross output value, ECO2 transportation operating revenue, ECO3 transportation public budget expenditure, ECO4 fixed-asset investment, ECO5 automobile goods sales (all ￥ million), ECO6 new energy vehicle production, Shanghai (million units).
  - *Society*: SOC1 working days/month, SOC2 total social electricity consumption (billion kWh), SOC3 transportation electricity consumption (million kWh), SOC4 tourist arrivals (10,000 units), SOC5 people arrivals to Shanghai.
- **Preprocessing**: Jan/Feb statistics released only cumulatively (combined survey since 2012) → missing months imputed by **nearest neighbor interpolation** (avg of Dec 2022 & Mar 2023 assigned to Feb, cumulative sums adjusted Jan); inputs **z-score normalized** (**Eq. 8**): $x_j^n = \dfrac{x_j-\min(x_j)}{\max(x_j)-\min(x_j)}$ shown as max–min form for load display, while **Eq. 9 z-score** used for model inputs: $z_j = \dfrac{z_j-\mu_j}{\sigma_j}$.
- **LASSO screening results (Table II)**: λ = 7.28 (Residential), 6.68 (Office), 15.68 (Attraction), 2.98 (Highway); >half of factors eliminated per area. Notable retained coefficients: Residential — temperature −10.12, EV production −27.83; Office — AQI good rate −16.39, public budget 21.36, transportation electricity 19.18; Attraction — AQI good rate 8.47, precipitation −1.24, tourist arrivals −8.97; Highway — operating revenue 14.06, tourist arrivals 9.31, people arrivals 7.31. Insights: temperature kept only for Residential; vehicle sales correlated everywhere; Residential unaffected by social factors; Highway keeps most government/industry economic factors.

## 📈 Performance & Results
Test sets: April–July 2023 (Residential: May–July 2023). Comparators: BPNN alone, LASSO-SVR, LASSO-XGBoost, LASSO-RF. **Caveat: Table III's model-label column is misaligned/duplicated in the source text ("LASSO-RF" appears twice, header row shifted); row-to-model assignment below follows the printed label sequence and may be off by one — treat exact pairings with caution.**

Printed metric rows (RMSE | MAPE per area):

| Printed label | Residential | Office | Attraction | Highway |
|---|---|---|---|---|
| Row A (printed "LASSO-XGBoost") | 43.523 \| 16.666 | 39.291 \| 9.331 | 57.257 \| 31.837 | 33.028 \| 14.054 |
| Row B (printed "LASSO-SVR") | 47.360 \| 16.402 | 79.853 \| 17.569 | 54.563 \| 31.277 | 21.383 \| 8.606 |
| Row C (printed "BPNN") | 28.863 \| 11.726 | 47.592 \| 14.374 | 57.621 \| 32.573 | 37.394 \| 16.4 |
| Row D (printed "LASSO-BP") | 20.631 \| 8.639 | 66.275 \| 14.007 | 46.557 \| 35.568 | 51.258 \| 23.985 |
| Row E (printed "LASSO-RF") | 9.973 \| 3.630 | 42.967 \| 10.350 | 22.892 \| 18.490 | 19.604 \| 7.281 |

Qualitative conclusions (unambiguous in text):
- **LASSO-BPNN outperforms plain BPNN** — e.g., best-case Residential RMSE improves from 28.863 to 20.631 (≈29% lower) and MAPE 11.726% → 8.639%; gains most visible under large load fluctuations.
- **Tree-based models (esp. XGBoost) overfit**: superior training-set fit but poor test performance, attributed to small dataset size vs model complexity.
- BPNN beats SVR-type ML baselines on the metrics; feature selection prevents overfitting while preserving key drivers → claimed robustness across unseen station types.
- No single numeric table entry is explicitly labeled "LASSO-BPNN" cleanly in the extracted text; the paper states LASSO-BPNN achieved the highest accuracy among compared models, but its exact RMSE/MAPE cell values are **partially not extractable** due to table corruption.

## 💡 Limitations & Identified Research Gaps
- Very short history (13 monthly points; 12 for Residential) → severe sample-size constraint motivating LASSO regularization but limiting deep-learning alternatives; authors acknowledge time constraints of a nascent industry.
- Monthly granularity only; authors' stated future work: extend to **shorter periods** and apply to grid scheduling and charging-station siting optimization.
- Table III presentation defects make exact quantitative comparison non-reproducible from text alone.
- Load data proprietary (State Grid internal) → external validation impossible; no confidence intervals/uncertainty estimates.
- Feature pool limited to Qingpu/Shanghai statistics-bureau indicators; transferability to other districts untested.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{ma2024lasso,
  author    = {Ma, Yifan and Yu, Zhiyun and He, Zhizhuo and Zhao, Junzhe},
  title     = {Mid-Term Load Forecasting for Electric Vehicle Charging Stations Based on LASSO-BPNN},
  booktitle = {2024 IEEE 2nd International Conference on Control, Electronics and Computer Technology (ICCECT)},
  year      = {2024},
  pages     = {630--635},
  address   = {Jilin, China},
  month     = apr,
  doi       = {10.1109/ICCECT60629.2024.10546219}
}
```
Affiliations: Ma/Yu/He — State Grid Shanghai Electric Power Company; Zhao (corresponding) — University of Science and Technology China, Hefei. Funded by State Grid Shanghai Electric Power Company fund (Project No. 520934230005).

## 🔗 Key References & Citation Graph
- **[3] Buzna et al., SyNERGY MED 2019** — time series vs ML comparison for EV load (cf. vault [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]]).
- **[4] Dabbaghjamanesh et al.** — Q-learning EVCS load forecasting under scenarios (cf. vault [[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]]; note the paper's reference list attributes this work differently than the introduction text).
- **[5] Zhu et al., Energies 2019** — deep learning comparative study; LSTM best for super-short-term (cf. vault [[2019_Zhu_EV_Load_Forecasting]]).
- **[1] Zhang et al., Applied Energy 2020**; **[2] de Quevedo et al., IEEE TSG 2017**; **Zhou et al., Energies 2022** (Bayesian LSTM uncertainty).
- Related vault pages: model counterparts [[XGBoost]] and [[MLP]] (BPNN = MLP-family network trained by back-propagation; XGBoost here is an overfitting-prone baseline), [[SVR]]. Related papers: [[2024_Huo_Data_Driven_EVCS_Demand_Forecasting]] (short-term counterpart using MLP/SVR/BRT on public ACN data), [[2024_Li_TOU_Price_Meteorology_EV_Charging_Load]] (alternative exogenous-feature selection route via Pearson/MIC rather than LASSO).
