---
type: paper
title: "EV Charging Load Forecasting Method Considering Time-of-Use Price and Meteorological Factors"
authors: [Guangxiao Li, Yilu Yang, Chunyi Wang, Ziyu Xu, Yue Wang, Yutian Liu]
year: 2024
journal_conference: "2024 7th International Conference on Power and Energy Applications (ICPEA)"
doi_url: "https://doi.org/10.1109/ICPEA63589.2024.10784728"
models_used: ["[[CNN]]", "[[GRU]]", "[[LSTM]]", "[[MLP]]"]
datasets_used: ["[[Jining_Mall_EV_Charging_Station]]"]
features_used: ["[[Historical_Load]]", "[[Electricity_Tariff]]", "[[Weather_Traffic]]", "[[Cyclical_Encodings]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: EV Charging Load Forecasting Method Considering Time-of-Use Price and Meteorological Factors

## 🎯 Main Objective & Contribution
- Proposes an EV charging station load forecasting method that explicitly incorporates **time-of-use (TOU) price** and **meteorological factors** alongside historical load.
- Contribution chain: (1) quantitative factor screening via **Pearson correlation coefficient** (load-load autocorrelation) and **Maximum Information Coefficient (MIC)** (load-factor nonlinear coupling); (2) **[[CNN]] feature extraction** from the multi-dimensional inputs; (3) **two-layer [[GRU]]** for temporal dependency capture; (4) forecasting at multiple time scales (**4 h, 24 h, 72 h, 168 h**) with demonstrated superiority over BP, LSTM, and GRU baselines.
- Key empirical insight: mall-located station shows strong price-based demand response — load peaks during off-peak-price periods and is higher on weekends/holidays than weekdays.

## 🧠 Methodology & Model Architecture
### Factor screening
**Pearson autocorrelation (Eq. 1)** — used to determine the fluctuation period of the load sequence (one month of data analyzed; lag set $a=720$; OCR-degraded in source, reconstructed standard form):
$$\rho_A = \frac{\sum_{a=1}^{N-A}(x_a-\bar{x})(x_{a+A}-\bar{x})}{\sum_{a=1}^{N}(x_a-\bar{x})^2}$$
where $\rho$ = autocorrelation coefficient, $N$ = length of load sequence, $\bar{x}$ = mean. Result: clear daily cycle; same-time correlations for previous 2 hours and previous 18 days both > 0.6 ("high" band); correlation decays with forecast distance → recent historical load emphasized.

**Mutual information (Eq. 2)** and **Maximum Information Coefficient (Eqs. 3)**:
$$I(x,y) = \iint p(x,y)\log\frac{p(x,y)}{p(x)\,p(y)}\,\mathrm{d}x\,\mathrm{d}y$$
$$\mathrm{MIC}(x,y) = \max_{ab<B} \frac{I(x,y)}{\log_2 \min(a,b)}$$
where $ab$ is the number of grid distributions; $B$ empirical value ≈ 0.6 × number of samples. MIC ∈ [0,1] captures linear AND nonlinear relations uniformly.

Selected factors (Table II): temperature (Pearson 0.4738, MIC 0.5698), TOU price (0.7259, 0.5946), weekday type (−0.4455, 0.3261). Rejected: rain (0.2867, 0.2110), wind (0.1133, 0.1025).

### CNN-GRU model
Four parts: input layer → CNN feature-extraction network (convolution kernels extract local features; pooling reduces dimensionality/anti-overfitting; fully connected layer flattens) → **two-layer GRU network** → output layer emitting next $n$ consecutive points.

**Input vector (Eq. 5 – training vector construction)**: recent history = first 24 moments before predicted moment + $m$ discontinuous points $l_{t-48}, l_{t-72}, l_{t-168}$, spliced with current exogenous data:
$$x_t = \mathrm{Concat}\bigl(l_{t-1}, l_{t-2}, \ldots, l_{t-m},\ \mathrm{temp}_t,\ \mathrm{price}_t,\ \mathrm{week}_t\bigr)$$

**GRU equations (Eq. 4)** — as printed (OCR-degraded vertical layout; reconstructed standard form). Note: the source text's gate naming ("$r_t$, $x_t$ and $z_t$ are the update gate, input gate, and reset gate") is internally inconsistent; standard GRU notation given here:
$$z_t = \sigma\bigl([h_{t-1}, x_t]\,w_z\bigr)\qquad r_t = \sigma\bigl([h_{t-1}, x_t]\,w_r\bigr)$$
$$\tilde{h}_t = \tanh\bigl([r_t \times h_{t-1},\, x_t]\,w\bigr)\qquad h_t = (I - z_t)\times h_{t-1} + z_t\times \tilde{h}_t$$
with $w_z,w_r,w$ weight matrices, $\sigma$/tanh activations, $[\cdot]$ vector concatenation, $I$ identity matrix. GRU chosen over LSTM for its two gates vs three → computationally cheaper, less training time.

**Training**: RMSE as loss function, Adam optimizer, 50 training rounds, ReLU activation.

**Metrics (Eqs. 6–7)**:
$$\mathrm{MAE} = \frac{1}{n}\sum_{i=1}^{n}\left|y_i - \hat{y}_i\right|\qquad \mathrm{RMSE} = \sqrt{\frac{1}{n}\sum_{i=1}^{n}\left(y_i - \hat{y}_i\right)^2}$$

## 📊 Dataset & Input Features
- **Dataset**: charging power data of one EV charging station with a **capacity of 1800 kW** located in a large underground shopping-mall parking lot in a **prefecture-level city in China**, spanning **nearly one year**, at **1-hour resolution**, managed by a dedicated EV charging operator.
  - Access status: **NOT public** — proprietary operator/utility data; no URL or repository provided in the paper. Not independently downloadable.
  - Service charge at the station: **0.45 Yuan/kWh** (vs home charging).
  - Data cleaning: missing/abnormal values (failures/maintenance) corrected by a **modified GAN** (ref. [6] Tao et al., IEEE TTE 2022).
- **TOU price scheme**: peak **1.1526 Yuan/kWh** (8:00–11:00 & 17:00–22:00); flat **0.6703 Yuan/kWh**; off-peak **0.2805 Yuan/kWh** (0:00–8:00). (Flat-period boundaries garbled in extracted text.)
- **Meteorological features gathered**: temperature, rainfall, wind speed (numerically processed per ref. [7]); rain/wind then rejected by MIC screening.
- **Calendar features**: weekday type (weekday/weekend/holiday) — cyclical/calendar feature usage connects to [[2021_Day_Ahead_EV_Demand]], which likewise encodes day-type/cyclic calendar effects for day-ahead EV demand.
- Empirical load patterns (Fig. 1): weekday load lower than weekend/holiday; zero-load scenarios occur (mall closed at night even in low-price period); load concentrated after 18:00 on weekdays; users shift charging to off-peak price windows (price-based demand response).

## 📈 Performance & Results
Baselines: BP, LSTM, GRU. Training set: **first 18 days of data**; forecast lengths 4 h / 24 h / 72 h / 168 h (Table III):

| Length | BP MAE | BP RMSE | LSTM MAE | LSTM RMSE | GRU MAE | GRU RMSE | CNN-GRU MAE | CNN-GRU RMSE |
|---|---|---|---|---|---|---|---|---|
| 4h   | 53.49 | 58.49 | 42.10 | 50.41 | 49.04 | 50.29 | **36.33** | **46.42** |
| 24h  | 64.77 | 79.81 | 62.65 | 80.88 | 59.72 | 75.77 | **50.35** | **64.04** |
| 72h  | 57.38 | 73.93 | 55.36 | 72.79 | 58.89 | 76.68 | **52.81** | **69.09** |
| 168h | 58.31 | 75.07 | 56.83 | 74.06 | 58.66 | 77.09 | **54.32** | **71.50** |

(Note: body text quotes 168 h MAE as 54.329 while the table prints 54.32.)
Findings:
- CNN-GRU achieves lowest MAE/RMSE at **every** horizon; best relative gains at short horizons (4 h: MAE 36.33 vs GRU 49.04, ≈26% lower).
- Competing models' errors fluctuate strongly as horizon grows; CNN-GRU shows small error variation across horizons → good stability (4 h→168 h RMSE degradation only +25.08 vs +26.80 for GRU, larger for BP/LSTM).
- Visual check (Fig. 5, 168 h): CNN-GRU curve tracks actual load closely and captures trend changes.

## 💡 Limitations & Identified Research Gaps
- Single station, ~1 year of hourly data; very small training set (first 18 days) — generalization untested; no cross-station validation.
- Authors' own future work: explore impact of **additional external factors** on load forecasting to improve applicability and accuracy.
- Only point forecasts; no probabilistic/uncertainty quantification.
- TOU flat-period definition partially unreadable in source text; dataset private → results not reproducible externally.
- No comparison against attention/Transformer-class models or against persistence baseline.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{li2024tou,
  author    = {Li, Guangxiao and Yang, Yilu and Wang, Chunyi and Xu, Ziyu and Wang, Yue and Liu, Yutian},
  title     = {EV Charging Load Forecasting Method Considering Time-of-Use Price and Meteorological Factors},
  booktitle = {2024 7th International Conference on Power and Energy Applications (ICPEA)},
  year      = {2024},
  pages     = {610--614},
  address   = {Jining/Jinan, China},
  doi       = {10.1109/ICPEA63589.2024.10784728}
}
```
Affiliations: Li/Yang/Yue Wang — State Grid Jining Power Supply Company; Chunyi Wang — State Grid Shandong Electric Power Company; Ziyu Xu (corresponding)/Yutian Liu — Shandong University. Funded by State Grid Shandong Electric Power Company Technology Project 520606240008.

## 🔗 Key References & Citation Graph
- **[8] Reshef et al., Science 2011** — original MIC ("Detecting Novel Associations in Large Data Sets").
- **[6] Tao, Qiu, Lai, IEEE TTE 2022** — modified GAN used for abnormal-value correction.
- **[7] Xu et al., ICPST 2024** — LSTM-recursion short-term EVCS prediction; source of meteorological processing approach.
- **[3] Ferro et al., IEEE TVT 2020** — TOU pricing background.
- **[9] Zhang et al., IEEE Trans. Cybernetics 2021** — deep-learning EV charging forecasting context.
- Related vault papers: [[2021_Day_Ahead_EV_Demand]] (↔ shared use of cyclical/calendar/day-type features for station-level EV demand), [[2024_Data_Driven_EVCS_Demand_Forecasting]] (pure-autoregressive counterpart on public ACN data), [[2024_LASSO_BPNN_Mid_Term_EV_Load]] (alternative exogenous-feature route via LASSO screening).
