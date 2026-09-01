---
type: paper
title: "A Method of Short-term Load Forecasting at Electric Vehicle Charging Stations through Combining Multiple Deep Learning Models"
authors: [Xiaozhou Xiong, Lanzhihao Zhou]
year: 2023
journal_conference: "2023 2nd Asia Power and Electrical Technology Conference (APET), IEEE"
doi_url: "https://doi.org/10.1109/APET59977.2023.10489548"
models_used: ["[[CNN_LSTM_Transformer_Combined_Model]]", "[[CNN]]", "[[LSTM]]", "[[Transformer]]"]
datasets_used: ["[[Boulder_Colorado]]"]
features_used: ["[[Historical_Load]]", "[[Charging_Event_Records]]", "[[Timestamp]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Method of Short-term Load Forecasting at Electric Vehicle Charging Stations through Combining Multiple Deep Learning Models

## 🎯 Main Objective & Contribution
- Propose a **combined deep learning model** for short-term load forecasting (STLF) at EV charging stations, integrating **CNN + LSTM + Transformer** to improve forecasting accuracy over single models.
- Motivation: rapid EV growth (global sales >10 million in 2022; IEA projects ~10x by 2030); concentrated charging demand causes grid overload; harmonic pollution and low power factor of charging equipment.
- Division of labor: **CNN** extracts local load-curve features, **LSTM** captures temporal/contextual long-term dependencies, **Transformer multi-head attention** captures global information.
- Contribution is an empirical combination study — also ablates all pairwise combinations (CNN+LSTM, LSTM+Transformer, CNN+Transformer) against single models.

## 🧠 Methodology & Model Architecture
Pipeline: CNN module → cascaded LSTM module → Transformer encoder → fully connected output.

**CNN module**: one convolutional layer, 3×3 kernel, 64 output channels on 1-D input (**Eq. 1, CNN Feature Extraction**):
$$X_1 = H_{3\times3}(I_{Input})$$
where $H_{3\times3}(\cdot)$ denotes the 3×3 convolution operation; yields initial features $X_1[x_1, x_2, \cdots, x_n]$.

**LSTM module**: $n$ LSTM units, input dimension 64, hidden layer dimension 128 (**Eq. 2, LSTM Recursion**):
$$f_{i+1} = L_i(x_i), \quad i = 1, 2, \cdots, n$$
where $L_i(\cdot)$ is the $i$-th LSTM unit producing time-series prediction features $F_2[f_2, f_3, \cdots, f_n]$.

Standard LSTM cell equations reproduced in the paper:
Forget gate (**Eq. 5**):
$$f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$$
Input gate and candidate cell state (**Eqs. 6–7**):
$$i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$$
$$\bar{C}_t = tanh(W_c \cdot [h_{t-1}, x_t] + b_c)$$
Cell state update (**Eq. 8**):
$$C_t = f_t \cdot C_{t-1} + i_t \cdot \bar{C}_t$$
Output gate and hidden state (**Eqs. 9–10**):
$$o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$$
$$h_t = o_t \cdot tanh(C_t)$$

**Transformer module**: two encoder layers in implementation (the paper describes the canonical architecture with N=6 identical layers, each with multi-head self-attention + feed-forward sublayer with residual connection and LayerNorm: LayerNorm(x+Sublayer(x)); $d_{model}=128$). Scaled dot-product attention (**Eq. 11, Scaled Dot-Product Attention**):
$$\mathrm{Attention}(Q,K,V)=\mathrm{Softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
Feed-forward network as Linear → GELU, then Dropout–Linear–Dropout chain (**Eqs. 12–13, Feed-Forward Network**):
$$p_i = G(L(z_i)), \quad i = 1, 2, \cdots, n$$
$$O_i = D(L(D(p_i))), \quad i = 1, 2, \cdots, n$$
where $G(\cdot)$ = GELU activation, $L(\cdot)$ = linear fully connected layer, $D(\cdot)$ = dropout.

Transformer encoding of LSTM features (**Eq. 3**):
$$F_3 = H_{Trans}(F_2)$$
Final linear prediction via fully connected layers (two linear layers mapping into higher-dimensional feature space then reducing output dimension; two normalization layers against vanishing gradients; two dropout layers against overfitting) (**Eq. 4, Output Prediction**):
$$I_{output} = H_{FC}(F_3)$$

## 📊 Dataset & Input Features
- Dataset: **BOULDER/BASELINE ST1 charging station**, year 2020, from the City of Boulder open data portal.
  - URL: https://bouldercolorado.gov/open-data/electric-vehicle-charging-stations (cited as reference [10], "Electric vehicle charging stations: Energy consumption and savings", L. Markram).
- Fields used from raw charging-event records: Start-Date-Time, Charging-Time-hh-mm-ss, Energy-kWh per charging event.
- Preprocessing: (1) compute charging end time / energy consumption per minute; (2) compute real-time load at each time point at **15-minute resolution (96 points/day)**, zero when no charging; (3) aggregate same-day points; merge timestamps and load into a two-column dataset.
- Model input: vector of the **previous 24 hours = 96 points**, predicting the current moment's load (single-step ahead). Data split 0.8/0.2 train/validation, last three days (Dec 28–30, 2020) held out as test set.
- Min-max normalization to (0, 1) (**Eq. 14, Min-Max Normalization**):
$$Y = \frac{X - X_{min}}{X_{max} - X_{min}}$$
- No exogenous features (weather, holidays, calendar) used — only historical load.

## 📈 Performance & Results
Evaluation metrics (Eqs. 15–16):
$$RMSE = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i^p - y_i)^2}, \qquad MAE = \frac{1}{N}\sum_{i=1}^{N}|y_i^p - y_i|$$

Table I — test-set performance (last 3 days, Dec 28–30, 2020):

| Model | RMSE | MAE |
|---|---|---|
| CNN | 0.428 | 0.306 |
| LSTM | 0.317 | 0.153 |
| Transformer | 0.387 | 0.271 |
| CNN+LSTM | 0.312 | 0.129 |
| LSTM+Transformer | 0.428 | 0.315 |
| CNN+Transformer | 0.303 | 0.128 |
| **CNN+LSTM+Transformer** | **0.300** | **0.120** |

- Full combination achieves lowest error: **RMSE 0.300, MAE 0.120**.
- vs. best single model (LSTM): **5.36% improvement in RMSE** and **21.27% improvement in MAE**.
- Notable negative result: LSTM+Transformer (without CNN) performs worst overall among combinations (RMSE 0.428), suggesting CNN feature extraction is essential before attention.
- Qualitative load-pattern analysis: near-zero load 0:00–7:00, morning ramp 8:00–9:00, midday peak 11:00–16:00, evening decline.

## 💡 Limitations & Identified Research Gaps
- Authors' own limitation: "**only limited data is used**" — single charging station, single year (2020), three-day test set; they plan to explore wider data and additional influencing factors (multi-faceted prediction) in future work.
- No exogenous variables (weather, temperature, holidays, tariff/price, point-of-interest) despite citing SVR work that used them.
- No comparison against classical ML baselines (SVR, PSO-SVM) or recent hybrid models; no statistical significance testing.
- Hyperparameters (kernel size, LSTM units, number of encoder layers) not systematically tuned or justified; training details (optimizer, epochs, loss function) not reported in extracted text.
- Single-step-ahead prediction only (96-point daily profile implied); no multi-horizon evaluation.
- Research gap: ensemble/hybrid approaches with richer feature sets and probabilistic uncertainty quantification remain open — connects to [[2020_Ensemble_EV_Load]] and [[2026_Hybrid_XGBoost_BiLSTM_EV_Load]].

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{xiong2023combined,
  title     = {A Method of Short-term Load Forecasting at Electric Vehicle Charging Stations through Combining Multiple Deep Learning Models},
  author    = {Xiong, Xiaozhou and Zhou, Lanzhihao},
  booktitle = {2023 2nd Asia Power and Electrical Technology Conference (APET)},
  year      = {2023},
  address   = {Nanchang, China},
  publisher = {IEEE},
  doi       = {10.1109/APET59977.2023.10489548},
  pages     = {740--744}
}
```

## 🔗 Key References & Citation Graph
- [[2019_EV_Load_Forecasting]] — reference [4]: Zhu et al., "Electric Vehicle Charging Load Forecasting: A Comparative Study of Deep Learning Approaches," Energies, vol. 12, p. 2692, 2019; found LSTM superior to RNN/GRU/BiLSTM — direct motivation for this paper's LSTM backbone.
- Aduama et al. [5], "Multi-Feature Data Fusion-Based Load Forecasting of Electric Vehicle Charging Stations Using a Deep Learning Model," Energies, vol. 16, p. 1309, 2023 — LSTM with historical weather features; addresses this paper's missing-exogenous-features gap.
- Sun et al. [1] (SVR-based station forecasting, IEEE APPEEC 2016); Liao et al. [2] (PSO-SVM, ICITBS 2019); Ahmad et al. [3] (ANN modular STLF, Energies 2019) — traditional ML baselines discussed in related work.
- Feng et al. [6] (grey theory + neural network, Energy Reports 2021) — earlier hybrid/traditional+deep combination approach.
- Hochreiter & Schmidhuber [7] (LSTM, 1997); Vaswani et al. [9] ("Attention Is All You Need," NeurIPS 2017) — foundational components.
- Related vault lines: [[2020_Ensemble_EV_Load]] and [[2026_Hybrid_XGBoost_BiLSTM_EV_Load]] — same problem setting (EV charging station STLF via combined/hybrid deep models), useful for comparative discussion of combination strategies.
