---
type: paper
title: "Attention-Enhanced CNN-LSTM Models for Forecasting EV Fast-Charging Load at Public Stations"
authors: [Asmaa Romia, Qiuhua Huang]
year: 2026
journal_conference: "IEEE Transactions on Industry Applications"
doi_url: "https://doi.org/10.1109/TIA.2026.3677828"
models_used: ["[[CNN_LSTM_Attention]]", "[[CNN_LSTM_Transformer]]", "[[GRU]]", "[[RNN]]", "[[Transformer]]", "[[LSTM_Transformer]]", "[[SARIMA]]", "[[SVR]]", "[[Optuna_TPE]]"]
datasets_used: ["[[Caltech_ACN]]", "[[Weather]]"]
features_used: ["[[Historical_Load]]", "[[Temperature]]", "[[Humidity]]", "[[Calendar_Features]]", "[[Calendar_Features]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[R_squared]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Attention-Enhanced CNN-LSTM Models for Forecasting EV Fast-Charging Load at Public Stations

## 🎯 Main Objective & Contribution
- DC fast-charging (DCFC) station loads are far more volatile than AC Level-2 loads; prior work targets single-step forecasts, coarse resolutions, aggregated regional loads, and ignores exogenous drivers (weather, day-type). Statistical models ([[SARIMA]]) miss nonlinearity; ML methods ([[SVR]], LR, XGBoost/CatBoost) treat time steps independently; plain DL ([[LSTM]], [[GRU]], CNN) struggles with long-range dependencies at station level.
- Proposes two complementary application-driven hybrids (novelty is the tailored hybrid design, not attention itself): **[[CNN_LSTM_Attention]]** for single-step (1-h ahead) forecasting via single-head attention over LSTM hidden states, and **[[CNN_LSTM_Transformer]]** for multi-step (24-h, 48-h ahead) forecasting via multi-head self-attention + positional encodings over stacked Transformer layers. Includes an [[Optuna_TPE]] TPE-based hyperparameter optimization framework per horizon; extends the authors' earlier IAS 2024 conference paper [1].

## 🧠 Methodology & Model Architecture
- Pipeline: multivariate inputs → 1-D CNN layers (kernel size 3, ReLU, max pooling size=2) for local temporal–feature extraction → stacked LSTM layers for sequential dependencies → attention/Transformer head → dense output.
- **Basic attention scores**:
$$ \text{score}(Q,K) = Q^\top K \tag{1} $$
$$ \alpha_m = \frac{\exp(e_m)}{\sum_{k=1}^{n}\exp(e_k)}, \quad e_m = Q^\top K_m \tag{2} $$
$$ \text{Attention}(Q,K,V) = \sum_{m=1}^{n} \alpha_m h_m \tag{3} $$
where $h_m$ are LSTM hidden states (single-head attention).
- **Multi-head self-attention**:
$$ \text{MHA}(Q,K,V) = \text{Concat}(\text{head}_1,\dots,\text{head}_h)W^O \tag{4} $$
- **Transformer layer** (residual connections + layer norm):
$$ \hat{H} = \text{Norm}(H + \text{MHA}(Q,K,V)) \tag{5} $$
$$ H' = \text{Norm}(\hat{H} + \text{MLP}(\hat{H})) \tag{6} $$
- **Composite model maps**: 
$$ \bar{y}(t+\Delta) = f_{\text{Dense}}(f_{\text{Attention}}(f_{\text{LSTM}}(f_{\text{CNN}}(x)))) \tag{7} $$ 
(single-step) and 
$$ \bar{y}(t+\Delta) = f_{\text{Dense}}(f_{\text{Transformer}}(f_{\text{LSTM}}(f_{\text{CNN}}(x)))) \tag{8} $$ 
(multi-step).
- **Hyperparameter optimization** ([[Optuna_TPE]], Tree-Structured Parzen Estimator), minimizing MSE:
$$ \lambda^* = \arg\min_{\lambda\in\Lambda} f(\lambda) \tag{9} $$
Search spaces: hidden size H∈[64,256], LSTM layers [1,3], dropout [0.1,0.5], lr [1e−5,1e−2]; Transformer nhead∈[2,8], $d_{ff}$∈[2H,8H]. Best configs: Attention 1h (H=64, drop=0.4, η=0.001); 24h (H=128, 0.35, 0.0008); 48h (H=256, 0.3, 0.0005). Transformer: 1h (nhead=4, H=128, $d_{ff}$=512, 0.3, 0.001); 24/48h (nhead=6, H=256, $d_{ff}$=2048, 0.25, 0.0003).
- Training: Adam, MSE loss, 50 epochs; look-back window 48 h (single-step) / 196 h (multi-step); input 5 features; outputs of size 1, 24, or 48.

## 📊 Dataset & Input Features
- **[[Caltech_ACN]]** — real-world public EV fast-charging station in Pasadena, CA, USA [52]: **16,155 hourly samples** of charging demand (kWh), 26 April 2018 – 28 February 2020; mean 15.15 kWh/h, max 133.82 kWh, std 18.04 kWh. Source citation: Lee, Li & Low, "ACN-Data: Analysis and Applications of an Open EV Charging Dataset," ACM e-Energy '19 (dataset portal: https://ev.caltech.edu/dataset).
- Weather from NREL System Advisor Model database [53]: temperature and humidity (https://sam.nrel.gov, accessed 26 July 2023). Demand concentrates at moderate temperatures (~10–20 °C) and high humidity (60–90%).
- Engineered features: day-type indicator (weekday/weekend), season categorical; evening peak 17:00–21:00 with maximum at 18:00; weekday demand higher than weekend across temperatures.
- Split: strict chronological 75% train / 10% validation / 15% test, no shuffling; sliding windows built within subsets to prevent temporal leakage.

## 📈 Performance & Results
- **Single-step (1-h)** vs best baseline GRU: [[CNN_LSTM_Attention]] MAE 2.98, RMSE 4.61, R² 0.89 → **17.45% MAE reduction, 13.83% RMSE reduction, +3.49% R²**; also fastest training (144.63 s vs GRU 225.79 s) and lowest inference latency (0.742 ms/sample vs GRU 2.319 ms). CNN-LSTM-Transformer: MAE 3.17 (−12.18%), RMSE 4.71 (−11.96%), R² 0.88 (+2.33%). Other baselines: RNN 4.02/6.22/0.80, LSTM-Transformer 4.72/5.74/0.83, Transformer 5.15/7.07/0.75.
- **24-h horizon**: CNN-LSTM-Transformer best — MAE 5.17, RMSE 7.68, R² 0.70 (**−5.48% MAE, −4.0% RMSE, +2.94% R² vs GRU**); CNN-LSTM-Attention 5.35/7.78/0.69; Transformer collapses to 7.77/11.05/0.39.
- **48-h horizon**: CNN-LSTM-Transformer best — MAE 5.60, RMSE 8.16, R² 0.66 (**−7.59% MAE, −4.45% RMSE, +4.76% R² vs RNN**, the strongest traditional baseline here); CNN-LSTM-Attention degrades (5.61/8.34/0.65) due to error accumulation over long horizons.
- SARIMA produced smoothed trajectories missing sharp peaks; SVR/LR lagged behind all DL hybrids. Lowest cumulative squared error throughout fall/winter test weeks for CNN-LSTM-Attention.

## 💡 Limitations & Identified Research Gaps
- Both models underestimate rare, abrupt high-magnitude charging spikes (irregular events underrepresented in training data).
- Single-station evaluation only; no cross-network generalization tested. Future work: transfer learning / low-rank adaptation (LoRA-style) to multiple fast-charging networks, online/continuous learning for evolving behavior.
- Maintaining two separate models per horizon adds deployment cost; a mixture-of-experts unification proposed as future direction.
- No probabilistic/uncertainty outputs; integration with grid-aware optimization (storage scheduling, smart charging, market participation) left future; interpretability (e.g., SHAP) noted as open area.

## 📚 BibTeX & Citation Reference
```bibtex
@article{romia2026attention,
  author  = {Romia, Asmaa and Huang, Qiuhua},
  title   = {Attention-Enhanced {CNN-LSTM} Models for Forecasting {EV} Fast-Charging Load at Public Stations},
  journal = {IEEE Transactions on Industry Applications},
  year    = {2026},
  doi     = {10.1109/TIA.2026.3677828}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] (Vaswani et al., NeurIPS 2017) [32] — attention/MHA foundations
- Authors' prior work: Romia & Huang, IEEE IAS Annual Meeting 2024 (hybrid CNN-LSTM-Attention for EV fast charging) [1]
- [[Informer]] (Zhou et al., AAAI 2021) [49]; Autoformer (Wu et al., NeurIPS 2021) [48]; Temporal Fusion Transformer (Lim et al., IJCAI 2021) [50] — hyperparameter range justifications
- [[LSTM]] (Hochreiter & Schmidhuber, 1997) [31]; LSTM search-space odyssey (Greff et al.) [44]
- [[Optuna_TPE]] TPE framework (Akiba et al., KDD 2019) [39] — https://optuna.org, https://github.com/optuna/optuna
- Bayesian LSTM EV load forecasting (Zhou et al., Energies 2022) [16]; MetaProbformer probabilistic forecasting (Huang et al., IEEE T-ITS 2023) [18]; ConvLSTM/BiConvLSTM networks (Mohammad et al., IEEE Access 2023) [17]
- [[Caltech_ACN]] (Lee, Li & Low, ACM e-Energy 2019) [52]; NREL SAM weather data [53] — https://sam.nrel.gov
