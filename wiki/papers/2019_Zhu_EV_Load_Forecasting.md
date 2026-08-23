---
type: paper
title: "Electric Vehicle Charging Load Forecasting: A Comparative Study of Deep Learning Approaches"
authors: [Juncheng Zhu, Zhile Yang, Monjur Mourshed, Yuanjun Guo, Yimin Zhou, Yan Chang, Yanjie Wei, Shengzhong Feng]
year: 2019
journal_conference: "Energies 2019, 12(14), 2692 (MDPI)"
doi_url: "https://doi.org/10.3390/en12142692"
models_used: ["[[ANN]]", "[[RNN]]", "[[LSTM]]", "[[Bi-LSTM]]", "[[GRU]]", "[[Stacked_AutoEncoder|SAEs]]"]
datasets_used: ["[[Shenzhen_PEV_Charging_Station_Dataset]]", "[[Shenzhen_PEV_Aggregator_Dataset]]"]
features_used: ["[[Historical_Load]]", "[[Minute_Level_Load]]", "[[Seasonality|Rainy/Dry_Season_Indicator]]", "[[Holiday_Flag]]", "[[Time_Step_Lookback]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[R2|R² Score]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Electric Vehicle Charging Load Forecasting: A Comparative Study of Deep Learning Approaches

## 🎯 Main Objective & Contribution
- First study to use **real-world super-short-term (minute-level) EV charging data** (rather than simulation) for multi-time-step extra-short-term PEV charging load forecasting.
- Proposes a **super-short-term multi-step forecasting framework** comparing six models — [[ANN]], [[RNN]], canonical [[LSTM]], [[GRU]], [[Stacked_AutoEncoder|SAEs]], [[Bi-LSTM]] — across three look-back time steps ($T_{\text{step}} = 1, 5, 15$ minutes).
- Headline result: [[LSTM]] performs best, reducing forecasting error by **over 30%** on all index criteria vs. the best counterparts (and ~80% MAE reduction vs. ANN).
- Claims univariate historical-load input suffices: deep sequence models capture nonlinear features and temporal correlations without exogenous variables.

## 🧠 Methodology & Model Architecture
- **Vanilla RNN** (Eqs. 1–3): hidden state recurrence and output mapping
$$S_t = \phi(U x_t + W S_{t-1} + b_1),\qquad o_t = \phi(V S_t + b_2),\qquad \hat{y}_t = \phi(o_t)$$
suffers from vanishing gradient with long sequences.
- **[[LSTM]] cell equations** (Eqs. 4–9), trained via back-propagation through time ([[BPTT]]):
$$f_t = \sigma(W_f [h_{t-1}, x_t] + b_f) \tag{Forget gate}$$
$$i_t = \sigma(W_i[h_{t-1}, x_t] + b_i) \tag{Input gate}$$
$$e_{C_t} = \tanh(W_c[h_{t-1}, x_t] + b_c) \tag{Candidate cell state}$$
$$C_t = i_t * e_{C_t} + f_t * C_{t-1} \tag{Cell memory update}$$
$$o_t = \sigma(W_o[h_{t-1}, x_t] + b_o) \tag{Output gate}$$
$$h_t = o_t * \tanh(C_t) \tag{Hidden output state}$$
with $\sigma(x) = \frac{1}{1+e^{-x}}$ (Eq. 10) and $\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ (Eq. 11).
- **Min-Max normalization** before training:
$$y = \frac{x - x_{\min}}{x_{\max} - x_{\min}} \tag{12}$$
- **Outlier detection threshold** for minute-level readings $y_{dt}$:
$$\max\left[\left|\frac{y_{dt} - y_{dt-1}}{y_{dt}}\right|,\ \left|\frac{y_{dt} - y_{dt+1}}{y_{dt}}\right|\right] \leq \epsilon_a \tag{13}$$
with linear interpolation repair for flagged values:
$$y_{dt} = \frac{y_{dt-1} + y_{dt+1}}{2} \tag{14}$$
- **Evaluation metrics**: RMSE (Eq. 15), MAPE (Eq. 16 — excluded because actual load is often $0$ during non-charging periods → division by zero), MAE (Eq. 17):
$$\text{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^{n}(\hat{y}_i - y_i)^2},\quad \text{MAE} = \frac{1}{N}\sum_{i=1}^{n}|\hat{y}_i - y_i|,\quad R^2 = 1 - \frac{\sum_{i=1}^{n}(\hat{y}_i - y_i)^2}{\sum_{i=1}^{n}(\bar{y}_i - y_i)^2} \tag{15–18}$$
- **Framework**: pre-processing (per-minute load aggregation over all piles) → normalization → sliding-window time-step input (look-back $T_{\text{step}}$; dense layer maps LSTM block output to single value) → BPTT training → inverse normalization. Implemented in Keras/TensorFlow on i7-3.0 GHz, 64 GB RAM, GTX-1080Ti GPU.
- **Hyperparameters**: ANN = 1 hidden layer; RNN/GRU/Bi-LSTM/LSTM = 2 hidden layers; SAEs = 4 hidden layers; all hidden layers 16 nodes; learning rate 0.001 (RMSprop optimizer); epochs 30; batch size 512; dropout 0.3; MAE as loss function.

## 📊 Dataset & Input Features
- **[[Shenzhen_PEV_Charging_Station_Dataset]] (Case 1)**: large-scale PEV charging station in Shenzhen with rooftop PV panels and battery energy storage; 64 bus parking spaces, 12 car charging spaces, **24 charging piles**. Original records contain charging start time, end time, total charging amount; raw data span 31 Mar 2017 – 17 Jul 2018; one full year used: 1 Jul 2017 – 30 Jun 2018 (built from data of 3 Jun 2017 – 1 Jul 2018 since night charging spans two days). Resampled to **1-minute intervals → 525,600 rows**.
- **[[Shenzhen_PEV_Aggregator_Dataset]] (Case 2)**: second minute-level dataset from a PEV aggregator of commercial building chargers in Shenzhen (more random/fluctuating profile); same year-long, 525,600-point setup.
- **Split**: 0.7/0.2/0.1 — train 1 Jul 2017–31 Jan 2018 & 22 Apr–21 May 2018; test 1 Feb–21 Apr 2018; validation 22 May–30 Jun 2018.
- **Features**: univariate [[Historical_Load]] only; seasonality analysis (rainy season April–September vs dry October–March; rainy-season peak > 40 kW), weekday/holiday patterns (Spring Festival Feb 2018 load drop), 23:00 off-peak-tariff charging spike of electric buses/taxis.
- **Data availability**: no public repository; data kindly provided by Huikun Yang, Winline Co. Ltd. (Shenzhen). Only URLs in the text are tool/library links: https://keras.io/ ; code stack TensorFlow/Keras. Paper open access under CC BY: http://creativecommons.org/licenses/by/4.0/

## 📈 Performance & Results
- **Case 1 — charging station (Table 2)**:

| T-Step | Metric | ANN | RNN | GRU | SAEs | Bi-LSTM | **LSTM** |
| :---: | :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | MAE | 2.3582 | 3.2397 | 1.9116 | 1.0886 | 1.3096 | **0.4782** |
| 1 | RMSE | 4.3078 | 3.7915 | 2.4333 | 1.5689 | 1.5996 | **0.9546** |
| 1 | R² | 0.8623 | 0.8716 | 0.9495 | 0.9403 | 0.9844 | **0.9953** |
| 5 | MAE | 3.0206 | 2.7457 | 1.3134 | 2.1616 | 0.9045 | **0.5734** |
| 5 | RMSE | 5.0117 | 3.5703 | 1.7376 | 3.1042 | 1.2288 | **0.8937** |
| 5 | R² | 0.8136 | 0.9104 | 0.9788 | 0.9323 | 0.9894 | **0.9944** |
| 15 | MAE | 2.9988 | 3.1559 | 1.3269 | 2.2516 | 0.8296 | **0.5500** |
| 15 | RMSE | 4.9680 | 3.8630 | 1.7880 | 3.1556 | 1.0934 | **0.8452** |
| 15 | R² | 0.8168 | 0.8941 | 0.9756 | 0.9292 | 0.9916 | **0.9950** |

- Final training losses (epoch 30): LSTM 0.0068/0.0065/0.0064 for 1/5/15 steps; validation loss 0.0031/0.0043/0.0034 — minimum among all six models at every setting.
- **Efficiency**: Bi-LSTM needed **58 s/epoch** at 15 time steps vs. **8 s/epoch** for LSTM.
- Sequence insight: RMSE of RNN/GRU/Bi-LSTM/LSTM decreases going 1→5 steps (sequence models prefer longer inputs); only LSTM and Bi-LSTM keep improving 5→15 steps.
- **Case 2 — aggregator (Table 3)**: LSTM again best everywhere — MAE 0.3096/0.4699/0.2864 and RMSE 0.5095/0.6219/0.4418 for 1/5/15 steps (best R² = 0.9828 at 15 steps); ANN flat at MAE ≈ 0.88–0.91 across all steps.
- Load-pattern findings: sharp load rise at 23:00 (electric buses/taxis recharge during lowest tariff after being uncommitted), decline at 03:00, rise at 08:00; higher working-day than holiday loads.

## 💡 Limitations & Identified Research Gaps
- [[MAPE]] unusable due to zero-load periods — motivates alternative relative-error metrics for sparse EV data.
- Interpolation repair (Eq. 14) only effective for minor outliers; heavy sensor error requires more specific handling.
- Univariate model ignores weather, calendar, price, and spatial context; no probabilistic/interval output; fixed shallow architecture (≤4 layers, 16 nodes) not optimized systematically.
- Aggregator case shows degraded accuracy vs. periodic station case — highly stochastic commercial profiles remain hard.
- Gap for thesis: minute-level point forecasts only; extension to multi-station spatio-temporal and probabilistic settings left open.

## 📚 BibTeX & Citation Reference
```bibtex
@article{zhu2019evchargingload,
  title={Electric Vehicle Charging Load Forecasting: A Comparative Study of Deep Learning Approaches},
  author={Zhu, Juncheng and Yang, Zhile and Mourshed, Monjur and Guo, Yuanjun and Zhou, Yimin and Chang, Yan and Wei, Yanjie and Feng, Shengzhong},
  journal={Energies},
  volume={12},
  number={14},
  pages={2692},
  year={2019},
  publisher={MDPI},
  doi={10.3390/en12142692}
}
```

## 🔗 Key References & Citation Graph
- Companion hourly-level predecessor: [[2019_Zhu_ApplSci_EV_Load_Forecasting]] (Appl. Sci. 9, 1723)
- Foundation: [[1997_Hochreiter_Long_Short_Term_Memory|Hochreiter & Schmidhuber, LSTM (1997)]]
- Related vault papers: [[2020_DeepAR_Probabilistic_Forecasting_with_Autoregressive_Recurrent_Networks]]
- Cited methodological anchors: GRU (Cho et al., 2014), Stacked denoising autoencoders (Vincent et al., JMLR 2010), Bi-LSTM (Graves & Schmidhuber, 2005), RMSprop (Tieleman & Hinton, 2012), BPTT (Werbos, 1990), Dropout (Hinton et al., 2012)
