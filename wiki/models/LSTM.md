---
type: model
name: Long Short-Term Memory (LSTM)
category: Deep Learning / Recurrent Neural Network
tags:
  - model
  - deep-learning
  - rnn
---

# 🧠 Long Short-Term Memory (LSTM)

## Overview
LSTM is a specialized Recurrent Neural Network (RNN) architecture capable of learning long-term dependencies through input, output, and forget gates. In EV load forecasting, it is widely used for processing time-series sequence data (e.g. 15-minute resolution power load).

## Typical Usage in EV Load Forecasting
- **Input**: [[Historical_Load]], [[Arrival_Departure_Time]], [[State_of_Charge]].
- **Forecasting Horizon**: [[Short_Term_Forecasting]], [[Day_Ahead_Forecasting]].
- **Strengths**: Captures temporal sequential patterns well; avoids vanishing gradient problems of standard RNNs.
- **Weaknesses**: Cannot capture spatial relationships between multiple stations directly; computationally heavier than tree models.

## Literature Usage
- [[1997_Hochreiter_Long_Short_Term_Memory]] — Original LSTM paper: constant error carousels overcome vanishing gradients, bridging time lags of 1000+ steps where BPTT/RTRL fail entirely.
- [[2018_Bai_Empirical_TCN_Sequence_Modeling]] — Empirical evaluation finding generic TCNs beat canonical LSTM across sequence benchmarks (Seq. MNIST 99.0 vs 87.2 accuracy; Copy Memory loss 3.5e-5 vs 0.0204).
- [[2019_Toubeau_Deep_Probabilistic_Scheduling_Power_Markets]] — Bidirectional LSTM (BLSTM) generates multivariate probabilistic day-ahead forecasts/scenarios; ranking BLSTM < unidirectional LSTM < MLP < RF/SVR < ARIMA, with copula scenarios adding ~€4–10k retailer profit.
- [[2019_Zhu_ApplSci_EV_Load_Forecasting]] — LSTM compared against DNN/RNN/GRU for hourly EV station load; best LSTM Test-NRMSE 3.36% vs GRU 2.89%.
- [[2019_Zhu_EV_Load_Forecasting]] — Minute-level comparative study: LSTM best of six models at all look-back steps, cutting error by over 30% vs counterparts (e.g. 1-step MAE 0.4782 vs BiLSTM 1.3096).
- [[2019_Wu_Graph_WaveNet_Spatial_Temporal_Modeling]] — Motivated by avoiding RNN-style iterative propagation: gated dilated causal TCNs replace the recurrent decoder entirely and beat FC-LSTM on METR-LA at every horizon (60-min MAE 3.53 vs 4.37) with no gradient-explosion issues; one-shot multi-step output also eliminates train/test inconsistency of seq2seq recurrence.
- [[2020_Huang_Ensemble_EV_Load]] — LSTM used as base learner in LR-weighted ensemble; ensemble RMSE 3.83 vs standalone LSTM 3.89.
- [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — DeepAR trains a global autoregressive multi-layer LSTM with flexible likelihoods; ~15% accuracy improvement over SoTA probabilistic baselines.
- [[2021_Lim_TFT_Temporal_Fusion_Transformers]] — TFT uses an LSTM sequence-to-sequence encoder-decoder for local processing inside its attention architecture; average 7% lower P50 loss than next-best model.
- [[2021_Rasul_TimeGrad_Diffusion_Forecasting]] — TimeGrad conditions a DDPM diffusion head on an LSTM hidden state for autoregressive multivariate probabilistic forecasting; new SOTA CRPSsum on Traffic/Wikipedia/Taxi.
- [[2021_Stankeviciute_Conformal_Time_Series_Forecasting]] — CF-RNN wraps direct multi-horizon LSTM forecasters with inductive conformal prediction; only method to hit target joint coverage on all real datasets (MIMIC-III 94.0%).
- [[2021_VanKriekinge_Day_Ahead_EV_Demand]] — LSTM-B/C/W variants forecast 15-min day-ahead EV charging demand for a small stochastic fleet; calendar/weather features cut MAE up to 28.8% (MAE < 1 kW).
- [[2023_Cheng_VMD_Prophet_LSTM]] — VMD-Prophet-LSTM hybrid assigns high-frequency IMFs reconstructed sequences to LSTM; MAE 109.22 kW vs standalone LSTM 119.67 kW (−8.73%).
- [[2023_Huang_MetaProbformer_EV_Load]] — LSTM serves as point-forecast baseline; ordering MetaProbformer < MetaTransformer < Informer < LSTM < Transformer < ARIMA on heterogeneous task.
- [[2023_Koohfar_Transformer_EV_Demand]] — LSTM comparable to Transformer only at K=7 days (RMSE 0.036 vs 0.055) but degrades sharply at 30/60/90-day horizons (0.522 vs 0.085 at K=90).
- [[2023_Ziyabari_Multi_Branch_ResTrans_Solar]] — LSTM used as temporal baseline for spatio-temporal solar irradiance forecasting; multi-branch ResTrans beats it by 57.14% RMSE on 12 sites.
- [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] — FEDM benchmarked against deep recurrent baselines (incl. DeepAR) for low-data probabilistic EV demand; FEDM qualified rate 99.22% vs DeepTCN 94.79%.
- [[2024_Das_TiDE_Long_Term_Forecasting]] — Synthetic LDS experiment shows linear TiDE analogue (MSE 0.510) far outperforms LSTM (1.455), motivating MLP-based encoders over recurrence.
- [[2024_Feng_LSTM_Transformer_EV_Consumption]] — Standalone LSTM reaches MAPE 10.69% for EV energy consumption vs 4.63% for the proposed LSTM-Transformer hybrid.
- [[2024_Helmy_Autoformer_EV_Charging]] — LSTM baseline degrades sharply at long horizons (90-day RMSE 0.540 kWh/h); Autoformer cuts RMSE ~15% at 30 days and >50% at 90 days.
- [[2024_Ke_Divide_Conquer_Transformer_EV]] — LSTM baseline for home EV charging-event prediction from smart-meter data (F1@.5 83.91%) beaten by DCT-EV Transformer (87.35%).
- [[2024_Li_DiffPLF_Conditional_Diffusion_EV]] — Recurrent baselines sit within the DiffPLF comparison set for probabilistic EV charging-load forecasting; conditional diffusion cuts MAE 39.58% vs quantile regression.
- [[2024_Qu_Physics_Informed_GAT_EV_Load]] — TPA-LSTM attention-augmented recurrent decoding inside PAG; standalone LSTM baseline RMSE 0.0670 vs PAG 0.0548 on Shenzhen regional demand.
- [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] — LSTM among 10 baselines for Beijing fast-charging load; STMGCN reduces MAE ~2–20 kW below all baselines including LSTM.
- [[2024_Zhou_Conformal_Prediction_DER]] — RNN/LSTM listed among point-prediction models for DER adoption; Multivariate Hawkes + hierarchical conformal prediction gives valid circuit/substation coverage.
- [[2025_Bao_ResMMoT_Informer_Time_Series]] — BiLSTM and CNN-LSTM baselines for long-term financial series; ResMMoT-Informer improves ~30–40% (BiLSTM 20-step MAE 8.88 vs 4.72).
- [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] — LSTM baseline for Shenzhen charging-volume forecasting; few-shot Data-2 RMSE 47.92 vs LSTM 98.82 (−51.5%).
- [[2025_Han_Vertical_Federated_EGAT_LSTM]] — Core component: V2AFedEGAT-LSTM vertically federated EGAT-LSTM predictor reaching R² = 0.973 (IEEE 33-bus/7-node), ~4% better than alternatives.
- [[2025_Hussain_CAT_Former_Short_Term_EV]] — Weakest baseline in CAT-Former study (e.g. Street 1 1-h MSE 3.40 vs CAT-Former 1.41), confirming context-aware attention over plain recurrence.
- [[2025_Hussain_Hybrid_LSTM_Transformer_Demand]] — Standalone LSTM baseline for 30/120/240-day ACN demand; LSTM-Transformer hybrid cuts 30-day Caltech MAE from 38.68 to 32.42 (−16.18%).
- [[2025_Khan_Transformer_BiLSTM_Price_Forecasting]] — LSTM/BiLSTM benchmarks for day-ahead price forecasting on NYISO; Transformer-BiLSTM cuts MAE 10.3% vs BiLSTM ($3.10→$2.78/MWh).
- [[2025_Li_DC_Charging_Profiles_TFT]] — TFT beats RNN/GRU/LSTM baselines when predicting real-world DC fast-charging profiles/durations (95% relative accuracy within six input points).
- [[2025_Li_Multi_View_Graph_Intrusion_Detection_EV]] — LSTM baseline for EV charging-station intrusion detection (weighted F1 96.54%) vs MVGCRL graph contrastive learning (97.20%).
- [[2025_Matrone_QR_LSTM_Attention_EV_Load]] — Probabilistic QR-LSTM-attention model (quantile-specific LSTM encoder-decoders) for office parking-lot charging demand; CRPS −67.70% vs persistence benchmark.
- [[2025_Weqar_LTLM_LSTM_EV_Load]] — LTLM framework built on LSTM networks for long-term (1–10 yr) EV charging-station load prediction; tracks trends but flattens peaks (no numeric metrics reported).
- [[2025_Zheng_Coherent_Hierarchical_EV_Load]] — Modular LSTM forecasting engine inside PICNN + differentiable convex reconciliation layer; total MAE 2.15 vs DeepVAR 7.40 and DeepAR 9.67.
- [[2025_Zhu_Personalized_Federated_Learning]] — End-to-end federated LSTM encoder-decoder (PF-HoLo) for appliance-level household load; 13.41% MSE / 11.33% MAE improvement over FedAvg.
- [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] — LSTM among four recurrent baselines for multi-scale EV station load; MFT achieves 21.88% average improvement over LSTM (35.78% MSE gain at 96 h).
- 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] — LSTM baseline crushed by conformal-calibrated TFT on Palo Alto hourly load (RMSE 5.967 vs 1.2687 kWh, >78% cut); also the seq2seq encoder-decoder inside TFT's local processing.
- 2026 — [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] — LSTM baseline for Shenzhen UrbanEV 15–60-min demand; TriCast cuts average MAE to 2.53 vs LSTM 4.06 (×10² units).
- 2026 — [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] — Similar-day selection trims LSTM day-ahead MAE/RMSE ~1.5–2% (62.63/77.23 kW) across UrbanEV Shenzhen traffic zones.
- 2026 — [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] — LSTM point/probabilistic baseline beaten by MAML-Informer on all three datasets (e.g., Boulder RMSE 8.561 → 7.095).
- 2026 — [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] — 2×64-unit LSTM among six ML/DL models over 12 cities: beats MLP/LASSO on MAE, transfers well zero-/few-shot, but SGD linear regression best overall.
- 2026 — [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] — LSTM baseline far behind USDT (EVnetNL RMSE 13.448 vs 8.781; Perth RMSE 19.202 vs 13.837).
- 2026 — [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]] — GRU/LSTM consistently beat Transformers at mid-term (2–8 h) and long-term (1–5 d) horizons across Palo Alto/Boulder/Dundee/Perth (in some mid-term city cases >50% MAE reduction vs ARIMA); Perth LSTM best at every short-term level (station MAE 0.43–0.46).
- 2024 — [[2024_Qu_Forwardformer_Day_Ahead_Load]] — Attention-augmented LSTMa baseline beats Informer/LogTrans in most day-ahead cases but needs tens of times longer computation; on high-frequency AEL New York data LSTM-family degrades sharply while Forwardformer stays stable.
- 2026 — [[2026_Hong_SSM_Transformer_LSTM_Grid_Benchmark]] — Worst across all 30 grid×horizon evaluations in the modern controlled US benchmark (avg 6.83% MAPE / 9.13 MSE%, 0/30 wins; smallest weather gain −0.36 pp) — recurrence trails SSMs/Transformers under identical protocols and matched capacity (~2.6M params).
