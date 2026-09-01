---
type: paper
title: "Prediction of Electric Vehicles Charging Demand: A Transformer-Based Deep Learning Approach"
authors: [Sahar Koohfar, Wubeshet Woldemariam, Amit Kumar]
year: 2023
journal_conference: "Sustainability 2023, 15(3), 2105"
doi_url: "https://doi.org/10.3390/su15032105"
models_used: ["[[Transformer]]", "[[LSTM]]", "[[RNN]]", "[[ARIMA]]", "[[SARIMA]]"]
datasets_used: ["[[Boulder_Colorado]]", "[[Weather]]"]
features_used: ["[[Historical_Load]]", "[[Calendar_Features|Binary_Weekend_Indicator]]", "[[Temperature]]", "[[Snowfall]]", "[[Precipitation]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Prediction of Electric Vehicles Charging Demand: A Transformer-Based Deep Learning Approach

## 🎯 Main Objective & Contribution
- One of the first applications of the [[Transformer]] architecture to EV charging demand forecasting, benchmarked against [[LSTM]], [[RNN]], [[ARIMA]], and [[SARIMA]] on real-world public charging data.
- Evaluates multi-step forecasts at K = 7 (short-term), 30, 60, and 90 days ahead (long-term) using daily aggregated charging demand.
- Key finding: Transformer is comparable to LSTM at K=7 but outperforms the next-best model by 62%, 78%, and 84% for 30, 60, and 90 days ahead respectively; statistical baselines collapse to near flat-line mean predictions.

## 🧠 Methodology & Model Architecture
- Five models implemented ([[Keras]] for LSTM/RNN, [[PyTorch]] for Transformer); deep hyperparameters: hidden dim 128, 1 layer, 8 attention heads, batch size 64, 100 epochs; 80/20 chronological train/test split (first 38 months train / last ~9 months test); min-max normalization.
- **Self-attention (scaled dot-product)** — output layer at step $i$:
$$y_i = \sum_{j=1}^{n} a_{ij}\left(x_j W_V\right) \tag{15}$$
- **Softmax attention score**:
$$a_{ij} = \frac{\exp\left(e_{ij}\right)}{\sum_{k=1}^{n}\exp\left(e_{ik}\right)} \tag{16}$$
- **Scaled dot-product compatibility** ($W_Q, W_K, W_V$: learned projection matrices, $h$: model dimension):
$$e_{ij} = \frac{\left(x_i W_Q\right)\left(x_j W_K\right)^T}{\sqrt{h}} \tag{17}$$
- Encoder = masked-free multi-head self-attention + feed-forward with residual connections and layer normalization; decoder adds masked multi-head attention. Auto-regressive decoding; no recurrence → parallelizable, no vanishing gradients, direct access to arbitrary past time steps.
- **RNN update**:
$$h_t = f\left(Wh_{t-1} + Ux_t + b\right), \qquad y_t = g\left(Vh_t\right) \tag{8–9}$$
- **LSTM gates** (forget/input/candidate/cell/output):
$$f_t = \sigma\left(x_t U_f + h_{t-1} W_f\right), \quad i_t = \sigma\left(x_t U_i + h_{t-1} W_i\right), \quad \tilde{C}_t = \tanh\left(x_t U_g + h_{t-1} W_g\right)$$
$$C_t = \sigma\left(f_t \times C_{t-1} + i_t \times \tilde{C}_t\right), \quad h_t = \tanh\left(C_t\right) \times o_t \tag{10–14}$$
- **[[ARIMA]](p,d,q)**:
$$y = c + \epsilon_t + \sum_{i=1}^{p}\phi_i y_{t-i} + \sum_{i=1}^{q}\theta_j y_{t-j} \tag{1}$$
- **[[SARIMA]]**$(p,d,q)\times(P,D,Q)_s$ via lag operator $L^i y_t = y_{t-i}$ (Eq. 2) and seasonal/non-seasonal lag polynomials $\phi(L), \theta(L), \Phi(L), \Theta(L)$ (Eqs. 3–7).
- **Min–max normalization**:
$$x_N = \frac{x_t - x_{\min}}{x_{\max} - x_{\min}} \tag{18}$$
- **Evaluation metrics**:
$$RMSE = \sqrt{\frac{1}{N}\sum_{i=1}^{n}\left(\hat{y}_i - y_i\right)^2}, \qquad MAE = \frac{1}{N}\sum_{i=1}^{n}\left|\hat{y}_i - y_i\right| \tag{19–20}$$

## 📊 Dataset & Input Features
- **[[Boulder_Colorado]]**: real-world charging records from **25 public EV charging stations** in Boulder, Colorado (Type 2 connectors, 22 kW), 1 January 2018 – 28 December 2021 (~4 years). Raw sessions: **29,780 individual charging events** (0.001–85.2 kW/event); aggregated to **1,425 daily records** (0.74–531.6 kW/day) after removing missing/negative values. Daily resolution (no sub-daily data).
- **Weather data** (Boulder, CO, from National Weather Service): max/min temperature (°F), snowfall (mm/day), precipitation (mm/day).
- Calendar feature: binary weekend indicator (0/1).
- Exploratory analysis: dry season (Sep–Mar) shows higher load distribution than rainy season; weekday median/peak load exceeds weekend (public-station workday charging behavior); COVID-19 lockdown caused an abrupt demand drop mid-2020; series is non-stationary with clear seasonality.
- Data availability links:
  - Data Availability Statement: https://webappsprod.bouldercolorado.gov/opendata/ev_datadictionary.csv (accessed 16 Dec 2022)
  - City of Boulder Open Data portal: https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0/explore (accessed 28 Dec 2022)
  - Paper DOI: https://doi.org/10.3390/su15032105 (open access, CC BY 4.0)

## 📈 Performance & Results
RMSE / MSE by horizon (Table 4):

| Steps ahead | [[Transformer]] | [[LSTM]] | [[RNN]] | [[SARIMA]] | [[ARIMA]] |
|---|---|---|---|---|---|
| K=7 | **0.055** / 0.043 | 0.036 / 0.026 | 0.367 / 0.229 | 1.06 / 0.819 | 0.831 / 0.643 |
| K=30 | **0.112** / 0.085 | 0.425 / 0.317 | 0.348 / 0.224 | 1.02 / 0.776 | 0.779 / 0.586 |
| K=60 | **0.096** / 0.073 | 0.488 / 0.373 | 0.438 / 0.310 | 0.960 / 0.729 | 0.841 / 0.639 |
| K=90 | **0.085** / 0.070 | 0.522 / 0.427 | 0.564 / 0.427 | 0.903 / 0.683 | 0.920 / 0.680 |

- Transformer best model at K=30/60/90; LSTM marginally better only at K=7 (RMSE 0.036 vs 0.055).
- Long-horizon advantage attributed to global self-attention (no memory decay/error propagation as in recurrent states); ARIMA/SARIMA degrade to straight-line predictions ignoring exogenous features.
- Transformer converged fastest with lowest training loss among DL models.

## 💡 Limitations & Identified Research Gaps
- Daily aggregation only — cannot forecast sub-hourly steps (15 min, 1 h); authors recommend larger datasets with finer resolution (e.g., residential charging).
- Small sample size (1,425 points) limits deep model training.
- No traffic distribution features despite their influence on charging behavior; suggested for future work.
- Only single-layer networks tested; other regression/DL/neural architectures recommended for future analysis.

## 📚 BibTeX & Citation Reference
```bibtex
@article{koohfar2023prediction,
  author  = {Koohfar, Sahar and Woldemariam, Wubeshet and Kumar, Amit},
  title   = {Prediction of Electric Vehicles Charging Demand: A Transformer-Based Deep Learning Approach},
  journal = {Sustainability},
  volume  = {15},
  number  = {3},
  pages   = {2105},
  year    = {2023},
  doi     = {10.3390/su15032105}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — original Transformer/self-attention architecture ([Vaswani et al., arXiv:1706.03762])
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM gate formulation baseline
- [[2019_Zhu_ApplSci_EV_Load_Forecasting]] / [[2019_Zhu_EV_Load_Forecasting]] — comparative deep-learning study of EV charging load forecasting (ref [6])
- [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] — SARIMA vs RF/GBRT comparison up to 28 days ahead (ref [9])

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2023_Koohfar_Transformer_EV_Demand_refs]]
