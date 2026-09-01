---
type: metric
name: Mean Absolute Error (MAE)
category: Evaluation Metric / Loss Function
tags:
  - metric
  - mae
  - loss-function
---

# 📐 Mean Absolute Error (MAE)

## Definition & Mathematical Formula
MAE measures the average absolute magnitude of errors between predicted values ($\hat{y}_i$) and actual target values ($y_i$):
$$\text{MAE} = \frac{1}{N} \sum_{i=1}^N |\hat{y}_i - y_i|$$

## Application in EV Charging Load Forecasting
- **Primary Loss Function**: Frequently chosen as the loss function for training neural networks (e.g. [[2019_Zhu_EV_Load_Forecasting]]) because it is less sensitive to extreme single-point outliers compared to MSE/RMSE.
- **Advantage over MAPE**: Unlike MAPE, MAE does not involve division by actual load values ($y_i$), avoiding division-by-zero errors during non-charging hours when load is 0 kW.

## Literature References
- [[2019_Zhu_EV_Load_Forecasting]] - Used MAE as network loss function and primary evaluation metric.
- 2014 — [[2014_Alizadeh_Scalable_Stochastic_EV_Demand]] : Validated the M/G/∞ queue-based stochastic EV demand model against UC Davis/NHTS data using absolute error in kW.
- 2017 — [[2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load]] : MAE used to select best-in-window "sister" forecasts before QRA combination; worst QRA still beat the best individual sister.
- 2020 — [[2020_Huang_Ensemble_EV_Load]] : Boulder ensemble reached MAE 2.42 kWh, improving 5.79%/2.48%/0.83% vs LR/ANN/RNN and tying LSTM.
- 2021 — [[2021_VanKriekinge_Day_Ahead_EV_Demand]] : Day-ahead LSTM variants achieved **MAE < 1 kW** (15-min resolution); calendar features cut MAE up to 28.8%.
- 2021 — [[2021_Zhang_Probabilistic_Queuing_EV_Load]] : WT-CNN 1-h-ahead MAE 93.42 vs BPNN 296.59 and SVM-RBF 229.81 — roughly half the error of six benchmarks.
- 2022 — [[2022_Zhang_GCN_TRN_EV_Availability]] : GCN-TRN station availability forecasting: MAE 0.0856 vs ≥ 0.0952 for all baselines across three stations.
- 2023 — [[2023_Cheng_VMD_Prophet_LSTM]] : VMD + Prophet-LSTM evaluated with MAE alongside R²; raw Prophet collapses without decomposition (R² ≈ 0.49).
- 2023 — [[2023_Huang_MetaProbformer_EV_Load]] : Reptile-meta Probformer improved MAE by **3.614%** (homogeneous) and **8.479%** (heterogeneous) over MetaTransformer.
- 2023 — [[2023_Koohfar_Transformer_EV_Demand]] : Transformer benchmark on Boulder EV data reporting MAE alongside RMSE/MSE.
- 2024 — [[2024_Helmy_Autoformer_EV_Charging]] : Autoformer MAE ≈ 0.155–0.161 kWh/h flat across 30/60/90-day horizons vs LSTM 0.424 at 90 days (~60% lower).
- 2024 — [[2024_Li_DiffPLF_Conditional_Diffusion_EV]] : DiffPLF diffusion model improved MAE by **39.58%** over conventional quantile regression on Palo Alto data.
- 2024 — [[2024_Qu_Physics_Informed_GAT_EV_Load]] : PAG reduced MAE by 17.98% vs LSTM and 7.51% vs SOTA spatiotemporal baselines via physics-informed price elasticity.
- 2024 — [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] : STMGCN MAE 53.287 kW at 15 min, degrading slowest with horizon (54.519 @ 1 h, 55.834 @ 2 h) vs CNN-LSTM 60+ kW.
- 2024 — [[2024_Zhou_Conformal_Prediction_DER]] : Point forecasts for DER adoption reported with MAE alongside conformal coverage metrics.
- 2025 — [[2025_Alghamdi_REST_Network_Port_EV]] : RESTNet weighted ensemble beat SVR/RF/CNN/VGGNet/DeepSigRNet on MAE (headline RMSE 9.8 kW, MAPE 6.5%).
- 2025 — [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] : Customized loss = MAE + λ·FFT frequency-domain term; Data 1 3-step volume MAE 19.49 (40.81% better than ChatEV); critical-day few-shot MAE 8.49.
- 2025 — [[2025_Hussain_CAT_Former_Short_Term_EV]] : CAT-Former Park 1 MSE 0.4610 / MAE 0.6789 (−5.75% MAE vs Hybrid Transformer).
- 2025 — [[2026_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] : Stacking Hybrid 3 test MAE 2.6870 kWh; removing meta-learner degrades MAE to 3.5071 (+30.5%, p < 0.001).
- 2025 — [[2025_Tian_MSSTGAN_City_EV_Load]] : MSSTGAN Palo Alto MAE 0.0332 vs ST-GAT 0.0697; best MAPE on all four city datasets.
- 2025 — [[2025_Zheng_BWO_ICEEMDAN_iTransformer]] : BWO-tuned ICEEMDAN + iTransformer pipeline on Singapore market data evaluated with MAE/RMSE.
- 2025 — [[2025_Zheng_Coherent_Hierarchical_EV_Load]] : PICNN + DCL coherent reconciliation achieved best MAE at nearly all stations in hierarchical ACN evaluation.
- 2026 — [[2026_Hao_Mamba_KAN_HyKANet_EV]] : HyKANet average MAE 2.49 (×10² units) across 15–60 min horizons — 12.2% lower than PAG.
- 2026 — [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] : CNN-LSTM-Attention 1-h-ahead MAE 2.98 (**−17.45% vs GRU**); CNN-LSTM-Transformer best at 24-h/48-h horizons.
- 2026 — [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] : STL-Hybrid MAE 0.614 on ACN data (>88% reduction vs Informer's 4.667), robust to hyperparameter perturbation.
- 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] : TFT hourly (1–24 h) MAE 0.8399 kWh vs LSTM 4.464 / GRU 5.015 on Palo Alto data.
- 2026 — [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] : TriCast average MAE 2.53 (×10² units) across Shenzhen 15–60-min horizons, beating PIAST 2.54 and 14 other baselines.
- 2026 — [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] : Similar-day selection cuts global-average day-ahead MAE ~4.5% across RF/LightGBM/LSTM/SVR on UrbanEV zones.
- 2026 — [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] : MAML-Informer lowest MAE on all three datasets (Boulder 3.676 vs LSTM 5.374); Wilcoxon p = 1.95×10⁻³ vs Informer.
- 2026 — [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] : SGD linear regression best overall MAE across 12 city benchmarks; DL transfer MAE sometimes better than in-city applicability MAE.
- 2026 — [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] : USDT EVnetNL MAE 6.097 vs Informer 6.733 (−9.45%) and Perth MAE 9.042; ablation shows DDI removal hurts long horizons most.
- 2026 — [[2026_Jia_EVformer_Spatio_Temporal_Decoupled_Citywide]] : EVformer best MAE at all horizons on Shenzhen ST-EVCDP — 1.78/3.05/3.93 (×10⁻²) at 15/30/45 min; also trains with pure MAE loss for outlier robustness.
- 2026 — [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]] : MAE-only benchmark protocol (MAPE rejected as unstable near zero loads, R² rejected as uninterpretable) across 5 models × 4 cities × 3 spatial scales × 3 horizon regimes.
- Canonical TS benchmarks also rely heavily on MAE/MSE families: [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] (channel-independent patching), [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] (linear models rival Transformers in long-term MAE benchmarks), [[2025_Meyer_Benchmark_Foundation_Models]] (zero-shot foundation-model comparison).

## Literature Usage
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Primary metric (Eq. 6): MAE = 1/H ||y - hat y||_1; scaled by naive baseline (GM) on Monash/Darts.
