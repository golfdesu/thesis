---
type: paper
title: "Short-Term Load Forecasting for Electric Vehicle Charging Stations Based on Deep Learning Approaches"
authors: [Juncheng Zhu, Zhile Yang, Yuanjun Guo, Jiankang Zhang, Huikun Yang]
year: 2019
journal_conference: "Applied Sciences 2019, 9(9), 1723 (MDPI)"
doi_url: "https://doi.org/10.3390/app9091723"
models_used: ["[[DNN]]", "[[RNN]]", "[[LSTM]]", "[[GRU]]"]
datasets_used: ["[[Liuyue_Charging_Station_Dataset]]"]
features_used: ["[[Historical_Load]]", "[[Charging_Time]]", "[[Electricity_Tariff|Real-Time Electricity Price (TOU)]]", "[[Holiday_Flag|One-Hot Encoded Holiday Marks]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[NRMSE]]", "[[NMAE]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Short-Term Load Forecasting for Electric Vehicle Charging Stations Based on Deep Learning Approaches

## 🎯 Main Objective & Contribution
- Applies and compares four deep learning models — [[DNN]], [[RNN]], [[LSTM]], [[GRU]] — for **hourly-based short-term (1 hour to 1 day/week ahead) EV charging station load forecasting** on real-world Shenzhen charging station data.
- Incorporates multi-dimensional contextual inputs beyond historical load: charging time sequence, real-time peak/valley electricity price, one-hot encoded holiday marks.
- Key finding: the **single-hidden-layer [[GRU]] achieves the best accuracy** (Test-NRMSE 2.89%, Test-NMAE 0.77%) with fewer parameters than LSTM; adding hidden layers degrades accuracy and training speed.
- Companion minute-level study: [[2019_Zhu_EV_Load_Forecasting]].

## 🧠 Methodology & Model Architecture
- **Vanilla RNN** (Eqs. 1–4):
$$S_t = \phi(U x_t + W S_{t-1} + b_1),\qquad o_t = \phi(V S_t + b_2),\qquad \hat{y}_t = \phi(o_t),\qquad \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$
- **[[LSTM]] gates** (input $\Gamma_i$, forget $\Gamma_f$, output $\Gamma_o$; Eqs. 5–11):
$$\Gamma_f = \sigma(\omega_f[o_{t-1}, x_t] + b_f) \tag{Forget gate}$$
$$\Gamma_i = \sigma(\omega_i[o_{t-1}, x_t] + b_i) \tag{Input gate}$$
$$\Gamma_o = \sigma(\omega_o[o_{t-1}, x_t] + b_o) \tag{Output gate}$$
$$e_{S_t} = \tanh(\omega_s[o_{t-1}, x_t] + b_s) \tag{Candidate state}$$
$$S_t = \Gamma_i * e_{S_t} + \Gamma_f * S_{t-1} \tag{Cell state update}$$
$$o_t = \Gamma_o * \tanh(S_t),\qquad \sigma(x) = \frac{1}{1+e^{-x}} \tag{Output & sigmoid}$$
- **[[GRU]] equations** (Cho et al.; merges LSTM input/forget gates into an update gate; output gate becomes reset gate; Eqs. 12–16):
$$\Gamma_{r-1} = \sigma(W_{r-1}[S_{t-1}, x_t] + b_{r-1}) \tag{Reset gate}$$
$$\Gamma_{u-1} = \sigma(W_{u-1}[S_{t-1}, x_t] + b_{u-1}) \tag{Update gate}$$
$$e_{S_t} = \tanh(W_s[\Gamma_{r-1} * S_{t-1}, x_t] + b_s) \tag{Candidate state}$$
$$S_t = (1 - \Gamma_{u-1}) * S_{t-1} + \Gamma_{u-1} * e_{S_t} \tag{Hidden state update}$$
$$\hat{y}_t = \sigma(W_o S_t) \tag{Forecast output}$$
Fewer parameters → faster training than LSTM.
- **Input feature vector** (Eq. 20): 4-dimensional input after min-max normalization of $C, T, E$ and one-hot encoding of $H$:
$$\vec{X}_t = [\vec{C}_t,\ \vec{T}_t,\ \vec{E}_t,\ \vec{H}_t]$$
Data read as `(samples, time steps, features)`; label is load at time $t$, input at $t-1$.
- **Outlier processing** (Eqs. 17–18): threshold test then mean-of-neighbors repair:
$$\max\left[\left|\frac{y_{dt}-y_{dt-1}}{y_{dt}}\right|,\left|\frac{y_{dt}-y_{dt+1}}{y_{dt}}\right|\right] \leq \epsilon_a \quad\Rightarrow\quad y_{dt} = \frac{y_{dt-1}+y_{dt+1}}{2}$$
Values exceeding the threshold are replaced by the previous same-type value; null columns are deleted or filled with 0.
- **Min-max normalization** to [0,1]:
$$y = \frac{x - x_{\min}}{x_{\max} - x_{\min}} \tag{19}$$
- **Loss function ([[MSE]])**:
$$\text{MSE} = \frac{1}{N}\sum_{i=1}^{n}(\hat{y} - x)^2 \tag{21}$$
Optimizer comparison of [[Adam]], SGD, Adagrad, Adadelta, RMSProp → Adam selected.
- **Normalized metrics** (Eqs. 22–23; MAPE excluded because station load is 0 when posts unused → zero denominator):
$$\text{NRMSE} = \frac{\sqrt{\frac{1}{N}\sum_{i=1}^{n}(\hat{y}-x)^2}}{x_{\max}-x_{\min}},\qquad \text{NMAE} = \frac{\frac{1}{N}\sum_{i=1}^{n}|\hat{y}-x|}{x_{\max}-x_{\min}}$$
- Implementation: Keras + TensorFlow backend, i7-3.0 GHz desktop, 64 GB RAM, GTX-1080Ti GPU; train/test split 0.7/0.3.

## 📊 Dataset & Input Features
- **[[Liuyue_Charging_Station_Dataset]]**: charging load of the Liuyue charging station (many charging piles, random pile selection by arriving vehicles), provided via the big-data platform of a Shenzhen charging company (co-author Huikun Yang, Winline Technology Co., Ltd., huikunyang@szwinline.com). Period: **April 2017 – June 2018** (~15 months).
- Three valuable data types in raw data: **charging time, charging quantity, real-time electricity price**; raw data quality low → heavy pre-processing.
- **Time interval processing**: pandas aggregates all piles per time point into 24 hourly points/day → **10,944 rows total** (hourly resolution).
- **Features**: $\vec{C}_t$ hourly charging-load sequence; $\vec{T}_t$ hourly charging-time sequence; $\vec{E}_t$ TOU electricity price — valley 23:00–07:00 (load peaks as most EVs charge there), peak 09:00–12:00 / 14:00–17:00 / 19:00–21:00 (load minimum); $\vec{H}_t$ holiday marks — weekday = 1, weekend = 2, special holiday = 3 (one-hot encoded).
- **Data availability**: no public repository or URL stated; only tool/library link is TensorFlow (USENIX OSDI'16 reference). Paper open access CC BY: http://creativecommons.org/licenses/by/4.0/

## 📈 Performance & Results
- **Table 1 — hidden-layer depth sweep**:

| Model | Hidden Layers | Train-NRMSE (%) | Test-NRMSE (%) | Train-NMAE (%) | Test-NMAE (%) |
| :--- | :---: | :---: | :---: | :---: | :---: |
| DNN | 2/3/4 | 2.05 / 1.97 / 1.98 | 3.69 / 3.79 / 3.81 | 1.06 / 0.50 / 0.46 | 1.32 / 0.94 / 0.92 |
| RNN | 1/2/3 | 1.50 / 1.52 / 1.61 | 2.91 / 2.91 / 2.96 | 0.62 / 0.70 / 0.84 | 0.91 / 1.01 / 1.19 |
| LSTM | 1/2/3 | 1.71 / 1.71 / 1.74 | 3.36 / 3.36 / 3.39 | 0.59 / 0.79 / 0.68 | 0.90 / 1.11 / 1.01 |
| **GRU** | **1** | **1.48** | **2.89** | **0.47** | **0.77** |
| GRU | 2/3 | 1.56 / 1.52 | 2.92 / 2.91 | 0.48 / 0.51 | 0.78 / 0.84 |

- Best model overall: **1-hidden-layer GRU** (Train-NRMSE 1.48%, Test-NRMSE 2.89%, Train-NMAE 0.47%, Test-NMAE 0.77%).
- **Depth counter-intuition**: multi-hidden-layer models performed worst — more layers without tuning other parameters lowered both training speed and accuracy (over-fitting); DNN trained fastest at 68.88 s but least accurate.
- Peak loads (17:00 training stage, 11:00 test stage) have largest real error points (REP) for all models; GRU keeps lowest REP at peaks.
- Seasonal behavior: summer charging overall high; winter shows no-charging periods, directly degrading model performance.

## 💡 Limitations & Identified Research Gaps
- Only a single charging station's limited data used; number of covered EVs is a small fraction of actual vehicle population → results cannot prove absolute superiority of any model.
- Point forecasts only (no probabilistic output); no weather/spatial covariates; peak-hour errors remain large for all four models.
- Authors' future work: incorporate more influencing factors and larger datasets as EV adoption grows; improve both prediction speed and accuracy; new models needed.
- Thesis relevance: validates [[GRU]] > [[LSTM]] at hourly resolution and the importance of [[Electricity_Tariff|TOU price]] + holiday features for day-ahead EV forecasting.

## 📚 BibTeX & Citation Reference
```bibtex
@article{zhu2019shortterm,
  title={Short-Term Load Forecasting for Electric Vehicle Charging Stations Based on Deep Learning Approaches},
  author={Zhu, Juncheng and Yang, Zhile and Guo, Yuanjun and Zhang, Jiankang and Yang, Huikun},
  journal={Applied Sciences},
  volume={9},
  number={9},
  pages={1723},
  year={2019},
  publisher={MDPI},
  doi={10.3390/app9091723}
}
```

## 🔗 Key References & Citation Graph
- Companion minute-level study: [[2019_Zhu_EV_Load_Forecasting]] (Energies 12(14):2692)
- Foundation: [[1997_Hochreiter_Long_Short_Term_Memory|Hochreiter & Schmidhuber, LSTM (1997)]]
- Method sources cited: GRU (Cho et al., arXiv:1409.1259), [[2014_Adam_Adam_Stochastic_Optimization|Adam (Kingma & Ba, arXiv:1412.6980)]], Adagrad (Duchi et al., 2011), Adadelta (Zeiler, 2012), RMSProp (Tieleman & Hinton, 2012)
- Metric definitions from Willmott et al., J. Geophys. Res. Oceans (1985)
