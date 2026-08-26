---
type: paper
title: "Short term demand forecasting of electric vehicle charging stations using context aware temporal transformer model"
authors: [Adil Hussain, Qing-Chang Lu, Sanam Shahla Rizvi, Shixin Wang, Se Jin Kwon]
year: 2025
journal_conference: "Scientific Reports, Vol. 15, Article 36652"
doi_url: "https://doi.org/10.1038/s41598-025-20557-x"
models_used: ["[[CAT_Former|CAT-Former (Context-Aware Temporal Transformer)]]", "[[Transformer]]", "[[Multi_Head_Attention]]", "[[LSTM]]", "[[BiLSTM]]", "[[CNN-LSTM]]", "[[CNN-BiLSTM]]", "[[Hybrid_Transformer|Hybrid Transformer (LSTM Encoder-Decoder)]]"]
datasets_used: ["[[Boulder_City_EV_Charging_Dataset]]", "[[Boulder_Weather_Data]]"]
features_used: ["[[Temporal_Features]] $X_{temporal,t} = [h, dw, dt, dm, sd]$", "[[Contextual_Features]] $X_{context,t} = [C_{location}, C_{weather}]$", "[[Positional_Encoding]] $P_t$"]
forecasting_horizon: "[[Short_Term|1-Hour Ahead and 1-Day Ahead]]"
metrics: ["[[MSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Short Term Demand Forecasting of EV Charging Stations Using Context-Aware Temporal Transformer Model

## 🎯 Main Objective & Contribution
- Most existing EV charging demand forecasts target a single or city-aggregated charging station; charging behavior actually **differs across locations** within a city (time-of-day dependent trends).
- Proposes **[[CAT_Former]]**, a Context-Aware Temporal Transformer that fuses **Temporal features** (calendar/session-based) and **Contextual features** (station coordinates + weather) inside a multi-head self-attention encoder-decoder for **1-hour and 1-day ahead** demand forecasts at multiple stations simultaneously.
- Evaluated on public Boulder City, Colorado data at the three busiest sites (**Park 1 / Carpenter Park 1, Rec 1 / N Boulder Rec 1, Street 1 / Baseline St 1**), against [[LSTM]], [[BiLSTM]], [[CNN-LSTM]], [[CNN-BiLSTM]], simple Transformer, and a Hybrid Transformer with LSTM encoder-decoder.

## 🧠 Methodology & Model Architecture
### Feature Construction
(**Eq. 1 — temporal vector**): $X_{\text{temporal},t} = [h, dw, dt, dm, sd]$ — hour of day $h \in [0,24)$, day of week $dw \in \{0..6\}$ (0 = Monday), day type $dt \in \{0 \text{ weekday}, 1 \text{ weekend}\}$, day of month $dm \in [1,31]$, session duration $sd$
Session duration: (**Table 2**) $sd = \frac{End\_time(e_t) - Start\_time(s_t)}{3600}$
(**Eq. 2 — contextual vector**): $X_{\text{context},t} = [C_{\text{location}}, C_{\text{weather}}] = [S_{lat}, S_{long}, W_{temp}, W_{percip}, W_{wind}]$
(**Eq. 3 — combined input**): $Z_t = [X_{\text{temporal},t}, X_{\text{context},t}]$

### CAT-Former Transformer Core
(**Eq. 4 — positional encoding**): $P_t = \text{PositionalEncoding}(t)$
(**Eq. 5**): $Z'_t = Z_t + P_t$
(**Eqs. 6–8 — projections**): $Q = W^Q Z'_t$, $\quad K = W^K Z'_t$, $\quad V = W^V Z'_t$
(**Eq. 9 — attention score**): $\text{Attention}(Q,K) = \frac{QK^T}{\sqrt{d_k}}$
(**Eq. 10 — weighted output**): $Output_{t,t'} = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
(**Eq. 11 — multi-head**): $\text{MultiHead}(Q,K,V) = \text{Concat}(head_1, head_2, \dots, head_h)\,W^O$
(**Eq. 12 — encoder output**): $H_t = \text{FeedForward}(\text{MultiHead}(Q,K,V))$
(**Eq. 13 — decoder cross-attention**): $D_t = \text{MultiHead}(Q_{\text{decoder}}, K_{\text{encoder}}, V_{\text{encoder}})$
(**Eq. 14 — prediction**): $\hat{d}_t = \text{Linear}(D_t)$
Training optimized by MSE loss (**Eq. 15**: $\text{MSE} = \frac{1}{n}\sum_{i=1}^n (y_i - \hat{y}_i)^2$; **Eq. 16**: $\text{MAE} = \frac{1}{n}\sum_{i=1}^n |y_i - \hat{y}_i|$).

### Implementation Details
- Preprocessing: MinMaxScaler normalization; weekdays encoded 0–6.
- Training: Adam optimizer, learning rate **0.001**, **100 epochs**, batch size **32**, ReLU/Tanh activations, dropout **0.3** (grid over epochs {20,50,100}, batch {32,64}, LR {0.01, 0.001, 0.0001}).
- Baselines: 3-layer LSTM (100→50→25 units + Dense 64→1); 3-layer BiLSTM (128/128/64); CNN-LSTM (Conv1D 64+128 → LSTM 50/30); CNN-BiLSTM (Conv1D 64/128 → BiLSTM 50/30); simple Transformer (MultiHeadAttention + GlobalAveragePooling1D); Hybrid Transformer (LSTM encoder-decoder + multi-head attention).

## 📊 Dataset & Input Features
- **[[Boulder_City_EV_Charging_Dataset]]**: public dataset of **26 EV charging stations in Boulder City, Colorado**, spanning **January 2018 – November 2023**; one row per charging session (Station Name, Address, City, State/Province, Start/End Date Time, Total Duration, Charging Time, Energy kWh, GHG Savings kg, Gasoline Savings gallons, Port Type, ObjectID).
  - **Data availability (verbatim)**: "The datasets generated and/or analyzed during the current study are available in the Electric Vehicle Charging Station Data repository, https://opendata.bouldercolorado.gov/datasets/95992b3938be4622b07f0b05eba95d4c_0/explore."
  - Split: train **Jan 2018 – Jun 2023**, test **Jul – Nov 2023** (fixed date split, seasonality not preserved).
- Three top sites by session count: Carpenter **Park 1**, N Boulder **Rec 1**, Baseline **Street 1**.
- **[[Boulder_Weather_Data]]**: hourly temperature, wind speed, precipitation (no missing values), synchronized to hourly charging sessions via datetime.
- Temporal analysis: summer peaks (May–Oct), weekday > weekend demand, peak hours 7 AM–6 PM (sessions peak 1–2 PM; energy peaks 2–3 PM).
- Open Access CC BY-NC-ND 4.0; funding acknowledged from NRF Korea RS-2023-00244091 and MOTIE RS-2024-00507228 (though Funding section states no external funding for the research itself).

## 📈 Performance & Results
### 1-Hour Ahead (hourly sessions data)
| Location | Best baseline | CAT-Former | Reduction |
| :--- | :--- | :--- | :--- |
| Park 1 | Hybrid Transformer MSE 0.5155 | **MSE 0.4610, MAE 0.6789** | −11.82% MSE, −5.75% MAE |
| Rec 1 | Hybrid Transformer MSE 1.3381* | **MSE 1.1885, MAE 1.0901** | −11.18% MSE vs Transformer |
| Street 1 | Hybrid Transformer MSE 1.5425 | **MSE 1.4113, MAE 1.1880** | −8.50% MSE |

vs best-performing baseline (Hybrid Transformer): Rec 1 −6.23% MSE / −12.87% MAE; Street 1 −4.54% MSE / −9.28% MAE. Weakest baselines: Park 1 LSTM MSE 1.5286/MAE 1.2364; Rec 1 LSTM MSE 2.7324; Street 1 LSTM MSE 3.4000/MAE 1.8439.

### 1-Day Ahead (daily aggregated data)
- **Park 1**: CAT-Former **MSE 0.83557, MAE 0.9141** vs Hybrid Transformer 0.96177 and LSTM 2.7725/1.6651 → −13.12% vs hybrid; reported −7.22% MSE / −15.08% MAE vs best baseline.
- **Rec 1**: CAT-Former MSE 0.51552, MAE 0.718 — **Hybrid Transformer wins here** (MSE 0.4844, MAE 0.6959); CAT-Former 3.30% MSE / 6.40% MAE *higher* than best baseline.
- **Street 1**: CAT-Former **MSE 0.5069** vs Hybrid Transformer 0.5520 and LSTM 1.1223 → −8.17%; reported −4.23% MSE / −9.09% MAE vs best baseline.

### Point-prediction spot check (31 Oct., last 30 days input)
Park 1 actual 58.294 kWh → CAT-Former 59.208 (closest among most models); Rec 1 actual 47.814 → CAT 47.196; Street 1 actual 42.739 → CAT 43.451 (Tables 6–7).

- Overall: CAT-Former beats all individual/hybrid baselines in **most** settings and clearly beats the simple Transformer; it is only competitive (not always superior) vs the Hybrid Transformer (loses on Rec 1 daily task).

## 💡 Limitations & Identified Research Gaps
- Only 3 stations of one mid-size US city; authors note future work should add other cities and external factors like road traffic/networks.
- No probabilistic outputs; deterministic point forecast only (MSE loss).
- Daily aggregation discards hourly structure for the 1-day task; seasonality deliberately not preserved in the split.
- Electricity prices and traffic volumes excluded (deemed low impact for short-term); unverified for other regions.
- Loses to the LSTM-based Hybrid Transformer on the Rec 1 1-day-ahead case — context-aware attention does not universally dominate.
- Thesis gap: explicit lat/long + weather injection into vanilla Transformer attention is a strong, simple spatial-context baseline for cross-station short-term forecasting.

## 📚 BibTeX & Citation Reference
```bibtex
@article{hussain2025catformer,
  title   = {Short term demand forecasting of electric vehicle charging stations using context aware temporal transformer model},
  author  = {Hussain, Adil and Lu, Qing-Chang and Rizvi, Sanam Shahla and Wang, Shixin and Kwon, Se Jin},
  journal = {Scientific Reports},
  volume  = {15},
  pages   = {36652},
  year    = {2025},
  doi     = {10.1038/s41598-025-20557-x}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — source of the multi-head self-attention encoder-decoder backbone (Eqs. 9–13).
- [[1997_Long_Short_Term_Memory]] — LSTM/BiLSTM baselines used for comparison.
- Koohfar, Woldemariam & Kumar (2023), *Prediction of electric vehicles' charging demand: A Transformer-based deep learning approach* (Sustainability 15(3):2105) — direct predecessor using Boulder data but daily aggregation only; see [[2023_Prediction_of_Electric_Vehicles_Charging_Demand_A_Transformer_Based_Deep_Learning_Approach]], ref [28].
- Zhu et al. (2019), *Short-Term Load Forecasting for Electric Vehicle Charging Stations Based on Deep Learning Approaches* (Appl. Sci.) — see [[2019_Short_Term_Load_Forecasting_for_Electric_Vehicle_Charging_Stations_Based_on_Deep_Learning_Approaches]], ref [24].
- Zhang et al. (2022), *Hybrid STLF based on empirical wavelet transform and BiLSTM*, doi:10.35833/MPCE.2021.000276, ref [35]; Zhang et al. (2024), *Privacy-preserving federated learning for AMI*, IEEE TCSS, ref [36].
