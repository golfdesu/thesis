---
type: paper
title: "Energy Consumption Prediction Strategy for Electric Vehicle Based on LSTM-Transformer Framework"
authors: [Zhanyu Feng, Jian Zhang, Han Jiang, Xuejian Yao, Yu Qian, Haiyan Zhang]
year: 2024
journal_conference: "SSRN Preprint 4747046 (not peer reviewed)"
doi_url: "https://ssrn.com/abstract=4747046"
models_used: ["[[LSTM_Transformer]]", "[[LSTM]]", "[[Transformer]]", "[[KMeans_Clustering]]", "[[Linear_Regression]]"]
datasets_used: ["[[GBT_32960_Telemetry_Dataset]]"]
features_used: ["[[Battery_SOC]]", "[[Vehicle_Speed_Features]]", "[[Acceleration_Ratios]]", "[[Wind_Speed]]", "[[Temperature]]", "[[Visibility]]", "[[Driver_Style]]", "[[Driving_Condition_Clusters]]", "[[Cruise_Time_Ratio]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAPE]]", "[[MAE]]", "[[RMSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Energy Consumption Prediction Strategy for Electric Vehicle Based on LSTM-Transformer Framework

## 🎯 Main Objective & Contribution
- Mitigate driver **range anxiety** via accurate real-time EV battery [[Battery_SOC]] / energy consumption prediction, integrating vehicle, environmental, **driver style**, and **driving condition** factors.
- Contributions:
  1. **[[LSTM_Transformer]] hybrid framework** — LSTM layer extracts short-term temporal dependencies; Transformer encoder layers capture long-range dependencies; linear output head.
  2. Comprehensive energy-consumption factor framework (18 features) with special emphasis on individual driving styles and driving-condition recognition via [[KMeans_Clustering]].
  3. Novel **long-distance prediction strategy built from short-distance segment forecasts** (cumulative SOC roll-out), achieving MAPE = 6.7% for a 90→40% SOC discharge.

## 🧠 Methodology & Model Architecture
### Factor framework (Eqs. 1–2)
Vehicle factors (**Eq. 1**): $V = (x_1, x_2, x_3 \cdots x_{15})$ — average speed, speed range/std-dev, mean squared speed, average acceleration, accumulated/segment mileage, acceleration/deceleration/constant-speed segment ratios, low-/medium-/high-speed ratios, accel-decel switching frequency, cruise time ratio. Environmental factors (**Eq. 2**): $T = (x_{16}, x_{17}, x_{18})$ — average wind speed (m/s), sensible temperature (°C), visibility (m). Driver factor handled by training per-driver models on each single vehicle's data (no cluster averaging).

### K-means driving-condition recognition (Eq. 3)
$$E = \sum_{i=1}^{k} \sum_{x \in c_i} \|x - \bar{x}_i\|^2$$
with $k = 3$ (aligned to CLTC cycle classes), features = {average speed, cruise time ratio, max acceleration}; Euclidean distance; clusters map to urban (low speed/ratio), suburban (medium), high-speed (high).

### Positional encoding (Eqs. 4–5)
$$PE(t, 2i) = \sin(t/10000^{2i/d_{model}})$$
$$PE(t, 2i+1) = \cos(t/10000^{2i/d_{model}})$$

### LSTM gates (Eqs. 6–11)
$$f_t = \sigma(W_f \cdot [h_{t-1}, X_t] + b_f)$$
$$i_t = \sigma(W_i \cdot [h_{t-1}, X_t] + b_i)$$
$$\tilde{C}_t = \tanh(W_c[h_{t-1}, X_t] + b_c)$$
$$C_t = C_{t-1} \cdot f_t + i_t \cdot \tilde{C}_t$$
$$O_t = \sigma(W_o \cdot [h_{t-1}, X_t] + b_i)$$
$$h_t = O_t \cdot \tanh(C_t) = O_t \cdot \tanh(C_{t-1} \cdot f_t + i_t \cdot \tanh(W_c \cdot [h_{t-1}, X_t] + b_c))$$

### Attention & multi-head self-attention (Eqs. 12–20)
Attention distribution (**Eq. 12**): $\alpha_i = \text{softmax}(h(x_i, p))$, with scoring options (**Eqs. 13–14**): $s(x_i,p) = x_i^T W p$ or $s(x_i,p) = x_i^T p$; weighted representation (**Eq. 15**): $Z = att(X,p) = \sum_{i}^{n} \alpha_i x_i$. Projections (**Eqs. 16–18**): $\mathcal{Q} = Linear(X) = XW^Q$, $K = Linear(X) = XW^K$, $V = Linear(X) = XW^V$; scaled dot-product head (**Eq. 19**):
$$head = attention(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
Multi-head (**Eq. 20**): $multihead = concat(head_1,\ldots,head_h)W$

### Pipeline (5 steps)
Collect operational data → high-dim input mapping → [[LSTM]] layer (short-term dependencies, order preservation) → Transformer encoder stack (global long-range dependencies) → fully-connected linear output. Training: ADAM optimizer, lr=0.001, dropout=0.1, 100 iterations, MAE loss; hyperparameters tuned manually/grid search; 7:3 train/test split.

### Ah-integration SOC reconstruction (Eqs. 21–23)
GB/T 32960 reports integer-precision SOC only, so continuous SOC is reconstructed from battery current integration:
$$SOC_{t+1} = SOC_t + \frac{\sum_{t}^{t+1} I dt}{C} \quad (21), \qquad C = \sum_{t=0}^{t=MAX} I dt \quad (22), \qquad \Delta SOC = SOC_{t+1} - SOC_t \quad (23)$$

### Long-distance strategy (Eq. 27)
$$SOC_{Remaining}^{t+1} = SOC_{Remaining}^{t} - SOC_{Prediction}^{t+1}$$
Cumulative stage-wise roll-up of 400-s segment predictions over the trip.

## 📊 Dataset & Input Features
- **[[GBT_32960_Telemetry_Dataset]]**: one year of real-world operational data (from April 2022 onward in raw samples) from **10 vehicles/drivers** (5 Type A + 5 Type B vehicles), collected by on-board data acquisition devices transmitted per the Chinese national standard **GB/T 32960** (EV Remote Service and Management System), sampling frequency **0.05 Hz** (~20 s). No public URL — private fleet telemetry.
- Hourly weather data from https://www.visualcrossing.com (Visual Crossing), time-aligned with vehicle data. Paper preprint: https://ssrn.com/abstract=4747046 .
- Driving segments aggregated at 200/400/600/1000 s windows with outlier-filtering data-cleaning rules; charging vs driving status separation; SOC label reconstructed via Ah integration.
- Features: 15 vehicle factors ($x_1$–$x_{15}$), 3 environmental factors ($x_{16}$–$x_{18}$), plus per-driver model specialization and k-means driving-condition labels.

## 📈 Performance & Results
- **400-s window test set (10 drivers)**: [[LSTM_Transformer]] avg **MAPE = 4.63%**, MAE ≈ 0.027, RMSE ≈ 0.036; standalone [[LSTM]] MAPE = 10.69% (+6.06%); [[Linear_Regression]] MAPE = 21.87%. Per-driver best/worst: B3 MAPE 3.0%, A5 5.9%.
- **Window sensitivity**: MAPE = 13.9% (200 s), **4.6–4.63% (400 s, best)**, ~5.1% (600 s), 8.3% (1000 s) — too-short windows lose motion context at 0.05 Hz sampling; too-long windows dilute fine-grained detail.
- **Ablation**: removing driver-style personalization raised MAPE by up to **18.47%**; removing driving-condition features raised it by **15.27%**; ignoring both increased MAPE by 12.4%/17.0%/16.5%/14.0% at 200/400/600/1000 s.
- **Long-distance (250 km-class trip, SOC 90→40%)**: cumulative strategy achieves avg **MAPE = 6.7%** across drivers (best B3 5.1%, worst A5 7.7%).

## 💡 Limitations & Identified Research Gaps
- Small, single-region dataset (10 vehicles, China); authors explicitly call for validation on broader datasets under diverse geographic/climatic conditions.
- Battery state-of-health ([[SOH]]) not modeled — future work for extended-range prediction.
- Feature engineering limited to powertrain subsystems; other vehicle subsystem data unexploited.
- Long-distance accuracy depends on data quality; error accumulation possible during stage-wise SOC roll-forward.
- Preprint, not peer-reviewed; no public code/data release.

## 📚 BibTeX & Citation Reference
```bibtex
@article{feng2024lstmtransformer,
  title   = {Energy Consumption Prediction Strategy for Electric Vehicle Based on LSTM-Transformer Framework},
  author  = {Feng, Zhanyu and Zhang, Jian and Jiang, Han and Yao, Xuejian and Qian, Yu and Zhang, Haiyan},
  journal = {SSRN Electronic Journal (preprint 4747046)},
  year    = {2024},
  doi     = {10.2139/ssrn.4747046}
}
```

## 🔗 Key References & Citation Graph
- Related vault concepts: [[2017_Attention_Is_All_You_Need]] — self-attention/positional encoding basis of the Transformer stage ([44]).
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM gating foundation ([62], [66]).
- [[2024_Bampos_EV_Load_Forecasting_DAM]] — complementary EV load (vs energy consumption) forecasting benchmark.
- Vault concepts: [[LSTM_Transformer]], [[Battery_SOC]], [[Range_Anxiety]], [[Driving_Cycle]], [[KMeans_Clustering]]
