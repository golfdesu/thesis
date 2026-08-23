---
type: paper
title: "Ensemble Learning for Charging Load Forecasting of Electric Vehicle Charging Stations"
authors: [Xingshuai Huang, Di Wu, Benoit Boulet]
year: 2020
journal_conference: "2020 IEEE Electric Power and Energy Conference (EPEC)"
doi_url: "https://doi.org/10.1109/EPEC48502.2020.9319916"
models_used: ["[[Ensemble_Learning]]", "[[ANN]]", "[[RNN]]", "[[LSTM]]", "[[Linear_Regression]]"]
datasets_used: ["[[Boulder_EV_Charging_Dataset]]"]
features_used: ["[[Historical_Load]]", "[[Transaction_Start_Time]]", "[[Charging_Time]]", "[[Energy_Consumption]]", "[[Hourly_Aggregated_Load]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Ensemble Learning for Charging Load Forecasting of Electric Vehicle Charging Stations

## 🎯 Main Objective & Contribution
- Proposes a novel **ensemble learning-based forecasting model** for EV charging station load, combining three base learners — [[ANN]], [[RNN]], and [[LSTM]] — via **weighted averaging**, where the weights are learned by a [[Linear_Regression]] (LR) meta-learner.
- Motivation: most prior work uses only one ML model per forecaster; ensemble learning was not well studied for EV charging load forecasting. The forecast serves as a reference for grid energy dispatching and mitigates peak/valley fluctuations from disordered charging.
- Demonstrated on a real-world dataset with comparisons against 4 baselines (LR, ANN, RNN, LSTM).

## 🧠 Methodology & Model Architecture
- **ANN neuron output**:
$$a_j^l = \sigma_j^l\!\left(\sum_{i=0}^{n_{l-1}} a_i^{l-1}\omega_{ij} + b_j^l\right) \tag{1}$$
where $a_j^l$ is the output of the $j$-th node in layer $l$, $\sigma_j^l$ the activation function (ReLU), $\omega_{ij}$ and $b_j^l$ weight and bias. Architecture: 1 input layer, 3 hidden layers, 1 output layer.
- **RNN hidden/output state equations**:
$$h_T = f(Uh_{T-1} + Wx_T + b) \tag{2}$$
$$y_T = g(Vh_T + c) \tag{3}$$
with $U, W, V$ weight matrices and $b, c$ biases; $f, g$ activation functions.
- **LSTM gate/cell update equations** (input gate $i_T$, forget gate $f_T$, output gate $o_T$, memory cell $c_T$, candidate $\tilde{c}_T$):
$$\begin{bmatrix} i_T \\ f_T \\ o_T \\ \tilde{c}_T \end{bmatrix} = \begin{bmatrix} \sigma \\ \sigma \\ \sigma \\ \tanh \end{bmatrix}\left(W\begin{bmatrix} x_T \\ h_{T-1} \end{bmatrix} + b\right) \tag{4}$$
$$c_T = f_T * c_{T-1} + i_T * \tilde{c}_T \tag{5}$$
$$h_T = o_T * \tanh(c_T) \tag{6}$$
LSTM's gating mechanism addresses vanishing/exploding gradients of standard RNNs.
- **Min–max input normalization** to [0, 1] (needed because data scale strongly impacts NN training):
$$X' = \frac{X - x_{\min}}{x_{\max} - x_{\min}} \tag{7}$$
- **Training loss (MSE)** used for all models:
$$\text{MSE} = \frac{1}{N}\sum_{i=1}^{N}(y_i^p - y_i)^2 \tag{8}$$
- **Ensemble procedure**: train the three base learners on the training set; generate their predictions on training data; concatenate predictions as features with true labels as targets to train the LR meta-learner ($h_L \leftarrow L(P_T, Y)$); at test time LR combines base learner test predictions ($P_l = h_L(P_t)$), then invert normalization. LR-as-baseline uses previous loads as independent variables; LR-in-ensemble uses base learner outputs.
- Optimizers: [[Adam]] for ANN and LSTM; RMSProp for RNN. Look-back timestep = 24 hours (also tested at 12).

## 📊 Dataset & Input Features
- **[[Boulder_EV_Charging_Dataset]]**: real-world EV charging load data of all city-owned EV charging stations in Boulder, Colorado, from **1 January 2018 to 31 July 2020**, containing an overview of **20,562 random transactions**.
- Data availability / source link (ref. [24]): https://bouldercolorado.gov/open-data/electric-vehicle-charging-stations
- Fields used: transaction start time, charging time, energy consumption. Preprocessing: convert transactions → real-time charging power using charging time, aggregate into **1-hour average charging load** windows; defective data replaced by the average charging load at the same hour of the day before and after.
- Split: **70% training / 30% test**. Input look-back window: previous 24 hours (or 12) → predict current hourly load.

## 📈 Performance & Results
- Metrics: [[RMSE]] $= \sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i^p - y_i)^2}$ and [[MAE]] $= \frac{1}{N}\sum_{i=1}^{N}|y_i^p - y_i|$ (Eq. 10 and Eq. 9).
- Test set results, look-back = 24:

| Model | LR | ANN | RNN | LSTM | **Ensemble** |
|---|---|---|---|---|---|
| RMSE | 3.90 | 3.84 | 3.90 | 3.89 | **3.83** |
| MAE | 2.56 | 2.48 | 2.44 | 2.42 | **2.42** |

- Ensemble improves RMSE accuracy by **1.79%, 0.26%, 1.83%, 1.57%** vs LR, ANN, RNN, LSTM respectively; MAE improvements of **5.79%, 2.48%, 0.83%** vs LR, ANN, RNN, tied with LSTM (2.42).
- Look-back = 12 (all models degrade): Ensemble still best — RMSE **4.00**, MAE **2.57**, vs LSTM 4.13/2.83, ANN 4.06/2.80, LR 4.24/2.96, RNN 4.22/2.96.
- Qualitative: load near zero from 0:00–8:00, daily peak at noon (10:00–14:00), decline at night; clear weekly periodicity observed (week of Oct 25–31, 2019). All models follow the load trend; the ensemble shows lowest errors.

## 💡 Limitations & Identified Research Gaps
- Authors explicitly note: **only limited data is used** and only **one-step-ahead forecasting** is considered; future work targets wider-range data and multi-step forecasting methods.
- No calendar/weather covariates beyond historical load; single-station aggregation level (all Boulder city stations pooled).
- Modest gains (~1–2% RMSE over best base learner) suggest headroom via richer ensembling or probabilistic outputs.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{huang2020ensemble,
  title     = {Ensemble Learning for Charging Load Forecasting of Electric Vehicle Charging Stations},
  author    = {Huang, Xingshuai and Wu, Di and Boulet, Benoit},
  booktitle = {2020 IEEE Electric Power and Energy Conference (EPEC)},
  pages     = {1--6},
  year      = {2020},
  organization = {IEEE},
  doi       = {10.1109/EPEC48502.2020.9319916}
}
```

## 🔗 Key References & Citation Graph
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM foundation (ref. [14])
- [[2014_Kingma_Adam_Stochastic_Optimization]] — Adam optimizer for ANN/LSTM
- [[2019_Zhu_EV_Load_Forecasting]] — Zhu et al., comparative deep learning study for EV charging stations (refs. [17], [18])
- [[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]] — Q-learning-based EV charging load forecasting (ref. [19])
- Sutskever et al. (2014) — sequence-to-sequence learning (ref. [12])
