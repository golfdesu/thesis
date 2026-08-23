---
type: paper
title: "Charging stations demand forecasting using LSTM based hybrid transformer model"
authors: [Adil Hussain, Vishwanath Eswarakrishnan, Ayesha Aslam, Sajib Tripura]
year: 2025
journal_conference: "Scientific Reports (Nature Portfolio), vol. 15, art. 36639"
doi_url: "https://doi.org/10.1038/s41598-025-20421-y"
models_used: ["[[LSTM]]", "[[Transformer]]", "[[LSTM_Transformer|Hybrid LSTM-Transformer]]"]
datasets_used: ["[[ACN_Dataset]]", "[[Caltech_ACN_Dataset]]", "[[JPL_ACN_Dataset]]"]
features_used: ["[[Historical_EV_Charging_Energy]]", "[[Lookback_Window]]"]
forecasting_horizon: "[[Long_Term]]"
metrics: ["[[MAE]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Charging stations demand forecasting using LSTM based hybrid transformer model

## 🎯 Main Objective & Contribution
- **Problem**: Accurate medium-term (30 days) and long-term (120/240 days) EV charging station (EVCS) demand forecasting is hard for single models — LSTMs miss long-range context; Transformers need large data and overfit to medium/long-term trends; LSTM+Transformer combination had been ignored for EV charging demand.
- **Contribution**: First study proposing a Transformer with an **LSTM-based encoder–decoder** ([[LSTM_Transformer]]) for EV charging demand forecasting:
  - LSTM encoder captures local/temporal dependencies of the input sequence; multi-head attention captures global long-range patterns.
  - Look-back window equals prediction period (30/120/240 daily steps).
  - Benchmarked against standalone [[LSTM]] and [[Transformer]] on two real ACN sites.

## 🧠 Methodology & Model Architecture
- **Baseline LSTM gates** (Eqs. 1–6):
$$f_t = \sigma(W_f[h_{t-1}, x_t] + b_f) \quad \text{(forget gate)}$$
$$i_t = \sigma(W_i[h_{t-1}, x_t] + b_i), \qquad \tilde{C}_t = \tanh(W_c[h_{t-1}, x_t] + b_C) \quad \text{(input gate / candidate state)}$$
$$C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t \quad \text{(cell-state update)}$$
$$o_t = \sigma(W_o[h_{t-1}, x_t] + b_o), \qquad h_t = o_t \odot \tanh(C_t) \quad \text{(output gate)}$$
- **LSTM demand output** (Eq. 7): $\hat{y}_t = W_y h_t + b_y$
- **Standalone Transformer baseline** (Eqs. 8–12): dense ReLU input encoding $i_e = \text{ReLU}(W_{input}x + b_{input})$; scaled dot-product attention
$$Attention(Q,K,V) = softmax\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
global average pooling $h_{pool} = \frac{1}{n}\sum_{i=1}^{n} h_i$; flatten $\hat{h}_{flat} = Reshape(h_{pool})$; decoder regression head $\hat{y}_t = W_{decode}h + b_{decode}$.
- **Proposed Hybrid LSTM-Transformer**: encoder = single LSTM layer (128 cells = $d_{model}$) processing input shape $(batch\_size,\ time\_steps,\ features)$ → encoded sequence $(batch\_size,\ time\_steps,\ d_{model})$; positional encoding preserves event order; multi-head attention layers + layer normalization + dropout (0.2) regularization; decoder = additional LSTM layer (128 cells) over the target sequence fused with encoder outputs via cross-attention; flatten layer → final dense output $(batch\_size,\ time\_steps,\ 1)$.
- **Hyperparameters**: MinMaxScaler normalization; [[Adam]] optimizer, lr 0.001; batch size 32; 100 epochs; ReLU activations; dropout 0.2; ReduceLROnPlateau scheduler + early stopping; fully-connected layers 64→32→1 in the baseline variant description.
- **Metrics** (Eqs. 13–14):
$$MAE = \frac{1}{N}\sum_{i=1}^{n}|y_i - \hat{y}_i|, \qquad MSE = \frac{1}{N}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

## 📊 Dataset & Input Features
- **[[ACN_Dataset]]** (Adaptive Charging Network, California):
  - [[Caltech_ACN_Dataset]] — Caltech campus parking garage, public workplace charger: **54 EVSE units + one 50 kW DC fast charger**; energy data April 2018 – mid-2021 (0–1000 kWh range).
  - [[JPL_ACN_Dataset]] — JPL campus restricted employee parking: **52 EVSEs**; data September 2018 – mid-2021 (0–1200 kWh); high utilization, drivers shuffle cars after charging.
- Aggregated daily energy consumption (kWh) as univariate time series; train/test timesteps for JPL: **739 training / 210 testing**; training ~2018–early/mid-2020(2021), test later periods per figures.
- Features: historical charging demand only (univariate, input size 1); look-back window = forecast horizon.
- **Data availability statement**: "The data will be made available upon request to the corresponding authors." ACN source: https://doi.org/10.1038/s41598-025-20421-y (paper); ACN-Data platform referenced for Caltech/JPL charging sessions.

## 📈 Performance & Results
**Caltech test set (MAE / MSE):**

| Horizon | LSTM | Transformer | LSTM-Transformer |
|---|---|---|---|
| 30 days | 38.683 / 47.658 | 39.183 / 47.507 | **32.416 / 38.221** |
| 120 days | 91.940 / 97.749 | 93.461 / 98.835 | **89.256 / 94.040** |
| 240 days | 109.754 / 114.567 | 113.956 / 117.653 | **107.452 / 112.040** |

Relative gains vs baselines: 30 d — MAE −16.18% (vs LSTM) / −17.27% (vs Transformer), MSE −19.79%/−19.56%; 120 d — MAE −2.92%/−4.50%, MSE −3.79%/−4.85%; 240 d — MAE −2.10%/−5.71%, MSE −2.20%/−4.77%.

**JPL test set (MAE / MSE):**

| Horizon | LSTM | Transformer | LSTM-Transformer |
|---|---|---|---|
| 30 days | 82.813 / 90.528 | 82.813 / 77.098 | **62.186 / 69.536** |
| 120 days | 94.231 / 98.424 | 92.247 / 97.392 | **89.526 / 93.328** |
| 240 days | 105.238 / 112.687 | 107.266 / 114.581 | **103.085 / 109.010** |

Relative gains: 30 d — MAE −24.91%, MSE −23.17% (vs LSTM) / −9.82% (vs Transformer MSE); 120 d — MAE −5.00%/−2.96%, MSE −5.17%/−4.17%; 240 d — MAE −2.05%/−3.90%, MSE −3.26%/−4.86%.
- Largest improvements at 30-day horizon; gains shrink but stay consistent at 120/240 days (longer horizons carry more uncertainty from seasonality, behavior shifts, external events). Standalone LSTM generally beat standalone Transformer.

## 💡 Limitations & Identified Research Gaps
- Higher model complexity → longer training time; restrictive for real-time/resource-limited deployment.
- Univariate, history-only inputs — no weather, traffic patterns, or user-behavior covariates; multimodal integration proposed as future work.
- No short-term evaluation (1 h / 24 h / 7 days ahead) though architecture permits it.
- Model compression and adaptive updating to shifting charging patterns left unexplored.
- Minor inconsistencies in reported numbers (e.g., abstract's 5.71%/4.85% vs conclusion attributing them differently; Table 4 lists Transformer 30-day MAE identical to LSTM).

## 📚 BibTeX & Citation Reference
```bibtex
@article{hussain2025charging,
  author  = {Hussain, Adil and Eswarakrishnan, Vishwanath and Aslam, Ayesha and Tripura, Sajib},
  title   = {Charging stations demand forecasting using {LSTM} based hybrid transformer model},
  journal = {Scientific Reports},
  volume  = {15},
  pages   = {36639},
  year    = {2025},
  doi     = {10.1038/s41598-025-20421-y}
}
```

## 🔗 Key References & Citation Graph
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM foundation
- [[2017_Attention_Is_All_You_Need]] — scaled dot-product attention / Transformer backbone
- [[2023_Koohfar_Transformer_EV_Demand]] — Transformer baseline precedent on ACN data [43]
- [[2024_Ke_Divide_Conquer_Transformer_EV]] — divide-conquer Transformer for EV charging events [47]
- [[2019_Zhu_EV_Load_Forecasting]] / [[2019_Zhu_ApplSci_EV_Load_Forecasting]] — deep learning comparative studies cited [14,15]
- [[2021_Zhang_Probabilistic_Queuing_EV_Load]] — queuing-based probabilistic framework [18]
- [[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]] — RL-based EVCS load forecasting [42]
- Related vault papers: [[2024_Feng_LSTM_Transformer_EV_Consumption]], [[2025_Hussain_CAT_Former_Short_Term_EV]]
