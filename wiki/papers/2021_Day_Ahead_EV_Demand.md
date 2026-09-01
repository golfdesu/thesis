---
type: paper
title: "Day-Ahead Forecast of Electric Vehicle Charging Demand with Deep Neural Networks"
authors: [Gilles Van Kriekinge, Cedric De Cauwer, Nikolaos Sapountzoglou, Thierry Coosemans, Maarten Messagie]
year: 2021
journal_conference: "World Electric Vehicle Journal, 12(4), 178"
doi_url: "https://doi.org/10.3390/wevj12040178"
models_used: ["[[LSTM]]", "[[LSTM_B]]", "[[LSTM_C]]", "[[LSTM_W]]", "[[RNN]]"]
datasets_used: ["[[Hospital_Semi_Public_Charging_Site_Dataset]]"]
features_used: ["[[EV_Charging_Demand]]", "[[EV_Charging_Demand]]", "[[Cyclical_Quarter_Hour_Features]]", "[[Cyclical_Day_Number_Features]]", "[[Holiday_Flag]]", "[[Holiday_Flag]]", "[[Temperature]]", "[[Daily_Rainfall]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Day-Ahead Forecast of Electric Vehicle Charging Demand with Deep Neural Networks

## 🎯 Main Objective & Contribution
- Enhances a state-of-the-art deep neural network to forecast the **day-ahead aggregated EV charging demand** at **15-min resolution** (96 timesteps/day) for a **small, highly stochastic EV fleet** — a use case underrepresented in the literature (most work targets large fleets or super-short-term horizons).
- New contributions over the reference forecaster ([[LSTM_B]], from Zhu et al.): additional calendar and weather input features, a **variable learning rate function**, and **forecast post-processing** rules; plus a feature-importance analysis.
- Main achievement: day-ahead forecast of high-stochasticity demand with **MAE < 1 kW**; MAE reduced by up to **28.8%** and RMSE by **19.22%** thanks to calendar/weather features. Extended version of the authors' EVS34 paper.

## 🧠 Methodology & Model Architecture
### Data transformation
Raw individual charging sessions (RFID, arrival/departure times, kWh energy) → individual EV charging profiles via average power (**Average Power Equation**):
$$P_{avg} = \frac{\text{Energy consumed [kWh]}}{\text{Parking time [h]}} \tag{1}$$
Individual profiles are stacked into the aggregated EV charging demand time series. This indirectly encodes user charging flexibility (same energy over shorter parking time → higher power).
Min–max normalization (**Min-Max Normalization**), selected over z-score after preliminary tests:
$$x_N = \frac{x_t - x_{\min}}{x_{\max} - x_{\min}} \tag{2}$$

### RNN / LSTM background equations
RNN hidden and output states:
$$h_t = f(Uh_{t-1} + Wx_t + b) \tag{3}$$
$$y_t = g(Vh_t + c) \tag{4}$$
LSTM gates and cell (input gate $i$, forget gate $f$, output gate $o$, candidate/unit $m$, memory $c$; sigmoid activation $s$):
$$i_t = s(W_i(x_t + h_{t-1}) + b) \tag{5}$$
$$f_t = s(W_f(x_t + h_{t-1}) + b) \tag{6}$$
$$o_t = s(W_o(x_t + h_{t-1}) + b) \tag{7}$$
$$m_t = \tanh(W_m(x_t + h_{t-1}) + b) \tag{8}$$
$$c_t = f_t \times c_{t-1} + i_t \times m_t \tag{9}$$
$$h_t = o_t \times \tanh(c_t) \tag{10}$$
All configurations: input layer + **two hidden layers** + output layer; implemented in Python/TensorFlow/Keras.

### Cyclical feature transformations
Quarter-hour ($DT \in [0,95]$) and day-number ($D \in [0,6]$) periodicities encoded as sine/cosine pairs (**Cyclical Encoding Equations**):
$$DT_{\sin/\cos} = \begin{cases}\sin(DT\times2\pi\times\frac{1}{96}) \\ \cos(DT\times2\pi\times\frac{1}{96})\end{cases} \tag{11}$$
$$D_{\sin/\cos} = \begin{cases}\sin(D\times2\pi\times\tfrac{1}{7}) \\ \cos(D\times2\pi\times\frac{1}{7})\end{cases} \tag{12}$$

### Configurations & training
| Parameter | LSTM-B | LSTM-C | LSTM-W |
|---|---|---|---|
| Epochs | 30 | 50 | 50 |
| Batch size | 512 | 192 | 192 |
| Optimizer | RMSprop | [[Adam]] | Adam |
| Loss function | MAE | MSE | MSE |
| Learning rate | 0.001 | variable (0.001→0.0005) | variable |
| Hidden neurons | 16 | 25* | 30* |
| Activation | tanh | tanh* | tanh* |
| Dropout | 0.3 | 0* | 0.3* |

(*hyperparameters tuned by Bayesian optimization with Gaussian processes, Scikit-optimize.) Variable learning rate (**Stepwise LR Schedule**):
$$\text{learning rate} = \begin{cases}0.001 & \text{when epochs} < 20\\ 0.0005 & \text{when epochs} \geq 20\end{cases} \tag{13}$$

### Post-processing
Two domain rules: negative forecasts set to zero; night demand (00:00–05:00) set to zero (mean observed demand is zero in that window).

## 📊 Dataset & Input Features
- **[[Hospital_Semi_Public_Charging_Site_Dataset]]**: real charging sessions from a hospital semi-public site in Belgium with **6 chargers × two Type 2 connectors of 22 kW each** (12 outlets). Period: **mid-June 2018 – end July 2019** (~1 year); **15-min timestep** resolution; 95.2% of sessions from commuters; max average power up to ~30 kW (≈6× the mean).
- Split: training/validation/test = **0.7/0.2/0.1** chronological partition.
- Data availability statement: *"The datasets used during the current study are not available since they are protected by privacy reasons, mainly because of the presence of EV users' radio frequency identification (RFID)."* No public URL/DOI for the data.
- Feature table: Load — EV charging demand [kW] (all models), average weekly EV demand [kW]; Calendar — quarter-hour number, day number, binary working day, binary holiday (LSTM-C, LSTM-W); Weather — daily temperature [°C], daily rainfall [mm/h] (LSTM-W only).
- Other URLs found in text: https://www.iea.org/reports/electric-vehicles ; TensorFlow https://www.tensorflow.org/ ; VIANN code https://github.com/rebelosa/feature-importance-neural-networks ; funding VLAIO grant HBC.2018.0519.

## 📈 Performance & Results
Metrics: RMSE $= \sqrt{\frac{1}{N}\sum_{t=1}^{N}(\hat{P}_t - P_t)^2}$ (Eq. 14), MAE $= \frac{1}{N}\sum_{t=1}^{N}|\hat{P}_t - P_t|$ (Eq. 15), N = 96 timesteps per day-ahead forecast.
Test-subset results:

| Model | MAE | RMSE |
|---|---|---|
| LSTM-B (reference) | 1.25 kW | 2.29 kW |
| LSTM-C (calendar) | 0.96 kW (−23.2%) | **1.85 kW (−19.22%)** |
| LSTM-W (weather) | **0.89 kW (−28.8%)** | 1.92 kW (−16.16%) |

- Calendar features help most on peaks/extreme days (lowest RMSE); weather features improve overall MAE.
- Two-week example: on 13 & 15 July, LSTM-W reduced RMSE by up to **92.7%** and MAE by up to **92.5%** vs LSTM-B (correctly forecasting Saturday as non-working day).
- Weekend days remain hard (random non-commuter sessions unpredicted by all networks).
- Feature importance (VIANN weight analysis): past-24-h demand dominant for both; binary holiday most important calendar feature for LSTM-C; weather features carry large weights in LSTM-W. Leave-One-Feature-Out: removing the binary holiday feature raises that day's MAE **5.78×** and RMSE **6.11×** (15 Aug, Belgian national holiday).
- Timing (Intel Xeon E-2176M, 64 GB RAM): training+validation 3.88–15.04 min; one day-ahead forecast ≈ **0.063–0.068 s** → real-time capable.

## 💡 Limitations & Identified Research Gaps
- Average-power profile construction yields discrete steps in the real aggregated demand curve that the networks cannot accurately predict.
- Poor weekend forecasts due to stochastic non-commuter behavior.
- Dataset private (RFID privacy) — no public benchmark reproducibility.
- Single use case only; authors call for testing across different sites to check whether behavioral patterns generalize and to guide forecaster selection per application.
- Point forecast only — no probabilistic/uncertainty output despite high stochasticity.

## 📚 BibTeX & Citation Reference
```bibtex
@article{vankriekinge2021dayahead,
  title   = {Day-Ahead Forecast of Electric Vehicle Charging Demand with Deep Neural Networks},
  author  = {Van Kriekinge, Gilles and De Cauwer, Cedric and Sapountzoglou, Nikolaos and Coosemans, Thierry and Messagie, Maarten},
  journal = {World Electric Vehicle Journal},
  volume  = {12},
  number  = {4},
  pages   = {178},
  year    = {2021},
  doi     = {10.3390/wevj12040178}
}
```

## 🔗 Key References & Citation Graph
- [[2020_Ensemble_EV_Load]] — ensemble ANN/RNN/LSTM forecaster cited as prior hour-ahead EV demand work (ref. [26])
- [[2019_EV_Load_Forecasting]] — source of the LSTM-B baseline configuration (refs. [24], [25])
- [[2021_Hierarchical_Probabilistic_EV_Load]] — hierarchical probabilistic approach cited in literature review (+9.5% accuracy gain)
- [[1997_Long_Short_Term_Memory]] — vanishing-gradient problem context (ref. [28], Hochreiter 1998)
- [[2014_Kingma_Adam_Optimization]] — Adam optimizer used in LSTM-C/LSTM-W
