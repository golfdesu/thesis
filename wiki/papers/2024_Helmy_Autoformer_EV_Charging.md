---
type: paper
title: "On the Utilization of Autoformer-Based Deep Learning for Electric Vehicle Charging Load Forecasting"
authors: [Maram Helmy, Eiman ElGhanam, Mohamed S. Hassan, Ahmed Osman]
year: 2024
journal_conference: "2024 6th International Conference on Communications, Signal Processing, and their Applications (ICCSPA)"
doi_url: "https://doi.org/10.1109/ICCSPA61559.2024.10794251"
models_used: ["[[Autoformer]]", "[[LSTM]]"]
datasets_used: ["[[Boulder_Colorado]]"]
features_used: ["[[Charging_Demand]]", "[[Calendar_Features]]", "[[Calendar_Features]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MAPE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: On the Utilization of Autoformer-Based Deep Learning for EV Charging Load Forecasting

## 🎯 Main Objective & Contribution
- Open-source EV charging data is scarce/limited in volume and time span, degrading the reliability of statistical (ARIMA/SARIMA) and ML (XGBoost, RF, SVM) predictors; vanilla [[Transformer]] self-attention also struggles with complex temporal patterns and needs sparse point-wise attention for long sequences.
- Adopts **[[Autoformer]]** — decomposition Transformer with **Auto-Correlation** replacing self-attention — for **long-term EV charging load forecasting** at 30-, 60-, and 90-day horizons on an open Boulder, Colorado dataset.
- Result: 15% RMSE improvement over benchmark [[LSTM]] at 30 days and >50% improvement at 90 days (~60% RMSE/MAE reduction), confirming Autoformer's stability for long-term horizons.

## 🧠 Methodology & Model Architecture
Encoder–decoder Transformer with an inner series-decomposition layer and auto-correlation attention (input-I-predict-O formulation).

**Series decomposition** (**Eq. 1–3 – SeriesDecomp**), based on moving averages as a built-in layer rather than preprocessing:
$$X_s = X - X_t, \qquad X_t = \text{AvgPool}(\text{padding}(X)), \qquad \{X_s, X_t\} = \text{SeriesDecomp}(X)$$
where $X_s$/$X_t$ are seasonal/trend components. The encoder progressively strips trend via SeriesDecomp and discovers seasonal patterns; the decoder aggregates trend from intermediate hidden variables while stacking auto-correlation for seasonality, with encoder outputs fed as cross information.

**Auto-Correlation mechanism** (**Eq. 4 – Auto-correlation coefficient**) replaces point-wise self-attention with period-based dependencies and time-delay aggregation:
$$R_{XX}(\tau) = \lim_{L\to\infty}\frac{1}{L}\sum_{t=1}^{L} X_t X_{t-\tau}$$
Confidence $R(\tau)$ selects top-k period lengths $\tau_1,\dots,\tau_k$; a **Roll()** operation aligns similar sub-series across cycles and softmax-normalized confidences aggregate them.

**Training setup** (**Eq. 5 – Min-max normalization**): $x = \frac{x - x_{min}}{x_{max}-x_{min}}$; metrics RMSE/MAE/MAPE (**Eq. 6–8**). Hyperparameters: hidden dim 128, 100 epochs, 2 encoder layers, 1 decoder layer, input length 96, prediction lengths {30, 60, 90}, 8 attention heads, batch size 64. Benchmark: LSTM trained identically.

## 📊 Dataset & Input Features
- **[[Boulder_Colorado]]**: open-source City of Boulder (Colorado, U.S.) charger data from **51 public charging stations**, Jan 1 2018 – Nov 30 2023.
- Raw data: **148,136 individual EV charging events**; aggregated to daily charging demand across all stations → **2155 records** (kWh/h/day); missing/negative entries removed.
- Input variables: charging demand (numeric, kWh/h/day), weekday (categorical Mon–Sun), month (categorical Jan–Dec). Output: EV charging demand (kWh/h).
- Split: 70% train / 10% validation / 20% test; min-max normalized.
- Data availability URL given in ref [33]: https://open-data.bouldercolorado.gov/datasets/39288b03f8d54b39848a2df9f1c5fca2_0/explore

## 📈 Performance & Results
| Horizon | Metric | Autoformer | LSTM |
|---|---|---|---|
| 30-day | RMSE / MAE / MAPE | 0.202 kWh/h / 0.155 kWh/h / 35.7% | 0.239 / 0.160 / 37.6% |
| 60-day | RMSE / MAE / MAPE | 0.209 / 0.161 / 36.3% | 0.296 / 0.207 / 48.7% |
| 90-day | RMSE / MAE / MAPE | 0.210 / 0.161 / 35.0% | 0.540 / 0.424 / 75.4% |

- Autoformer accuracy is essentially flat across horizons (RMSE ≈ 0.21, MAE ≈ 0.16, MAPE ≈ 35%) whereas LSTM degrades sharply — 30-day: −15% RMSE, −3% MAE, −2 pp MAPE; 90-day: ~60% lower RMSE and MAE, roughly half the MAPE.

## 💡 Limitations & Identified Research Gaps
- Data aggregated **daily and across all 51 stations** — masks station-level and sub-daily fluctuations; no spatial dimension.
- Only one baseline ([[LSTM]]); no other Transformer variants or statistical baselines evaluated.
- High MAPE (~35%) even for Autoformer reflects difficulty of long-term EV demand prediction with limited features.
- Authors' future work: effect of hyperparameter tuning of Autoformer using different EV charging datasets to confirm reliability against more DL models.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{helmy2024autoformer,
  title     = {On the Utilization of Autoformer-Based Deep Learning for Electric Vehicle Charging Load Forecasting},
  author    = {Helmy, Maram and ElGhanam, Eiman and Hassan, Mohamed S. and Osman, Ahmed},
  booktitle = {2024 6th International Conference on Communications, Signal Processing, and their Applications (ICCSPA)},
  pages     = {1--6},
  year      = {2024},
  doi       = {10.1109/ICCSPA61559.2024.10794251}
}
```

## 🔗 Key References & Citation Graph
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — source architecture (decomposition + auto-correlation)
- [[2017_Attention_Is_All_You_Need]] — underlying Transformer attention mechanism
- [[2019_Zhu_EV_Load_Forecasting]] — cited comparative DL study for EV charging load (LSTM best among CNN/RNN/LSTM/GRU)
- [[2023_Koohfar_Transformer_EV_Demand]] — prior vanilla-Transformer EV demand forecasting that Autoformer improves upon
- [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]] — decomposition-based forecaster contrasted with Autoformer's inner decomposition
- [[1997_Hochreiter_Long_Short_Term_Memory]] — LSTM benchmark model
