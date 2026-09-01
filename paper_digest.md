# 📋 One-File Paper Digest — All Papers (for AI Gap Analysis)

> **Purpose**: single-file, self-contained digest of ALL 130 ingested papers (source: `wiki/papers/*.md`, generated 2026-09-01). Built so an AI agent can read ONE file and immediately know what every paper did — enabling research-gap identification without opening individual notes.
> **Entry format**: `### filename` → Title — venue, year → metadata line (Models / Horizon / Metrics / Data / Features) → **What they did** (objective & contribution) → **Method core** → **Key results** (numbers) → **Gaps/Limitations**.
> **Ordering**: newest first. Wikilinks were flattened to plain text; equations omitted; full details/equations/BibTeX live in the linked per-paper note. GENERATED FILE — do not hand-edit; fix source notes and rerun `gen_paper_digest.py`.

## 🗂️ Corpus Snapshot
- Total papers: **130**
- By year: 1997 (1) · 2001 (1) · 2013 (1) · 2014 (2) · 2015 (1) · 2017 (3) · 2018 (2) · 2019 (5) · 2020 (3) · 2021 (10) · 2022 (3) · 2023 (12) · 2024 (27) · 2025 (24) · 2026 (23) · ???? (12)
- Most-cited model concepts: LSTM (47), Transformer (34), Informer (18), DeepAR (16), PatchTST (16), ARIMA (13), RNN (12), MLP (12), GRU (11), SVR (11), TimesFM (11), XGBoost (10)

## 🔎 Quick-Scan Table
| Paper | Yr | Venue | Core Models | Horizon | Data (#) |
|---|---|---|---|---|---|
| 2026_CNN_LSTM_Attention_Fast_Charging | 2026 | IEEE Transactions on Industry … | CNN_LSTM_Attention, CNN_LSTM_Transformer … | Short_Term_Forecasting | 2 |
| 2026_Decomposition_Stacked_Meta_Learning_EV_Load | 2026 | IEEE Transactions on Smart Grid | STL_Hybrid, STL … | Short_Term_Forecasting | 4 |
| 2026_DualDirection_Transformer_EV_Charging | 2026 | Sustainable Energy, Grids and Networks | USDT, SMAN … | Long_Term_Forecasting | 4 |
| 2026_EVformer_Spatio_Temporal_Decoupled_Citywide | 2026 | World Electric Vehicle Journal … | EVformer, Multi_Head_Attention … | Spatial_Temporal_Forec … | 1 |
| 2026_EnergyMamba_Graph_Mamba_ASCQR | 2026 | ACM SIGKDD Conference on Knowledge … | EnergyMamba, AS_CQR … | Short_Term_Forecasting | 3 |
| 2026_FlowState_Sampling_Rate_Equivariant_Forecasting | 2026 | Proceedings of the 43rd International … | FlowState, Mamba_SSM … | Short_Term_Forecasting … | 7 |
| 2026_INLA_Spatio_Temporal_EV_Demand | 2026 | arXiv preprint (arXiv:2604.19841) | INLA_Latent_Gaussian_Model (proposed-new; … | day-ahead daily … | 1 |
| 2026_Lyapunov_EV_Scheduling | 2026 | arXiv preprint arXiv:2604.16873 … | Forecast-Enhanced Lyapunov Optimization, RHC … | Short_Term_Forecasting | 2 |
| 2026_MFT_Multi_Scale_Fusion_Transformer | 2026 | Scientific Reports (Nature … | MFT, Transformer … | Long_Term_Forecasting | 1 |
| 2026_ML_Comparison_EV_Charging_Forecasting | 2026 | arXiv preprint arXiv:2512.17257 … | ARIMA, XGBoost … | Short_Term_Forecasting | 4 |
| 2026_ML_Geographical_Transferability_EV | 2026 | Journal of Energy Storage | SGD, Random_Forest … | Short_Term_Forecasting | 5 |
| 2026_Mamba_3_Sequence_Modeling | 2026 | arXiv preprint (arXiv:2603.15569); … | Mamba-3, Mamba_SSM … |  | 8 |
| 2026_Mamba_KAN_HyKANet_EV | 2026 | ICASSP 2026 (IEEE International … | HyKANet, Mamba_SSM … | Short_Term_Forecasting | 1 |
| 2026_MetaLearning_Informer_Probabilistic_EV | 2026 | Applied Soft Computing | MAML-Informer, Informer … | Short_Term_Forecasting | 3 |
| 2026_Moirai_2_When_Less_Is_More | 2026 | arXiv preprint arXiv:2511.11698v3 … | Moirai, Moirai_MoE … | Long_Term_Forecasting | 5 |
| 2026_PC_M3_Mamba_EV_Clusters | 2026 | Electronics (MDPI), vol. 15, art. 2380 | PC-M3, Mamba-3 … | Day_Ahead_Forecasting | 5 |
| 2026_SSM_Transformer_LSTM_Grid_Benchmark | 2026 | arXiv preprint (arXiv:2602.21415) | S_Mamba, PowerMamba … | Long_Term_Forecasting | 1 |
| 2026_Similar_Day_Selection_EV_Load | 2026 | Applied Energy | XGBoost, NSGA-II … | Day_Ahead_Forecasting | 1 |
| 2026_TFT_Conformal_Environmental_EV_Load | 2026 | Computers and Electrical Engineering, … | Temporal_Fusion_Transformer, … | Short_Term_Forecasting | 2 |
| 2026_TS_ICL_Time_Indexed_Foundation_Model | 2026 | arXiv preprint arXiv:2606.05878 … | TS-ICL, Chronos-2 … | Short_Term_Forecasting … | 6 |
| 2026_TiRex_2_Multivariate_Streaming_Forecasting | 2026 | arXiv preprint arXiv:2607.01204 … | TiRex-2, TiRex … | Short_Term_Forecasting … | 8 |
| 2026_Toto_2_Scaling_Era | 2026 | arXiv preprint arXiv:2605.20119v2 … | Toto, TimesFM … | Long_Term_Forecasting | 6 |
| 2026_TriModal_Causal_EV_Demand | 2026 | Pattern Recognition Letters, Vol. … | TriCast, SAGE_Semantic_Aware_Graph_Encoder … | Short_Term_Forecasting | 1 |
| 2025_BWO_ICEEMDAN_iTransformer | 2025 | Algorithms (MDPI), vol. 18, no. 5, … | iTransformer, ICEEMDAN … | Short_Term_Forecasting | 1 |
| 2025_Benchmark_Foundation_Models | 2025 | IEEE Access | Chronos, Chronos-Bolt … | Short_Term_Forecasting | 4 |
| 2025_CAT_Former_Short_Term_EV | 2025 | Scientific Reports, Vol. 15, Article … | CAT-Former (Context-Aware Temporal … | 1-Hour Ahead and … | 2 |
| 2025_Chronos_2_Univariate_to_Universal | 2025 | arXiv preprint arXiv:2510.15821v1 … | Chronos-2, Chronos … | Long_Term_Forecasting | 12 |
| 2025_Coherent_Hierarchical_EV_Load | 2025 | IEEE Transactions on Industry … | LSTM, PICNN … | Day_Ahead_Forecasting | 1 |
| 2025_DC_Charging_Profiles_TFT | 2025 | Nature Communications 16:10921 | Temporal_Fusion_Transformer, beta-VAE … | Short_Term_Forecasting | 2 |
| 2025_EV_STLLM_Spatio_Temporal_LLM | 2025 | arXiv preprint (arXiv:2507.09527), … | EV-STLLM, GPT-2 … | Short_Term_Forecasting | 2 |
| 2025_Hybrid_LSTM_Transformer_Demand | 2025 | Scientific Reports (Nature … | LSTM, Transformer … | Long_Term_Forecasting | 3 |
| 2025_LTLM_LSTM_EV_Load | 2025 | 2025 IEEE DELCON - International … | LTLM, LSTM | Long_Term_Forecasting | 1 |
| 2025_MSSTGAN_City_EV_Load | 2025 | IEEE Access, Vol. 13, pp. 29000-29017 | Multi-Scale Spatial-Temporal Graph Attention … | City-Level … | 4 |
| 2025_Meta_Learning_Physics_Informed_GACN_Power_System | 2025 | IEEE Transactions on Network Science … | Meta-PIGACN, Physics-Informed Graph Attention … | Real-Time … | 4 |
| 2025_MixerInformer_Transfer_Learning_New_EV_Stations | 2025 | arXiv preprint (submitted to … | MIK-TST, MLP-Mixer … | Long_Term_Forecasting | 1 |
| 2025_Multi_View_Graph_Intrusion_Detection_EV | 2025 | Applied Energy | MVGCRL, Mask_Attention_Graph_Transformer … | Spatial_Temporal_Forec … | 1 |
| 2025_Personalized_Federated_Learning | 2025 | Applied Energy | PF-HoLo, LSTM … | Short_Term_Forecasting | 1 |
| 2025_QR_LSTM_Attention_EV_Load | 2025 | ACM E-Energy '25: 16th ACM … | QR-LSTM-Attention, LSTM … | 24-Hour Day-Ahead … | 2 |
| 2025_REST_Network_Port_EV | 2025 | IEEE Access | RESTNet, ResNet … | Short_Term_Forecasting | 2 |
| 2025_ResMMoT_Informer_Time_Series | 2025 | IEEE Transactions on Neural Networks … | ResMMoT_Informer, Sparse_Mixture_of_Experts … | Long_Term_Forecasting | 3 |
| 2025_Stochastic_MPC_Conformal_Hub | 2025 | IEEE Conference on Decision and … | XGBoost (Scikit-learn … | day-ahead 24 h @ 15 … | 4 |
| 2025_Stochastic_MPC_Microgrid_EV | 2025 | IEEE Transactions on Transportation … | MS_MPC, MPC … | Short_Term_Forecasting | 2 |
| 2025_Sundial_Highly_Capable_Time_Series_Foundation_Models | 2025 | Proceedings of the 42nd International … | Sundial, Transformer … | Long_Term_Forecasting | 11 |
| 2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning | 2025 | 39th Conference on Neural Information … | TiRex, xLSTM … | Short_Term_Forecasting … | 9 |
| 2025_Transformer_BiLSTM_Price_Forecasting | 2025 | IEEE Transactions on Industry … | Transformer_BiLSTM, Transformer … | Day_Ahead_Forecasting | 3 |
| 2025_Vertical_Federated_EGAT_LSTM | 2025 | Processes | V2AFedEGAT-LSTM, EGAT … | Short_Term_Forecasting | 3 |
| 2026_Hybrid_XGBoost_BiLSTM_EV_Load | 2025 | Scientific Reports 16:374 | XGBoost, BiLSTM … | Short_Term_Forecasting | 2 |
| 2024_Adaptive_Probabilistic_Netload | 2024 | IEEE Transactions on Power Systems, … | GAM, Kalman_Filter … | Day_Ahead_Forecasting | 2 |
| 2024_Attention_Spatiotemporal_MultiGraph_EV_Load | 2024 | IEEE Transactions on Smart Grid, Vol. … | STMGCN, TCN … | Short_Term_Forecasting | 1 |
| 2024_Autoformer_EV_Charging | 2024 | 2024 6th International Conference on … | Autoformer, LSTM | Long_Term_Forecasting | 1 |
| 2024_BiMamba_Bidirectional_Mamba_Forecasting | 2024 | arXiv preprint (arXiv:2404.15772v3, … | Bi-Mamba+, Mamba_SSM | Long_Term_Forecasting | 8 |
| 2024_Conformal_Prediction_DER | 2024 | arXiv preprint arXiv:2411.12193 (v4) | HPCP, Multivariate_Hawkes_Process … | Long_Term_Forecasting | 1 |
| 2024_Data_Driven_EVCS_Demand_Forecasting | 2024 | 2024 IEEE 7th International … | MLP, SVR … | Short_Term_Forecasting | 1 |
| 2024_Day_Ahead_EVCB_EVSC_Parking_Lot | 2024 | Energy, vol. 309, 133090 | ADMM-NN, KMeans_Clustering … | Day_Ahead_Forecasting | 3 |
| 2024_DiffPLF_Conditional_Diffusion_EV | 2024 | 23rd Power Systems Computation … | DiffPLF, DDPM … | Day_Ahead_Forecasting | 2 |
| 2024_Divide_Conquer_Transformer_EV | 2024 | arXiv preprint (arXiv:2403.13246) | DCT-EV, Transformer … | Short_Term_Forecasting | 1 |
| 2024_EV_Load_Forecasting_DAM | 2024 | Applied Energy 360 (2024) 122801 | XGBoost, MLP … | Day_Ahead_Forecasting | 4 |
| 2024_Feature_Enhanced_Probabilistic_EV_Load | 2024 | Applied Energy 371 (2024) 123751 | FEDM, GRN … | Day_Ahead_Forecasting | 1 |
| 2024_Forwardformer_Day_Ahead_Load | 2024 | IEEE Transactions on Power Systems, … | 2024_Forwardformer_Day_Ahead_Load, … | Day_Ahead_Forecasting | 5 |
| 2024_KAN_Kolmogorov_Arnold_Networks | 2024 | arXiv:2404.19756 (accepted at ICLR … | KAN, MLP … | Short_Term_Forecasting | 5 |
| 2024_LASSO_BPNN_Mid_Term_EV_Load | 2024 | 2024 IEEE 2nd International … | MLP, XGBoost … | Long_Term_Forecasting | 2 |
| 2024_LSTM_Transformer_EV_Consumption | 2024 | SSRN Preprint 4747046 (not peer … | LSTM_Transformer, LSTM … | Short_Term_Forecasting | 1 |
| 2024_MQ_TCN_Transfer_Learning_EV | 2024 | arXiv preprint arXiv:2409.11862 (Sep … | MQ_TCN, TCN … | Day_Ahead_Forecasting | 2 |
| 2024_Physics_Informed_GAT_EV_Load | 2024 | IEEE Transactions on Intelligent … | PAG, PIML … | Short_Term_Forecasting | 1 |
| 2024_PowerMamba_Power_Systems_SSM | 2024 | arXiv preprint (arXiv:2412.06112), v2 … | PowerMamba, Mamba_SSM … | Short_Term_Forecasting … | 1 |
| 2024_Prediction_Interval_EV_Loads | 2024 | 2024 56th North American Power … | Gaussian_Process_Regression, … | Short_Term_Forecasting | 2 |
| 2024_Robust_MTS_Transitional_Shift | 2024 | arXiv preprint (IEEE journal … | JointPGM | Short_Term_Forecasting | 6 |
| 2024_TOU_Price_Meteorology_EV_Charging_Load | 2024 | 2024 7th International Conference on … | CNN, GRU … | Short_Term_Forecasting | 1 |
| 2024_TiDE_Long_Term_Forecasting | 2024 | arXiv:2304.08424v5 [stat.ML] (Google … | TiDE, DLinear … | Long_Term_Forecasting | 9 |
| 2024_TimeMachine_Mamba_Long_Term_Forecasting | 2024 | arXiv preprint (arXiv:2403.09898v2, … | 2024_TimeMachine_Mamba_Long_Term_Forecasting, … | Long_Term_Forecasting | 7 |
| 2024_TimesFM_Decoder_Only_Foundation_Model | 2024 | arXiv preprint arXiv:2310.10688v4 … | TimesFM, PatchTST … | Long_Term_Forecasting | 11 |
| 2024_Unified_Training_Universal_Time_Series_Transformers | 2024 | Proceedings of the 41st International … | Moirai, Transformer … | Short_Term_Forecasting … | 13 |
| 2024_V2G_SVE_Evaluation_Metric | 2024 | IEEE Transactions on Smart Grid, vol. … | V2G-SVE, Aggregate_EV_Fleet_Model … | Day_Ahead_Forecasting | 2 |
| 2024_iTransformer_Inverted_Transformers_Effective_Time_Series | 2024 | ICLR 2024 (Spotlight) | iTransformer, Transformer … | Long_Term_Forecasting | 8 |
| 2023_Combined_Deep_Learning_EV_Station_STLF | 2023 | 2023 2nd Asia Power and Electrical … | CNN_LSTM_Transformer_Combined_Model, CNN … | Short_Term_Forecasting | 1 |
| 2023_Crossformer_Cross_Dimension_Dependency | 2023 | ICLR 2023 | Crossformer, DSW_Embedding … | Long_Term_Forecasting | 6 |
| 2023_DLinear_Are_Transformers_Effective_LTSF | 2023 | AAAI 2023 | DLinear, DLinear … | Long_Term_Forecasting | 9 |
| 2023_DiffSTG_Probabilistic_ST_Graph_Diffusion | 2023 | ACM conference proceedings (© 2023 … | DiffSTG, UGnet | Spatial_Temporal_Forec … | 3 |
| 2023_MetaProbformer_EV_Load | 2023 | IEEE Transactions on Intelligent … | MetaProbformer, MetaProbformer … | Short_Term_Forecasting | 4 |
| 2023_Multi_Branch_ResTrans_Solar | 2023 | IEEE Transactions on Industry … | Multi-Branch ResNet-Transformer (ResTrans), … | Spatial_Temporal_Forec … | 1 |
| 2023_NHiTS_Neural_Hierarchical_Interpolation | 2023 | AAAI 2023 | NHiTS, NBEATS … | Long_Term_Forecasting | 6 |
| 2023_PatchTST_A_Time_Series_is_Worth_64_Words | 2023 | ICLR 2023 | PatchTST, Transformer … | Long_Term_Forecasting | 8 |
| 2023_TimesNet_Temporal_2D_Variation_Modeling | 2023 | ICLR 2023 | TimesNet, TimesNet … | Long_Term_Forecasting | 16 |
| 2023_Transformer_EV_Demand | 2023 | Sustainability 2023, 15(3), 2105 | Transformer, LSTM … | Long_Term_Forecasting | 2 |
| 2023_Treatment_Effects_Continuous_Time_Hidden_Confounders | 2023 | arXiv preprint arXiv:2302.09446 … | LipSCDE, Neural_SDE … | Short_Term_Forecasting | 3 |
| 2023_VMD_Prophet_LSTM | 2023 | Frontiers in Energy Research, Vol. … | VMD, Prophet … | Short_Term_Forecasting | 1 |
| 2022_GCN_TRN_EV_Availability | 2022 | 2022 5th International Conference on … | GCN-TRN, GCN … | Spatial_Temporal_Forec … | 1 |
| 2022_RevIN_Reversible_Instance_Normalization | 2022 | ICLR 2022 | RevIN, Informer … | Long_Term_Forecasting | 5 |
| 2022_Robust_Deep_Gaussian_Process_Load | 2022 | IEEE Transactions on Industrial … | Deep_Gaussian_Process, Sparse_GP … | Day_Ahead_Forecasting | 3 |
| 2021_Autoformer_Decomposition_Transformers_AutoCorrelation | 2021 | NeurIPS 2021 (35th Conference on … | Autoformer, Auto-Correlation Mechanism … | Long_Term_Forecasting | 7 |
| 2021_CSDI_Conditional_Diffusion_Forecasting | 2021 | NeurIPS 2021 (35th Conference on … | CSDI, Conditional Score-based Diffusion Model … | Short_Term_Forecasting | 7 |
| 2021_Conformal_Time_Series_Forecasting | 2021 | NeurIPS 2021 (35th Conference on … | CF-RNN, Conformal_Prediction … | Short_Term_Forecasting | 4 |
| 2021_Day_Ahead_EV_Demand | 2021 | World Electric Vehicle Journal, … | LSTM, LSTM_B … | Day_Ahead_Forecasting | 1 |
| 2021_Hierarchical_Probabilistic_EV_Load | 2021 | Applied Energy, 283, 116337 | GBRT, QRF … | Short_Term_Forecasting | 3 |
| 2021_Informer_Beyond_Efficient_Transformer | 2021 | AAAI 2021 (Best Paper Award) | Informer, ProbSparse Self-Attention … | Long_Term_Forecasting | 3 |
| 2021_Probabilistic_Queuing_EV_Load | 2021 | IEEE Transactions on Cybernetics, … | CNN, Discrete Wavelet Transform (WT) … | Short_Term_Forecasting | 3 |
| 2021_RL_Q_Learning_EV_Load | 2021 | IEEE Transactions on Industrial … | Q-Learning (off-policy RL), ANN … | Short_Term_Forecasting | 1 |
| 2021_TFT_Temporal_Fusion_Transformers | 2021 | International Journal of Forecasting, … | Temporal Fusion Transformer, Gated Residual … | Multi_Horizon | 4 |
| 2021_TimeGrad_Diffusion_Forecasting | 2021 | ICML 2021 (International Conference … | TimeGrad, Denoising Diffusion Probabilistic … | Short_Term_Forecasting | 6 |
| 2020_DeepAR_Probabilistic_Forecasting | 2020 | International Journal of Forecasting, … | DeepAR, LSTM | Short_Term_Forecasting | 5 |
| 2020_Ensemble_EV_Load | 2020 | 2020 IEEE Electric Power and Energy … | Ensemble_Stacking, ANN … | Short_Term_Forecasting | 1 |
| 2020_NBEATS_Interpretable_Time_Series_Forecasting | 2020 | ICLR 2020 | NBEATS, NBEATS-G … | Long_Term_Forecasting | 5 |
| 2019_ApplSci_EV_Load_Forecasting | 2019 | Applied Sciences 2019, 9(9), 1723 … | ANN, RNN … | Short_Term_Forecasting | 1 |
| 2019_Deep_Probabilistic_Scheduling_Power_Markets | 2019 | IEEE Transactions on Power Systems, … | Bidirectional LSTM (BLSTM), LSTM … | Day_Ahead_Forecasting | 2 |
| 2019_EV_Load_Forecasting | 2019 | Energies 2019, 12(14), 2692 (MDPI) | ANN, RNN … | Short_Term_Forecasting | 2 |
| 2019_Graph_WaveNet_Spatial_Temporal_Modeling | 2019 | IJCAI 2019 (28th International Joint … | Graph_WaveNet | Short_Term_Forecasting | 2 |
| 2019_LogSparse_Enhancing_Locality_Transformer | 2019 | NeurIPS 2019 (33rd Conference on … | LogSparse_Transformer, … | Short_Term_Forecasting | 6 |
| 2018_Empirical_TCN_Sequence_Modeling | 2018 | arXiv preprint arXiv:1803.01271 … | TCN, LSTM … | Short_Term_Forecasting | 10 |
| 2018_Reptile_First_Order_Meta_Learning | 2018 | arXiv preprint (OpenAI), … | Reptile, MAML … | MAML | 3 |
| 2017_Attention_Is_All_You_Need | 2017 | Advances in Neural Information … | Transformer, Multi_Head_Attention … | Short_Term_Forecasting | 4 |
| 2017_MAML_Model_Agnostic_Meta_Learning | 2017 | Proceedings of the 34th International … | MAML, FOMAML … | Short_Term_Forecasting | 6 |
| 2017_QRA_Sister_Forecasts_Probabilistic_Load | 2017 | IEEE Transactions on Smart Grid, vol. … | QRA, Quantile_Regression … | Day_Ahead_Forecasting | 1 |
| 2015_Review_AI_Load_Demand | 2015 | Renewable and Sustainable Energy … | ANN, MLP … | Short_Term_Forecasting | 8 |
| 2014_Kingma_Adam_Optimization | 2014 | ICLR 2015 (arXiv:1412.6980) | Adam, Adam … | Short_Term_Forecasting | 4 |
| 2014_Scalable_Stochastic_EV_Demand | 2014 | IEEE Transactions on Smart Grid, … | Queuing_Model, Queuing_Model … | Short_Term_Forecasting | 2 |
| 2013_Gaussian_Processes_Time_Series | 2013 | Philosophical Transactions of the … | Gaussian_Process, … | Short_Term_Forecasting | 4 |
| 2001_Neural_Networks_STLF_Review | 2001 | IEEE Transactions on Power Systems, … | MLP, ANN … | Day_Ahead_Forecasting | 4 |
| 1997_Long_Short_Term_Memory | 1997 | Neural Computation, 9(8), 1735-1780 | LSTM, RNN … | Long_Term_Forecasting | 5 |
| 2014_A_Method_for_Stochastic_Optimization | ???? |  |  |  | 0 |
| 2014_Adam_Stochastic_Optimization | ???? |  |  |  | 0 |
| 2019_EV_Charging_Load_Forecasting_Comparative_DL | ???? |  |  |  | 0 |
| 2019_STLF_EVCS_Deep_Learning | ???? |  |  |  | 0 |
| 2021_APLF_Adaptive_Probabilistic_Load | ???? |  |  |  | 0 |
| 2021_Day_Ahead_Forecast_EV_Demand_DNN | ???? |  |  |  | 0 |
| 2021_Ensemble_Hierarchical_Probabilistic_EV_Load | ???? |  |  |  | 0 |
| 2021_Kalman_COVID_France | ???? |  |  |  | 0 |
| 2021_Regional_Netload | ???? |  |  |  | 0 |
| 2022_State_Space_PostCOVID | ???? |  |  |  | 0 |
| 2023_Prediction_EV_Charging_Demand_Transformer | ???? |  |  |  | 0 |
| 2024_Physics_Informed_Attention_Graph_Regional_EV_Demand | ???? |  |  |  | 0 |

---
## 📄 Entries

### 2026_CNN_LSTM_Attention_Fast_Charging
**Attention-Enhanced CNN-LSTM Models for Forecasting EV Fast-Charging Load at Public Stations**  
Romia et al. · IEEE Transactions on Industry Applications · 2026
<https://doi.org/10.1109/TIA.2026.3677828>
**Models**: CNN_LSTM_Attention, CNN_LSTM_Transformer, GRU, RNN, Transformer, LSTM_Transformer, SARIMA, SVR, Optuna_TPE  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAE, R_squared  
**Data**: Caltech_ACN; Weather  
**Features**: Historical_Load, Temperature, Humidity, Calendar_Features, Calendar_Features

- **What they did:**
  - DC fast-charging (DCFC) station loads are far more volatile than AC Level-2 loads; prior work targets single-step forecasts, coarse resolutions, aggregated regional loads, and ignores exogenous drivers (weather, day-type). Statistical models (SARIMA) miss nonlinearity; ML methods (SVR, LR, XGBoost/CatBoost) treat time steps independently; plain DL (LSTM, GRU, CNN) struggles with long-range dependencies at station …
  - Proposes two complementary application-driven hybrids (novelty is the tailored hybrid design, not attention itself): **CNN_LSTM_Attention** for single-step (1-h ahead) forecasting via single-head attention over LSTM hidden states, and **CNN_LSTM_Transformer** for multi-step (24-h, 48-h ahead) forecasting via multi-head self-attention + positional encodings over stacked Transformer layers. Includes an Optuna_TPE …
- **Method core:** Pipeline: multivariate inputs → 1-D CNN layers (kernel size 3, ReLU, max pooling size=2) for local temporal–feature extraction → stacked LSTM layers for sequential dependencies → attention/Transformer head → dense output.
- **Key results:**
  - **Single-step (1-h)** vs best baseline GRU: CNN_LSTM_Attention MAE 2.98, RMSE 4.61, R² 0.89 → **17.45% MAE reduction, 13.83% RMSE reduction, +3.49% R²**; also fastest training (144.63 s vs GRU 225.79 s) and lowest inference latency (0.742 ms/sample vs GRU 2.319 ms). CNN-LSTM-Transformer: MAE 3.17 (−12.18%), RMSE 4.71 …
  - **24-h horizon**: CNN-LSTM-Transformer best — MAE 5.17, RMSE 7.68, R² 0.70 (**−5.48% MAE, −4.0% RMSE, +2.94% R² vs GRU**); CNN-LSTM-Attention 5.35/7.78/0.69; Transformer collapses to 7.77/11.05/0.39.
  - **48-h horizon**: CNN-LSTM-Transformer best — MAE 5.60, RMSE 8.16, R² 0.66 (**−7.59% MAE, −4.45% RMSE, +4.76% R² vs RNN**, the strongest traditional baseline here); CNN-LSTM-Attention degrades (5.61/8.34/0.65) due to error accumulation over long horizons.
- **Gaps/Limitations:**
  - Both models underestimate rare, abrupt high-magnitude charging spikes (irregular events underrepresented in training data).
  - Single-station evaluation only; no cross-network generalization tested. Future work: transfer learning / low-rank adaptation (LoRA-style) to multiple fast-charging networks, online/continuous learning for evolving behavior.
  - Maintaining two separate models per horizon adds deployment cost; a mixture-of-experts unification proposed as future direction.
  - No probabilistic/uncertainty outputs; integration with grid-aware optimization (storage scheduling, smart charging, market participation) left future; interpretability (e.g., SHAP) noted as open area.

### 2026_Decomposition_Stacked_Meta_Learning_EV_Load
**Decomposition and Stacked Meta-Learning for Short-Term Electric Vehicle Load Forecasting**  
Ullah et al. · IEEE Transactions on Smart Grid · 2026
<https://doi.org/10.1109/TSG.2026.3677496>
**Models**: STL_Hybrid, STL, Ridge_Regression, XGBoost, Random_Forest, Gradient_Boosting_Regressor, Prophet, CatBoost, Informer, CNN-LSTM-AM, DeepBoost  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, RMSE, MAPE, R_squared  
**Data**: Caltech_ACN; ChargePlace_Scotland; Palo_Alto_EV; Paris_Belib_EV  
**Features**: Historical_Load, Lag_Features, Calendar_Features, Trend_Component, Seasonal_Component, Residual_Component

- **What they did:**
  - Short-term EV load forecasting (STLF) must jointly capture **multi-scale temporal structure** (diurnal/weekly/annual cycles + adoption trend), **nonlinear interactions**, and **cross-dataset heterogeneity**; existing statistical/ensemble/DL models rely on implicit sequence learning, uniform learners across decomposed components, or simple linear fusion.
  - Contributions: 1. A decomposition-driven hybrid framework integrating **STL** with a stacked ensemble architecture that explicitly disentangles multi-scale temporal structures before fusion. 2. **Component-specific modeling**: Ridge regression → smooth trend; XGBoost → nonlinear seasonal patterns; Random_Forest → stochastic residual fluctuations. 3. Stacked fusion via a **Gradient Boosting Regressor (GBR) …
- **Method core:** **STL decomposition** ("additive decomposition"):   y_t = T_t + S_t + R_t   computed iteratively via Loess local regression ("Loess smoothing equations"):   S_t = Loess(y_t, w_S), \qquad T_t = Loess(y_t - S_t, w_T), \qquad R_t = y_t - T_t - S_t   ($w_S$, $w_T$ seasonal/trend smoothing windows; robust-weight refinement pass).
- **Key results:**
  - **ACN dataset (Table VIII)**: Proposed STL-Hybrid **MAE 0.614, RMSE 0.797, MAPE 12.71%** vs Informer (4.667/8.734/74.17%), CatBoost (5.126/7.586/85.88%), Prophet (10.392/23.911/121.37%), CNN-LSTM-AM (7.071/9.819/166.58%), DeepBoost (7.146/9.884/168.86%) → **>90% RMSE and >88% MAPE reduction vs strongest benchmark …
  - **Other datasets**: Palo Alto — proposed 1.302/1.646/14.51% vs CatBoost 2.628/3.542/40.18%; Perth — 1.206/1.531/11.32% vs CatBoost 5.038/7.291/156.7%; Paris — 0.993/1.336/12.45% vs CatBoost 3.928/6.272/142.06%. Consistent wins across scales from 259,352 samples down to 5,780 samples.
  - **Robustness (Table VI)**: 5-fold time-series CV mean MAE/RMSE/MAPE = 0.614/0.797/12.71% with tiny stds (0.021/0.035/0.84); hyperparameter perturbations (trees ±20%, depth ±2, LR ±0.02) change MAE by at most ~0.02 — low tuning sensitivity.
- **Gaps/Limitations:**
  - Relies only on load-intrinsic features; **no exogenous variables** (temperature, precipitation) yet — weather-aware features are planned future work.
  - No probabilistic/uncertainty-quantified forecasts (deterministic point predictions only); probabilistic extension planned.
  - No adaptive online learning mechanism for evolving charging environments; scalability/real-time adaptation left open.
  - STL assumes additive structure; strong nonstationarity or multiplicative seasonality may require alternative decompositions.

### 2026_DualDirection_Transformer_EV_Charging
**Dynamic charging load prediction using uncertainty-scale dual-direction transformer**  
Zhang et al. · Sustainable Energy, Grids and Networks · 2026
<https://doi.org/10.1016/j.segan.2026.102428>
**Models**: USDT, SMAN, DDI, Informer, MetaProbformer, Transformer, DeepAR, LSTM, ARIMA, Prophet, SVR, FEDM, PICCN  
**Horizon**: Long_Term_Forecasting  
**Metrics**: RMSE, MSE, MAE, R_squared, ACE, CRPS  
**Data**: ElaadNL; Perth_EV; Boulder_Colorado; Palo_Alto_EV  
**Features**: Historical_Load, Cyclical_Encodings, Calendar_Features

- **What they did:**
  - **Problem:** Conventional EV charging load forecasting struggles with (i) intricate temporal dependencies and spatial characteristics and (ii) uncertainty in load fluctuations.
  - **Proposal:** **USDT — Uncertainty-Scale Dual-Direction Transformer**, a probabilistic charging-load forecasting model on an Informer/MetaProbformer backbone with two new modules:
  - **SMAN (Scalable Multi-Scale Linear Attention Network):** captures load variation across multiple temporal/spatial scales using convolutional projections + query sparsity.
  - **DDI (Dual-Direction Interaction module):** bidirectional attention (horizontal = cross-station patterns, vertical = within-station temporal dynamics) for local spatial relationships.
  - Probabilistic output $\mathcal{N}(\mu_t,\sigma_t^2)$ per step; **>10% improvement** in RMSE on ElaadNL vs existing methods.
- **Method core:** $N$ interrelated univariate series; conditioning range Seq$(1,t_0)$, prediction range Seq$(t_0+1,t_0+\tau)$; known covariate matrix $X$ (time-independent e.g. station IDs and/or time-dependent e.g. month). **Historical sequence (Eq. 3.1):**  y_{i,1:t_0} = \begin{cases} y_{i,1} & t=1 \\ y_{i,2} & t=2 \\ \vdots & \\ y_{i,t_0} & t=t_0 \end{cases} \tag{3.1}  **Covariate matrix …
- **Key results:**
  - **EVnetNL (Table 2):** vs Informer/Probformer: RMSE −10.99%/−14.01%, MSE −21.11%/−26.07%, MAE −9.45%/−11.59%. **Perth (Table 3):** USDT RMSE **13.837**, MSE **191.457**, MAE **9.042** vs Informer 14.319/205.021/9.189 and Probformer 14.176/200.959/9.245 (RMSE −3.37%/−2.39%; MSE −6.62%/−4.73%; MAE −1.60%/−2.20%). Other …
- **Gaps/Limitations:**
  - **Short-horizon accuracy:** advantage concentrated at long horizons; short-term gains over strong baselines are modest (inductive biases favor low-frequency components/cross-station co-movements). Future: horizon-aware loss weighting, curriculum fine-tuning on high-variance intervals, lightweight residual correction heads.
  - **Computational complexity:** +213% iteration latency from multi-scale pathways, dual-direction interactions and test-time adaptation; pruning, knowledge distillation, low-rank factorization and quantization-aware training planned.
  - **Domain shift:** absolute accuracy degrades under pronounced distributional discrepancies (temporal coverage, station configuration, regional usage patterns); domain adaptation / robust normalization protocols needed.
  - Text inconsistently attributes robustness to a "meta-learning framework" although no explicit meta-learning algorithm is defined.
  - Table 1 loss (MSE) conflicts with stated NLL objective.

### 2026_EVformer_Spatio_Temporal_Decoupled_Citywide
**EVformer: A Spatio-Temporal Decoupled Transformer for Citywide EV Charging Load Forecasting**  
Jia et al. · World Electric Vehicle Journal (MDPI), Vol. 17 · 2026
<https://doi.org/10.3390/wevj17020071>
**Models**: EVformer, Multi_Head_Attention, Gated_Fusion, Top-K_Spatial_Attention, STGCN, DCRNN, MTGNN, Graph_WaveNet, GAT, AST-GAT, PAG  
**Horizon**: Spatial_Temporal_Forecasting  
**Metrics**: RMSE, MAE, MAPE  
**Data**: ST-EVCDP  
**Features**: Charging_Demand, Charging_Duration, Pile_Utilization_Rate, Pricing_Mechanism (fixed/dynamic), Regional_Functional_Type (residential/commercial/industrial), Charging_Pile_Density, Temperature, Time_of_Day, Spatio_Temporal_Embedding

- **What they did:**
  - Citywide EV charging demand forecasting suffers from (i) quadratic self-attention cost in long-sequence temporal modeling, (ii) quadratic spatial attention cost w.r.t. number of stations $N$, and (iii) tightly coupled architectures lacking modular flexibility.
  - Proposes **EVformer**, a **modular encoder–decoder framework that explicitly decouples temporal sequence modeling from spatial dependency learning**:
  - **Temporal module**: a *global aggregation mechanism* compresses multi-station/multi-channel time-series into a shared latent global context used as attention query → avoids $O(T^2 C)$ time–time self-attention.
  - **Spatial module**: a *dynamic semantics-aware Top-K spatial attention* combining physical graph topology with data-driven neighbor selection → reduces complexity from $O(N^2)$ to $O(K^2)$.
  - **Bidirectional Temporal Bridge (BTB)** maps historical context to future steps bidirectionally to reduce error propagation/drift in multi-horizon decoding; plus a **Multi-Horizon Decoder (MHD)** and **Gated Fusion Unit** that adaptively balances temporal vs. spatial contributions per horizon/node/time-step.
  - Validated on Shenzhen dataset (18,061 public charging piles); beats VAR/Lasso/KNN/FCNN/LSTM/GCN/GAT/STGCN/DCRNN/MTGNN/GraphWaveNet/AST-GAT/PAG on MAE, RMSE, MAPE at 15/30/45 min horizons.
- **Method core:** Station set (**Eq. 3 — station set**): $\mathcal{S} = \{s_1, s_2, \ldots, s_N\}$ (**Eq. 4 — feature matrix per step**): $X_t \in \mathbb{R}^{N \times D}$ ($D$ observed features: charging indicators + external factors) (**Eq. 5 — history window**): $X_{1:T} = \{X_1, X_2, ..., X_T\} \in \mathbb{R}^{T \times N \times D}$ (**Eq. 6 — mapping**): $\mathcal{F}(\cdot) : X_{1:T} …
- **Key results:**
  - Table 1 metrics ×10⁻² (RMSE/MAE as reported; MAPE in %):
  - EVformer best on ALL metrics/horizons; at 30 min beats best baseline PAG by **3.8% RMSE / 2.1% MAE / 3.1% MAPE**; ~**1–6% relative RMSE reduction** vs. graph-based SOTA at 45 min and up to **~13% improvement at 15 min** (conclusions section).
  - w/o Spatial (replaced by static GCN): RMSE +7.2%, MAPE +13.9% at 15 min; w/o BTB: RMSE +3.9%, MAPE +7.3%; w/o Gating (simple concat): RMSE +2.6%, MAPE +5.4%.
- **Gaps/Limitations:**
  - Dataset covers only ~1 month (single season, summer Shenzhen); authors state reaching ~1% RMSE would require **longer-term, multi-season datasets**, **exogenous variables (weather conditions, traffic flow)**, and finer temporal resolution.
  - Future work: incorporate external data sources (weather, traffic flow); develop lighter-weight models for real-time scheduling and edge computing; extend evaluation to seasonal effects and cross-seasonal generalization.
  - Evaluation limited to very short horizons (≤45 min) with 247 aggregated region nodes rather than individual stations; no probabilistic/uncertainty quantification; GMAN appears in efficiency Table 3 but not in accuracy Table 1 (baseline list inconsistency).

### 2026_EnergyMamba_Graph_Mamba_ASCQR
**EnergyMamba: An Uncertainty-Aware Graph-Enhanced Selective State Space Model for Energy Consumption Prediction**  
Yu et al. · ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '26) · 2026
<https://doi.org/10.1145/3770855.3818841>
**Models**: EnergyMamba, AS_CQR, Mamba_SSM, GCN, PatchTST, Transformer, LSTM  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, RMSE, MPIW, Interval_Score, PICP  
**Data**: Florida_CBG_Smart_Meter; NYISO; CAISO  
**Features**: Historical_Load

- **What they did:**
  - Reformulates energy-consumption prediction as an **uncertainty-aware spatiotemporal** task (not a purely temporal one): spatial dependencies among Census Block Groups (CBGs)/grid zones are explicitly modeled via grid-topology graphs.
  - Proposes **GE-Mamba**: GCN-extracted spatial context injected into the selective-scan dynamics of a **bidirectional Mamba** (Mamba_SSM) organized in a U-Net encoder–decoder for multi-scale temporal modeling.
  - Proposes **AS-CQR** (AS_CQR): Adaptive Sequential Conformalized Quantile Regression with locally adaptive nonconformity normalization + online feedback calibration of the target quantile level for non-stationary/extreme-event conditions.
  - Empirically beats 15 SOTA baselines on four real-world datasets (~5% accuracy, ~6% UQ improvement over the best baseline).
- **Method core:** Model Type: **GE-Mamba** = per-time-step GCN (learnable surrogate for power-flow/Kirchhoff propagation) whose output conditions the input-dependent B, C, Δ of a selective SSM; blocks stacked in a U-Net (S=2 stages, K=2 blocks/stage, D=64, state dim D_s=16, expansion 2); skip connections preserve spikes; three linear heads output median/lower/upper quantiles. **AS-CQR** wraps …
- **Key results:**
  - Overall (Table 1): best on nearly all metrics on all four datasets; ≈5% lower MAE and ≈6% better IS vs the best baseline averaged over datasets; achieves ≥90% target coverage (COV ✓) everywhere.
  - Florida 1: MAE 36.57 / RMSE 61.06 / MPIW 122.51 / IS 231.86 (best baseline ST-LLM: 38.49 / 64.27 / 134.28 / 246.66).
  - Florida 2: 32.42 / 52.66 / 107.83 / 198.23 (ST-LLM: 34.12 / 55.42 / 114.71 / 210.64).
- **Gaps/Limitations:**
  - **Domain granularity**: regional/building-aggregate energy consumption (CBGs, ISO zones) — NOT EV-charging-station-level forecasting; no plug-in/session dynamics, no SOC or user behavior. Direct transfer to EV station loads is untested.
  - Authors' own limitation (Sec. 8): graph edges are geographic-proximity proxies; physical grid topology is not modeled (future work: true topology + adaptive graph learning).
  - No monotonicity/exogeneity guarantees à la PICNN: intervals come from quantile heads + post-hoc conformal wrapper, so there is no structural constraint linking covariates to interval width; also no cross-attention exogenous fusion at all (univariate inputs).
  - Static vs adaptive calibration: standard CQR (exchangeability-assuming, static Q) fails coverage under distribution shift (their ablation); AS-CQR fixes this online but only via scalar feedback γ(α − miss indicator) — window m and γ are fixed hyperparameters; no per-region/per-horizon adaptive learning rates.
  - Coverage guarantee is marginal long-run average (Eq. 25), not finite-sample per-step conditional coverage.

### 2026_FlowState_Sampling_Rate_Equivariant_Forecasting
**FlowState: Sampling-Rate-Equivariant Time-Series Forecasting**  
Graf et al. · Proceedings of the 43rd International Conference on Machine Learning (ICML 2026), PMLR 306 · 2026
<https://arxiv.org/abs/2508.05287>
**Models**: FlowState, Mamba_SSM, S5, HiPPO, TimesFM, Chronos, Chronos-Bolt, Moirai, TiRex, TTM, PatchTST, DLinear  
**Horizon**: Short_Term_Forecasting / Long_Term_Forecasting / Continuous_Horizon  
**Metrics**: MASE, CRPS, WQL  
**Data**: GIFT-Eval; Chronos_Corpus; KernelSynth; Electricity_ECL; Solar_Dataset; Weather; ETT  
**Features**: Historical_Load, Continuous_Time_Basis, Legendre_Polynomials, Dynamic_Covariates

- **What they did:**
  - **Core Problem**: Existing time series foundation models (TSFMs) based on Transformers, patch tokenizers, or discrete RNNs are inherently fixed to discrete grids. They lack adaptability to different or unseen sampling rates (e.g., predicting 15-min data from 1-hour context), struggle with varying context and target lengths, and incur high computational and memory costs.
  - **Primary Novel Contribution**: 1. **FlowState Architecture**: Introduces FlowState, a continuous-time foundation model pairing a State Space Model (**S5-based SSM encoder**) with a novel **Functional Basis Decoder (FBD)** using orthogonal Legendre polynomials (and Fourier bases). 2. **Sampling-Rate Equivariance**: By adjusting continuous discretization scaling factors ($s_{\Delta_E}, s_{\Delta_F}$), FlowState …
- **Method core:** FlowState comprises $N=12$ S5 layers with gating and MLPs, followed by the Functional Basis Decoder (FBD). It operates directly on raw unpatched points without quantization or tokenization. **Eq. 1 — S5 Block State Transition & Output**:  \begin{aligned} s_t^l &= \bar{A}_l s_{t-1}^l + \bar{B}_l x_t^{l-1} \\ c_t^l &= \bar{C}_l s_t^l \\ o_t^l &= c_t^l \odot \sigma(W_l c_t^l + …
- **Key results:**
  - **FlowState-18.6M (Context 4k)**: **MASE 0.706**, **CRPS 0.442** (Rank 1 Overall).
  - **FlowState-3M (Context 4k)**: **MASE 0.718**, **CRPS 0.446** (Rank 2 Overall).
  - **TimesFM-2.5 (500M)**: MASE 0.724, CRPS 0.468.
- **Gaps/Limitations:**
  - 1. **Polynomial Truncation Error**: Truncating Legendre polynomials to $K$ basis terms limits extremely high-frequency oscillation representation beyond degree $K$. 2. **Channel-Independent Univariate Processing**: Multivariate series are handled by mapping each variate independently, omitting spatial cross-channel correlations. 3. **Application to EV Charging Stations**: Highly suited for multi-resolution EV …

### 2026_INLA_Spatio_Temporal_EV_Demand
**Spatio-Temporal Modelling of Electric Vehicle Charging Demand**  
Bouaachra et al. · arXiv preprint (arXiv:2604.19841) · 2026
<https://arxiv.org/abs/2604.19841>
**Models**: INLA_Latent_Gaussian_Model (proposed-new; SPDE–RW2 and ICAR–RW2 variants), XGBoost (station-level baseline), Poisson GLM (station-level baseline)  
**Horizon**: day-ahead daily session counts  
**Metrics**: MAE, RMSE, MAPE, WAIC/DIC  
**Data**: ChargePlace_Scotland (proposed-new, open benchmark Oct 2022 – Apr 2025)  
**Features**: spatial coordinates (lon/lat, British National Grid), weather covariates (temperature splines, humidity, wind speed via riem package), tariff status free/paid (time-varying), charger type (AC vs Rapid/Ultra-Rapid), public/private access, …

- **What they did:**
  - Two-part contribution: 1. **New open benchmark dataset**: large-scale longitudinal EV charging dataset from Scotland (October 2022 – April 2025), released openly via ChargePlace Scotland with a reproducible preprocessing pipeline (cleaning, enrichment, spatial indexing). Explicitly positioned as a **modern replacement for stale legacy benchmarks such as Palo Alto (2020)** that "fail to reflect the scale and …
- **Method core:** **Observation model** (daily session counts $y_{i,t}$ at charge point $i$, day $t$), Poisson likelihood with log link (Eqs. 1–3):  y_{i,t} \mid \mu_{i,t} \sim \text{Poisson}(\mu_{i,t})   \mu_{i,t} = \exp(\eta_{i,t})   \eta_{i,t} = \alpha + \sum_{k=1}^{K} \beta_k x_k(i,t) + f_{space}(i) + f_{time}(t) 
- **Key results:**
  - **Model fit (in-sample)**: ICAR–RW2 slightly better than SPDE–RW2 — ICAR: DIC = 136,562.8, WAIC = 136,509.1; SPDE: DIC = 136,941.3, WAIC = 136,909.1. Posterior fixed effects consistent across both.
  - **Key drivers**: Rapid connector strongest positive effect (ICAR $\hat\beta$=0.872, CI [0.599, 1.146]; SPDE 0.914 [0.819, 1.008]); public access (+0.321/+0.350); free charging (+0.146/+0.142); Sunday largest negative day effect (−0.063/−0.066); only temperature spline 1 credibly negative among weather covariates …
  - **MAE**: 70.1% (ICAR vs GLM), **77%** (ICAR vs XGBoost), 72.4% (SPDE vs GLM), 73.6% (SPDE vs XGBoost) ⇒ **70–77% dominance**, tighter error distributions.
- **Gaps/Limitations:**
  - **Session counts, not kWh load or peak power** — energy/power modelling flagged as future work needing heavier-tailed likelihoods.
  - Day-level aggregation; Poisson likelihood imperfect under observed over-/under-dispersion (Negative Binomial suggested).
  - Case study limited to dense central Glasgow — generalisation to sparse Scottish regions unclear; CPS network may not represent private/workplace charging.
  - **Proposed future directions**: scaling to all of Scotland; hierarchical multi-scale forecasting (CPID → neighbourhood → local authority, coherent across aggregations); **hybrid two-stage INLA–ML pipeline** — XGBoost first stage for nonlinear covariate interactions, INLA second stage on its residuals (following Hu et al. 2026, "XGBoost meets INLA", wildfire forecasting) — directly relevant to thesis hybrid-model …

### 2026_Lyapunov_EV_Scheduling
**Forecast-Enhanced Lyapunov Optimization for Real-Time EV Charging Scheduling**  
Huang et al. · arXiv preprint arXiv:2604.16873 [math.OC] · 2026
<https://arxiv.org/abs/2604.16873>
**Models**: Forecast-Enhanced Lyapunov Optimization, RHC, Queuing_Model, Linear_Programming, MPC (benchmark)  
**Horizon**: Short_Term_Forecasting  
**Metrics**: Total_Cost, Unit_Cost_USD_per_kWh, Maximum_Charging_Delay, Optimality_Gap, Computational_Time  
**Data**: Shanghai_EV_Arrival_Data; CAISO  
**Features**: EV_Arrival_Rate, Electricity_Tariff, Arrival_Departure_Time, EV_Charging_Demand, Charging_Power

- **What they did:**
  - **First work to incorporate short-term forecasts into the Lyapunov optimization framework** for online EV charging scheduling, overcoming the myopia of prediction-free Lyapunov methods while retaining rigorous theoretical guarantees.
  - Novel **forecast-integrated virtual queue design** ($q_g$, $z_g$) embedded in a MPC framework; extended with **heterogeneous penalty parameters** $V_g$ per EV group to shrink the optimality gap.
  - Proves charging delay upper bound $O(w)$ and optimality gap bound $O(1/(wV))$ — both improving with lookahead window length $w$.
  - Case study (100 EVs, real Shanghai arrivals + CAISO prices): A1 reaches within **1% of offline optimal cost**, vs 46% for homogeneous-penalty A2; both beat MPC and greedy.
- **Method core:** Available charging window $U_v \triangleq \{T_v^a,\dots,T_v^d-1\}$; instantaneous cost:  f(t) \triangleq \pi(t) \sum_{v\in S} p_v(t)   \text{P1:} \quad \min \frac{1}{T}\sum_{t=1}^{T} f(t) \quad \text{s.t. } 0\le p_v(t)\le P_v\ (\forall t\in U_v),\; p_v(t)=0\ (\forall t\notin U_v),\; E_v^{req}\le \eta\Delta t \sum_{t=1}^T p_v(t)\le E_v^{max}  EVs grouped so $|U_v|=R_g$; …
- **Key results:**
  - Cost & delay comparison (Table II, 100 EVs, MPC at $w=12$):
  - A1 cost gap only **1%** vs offline; A2 gap **46%**; both below theoretical bounds.
  - Delay bounds validated empirically for $w=1,2,5,8,12$: e.g., average max delay grows 1.19→2.63 h (all under bound (18)).
- **Gaps/Limitations:**
  - Assumes i.i.d. prices/arrivals/energy demands for P4; forecasts assumed accurate inside window (only Gaussian-noise robustness test).
  - Grouping by parking time is an aggregation approximation; per-EV disaggregation via FIFO may be suboptimal.
  - Single-station scope; no network constraints, transformer limits, or renewable co-optimization; V2G explicitly left to future work.
  - Heterogeneous penalty (A1) requires careful per-group tuning of $V_g$ and degrades under forecast error.
  - Gap for thesis: the framework consumes generic short-term load/price forecasts — coupling probabilistic forecasters (TimeGrad, Temporal_Fusion_Transformer) with uncertainty-aware Lyapunov control is unexplored.

### 2026_MFT_Multi_Scale_Fusion_Transformer
**Multi-scale fusion transformer for EV charging station load prediction**  
Liu et al. · Scientific Reports (Nature Portfolio), vol. 16, art. 8609 · 2026
<https://doi.org/10.1038/s41598-026-38562-z>
**Models**: MFT, Transformer, LSTM, BiLSTM, GRU  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, RMSE, MAE  
**Data**: Norway_Residential_EV_Charging_Dataset  
**Features**: Historical_Load, Weather_Features, Traffic_Density, Scale_Mask, Positional_Encoding

- **What they did:**
  - EV charging station load prediction is challenged by stochastic charging behavior and complex external influences (weather, traffic). Existing deep models fail to capture **multi-scale temporal dependency** and underuse the **dynamic influence of external factors**; statistical methods (SARIMA, RF, GBRT, Monte Carlo) miss nonlinear evolution.
  - Proposes **MFT** (Multi-scale Fusion Transformer) combining three modules: 1. **3M** — Multi-scale Modeling Mechanism: predefined *scale masks* constrain each attention head to model temporal dependency at a distinct granularity in parallel (fine-to-coarse), extending the padding-mask mechanism of multi-head attention. 2. **FAM** — Feature-correlation Analysis Module: Pearson Correlation Coefficient (PCC) analysis …
  - Up to **25.59% average performance improvement** over competitors, with gains growing monotonically with horizon — strongest for long-term prediction.
- **Method core:** **Input embedding + positional encoding**: load sequence $l \in \mathbb{R}^{T_h\times 1}$ projected by MLP $\eta$ into high-dimensional space; sinusoidal positional encoding:   p_t(2q) = \sin(t/10000^{2q/d_{\text{model}}}), \quad p_t(2q+1) = \cos(t/10000^{2q/d_{\text{model}}}) \tag{2}  
- **Key results:**
  - Average gains over competitors: 26.54% (GRU), 21.88% (LSTM), 12.85% (BiLSTM), 10.79% (Transformer); by metric: MSE 23.73%, RMSE 12.58%, MAE 17.73%.
  - Improvements grow monotonically with horizon (MSE: 17.30%/19.14%/22.69%/**35.78%** at 24/48/72/96 h) — best exactly where baselines degrade most.
  - Incremental ablation (TF → MT(+3M) → MFT(+MFM)): 3M yields 6.27%/3.19%/3.86% (MSE/RMSE/MAE); MFM adds 6.42%/3.34%/5.49%. At long horizons (K=72, 96) MFM's contribution exceeds 3M's (e.g., 9.73% vs 3.48% at K=96), indicating weather/traffic dominate long-term behavior.
- **Gaps/Limitations:**
  - Dataset is a single Norwegian residential area; station/session counts and public provenance are not fully specified (only a GitHub mirror link provided).
  - Weather features only at daily resolution (assumed stable within a day) — limits fine-grained weather response modeling.
  - Scale masks are predefined rather than learned; number of heads fixes the scale set.
  - Authors' future work: incorporate battery-related factors (charging/discharging influenced by battery characteristics) to further improve accuracy.
  - Baselines limited to classic RNN/Transformer family; no comparison against modern SSM/Mamba or specialized long-horizon forecasters.

### 2026_ML_Comparison_EV_Charging_Forecasting
**Electric Vehicle Charging Load Forecasting: An Experimental Comparison of Machine Learning Methods**  
Kyriakopoulos et al. · arXiv preprint arXiv:2512.17257 [cs.LG] (v2, 31 Mar 2026; dated April 1, 2026), … · 2026
<https://doi.org/10.48550/arXiv.2512.17257>
**Models**: ARIMA, XGBoost, GRU, LSTM, Transformer  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, RMSE  
**Data**: Palo_Alto_EV; Boulder_Colorado; Dundee_EV; Perth_EV  
**Features**: Historical_Load, Calendar_Features, Holiday_Indicator, Calendar_Features, Calendar_Features, Calendar_Features, Station_ID_One_Hot, Region_ID_One_Hot

- **What they did:**
  - A systematic, reproducible experimental benchmark — not a new model — comparing five forecasting families (**ARIMA**, **XGBoost**, **GRU**, **LSTM**, **Transformer**) for EV charging energy consumption (kWh) across:
  - **Three temporal resolutions**: short-term (10–30 min ahead, 10-min steps), mid-term (2–8 h ahead, 2-h steps), long-term (1–5 days ahead, 1-day steps);
  - **Three spatial aggregation levels**: station, region, city;
  - **Four real-world datasets**: Palo Alto (USA), Boulder (USA), Dundee (UK), Perth (Australia). Contributions: (i) unified multi-scale EV charging benchmark; (ii) consistent/reproducible evaluation protocol with public codebase and dataset links; (iii) systematic comparison showing model rankings change with horizon and spatial scale; (iv) family-level insights — Transformers dominate short-term regional/city …
- **Method core:** **Problem formulation (EV Charging Load Forecasting Problem):**  X = \{x_1, x_2, \ldots, x_T\}  where $x_t$ is total energy consumed at step $t$; the goal is to predict:  \hat{X} = \{\hat{x}_{T+1}, \hat{x}_{T+2}, \ldots, \hat{x}_{T+H}\}  over forecasting horizon $H$ (minutes / hours / days regimes). **Two modeling strategies:** 1. **Multi-station (global) learning** for …
- **Key results:**
  - All values are MAE/RMSE in the normalized domain (Tables 2–4 of the paper). Key findings: **Short-term (10–30 min):**
  - Perth: LSTM best everywhere (station MAE 0.43–0.46, RMSE < 1.1; e.g., city MAE 7.97@10min → 7.27@30min vs Transformer 42.94 → 42.90).
  - Boulder: Transformer best at all levels (station MAE ≈ 0.21 vs ARIMA 0.26; city MAE 2.71→2.65).
- **Gaps/Limitations:**
  - Input space deliberately restricted to historical load + calendar features; exogenous drivers (weather, electricity prices, traffic, events) unmodeled → reported scores are a **lower bound**.
  - Only widely used baselines; excludes GNNs, decomposition hybrids, EV-specific global/foundation models ([29][30] reviewed only) ↔ benchmark positioning against 2024_EV_Load_Forecasting_DAM, 2025_Benchmark_Foundation_Models, 2026_ML_Geographical_Transferability_EV.
  - Recursive multi-step forecasting introduces error accumulation, hurting some architectures (Transformers on sparse data like Dundee) disproportionately.
  - Fixed hyperparameters trade peak performance for comparability.
  - Future work: hyperparameter optimization/deeper architectures; exogenous variables; explainable AI (XAI); transfer learning across cities (explicitly proposed as follow-up, connecting to 2024_MQ_TCN_Transfer_Learning_EV, 2023_MetaProbformer_EV_Load).

### 2026_ML_Geographical_Transferability_EV
**Machine learning approaches to short-term electric vehicle charging demand prediction: Applicability and geographical transferability**  
Wang et al. · Journal of Energy Storage · 2026
<https://doi.org/10.1016/j.est.2026.122141>
**Models**: SGD, Random_Forest, Lasso, LSTM, MLP, GRU  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, MAPE  
**Data**: Perth_EV; Dundee_EV; Hong_Kong_EV_Charging_Dataset; Palo_Alto_EV; Boulder_Colorado  
**Features**: Historical_Load, Sliding_Window_Lags, EV_Charging_Demand

- **What they did:**
  - **Objective:** Benchmark six popular ML methods (three traditional ML + three deep learning) for **station-level, 1-hour-ahead** EV_Charging_Demand prediction across **12 real-world cities** in China, the UK and the USA, and examine their **geographical transferability** (can a model trained on city A predict city B with little/no local data?).
  - **Contributions:** 1. First systematic station-level comparison of ML/DL methods for short-term (hourly) EV charging demand at small temporal resolution across many scenarios (stations range 1–27 per city; 5.5–29.4 charging events/day/station). 2. Explicit evaluation of geographical transferability via a pre-train → parameter-copy → fine-tune/test protocol (zero-shot T=0 or few-shot T≤11 h adaptation). 3. Three key …
  - Deliberately *not* a new architecture: a practical applicability/transferability benchmark.
- **Method core:** Input: source dataset $D_s=\{(x_i^{(s)},y_i^{(s)})\}_{i=1}^{N_s}$, target dataset $D_t$, architecture $f_\theta$, adaptation length $T\in\{0,1,2,\dots,11\}$ hours.
- **Key results:**
  - **Applicability (same-city train/test):** By MAE, LSTM, GRU, RF and SGD beat MLP and LASSO; by MAPE the three traditional ML methods (especially SGD and RF) were better. **SGD was best overall on both metrics** across the 12 cities. Group-High demand cities → lower MAPE but higher MAE; LSTM/GRU/RF/SGD best in …
  - **Training-length analysis:** performance improves with training length up to **3 days (~72 h)**, then plateaus for all six models and all cities → only 3 days of session data needed for near-optimal accuracy.
- **Gaps/Limitations:**
  - Only univariate historical-demand inputs — no spatial/urban features (distances to nearby stations, station density, land use, POIs), weather, or calendar indicators.
  - Single-hour horizon only; multi-hour-ahead (1–3 h) extension needed for operational planning.
  - Underlying drivers of cross-city transferability (urban structure, socioeconomic profiles, user behavior similarity) unexplained — planned investigation via city-level metadata.
  - Future work: extend benchmark to emerging architectures (**Transformers**, TCNs), expand datasets, add weekday/weekend/holiday/time-of-day context features.
  - Only 30 days of data per city; short windows may not capture seasonality.

### 2026_Mamba_3_Sequence_Modeling
**Mamba-3: Improved Sequence Modeling using State Space Principles**  
Lahoti et al. · arXiv preprint (arXiv:2603.15569); CMU / Princeton / Together AI / Cartesia AI · 2026
<https://arxiv.org/abs/2603.15569>
**Models**: Mamba-3, Mamba_SSM, Mamba_SSM, Gated_DeltaNet, Transformer, S4  
**Metrics**: Perplexity, Accuracy, Decode_Latency, Arithmetic_Intensity  
**Data**: FineWeb-Edu; LAMBADA; HellaSwag; PIQA; ARC; WinoGrande; OpenBookQA; RULER_NIAH  
**Features**: Text_Tokens

- **What they did:**
  - From an **inference-first** perspective: sub-quadratic linear models (SSMs, linear attention) have constant memory/linear compute but trade off model quality and state-tracking capability for efficiency (e.g., Mamba-2 fails parity), and their decoding algorithms are memory-bound with low arithmetic intensity (~2.5 ops/byte vs ~295 for bf16 matmul on H100).
  - **Mamba-3** introduces three SSM-principled improvements: (1) **exponential-trapezoidal discretization** → more expressive recurrence that acts as an implicit width-2 convolution inside the core recurrence, obviating the short causal conv; (2) **complex-valued state transitions**, implemented efficiently via *data-dependent RoPE*, restoring rotational dynamics needed for state tracking (TC0 tasks like parity); (3) …
  - Results: at 1.5B scale, +0.6 avg downstream accuracy over GDN (SISO) and +1.8 total with MIMO; matches Mamba-2 perplexity with half the state size. Code/kernels: https://github.com/state-spaces/mamba
- **Method core:** **Architecture**: Llama-style alternating Mamba-3 + SwiGLU blocks, pre-norm; adds BC/QK RMSNorm after $B,C$ projections (removes post-gate RMSNorm in pure models; reintroduced pre-gate grouped RMSNorm for hybrid long-context extrapolation), learnable head-specific channel-wise $B,C$ biases, no short causal conv.
- **Key results:**
  - **Downstream average accuracy** (100B FineWeb-Edu): Mamba-3-SISO beats all baselines at every scale (43.4 vs GDN 43.2 @180M; 49.8 vs 49.7 @440M; 54.4 vs 53.7 @880M; **56.4 vs GDN 55.8, Transformer 55.4 @1.5B**). MIMO ($R=4$) adds ~+1.2 pts over SISO (**57.6 @1.5B**; +2.2 over Transformer, +1.9 over Mamba-2, +1.8 over …
  - **State-size Pareto**: Mamba-3 MIMO at $d_{\text{state}}=64$ matches Mamba-2 at $d_{\text{state}}=128$ → same quality at half decode latency; downward Pareto shift also vs GDN.
  - **State tracking** (scaled acc): Parity 100.00 / Arith w/o brackets 98.51 / w/ brackets 87.75 for Mamba-3 vs Mamba-3 w/o RoPE 2.27/1.49/0.72, standard-RoPE 1.56/20.70/2.62, Mamba-2 0.90/47.81/0.88; competitive with state-tracking-enabled GDN [-1,1] (100/99.25/93.50).
- **Gaps/Limitations:**
  - Fixed-state linear models remain weak at extracting information from semi-structured/unstructured data (SWDE, FDA) versus exact attention; hybrids with interleaved self-attention are needed to close long-context retrieval gaps.
  - Ideal norm type/placement for hybrids (grouped vs default RMS, pre- vs post-gate) involves unintuitive competing tradeoffs.
  - Second-order error bound of trapezoidal rule only holds if $\lambda_t=\frac{1}{2}+O(\Delta_t)$, which empirically is *not* enforced (learned $\sigma(u_t)$ performs better) — theory-practice gap.
  - MIMO training costs up to $R\times$ more FLOPs (moderate prefill overhead); vehicle-as-channel-style reuse at ranks far beyond validated $R\in\{4,8,16\}$ carries no quality guarantees (as noted by downstream users).

### 2026_Mamba_KAN_HyKANet_EV
**When Mamba Meets KAN: A Hybrid Learning Network for Electric Vehicle Charging Demand Prediction**  
Hao et al. · ICASSP 2026 (IEEE International Conference on Acoustics, Speech and Signal Processing), … · 2026
<https://doi.org/10.1109/ICASSP55912.2026.11461366>
**Models**: HyKANet, Mamba_SSM, Mamba_SSM, KAN, PAG, FourierGNN, AST-GAT, DCRNN, STGCN  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAE, MAPE, RAE  
**Data**: Real_World_EV_DC_Charging  
**Features**: Historical_Demand, Weather, Calendar_Features, Electricity_Tariff, Adjacency_Matrix

- **What they did:**
  - EV charging demand forecasting must jointly capture (i) local + global spatial dependencies between stations, (ii) multi-scale temporal dynamics, and (iii) heterogeneous contextual signals (weather, calendar, pricing). Prior work either ignores spatial structure (LSTM with weather/calendar [4]), relies on static graphs (ASTGCN [6]), or underuses recent physics-informed graph learning and Transformer spatiotemporal …
  - Proposes **HyKANet** (Hybrid Mamba-KAN Network): a unified graph-temporal framework with (i) a Graph-aware MambaBlock embedding spatial topology into long-range temporal modeling, (ii) **HydraMamba**, a multi-scale routing module with three parallel Mamba branches (short/medium/long-term) plus dynamic graph learning, (iii) factor-wise external encoding with bidirectional cross-attention fusion, and (iv) a KAN …
- **Method core:** **Problem definition**: charging network as undirected graph $\mathcal{G} = (\mathcal{V}, \mathcal{E}, \mathcal{A})$ with $N$ stations; static physical adjacency $A_{\text{phy}} \in \mathbb{R}^{N\times N}$ and learned dynamic adjacency $A_{\text{dyn}}$ from node embeddings; input $X = (X_1,\dots,X_P) \in \mathbb{R}^{P\times N\times C}$, external factors $E_P = …
- **Key results:**
  - Best average across 15–60 min horizons: **RMSE 4.67, MAPE 15.33, RAE 17.86, MAE 2.49** (×10² units).
  - Per-horizon RMSE: 2.81 (15min), 4.47 (30min), 5.26 (45min), 6.12 (60min). vs best baseline PAG: 3.02/5.16/6.52/7.21 (avg 5.48) → up to **14.8% RMSE improvement** and 17.3% over FourierGNN (5.65); **MAE reduced 12.2% on average** (2.49 vs PAG 3.33). MAPE 15.33 vs PAG 16.87.
  - Baselines beaten: FCNN (6.37), LSTM (6.70), GCN (6.76), GAT (6.36), GCN-LSTM (5.81), STGCN (6.20), HSTGCN (6.39), DCRNN (5.93), AST-GAT (5.73), FourierGNN (5.65), PAG (5.48) average RMSE.
- **Gaps/Limitations:**
  - Only short-term horizons evaluated (15–60 min); extrapolation of the KAN decoder to day-ahead horizons untested.
  - Dataset not named or released; no comparison against other Mamba/KAN-based forecasting models.
  - Dynamic adjacency learning may scale poorly to very large station networks.
  - Self-supervised/meta-learning appear only in index terms, not developed in the method.

### 2026_MetaLearning_Informer_Probabilistic_EV
**Probabilistic computing forecasting approach for EV charging load forecasting using meta-learning enhanced informer**  
Singh et al. · Applied Soft Computing · 2026
<https://doi.org/10.1016/j.asoc.2026.115869>
**Models**: MAML-Informer, Informer, MAML, Transformer, LSTM, SVR, Reptile, LSTM-Informer, LSTM_Transformer  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAE, MSE, CRPS, PICP, MPIW, Pinball_Loss, Winkler_Score, Pinball_Loss  
**Data**: Caltech_ACN; Boulder_Colorado; Palo_Alto_EV  
**Features**: Historical_Load, Weather_Features, Calendar_Features, Token_Embeddings, ProbSparse_Attention

- **What they did:**
  - Propose **MAML-Informer**: a MAML (MAML)-enhanced Informer for **multi-horizon point + probabilistic** EV charging load forecasting under sparse, heterogeneous, non-stationary data (e.g., newly commissioned stations). Each charging station is treated as a meta-learning task; the model first learns common charging-demand patterns across station clusters, then adapts quickly with few gradient steps. Contributions: 1. …
- **Method core:** **Problem formulation** — net load series per station $i$ (Eq. 1): $\{P_{i,t}\},\ t=1,\dots,T$. Training set (Eq. 2): $\mathcal{T} = \{\Theta_t, y_{t+1}\}_{t=1}^{T}$ where $\Theta_t$ is the input feature vector (historical load + meteorological data + temporal indices). Mapping (Eq. 3): $y_{t+1} = g(\Theta_t)$. Dual-dataset design: primary set $\mathcal{T}$ trains the …
- **Key results:**
  - **Point forecasting (Table 4)** — MAML-Informer lowest RMSE & MAE on all three datasets: (*ACN SVM row prints MAE/RMSE columns swapped in source table; best overall reported as MSE 0.009, RMSE 0.095.) **Probabilistic forecasting (Table 5)**:
  - Headline gains: up to **51.21% lower RMSE$_{Q50}$** (vs SVR, Boulder), **12.53–12.98% lower RMSE$_{Q90}$**, up to **48% CRPS reduction**, ~17% PICP rise; PICP ≈100% (ACN 99.82%) with narrow MPIW ≈0.148–0.164 kWh; CRPS 0.065 (ACN), 0.023 (Boulder), 0.025 (Palo Alto) in Fig. 10 reporting.
  - **Few-shot ablation (10% training data)** vs vanilla Informer: RMSE$_{Q50}$ cut by **36.5% (ACN), 48.1% (Boulder), 42.4% (Palo Alto)** plus consistently lower CRPS → gains stem from meta-learned initialization, not capacity.
- **Gaps/Limitations:**
  - Authors explicitly scope the work as methodological integration + empirical validation: **no formal convergence analysis of MAML optimization** nor theoretical treatment of Informer sparsity.
  - Gaussian likelihood assumption may misfit multimodal/spiky charging distributions (quantile metrics used as robustness check).
  - Meta-training adds ~30% training-time overhead; future work: reducing meta-training complexity, event-aware forecasting strategies.
  - Absolute MAE/RMSE margins over strong baselines are modest; superiority argued primarily through probabilistic metrics and few-shot ablations.
  - Experiments in MATLAB R2022b on CPU (i7-13700, 32 GB RAM); distributed/high-performance claims not benchmarked on GPU-scale hardware in detail.

### 2026_Moirai_2_When_Less_Is_More
**Moirai 2.0: When Less Is More for Time Series Forecasting**  
Liu et al. · arXiv preprint arXiv:2511.11698v3 [cs.LG] — Salesforce AI Research (2026-02-04) · 2026
<https://arxiv.org/abs/2511.11698>
**Models**: Moirai, Moirai_MoE, Transformer, Chronos, Chronos-2, Chronos-Bolt, TimesFM, Toto, TiRex, FlowState, Sundial, TabPFN-TS, PatchTST, TTM, Lag-Llama  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MASE, CRPS, WQL  
**Data**: GIFT-Eval; GIFT_Eval_Pretrain; Chronos_Corpus; KernelSynth; Salesforce_Internal_Telemetry  
**Features**: Historical_Load

- **What they did:**
  - **Research gap**: Scaling time series foundation models (TSFMs) has been ad hoc — Moirai 1.0's masked-encoder design wastes data (1 loss per sampled config, ~15% tokens in loss), multi-patch sizes complicate training, and mixture-of-distributions output adds complexity yet underperforms empirically. Parameter scaling without matched data scaling does not reliably improve GIFT-Eval scores across families.
  - **Core contribution — Moirai 2.0 (small 11.4M / base 87.1M / large 305M)**: A refined decoder-only patched Transformer that pairs **quantile forecasting with multi-token prediction** and is trained on a newly curated **36M series / ~295B observations** corpus — the main empirical message is *less complexity is more*.
  - **Three pillars**: 1. **Architecture simplification**: Decoder-only causal Transformer (from masked encoder), single patch size (from multi-patch), and **quantile loss** (from distribution NLL) with a residual-block output projection `R^d → R^{n_token × n_q × p}` (`n_q=9`). 2. **Training/inference strategies**: Patch-level random masking (50% patches), statistical anomaly filtering (§3.2), **recursive multi-quantile …
  - **Empirical claim**: On **GIFT-Eval (97 tasks, 55 datasets)** Moirai 2.0 small **ranks 5th (MASE) / 6th (CRPS)** among 37 pretrained FMs (Fig. 2 normalized geometric mean), beating Moirai 1.0-Large while being **≈30× smaller and 2× faster**; ablations show decoder-only + quantile loss + recursive decoding drive most gains (Table 2). Scaling the same Moirai 2.0 to base/large on this corpus **does not help** (Table 1) …
- **Method core:** **Model Type**: Decoder-only patched Transformer for univariate series (multivariate via independent channels). Pipeline (Fig. 1): Instance normalization (stats from first 30% only to avoid leakage) → Non-overlapping patching with missing indicator `m_i` concatenated `x̂_i = x_i || m_i` → Input residual projection → Stacked causal Transformer decoders (RMSNorm, self-attention, …
- **Key results:**
  - **GIFT-Eval overall (Fig. 2 normalized geometric mean; 30 FMs, zero-shot, pretrained only; lower is better)** — Moirai 2.0 small ranks **5th MASE / 6th CRPS** among 37 foundation models (incl. size variants); substantially above Moirai-Large despite fewer params:
  - Normalized MASE (geometric mean ÷ seasonal naive; Fig. 2 left): leaders Chronos-2 / TimesFM-2.5 / TiRex / FlowState-9.1M / granite-flowstate-r1 / **Moirai 2.0** before Kairos/Toto/Sundial/TabPFN-TS/YingLong etc.; exact values from replication code at …
  - Normalized CRPS (geometric mean; Fig. 2 right): same ordering; Moirai 2.0 6th overall.
- **Gaps/Limitations:**
  - **No multivariate / covariate support**: Dropped in 2.0 due to limited high-quality covariate data; multivariate tasks treated as independent univariate — sparse, spiky EV regimes (arrival/departure, SoC, tariff, weather) not modeled jointly; future via synthetic causal data prior (§6, cf. Chronos-2 [3] approach).
  - **Negative scaling on current corpus**: Base (87M) / Large (305M) underperform Small (11.4M) on same 36M/295B data (Table 1) → architecture-data mismatch; data scale/diversity must grow with params.
  - **Long-horizon degradation**: Rank 8th on long horizons vs 4th short (Fig. 4); multi-token + recursive decoding mitigate but do not close gap — architectural innovation and data scaling needed.
  - **Domain gap — Nature tasks**: Pretraining underrepresents natural/environmental series → weakest domain (Fig. 3); transport highly competitive suggests uneven domain utility.
  - **Probabilistic limited to 9 quantiles**: Fixed `Q={0.1,…,0.9}` (equal-weighted) — no continuous sampling, no tail beyond 0.1/0.9 unless reweighted `w_q`; weighted variant mentioned but not evaluated.
  - **Operationalization**: Agentic (LLM+time-series reasoning) and multimodal (text+image+series) future work highlighted; incident reasoning (cf. ARFBench) not addressed.
  - **Domain gap for EV load**: No EV charging datasets (ACN, ElaadNL, Boulder, Pecan Street) evaluated — transfer to sparse, bursty EV loads unproven; covariate-free design is an open thesis gap.
  - **Replication**: Results anchored to `gift-eval` replication code + Hugging Face release; internal telemetry not distributable (1.48B private obs).

### 2026_PC_M3_Mamba_EV_Clusters
**A Mamba State-Space Sequence Model for AI-Driven Dynamic Aggregation and Predictive Control of Electric Vehicle Clusters in Vehicle-to-Grid Energy Management**  
Tang et al. · Electronics (MDPI), vol. 15, art. 2380 · 2026
<https://doi.org/10.3390/electronics15112380>
**Models**: PC-M3, Mamba-3, Routing_Mamba, PowerMamba, Informer, Mamba_SSM, TD3, MPC  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: RMSE, Hausdorff_Distance, Polytope_Feasibility, Inference_Latency  
**Data**: Caltech_ACN; ACN-Sim; ElaadNL; NREL_dsgrid_TEMPO; NHTS_2009  
**Features**: State_of_Charge, Charging_Power, Arrival_Departure_Time, Arrival_Departure_Time, Energy_Requirement, Battery_Capacity, Pilot_Signal

- **What they did:**
  - Real-time EMS for large EV clusters needs both fast aggregate flexibility estimation and executable per-vehicle dispatch. Exact Minkowski-sum aggregation of per-vehicle feasibility polytopes scales super-polynomially in $N$; LP/MILP/MPC solve times explode online; learning-based aggregators treat constraints as soft penalties (3–15% session violations observed).
  - Proposes **PC-M3** (Physics-Constrained Mamba-3 MIMO Aggregator): an amortized, constraint-aware sequence model combining (i) a vehicle-as-channel Mamba-3 MIMO backbone, (ii) a history-dependent differentiable feasibility projection fused *inside* the recurrent state update, (iii) a sparse Routing_Mamba mixture-of-experts layer, and (iv) a consistency-trained aggregation–disaggregation closed loop. Scales AI-EMS …
- **Method core:** **Problem setup**: cluster of $N$ EVs over horizon $t \in \{1,\dots,T\}$ ($T=96$, $\Delta t = 15$ min); vehicle $i$ has arrival $a_i$, departure $d_i$, initial SoC $s_i^0$, energy requirement $E_i^{\text{req}}$, capacity $C_i$, rate limits $[\underline{p}_i, \bar{p}_i]$; SoC dynamics $s_{i,t+1} = s_{i,t} + (\eta_i p_{i,t}\Delta t)/C_i$. Output: envelope …
- **Key results:**
  - **Envelope approximation** (Hausdorff_Distance, % width-normalised, ACN-Data / ElaadNL zero-shot): PC-M3 **3.4 / 4.1** vs PowerMamba 9.7/11.2, Informer 11.8/14.6, Mamba-2+proj 10.4/12.1, Zonotope 13.2/15.9, LP outer bound 21.6/24.2. Envelope width 92.4% of true vs 118.3% (PowerMamba), 131.4% (Zonotope).
  - **10k-vehicle dsgrid-TEMPO stress test**: PC-M3 3.8% vs sandwich reference vs PowerMamba 10.6%, Informer 13.5%.
  - **Closed-loop tracking on ACN-Sim** (500 simulated days, 6200 sessions): tracking RMSE 0.82 MW (PC-M3) vs MPC 1.45 MW, TD3 1.78 MW, PowerMamba+proj 1.18 MW, uncoordinated 3.12 MW → 43% reduction vs strongest control baseline; **zero polytope violations** (structural, via in-loop clamp) across all evaluated sessions …
- **Gaps/Limitations:**
  - Differentiable projection relies on separable per-vehicle polytopes (one intertemporal energy constraint); shared-infrastructure coupling (DC fast-charging hubs) is an open problem.
  - Assumes arrival time and requested energy known at connection; mid-session revisions require re-running the projection.
  - Vehicle-as-channel use of Mamba-3 MIMO is far beyond validated rank range ($R \in \{4,8,16\}$ originally); no quality guarantees inherited at $N \gg 16$; claims limited to $N \le 10{,}000$; 100k-vehicle regime would need hierarchical routing/sparse MIMO decomposition.
  - Feasibility certified only relative to imputed polytopes (no true BMS data in ACN-Data/ElaadNL); validation on true vehicle-side measurements is next step.
  - Bidirectional V2G/G2V exercised only on synthetic dsgrid-TEMPO stress test (real corpora charge-only); future work: degradation co-optimisation head.

### 2026_SSM_Transformer_LSTM_Grid_Benchmark
**Benchmarking State Space Models, Transformers, and Recurrent Networks for US Grid Forecasting**  
Hong et al. · arXiv preprint (arXiv:2602.21415) · 2026
<https://arxiv.org/abs/2602.21415>
**Models**: S_Mamba, PowerMamba, PatchTST, iTransformer, LSTM  
**Horizon**: Long_Term_Forecasting  
**Metrics**: NRMSE (reported as normalized 'MSE %'), MAPE, MAE (nMAE for non-load tasks), signed-error tails P0.5/P99.5  
**Data**: EIA-930 hourly system load: CAISO, ISO-NE, MISO, PJM, ERCOT, NYISO (+ SWPP for weather experiments only)  
**Features**: Historical_Load, temporal embeddings (hour-of-day, day-of-week), Weather_Traffic, weather covariates: temperature, humidity, wind speed, GHI, cloud cover

- **What they did:**
  - First benchmark of SSM vs Transformer vs RNN architectures **across multiple US ISOs under identical protocols**. Five models — PowerMamba, S_Mamba, iTransformer, PatchTST, 2-layer bidirectional LSTM (~2.6M params) — on hourly EIA-930 demand from six ISOs (seven for weather), forecast windows W = 24–168 h. Three contributions: 1. **US Grid Benchmark** — consistent hyperparameters/preprocessing across grids; PatchTST …
- **Method core:** **Five architectures**: — **Architecture-matched weather fusion**: S-Mamba early summation into d_model before BiMamba stack; PowerMamba pre-decomposition fusion (routes weather variance to both trend/seasonal streams); PatchTST interleaved cross-attention (load patches query independently-patched weather patches); iTransformer weather as additional variate tokens; LSTM early per-timestep …
- **Key results:**
  - **Load-only (30 grid×window rows)** — Table IV macro averages: Grid split: PatchTST leads CAISO/MISO/ERCOT (regular diurnal shapes fit patch boundaries); SSMs lead ISO-NE/PJM/NYISO (irregular modulation rewards selective gating). Best W=24 examples: ERCOT PatchTST 2.85%, MISO S-Mamba 2.33%, PJM S-Mamba 2.97%. …
- **Gaps/Limitations:**
  - **System/balancing-authority level only** — explicitly not nodal/zonal, and nowhere near EV charging-station granularity; station-level loads are far sparser and event-driven.
  - **Point forecasts only** — deterministic MSE/MAPE; no prediction intervals, quantiles, or probabilistic heads.
  - **Hourly resolution** — no sub-hourly dynamics relevant to fast-charging ramps.
  - Weather benchmark only at W=24; single seed (42), no significance testing; L=240 not ablated; efficiency measured by parameter count, not wall-clock latency; ancillary-service results preliminary (ERCOT only); excludes foundation models (Chronos, TimesFM), TimeMixer, and hybrid Mamba-Transformer designs.
  - Reanalysis weather instead of operational NWP forecasts inflates weather benefit at longer horizons. **Thesis relevance**: provides exactly the three-way (SSM/Transformer/RNN) architectural comparison Gap T-7 asks for — but at grid aggregate scale, leaving open whether the channel-independence vs cross-variate vs selective-SSM trade-off transfers to sparse, stochastic, price/weather-sensitive station-level EV loads.

### 2026_Similar_Day_Selection_EV_Load
**A similar day selection framework with heterogeneous feature integration for electric vehicle charging load forecasting**  
Wang et al. · Applied Energy · 2026
<https://doi.org/10.1016/j.apenergy.2026.127731>
**Models**: XGBoost, NSGA-II, Random_Forest, SVR, LSTM, LightGBM, ShapeDTW, Multi_Dimensional_DTW, Adjacency_Matrix  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: MAE, RMSE, Precision, Recall, F1_Score, AUC  
**Data**: UrbanEV_Dataset  
**Features**: Historical_Load, Temperature, Air_Pressure, Sea_Level_Pressure, Humidity, Rainfall_Intensity, Dew_Point, Calendar_Features, Holiday_Flag, Holiday_Flag, POI_Functional_Entropy

- **What they did:**
  - Improve Day_Ahead_Forecasting EV charging load forecasting by optimizing the **training-data structure** rather than the forecaster itself: select a set of historical "similar days" whose load patterns match the target day, then feed them into standard forecasting models. Key contributions: 1. **Hybrid similarity engine** combining ShapeDTW (load curves), Multi_Dimensional_DTW (weather vectors), and MAD (contextual …
- **Method core:** Three-stage pipeline (Sec. 2): multi-feature similarity computation → adaptive weight optimization (NSGA-II) → leakage-free XGBoost pattern matching. **Weighted overall similarity score (Eq. 1, Weighted Similarity Score)**:  S_{final,e} = \vec{w} \cdot \vec{s}_e = \sum_{k \in \{load,\,weather,\,context\}} w_k \cdot s_{k,e}  with $\vec{s}_e = (s_{load,e}, s_{weather,e}, …
- **Key results:**
  - **Pattern matching quality (Table 2)** — XGBoost beats KNN and LightGBM (LightGBM unstable at small samples); all metrics equal because Precision=Recall=F1 at matched set sizes: AUC >0.93 across all sizes; **M*=35** chosen via elbow method and confirmed by forecasting sensitivity analysis (MAE/RMSE minimum at M=35 for …
  - Average error reduction ≈ **4.5%** (largest: LightGBM, ~4.5% MAE & RMSE cut); RF and LSTM ≈1.5%; SVR marginal.
  - vs. **Standard Similar Day Selection (SSDS)**: proposed framework better for all models — e.g., **30.1% MAE reduction for LightGBM**; SSDS even underperforms the no-similar-day baseline (naive similarity injects noise).
- **Gaps/Limitations:**
  - Global average improvement modest (~4.5%) due to strong station-level heterogeneity; SDA has intrinsic performance limits in regions with functional entropy >0.94.
  - Future work (authors): incorporate socio-demographic variables; hybrid modeling / entropy-adaptive weighting or structural adjustments for mixed-use (high-entropy) areas; validate portability across cities with diverse climates and functional characteristics.
  - Methodological caveats: framework tuned/validated on one city and one year of data; similar-day features add inputs requiring re-tuning per zone; POI-based entropy may incompletely capture social dynamics (Tier 3 urban cores).

### 2026_TFT_Conformal_Environmental_EV_Load
**Forecasting EV charging load with a temporal fusion transformer: A multi-horizon and interpretable approach with environmental features**  
Dost et al. · Computers and Electrical Engineering, Vol. 135, Art. 111201 (Elsevier) · 2026
<https://doi.org/10.1016/j.compeleceng.2026.111201>
**Models**: Temporal_Fusion_Transformer, Conformal_Prediction, Quantile_Regression  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAE, MSE, MAPE, SMAPE, R_squared, Pinball_Loss, PICP, MPIW, NPIW  
**Data**: Palo_Alto_EV; Weather  
**Features**: Temperature, Precipitation, Solar_Radiation, Calendar_Features, Calendar_Features, Calendar_Features, Calendar_Features, Cyclical_Encodings, Historical_Load, Rolling_Energy_Aggregates, Session-Level_Statistics, Charging_Efficiency_Metrics, …

- **What they did:**
  - Develop a unified, interpretable, probabilistic framework for EV charging load forecasting using the Temporal_Fusion_Transformer (TFT), providing **native multi-horizon** predictions at two timescales — **hourly (1–24 h ahead)** and **daily (1–7 days ahead)** — enriched with environmental covariates and calibrated by conformal prediction. Four identified research gaps motivate the work:
  - **RG1**: Prior models target a single resolution or rely on recursive/iterative multi-step strategies prone to error accumulation; no unified native dual-timescale architecture existed.
  - **RG2**: Environmental variables (temperature, rainfall, solar radiation) are underutilized despite their documented effect on EV user behavior.
  - **RG3**: Most DL forecasters are black boxes without actionable feature attribution.
  - **RG4**: Literature fragments into point-accuracy work vs. probabilistic pipelines; no single end-to-end DL model delivers both. Contributions: (C1) first native short-term + medium-term EV load forecaster in one end-to-end TFT; (C2) rich environmental + calendar covariate integration synchronized to high-resolution records; (C3) built-in interpretability via variable selection networks, attention, GRNs; (C4) …
- **Method core:** TFT processing two input streams: past observed inputs (historical load + rolling stats) and future known inputs (calendar + environmental forecasts). Core mechanisms: 1. **Variable Selection Networks (VSN)** — instance-wise feature selection per time step, separate modules for encoder and decoder inputs. 2. **Temporal processing** — seq2seq LSTM encoder-decoder for local …
- **Key results:**
  - **Table 5 — proposed TFT (real scale):** **Table 6 — daily-scale vs literature baselines:** TFT (MSE 0.508, RMSE 0.71, MAPE 6.17 %, SMAPE 4.37 %, MAE 0.662, R² 0.98) vs ConvLSTM+BiLSTM (MSE 0.878, RMSE 0.71, MAPE 18.31 %), BiConvLSTM+LSTM (MSE 0.87, RMSE 0.73, MAPE 24.58 %), XGBoost_sc (RMSE 2.748, MAE 5.37, R² 0.81), …
- **Gaps/Limitations:**
  - Environmental/pricing variables showed comparatively **small** VSN importance — demand governed mainly by temporal regularities and recent usage in this dataset.
  - Static tariff structure limits behavioral insight; authors hypothesize dynamic pricing would reweight attention toward price features (future work).
  - Post-conformal coverage (96.2 %) far exceeds nominal 80 % → conservative/wider intervals; marginal degradation of point accuracy.
  - Future work suggested: electricity pricing, traffic density, charging-behavior segmentation, socioeconomic indicators; cross-city/climate generalization tests; real-time/edge deployment; coupling probabilistic outputs with optimization for station/grid management.
  - Single-city validation only; no spatial dimension modeled.

### 2026_TS_ICL_Time_Indexed_Foundation_Model
**TS-ICL: A Flexible Time-Indexed Foundation Model for Time Series via In-Context Learning**  
Naour et al. · arXiv preprint arXiv:2606.05878 (Under review, EDF R&D) · 2026
<https://arxiv.org/abs/2606.05878>
**Models**: TS-ICL, Chronos-2, TimesFM, TiRex, TabPFN-TS, Transformer, SAITS, BRITS  
**Horizon**: Short_Term_Forecasting / Long_Term_Forecasting / Continuous_Horizon  
**Metrics**: CRPS, MAE, MSE, MASE  
**Data**: fm-impute-bench; fev-bench; Electricity_ECL; Solar_Dataset; Weather; ETT  
**Features**: Historical_Load, Continuous_Time_Basis, Dynamic_Covariates, Time_Encoding, Missing_Value_Mask

- **What they did:**
  - **Core Problem**: Existing Time Series Foundation Models (TSFMs) focus almost exclusively on forecasting with regularly sampled, complete observation grids. In real-world industrial and grid operations (e.g., EV charging stations and smart meter telemetry), time series are frequently partially observed, irregularly sampled, and corrupted by missing chunks, requiring models that can jointly forecast, impute missing …
  - **Primary Novel Contribution**: 1. **TS-ICL Architecture**: Introduces TS-ICL, a probabilistic In-Context Learning (ICL) foundation model built on a 4-module **Encoder–Regressor Transformer** framework that natively unifies forecasting, missing-value imputation, and irregular sampling under a single timestamp-aligned regression formulation. 2. **Timestamp-Aligned Perceiver & Cross-Channel Encoder**: Employs a …
- **Method core:** Let $x = (x_t)_{t \in \mathcal{T}}$ be a time series on irregular timestamps $\mathcal{T} = \mathcal{T}_{\text{ctxt}} \cup \mathcal{T}_{\text{tgt}}$, where observed context is $x_{\text{ctxt}} = (x_t)_{t \in \mathcal{T}_{\text{ctxt}}}$ and target is $x_{\text{tgt}} = (x_t)_{t \in \mathcal{T}_{\text{tgt}}}$. When $\max(\mathcal{T}_{\text{ctxt}}) < …
- **Key results:**
  - **Univariate Imputation (132 Tasks)**:
  - **TS-ICL**: Achieves lowest **NMAE** and **CRPS** across all 132 tasks, outperforming TabPFNv2.5-TS, TabICLv2-TS, and supervised baselines (SAITS, BRITS).
  - **Inference Speed (Table 2 p.7)**: TS-ICL is **two orders of magnitude faster** (median 0.12s per task on H100 vs 15.4s for TabPFNv2.5-TS).
- **Gaps/Limitations:**
  - 1. **Perceiver Token Compression**: Compressing high-frequency long-context sequences into $M$ latent grid tokens can induce information bottlenecks for extremely long horizons (>4096). 2. **Computational Scaling of Full Cross-Attention**: Computing pairwise cross-attention across large numbers of covariate channels ($C > 20$) increases inference memory. 3. **Application to EV Charging Analytics**: Ideal for …

### 2026_TiRex_2_Multivariate_Streaming_Forecasting
**TiRex-2: Generalizing TiRex to Multivariate Data and Streaming**  
Podest et al. · arXiv preprint arXiv:2607.01204 (ELLIS Unit Linz, JKU Linz & NXAI) · 2026
<https://arxiv.org/abs/2607.01204>
**Models**: TiRex-2, TiRex, xLSTM, Chronos-2, TimesFM, Moirai, FlowState, TabPFN-TS, PatchTST, DLinear  
**Horizon**: Short_Term_Forecasting / Long_Term_Forecasting / Streaming_Forecasting  
**Metrics**: CRPS, MASE, WQL  
**Data**: GIFT-Eval; fev-bench; Chronos_Corpus; KernelSynth; Electricity_ECL; Solar_Dataset; Weather; ETT  
**Features**: Historical_Load, Dynamic_Covariates, Future_Known_Covariates, Patched_Embeddings, Asymmetric_Variate_Attention

- **What they did:**
  - **Core Problem**: Real-world time series forecasting is inherently multivariate, streaming, and conditioned on known future covariates (e.g., weather forecasts, electricity price signals, planned EV charging events). Existing Transformer-based multivariate foundation models (e.g., Chronos-2, MOIRAI-2) incur quadratic complexity $\mathcal{O}(L^2)$ in context length, recompute entire histories when new observations …
  - **Primary Novel Contribution**: 1. **TiRex-2 Architecture**: Introduces TiRex-2, a recurrent foundation model scaling from 38.4M active parameters in univariate mode to 82.5M (38.4M + 44.1M) for multivariate forecasting with past and future-known covariates. 2. **Decoupled Time & Variate Mixing**: Alternates an **$\mathcal{O}(VL)$ bidirectional xLSTM time mixer** along the patch axis with an **asymmetric …
- **Method core:** Input tensors $X \in \mathbb{R}^{V \times (T+F)}$ containing $V_{\text{tgt}}$ target series, $V_{\text{pcov}}$ past covariates, and $V_{\text{fcov}}$ future-known covariates are patched into non-overlapping windows of length $P=32$. The model alternates $N=12$ blocks of time and variate mixing. **Eq. 1 — Robust Variate Preprocessing & Binary Bypass**:  \tilde{x}_t = (1 - b) …
- **Key results:**
  - **fev-bench Zero-Shot (100 Tasks, including 30 with known covariates)**:
  - **TiRex-2 (82.5M)**: Achieves **lowest MASE and SQL**, establishing Rank 1 overall and a **>70% pairwise win rate** against competing foundation models.
  - Outperforms Chronos-2, TimesFM 2.0, FlowState, and TabPFN-TS.
- **Gaps/Limitations:**
  - 1. **Dynamic Variate Selection**: Assumes static grouping of $V$ channels during a given forward window rather than dynamic sparsity selection over thousands of ambient sensors. 2. **Fixed Patch Granularity ($P=32$)**: Streaming updates operate at 32-step patch boundaries rather than single-tick continuous time (which can be complemented by continuous models like FlowState). 3. **High Relevance to EV Charging …

### 2026_Toto_2_Scaling_Era
**Toto 2.0: Time Series Forecasting Enters the Scaling Era**  
Khwaja et al. · arXiv preprint arXiv:2605.20119v2 [cs.LG] · 2026
<https://arxiv.org/abs/2605.20119v2>
**Models**: Toto, TimesFM, Chronos, Moirai, TiRex, PatchTST, FlowState, Xihe, Timer, Time-MoE, Sundial, Granite, TTM, Transformer, xLSTM, Migas, Reverso  
**Horizon**: Long_Term_Forecasting  
**Metrics**: CRPS, MASE, Pinball_Loss, OWA  
**Data**: BOOM; GIFT-Eval; TIME_Benchmark; Datadog_Observability; TempoPFN_Synthetic; GIFT_Eval_Pretrain  
**Features**: Historical_Load

- **What they did:**
  - **Research question**: Do time series foundation models (TSFMs) scale reliably — can a single training recipe applied at successively larger widths and token budgets produce predictable returns, as in NLP/vision (Kaplan et al. 2020; Radford et al. 2019)?
  - **Core contribution — Toto 2.0 family**: Five open-weights decoder-only patched transformers **4M / 22M / 313M / 1B / 2.5B params** trained under ONE recipe that shows **monotonic scaling**: every size improves on the one below on BOOM, GIFT-Eval and TIME. First TSFM demonstration of reliable scaling.
  - **Three design pillars**: 1. **Architecture refinements over Toto 1.0 (Cohen et al. 2024)**: Contiguous Patch Masking (CPM) for single-pass parallel decoding; quantile output head (9 levels) replacing Student-T mixture (SMM); **NorMuon** optimizer replacing AdamW to handle sign-valued pinball gradients; patch size 32 (from 64), robust causal scaler with `arcsinh`, residual MLP patch projections, PerDimScale …
  - **Empirical claim**: Toto 2.0 sets **new SOTA zero-shot** on all three benchmarks — **BOOM** (observability), **GIFT-Eval** (97 tasks, 23 datasets; top-3 CRPS ranks 20.3/21.1/21.4), **TIME** (98 fresh tasks, 50 datasets; top-3 on every metric). Finetuned 2.5B-FT and FnF ensemble additionally take #1/#2 on full GIFT-Eval leaderboard (all tiers). Every size sits on/near Pareto frontier; 22M matches Toto 1.0 (151M) …
- **Method core:** **Model Type**: Decoder-only patched Transformer with **alternating time-axis (causal) and variate-axis (full) attention** retained from Toto 1.0. Pipeline (Fig. 2): Robust Causal Scaler → Patch Embedding + CPM (binary mask channel) → Input Residual MLP → Variate-Time Transformer Decoder → Output Residual MLP → **Quantile Output Head** (9 levels). Context 4096 timesteps (2048 …
- **Key results:**
  - **BOOM (Fig. 5, §5.1)** — CRPS rank / CRPS / MASE; lower is better; all 5 Toto 2.0 on Pareto frontier; every size beats every external FM:
  - CRPS rank: **2.5B 3.88**, **1B 3.96**, **313M 4.26**, **22M 5.53**, **4M 7.17** vs Toto 1.0 (151M) 6.94, Chronos-2 7.39, TimesFM 2.5 10.7, Moirai 2 11.9, TimesFM 2.0 11.3, Chronos Bolt 12.3, Time-MoE/Timer s1 ~17.5.
  - CRPS: 2.5B/1B 0.349, 313M 0.351 … Toto 1.0 0.375, Chronos-2 0.382 etc.
- **Gaps/Limitations:**
  - **Long-horizon coherent extrapolation still lags classical baselines**: Even 2.5B loses structure at 8192 steps where a well-specified seasonal ARIMA/ETS would extrapolate cleanly; tail behavior, regime shifts, far-OOD signals remain open (§6). Suggests need for architectural changes + scaling + post-training objectives.
  - **Data curation ad hoc**: Proportions chosen by sweep rather than principled filtering/dedup/annotation/curriculum (contrast LLM curation). Optimal mix excluding public data for pretraining yet requiring 45% public for FT is non-intuitive and empirically found, not explained.
  - **Evaluation tracks forecast error, not downstream value**: CRPS/MASE ≠ production value (cf. V2G-SVE [Zhong et al. 2024]); ARFBench multimodal incident reasoning and observability world-model (metrics+traces+logs+topology+code+events) remain future.
  - **Metrics as distinct modality ignored**: Compressing Datadog metrics into generic time-series discards structure; heterogeneous frequencies, extremely high dimensionality (context selection), histogram/distribution metric types, complex/multiple/non-integer/uneven seasonalities all unsolved.
  - **No EV or power-systems evaluation**: All benchmarks are generic/observability; transfer to sparse, spiky EV charging loads (ACN, ElaadNL, Boulder, Pecan Street) unproven; covariate-free design leaves arrival/departure, SoC, tariff, weather+traffic fusion via cross-attention as open gap.
  - **Inference-time coherence horizon ~768 steps single-pass**: Beyond that requires block decoding (mitigates drift but not perfectly); zero-shot beyond 2× training context degrades even for largest model.
  - **Width scaling validated, depth/data scaling not isolated**: Recipe scales width/depth/heads jointly; compute-optimal frontier vs Hoffmann et al. not mapped; total training cost (600k steps × 64 batch × 4096 length) and carbon not reported beyond step counts.
  - **Weight decay not guaranteed to transfer under u-µP**: Held fixed from proxy; theory guarantees LR only.

### 2026_TriModal_Causal_EV_Demand
**Tri-modal causal learning for forecasting EV charging demand**  
Wang et al. · Pattern Recognition Letters, Vol. 206, pp. 8–14 (Elsevier) · 2026
<https://doi.org/10.1016/j.patrec.2026.04.028>
**Models**: TriCast, SAGE_Semantic_Aware_Graph_Encoder, TACT_Causal_Temporal_Alignment, Price_Elasticity_Modulator, Causal_Dilated_Convolution, Set_Transformer_Induced_Attention  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAE, MAPE, RAE  
**Data**: UrbanEV_Dataset  
**Features**: Station_Occupancy, Electricity_Tariff, Traffic_Zone_Adjacency

- **What they did:**
  - Proposes **TriCast**, a tri-modal forecasting framework that jointly models **spatial, temporal, and economic modalities** for urban EV charging demand prediction. Targets three core deficiencies of prior methods: 1. **Static spatial graphs** based only on geographic proximity miss latent functional similarity between regions → poor generalization to unseen zones. 2. **Temporal information leakage** in …
- **Method core:** **Problem definition**: charging network as graph $G=(V,E,A)$, $N=|V|$ stations, adjacency $A \in \mathbb{R}^{N\times N}$; node features $x_{t,i} \in \mathbb{R}^C$ (occupancy, electricity pricing, contextual signals). Given historical window $X = (X_{t-P+1},\dots,X_t) \in \mathbb{R}^{P\times N\times C}$, predict $Y = (X_{t+1},\dots,X_{t+Q}) \in \mathbb{R}^{Q\times N\times C}$.
- **Key results:**
  - Evaluated at horizons 15/30/45/60 min (3/6/9/12 steps) vs **16 baselines**: traditional — VAR, Lasso, KNN; deep learning — FCNN, LSTM, GCN, GAT, GCN-LSTM, STGCN, HSTGCN, DCRNN, AST-GAT, FourierGNN, PAG, CityEVCP, PIAST. Metrics reported ×10² (Table 1): Horizon detail (RMSE 15/30/45/60 min): TriCast **2.92 / 4.39 / …
- **Gaps/Limitations:**
  - Short 30-day record and single city (Shenzhen) in the main experiments; cross-city transfer claimed as design motivation ("transferable") but quantitative cross-city results are limited to robustness/stability claims under distribution shift.
  - Occupancy used as a proxy for demand rather than measured energy.
  - Deterministic MSE-trained point forecasts only — no probabilistic/interval outputs.
  - Only 57/247 zones have dynamic pricing; elasticity learning is constrained by sparse dynamic-price coverage.
  - Conclusion text inconsistently states "outperforms 14 baselines" vs 16 baselines compared in Section 3.2/Table 1.
  - Data/code availability by request only — reproducibility depends on authors.

### 2025_BWO_ICEEMDAN_iTransformer
**BWO–ICEEMDAN–iTransformer: A Short-Term Load Forecasting Model for Power Systems with Parameter Optimization**  
Zheng et al. · Algorithms (MDPI), vol. 18, no. 5, art. 243 · 2025
<https://doi.org/10.3390/a18050243>
**Models**: iTransformer, ICEEMDAN, BWO  
**Horizon**: Short_Term_Forecasting  
**Metrics**: R_squared, MAE, RMSE  
**Data**: Singapore_Energy_Market_Dataset  
**Features**: Electricity_Load, Electricity_Tariff, Temperature, Humidity, Historical_Load

- **What they did:**
  - **Problem**: Growing irregularity/non-stationarity of power load data (diverse consumption patterns, distributed microgrids, renewables) makes precise short-term load forecasting difficult; demand-response programs depend on accurate forecasts.
  - **Contribution**: A hybrid decomposition–optimization–forecasting pipeline, **BWO–ICEEMDAN–iTransformer**: 1. BWO (Beluga Whale Optimization) optimizes the two ICEEMDAN parameters — noise standard deviation (Nstd) and number of realizations (NR) — using minimum envelope entropy as fitness function. 2. Optimized ICEEMDAN decomposes volatile load into IMFs + residual (13 IMFs + 1 residual on all splits). 3. Each IMF …
  - Claimed first use of a metaheuristic to tune ICEEMDAN parameters rather than relying on empirical settings.
- **Method core:** **iTransformer architecture** (inverted transformer; each variate's whole series becomes one token):
- **Key results:**
  - Proposed model (test set): **R² 0.9873, MAE 48.0014, RMSE 66.2221** (note: abstract mislabels MAE/RMSE; Table 4 values used here).
  - Decomposition gains over raw iTransformer: ICEEMDAN improved R²/MAE/RMSE by 1.68%/14.49%/21.37%; CEEMD 1.58%/13.51%/19.76%; EEMD 1.14%/3.42%/13.89%.
  - Full model improves 1.39% over ICEEMDAN–iTransformer and 3.09% over plain iTransformer; ablation error curves stay smooth while baseline errors reach ~200 MW during daytime peaks.
- **Gaps/Limitations:**
  - Model fusion (decomposition + optimization + deep forecaster) adds computational burden at training time; acceptable but must be managed for real-time operation.
  - Single-country dataset (Singapore), system-level load only — no EV-station or spatio-temporal evaluation; no probabilistic/uncertainty quantification.
  - Deterministic point forecasts only; decomposition performed per-split requires care against information leakage in operational deployment.

### 2025_Benchmark_Foundation_Models
**Benchmarking Time Series Foundation Models for Short-Term Household Electricity Load Forecasting**  
Meyer et al. · IEEE Access · 2025
<https://doi.org/10.1109/ACCESS.2025.3648056>
**Models**: Chronos, Chronos-Bolt, TimesFM, TimesFM_2.0, LagLlama, Moirai, Time-MoE, Sundial, PatchTST, Transformer, iTransformer, Temporal_Fusion_Transformer, SeasonalAverage  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, MSE, APNE  
**Data**: Lower_Saxony_Dataset; Southern_Germany_Dataset; IDEAL_Dataset; REFIT  
**Features**: Household_Electricity_Consumption

- **What they did:**
  - **Research question**: "Can zero-shot TSFMs match the capabilities of state-of-the-art trained-from-scratch Transformers in forecasting household electricity load?"
  - **Contribution**: First multi-dataset, time-series-cross-validation benchmark of zero-shot Time Series Foundation Models (Chronos, Chronos-Bolt, TimesFM, TimesFM_2.0, LagLlama, Moirai, Time-MoE, Sundial) against trained-from-scratch (TFS) Transformers (PatchTST, Transformer, iTransformer, Temporal_Fusion_Transformer) on univariate household STLF.
  - **Key methodological contributions**:
  - Contamination-aware dataset selection: excludes datasets present in TSFM pre-training corpora (Electricity Dataset, Ausgrid Solar Home, London Smart Meters, Portuguese Household); rejects BuildingsBench and TimeGPT-1 due to undisclosed training data → leakage risk.
  - Leakage-safe global train-test split: a single split date per dataset chosen via percentile logic over household max dates (0.25th percentile of max dates; 0.8th percentile of possible time points), preventing cross-household leakage of global patterns (e.g., Covid-19).
  - **Finding**: Zero-shot TSFMs are comparable to — and with longer input sizes (96/168 h) often better than — TFS Transformers, while requiring no domain-specific training.
- **Method core:** **Benchmark design**: 6 zero-shot TSFMs (official weights, no fine-tuning) vs 4 TFS Transformers (implemented in NeuralForecast, trained globally on all households' training splits) vs statistical baselines (SeasonalAverage seasonality=24, Naive Forecast). No extensive hyperparameter tuning — default parameters from original papers.
- **Key results:**
  - Chronos-Bolt is best on $MAE_h$ across Lower Saxony, REFIT, Southern Germany; TimesFM 2.0 best on IDEAL; PatchTST best on IDEAL $MSE_h$ (0.969). Best $MSE_h$: Time-MoE & Sundial (e.g., 0.892/0.894 Lower Saxony). Best $APNE_h$: Time-MoE (1.563 S. Germany) & Sundial (1.594).
  - Input-size effect: at input size 24, PatchTST ranks best (rank 2.36 @ horizon 24); TSFMs overtake it at input sizes 96 and 168 — Chronos-Bolt rank 2.05–2.62, TimesFM 2.0 rank 2.18–2.95, Sundial ~3.25–3.54 vs PatchTST 3.73–4.76. LagLlama (best rank 7.91) and Moirai (up to rank 14.00, MSE>10 on REFIT) fail to beat even …
  - Statistical robustness: >99% of pairwise comparisons significant (p<0.05); <1.5% remain at α=0.01.
- **Gaps/Limitations:**
  - Possible cross-domain temporal information leakage: TSFMs pre-trained on data covering the same calendar period may encode global patterns (Covid-19, geopolitical crises); only solvable with post-training collection dates. Unaddressed in original TSFM papers.
  - No hyperparameter tuning of TFS baselines (compute constraints) could understate their performance.
  - Restricted input sizes (max 168 h) disadvantage architecture-dependent models (LagLlama's lags, Moirai's context 1000); longer contexts unexplored.
  - Univariate only — multivariate extension with weather covariates proposed as future work; fine-tuning and energy-domain-pre-trained foundation models identified as promising directions.
  - TSFMs predict conservatively, underestimating extreme load peaks relevant for grid capacity (small APNE gap to baseline).

### 2025_CAT_Former_Short_Term_EV
**Short term demand forecasting of electric vehicle charging stations using context aware temporal transformer model**  
Hussain et al. · Scientific Reports, Vol. 15, Article 36652 · 2025
<https://doi.org/10.1038/s41598-025-20557-x>
**Models**: CAT-Former (Context-Aware Temporal Transformer), Transformer, Multi_Head_Attention, LSTM, BiLSTM, CNN_LSTM, BiLSTM, Hybrid Transformer (LSTM Encoder-Decoder)  
**Horizon**: 1-Hour Ahead and 1-Day Ahead  
**Metrics**: MSE, MAE  
**Data**: Boulder_Colorado; Weather  
**Features**: Calendar_Features $X_{temporal,t} = [h, dw, dt, dm, sd]$, Contextual_Features $X_{context,t} = [C_{location}, C_{weather}]$, Positional_Encoding $P_t$

- **What they did:**
  - Most existing EV charging demand forecasts target a single or city-aggregated charging station; charging behavior actually **differs across locations** within a city (time-of-day dependent trends).
  - Proposes **CAT_Former**, a Context-Aware Temporal Transformer that fuses **Temporal features** (calendar/session-based) and **Contextual features** (station coordinates + weather) inside a multi-head self-attention encoder-decoder for **1-hour and 1-day ahead** demand forecasts at multiple stations simultaneously.
  - Evaluated on public Boulder City, Colorado data at the three busiest sites (**Park 1 / Carpenter Park 1, Rec 1 / N Boulder Rec 1, Street 1 / Baseline St 1**), against LSTM, BiLSTM, CNN_LSTM, BiLSTM, simple Transformer, and a Hybrid Transformer with LSTM encoder-decoder.
- **Method core:** (**Eq. 1 — temporal vector**): $X_{\text{temporal},t} = [h, dw, dt, dm, sd]$ — hour of day $h \in [0,24)$, day of week $dw \in \{0..6\}$ (0 = Monday), day type $dt \in \{0 \text{ weekday}, 1 \text{ weekend}\}$, day of month $dm \in [1,31]$, session duration $sd$ Session duration: (**Table 2**) $sd = \frac{End\_time(e_t) - Start\_time(s_t)}{3600}$ (**Eq. 2 — contextual …
- **Key results:**
  - vs best-performing baseline (Hybrid Transformer): Rec 1 −6.23% MSE / −12.87% MAE; Street 1 −4.54% MSE / −9.28% MAE. Weakest baselines: Park 1 LSTM MSE 1.5286/MAE 1.2364; Rec 1 LSTM MSE 2.7324; Street 1 LSTM MSE 3.4000/MAE 1.8439.
  - **Park 1**: CAT-Former **MSE 0.83557, MAE 0.9141** vs Hybrid Transformer 0.96177 and LSTM 2.7725/1.6651 → −13.12% vs hybrid; reported −7.22% MSE / −15.08% MAE vs best baseline.
  - **Rec 1**: CAT-Former MSE 0.51552, MAE 0.718 — **Hybrid Transformer wins here** (MSE 0.4844, MAE 0.6959); CAT-Former 3.30% MSE / 6.40% MAE *higher* than best baseline.
- **Gaps/Limitations:**
  - Only 3 stations of one mid-size US city; authors note future work should add other cities and external factors like road traffic/networks.
  - No probabilistic outputs; deterministic point forecast only (MSE loss).
  - Daily aggregation discards hourly structure for the 1-day task; seasonality deliberately not preserved in the split.
  - Electricity prices and traffic volumes excluded (deemed low impact for short-term); unverified for other regions.
  - Loses to the LSTM-based Hybrid Transformer on the Rec 1 1-day-ahead case — context-aware attention does not universally dominate.
  - Thesis gap: explicit lat/long + weather injection into vanilla Transformer attention is a strong, simple spatial-context baseline for cross-station short-term forecasting.

### 2025_Chronos_2_Univariate_to_Universal
**Chronos-2: From Univariate to Universal Forecasting**  
Ansari et al. · arXiv preprint arXiv:2510.15821v1 [cs.LG] — Technical Report of Chronos-2 (Amazon Web … · 2025
<https://arxiv.org/abs/2510.15821>
**Models**: Chronos-2, Chronos, Chronos-Bolt, TimesFM, TiRex, Toto, COSMIC, Moirai, Sundial, TabPFN-TS, AutoARIMA, AutoETS, AutoTheta, PatchTST, TFT, DeepAR, N-BEATS, Transformer  
**Horizon**: Long_Term_Forecasting  
**Metrics**: SQL, WQL, MASE, CRPS, Win_Rate, Skill_Score  
**Data**: fev-bench; GIFT-Eval; Chronos_Benchmark_II; GIFT_Eval_Pretrain; Chronos_Corpus; Electricity; M4; Solar; Traffic; Weatherbench; Wiki_Pageviews; Buildings_900K  
**Features**: Historical_Load, Known_Covariates, Past_Only_Covariates, Categorical_Covariates

- **What they did:**
  - **Research question**: Can a single pretrained model handle the full spectrum of real-world forecasting tasks — univariate, multivariate, and covariate-informed (past-only / known-future, real-valued / categorical) — in a zero-shot manner without task-specific training or architectural changes?
  - **Core contribution — Chronos-2 (120M base; 28M small)**: First **universal** pretrained forecaster that replaces task-specific heads with **group attention** enabling in-context learning (ICL) across arbitrarily grouped time series. A single inference pipeline solves all four task families (Table 1, Table 2) via group-ID + future-input masking alone. State-of-the-art on all three comprehensive benchmarks — …
  - **Two pillars**: 1. **Group attention architecture** (encoder-only T5 + RoPE) that alternates **time attention** (self-attention along patches within one series) and **group attention** (attention across series at the same patch index within a group ID). Groups flexibly represent related series / multivariate variates / targets+covariates; memory scales **O(V)** vs O(V²) for flattened baselines (Table 1). …
  - **Empirical claim**: Chronos-2 beats every prior TSFM on all three benchmarks and beats **Chronos-Bolt** (its direct predecessor) decisively. On **fev-bench** (the only benchmark covering covariates) win rate **90.7%, skill 47.3%** SQL, statistically significant vs TiRex/TimesFM-2.5/Toto-1.0; inference **~3.6 s median, 300 series/s on single A10G**. Ablations: 28M small loses ≤1 pt skill, synthetic-only model nearly …
- **Method core:** **Model Type**: Encoder-only Transformer (T5 encoder backbone). Pipeline (Fig. 1): Robust Scaling → Meta Features (time index + mask) → Patching → Patch Embedding (residual network) → REG separator token → Alternating Time/Group Attention stack → Residual block on future-patch embeddings of D targets → **Quantile Head** (direct multi-patch, 21 quantiles). Inference-only; … — Architecture (Section 3.2): **Time Attention** = standard self-attention along temporal axis with **RoPE** (Su et al. 2024, replaces T5 relative embeddings). **Group Attention** = attention across all series within same group at each patch index; groups identified by vector $g$ of length batch size $B$ mapped to 2D attention mask (within-group only); **no positional …
- **Key results:**
  - Chronos-2: **W 90.7%, S 47.3%, 3.6s, 0% leakage, 0 failures**
  - Next best: TiRex 80.8/42.6/1.4s, TimesFM-2.5 75.9/42.3/16.9s, Toto-1.0 66.6/40.7/90.7s, COSMIC 65.6/39.0/34.4s, Moirai-2.0 61.1/39.3/2.5s, Chronos-Bolt 60.3/38.9/1.0s, TabPFN-TS 59.3/39.6/305.5s, Sundial 41.0/33.4/35.6s
  - Pairwise 95% CIs (bootstrap, Fig. 2) confirm Chronos-2 statistically significantly outperforms every baseline on both W and S (CIs exclude 50% and 0% respectively).
- **Gaps/Limitations:**
  - **Covariate scope**: Only numeric + categorical covariates; **multimodal (e.g. text) covariates** not supported — noted as promising future direction (Zhang et al. 2025).
  - **ICL limited on multivariate**: Gains smallest on multivariate subset; suggests current multivariate leverage may not yet exploit cross-variate structure as effectively as covariate usage — room for stronger multivariate ICL.
  - **No EV-specific evaluation**: Benchmarks are general time-series; performance on **EV charging load** with its specific covariates (ToU price, weather, SoC, arrival/departure) not evaluated — direct thesis transfer gap.
  - **Synthetic gap on fev-bench**: Synthetic-only variant shows meaningful gap on the most diverse/covariate-heavy benchmark, implying synthetic multivariatizers not yet fully capturing real-world dependency diversity.
  - **Context vs horizon trade-offs not ablated for forecasting horizons relevant to EV** (day-ahead vs ultra-long); long-context post-training gains are aggregate, not broken out by horizon frequency.
  - **Scalability upper bound** not explored beyond 120M; whether group attention scales to hundreds of variates / very large groups untested.

### 2025_Coherent_Hierarchical_EV_Load
**Coherent Hierarchical Probabilistic Forecasting of Electric Vehicle Charging Demand**  
Zheng et al. · IEEE Transactions on Industry Applications, vol. 61, no. 1, pp. 1329-1340 · 2025
<https://doi.org/10.1109/TIA.2023.3344544>
**Models**: LSTM, PICNN, DCL, DeepAR, DeepVAR, MLP  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: MAE, RMSE, MASE, Pinball_Loss, Winkler_Score, Energy_Score  
**Data**: Caltech_ACN  
**Features**: EV_Charging_Demand, Temperature, Dew_Point, Precipitation, Calendar_Features, Holiday_Indicator, Calendar_Features

- **What they did:**
  - **Problem**: EV charging station (EVCS) operators manage multiple geographically distributed stations hierarchically; probabilistic forecasting across stations must handle (1) strong stochasticity of user behavior without parametric distribution assumptions, (2) **quantile crossing** in classical quantile regression, and (3) **hierarchical incoherency** — individual station forecasts don't sum to the operator total.
  - **Contributions**: 1. A deep learning framework for hierarchical probabilistic EVCS demand forecasting solving multivariate stochasticity + coherency jointly. 2. PICNN (partial input convex neural network) models the joint multi-horizon conditional distribution as the gradient of a convex function w.r.t. quantile levels α → structurally prevents quantile crossing. 3. DCL (differentiable convex optimization layers, …
  - Forecasting engine is modular (LSTM used in case study); explicitly out of scope to innovate on engines.
- **Method core:** **Quantile function definition**, Eq. (1): $q_Z(\alpha) = F_Z^{-1}(\alpha) = \inf\{z \in \mathbb{R} : \alpha \le F_Z(z)\}$; monotonicity requirement (no quantile crossing), Eqs. (3)–(4): $(q_{Z,t}(\alpha_1) - q_{Z,t}(\alpha_2))(\alpha_1 - \alpha_2) \ge 0,\ \forall \alpha_{1,2} \in (0,1)^\tau$.
- **Key results:**
  - **Point forecasting (test set, Table I)** — proposed LSTM+PICNN vs baselines (MAE; proposed error ≈ 30% of DeepVAR for Total):
  - **Probabilistic evaluation (Table II)**: best on nearly all metrics/stations (QL at all α levels, Winkler Score), except QL(0.7)/QL(0.8) on Total where DeepVAR slightly better. Quantile performance asymmetric in α — large α harder due to skewed demand distributions.
  - **Reconciliation (Tables III–IV)**, energy score on 1,000 sampled scenarios:
- **Gaps/Limitations:**
  - Only a flat two-level hierarchy (3 stations + total) tested; authors state future work on more complicated hierarchical structures (grouped/nested trees).
  - Reconciliation applied to sampled scenarios rather than full predictive distributions (linear constraints on random variables induce intractable convolutions of CDFs/PDFs).
  - Probabilistic quality degrades at high quantile levels (skewed demand); forecast accuracy declines with longer horizons.
  - No exploration of alternative forecasting engines or cross-domain transfer; deterministic single-run case study on one dataset/workplaces only.

### 2025_DC_Charging_Profiles_TFT
**Deep learning predicts real-world electric vehicle direct current charging profiles and durations**  
Li et al. · Nature Communications 16:10921 · 2025
<https://doi.org/10.1038/s41467-025-65970-y>
**Models**: Temporal_Fusion_Transformer, beta-VAE, LSTM  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, Relative_Accuracy, Pinball_Loss, MSE  
**Data**: NW_Europe_DCFC_Dataset; Weather  
**Features**: Charging_Power, Battery_SOC, State_of_Charge, Temperature, Connector_Power_Rating, Connector_Type, Estimated_Battery_Capacity

- **What they did:**
  - Predict real-world EV DCFC (direct current fast charging) power–SoC charging profiles and charging **durations** from as little as a **single data point**, updating predictions in real time (event-driven) as new SoC readings arrive.
  - Contributions:
  - Two-stage deep learning workflow on **909,135 real-world DCFC sessions** (612 chargers, NW Europe, Nov 2021–Jul 2024): a β-VAE anomaly detector + a probabilistic profile prediction model (Temporal_Fusion_Transformer-based).
  - Self-supervised training with random masking enables operation on partial profiles of arbitrary length; quantile outputs give calibrated uncertainty.
  - Demonstrated operational accuracy: **90% relative accuracy** from 1 point; **95% relative accuracy and <1 min absolute error from six points within five minutes**.
  - Real-time capable: forward pass over 1024 sessions in ~100 ms (>10,000 sessions/s).
- **Method core:** **Stage 2 – Profile prediction**: TFT-style architecture — feature projection layer (linear projections for numeric series; trainable embedding for categorical connector type), variable selection networks (VSNs), gated residual networks (GRNs), gated linear units (GLUs), layer norm, 5 LSTM layers + 3 multi-head attention layers (4 heads each), state size 256, ~9.8M params. …
- **Key results:**
  - **Duration prediction**: ~90% average relative accuracy from a single input point (MAE < 2.5 min); explains 91% of variance at n=1. With 6 points (≤5 min): >90% accuracy for 90% of sessions; headline result **95% relative accuracy, absolute error < 1 min**. At n=15 points only 1.45% of sessions fall below 90% …
  - **Uncertainty**: share of high-uncertainty sessions (P10–P90 duration gap >20 min or >50% of median) drops from 15% (n=1) to <2% (n≥5). Persistent uncertainty flags residual anomalies at inference time.
- **Gaps/Limitations:**
  - Proprietary NDA-restricted dataset limits external replication; generalization beyond northwestern Europe / other climates may need new training data or transfer learning.
  - 60-s charger logging interval and OCPP integer SoC precision bound effective temporal resolution; updates become sparse late in sessions.
  - No cross-session user modelling/personalization (privacy constraints); future work suggests differential privacy or federated learning for user-level modelling.
  - Potential extensions: forward simulator inside reinforcement-learning smart-charging control, charger assignment/load scheduling/dynamic pricing optimisation, more advanced uncertainty quantification for safety/cost-sensitive uses.

### 2025_EV_STLLM_Spatio_Temporal_LLM
**EV-STLLM: Electric vehicle charging forecasting based on spatio-temporal large language models with multi-frequency and multi-scale information fusion**  
Fan et al. · arXiv preprint (arXiv:2507.09527), preprint submitted to Elsevier · 2025
<https://doi.org/10.48550/arXiv.2507.09527>
**Models**: EV-STLLM, GPT-2, PFGA, QLoRA, VMD, ICEEMDAN, FIG, ReliefF, GCN, LSTM  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAE, MAPE  
**Data**: UrbanEV_Dataset; Shenzhen_ST_EVCDP  
**Features**: Charging_Volume, Station_Occupancy, Holiday_Indicator, Adjacency_Matrix, Spatio_Temporal_Frequency_Embeddings, Electricity_Tariff, Weather

- **What they did:**
  - Forecast EV **charging volume (kWh)** and **station occupancy rate (%)** across a spatial network of charging stations, capturing complex spatio-temporal dependencies and multi-frequency/multi-scale dynamics that small-parameter models cannot learn from large datasets.
  - Contributions:
  - **EV-STLLM**: a two-module framework — (1) data preprocessing module fusing multi-frequency (VMD-ICEEMDAN + Multi-Scale Sample Entropy) and multi-scale (FIG) information with ReliefF feature selection; (2) a customized spatio-temporal LLM with the **Partially Frozen Graph Attention (PFGA)** module that injects station-network topology into a pre-trained LLM (GPT-2 backbone) via adjacency-matrix attention masks, …
  - Customized **time-frequency domain fusion loss** combining time-domain MAE with an FFT-based frequency-domain term to suppress label autocorrelation issues in direct multi-step forecasting.
  - Validated on real-world Shenzhen data against traditional (GCN/LSTM/PAG) and LLM-based baselines (ChatEV, GCNGPT, GATGPT, GPT4TS); strong few-shot and critical-day (Chinese Spring Festival) robustness.
- **Method core:** **Pipeline**: VMD denoising (drop highest-frequency IMF) → ICEEMDAN secondary decomposition of the most complex component (guided by MSSE) → recombine sub-components into high/mid/low-frequency series by MSSE similarity → FIG multi-scale granulation → ReliefF feature selection → Spatio-Temporal-Frequency Embedding layer → fusion convolution → PFGA LLM (F frozen + U …
- **Key results:**
  - Data 1, 3-step volume: EV-STLLM **RMSE 26.42 / MAPE 0.14 / MAE 19.49** — 44.26% RMSE reduction vs GCN (47.40), 40.81% MAE improvement vs ChatEV (32.93), beats GPT4TS (29.27/0.16/21.85).
  - Data 1, 6-step volume: RMSE 27.78 — 53.12% lower than GATGPT (59.26).
  - Data 2, 3-step volume: RMSE 58.89 / MAPE 0.09 / MAE 42.85 — 51.56% RMSE cut vs GCN (120.95), 46.30% MAE cut vs GCNGPT (79.80), 46.23% RMSE cut vs ChatEV (109.53), 9.75% RMSE cut vs GPT4TS (65.25), 50% MAPE cut vs both (0.18→0.09, 0.12→0.09).
- **Gaps/Limitations:**
  - Framework is heavy (LLM-based); authors propose **knowledge distillation** to build lighter-weight models suitable for localized deployment at individual stations.
  - Predictions not yet coupled to downstream action — future work should integrate forecasts with scheduling strategies for electricity-market transactions of charging stations/EV aggregators.
  - Only two randomly selected zones evaluated; generalization across many zones/cities untested. Prompt-free topology injection relies on proximity-based adjacency only (no semantic/road-network graphs).

### 2025_Hybrid_LSTM_Transformer_Demand
**Charging stations demand forecasting using LSTM based hybrid transformer model**  
Hussain et al. · Scientific Reports (Nature Portfolio), vol. 15, art. 36639 · 2025
<https://doi.org/10.1038/s41598-025-20421-y>
**Models**: LSTM, Transformer, Hybrid LSTM-Transformer  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MAE, MSE  
**Data**: Caltech_ACN; Caltech_ACN; Caltech_ACN  
**Features**: Historical_EV_Charging_Energy, Lookback_Window

- **What they did:**
  - **Problem**: Accurate medium-term (30 days) and long-term (120/240 days) EV charging station (EVCS) demand forecasting is hard for single models — LSTMs miss long-range context; Transformers need large data and overfit to medium/long-term trends; LSTM+Transformer combination had been ignored for EV charging demand.
  - **Contribution**: First study proposing a Transformer with an **LSTM-based encoder–decoder** (LSTM_Transformer) for EV charging demand forecasting:
  - LSTM encoder captures local/temporal dependencies of the input sequence; multi-head attention captures global long-range patterns.
  - Look-back window equals prediction period (30/120/240 daily steps).
  - Benchmarked against standalone LSTM and Transformer on two real ACN sites.
- **Method core:** **Baseline LSTM gates** (Eqs. 1–6):  f_t = \sigma(W_f[h_{t-1}, x_t] + b_f) \quad \text{(forget gate)}   i_t = \sigma(W_i[h_{t-1}, x_t] + b_i), \qquad \tilde{C}_t = \tanh(W_c[h_{t-1}, x_t] + b_C) \quad \text{(input gate / candidate state)}   C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t \quad \text{(cell-state update)}   o_t = \sigma(W_o[h_{t-1}, x_t] + b_o), \qquad …
- **Key results:**
  - **Caltech test set (MAE / MSE):** Relative gains vs baselines: 30 d — MAE −16.18% (vs LSTM) / −17.27% (vs Transformer), MSE −19.79%/−19.56%; 120 d — MAE −2.92%/−4.50%, MSE −3.79%/−4.85%; 240 d — MAE −2.10%/−5.71%, MSE −2.20%/−4.77%. **JPL test set (MAE / MSE):** Relative gains: 30 d — MAE −24.91%, MSE −23.17% (vs …
  - Largest improvements at 30-day horizon; gains shrink but stay consistent at 120/240 days (longer horizons carry more uncertainty from seasonality, behavior shifts, external events). Standalone LSTM generally beat standalone Transformer.
- **Gaps/Limitations:**
  - Higher model complexity → longer training time; restrictive for real-time/resource-limited deployment.
  - Univariate, history-only inputs — no weather, traffic patterns, or user-behavior covariates; multimodal integration proposed as future work.
  - No short-term evaluation (1 h / 24 h / 7 days ahead) though architecture permits it.
  - Model compression and adaptive updating to shifting charging patterns left unexplored.
  - Minor inconsistencies in reported numbers (e.g., abstract's 5.71%/4.85% vs conclusion attributing them differently; Table 4 lists Transformer 30-day MAE identical to LSTM).

### 2025_LTLM_LSTM_EV_Load
**Data-Driven Long-Term Learning Model for EV Charging Load Prediction**  
Weqar et al. · 2025 IEEE DELCON - International Conference on Recent Smart Technologies in Engineering … · 2025
<https://doi.org/10.1109/DELCON68055.2025.11400364>
**Models**: LTLM, LSTM  
**Horizon**: Long_Term_Forecasting  
**Data**: LA_Charging_Station_Dataset  
**Features**: Historical_Load, Daily_Weekly_Cycles, Seasonal_Trends

- **What they did:**
  - **Problem**: EV charging station (EVCS) load forecasting has focused on short-term horizons (30 min–24 h); long-term load forecasting (LTLF, 1–10 years) and medium-term (MTLF, 1 day–1 year) are needed for infrastructure planning, substation/circuit sizing, renewable integration, maintenance cycles, and investment decisions. Statistical/non-learning models fail under nonlinearity, rapid EV adoption growth, price …
  - **Contribution**: A **LTLM (Long-Term Load Memory)** framework built on LSTM networks that captures both short-term fluctuations (daily/weekly cycles) and long-term trends (monthly/seasonal variation, sectoral growth) in EVCS demand over extended horizons.
  - Also provides structured taxonomies: comparison of ANN-based learning methods (FNN/ANN, RBFNN, hybrid ANN+fuzzy/wavelet) and deep-learning limitations (RNN vanishing gradients, CNN locality-only, ARIMA/SARIMA linearity assumption, GRU less expressive than LSTM for very long sequences).
- **Method core:** **No explicit mathematical equations are presented in the paper**; the LTLM model is described architecturally:
- **Key results:**
  - Next-horizon forecast (Fig. 7): 100-day prediction from a 200-day lookback follows the actual trend closely.
- **Gaps/Limitations:**
  - Peak underestimation/flattening due to long-period averaging — a core accuracy deficit for capacity-planning use cases.
  - Single-station, partially synthetic, extrapolated dataset (~6 months real stretched to 1000 days) — weak evidence base for genuine multi-year LTLF claims.
  - No quantitative benchmarking against baselines (ARIMA, GRU, SVR, Transformer), no reported error metrics, and no ablations.
  - Exogenous drivers absent: weather (cloudy/rainy/stormy/clear), vacations/usage patterns deferred to future work.
  - Authors' own improvement roadmap: hyperparameter tuning (epochs, batch size, lr, dropout), GRU/Transformer alternatives, recursive multi-step forecasting, hybrid LSTM+ARIMA, continuous re-training via real-time API service.

### 2025_MSSTGAN_City_EV_Load
**Multi-Scale Spatial-Temporal Graph Attention Network for Charging Station Load Prediction**  
Tian et al. · IEEE Access, Vol. 13, pp. 29000-29017 · 2025
<https://doi.org/10.1109/ACCESS.2025.3541118>
**Models**: Multi-Scale Spatial-Temporal Graph Attention Network (MSSTGAN), Pyramid Split Attention (PSA), Multi_Head_Attention, Gated_Fusion, Transform Attention (TA), ST-GAT, T-GCN, STSGCN, STFGNN, Informer, LDformer  
**Horizon**: City-Level Multi-Station Forecasting: Task 7-1 (7 days → 1 day) & Task 30-7 (30 days → 7 days)  
**Metrics**: MAE, RMSE, MAPE  
**Data**: Palo_Alto_EV; Boulder_Colorado; Dundee_EV; Perth_EV  
**Features**: Adjacency_Matrix $A \\in \\mathbb{R}^{N\\times N}$, Spatio_Temporal_Embedding $X_{STE}$, Calendar_Features (week/day), EV_Charging_Demand

- **What they did:**
  - Targets two under-addressed problems in **city-level** EV charging station network forecasting: 1. **Low spatial resolution**: sparse data across geographically dispersed stations → solved by a **Pyramid_Split_Attention (split-pyramid)** module enabling multi-scale feature extraction. 2. **Spatial heterogeneity**: regional demand differences (station type, surroundings, usage patterns) → solved by **Spatio-Temporal …
  - Proposes **MSSTGAN**: encoder–decoder architecture where encoder/decoder each stack $L$ **Pyramid Multi-Head Attention Blocks (PMAB)** joined by a **Transform Attention (TA)** layer; parallel multi-scale input branches are merged into the final forecast.
  - Evaluated on **4 real-world datasets** over tasks **7-1** and **30-7**, outperforming LSTM/CNN/RNN/BiGRU, T-GCN, STSGCN, STFGNN, ConvLSTM+BiLSTM, ST-GAT, Informer, LDformer.
- **Method core:** Charging station network $\mathcal{G}=(V,E,A)$, signal $X \in \mathbb{R}^{T\times N\times C}$. (**Eq. 1 — forecasting map**):   h(\{X_{t_1}, X_{t_2}, \cdots, X_{t_P}\}, \mathcal{G}) = \{X_{t_{P+1}}, X_{t_{P+2}}, \cdots, X_{t_{P+Q}}\}   (**Eq. 2 — neighbor aggregation**): $v' = W\sum_{u\in\mathcal{N}(v)} h_u$ (**Eq. 3 — spatial embedding**): $X_{SE} = …
- **Key results:**
  - Palo Alto: MSSTGAN MAE **0.0332**, RMSE **0.1654**, MAPE **0.2014%** vs ST-GAT MAE 0.0697 / RMSE 0.4861 / MAPE 0.4386%.
  - Training time scales sub-linearly with size: Palo Alto 3,443 steps → 1,869 s; Boulder 1,150 → 1,531 s; Perth 1,094 → 1,426 s; Dundee 370 → 927 s (RTX 3090).
  - Parameter study: best at LR 0.001, 1 PMAB block, scale divisor $n=2$.
- **Gaps/Limitations:**
  - Authors explicitly acknowledge insufficient explanation of cross-dataset performance variation (esp. Boulder vs ST-GAT).
  - No exogenous covariates used — future work plans integration of **weather conditions and traffic flow**.
  - Computational efficiency optimization targeted for future real-time deployment.
  - Daily aggregation discards intra-day load shape; transferability to other spatio-temporal domains (renewables, urban traffic) left untested.
  - Thesis gap: multi-scale pyramid attention is a candidate module for handling sparse station networks; deterministic point forecasts only (no uncertainty quantification).

### 2025_Meta_Learning_Physics_Informed_GACN_Power_System
**Meta-Learning Enhanced Physics-Informed Graph Attention Convolutional Network for Distribution Power System State Estimation**  
Wu et al. · IEEE Transactions on Network Science and Engineering, Vol. 12, No. 2, pp. 1186-1198 · 2025
<https://doi.org/10.1109/TNSE.2025.3525625>
**Models**: Meta-PIGACN, Physics-Informed Graph Attention Convolutional Network (PIGACN), GCN, Multi_Head_Attention, Meta-Learning (MAML-style)  
**Horizon**: Real-Time Distribution System State Estimation (DSSE)  
**Metrics**: MAE, MAPE, RMSE  
**Data**: IEEE_33_Node_Distribution_System; IEEE_118_Node_Distribution_System; 1746_Node_Distribution_System; 2012 Global Energy Forecasting Competition RES data  
**Features**: Power_Injection, Line_Power_Flow, Admittance_Matrix, Node_Voltage_Magnitude, Voltage_Phase_Angle, Grid_Topology

- **What they did:**
  - **Problem**: Distribution_System_State_Estimation (DSSE) is challenged by frequent topology changes (reconfiguration/line switching), volatile renewable (WT/PV) power injections, and limited historical data covering all topologies.
  - **Contribution — Meta-PIGACN**, three innovations: 1. **Physics-informed edge weighting**: the nodal admittance matrix $Y$ is embedded into the graph attention operation as a masking matrix derived from the Gauss–Newton iteration, controlling neighbor aggregation via physical laws (Kirchhoff's Current Law). 2. **Graph attention convolution**: multi-head attention replaces a fixed adjacency matrix, automatically …
  - Validated on IEEE 33-node, 118-node, and a large-scale 1746-node system; beats WLS, FCN, CNN, GCN and their meta-learned variants.
- **Method core:** (**Eq. 1 — measurement model**):   z = h(x) + e   where $z$ = measurements, $h$ = measurement function, $x$ = true states, $e$ = noise. (**Eq. 2 — WLS estimator**):   \hat{x} = \arg\min_x \left(z - h(x)\right)^T R^{-1} \left(z - h(x)\right)   (**Eq. 3 — Gauss–Newton update**):   \hat{x}^{l+1} = \hat{x}^l + G(\hat{x}^l)^{-1} H(\hat{x}^l)^T R^{-1} \left[z - …
- **Key results:**
  - **Fixed topology (33-node)**: PIGACN reduces voltage-magnitude MAE by **32.26% vs FCN, 85.05% vs GCN, 22.10% vs CNN**; also beats WLS baseline.
  - **Fixed topology (118-node)**: RMSE of phase-angle estimation reduced by **99.87% vs both FCN and GCN**, and **11.51% vs CNN**.
  - **Changing topologies (no meta-learning)**: PIGACN MAE ($V_m$, 33-node) better than FCN/GCN/CNN by **9.09%/9.64%/7.98%**; MAPE ($V_a$, 118-node) better by **63.00%/66.63%/48.82%**.
- **Gaps/Limitations:**
  - Evaluation purely on simulation-generated data (MATPOWER power flow); no real SCADA/D-PMU field measurements.
  - Fine-tuning still requires gradient updates and labeled samples from each new topology; zero-shot adaptation not addressed.
  - Single-snapshot state estimation; temporal dynamics/unrolled spatio-temporal extensions left implicit.
  - Authors' future work: extension to other energy systems (natural gas, thermal networks) and **privacy-preserving distributed learning** for multi-party networks.
  - Thesis gap: the physics-masked attention ($QK^T/\sqrt{d_k} \otimes Y$) is directly transferable to EV-charging spatial-temporal graphs where feeder topology changes.

### 2025_MixerInformer_Transfer_Learning_New_EV_Stations
**Mixer-Informer-Based Two-Stage Transfer Learning for Long-Sequence Load Forecasting in Newly Constructed Electric Vehicle Charging Stations**  
Zhou et al. · arXiv preprint (submitted to Elsevier), arXiv:2505.06657 [eess.SY] · 2025
<https://doi.org/10.48550/arXiv.2505.06657>
**Models**: MIK-TST, MLP-Mixer, Informer, KAN  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MAE, MSE  
**Data**: Boulder_Colorado  
**Features**: Historical_Load, Calendar_Features, Charging_Session_Logs, Calendar_Features

- **What they did:**
  - Address EV charging station load forecasting when (a) long-sequence temporal dependencies (daily/weekly/seasonal cycles spanning hundreds–thousands of steps) must be captured, and (b) historical data are scarce because the station is newly constructed. Contributions: 1. **MIK hybrid architecture**: integrates an MLP-**Mi**xer module (multi-source feature fusion across temporal and channel dimensions), an …
- **Method core:** Pipeline: **Mixer (feature fusion) → Informer (temporal modeling) → KAN (nonlinear refinement)**, wrapped in a two-stage transfer learning pipeline. **Input standardization (Standardization Equation):**  X_{std} = \frac{x_i - u}{\theta}  where $u$ is the mean and $\theta$ the standard deviation scaling factor. Temporal-mixing layer (linear projection + fully connected ops …
- **Key results:**
  - Metrics: MAE and MSE (normalized domain). **Evaluation metrics:**  MAE = \frac{1}{N}\sum_{i=1}^{N}|y_i - \hat{y}_i| \qquad MSE = \frac{1}{N}\sum_{i=1}^{N}(y_i - \hat{y}_i)^2  **Main comparison (Table 1):** Best baseline PatchTST beaten by 4% MAE and 8% MSE. **Ablation (Table 2):** Transfer learning removal is the …
  - Hidden dim $d \in \{64,128,256,512,1024\}$: best at $d=256$ (MAE 0.4450, MSE 0.6322); d=64 → MAE 0.4599/MSE 0.6692; d=512 → 0.4475/0.6350; d=1024 → 0.4540 (overfitting).
  - Attention heads $N_{heads} \in \{1,2,4,6,8,10\}$: best at 8 (0.4450/0.6322); 1 head → 0.4611/0.6837; 10 heads → 0.4456/0.6368.
- **Gaps/Limitations:**
  - Relies mainly on station-specific historical data; external variables (weather, traffic patterns, socio-economic factors) not modeled.
  - Robustness in highly heterogeneous or rapidly evolving environments (drastically different usage profiles) unverified.
  - Computational efficiency still a challenge for real-time deployment on resource-constrained systems despite ProbSparse attention.
  - Future work: adversarial/domain-regularization-based domain adaptation; exogenous real-time features; model pruning/quantization for real-time energy management; uncertainty quantification via Bayesian/ensemble methods.
  - Research gaps relevant here: cold-start forecasting for new stations via transfer learning ↔ 2024_MQ_TCN_Transfer_Learning_EV, 2023_MetaProbformer_EV_Load; Informer-line evolution ↔ 2021_Informer_Beyond_Efficient_Transformer, 2026_MetaLearning_Informer_Probabilistic_EV; KAN foundations ↔ 2024_KAN_Kolmogorov_Arnold_Networks; benchmarked long-sequence backbones ↔ 2023_PatchTST_A_Time_Series_is_Worth_64_Words, …

### 2025_Multi_View_Graph_Intrusion_Detection_EV
**Multi-view graph contrastive representative learning for intrusion detection in EV charging station**  
Li et al. · Applied Energy · 2025
<https://doi.org/10.1016/j.apenergy.2025.125439>
**Models**: MVGCRL, Mask_Attention_Graph_Transformer, GNN, GCN, GAT, EdgeConv, CNN, LSTM, DGI, GRACE, MVGRL  
**Horizon**: Spatial_Temporal_Forecasting  
**Metrics**: Precision, Recall, F1_Score  
**Data**: CICEVSE2024  
**Features**: Hardware_Performance_Counters, Kernel_Events, Microarchitecture_Events

- **What they did:**
  - EV charging infrastructure (EVSE ↔ CSMS via OCPP, EVCC via ISO15118) is exposed to cyberattacks (DoS/DDoS, MitM, cryptojacking, scans, floods). Traditional IDS treat flow records independently (ignoring feature interrelations) and need large labeled datasets.
  - Contributions: 1. **MVGCRL**: supervised multi-view graph contrastive learning that represents Hardware_Performance_Counters (HPC) logs as two graph views — a *temporal graph* (log entries = nodes, full-connected weighted) and a *feature graph* (HPC metrics = nodes over the window transpose). 2. Weighted graphs with edge weights learned during training via edge-weight perturbation + edge-masked attention propagation …
- **Method core:** **Problem formulation** ("patching of HPC logs"): HPC logs split into patches $X_l = (\boldsymbol{x_t}, \ldots, \boldsymbol{x_{t+l-1}}) \in R^{l\times N}$, stride $s=l$, $P=\lfloor\frac{L-l}{s}\rfloor$; task ("intrusion target"):   f: X_l \rightarrow \{\hat{y}_t,\ldots,\hat{y}_{t+l-1}\} \quad\text{and}\quad f:\{X_l, G\} \rightarrow \{\hat{y}_t,\ldots,\hat{y}_{t+l-1}\}  
- **Gaps/Limitations:**
  - Performance highly sensitive to hyperparameter tuning (lr, augmentation rate); augmentations must be manually designed to align pretext tasks with downstream objectives.
  - Future work: adaptive graph-augmentation methods tailored automatically to tasks; theoretical grounding of multi-view contrastive objectives.
  - Broader applications proposed: anomaly detection/demand-response support in integrated power-transportation networks, soft-open-point scheduling with energy storage.
  - Note for load-forecasting research: the multi-view graph construction + mask attention recipe is transferable to spatio-temporal EV charging demand graphs.

### 2025_Personalized_Federated_Learning
**Personalized federated learning for household electricity load prediction with imbalanced historical data**  
Zhu et al. · Applied Energy · 2025
<https://doi.org/10.1016/j.apenergy.2025.125419>
**Models**: PF-HoLo, LSTM, Encoder_Decoder, FedAvg, FedAvg, Federated_Mutual_Learning  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MSE, MAE, R_squared  
**Data**: REFIT  
**Features**: Appliance_Level_Load, Historical_Load, Last_Observed_Power_Anchor

- **What they did:**
  - Household consumption accounts for 30–40% of global electricity; accurate Short_Term_Forecasting appliance-level prediction supports Smart Home Energy Management Systems (SHEMS), but faces four challenges: 1. **Non-IID user behavior** — the IID assumption of classical FL breaks at household level. 2. **Imbalanced residential data** — households differ in appliances and in data volume (different smart-meter …
  - Contributions: (a) the PF-HoLo framework for appliance-level prediction under imbalanced data; (b) an end-to-end federated Encoder_Decoder model where only the Encoder is shared; (c) a personalized loss using encoder hidden states as soft targets for mutual learning; (d) extensive ablations on real-world household data.
- **Method core:** **PF-HoLo**: each household holds a *Meme model* (participates in federation via FedAvg) and a *Personal model* (local-only), trained mutually via knowledge distillation. Only the **Encoder of the Meme model is shared** during aggregation; Decoders stay local to adapt to household-specific distributions.
- **Key results:**
  - Cascade households: PF-HoLo **11 298.66 W² / 18.00 W** vs FedAvg 13 198.92 / 20.38 → **14.40% MSE / 11.69% MAE improvement**; FedSGD −1.86%/−0.22%; Central −1.32%/+3.54% (worse).
  - Very-Little households: PF-HoLo **8028.87 / 12.28** vs FedAvg 9267.36 / 14.19 → **13.36% / 13.50% improvement**.
  - Enough households: PF-HoLo **6601.60 / 13.44** vs FedAvg 7349.58 / 14.83 → **10.18% / 9.37% improvement**.
- **Gaps/Limitations:**
  - Requires appliance-level sub-metering; future work integrates NILM disaggregation to enable sensor-free deployment.
  - 1-min resampling too coarse for short-duration appliances (microwave/kettle) — limited accuracy gains there.
  - Planned systematic comparison of household-level vs appliance-level prediction trade-offs.
  - Framework validated only on household loads (not EV charging stations), but the imbalanced non-IID personalization recipe transfers directly to heterogeneous-charger federated EV forecasting.

### 2025_QR_LSTM_Attention_EV_Load
**Probabilistic Forecast of EV Charging Demand using Quantile Regression and LSTM with Attention Mechanism**  
Matrone et al. · ACM E-Energy '25: 16th ACM International Conference on Future and Sustainable Energy … · 2025
<https://doi.org/10.1145/3679240.3734687>
**Models**: QR-LSTM-Attention, LSTM, Encoder-Decoder with Attention, Quantile_Regression, Persistence Benchmark  
**Horizon**: 24-Hour Day-Ahead Probabilistic Forecast, Rolling Horizon Refreshed Hourly (15-min resolution)  
**Metrics**: CRPS, Pinball_Loss (q20/q50/q80), PICP  
**Data**: SmoothEMS_Met_GridShield_ASR_Utrecht_Dataset; Weather  
**Features**: Historical_Load (96 input steps = previous day), Temperature, Global_Solar_Radiation, Number_of_Active_Sessions, Calendar_Features (month, day, hour, minute)

- **What they did:**
  - Point forecasts alone are inadequate for microgrid/distributed energy management under uncertainty; few studies address **probabilistic** EV charging demand forecasting.
  - Extends the authors' prior point-forecast LSTM-attention model (Matrone et al. 2024, IEEE T-ITS) into a probabilistic framework via **Quantile_Regression**: three separate LSTM encoder-decoder attention models trained for the **20th, 50th (median), and 80th quantiles**, producing continuous prediction bands for day-ahead EV charging demand.
  - Evaluated on real data from an office parking lot in Utrecht (NL); best model cuts CRPS by **67.70%** vs a persistence benchmark.
- **Method core:** **Encoder**: stacked LSTM layers compressing 96 input steps into a lower-dimensional representation — the last hidden state of the final LSTM layer becomes the **Context Vector** fed to the decoder.
- **Key results:**
  - **Benchmark**: weekly persistence median + fixed-width intervals (10% of persistence prediction) around it for q20/q80.
  - Improvements of Model 48-2 over benchmark: Pinball q20 ↓ **81.39%**, q50 ↓ **62.09%**, q80 ↓ **68.04%**; CRPS ↓ **67.70%**; PICP ↑ **+26.82 percentage points** (78.60% vs 51.78%).
  - Trade-off insight: 48 and 64-unit models beat 24-unit ones especially on point forecast; 2-layer 48-unit config achieves best CRPS/PICP balance — deeper/wider (64-2) does not help coverage.
- **Gaps/Limitations:**
  - Only three discrete quantile models rather than a full predictive distribution; quantile crossing not discussed.
  - Single site (one parking lot), single dataset; generalization to other station types untested.
  - Authors' stated future work: include **additional input lags** and **extend the forecasting horizon** beyond 24 h.
  - No exogenous events (holidays, pricing) beyond calendar/weather features; no comparison against modern deep probabilistic baselines (e.g., DeepAR, diffusion models).
  - Thesis gap: clean, reproducible QR-LSTM-Attention benchmark for Day_Ahead_Forecasting probabilistic EV load forecasting; motivates conformal or distributional extensions.

### 2025_REST_Network_Port_EV
**REST Network: An Ensemble Deep Learning Approach for EV Charging Load Forecasting in Artificial Port Supply Chains**  
Alghamdi et al. · IEEE Access · 2025
<https://doi.org/10.1109/ACCESS.2025.3589292>
**Models**: RESTNet, ResNet, SENet, Transformer, DeepSigRNet, CNN, VGGNet, SVR, Random_Forest  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAPE, RMSE, MAE, R_squared, EEE, LVD, CPE, TAA  
**Data**: EV_Intelligent_Port_Logistics_Dataset; Dallas_Port_EV  
**Features**: Historical_Load, Charging_Duration, Battery_Capacity, Grid_Demand, Fleet_Size, Connector_Power_Rating, Electricity_Tariff, Weather, Calendar_Features, Hourly_Demand_Variation, Cyclical_Encodings

- **What they did:**
  - Forecast EV charging load for logistics fleets at **artificial (smart) ports**, where charging patterns are highly variable, nonlinear, and imbalanced (over-representation of peak-hour usage) — settings where linear regression/ARIMA/smoothing baselines fail.
  - Contributions: 1. **RESTNet** ensemble: ResNet (deep spatial pattern extraction via skip connections) + SENet (channel-wise squeeze-and-excitation attention) + Transformer (multi-head self-attention for long-range temporal dependencies), combined by weighted averaging. 2. **Proportional Synthetic Sampling (PSS)** with Contextual Feature Synthesis (CFS) to balance under-represented load classes. 3. **Dual-Stage …
- **Method core:** Pipeline (Algorithm 1): preprocessing → DSRS feature selection + PSS balancing → train ResNet/SENet/Transformer submodules → weighted-average ensemble → validation/tuning on MAPE/RMSE/EEE. Hyperparameters: lr=0.001, batch=64, epochs=100; i7 CPU/32 GB RAM/4 GB GPU workstation.
- **Key results:**
  - Headline results: **MAPE = 6.5%, RMSE = 9.8 kW**, EEE = 3.2%, LVD = 4.1%, CPE = \$12.50, TAA = 92.3%.
  - Statistical tests: ANOVA F=5.67 (p=0.004); Pearson correlation 0.89 (p=0.0001); Student's t=3.12 (p=0.002); Kendall's τ=0.82, Spearman's ρ=0.86; Wilcoxon signed-rank statistic 3.45 (p=0.004); chi-square-like grouped test 7.23 (p=0.009).
  - Efficiency (Table 5): highest relative efficiency score (**99%**), training time **210 s**, inference **33 ms**, model size **20 MB** (vs 45–55 MB for VGGNet/CNN/DeepSigRNet) — suitable for edge deployment. Accuracy/loss curves rise from ~70%/0.70 to ~99%/0.29 over 20 epochs without overfitting.
- **Gaps/Limitations:**
  - Future work: incorporate real-time sensor feedback streams, external energy-market signals, adaptive learning mechanisms; scale to smart-city ecosystems and decentralized energy systems.
  - Dataset is a single-location Kaggle set for port logistics fleets (not public charging stations); key result tables only available as images, limiting reproducibility of baseline comparisons.

### 2025_ResMMoT_Informer_Time_Series
**Long Short-Term Financial Time Series Forecasting Based on Residual Multiscale TCN Sparse Expert Network and Informer**  
Bao et al. · IEEE Transactions on Neural Networks and Learning Systems, vol. 36, no. 10, pp. … · 2025
<https://doi.org/10.1109/TNNLS.2025.3584369>
**Models**: ResMMoT_Informer, Sparse_Mixture_of_Experts, TCN, Informer, LSTM  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MAE, RMSE, R_squared  
**Data**: NASDAQ100_Stock_Price_Dataset; Cryptocurrency_Dataset; Forex_Dataset  
**Features**: Wavelet_Decomposition, TCN, Top_K_Gating_Routing, Positional_Encoding, Cyclical_Encodings

- **What they did:**
  - Address the gap that most stock-forecasting models handle only short-term horizons and fail to capture long-term trends, global dependencies, multiscale features, and noise robustness in highly volatile financial series.
  - Contributions:
  - **ResMMoT-Informer**: couples a **residual multiscale TCN sparse expert network (ResMMoT)** — capturing multiscale local features + long-term dependencies — with an **Informer** module for global dependencies via ProbSparse_Attention.
  - **Structurally heterogeneous TCN experts** with **Top-K sparse activation routing**, dynamically selecting/fusing features across temporal scales (unlike conventional TCNs and static expert networks).
  - **Wavelet Noise Reduction (WNR)** as a data-augmentation strategy: both denoised (smooth) and raw data are fed to the network.
  - State-of-the-art results on NASDAQ100 at horizons of 1/5/10/20 steps; ~30–40% average improvement in RMSE/MAE/R² over baselines including iTransformer, PatchTST, N-HiTS.
- **Method core:** **Framework pipeline**: raw prices → WNR preprocessing → min–max normalization → sliding windows (**input length = 3× forecast horizon**) → Informer-style embedding (temporal feature encoding + positional encoding + value/numerical encoding) → ResMMoT module → Informer module (encoder–decoder) → **Forecasting Head** (stacked 1D-CNN + LSTM layers refining/dimension-reducing …
- **Key results:**
  - **Main benchmark (Table I, NASDAQ100)**:
  - Best at all horizons (1, 5, 10, 20 steps); R² > 96% everywhere; ~30–40% average improvement in RMSE/MAE/R² vs other models.
  - **Ablation (Table II)**: TCN < Informer < TCN-Informer < ResMMoT-Informer; replacing plain TCN with ResMMoT improves accuracy further; WNR preprocessing positively impacts accuracy. Top-K routing ablation: **K = 2 gives the best accuracy/compute trade-off (highest energy efficiency)**.
- **Gaps/Limitations:**
  - The multi-expert structure of ResMMoT introduces **parameter redundancy** — future work targets parameter sharing and module compression for lighter deployment.
  - Currently univariate price-based; authors plan to add multimodal exogenous context (macroeconomic indicators, social-media sentiment).
  - Financial-domain validation only; no energy/EV experiments (transferable architecture for volatile multi-resolution load/price forecasting remains untested).
  - Sliding-window design ties input length to horizon (3× rule), not evaluated against fixed-window alternatives.

### 2025_Stochastic_MPC_Conformal_Hub
**Stochastic Model Predictive Control of Charging Energy Hubs with Conformal Prediction**  
Fernandez-Zapico et al. · IEEE Conference on Decision and Control (CDC 2025) · 2025
<https://doi.org/10.1109/CDC57313.2025.11311970>
**Models**: XGBoost (Scikit-learn GradientBoostingRegressor, MAE loss, early stopping), EnbPI conformal wrapper (MAPIE implementation), Stochastic_MPC scenario-based SOCP  
**Horizon**: day-ahead 24 h @ 15 min (load/PV, Nwq=96; price 24 h @ 1 h, Nwh=24, upsampled to 15 min) -> Day_Ahead_Forecasting  
**Metrics**: normalized average daily operational cost (% vs Omniscient), daily net CO2 emissions (%), interval coverage CPI_alpha=0.1 (PICP-type), normalized MAE (nMAE)  
**Data**: simulated Charging Energy Hub (simulated) w/ publicly available real EV charging demand data (Gholizadeh & Musilek, Data in Brief 2024); NREL OpenEI/PVDAQ Farm Solar Array PV data (California); ENTSO-E Transparency Platform NL day-ahead prices + CO2; Open-Meteo.com Weather API (NOAA HRRR historical …  
**Features**: historical load/PV/prices (lagged daily sum & std, lagged intraday 6-h sum), weather forecasts (direct/diffuse radiation, temperature, wind speed), sun position (zenith angle, solar time), calendar (month, day-of-week, arrival hour, hour), …

- **What they did:**
  - Online energy management system (EMS) for an energy hub combining EV charging, on-site PV, battery energy storage (BESS) and grid connection, minimizing operational cost. First published EMS leveraging state-of-the-art ML forecasters with **calibrated distribution-free uncertainty intervals via conformal prediction**: a probabilistic prediction module for 24-h-ahead EV charging load (Pev), PV generation (Ppv) and …
- **Method core:** **Point forecaster**: GBT additive model F(x)=F0(x)+Σ ν·ρm·hm(x) trained on absolute error (linear cost justification, following Lago et al.), early stopping on validation set (Scikit-learn `GradientBoostingRegressor`).
- **Key results:**
  - Forecast quality (280-day test): nMAE all-season Pev 0.106, Ppv 0.057, pel 0.098 (price degrades sharply in Autumn: 0.228, blamed on the 2021 gas-price regime change in the day-ahead market).
  - Coverage (CPI, α=0.1): Pev 0.90, Ppv 0.91, **pel 0.60 overall (Autumn 0.22)** — price interval badly miscovered late in year, i.e., static calibration fails under regime shift.
  - Cost (normalized to Omniscient=100 %): Deterministic 113.65, **Stochastic 112.76, Recourse 112.77** → scenario-based MPCs are **13 % pricier than perfect forecast**, only **~0.9–1 % better than deterministic point-forecast**.
- **Gaps/Limitations:**
  - **Static EnbPI calibration is not adaptive/covariate-aware**: price coverage collapses to 0.60 (0.22 in Autumn) under the 2021 regime change — motivates online/weighted conformal recalibration.
  - **Simulation only**: closed-loop simulated environment, no hardware/real-time deployment; authors suggest future work on jointly optimizing charging power levels and schedules of individual vehicles (vs aggregated demand).
  - **Independence assumption between variables** when building the scenario tree (Pev × Ppv × pel cross-correlations ignored); equal scenario probabilities ρs = 1/Ns rather than learned.
  - Point estimates already yield acceptable control performance → value of probabilistic forecasts must be argued via downstream control benefit (marginal here).

### 2025_Stochastic_MPC_Microgrid_EV
**A Stochastic Model Predictive Control-Based Energy Management Approach for Microgrids With Electric Vehicles**  
Yang et al. · IEEE Transactions on Transportation Electrification, Vol. 11, No. 1, pp. 3137-3145 · 2025
<https://doi.org/10.1109/TTE.2024.3435426>
**Models**: MS_MPC, MPC, Latin_Hypercube_Sampling, Scenario_Reduction  
**Horizon**: Short_Term_Forecasting  
**Metrics**: Operating_Cost, Unbalance_Deviation, Computation_Time  
**Data**: ELIA_Belgian_Grid; NHTS_2009  
**Features**: Arrival_Departure_Time, State_of_Charge, Wind_Power, Solar_Power, Electricity_Tariff, Baseload

- **What they did:**
  - Addresses uncertainties of EVs (arrival/departure times, initial SOC) in V2G microgrid energy management (EMS) coordinating wind turbines (WT), PV, battery energy storage (BES), an EV aggregator, and the main grid.
  - Proposes a **two-layer stochastic MPC framework**:
  - **Upper layer**: MS_MPC (multiscenario MPC) with LHS scenario sampling over EV count + arrival SOC uncertainties, minimizing total operating cost while mitigating prediction error.
  - **Scenario reduction**: a **two-stage simultaneous backward reduction** compresses thousands of sampled scenarios for computational tractability (vs. monolithic single-state EV models or brute-force scenario sets).
  - **Lower layer**: EV aggregator allocation model distributing charging/discharging power to individual EVs (including discharging/V2G, absent from prior two-layer works).
  - Simulations confirm high cost-effectiveness at affordable computational burden; unbalanced deviation between EMS operating cost and actual optimum ≈ **3.38%**, better than RBC and deterministic MPC.
- **Method core:** **System modeling** (microgrid = WT + PV + BES + EV aggregator + baseload + grid):
- **Key results:**
  - Unbalance deviation between obtained EMS operating cost and actual optimum ≈ **3.38%** for MS-MPC — smaller than RBC and D-MPC, similar to OS-MPC.
  - Qualitative findings: EV aggregator discharges during high-demand periods (8:00–12:00, 14:00–17:00) to support the microgrid; charging is shifted to low-demand windows (12:30–15:30); strategy achieves peak shaving/load leveling vs unguided random charging that concentrates load in peak-price periods; individual SOC …
- **Gaps/Limitations:**
  - Only EV-related uncertainties are modeled stochastically; WT/PV/baseload/price forecasts treated as given (authors' future work: "more uncertain elements in the microgrid").
  - Computational burden still exceeds RBC/D-MPC due to multiscenario sampling.
  - No real-world/hardware validation; simulation only, single-day case study, 100-EV fleet.
  - Forecasting itself is not learned — EV uncertainty comes from parametric (Gaussian/log-normal) distribution sampling rather than data-driven forecast models; links directly to the thesis question of how EV load forecasting quality propagates into EMS scheduling performance.

### 2025_Sundial_Highly_Capable_Time_Series_Foundation_Models
**Sundial: A Family of Highly Capable Time Series Foundation Models**  
Liu et al. · Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), PMLR 267 · 2025
<https://arxiv.org/abs/2502.00816>
**Models**: Sundial, Transformer, TimeFlow, TimesFM, Timer, Timer-XL, Time-MoE, Moirai, Chronos, LLMTime, PatchTST, N-BEATS, DeepAR, TiDE  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE, MASE, CRPS, WQL  
**Data**: TimeBench; GIFT-Eval; Chronos_Corpus; Electricity; Traffic; Weather; ETTh1; ETTh2; ETTm1; ETTm2; ECL  
**Features**: Historical_Load

- **What they did:**
  - **Research gap**: Existing time series foundation models (TSFMs) fall into two limited regimes: (1) continuous-token models fitting unimodal parametric densities via MSE/quantile loss (TimesFM, Timer, Time-MoE) which risk mode collapse on heterogeneous data and cannot convey confidence, or (2) discrete-token language-modeling models with cross-entropy (Chronos, LLMTime) which suffer quantization error, large …
  - **Core contribution — Sundial family**: First family of **native, flexible, scalable generative** TSFMs built on minimal-but-crucial Transformer adaptations and a new **TimeFlow Loss** (flow-matching) that trains autoregressively on continuous patches and samples multiple plausible futures via an ODE push-forward.
  - **Three pillars**: 1. **TimeFlow Loss**: Parameterized flow-matching objective conditioned on per-patch Transformer representations; mitigates mode collapse, enables patch-level generation and fast inference with shared lookback representation. 2. **Enhanced decoder-only Transformer**: Re-normalization (stationarization), patch embedding with binary padding mask, Pre-LN, causal self-attention with RoPE, …
  - **Empirical claim**: Sundial (Small 32M / Base 128M / Large 444M) achieves **SOTA zero-shot** on both point (TSLib long-term) and probabilistic (GIFT-Eval, FEV) benchmarks, scales monotonically with size/data, and infers in **milliseconds** with ~35× speedup over Chronos on FEV while matching N-BEATS latency. Validates that generative modeling unlocks capacity (15.38% training-loss reduction Large vs Small).
- **Method core:** **Model Type**: Decoder-only patched Transformer + conditional flow-matching head (FM-Net). Pipeline: Re-Normalization → Patch Embedding (shared MLP on concat of patch + mask) → N-layer Transformer decoder (causal, Pre-LN, RoPE) → per-token condition $h_i$ → small MLP **FM-Net** that predicts the velocity field for flow-matching and generates future patch via K-step ODE …
- **Key results:**
  - **TSLib zero-shot long-term (Table 1/9, avg over 4 horizons; lower is better, context 2880, patch 16)** — Sundial consistently #1 vs 12 TSFMs: Sundial-L achieves **-7.57% MSE / -4.71% MAE** vs previous SOTA Time-MoE with fewer parameters; continuous patch tokenization avoids the long contexts and horizon sensitivity …
  - **GIFT-Eval probabilistic zero-shot (Table 2, 97 configs, 100 samples, lower better)** — Sundial **#1 MASE / #2 CRPS** among all: Sundial calculates median/quantiles from samples **without** quantile-loss pretraining.
  - **FEV leaderboard (Fig. 4–5, 27 datasets, 20 samples, AutoGluon)** — Sundial zero-shot beats >70% of statistical + supervised deep models trained in-distribution; ranks **2nd among zero-shot FMs** after Chronos but with **35× inference speedup** (Fig. 5, log-scale): Sundial ~ near N-BEATS latency via patch-wise + …
- **Gaps/Limitations:**
  - **Univariate-only pre-training** (S3 format, per-variable normalization): No explicit cross-variate / covariate modeling; multivariate dependencies and exogenous covariates (arrival/departure, SoC, tariff, weather) left as future multivariate pretraining (increasingly studied for domain-specific TSFMs).
  - **Very high-frequency data not guaranteed**: TimeBench dominated by middle/low frequencies (ERA5 daily etc.); performance on tick/10s-level series untested — multi-scale generalization needs work (§E).
  - **Naïve sampling**: Starts from $\mathcal{N}(0,I)$ with uniform $K=50$ Euler steps; frequency normalization / advanced samplers and post-processing unexplored.
  - **Long-context high-frequency gap**: Max context 2880 patches but still may need stronger long-context capability for high-frequency series (Fig. 10: optimum lookback depends on task periodicity/horizon).
  - **Potential hallucinations** despite mode-collapse mitigation; autoregressive rolling for horizons > $F$ may yield over-smooth/unreliable tails.
  - **Probabilistic calibration limited to sample statistics**: Direct quantile optimization not used; future work could co-train TimeFlow with quantile objectives.
  - **Domain gap for EV load**: All benchmarks generic (energy/weather/synthetic), no EV charging datasets (ACN, ElaadNL, Boulder) evaluated — transfer to sparse, spiky EV loads unproven; covariate-free design is an open gap for thesis.

### 2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning
**TiRex: Zero-Shot Forecasting Across Long and Short Horizons with Enhanced In-Context Learning**  
Auer et al. · 39th Conference on Neural Information Processing Systems (NeurIPS 2025) · 2025
<https://arxiv.org/abs/2505.23719>
**Models**: TiRex, xLSTM, LSTM, Chronos, Chronos-Bolt, TimesFM, Moirai, PatchTST, TFT, DLinear, DeepAR, TabPFN-TS, TTM  
**Horizon**: Short_Term_Forecasting / Long_Term_Forecasting  
**Metrics**: CRPS, MASE, WQL  
**Data**: GIFT-Eval; GIFT_Eval_Pretrain; Chronos_Corpus; KernelSynth; Electricity_ECL; Solar_Dataset; Weather; M4; ETT  
**Features**: Historical_Load, Patched_Embeddings, Dynamic_Covariates

- **What they did:**
  - **Core Problem**: Existing pre-trained zero-shot time series foundation models (TSFMs) predominantly rely on Transformer architectures (e.g., Chronos, TimesFM, Moirai, MOIRAI-2). While Transformers excel at short-term in-context learning, they lack true recurrent state-tracking, leading to degradation on long-horizon forecasting where recurrent models like LSTMs traditionally hold an edge. Conversely, classical …
  - **Primary Novel Contribution**: 1. **TiRex Architecture**: Introduces TiRex, a 35M-parameter decoder-only foundation model built on **xLSTM** (specifically scalar LSTM / **sLSTM** blocks with exponential gating and normalizer states). TiRex bridges the gap between Transformer in-context learning and LSTM recurrent state-tracking, retaining state-tracking across long sequences. 2. **Contiguous Patch Masking (CPM)**: …
- **Method core:** ### 1. Backbone Architecture (sLSTM xLSTM Blocks)
- **Gaps/Limitations:**
  - 1. **Univariate Formulation Only**: TiRex processes multivariate time series via channel-independence (independent univariate sequences), ignoring inter-variate cross-series correlations and spatio-temporal interactions. 2. **Deterministic Context Length (2048)**: While sLSTM allows long sequences, context windows remain bounded during standard pretraining. 3. **Absence of Dynamic Exogenous Covariates**: Cannot …

### 2025_Transformer_BiLSTM_Price_Forecasting
**Enhanced Transformer-BiLSTM Deep Learning Framework for Day-Ahead Energy Price Forecasting**  
Khan et al. · IEEE Transactions on Industry Applications, vol. 62, no. 2, pp. 1933-1947 (Mar/Apr 2026 … · 2025
<https://doi.org/10.1109/TIA.2025.3599812>
**Models**: Transformer_BiLSTM, Transformer, BiLSTM, XGBoost, GRU, CNN, CNN_LSTM, BiLSTM, LSTM  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: MAE, RMSE, MAPE, sMAPE, R_squared  
**Data**: NYISO; PJM_Energy_Market_Dataset; MISO_Market_Dataset  
**Features**: Historical_Zonal_Price, Sliding_Window_Lags, Positional_Encoding

- **What they did:**
  - Hybrid deep learning framework for **day-ahead electricity price forecasting (DA EPF)** to support strategic bidding by market participants, generation companies, and network operators — relevant for EV aggregators in deregulated DA markets.
  - Contributions:
  - **Transformer-BiLSTM hybrid**: Transformer multi-head self-attention captures long-range/parallel sequence patterns; BiLSTM adds bidirectional past+future temporal context.
  - Uses **only historical price data** (no load/weather/generation covariates), robust to raw datasets containing outliers — unlike prior work requiring extensive auxiliary features and preprocessing.
  - Outperforms XGBoost, LSTM, BiLSTM, GRU, CNN, CNN-LSTM, CNN-BiLSTM, Transformer on NYISO; generalizes to PJM and MISO markets.
  - Time-series decomposition analysis of prices into trend/seasonal/residual components to guide model selection.
- **Method core:** **Pipeline**: hourly LBMP data → missing-value imputation $x_t = \frac{x_{t-1}+x_{t+1}}{2}$ → Min_Max_Scaling $x' = \frac{x - X_{\min}}{X_{\max} - X_{\min}}$ → sliding-window feature/target pairs ($X_t = D(t-1:t-T_{lag})$, target next $T$ hours) → positional encoding → Transformer encoder (LayerNorm → Multi-Head Attention → Dropout(0.1) → LayerNorm → Dense ReLU → Dropout) → …
- **Key results:**
  - **NYISO CAPITL, 2023 test set (Table I)**:
  - Gains vs Transformer: −16.98% MAE, −11.6% RMSE, −19.5% sMAPE, −15.3% MAPE, +1.8% R²; vs BiLSTM: −10.3% MAE; vs XGBoost: −12.0% MAE, −16.2% RMSE.
  - **Cross-market generalization (Table IV)**: PJM MAE 1.9291 / RMSE 3.57 / sMAPE 6.1209% / R² 0.9396; MISO MAE 1.5543 / RMSE 2.4607 / sMAPE 5.6742% / R² 0.9280 (lower volatility than NYISO).
- **Gaps/Limitations:**
  - Degrades on extreme price spikes/outliers (February/July spikes, prices > $200/MWh systematically underestimated) — no explicit spike-handling mechanism.
  - Univariate design ignores load forecasts, weather, generation mix/renewables, and other market covariates that could improve accuracy in volatile periods.
  - Highest training time of the compared models; computational cost needs optimization.
  - Stated future work: LIME/SHAP explainability; decomposition preprocessing (FFT, wavelet, VMD, CEEMDAN); multivariate inputs; reduced training/inference time.

### 2025_Vertical_Federated_EGAT_LSTM
**A Vertical Federated Learning Method for Electric Vehicle Charging Station Load Prediction in Coupled Transportation and Power Distribution Systems**  
Han et al. · Processes · 2025
<https://doi.org/10.3390/pr13020468>
**Models**: V2AFedEGAT-LSTM, EGAT, LSTM, GGNN, GAT, Time_Aware_Attention  
**Horizon**: Short_Term_Forecasting  
**Metrics**: R_squared, MAE, MAPE, MSE  
**Data**: CTPS_IEEE33_7Node_TN; CTPS_IEEE69_12Node_TN; NYISO  
**Features**: Node_Voltage, Active_Power, Reactive_Power, Line_Active_Power, Line_Reactive_Power, Traffic, Congestion_Rate, Electricity_Tariff

- **What they did:**
  - Predict EV_Charging_Station_Load (EVCSL) using **both** Distribution Network (DN) and Transportation Network (TN) characteristics under a data-privacy barrier between the two operators in a coupled transportation–power distribution system (CTPS). DN-only prediction loses TN information (congestion, charging price) that strongly drives charging choice.
  - Contributions: 1. **V2AFedEGAT-LSTM**: vertical federated (VFL) prediction combining DN + TN features via an EGAT–LSTM spatio-temporal model inside a secure federated linear regression framework (ID = aligned time points). 2. A **spatio-temporal hybrid attention** method — EGAT at local feature-extraction level (spatial skew) and a time-aware attention module at the cloud aggregation level (temporal skew) — to …
- **Method core:** **Local model**: EGAT characteristic-extraction module (edge-aggregation graph attention; learns node AND edge features of DN/TN topologies; 4-head attention, output node-feature dim 6) → LSTM load-prediction module (Seq_len 5, 2 layers, 16 hidden units, dropout 0.05). Time-aware attention input dim 32; batch 16; lr 0.005; PyCharm/Xeon Platinum 8255C.
- **Key results:**
  - **IEEE 33-bus / 7-node** (Table 2): V2AFedEGAT-LSTM **R²=0.973, MAE=0.0382, MAPE=0.0421, MSE=0.0023** vs EGAT–LSTM (0.936/0.0523/0.0542/0.0050), VFedGGNN–LSTM (0.919/…/0.0058), GGNN–LSTM (0.911/0.0593/0.0625/0.0063).
  - **IEEE 69-bus / 12-node** (Table 3): V2AFedEGAT-LSTM **R²=0.976, MAE=0.0385, MAPE=0.0425, MSE=0.0023** vs EGAT–LSTM (0.938/…/0.0049); baselines degrade more at scale while the proposed method stays stable.
  - Convergence: R² converges by ~epoch 70 vs ~100 (EGAT–LSTM) and ~150 (GGNN variants).
- **Gaps/Limitations:**
  - Collaborative cloud assumed semi-honest ("not purely malicious"); malicious-cloud inference not covered — future work on data decomposition and multi-cloud collaborative training.
  - Encrypted offline training still ~10× slower than local training (homomorphic overhead); online stage avoids encryption.
  - Only simulated dispatch-generated data (no real charging-session records); single-station target per case.

### 2026_Hybrid_XGBoost_BiLSTM_EV_Load
**Electric vehicles charging stations load forecasting based on hybrid XGBoost-BiLSTM model**  
Mansour et al. · Scientific Reports 16:374 · 2025
<https://doi.org/10.1038/s41598-025-29739-z>
**Models**: XGBoost, BiLSTM, LightGBM, Ensemble_Stacking, CNN, TCN, Transformer, SARIMAX, Prophet  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, MSE, RMSE, R_squared  
**Data**: Caltech_ACN; Synthetic_Cross_Site_EVCS_Dataset  
**Features**: kWhDelivered, Charging_Duration, Arrival_Departure_Time, Calendar_Features, Calendar_Features, Lag_Features, Rolling_Mean_Features, Holiday_Indicator

- **What they did:**
  - Short-term, hourly, **station-level** EV charging load forecasting of session energy delivered (kWhDelivered) for energy management and grid stability.
  - Contributions:
  - **Hybrid 3**: a hybrid XGBoost–BiLSTM **stacking ensemble** with an XGBoost meta-learner that learns optimal nonlinear combinations of base-learner predictions.
  - Comprehensive benchmarking against **24 baseline models** spanning statistical (Persistence, Seasonal Naïve, SARIMAX, Prophet), ML (XGBoost, LightGBM), DL (CNN, TCN, Transformer, BiLSTM), and ensemble families (boosting/bagging/stacking/weighted), plus two alternative hybrids (Hybrid 1 feature concatenation; Hybrid 2 sequential prediction fusion).
  - Five-fold walk-forward validation, one-way ANOVA significance testing, component-wise ablation, and cross-site external validation on a synthetic ~1.96M-session dataset.
- **Method core:** **Hybrid 3 pipeline**: (1) optimized XGBoost base regressor (Optuna-tuned n_estimators/max_depth/learning_rate) trained on scaled features; (2) BiLSTM with three bidirectional LSTM layers (128, 64, 64 units), L2 = 0.0001, dropout = 0.07, learning rate 0.0005 (AdamW), batch size 128, on 3D reshaped input; (3) their predictions stacked column-wise into meta-feature matrices; (4) …
- **Key results:**
  - **Cleaned data test set (Table 7)**: Hybrid 3 **MAE 2.6870 kWh / RMSE 3.9825 kWh / R² 0.6395** — 3.4% better than standalone BiLSTM (MAE 2.7816, R² 0.5950), ranked 4th overall. Best model: Boosting (XGBoost+BiLSTM+LightGBM) MAE 2.6432 / R² 0.6437; Weighted Blending/Sum (XGB+BiLSTM+LGBM) 2.6438 / R² 0.6445; LightGBM …
  - **Original (outlier-retained) data (Table 8)**: Hybrid 3 led by test MAE **3.5431 kWh / RMSE 5.9546 / R² 0.5285**, showing robustness to noise; TCN unstable (train MAE 3246 kWh).
  - **Walk-forward validation (5 folds)**: Hybrid 3 lowest mean **MAE 2.5351 kWh (SD 1.2885)** and highest mean **R² 0.6289**, but high variability (CV 0.5082); best fold MAE 1.27 kWh / R² 0.91. XGBoost (mean MAE 3.0963, CV 0.1080) and LightGBM (3.1581, CV 0.1226) more stable → preferable for real-time deployment.
- **Gaps/Limitations:**
  - Single real site (ACN-Caltech) training limits geographic/operational generalization — demonstrated by weak zero-shot cross-site transfer (R² ≈ 0.01); domain adaptation or retraining needed.
  - Heavy reliance on accurate charging-duration data, which may be unavailable for long-horizon forecasts; temporal features are overshadowed, so time-of-use/grid-event-driven variation is poorly captured.
  - High walk-forward CV (0.51) indicates sensitivity to temporal drift → periodic (e.g., monthly) retraining advised.
  - Future work: incorporate weather/electricity prices/demand-response events; reinforcement-learning-based forecast-to-control; adaptive ensemble weighting; lightweight hybrids; enhanced SHAP/attention explainability.

### 2024_Adaptive_Probabilistic_Netload
**Adaptive Probabilistic Forecasting of Electricity (Net-)Load**  
Vilmarest et al. · IEEE Transactions on Power Systems, Vol. 39, No. 2, pp. 4154-4163, March 2024 · 2024
<https://doi.org/10.1109/TPWRS.2023.3310280>
**Models**: GAM, Kalman_Filter, Quantile_Regression, Online_Gradient_Descent, Bernstein_Online_Aggregation  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: RMSE, MAE, nRMSE, nMAE, RPS, RPS, Pinball_Loss, CRPS  
**Data**: GB_Regional_Netload; US_City_Daily_Load_COVID  
**Features**: Historical_Load, Temperature_Forecast, Solar_Radiation, Wind_Speed, Embedded_Generation_Capacity, Calendar_Features, Holiday_Flag, Precipitation, Humidity, Time_of_Year

- **What they did:**
  - Address the fact that both demand and supply characteristics evolve over time (COVID crisis, price shocks, growth in EV penetration and intermittent renewables) by making **probabilistic** net-load forecasting **adaptive** (online/streaming). Two main contributions: 1. A new method based on **time-varying quantile regression with online gradient descent (OGD)** on the pinball loss, where the gradient step size is …
- **Method core:** **Offline model (Section II-A):** 1. Gaussian GAM for the conditional mean ("GAM mean decomposition equation"):  y_t = \sum_{j=1}^{d} f_j(x_{t,j}) + \varepsilon_t, \qquad \varepsilon_t \sim \mathcal{N}(0,\sigma^2) \tag{1}  where nonlinear effects $f_j$ are built from spline bases (cubic regression splines). 2. Quantile regressions on GAM residuals ("offline quantile …
- **Key results:**
  - Evaluation metrics ("RMSE / MAE equations"):  \text{RMSE} = \sqrt{\frac{1}{|T|}\sum_{t\in T}(y_t-\hat{y}_t)^2}, \qquad \text{MAE} = \frac{1}{|T|}\sum_{t\in T}|y_t-\hat{y}_t| \tag{13,14}  Aggregate normalized metrics over $N$ series (unexplained-variance interpretation):  \text{nRMSE} = \sqrt{\frac{1}{N}\sum_{1\le …
  - GB point forecasting: dynamic Kalman vs incremental offline GAM reduces nRMSE by ≈**4% in 2019, 7% in 2020, 8% in 2021**, at far lower computational cost per day (exact per-model table values in Tables I–II **not extractable** from text).
  - GB probabilistic: adapting the GAM via Kalman + keeping offline QR already gives an important nRPS gain (even for stable 2019); adding OGD-adapted QR gives a tenuous difference; BOA combination **outperforms the best single expert (oracle)**. Reliability diagrams show offline model is not calibrated, Kalman Gaussian …
- **Gaps/Limitations:**
  - Adaptation of **multivariate probabilistic forecasts** (joint dependency structures) unexplored — how to adapt marginals and dependency structures simultaneously has not been studied.
  - Only **non-extreme quantiles** considered; adaptive estimation of extremes (e.g., replacing the generalized-Pareto tail modeling of Browell & Fasiolo) is open and challenging.
  - Gaussian Kalman posterior alone poorly calibrated (fixed variance assumption violated) — motivates nonparametric residual quantile correction.
  - Gains of adaptive QR depend on regime instability (large under COVID in cities; small in stable periods/regions).
  - EV relevance: paper explicitly names expected growth in **electric vehicle penetration** as a driver of changing demand patterns requiring adaptive methods.

### 2024_Attention_Spatiotemporal_MultiGraph_EV_Load
**Load Forecasting of Electric Vehicle Charging Stations: Attention Based Spatiotemporal Multi-Graph Convolutional Networks**  
Shi et al. · IEEE Transactions on Smart Grid, Vol. 15, No. 3, pp. 3016-3029 · 2024
<https://doi.org/10.1109/TSG.2023.3321116>
**Models**: STMGCN, TCN, GCN, Chebyshev_Graph_Convolution, Graph_WaveNet, STGCN, T-GCN, LSTM, GRU, CNN_LSTM, ARIMA  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MSE, MAE, MAPE, RMSE  
**Data**: Beijing_Fast_Charging  
**Features**: Historical_Load, Temperature, Wind_Speed, Humidity, Electricity_Tariff, Distance_Graph, Similarity_Graph

- **What they did:**
  - EV charging stations couple power and transportation systems; loads are shaped by driver charging behavior plus shared traffic/weather conditions of neighboring stations — yet most prior work uses only temporal (historical load) information with fixed single-graph topologies.
  - Proposes **STMGCN** to **collectively forecast charging load at every station** via three components: gated dilated causal TCN, spatiotemporal attention (Temporal_Attention + Spatial_Attention), and a **multi-graph convolutional layer** fusing a physical distance graph and a virtual load-similarity graph.
  - Evaluated on real-world Beijing fast-charging data (10 stations); outperforms 10 baselines including statistical, recurrent, and graph models.
- **Method core:** Charging-station network modeled as undirected graph $G=(V,E,A)$, $|V|=N$; graph signal $X \in \mathbb{R}^{N\times F\times T}$ over $T$ slices; predict next $T_p$ steps $Y \in \mathbb{R}^{N\times T_p}$. **Temporal dimension** — dilated causal convolution (**Eq. 1 – Dilated causal convolution**):  q(t) * x = \sum_{s=0}^{S-1} q(s)\, x(t - d_s s)  with filter $q \in …
- **Key results:**
  - Overall test set: **STMGCN MAE = 53.287 kW, RMSE = 78.831 kW** (best); MAE reduced ~2–20 kW vs all baselines. ARIMA best statistical baseline at MAE 72.236 kW; HA unacceptable.
  - Per-station: best at station NO. 6 (regular loads): MAE 29.438 kW, RMSE 45.249 kW; hardest at station NO. 10 (highest total load), ~103 kW MAE gap vs others.
  - Multistep: STMGCN MAE 53.287 / 54.519 / 55.834 kW at 15 min / 1 h / 2 h vs CNN-LSTM 60.061 / 62.114 / 63.715 kW — slowest degradation with horizon; ARIMA drops dramatically.
- **Gaps/Limitations:**
  - Model assumes location correlations exist in historical load series; cannot capture dependencies between distant stations whose loads are uncorrelated.
  - Robustness to missing/incorrect values (common in charging datasets) not addressed — flagged as future work.
  - Hyperparameters manually tuned; small network scale (10 stations); no probabilistic/uncertainty output.
  - Traffic-flow information motivates the coupling but is not an explicit input feature.

### 2024_Autoformer_EV_Charging
**On the Utilization of Autoformer-Based Deep Learning for Electric Vehicle Charging Load Forecasting**  
Helmy et al. · 2024 6th International Conference on Communications, Signal Processing, and their … · 2024
<https://doi.org/10.1109/ICCSPA61559.2024.10794251>
**Models**: Autoformer, LSTM  
**Horizon**: Long_Term_Forecasting  
**Metrics**: RMSE, MAE, MAPE  
**Data**: Boulder_Colorado  
**Features**: Charging_Demand, Calendar_Features, Calendar_Features

- **What they did:**
  - Open-source EV charging data is scarce/limited in volume and time span, degrading the reliability of statistical (ARIMA/SARIMA) and ML (XGBoost, RF, SVM) predictors; vanilla Transformer self-attention also struggles with complex temporal patterns and needs sparse point-wise attention for long sequences.
  - Adopts **Autoformer** — decomposition Transformer with **Auto-Correlation** replacing self-attention — for **long-term EV charging load forecasting** at 30-, 60-, and 90-day horizons on an open Boulder, Colorado dataset.
  - Result: 15% RMSE improvement over benchmark LSTM at 30 days and >50% improvement at 90 days (~60% RMSE/MAE reduction), confirming Autoformer's stability for long-term horizons.
- **Method core:** Encoder–decoder Transformer with an inner series-decomposition layer and auto-correlation attention (input-I-predict-O formulation). **Series decomposition** (**Eq. 1–3 – SeriesDecomp**), based on moving averages as a built-in layer rather than preprocessing:  X_s = X - X_t, \qquad X_t = \text{AvgPool}(\text{padding}(X)), \qquad \{X_s, X_t\} = \text{SeriesDecomp}(X)  where …
- **Key results:**
  - Autoformer accuracy is essentially flat across horizons (RMSE ≈ 0.21, MAE ≈ 0.16, MAPE ≈ 35%) whereas LSTM degrades sharply — 30-day: −15% RMSE, −3% MAE, −2 pp MAPE; 90-day: ~60% lower RMSE and MAE, roughly half the MAPE.
- **Gaps/Limitations:**
  - Data aggregated **daily and across all 51 stations** — masks station-level and sub-daily fluctuations; no spatial dimension.
  - Only one baseline (LSTM); no other Transformer variants or statistical baselines evaluated.
  - High MAPE (~35%) even for Autoformer reflects difficulty of long-term EV demand prediction with limited features.
  - Authors' future work: effect of hyperparameter tuning of Autoformer using different EV charging datasets to confirm reliability against more DL models.

### 2024_BiMamba_Bidirectional_Mamba_Forecasting
**Bi-Mamba+: Bidirectional Mamba for Time Series Forecasting**  
Liang et al. · arXiv preprint (arXiv:2404.15772v3, cs.LG, 27 Jun 2024); BUPT & China Telecom Research … · 2024
<https://doi.org/10.48550/arXiv.2404.15772>
**Models**: Bi-Mamba+, Mamba_SSM  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE  
**Data**: Weather_Dataset; Traffic; Electricity_ECL; Solar_Dataset; ETT; ETT; ETT; ETT  
**Features**: Historical_Load

- **What they did:**
  - Propose **Bi-Mamba+** for long-term time-series forecasting (LTSF) with three contributions: 1. An improved **Mamba+ block** that adds a **forget gate** inside Mamba to selectively combine new features with historical features in a complementary manner, preserving historical information over longer ranges. 2. A **bidirectional Mamba+ encoder** (forward + backward Mamba+) to comprehensively model interactions among …
  - Motivation: Transformers have quadratic complexity; existing SSM uses in LTSF are limited; prior unified channel strategies (e.g., TimeMachine) choose based only on look-back length and variable count, overlooking dataset statistics.
- **Method core:** **Task setup**: given $X_{in}=[x_1,\dots,x_L]\in\mathbb{R}^{L\times M}$ predict $X_{out}=[x_{L+1},\dots,x_{L+H}]\in\mathbb{R}^{H\times M}$.
- **Key results:**
  - Protocol: L=96 for all models, H ∈ {96,192,336,720}; MSE/MAE; ADAM + early stopping, ≤40 epochs; grid-searched LR in [5e-5 … 5e-3].
  - Average improvement: **−4.72% MSE / −2.60% MAE vs iTransformer**; **−3.76% MSE / −2.67% MAE vs S-Mamba**.
  - Electricity: T=96 → 0.140/0.238 (iTransformer 0.148/0.240, S-Mamba 0.142/0.238); T=720 → 0.197/0.293 (iTransformer 0.225/0.317).
- **Gaps/Limitations:**
  - Strategy switch threshold λ can change decisions near boundaries (e.g., ts flips between λ=0.6 and λ=0.8 on ETTh2/ETTm2), though impact is small when many highly correlated variables exist.
  - Patch-wise tokens retain mostly local information with less global information compared to whole-sequence tokens (mitigated but inherent trade-off).
  - Evaluated only on generic LTSF benchmarks; future work targets more diverse/complex scenarios such as network flow forecasting — EV charging load is an untested application domain.
  - No probabilistic/uncertainty quantification of forecasts. **Relevance to EV charging load forecasting:** As a foundational method paper in the Mamba line, its bidirectional selective-SSM encoder, forget-gate history preservation, and Spearman-based automatic channel-strategy selection transfer directly to multi-station EV charging series modeling in 2026_Mamba_3_Sequence_Modeling, 2026_Mamba_KAN_HyKANet_EV, and …

### 2024_Conformal_Prediction_DER
**Hierarchical Probabilistic Conformal Prediction for Distributed Energy Resources Adoption**  
Zhou et al. · arXiv preprint arXiv:2411.12193 (v4) · 2024
<https://arxiv.org/abs/2411.12193>
**Models**: HPCP, Multivariate_Hawkes_Process, Conformal_Prediction, VAR, Gaussian_Process_Regression, Quantile_Regression, RNN, LSTM  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MAE, PICP, Interval_Size  
**Data**: Indianapolis_DER_Adoption_Dataset  
**Features**: Grid_Topology, Historical_Installation_Events, SAIDI_Outages, Feeder_Electrical_Load, Electricity_Tariff, Education_Level, Median_Household_Income, Solar_Potential_Sunroof

- **What they did:**
  - Predict **DER adoption** (rooftop solar PV installations) with **uncertainty quantification that remains statistically valid at both circuit and substation levels** of the distribution-grid hierarchy — marginal circuit-level intervals do not guarantee valid aggregated substation coverage (shown via counterexample where Y₁+Y₂ ≡ 0 escapes [2,4]).
  - Proposes **HPCP** (Hierarchical Probabilistic Conformal Prediction): a Multivariate_Hawkes_Process base predictor + tailored split Conformal_Prediction with a **topology-aware non-conformity score** using "sibling circuits".
  - Contributions: (i) distribution-free framework satisfying both coverage constraints (Eqs. 1–2); (ii) theoretical finite-sample validity under strong-mixing residuals and universal efficiency guarantees (Prop. 1: sharper than PCP-style and any ℓp-norm score); (iii) superior empirical accuracy & calibration on synthetic + real Indianapolis data.
- **Method core:** K circuits, R substations, bipartite **affiliation matrix** $C \in \{0,1\}^{K\times R}$ ($c_{k,r}=1$ ⇔ circuit k under substation r). Target: intervals $\hat{L}, \hat{U}$ such that (**Eq. 1 circuit / Eq. 2 substation level**):  P\left(\hat{L}_k \leq Y_{n+1,k} \leq \hat{U}_k\right) \geq 1-\alpha, \quad P\left([C^\top\hat{L}]_r \leq [C^\top Y_{n+1}]_r \leq …
- **Key results:**
  - **Point-prediction MAE (Table 1, rolling 2019–2023, mean ± std over 100 trials)**: Multivariate Hawkes lowest in 9 of 12 resolutions: monthly **0.06±0.02**, seasonal (3-mo) 0.21±0.08, 5-mo **0.41±0.19**, vs Discrete Hawkes (0.08/0.24/0.42), VAR (0.12/0.29/0.45), GP (0.12/0.30/0.47), LSTM (0.16/0.37/0.54), RNN …
  - **Uncertainty quantification (Fig. 7, nominal 90%)**: HPCP closest to bottom-right ideal at BOTH circuit and substation levels; VAR/GP/QR baselines either miss coverage (< reference line) or produce overly wide intervals. Marginal conformal fails substation coverage; HPCP matches Joint/Bonferroni coverage with …
  - **Sensitivity**: interval size convex in simulation size M with minimum near **M = 5** (contrasts with monotonically-improving PCP); coverage stable and exceeds target as $\hat\alpha$ varies; interval size grows ~linearly as $\hat\alpha \to 0$.
- **Gaps/Limitations:**
  - Assumes a **fixed two-level hierarchy with linear (summation) aggregation**; deeper hierarchies (pole–circuit–substation–region) and nonlinear aggregations (e.g., sigmoid voltage-stability impacts) unsupported.
  - Primarily suited to short-to-medium horizon forecasts; data-driven nature cannot anticipate events absent from history (e.g., future DER policy shifts) — long-horizon planning remains hard.
  - Requires known, static topology C; restrictive for dynamic/unknown networks (healthcare, economics, social analysis).
  - Authors' future work: non-conformity scores compatible with estimated/non-static hierarchies; richer network structures; longer-term forecasting tasks.

### 2024_Data_Driven_EVCS_Demand_Forecasting
**Data-driven Short-term Electric Vehicle Charging Station Demand Forecasting**  
Huo et al. · 2024 IEEE 7th International Electrical and Energy Conference (CIEEC) · 2024
<https://doi.org/10.1109/CIEEC60922.2024.10583059>
**Models**: MLP, SVR, XGBoost  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, RMSE, R_squared  
**Data**: Caltech_ACN  
**Features**: Historical_Load

- **What they did:**
  - Proposes a **data-driven framework** for short-term (one-step-ahead, hourly) demand forecasting at EV charging stations (EVCS), motivated by grid-operation challenges posed by surging EV charging demand (IEA: ~10 million EVs worldwide by end of 2020, +41% registrations in 2020).
  - Builds three ML forecasting models of different families — **Artificial Neural Network (MLP)**, **Support Vector Regression (SVR)**, and **Boosted Regression Trees (BRT)** — and systematically compares them.
  - Key contribution: a **hyperparameter optimization method based on the parameter-free Rao-1 evolutionary algorithm**, avoiding the algorithm-self-hyperparameter problem of GA/swarm methods.
  - Verified on real public ACN data from two stations (JPL, Caltech); all ML models beat the persistence baseline; ANN/BRT outperform SVR.
- **Method core:** Pipeline: data cleaning + feature selection → train/test split → ML model trained on training set → hyperparameters tuned by Rao-1 evolutionary computation → error evaluated on test set. **Input definition (Eq. 1 – Historical load window)**: one-step prediction using hourly load within 24 h before forecast time:  H_t = \{h_{t-1}, h_{t-2}, \cdots, h_{t-24}\}  **Generic model …
- **Key results:**
  - Metrics: MAE, RMSE, R² (Eqs. 14–16). Baseline: **persistence model (PER)**, $\hat{h}_t = h_{t-1}$. **JPL station (Table II)**: **Caltech station (Table III)**: Findings:
  - All ML models substantially beat persistence (e.g., JPL RMSE 6.93 kW ANN vs 16.34 kW PER, ≈58% reduction).
- **Gaps/Limitations:**
  - Only **univariate autoregressive** inputs ($H_t$, past 24 h): no calendar, weather, TOU price, or traffic features (contrast 2024_TOU_Price_Meteorology_EV_Charging_Load which adds TOU price/meteorology, and 2024_LASSO_BPNN_Mid_Term_EV_Load which adds socio-economic indicators).
  - One-step (1 h ahead) only; no multi-step or day-ahead horizons.
  - Two workplace stations only (same ACN source); no cross-station/cross-region generalization testing.
  - No uncertainty/probabilistic forecasts; point predictions only.
  - Hyperparameter search cost of wrapping Rao-1 around retraining not quantified in detail.

### 2024_Day_Ahead_EVCB_EVSC_Parking_Lot
**Day-ahead Electric Vehicle Charging Behavior Forecasting and Schedulable Capacity Calculation for Electric Vehicle Parking Lot**  
Xu et al. · Energy, vol. 309, 133090 · 2024
<https://doi.org/10.1016/j.energy.2024.133090>
**Models**: ADMM-NN, KMeans_Clustering, EVSFD, Monte_Carlo_Sampling  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: Forecast Accuracy, Charging Cost Reduction  
**Data**: Suzhou_EVPL_Dataset; PJM_Day_Ahead_Tariff; NMMV_Platform_Data  
**Features**: EV_Access_Time, Access_Duration, State_of_Charge, State_of_Charge, Calendar_Features, Holiday_Flag, Weather_Conditions, Temperature, Recent_Access_Pattern

- **What they did:**
  - Enables **Electric Vehicle Parking Lots (EVPLs)** to participate in day-ahead energy and ancillary services markets via V2G by forecasting **EV Charging Behavior (EVCB)** day-ahead and computing **EV Schedulable Capacity (EVSC)** from those forecasts.
  - Three contributions: (1) a **day-ahead Time-of-Use (TOU) EVCB forecasting method** combining an ADMM-NN for hourly EV access numbers with TOU KMeans_Clustering clustering of historical EVCB into typical behavior sets (376 clusters), minimizing idealized assumptions; (2) classification of EVCB types + construction of the **EV Scheduling Feasible Domain (EVSFD)** under physical constraints; (3) an EVSC calculation …
  - Contrasts with model-driven Monte Carlo/PDF approaches (require assumptions on EV counts/targets/durations — infeasible when daily EVPL access varies with climate/date/user willingness) and data-driven load-profile methods (only forecast disorderly charging profiles, unusable for V2G scheduling).
- **Method core:** Day split into 24 one-hour periods; one model per period. Inputs: day-of-week, holiday flag, weather (sunny/cloudy/rainy/snowy), average temperature, recent-days access-number pattern. Architecture: **10 → 200 → 200 → 1** neurons; output (**Eq. 4**):
- **Key results:**
  - **Case 1 (access number)**: NN forecasts hourly EV access numbers for 29 January with **88.5% average accuracy**; Monte Carlo baseline cannot even produce this forecast since total daily EV count is unknown a priori.
  - **Case 2 (clustering)**: **376 typical EVCB clusters** across 24 periods; most accesses/clusters occur evening–late night (peak hour [21,22): 2150 EVs, 32 clusters). Of typical EVCBs, **76.3% have $t^{ad}>2h$** (46.3% >4 h, 32.2% >6 h); **67.6% expect $S^{ad}>40\%$** (35.9% >60%, 9.8% >80%).
  - **Case 3 (EVCB forecast)**: forecast distributions closely match actuals, e.g., $S^d$: 87.9% actual vs 88.4% forecast in (80,100] bin; duration distribution: >2 h actual 68.2% vs forecast 73.2%; >6 h 25.0% vs 23.3%.
- **Gaps/Limitations:**
  - Only slow-charging EVs modeled; fast-charging loads treated as uncontrollable.
  - Real-time scheduling strategy impact on EVSC calculation not analyzed — flagged as future work.
  - Further research planned on EVSC mining across different scenarios/EV clusters in EVPLs.
  - Cluster-C EVs (no feasible domain) contribute nothing to V2G; incentive design could target longer access durations.

### 2024_DiffPLF_Conditional_Diffusion_EV
**DiffPLF: A Conditional Diffusion Model for Probabilistic Forecasting of EV Charging Load**  
Li et al. · 23rd Power Systems Computation Conference (PSCC 2024), Paris, France, June 4-7 2024 · 2024
<https://doi.org/10.1016/j.epsr.2024.110723>
**Models**: DiffPLF, DDPM, TimeGrad, CSDI, Quantile Regression, LSTM  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: MAE, CRPS  
**Data**: Palo_Alto_EV; Weather  
**Features**: Historical_Load, Temperature_Forecast, Humidity, Calendar_Features, EV_Number

- **What they did:**
  - Probabilistic EV_Charging_Demand: explicitly approximate the predictive distribution $q(x_0|p,r)$ of future charging load profiles conditioned on historical demand and covariates, instead of point forecasts or quantile regression (which struggles with the extreme volatility and conditioning information of EV charging).
  - Proposes **DiffPLF**: a conditional denoising diffusion model (DDPM) with a **cross-attention conditioning mechanism** (from latent diffusion / text-to-image models) entangling perturbed load series with conditions; plus a **task-informed fine-tuning** stage via a 50%-quantile deviation minimization (QDM) loss that sharpens prediction intervals (~40% improvement vs standard quantile regression training).
  - Results: **39.58% MAE and 49.87% CRPS improvement** over conventional quantile regression; supports controllable generation conditioned on EV number and flexible horizons (24/12/6/4/1 h). Code public: https://github.com/LSY-Cython/DiffPLF
- **Method core:** Problem: context window $\omega$ of past charging demand $p_i \in \mathbb{R}, i\in[s-\omega,s]$; covariate set known in advance over horizon $\tau$: weather forecasts (temperature $u\in\mathbb{R}^\tau$, humidity $v\in\mathbb{R}^\tau$), one-hot day-of-week $d\in\mathbb{R}^7$, EV number $e$; i.e., $r=\{u,v,d,e\}$. Goal: sample plausible future profiles from $q(x_0|p,r)$. Forward …
- **Key results:**
  - Day-ahead forecasting (24 h horizon, past-5-days context), median-of-1000 as point forecast:
  - vs quantile regression: **−39.58% MAE, −49.87% CRPS**.
  - Covariates contribute 9.5%/10.4% on MAE/CRPS; cross-attention beats latent feature-fusion by >0.12 on both metrics; partial fine-tuning (denoising front only, freezing cross-attention/encoder weights) beats whole-model fine-tuning.
- **Gaps/Limitations:**
  - Requires a separate task-informed fine-tuning stage for accuracy — authors target a more efficient **end-to-end diffusion model** specialized for probabilistic load forecasting.
  - Performance sensitive to diffusion steps T; principled selection of T per scenario left as future work.
  - Univariate/station-level scope; extension to **multivariate diffusion** generative models for EV charging and general energy time-series is future work.
  - Long-term (multi-day) forecasting for charging-infrastructure planning not yet addressed; benchmarking across different EV charging dataset patterns suggested.

### 2024_Divide_Conquer_Transformer_EV
**Divide-Conquer Transformer Learning for Predicting Electric Vehicle Charging Events Using Smart Meter Data**  
Ke et al. · arXiv preprint (arXiv:2403.13246) · 2024
<https://arxiv.org/abs/2403.13246>
**Models**: DCT-EV, Transformer, Random_Forest, XGBoost, ANN, LSTM  
**Horizon**: Short_Term_Forecasting  
**Metrics**: F1_Score, AUC, Average_Precision, Accuracy, MSE, Precision, Recall  
**Data**: Pecan_Street  
**Features**: Smart_Meter_Load, Electricity_Usage, EV_Charging_Label

- **What they did:**
  - **Problem**: Predict **home** EV charging events using only historical Smart_Meter_Load data — at-home charging is behind-the-meter and invisible to grid operators, so historical charging profiles are unavailable (unlike public-station forecasting).
  - Inspired by NILM but goes beyond detection of past charging: provides *predictive* information about future charging occurrences.
  - **Contributions**: 1. New practical task formulation: home-charging event prediction from residential meter data alone. 2. **DCT-EV** (Divide-Conquer Transformer EV): non-intrusive, minute-interval model that divides long meter sequences into overlapping sub-sequences processed in parallel through a self-attention Transformer backbone (self-attention Transformer encoder, cf. 2017_Attention_Is_All_You_Need). 3. …
- **Method core:** Three modules: **Load Embedding → EV Representation Learning → Charging Event Prediction**. 1. **Load Embedding Module** ("divide" step): input sequence $\boldsymbol{x} = x_1,...,x_t,...,x_T \in \mathbb{R}^{1\times T}$ is split into $N = \frac{T-L}{stride}+1$ overlapping sub-sequences ($\bar{\boldsymbol{x}} = \{\boldsymbol{x}_1,...,\boldsymbol{x}_N\} \in \mathbb{R}^{N\times …
- **Key results:**
  - **1–10 minutes ahead** span: DCT-EV F1@.5 = **87.35%**, AUC = **97.90%**, AP = **88.55%**, ACC@.5 = **98.80%**, MSE = **0.0102**, beating LSTM (83.91%/97.73%/86.89%/98.74%/0.0103), DNN, XGBoost (83.43% F1), Random Forest (22.14% F1).
  - **1–60 minutes ahead**: DCT-EV F1@.5 = **63.78%**, AUC = 90.07%, AP = 61.59%, ACC = 96.81%, MSE = 0.0251 vs LSTM 55.94% F1 / 96.68% ACC / 0.0260 MSE and DNN 49.74% F1. ML baselines dropped out due to poor performance.
  - Per-minute degradation (Table II): 1-min ahead AUC 99.63%, F1 90.88% → 10-min ahead AUC 94.78%, F1 81.59%.
- **Gaps/Limitations:**
  - Performance degrades substantially with longer predictive spans (1–60 min much weaker than 1–10 min); far-future minute-level event prediction remains hard.
  - Supervised labels derived from a fixed >3 kW heuristic; requires EV-charging-aligned ground truth during training even though inference needs only meter data.
  - Single-dataset (Austin, TX) evaluation; no cross-region generalization or transfer learning tests.
  - Class imbalance inherent to sparse home-charging events not explicitly addressed (no re-weighting/resampling reported).

### 2024_EV_Load_Forecasting_DAM
**Electric vehicles load forecasting for day-ahead market participation using machine and deep learning methods**  
Bampos et al. · Applied Energy 360 (2024) 122801 · 2024
<https://doi.org/10.1016/j.apenergy.2024.122801>
**Models**: XGBoost, MLP, CNN_Dense, CNN_LSTM, TCN, SARIMA, Persistence_Model, Holt_Exponential_Smoothing  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: nMAE, nRMSE, R_squared  
**Data**: Palo_Alto_EV; CrowdCharge_EV; Greenflux; Caltech_ACN  
**Features**: EV_Charging_Demand, Trend_Residual_Decomposition, Cyclical_Encodings, Calendar_Features, Holiday_Flag, Lag_Features

- **What they did:**
  - First-of-its-kind systematic benchmark of **9 EV Load Curve (EVLC) forecasting methods** (statistical, ML, DL) designed specifically for the operational requirements of **Day_Ahead_Forecasting (DAM)** participation by EV aggregators/suppliers.
  - **36-h ahead hourly horizon** aligned with European DAM gate closure at 12 pm CET (first 12 h omitted → day-ahead 24 h forecast); conservative offline scenario extends to 48 h with 24 h omitted.
  - Compares models **with online data ("sc") vs without online data ("wo, sc")**; evaluates over a **full year of rolling daily simulations** to expose seasonal variation.
  - Provides a step-by-step methodology for **constructing hourly EVLCs from session-based tabular charging data**.
- **Method core:** **Two-component decomposition**: EVLC is split into trend + residual; each is forecast separately and recombined multiplicatively. 1. **EVLC construction from sessions** — assume constant power per session (**Eq. — Charging power**):  P_i = \frac{E_i}{t_i}  ($E_i$ = session energy [kWh], $t_i$ = actual charging duration [h]; plug-in ≠ charging duration). Per-second aggregate …
- **Key results:**
  - **Key findings**: simple ML (XGBoost, MLP) beats all complex DL models on nearly every dataset/metric. Best gains vs baseline: XGBoost$_{sc}$ +1.058% nMAE (Palo Alto); MLP$_{sc}$ +1.707% nMAE (Crowdcharge), +0.914% nMAE & +1.355% nMSE (Greenflux); MLP$_{wo,sc}$ +0.673% nMAE (ACN). Only TCN$_{sc}$ beat the baseline on …
  - On the small Caltech_ACN set, offline simple models outperformed online ones; DL architectures overfit (CNN-Dense R² = −0.9).
  - Online data helps but only marginally (~0.5–1%) → robust DAM forecasting possible without real-time feeds.
- **Gaps/Limitations:**
  - No probabilistic/quantile forecasts — point forecasts only, though DAM bidding and risk management need uncertainty quantification.
  - Best improvements over persistence are modest (<2%); no model dominates across datasets → no one-size-fits-all approach; performance tied to fleet characteristics (location, size, user habits).
  - Bid price strategy explicitly out of scope (quantity-only bidding).
  - DL underperformance suggests room for architectures/data regimes that handle small or volatile fleets; September-type anomalous peak events degrade all models.
  - Constant-power-per-session assumption in EVLC construction simplifies real charging curves.

### 2024_Feature_Enhanced_Probabilistic_EV_Load
**Feature-enhanced deep learning method for electric vehicle charging demand probabilistic forecasting of charging station**  
Cao et al. · Applied Energy 371 (2024) 123751 · 2024
<https://doi.org/10.1016/j.apenergy.2024.123751>
**Models**: FEDM, GRN, GLU, LSTM, Transformer, NBEATS, DeepAR, TCN, Temporal_Fusion_Transformer, LGBM, ARIMA, ESM, Persistence_Model  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: Qualified_Rate, Accuracy, Winkler_Score, AIW, Pinball_Loss, SMAPE, RMSE, R_squared, NRMSE, MAPE  
**Data**: Shenzhen_ST_EVCDP  
**Features**: Pearson_Correlation_Coefficient, Electricity_Tariff, Temperature, Calendar_Features, Weather_Conditions, Charging demand series

- **What they did:**
  - Proposes **FEDM** (Feature-Enhanced Deep Learning Method) for **station-level day-ahead probabilistic EV charging demand forecasting** under **low historical data stock** (12–24 days of training data).
  - Key novelty: a **two-stage feature selection model** injecting the Pearson_Correlation_Coefficient between charging demand and external features as *prior knowledge* to initialize feature-importance weights — instead of feeding all features equally.
  - Contributions: (1) improves accuracy rate, qualified rate, sharpness and computational efficiency vs 8 benchmarks; (2) correlation-coefficient-as-prior reweighting mechanism; (3) excellent performance with low data volume; solves the trend-lagging defect of non-enhanced models via GRN + multi-head self-attention.
- **Method core:** Pipeline: external features (static: date/weekday/holiday; dynamic: TOU price, temperature, weather) → two-stage feature selection → LSTM intermediate layer(s) → GRN with residual connections → multi-head self-attention → quantile outputs → PIs via Monte Carlo sampling. **Preliminaries**: Quantile definition (**Eq. 1**): $q_t^{(a)} = \inf\{y | F_t(y) \geq a\}$; approximate CDF …
- **Key results:**
  - **Feature-enhancement ablation (20-day training)**: FEDM vs FEDM w/o two-stage selection: RMSE 175.1 vs ~228–390 across seasons; SMAPE 7.95–9.89% vs 16.8–20.6%; R² up to 0.9839; **AR +8.3%, QR +3.1%, WS reduced by 33.64%**; fixes inaccurate fitting and trend lagging.
  - **Initial-weight ablation (Table IV)**: Case 1 (|r|≥0.1 prior, zeros below) best: QR 99.22%, WS −0.4323; all-r weights 98.44%/−0.4625; equal weights 96.88%; random weights worst (95.83%/−0.5413).
  - **Benchmark comparison (90% level)**: FEDM average **QR = 99.22%** (100% in spring & summer; best benchmark spring NBEATS 96.88%, summer DeepTCN/TFT 94.79%), i.e., **+5.21% over NBEATS, +4.54% over DeepTCN**. FEDM average **WS = −0.4323** vs DeepTCN −0.6443, NBEATS −0.6606, TFT −0.6951, LGBM −0.6820, ESM −0.8764, …
- **Gaps/Limitations:**
  - Single-station focus — authors flag extension to **spatio-temporal multi-station forecasting** as future work.
  - Assumes future values of exogenous features (price, weather, temperature) are reliably known.
  - Linear (Pearson-only) prior may miss nonlinear feature-demand relations; threshold |r| ≥ 0.1 is heuristic.
  - Point-interval construction relies on Monte Carlo dropout sampling rather than full distributional modeling.
  - Future work: more external features, integration into EV demand scheduling and renewable-energy complementarity applications.
  - Dataset access requires request (limited reproducibility despite GitHub link).

### 2024_Forwardformer_Day_Ahead_Load
**Forwardformer: Efficient Transformer With Multi-Scale Forward Self-Attention for Day-Ahead Load Forecasting**  
Qu et al. · IEEE Transactions on Power Systems, Vol. 39, No. 1, pp. 1421-1433, January 2024 · 2024
<https://doi.org/10.1109/TPWRS.2023.3266369>
**Models**: 2024_Forwardformer_Day_Ahead_Load, Transformer, Autoformer, FEDformer, Informer, LogTrans, LSTMa, Prophet, SARIMA  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: MSE, MAE, Accuracy  
**Data**: CEL_NW_China_Electric_Load; CEL_SE_China_Electric_Load; AEL_CNYS_America_Electric_Load; AEL_NNYS_America_Electric_Load; AEL_WNYS_America_Electric_Load  
**Features**: Historical_Load, Calendar_Features, Holiday_Flag, Temperature, Humidity, Rainfall, Pressure, Temperature

- **What they did:**
  - Design a Transformer purpose-built for **day-ahead load forecasting (DALF)** that (i) removes sequential computation and captures long-term dependence between distant special days, and (ii) explicitly targets the under-served problem of forecasting **special days (weekends and holidays)**. Contributions: 1. A **correction structure based on an encoder-dual decoder** improving DALF accuracy. 2. **Multi-scale forward …
- **Method core:** **Encoder-dual-decoder architecture:** Encoder ($N=4$ layers) with multi-head MSFSA sublayer + FFN sublayer:
- **Key results:**
  - Metrics ("MSE / MAE / ACC definitions"; MSE/MAE computed on zero-mean-normalized values $y_i^*=(y_i-\mu)/\sigma$, ACC on original magnitudes):  \begin{cases} \text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i^* - \hat{y}_i^*)^2\\[4pt] \text{MAE} = \frac{1}{n}\sum_{i=1}^{n}|y_i^* - \hat{y}_i^*|\\[4pt] \text{ACC} = …
  - Overall best ACC across all methods: **Forwardformer 98.51% (China) and 96.94% (America)**; smallest errors in most cases (full per-dataset Table I values **not extractable** from text).
  - Best baseline: PED/FEDformer with ACC **97.71% / 95.87%**, second to Forwardformer everywhere.
- **Gaps/Limitations:**
  - Hyperparameters chosen by grid search balancing accuracy vs runtime, not guaranteed globally optimal (e.g., N=6 might be slightly more accurate than N=4 but too slow).
  - MSFSA efficiency relies on a custom CUDA/TVM kernel requiring low-level GPU programming knowledge.
  - Future work stated by authors: day-ahead **load peak forecasting under special events**; transferring MSFSA to wind power and photovoltaic forecasting with targeted improvements.
  - Point forecasts only — no probabilistic/uncertainty quantification.
  - Datasets not released via public links in the paper (reproducibility gap).

### 2024_KAN_Kolmogorov_Arnold_Networks
**KAN: Kolmogorov-Arnold Networks**  
Liu et al. · arXiv:2404.19756 (accepted at ICLR 2025); MIT / Caltech / Northeastern / IAIFI · 2024
<https://doi.org/10.48550/arXiv.2404.19756>
**Models**: KAN, MLP, LAN  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MSE, L2_Error, H1_Error, Accuracy  
**Data**: Toy_Synthetic_Functions; Special_Functions_Dataset; Feynman_Dataset; Knot_Theory_Dataset; Anderson_Localization_Synthetic_Data  
**Features**: B-Spline_Basis_Functions, Learnable_Edge_Activations, Silu_Basis_Function

- **What they did:**
  - Proposes Kolmogorov-Arnold Networks (KANs) as alternatives to Multi-Layer Perceptrons (MLPs). While MLPs have **fixed activation functions on nodes** ("neurons"), KANs have **learnable activation functions on edges** ("weights") — every linear weight parameter is replaced by a univariate function parametrized as a B-spline. Contributions: 1. Generalization of the original depth-2 width-(2n+1) Kolmogorov-Arnold …
- **Method core:** For a smooth $f : [0,1]^n \to \mathbb{R}$:  f(\mathbf{x}) = f(x_1,\cdots,x_n) = \sum_{q=1}^{2n+1} \Phi_q \left( \sum_{p=1}^{n} \phi_{q,p}(x_p) \right),  where $\phi_{q,p} : [0,1] \to \mathbb{R}$ and $\Phi_q : \mathbb{R} \to \mathbb{R}$ are univariate continuous functions ("the only true multivariate function is addition"). A KAN layer with $n_{in}$ inputs and $n_{out}$ …
- **Key results:**
  - **Scaling laws (Fig. 3.1)**: KANs nearly saturate the theoretical $\alpha = 4$ exponent (test RMSE $\propto N^{-4}$) on all five toy tasks including the 100-dim example; MLPs scale slowly (≈ $N^{-2}$ or worse) and plateau quickly.
  - **Special functions (Table 1)**: KANs Pareto-dominate MLPs on all 15 functions; examples — ellipj: best KAN RMSE $1.33\times10^{-4}$ vs MLP $6.48\times10^{-4}$; lpmv(0,x,y): KAN $5.25\times10^{-5}$ vs MLP $1.74\times10^{-2}$; sph_harm(0,1): KAN $2.21\times10^{-7}$ vs MLP $1.25\times10^{-6}$.
  - **PDE solving (Poisson, PINN framework, Eq. 3.2)**: a 2-layer width-10 KAN is **100× more accurate** than a 4-layer width-100 MLP ($10^{-7}$ vs $10^{-5}$ MSE) with **100× fewer parameters** ($10^2$ vs $10^4$); steeper scaling laws in both L2 and H1 norms; but KAN training ≈10× slower.
- **Gaps/Limitations:**
  - **Slow training**: KANs are typically **10× slower than MLPs** for the same parameter count (no batch computation across distinct activations); authors deem it an engineering problem (multi-head/grouped activations proposed).
  - No generalized "deep" Kolmogorov-Arnold theorem exists; mathematical understanding of deeper KANs and dimension-dependence of constant $C$ left as future work.
  - Results demonstrated only on **small-scale AI + Science tasks**; unclear whether fast scaling holds for large tasks (e.g., language modeling).
  - Grid-size updates near the number of training points cause sudden performance drops (Appendix E); interpretability can be subtle since pruning may squash information into smaller graphs; unsupervised relation discovery relies on random seeds.
  - For EV forecasting (2026_Mamba_KAN_HyKANet_EV context): vanilla KANs' computational cost motivates hybrid architectures combining KAN decoders with efficient sequence backbones rather than pure KAN stacks.

### 2024_LASSO_BPNN_Mid_Term_EV_Load
**Mid-Term Load Forecasting for Electric Vehicle Charging Stations Based on LASSO-BPNN**  
Ma et al. · 2024 IEEE 2nd International Conference on Control, Electronics and Computer Technology … · 2024
<https://doi.org/10.1109/ICCECT60629.2024.10546219>
**Models**: MLP, XGBoost, SVR, Random_Forest  
**Horizon**: Long_Term_Forecasting  
**Metrics**: RMSE, MAPE  
**Data**: Qingpu_State_Grid_EV_Stations; Shanghai_Qingpu_Statistics_Bureau  
**Features**: Historical_Load, Weather_Traffic, Economic_Indicators, Social_Indicators

- **What they did:**
  - Proposes **LASSO-BPNN**, a combined model for **mid-term (monthly) load forecasting of EV charging stations**, addressing the gap that most EV charging-load research targets short/super-short-term horizons and considers only weather + time series.
  - Contributions: (a) combined LASSO→BPNN pipeline that **selects station-type-specific influencing factors**; (b) a broadened 15-indicator system spanning **environmental, economic, and societal** factors (beyond weather-only prior work); (c) multi-scenario design with four charging-station types (Residential / Office / Attraction / Highway areas) to support State Grid planning decisions in Qingpu District, Shanghai.
  - Motivation: stations in the same district share weather yet show divergent load trends → non-weather (economic/social) drivers matter; mid-term forecasts serve the **system planning phase** during rapid charging-infrastructure build-out.
- **Method core:** Five-step pipeline: collect load (State Grid) + factor data (statistics bureau monthly reports) → preprocess (missing values, normalization, four areas) → **LASSO** regression per area to screen variables by coefficients → per-area **BPNN** trained on selected variables with **grid search + cross-validation** hyperparameter tuning → evaluation. **Eq. 1 – LASSO estimator** (L1 …
- **Key results:**
  - Test sets: April–July 2023 (Residential: May–July 2023). Comparators: BPNN alone, LASSO-SVR, LASSO-XGBoost, LASSO-RF. **Caveat: Table III's model-label column is misaligned/duplicated in the source text ("LASSO-RF" appears twice, header row shifted); row-to-model assignment below follows the printed label sequence and …
  - **LASSO-BPNN outperforms plain BPNN** — e.g., best-case Residential RMSE improves from 28.863 to 20.631 (≈29% lower) and MAPE 11.726% → 8.639%; gains most visible under large load fluctuations.
- **Gaps/Limitations:**
  - Very short history (13 monthly points; 12 for Residential) → severe sample-size constraint motivating LASSO regularization but limiting deep-learning alternatives; authors acknowledge time constraints of a nascent industry.
  - Monthly granularity only; authors' stated future work: extend to **shorter periods** and apply to grid scheduling and charging-station siting optimization.
  - Table III presentation defects make exact quantitative comparison non-reproducible from text alone.
  - Load data proprietary (State Grid internal) → external validation impossible; no confidence intervals/uncertainty estimates.
  - Feature pool limited to Qingpu/Shanghai statistics-bureau indicators; transferability to other districts untested.

### 2024_LSTM_Transformer_EV_Consumption
**Energy Consumption Prediction Strategy for Electric Vehicle Based on LSTM-Transformer Framework**  
Feng et al. · SSRN Preprint 4747046 (not peer reviewed) · 2024
<https://ssrn.com/abstract=4747046>
**Models**: LSTM_Transformer, LSTM, Transformer, KMeans_Clustering, Linear_Regression  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAPE, MAE, RMSE  
**Data**: GBT_32960_Telemetry_Dataset  
**Features**: Battery_SOC, Vehicle_Speed_Features, Acceleration_Ratios, Wind_Speed, Temperature, Visibility, Driver_Style, Driving_Condition_Clusters, Cruise_Time_Ratio

- **What they did:**
  - Mitigate driver **range anxiety** via accurate real-time EV battery Battery_SOC / energy consumption prediction, integrating vehicle, environmental, **driver style**, and **driving condition** factors.
  - Contributions: 1. **LSTM_Transformer hybrid framework** — LSTM layer extracts short-term temporal dependencies; Transformer encoder layers capture long-range dependencies; linear output head. 2. Comprehensive energy-consumption factor framework (18 features) with special emphasis on individual driving styles and driving-condition recognition via KMeans_Clustering. 3. Novel **long-distance prediction strategy built …
- **Method core:** Vehicle factors (**Eq. 1**): $V = (x_1, x_2, x_3 \cdots x_{15})$ — average speed, speed range/std-dev, mean squared speed, average acceleration, accumulated/segment mileage, acceleration/deceleration/constant-speed segment ratios, low-/medium-/high-speed ratios, accel-decel switching frequency, cruise time ratio. Environmental factors (**Eq. 2**): $T = (x_{16}, x_{17}, …
- **Key results:**
  - **400-s window test set (10 drivers)**: LSTM_Transformer avg **MAPE = 4.63%**, MAE ≈ 0.027, RMSE ≈ 0.036; standalone LSTM MAPE = 10.69% (+6.06%); Linear_Regression MAPE = 21.87%. Per-driver best/worst: B3 MAPE 3.0%, A5 5.9%.
  - **Window sensitivity**: MAPE = 13.9% (200 s), **4.6–4.63% (400 s, best)**, ~5.1% (600 s), 8.3% (1000 s) — too-short windows lose motion context at 0.05 Hz sampling; too-long windows dilute fine-grained detail.
  - **Ablation**: removing driver-style personalization raised MAPE by up to **18.47%**; removing driving-condition features raised it by **15.27%**; ignoring both increased MAPE by 12.4%/17.0%/16.5%/14.0% at 200/400/600/1000 s.
- **Gaps/Limitations:**
  - Small, single-region dataset (10 vehicles, China); authors explicitly call for validation on broader datasets under diverse geographic/climatic conditions.
  - Battery state-of-health (SOH) not modeled — future work for extended-range prediction.
  - Feature engineering limited to powertrain subsystems; other vehicle subsystem data unexploited.
  - Long-distance accuracy depends on data quality; error accumulation possible during stage-wise SOC roll-forward.
  - Preprint, not peer-reviewed; no public code/data release.

### 2024_MQ_TCN_Transfer_Learning_EV
**Location based Probabilistic Load Forecasting of EV Charging Sites: Deep Transfer Learning with Multi-Quantile Temporal Convolutional Network**  
Ali et al. · arXiv preprint arXiv:2409.11862 (Sep 2024) · 2024
<https://doi.org/10.48550/arXiv.2409.11862>
**Models**: MQ_TCN, TCN, Meta_Learning, Quantile_Regression, XGBoost, DeepAR  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: PICP, Pinball_Loss, Winkler_Score, ND  
**Data**: Caltech_ACN; NREL_Workplace_Charging  
**Features**: Historical_Load, Calendar_Features, Cyclical_Encodings, StationID_Embedding, Adjacency_Matrix

- **What they did:**
  - Prior EV charging-site load models are use-case/location specific, need large data + compute, give point forecasts without uncertainty, and ignore high-cardinality categorical features.
  - Proposes **MQ_TCN** (Multi-Quantile TCN) with **Meta_Learning** to transfer day-ahead forecasting knowledge among geographically separated charging sites under extreme data scarcity and low compute.
  - Key results: PICP 93.62% at JPL (**+28.93% over XGBoost**, day-ahead); with TL from JPL, **PICP 96.88% at NREL using only 2 weeks of data** (+18.23% vs XGBoost trained on 6 months); Office-1 91.04% (4 h-ahead) / 87.30% (day-ahead) with only 1 month of data; up to **72% reduction in learnable parameters** at negligible accuracy cost (~3.4% PICP).
  - First (per authors) combination of multi-step quantile regression DL + inductive TL across separated EV sites; site selection for transfer guided by **Dynamic Time Warping (DTW)** similarity.
- **Method core:** **Problem**: multivariate series $X=\{x_t\}_{t=1}^T \in \mathbb{R}^{T\times d}$ (d non-predictive covariates), target $Y\in\mathbb{R}^{T\times1}$; forecast $\{\hat{y}_t\}_{t=T+1}^{T+\delta} = F(\{x_t\},\{y_t\})$ δ steps ahead; TL learns target function $f_{td}(.)$ from source domain $\mathcal{D}_{sd}$ to resource-constrained target site $\mathcal{D}_{td}$ …
- **Key results:**
  - Source domains (lookback/horizon in hours; quantiles 0.05/0.50/0.90):
  - **JPL (168→24)**: MQ-TCN PICP **93.62%**, Pinball 2.28, WS 21.55, ND 0.2226 vs XGBoost PICP 64.69%, ND 0.1770, DeepAR ND 0.1770 → +28.93% coverage improvement over XGBoost.
  - **JPL (168→48)**: MQ-TCN PICP 75.50% vs XGBoost — none (XGBoost row 78.96 belongs to Caltech); DeepAR ND 0.2955 vs MQ-TCN 0.2266.
- **Gaps/Limitations:**
  - Authors: model "failed in some novel situations" under transfer — future work on continual representation learning and adding meta-information.
  - No conclusive guidance on lookback/horizon choice; sensitivity is site-specific.
  - High NREL Winkler Scores despite high PICP indicate wide intervals (over-coverage without sharpness guarantees).
  - Single-step DeepAR comparisons limited (DeepAR could not support some single-step settings); point-forecast baseline (ND) favors XGBoost/DeepAR even when interval quality is poor.
  - Only quantile regression (no full predictive density); US workplace/public sites only.

### 2024_Physics_Informed_GAT_EV_Load
**A Physics-Informed and Attention-Based Graph Learning Approach for Regional Electric Vehicle Charging Demand Prediction**  
Qu et al. · IEEE Transactions on Intelligent Transportation Systems, vol. 25, no. 10, pp. 14284-14297 · 2024
<https://doi.org/10.1109/TITS.2024.3401850>
**Models**: PAG, PIML, GAT, TPA-LSTM, LSTM, FourierGNN, AST-GAT, DCRNN, STGCN, HSTGCN, GCN-LSTM, GCN, FCNN, VAR, Lasso, KNN  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAPE, RAE, MAE  
**Data**: Shenzhen_ST_EVCDP  
**Features**: Station_Occupancy, Charging_Price, Price_Elasticity_of_Demand, Spatial_Spillover

- **What they did:**
  - Solves **price misinterpretation** in data-driven EV_Charging_Demand: models trained on partially observed data learn "higher price → higher demand" because peak-price hours coincide with peak demand, which is fatal for pricing-policy decision support.
  - Proposes **PAG**: (a) a **graph embedding module** (GAT + temporal CNN), (b) a **multivariate decoder module** (TPA-LSTM) with revised hop-wise/sequence-wise attention, and (c) a **model pre-training module** based on **Physics-Informed Meta-Learning (PIML)** that generates synthetic tuning samples from economic laws (price elasticity of demand) and pre-trains via MAML.
  - Contributions: model-free PIML pre-training step; attention-based spatiotemporal network avoiding conv/recurrent inflexibility; SOTA accuracy on 18,061 Shenzhen charging piles with correct price-elasticity interpretation; demonstration that 1-hop spatial spillover offsets >90% of local demand loss after a 30% price increase.
- **Method core:** Problem setup: urban area as graph of $N$ zones (nodes = traffic zones, edges = centroid links); tensor $\mathcal{X}(i,j,t)$ = $j$-th feature of node $i$ at time $t$; sliding window $\{\mathbf{x}_{t-w},\dots,\mathbf{x}_{t-1}\}$; task: predict $\mathbf{y} = X(:,o,t+\Delta) = \mathbf{o}^{t+\Delta}$ for all zones at horizon $\Delta$. 2-D CNN extracts temporal features per node; …
- **Key results:**
  - Averages over 247 zones across 15/30/45/60-min horizons: (Note: text reports MAE 0.0393 vs table value 0.0333; both appear in paper.)
  - vs VAR: **61.3% average improvement**; vs LSTM: 18.21%/13.17%/11.37%/17.98% improvements in RMSE/MAPE/RAE/MAE; vs SOTA spatiotemporal baselines (DCRNN, AST-GAT, FourierGNN): 5.29% RMSE, 8.97% MAPE, 5.13% RAE, 7.51% MAE; overall ≈**6.73% average improvement** over SOTA.
  - Robustness: randomly dropping 20% (49) of zones (10 runs) still beats baselines by ≈17.09% on average.
- **Gaps/Limitations:**
  - Focus limited to the demand–price relationship; many other misinterpretations exist in spatiotemporal deep models and remain unaddressed.
  - Pre-training must be carefully monitored ("model curing" / overfitting to tuning samples); authors suggest an automated critique module trained by Reinforcement Learning as future work.
  - Spillover effects are detected but not quantified; quantification would help regulators evaluate policy impacts.

### 2024_PowerMamba_Power_Systems_SSM
**PowerMamba: A Deep State Space Model and Comprehensive Benchmark for Time Series Prediction in Electric Power Systems**  
Menati et al. · arXiv preprint (arXiv:2412.06112), v2 updated 20 Dec 2025 · 2024
<https://arxiv.org/abs/2412.06112>
**Models**: PowerMamba, Mamba_SSM, RevIN, iTransformer, PatchTST, DLinear, Autoformer, TimesNet, 2024_TimeMachine_Mamba_Long_Term_Forecasting  
**Horizon**: Short_Term_Forecasting / Long_Term_Forecasting  
**Metrics**: MSE, MAE  
**Data**: ERCOT_GridSet  
**Features**: Historical_Load, zonal electricity price, ancillary service price, renewable generation (wind/solar), ERCOT external forecasts (day-ahead load + renewables)

- **What they did:**
  - Grid volatility from electrification (incl. EVs), renewables, storage, and flexible loads motivates **multivariate** forecasting of load, price, ancillary-service (AS) price, and renewable generation *jointly* — prior art forecasted each variable separately, losing cross-variable correlations and inflating compute/training cost.
  - Three contributions: (1) **PowerMamba**, a selective-SSM (Mamba_SSM) multivariate forecaster with dual-path standard/inverse Mamba blocks and trend–seasonal decomposition tailored to power time series; (2) a **time-series processing block** that injects high-resolution external forecasts (ERCOT day-ahead load/renewables) into seq2seq predictors with negligible size increase; (3) an open-access benchmarking toolbox …
  - Headline: improves state-of-the-art prediction error by ~7% on average while cutting parameters 43% vs best Mamba baseline and 78% vs leading Transformer.
- **Method core:** **SSM foundation**: continuous latent dynamics (Eq. 1, reconstructed from PDF-extracted text):   \frac{dh(t)}{dt} = Ah(t) + Bx(t), \qquad y(t) = Ch(t) \tag{1}   zero-order-hold discretisation $\bar{A} = \exp(\Delta A)$, $\bar{B} = A^{-1}(\exp(\Delta A) - I)B$ gives (Eq. 3, reconstructed):   h_t = \bar{A}h_{t-1} + \bar{B}x_t, \qquad y_t = Ch_t \tag{3}   unrolled into a …
- **Key results:**
  - **Accuracy vs baselines** (TimeMachine [37], iTransformer, PatchTST, DLinear, TimesNet, Autoformer; L=240, W∈{24,48,72,96,168}, MSE/MAE on standardised series): PowerMamba best on nearly every task; e.g. GridSet W=24: **0.129/0.166** vs TimeMachine 0.135/0.166, iTransformer 0.147/0.181, PatchTST 0.142/0.183, …
  - **+7% avg accuracy over TimeMachine with −43% parameters**; −78% parameters vs leading Transformer (iTransformer). Only DLinear is smaller (but far less accurate at long horizons).
  - **External forecasts cut overall error 43%** (GridSet W=24 MSE 0.129→0.074); renewable error **−76%** (0.590→0.142); price error −7% *despite no external price forecasts* — evidence of cross-channel information transfer. Gains hold when the module is grafted onto every baseline.
- **Gaps/Limitations:**
  - **Point forecasts only** — trained with L2 loss, evaluated with MSE/MAE; no probabilistic/quantile output (contrast with Pinball_Loss-style methods relevant to EV charging).
  - **Zonal granularity, not station/nodal level** — authors position DSO-level adaptation as future work; nothing about EV charging stations or EV-specific load evaluation (EVs appear only as motivation for load volatility).
  - External forecasts unavailable for price/AS series; robustness tested only against synthetic iid Gaussian forecast noise.
  - Future work (authors): extend dataset with energy-storage and data-center series; use deep SSMs for transient/dynamic disturbance prediction.
  - Gap hooks for thesis: no uncertainty quantification, no station-level/EV case study, and no comparison against probabilistic baselines → direct openings for T-7-style comparator work.

### 2024_Prediction_Interval_EV_Loads
**Short-term Load Forecasting Considering EV Charging Loads with Prediction Interval Evaluation**  
Shi et al. · 2024 56th North American Power Symposium (NAPS), IEEE · 2024
<https://doi.org/10.1109/NAPS61145.2024.10741734>
**Models**: Gaussian_Process_Regression, Kernel_Density_Estimation  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAPE, PICP, NMPIL, CLC  
**Data**: US_Utility_Feeder_Residential_Load; Real_World_EV_DC_Charging  
**Features**: Historical_Load, Weather_Traffic, Calendar_Features, Charging_Habit_Probability

- **What they did:**
  - Probabilistic **day-ahead short-term load forecasting** for a distribution feeder whose load is the sum of residential demand + aggregated **EV charging loads**, using **Gaussian Process Regression (GPR)**.
  - Motivation: EV integration raises peak load *and shifts its timing*; deterministic point forecasts are inadequate under EV-induced uncertainty, especially at aggregate (feeder) level, which matters most to system operators.
  - Contributions: 1. A probabilistic (PI-producing) GPR forecaster adapted to day-ahead feeder-level load with integrated EV charging. 2. Quantitative **prediction interval (PI) evaluation** using metrics covering both interval length (NMPIL) and coverage probability (PICP), combined into a coverage-length-based criterion (CLC) — beyond purely deterministic MAPE/RMSE. 3. A novel input feature capturing **users' …
- **Method core:** Starting charging time CT fitted by **kernel density estimation** with Gaussian kernel (Eq. 1):  f(CT) = \frac{1}{nV}\sum_{i=1}^{n} K\!\left(\frac{CT - CT_i}{h}\right) \tag{1}  where $n$ = number of samples, $h$ = bandwidth, $K(\cdot)$ = kernel function (Gaussian chosen for symmetry).
- **Key results:**
  - Three cases (same GPR): **Case 1** = EV-free load forecast (features: time indices, $PH$, $T$, $TH$); **Case 2** = load including EVs, same features; **Case 3** = Case 2 + charging-habit feature $CH(t)$. **Table I — Deterministic metrics (verified verbatim):** Key finding: adding EV loads more than doubles MAPE (9.07% …
  - **PICP (%):** CI-68%: 67.8 (Case 1) / 50.4 (Case 2) / 73.6 (Case 3); CI-95%: 90.8 / 84.6 / 93.8; CI-99.7%: 97.5 / 95.5 / 98.5. Ideal values: 68 / 95 / 99.7. Case 3 closest to ideal; Case 2 far below.
  - **NMPIL:** CI-68%: 0.24 / 0.4 / 0.27; CI-95%: 0.48 / 0.8 / 0.54; CI-99.7%: 0.71 / 1.2 / 0.81. Case 2 produces the widest intervals yet worst coverage.
- **Gaps/Limitations:**
  - Single feeder, hourly resolution, ~2-month test window — generalization to other feeders/geographies/resolutions untested.
  - EV charging loads for only 30 vehicles, synthetically sampled from a statistical (KDE/Gamma/log-normal/uniform) model rather than directly measured per-EV metering.
  - GPR scales poorly to large training sets (kernel-matrix inversion); authors do not discuss computational cost or sparse/variational GP variants.
  - Day-ahead recursive scheme feeds predictions back as inputs → potential multi-hour error accumulation (not quantified).
  - PI construction relies on GP Gaussianity assumption; no comparison against quantile-regression or conformal alternatives; no pinball/Winkler scoring.
  - Gap: richer charging-behavior modeling, higher-resolution (sub-hourly) probabilistic forecasting, and benchmarking against QR/deep probabilistic methods (cf. 2017_QRA_Sister_Forecasts_Probabilistic_Load, 2025_QR_LSTM_Attention_EV_Load, 2021_Probabilistic_Queuing_EV_Load).

### 2024_Robust_MTS_Transitional_Shift
**Robust Multivariate Time Series Forecasting against Intra- and Inter-Series Transitional Shift**  
He et al. · arXiv preprint (IEEE journal template, Journal of LaTeX Class Files style); … · 2024
<https://doi.org/10.48550/arXiv.2407.13194>
**Models**: JointPGM  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, MSE  
**Data**: Exchange; ETT; ETT; Electricity_ECL; Traffic; ILI  
**Features**: Multivariate_Time_Series, Temporal_Order_Features

- **What they did:**
  - Tackle **distribution shift** in non-stationary Multivariate Time Series (MTS) forecasting by decomposing the coarse-grained transitional shift into two finer-grained components:
  - **Intra-series transitional shift**: $P(x^{(i)}_{u:u+H}|x^{(i)}_{u-L:u}) \neq P(x^{(i)}_{v:v+H}|x^{(i)}_{v-L:v})$ for any two steps $u \neq v$ (Definition 1).
  - **Inter-series transitional shift**: transitional distribution of series $i$ conditioned on its complementary set changes across time (Definition 2).
  - Argues normalization-based methods (RevIN, Dish-TS, SAN) assume a **time-invariant transition** between inputs and outputs and ignore inter-series dynamics; time-variant models (Koopa, meta-learning approaches) model transitions coarsely and remain black-box.
  - Proposes **JointPGM** ("Joint Probabilistic Graphical Model"): a unified PGM that *jointly* captures intra-/inter-series correlations AND models the time-variant transitional distribution.
  - Key contributions: (1) JointPGM framework built on a tailored PGM with theoretical guarantees; (2) dual learners — intra-series learner with temporal gates, inter-series learner with multi-hop propagation + Gumbel-softmax sampling; (3) SOTA on six highly non-stationary datasets with average improvement of **15.3% in MAE** and **37.9% in MSE** over all baselines.
- **Method core:** Dual-encoder architecture with four components: **Time Factor Encoder (TFE)**, **Independence-based Series Encoder (ISE)** (intra-series learner + inter-series learner), **Dynamic Inference (DI)**, and **Decoder**.
- **Key results:**
  - Metrics: MAE and MSE (lower better). Lookback 96 (ILI: 24). **vs. nine baselines (Table II)** — JointPGM best in ~80% of settings; selected results (MAE/MSE):
  - Exchange H=96: JointPGM 0.199/0.076 vs. best baseline iTransformer 0.206/0.086 → **13.2% MSE reduction (0.086→0.076)**.
  - ILI H=24: JointPGM 1.354/3.818 vs. Koopa 1.285/3.697 (Koopa wins here); ILI H=48: 4.8% MSE reduction over SOTA (4.000→3.818).
- **Gaps/Limitations:**
  - Authors' stated future work: exploring time-variant dynamics on **higher-dimensional MTS data** and further improving **efficiency**.
  - Slightly inferior MAE vs. MSE-only-trained baselines due to dual reconstruction+prediction MSE losses (bias of objective function).
  - Sensitive to trade-off parameter α (violent fluctuation when α < 0.6); requires tuning.
  - Multi-hop propagation suffers over-smoothing for larger depth K.
  - Evaluated only on generic non-stationary benchmarks (exchange, transformers, traffic, electricity, ILI) — no direct evaluation on EV charging station load, though electricity consumption planning is listed among motivating applications.
  - Research gap for thesis: probabilistic/fine-grained transitional-shift decomposition could be applied to non-stationary EV charging loads where intra-station dynamics and inter-station spatial correlation both shift.

### 2024_TOU_Price_Meteorology_EV_Charging_Load
**EV Charging Load Forecasting Method Considering Time-of-Use Price and Meteorological Factors**  
Li et al. · 2024 7th International Conference on Power and Energy Applications (ICPEA) · 2024
<https://doi.org/10.1109/ICPEA63589.2024.10784728>
**Models**: CNN, GRU, LSTM, MLP  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, RMSE  
**Data**: Jining_Mall_EV_Charging_Station  
**Features**: Historical_Load, Electricity_Tariff, Weather_Traffic, Cyclical_Encodings

- **What they did:**
  - Proposes an EV charging station load forecasting method that explicitly incorporates **time-of-use (TOU) price** and **meteorological factors** alongside historical load.
  - Contribution chain: (1) quantitative factor screening via **Pearson correlation coefficient** (load-load autocorrelation) and **Maximum Information Coefficient (MIC)** (load-factor nonlinear coupling); (2) **CNN feature extraction** from the multi-dimensional inputs; (3) **two-layer GRU** for temporal dependency capture; (4) forecasting at multiple time scales (**4 h, 24 h, 72 h, 168 h**) with demonstrated …
  - Key empirical insight: mall-located station shows strong price-based demand response — load peaks during off-peak-price periods and is higher on weekends/holidays than weekdays.
- **Method core:** **Pearson autocorrelation (Eq. 1)** — used to determine the fluctuation period of the load sequence (one month of data analyzed; lag set $a=720$; OCR-degraded in source, reconstructed standard form):  \rho_A = \frac{\sum_{a=1}^{N-A}(x_a-\bar{x})(x_{a+A}-\bar{x})}{\sum_{a=1}^{N}(x_a-\bar{x})^2}  where $\rho$ = autocorrelation coefficient, $N$ = length of load sequence, …
- **Key results:**
  - Baselines: BP, LSTM, GRU. Training set: **first 18 days of data**; forecast lengths 4 h / 24 h / 72 h / 168 h (Table III): (Note: body text quotes 168 h MAE as 54.329 while the table prints 54.32.) Findings:
  - CNN-GRU achieves lowest MAE/RMSE at **every** horizon; best relative gains at short horizons (4 h: MAE 36.33 vs GRU 49.04, ≈26% lower).
  - Competing models' errors fluctuate strongly as horizon grows; CNN-GRU shows small error variation across horizons → good stability (4 h→168 h RMSE degradation only +25.08 vs +26.80 for GRU, larger for BP/LSTM).
- **Gaps/Limitations:**
  - Single station, ~1 year of hourly data; very small training set (first 18 days) — generalization untested; no cross-station validation.
  - Authors' own future work: explore impact of **additional external factors** on load forecasting to improve applicability and accuracy.
  - Only point forecasts; no probabilistic/uncertainty quantification.
  - TOU flat-period definition partially unreadable in source text; dataset private → results not reproducible externally.
  - No comparison against attention/Transformer-class models or against persistence baseline.

### 2024_TiDE_Long_Term_Forecasting
**Long-term Forecasting with TiDE: Time-series Dense Encoder**  
Das et al. · arXiv:2304.08424v5 [stat.ML] (Google Research / Google Cloud / UC San Diego) · 2024
<https://arxiv.org/abs/2304.08424>
**Models**: TiDE, DLinear, PatchTST, NHiTS, DeepAR, S4, FEDformer, Autoformer, Informer, Pyraformer, LogTrans, LSTM  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE, WRMSSE  
**Data**: Electricity_ECL; Traffic; Weather_Dataset; ETT; ETT; ETT; ETT; M5_Dataset; Synthetic LDS Dataset  
**Features**: Lookback_Window, Dynamic_Covariates, Static_Attributes, Time_Derived_Features

- **What they did:**
  - Motivated by DLinear showing simple linear models beat Transformer-based long-term forecasters, proposes **TiDE (Time-series Dense Encoder)**: an MLP-based encoder-decoder with the simplicity/speed of linear models plus the ability to handle covariates and non-linear dependencies — no self-attention, recurrence, or convolution.
  - Theory: proves the simplest linear analogue of TiDE achieves **near-optimal error rate for Linear_Dynamical_Systems (LDS)** when the design matrix's maximum singular value is bounded away from 1; empirically validated on synthetic LDS data where Linear beats LSTM and Transformer.
  - Empirics: matches or outperforms prior neural approaches on standard benchmarks (>10% lower MSE on the largest dataset), while being **5x faster at inference and >10x faster in training** than the best Transformer baseline (PatchTST).
- **Method core:** Problem (**Eq. 1, forecaster mapping**): channel-independent mapping of one series' look-back $y^{(i)}_{1:L}$, dynamic covariates $x^{(i)}_{1:L+H} \in \mathbb{R}^r$, and static attributes $a^{(i)}$ to horizon predictions:  f: \left\{y^{(i)}_{1:L}\}_{i=1}^N,\ \{x^{(i)}_{1:L+H}\}_{i=1}^N,\ \{a^{(i)}\}_{i=1}^N\right\} \longrightarrow …
- **Key results:**
  - Benchmarks (MSE, selected): Traffic-720 **0.386 vs PatchTST 0.432 (10.6% better)**; Electricity-720 0.196 vs PatchTST 0.197; ETTh2-96 0.270 vs 0.274; ETTm2-96 0.161 vs 0.166; best or statistically-tied-with-best in nearly all settings except Weather horizons 96-336 where PatchTST wins (TiDE wins Weather-720: 0.313 vs …
  - Sub-quadratic attention approximations (FEDformer/Autoformer/Informer/Pyraformer/LogTrans) far behind, e.g., Informer Traffic-96 MSE 0.733 vs TiDE 0.336.
  - vs S4: vastly better, e.g., ETTh2-720 MSE 0.419 vs 2.650; Electricity-720 0.196 vs 0.578.
- **Gaps/Limitations:**
  - Self attention may still be unnecessary only for these long-term benchmarks; rigorous analysis of MLPs/Transformers under models with varying seasonality/trend levels remains open.
  - Transformers are more parameter-efficient than MLPs despite higher memory/compute intensity — a limitation for extremely large-scale pre-trained forecasting models.
  - Point forecasts with MSE loss only; no probabilistic outputs; no EV-specific evaluation (Electricity/Traffic are proxy domains).

### 2024_TimeMachine_Mamba_Long_Term_Forecasting
**TimeMachine: A Time Series is Worth 4 Mambas for Long-term Forecasting**  
Ahamed et al. · arXiv preprint (arXiv:2403.09898v2, cs.LG, 22 Aug 2024), University of Kentucky · 2024
<https://doi.org/10.48550/arXiv.2403.09898>
**Models**: 2024_TimeMachine_Mamba_Long_Term_Forecasting, Mamba_SSM  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE  
**Data**: Weather_Dataset; Traffic; Electricity_ECL; ETT; ETT; ETT; ETT  
**Features**: Historical_Load

- **What they did:**
  - Introduce **TimeMachine**, a model built on the selective-scan state-space model **Mamba** for long-term time-series forecasting (LTSF) that captures long-range dependencies in multivariate time series (MTS) with **linear scalability** and a **small memory footprint**.
  - Three stated contributions: 1. First model to leverage purely SSM modules for context-aware LTSF prediction with linear scalability and small memory footprints superior/comparable to linear models. 2. An innovative architecture unifying **channel-mixing and channel-independence** handling via an integrated **quadruple-Mamba** design, selecting contents against global and local contexts at multiple scales. 3. …
- **Method core:** **Quadruple Mamba architecture**: two outer Mambas on $DO(x^{(1)})$ (high resolution, fine scale) and two inner Mambas on $DO(x^{(2)})$ (low resolution, coarse scale). Channel independence reshapes input $\mathrm{BML} \mapsto (\mathrm{B}\times \mathrm{M})\,1\mathrm{L}$; one Mamba per pair sees token length $n_i$ / dim 1 (global context), the other dim $n_j$ / token length 1 …
- **Key results:**
  - Protocol: L=96 fixed for all models, T ∈ {96,192,336,720}; MSE/MAE metrics; baseline numbers taken from iTransformer paper.
  - Electricity: T=96 → 0.142/0.236 (iTransformer 0.148/0.240); T=720 → 0.207/0.298 (iTransformer 0.225/0.317).
  - Traffic: essentially tied with iTransformer (e.g., T=96: 0.397/0.268 both; T=720: 0.467/0.300 both).
- **Gaps/Limitations:**
  - Ranks second on Weather dataset at small prediction lengths — an area for future improvement.
  - Qualitative alignment with ground truth could still be enhanced (Figure 3).
  - Future work: extending TimeMachine to self-supervised learning settings.
  - Only supervised LTSF on generic benchmarks; no domain-specific evaluation (e.g., EV charging) or probabilistic forecasts. **Relevance to EV charging load forecasting:** This is a foundational method paper in the Mamba line — it established multi-scale quadruple-Mamba architectures and unified channel-mixing/channel-independence handling for long-horizon forecasting, directly informing the SSM-based EV forecasting …

### 2024_TimesFM_Decoder_Only_Foundation_Model
**A Decoder-Only Foundation Model for Time-Series Forecasting**  
Das et al. · arXiv preprint arXiv:2310.10688v4 [cs.CL] · 2024
<https://arxiv.org/abs/2310.10688>
**Models**: TimesFM, PatchTST, N-BEATS, DeepAR, WaveNet, Transformer, Informer, Autoformer, FEDFormer, TimesNet, DLinear, ARIMA, ETS, TBATS, Theta, CatBoost, LLMTime, TimeGPT-1  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MAE, msMAPE, MSE  
**Data**: Google_Trends; Wikipedia_Pageviews; M4; Electricity; Traffic; Weather; Favorita_Retail; LibCity; Monash_Archive; Darts; ETT  
**Features**: Historical_Load

- **What they did:**
  - **Research question**: Can a single decoder-only Transformer pretrained on massive time-series data achieve strong zero-shot forecasting across diverse unseen datasets, domains, horizons and granularities — analogous to LLMs in NLP?
  - **Core contribution — TimesFM (Time-series Foundation Model)**: First practical **decoder-only** patched foundation model (200M params, up to ~100B time-points pretraining) with **input patching + causal attention + longer output patches + patch masking** enabling variable context/horizon/granularity zero-shot inference. Out-of-the-box accuracy comes close to SOTA supervised models trained per-dataset.
  - **Two pillars**: 1. Large-scale pretraining corpus from **Google Trends (~0.5B pts, 22k head queries)** + **Wiki Pageviews (~300B pts, 5.6M hourly series)** + **3M synthetic series (6.1B pts, ARMA + seasonal + trend + step)** + M4/Electricity/Traffic/Weather/Favorita/LibCity (Table 1, ~100B total after mixing; 80% real / 20% synthetic with equal weight to hourly+sub-hourly / daily / weekly / monthly groups). 2. …
  - **Empirical claim**: Single TimesFM model is **SOTA or within significance of SOTA** zero-shot on held-out **Monash (18 datasets)**, **Darts (8 series)**, and **ETT (4 datasets × 2 horizons)** — beating LLM-based forecaster LLMTime (GPT-3) by >25% on Monash and beating most supervised long-horizon baselines, despite being orders of magnitude smaller than LLMs. Follow-up FINETUNING on only 10% of ETT data (tuning …
- **Method core:** **Model Type**: Decoder-only Transformer with patching. Three stages: Input Residual Block → Stacked Causal Transformer → Output Residual Block. Three model scales ablated: **17M (10 layers, d=512)**, **70M (10 layers, d=1024)**, **200M (20 layers, d=1280, 16 heads, input_patch_len=32, output_patch_len=128, dropout 0.2)**.
- **Key results:**
  - **Monash (18 datasets, scaled MAE — lower is better, Table 4 & Fig. 2a/4a)**:
  - Geometric mean scaled MAE: **TimesFM 0.6846** (best), N-BEATS 0.7005, CatBoost 0.7044, FFNN 0.7477, WaveNet 0.7733, PR 0.7736, DeepAR 0.8104, Transformer 0.9384, LLMTime (GPT-3 ZS) 0.9715, ETS 0.9337, ARIMA 0.9449, SES 1.0855. Arithmetic mean: TimesFM 0.8005 vs N-BEATS 0.7844 (within significance of top).
  - TimesFM is **top model overall**, >25% better than LLMTime (GPT-3) and better than supervised DeepAR/WaveNet/Transformer/CatBoost; within significance of N-BEATS (the strongest supervised baseline on Monash).
- **Gaps/Limitations:**
  - **Probabilistic forecasting not evaluated**: Only point MSE loss; quantile heads / distribution NLL discussed (§4 Loss, A.1) but left to future work/finetuning. No CRPS/Winkler/PICP reporting.
  - **No covariates**: Model is univariate-only at pretraining; multivariate / exogenous handling (weather, price, traffic) unsolved — paper proposes residual regression or finetuning with embeddings but does not test them. Directly relevant gap for EV load forecasting (arrival/departure, SoC, tariff, weather+traffic all unused).
  - **Granularity imbalance**: Performance relies on synthetic data to cover rare granularities (quarterly/yearly/weekly); real data dominated by hourly/daily. Monthly/weekly max context shortened (64/256) due to short series.
  - **No EV or station-level evaluation**: Benchmarks are generic (Monash/Darts/ETT); no EV charging datasets (ACN, ElaadNL, Palo Alto, etc.) tested — transfer to highly sparse, spiky EV loads unproven.
  - **No hyperparameter tuning of pretraining**: Single LR schedule, fixed architecture; authors note MLP [CLY+23] or SSM/Mamba [GD23] alternatives and broader HPO not explored due to compute cost.
  - **Data contamination / leakage risk**: Monash/Darts/ETT are public; overlap with web-scale pretraining not rigorously audited (unlike Meyer et al. 2025 contamination controls). TimeGPT-1 comparison omitted (not public).
  - **Interpretability**: Deep foundation model less interpretable than statistical baselines; SHAP/LOCO suggested but not demonstrated.
  - **Prompt/context tuning**: Context-length selection done via small validation sweep on Monash (32 vs 64 vs 512); systematic prompt-tuning / chain-of-thought analogues for time-series unclear.
  - **Compute reporting**: Final 200M run = 16×TPUv5e × 2 days; total experimentation cost higher — equitability concern if weights not released promptly.

### 2024_Unified_Training_Universal_Time_Series_Transformers
**Unified Training of Universal Time Series Forecasting Transformers**  
Woo et al. · Proceedings of the 41st International Conference on Machine Learning (ICML 2024) · 2024
<https://arxiv.org/abs/2402.02592>
**Models**: Moirai, Transformer, PatchTST, TimesFM, TiDE, TFT, DeepAR, DLinear, FEDformer, Autoformer, Informer, TimesNet, iTransformer, Lag-Llama  
**Horizon**: Short_Term_Forecasting / Long_Term_Forecasting  
**Metrics**: CRPS, MSIS, MAE, MSE, WQL  
**Data**: LOTSA; BuildingsBench; ClimateLearn; LargeST; LibCity; Monash_Archive; ProEnFo; SubseasonalClimateUSA; Electricity_ECL; Solar_Dataset; Weather; M4; KDD_Cup_2022  
**Features**: Historical_Load, Dynamic_Covariates, Time_Encoding, Variate_Identifier

- **What they did:**
  - **Core Problem Addressed**: Deep learning for time series forecasting has traditionally operated in an isolated "one-model-per-dataset" paradigm, lacking universal foundation models capable of zero-shot transfer across diverse domains, frequencies, and dimensionalities. Existing architectures fail because of three fundamental bottlenecks: 1. *Cross-Frequency Learning*: Time series span frequencies from yearly to …
  - **Primary Novel Contributions**:
  - **MOIRAI Architecture** (*Masked EncOder-based UnIveRsAl TIme Series Forecasting Transformer*):
  - *Multi Patch Size Input/Output Projections*: Frequency-aware projection layers mapping multiple patch sizes (8, 16, 32, 64, 128) to shared hidden representation space $\mathbb{R}^{d_h}$.
  - *Any-Variate Attention*: Flattens multivariate time series into a unified sequence and introduces binary attention biases combined with Rotary Position Embeddings (RoPE) to achieve permutation equivariance w.r.t. variate ordering and invariance w.r.t. variate indices.
  - *Parametric Mixture Distribution Head*: Flexible output head combining Student's $t$, continuous negative binomial, log-normal, and low-variance normal distributions.
  - **LOTSA Archive (*Large-scale Open Time Series Archive*)**:
  - The largest open collection of time series data curated for pre-training foundation models, comprising **27,646,462,733 (27.6B)** univariate observations (or **231,082,956,489 (231B)** observations when accounting for target variates) across 9 distinct domains in unified Apache Arrow format.
  - **Zero-Shot Generalization**: Outperforms or matches full-shot supervised models on in-distribution benchmarks (Monash) and out-of-distribution probabilistic forecasting benchmarks (CRPS / MSIS on Electricity, Solar, Walmart, Weather, Istanbul Traffic, Turkey Power). ---
- **Method core:** Consider a dataset $\mathcal{D} = \{(Y^{(i)}, Z^{(i)})\}_{i=1}^N$, where $Y^{(i)} \in \mathbb{R}^{d_{y_i} \times T_i}$ is a target time series with $d_{y_i}$ variates and $T_i$ time steps, and $Z^{(i)} \in \mathbb{R}^{d_{z_i} \times T_i}$ represents covariates. The model predicts the parameters $\hat{\phi}$ of predictive distribution $p(Y_{t:t+h} \mid \hat{\phi})$ from …
- **Key results:**
  - **$\text{MOIRAI}_{\text{Small}}$**: 6 layers, $d_{\text{model}}=384$, $d_{ff}=1536$, 6 heads, $d_{kv}=64$, **14M parameters**, 100K training steps.
  - **$\text{MOIRAI}_{\text{Base}}$**: 12 layers, $d_{\text{model}}=768$, $d_{ff}=3072$, 12 heads, $d_{kv}=64$, **91M parameters**, 1M training steps.
  - **$\text{MOIRAI}_{\text{Large}}$**: 24 layers, $d_{\text{model}}=1024$, $d_{ff}=4096$, 16 heads, $d_{kv}=64$, **311M parameters**, 1M training steps. --- Evaluated across 6 out-of-distribution benchmarks under rolling-window evaluation (CRPS & MSIS; mean $\pm$ std for 5 seeds on baselines): --- Averaged across …
- **Gaps/Limitations:**
  - 1. **Heuristic Frequency-to-Patch Mapping**: The mapping from sampling frequency to allowed patch sizes is fixed heuristically ($8 \dots 128$) rather than dynamically learned or continuous. 2. **Computational Overhead with High-Dimensional Variates**: Flattening $d$ variates scales the sequence length by $d$, causing the full self-attention matrix in the masked encoder to scale quadratically $O((d \cdot L / P)^2)$, …

### 2024_V2G_SVE_Evaluation_Metric
**A Reliable Evaluation Metric for Electrical Load Forecasts in V2G Scheduling Considering Statistical Features of EV Charging**  
Zhong et al. · IEEE Transactions on Smart Grid, vol. 15, no. 5, pp. 4917-4930 · 2024
<https://doi.org/10.1109/TSG.2024.3392910>
**Models**: V2G-SVE, Aggregate_EV_Fleet_Model, MLP, MLR, Simple Average (SA), 1-same-day persistence  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: V2G-SVE, SPDR, MAPE, RMSE, MAE, Pearson_Correlation_Coefficient  
**Data**: ASU_Campus_Metabolism_Dataset; Ausgrid_Zone_Substation_Dataset  
**Features**: Base_Electrical_Load, Arrival_Departure_Time, State_of_Charge, Battery_Capacity, Calendar_Features, Historical_Load

- **What they did:**
  - Shows that prevailing **forecast quality metrics** (MAPE, RMSE, MAE) fail to predict how a forecast will perform when fed into downstream **V2G** optimization — the relation between forecast *quality* and forecast *value* is not monotonic.
  - Proposes **V2G-SVE (V2G Scheduling Value Error)**: a value-oriented metric scoring a forecast by the relative degradation rate of load-variance-minimization scheduling performance caused by using it instead of actual load.
  - Builds an **aggregate model of the EV fleet** parameterized by statistical features of EV charging so V2G-SVE computes in constant time (~0.20 s) regardless of fleet size, avoiding the curse of dimensionality of per-EV quadratic programming.
  - Derives and experimentally verifies **three key findings** linking forecast errors to V2G scheduling degradation, with guidance for future forecasting loss design.
- **Method core:** Objective: minimize daily load variance (**Eq. 1**) with average load (**Eq. 2**):  \min \frac{1}{T}\sum_{t=1}^{T}\left(\sum_{n=1}^{N}P^{\text{cha}}_{n,t} + \sum_{n=1}^{N}P^{\text{dis}}_{n,t} + P^{\text{con}}_t - P^{\text{ave}}\right)^2, \qquad P^{\text{ave}} = \frac{1}{T}\sum_{t=1}^{T}\left(\sum_{n=1}^{N}P^{\text{cha}}_{n,t} + \sum_{n=1}^{N}P^{\text{dis}}_{n,t} + …
- **Key results:**
  - **Quality metrics are unreliable**: 6 experimental groups (+200/+500/+1000 kW and −200/−500/−1000 kW single-period errors, base load 110–170 MW-scale, schedulable power 0–1150 kW at N=100) show identical RMSE/MAE scores can produce substantially different scheduling results; MAPE contradicts scheduling impact in …
  - **Metric reliability**: 100 synthetic forecasts (MAPE 0.1%→10%). Pearson correlation between metric scores and actual scheduling performance: **V2G-SVE > 0.99 across all three experiments (N = 100, 95, 105), significantly surpassing MAPE, RMSE, MAE**. Scheduling performance loses monotonicity vs MAPE once MAPE > 2%; …
  - **Generalizability**: on Oct 15, 2022 base load with modified arrival/departure distributions (μ=8:00 σ=120 min arrivals; μ=20:00 σ=60 min departures), V2G-SVE ≈ SPDR along the diagonal for 50/100/150/200 EVs; robust under 1-hour time resolution too (errors hurt more at coarser resolution).
- **Gaps/Limitations:**
  - V2G-SVE reliability presupposes actual EV charging behavior follows the predefined statistical features; impractical when few EVs or statistically irregular behavior.
  - Metric tied to the load-variance-minimization objective; may not transfer to other V2G scheduling objectives (different stakeholders/objectives need re-derived value metrics).
  - Non-uniformity: metric built on aggregate model while ground-truth performance solved directly per-EV; conventional solvers hit resource limits at scale.
  - Future directions: custom differentiable loss functions weighting dense-EV periods more heavily; using inter-period **load differences** as forecasting inputs rather than raw historical loads; integrating forecasting and optimization (predict-and-optimize); advanced scheduling algorithms could improve both metric construction and validation.

### 2024_iTransformer_Inverted_Transformers_Effective_Time_Series
**iTransformer: Inverted Transformers Are Effective for Time Series Forecasting**  
Liu et al. · ICLR 2024 (Spotlight) · 2024
<https://doi.org/10.48550/arXiv.2310.06625>
**Models**: iTransformer, Transformer, Informer, Reformer, Flowformer, FlashAttention, PatchTST, Crossformer, DLinear, TimesNet, TiDE, SCINet, FEDformer, Stationary_Transformer  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE, CKA_Similarity  
**Data**: Electricity_ECL; ETT; Exchange; Traffic; Weather; Solar_Energy; Traffic; Market_Alipay  
**Features**: Variate_Tokens, Series_Representations, Multivariate_Correlation_Map, Transformer, Feed_Forward_Temporal_MLP

- **What they did:**
  - Diagnoses why Transformer-based forecasters underperform simple linear models in multivariate time series forecasting: embedding multiple variates of the *same timestamp* into one temporal token fuses distinct physical measurements (delayed events, inconsistent measurements), yields meaningless attention maps, and applies permutation-invariant attention to an order-sensitive dimension.
  - Proposes **iTransformer**: simply **inverts** the duties of the native Transformer components without modifying them — each variate's whole lookback series is embedded as a **variate token**; **self-attention operates across variates** to capture multivariate correlations; the **feed-forward network operates along time** to learn series representations.
  - Achieves comprehensive state-of-the-art on real-world benchmarks; shows the inversion framework consistently improves Transformer variants (38.9% avg promotion on vanilla Transformer, 36.1% Reformer, 28.5% Informer, 16.8% Flowformer, 32.2% Flashformer); enables generalization to unseen variates and better use of enlarged lookback windows.
  - Code: https://github.com/thuml/iTransformer
- **Method core:** Encoder-only Transformer with embedding → L inverted blocks → projection. Given lookback $X \in \mathbb{R}^{T\times N}$ (T steps, N variates), predict $\hat{Y} \in \mathbb{R}^{S\times N}$. The per-variate forecast is formulated as (**Eq. 1 – Overall formulation**):  h_n^0 = \text{Embedding}(X_{:,n}), \quad H^{l+1} = \text{TrmBlock}(H^l),\ l=0,\dots,L-1, \quad \hat{Y}_{:,n} = …
- **Key results:**
  - **ECL**: 0.178/0.270 (best; PatchTST 0.205/0.290, TimesNet 0.192/0.295, Autoformer 0.227/0.338). Per-horizon ECL MSE: 0.148 (96), 0.162 (192), 0.178 (336), 0.225 (720).
  - **Traffic**: 0.428/0.282 (best; PatchTST 0.481/0.304, RLinear 0.626/0.378).
  - **Solar-Energy**: 0.233/0.262 (best; PatchTST 0.270/0.307).
- **Gaps/Limitations:**
  - Quadratic complexity O(N²) in number of variates for high-dimensional datasets; mitigated by efficient attentions or variate sampling but not solved natively.
  - Under univariate scenarios iTransformer degrades into a stackable linear forecaster; temporal dependency modeling could be further enhanced (structural TCN-like embeddings suggested).
  - Distribution shift handling left to layer norm; explicit non-stationarity modules remain future work.
  - Future directions stated by authors: large-scale pre-training / foundation models for diverse multivariate series, more time series analysis tasks, fine-grained variate tokenization and better embedding mechanisms.
  - No probabilistic forecasts (point predictions only, L2 loss) — relevant gap for EV charging demand uncertainty quantification.

### 2023_Combined_Deep_Learning_EV_Station_STLF
**A Method of Short-term Load Forecasting at Electric Vehicle Charging Stations through Combining Multiple Deep Learning Models**  
Xiong et al. · 2023 2nd Asia Power and Electrical Technology Conference (APET), IEEE · 2023
<https://doi.org/10.1109/APET59977.2023.10489548>
**Models**: CNN_LSTM_Transformer_Combined_Model, CNN, LSTM, Transformer  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAE  
**Data**: Boulder_Colorado  
**Features**: Historical_Load, Charging_Event_Records, Timestamp

- **What they did:**
  - Propose a **combined deep learning model** for short-term load forecasting (STLF) at EV charging stations, integrating **CNN + LSTM + Transformer** to improve forecasting accuracy over single models.
  - Motivation: rapid EV growth (global sales >10 million in 2022; IEA projects ~10x by 2030); concentrated charging demand causes grid overload; harmonic pollution and low power factor of charging equipment.
  - Division of labor: **CNN** extracts local load-curve features, **LSTM** captures temporal/contextual long-term dependencies, **Transformer multi-head attention** captures global information.
  - Contribution is an empirical combination study — also ablates all pairwise combinations (CNN+LSTM, LSTM+Transformer, CNN+Transformer) against single models.
- **Method core:** **Transformer module**: two encoder layers in implementation (the paper describes the canonical architecture with N=6 identical layers, each with multi-head self-attention + feed-forward sublayer with residual connection and LayerNorm: LayerNorm(x+Sublayer(x)); $d_{model}=128$). Scaled dot-product attention (**Eq. 11, Scaled Dot-Product Attention**):
- **Key results:**
  - Evaluation metrics (Eqs. 15–16):  RMSE = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i^p - y_i)^2}, \qquad MAE = \frac{1}{N}\sum_{i=1}^{N}|y_i^p - y_i|  Table I — test-set performance (last 3 days, Dec 28–30, 2020):
  - Full combination achieves lowest error: **RMSE 0.300, MAE 0.120**.
  - vs. best single model (LSTM): **5.36% improvement in RMSE** and **21.27% improvement in MAE**.
- **Gaps/Limitations:**
  - Authors' own limitation: "**only limited data is used**" — single charging station, single year (2020), three-day test set; they plan to explore wider data and additional influencing factors (multi-faceted prediction) in future work.
  - No exogenous variables (weather, temperature, holidays, tariff/price, point-of-interest) despite citing SVR work that used them.
  - No comparison against classical ML baselines (SVR, PSO-SVM) or recent hybrid models; no statistical significance testing.
  - Hyperparameters (kernel size, LSTM units, number of encoder layers) not systematically tuned or justified; training details (optimizer, epochs, loss function) not reported in extracted text.
  - Single-step-ahead prediction only (96-point daily profile implied); no multi-horizon evaluation.
  - Research gap: ensemble/hybrid approaches with richer feature sets and probabilistic uncertainty quantification remain open — connects to 2020_Ensemble_EV_Load and 2026_Hybrid_XGBoost_BiLSTM_EV_Load.

### 2023_Crossformer_Cross_Dimension_Dependency
**Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting**  
Zhang et al. · ICLR 2023 · 2023
<https://arxiv.org/abs/2301.03982>
**Models**: Crossformer, DSW_Embedding, Two_Stage_Attention, Hierarchical_Encoder_Decoder, Router_Attention  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE  
**Data**: ETT; ETT; Weather; Electricity_ECL; ILI; Traffic  
**Features**: Multivariate_Time_Series, Cross_Time_Dependency, Cross_Dimension_Dependency, Segment_Embeddings, Multi_Scale_Representations

- **What they did:**
  - Identifies that existing Transformer-based MTS models embed all dimensions at one time step into a single vector and only model **cross-time dependency**, omitting **cross-dimension (cross-variate) dependency** — critical when series are associated (e.g., temperature ↔ wind speed; correlated EV charging stations).
  - Proposes Crossformer — among the first Transformers to explicitly exploit cross-dimension dependency — via three components: **Dimension-Segment-Wise (DSW) embedding** into a 2D vector array (time × dimension), **Two-Stage Attention (TSA)** layer with a router mechanism, and a **Hierarchical Encoder-Decoder (HED)** using multi-scale information.
  - Ranks top-1 in 36/58 settings and top-2 in 51/58 against 8 baselines across six real-world benchmarks.
- **Method core:** Task: predict $x_{T+1:T+\tau} \in \mathbb{R}^{\tau \times D}$ from history $x_{1:T} \in \mathbb{R}^{T \times D}$ ($D$ = number of dimensions).
- **Key results:**
  - Main benchmark (Table 1): top-1 in 36/58, top-2 in 51/58 settings vs LSTMa, LSTnet, MTGNN, Transformer, Informer, Autoformer, Pyraformer, FEDformer. Highlights (MSE): ETTh1 τ=168 Crossformer **0.410** vs FEDformer 0.412, Autoformer 0.493; ETTh1 τ=720 **0.519** vs FEDformer 0.521; ETTm1 τ=96 **0.320** vs FEDformer …
  - Extra comparison (Appendix Table 4): beats STformer (which flattens 2D→1D and OOMs on ECL/Traffic). DLinear wins on ETTm1 (τ≥288), ECL and Traffic (e.g., Traffic τ=24 DLinear 0.351 vs Crossformer 0.491); Crossformer wins on WTH and long-horizon ETTh1 (τ=168: 0.410 vs 0.416).
  - Ablation (Table 2, ETTh1): Transformer→DSW alone improves (τ=24: 0.620→0.373 MSE) proving embedding/cross-dimension value; +TSA improves further (0.305 at τ=24 with HED); HED helps long-term but slightly hurts short-term; full model best everywhere.
- **Gaps/Limitations:**
  - Router builds full all-to-all dimension connections → introduces noise on high-dimensional datasets; sparse graph-transformer structures suggested as future improvement.
  - Permutation-invariance critique of DLinear acknowledged: Crossformer is outperformed by DLinear on several datasets (ETTm1 long horizons, ECL, Traffic); enhancing order preservation (relative position encodings) is flagged as promising.
  - Straightforward covariate embedding does not improve accuracy — incorporating covariates remains an open problem.
  - Time-series benchmark datasets are too small/simple relative to vision/text; larger, more diverse datasets needed for Transformers to reach their potential.

### 2023_DLinear_Are_Transformers_Effective_LTSF
**Are Transformers Effective for Time Series Forecasting?**  
Zeng et al. · AAAI 2023 · 2023
<https://arxiv.org/abs/2205.13504>
**Models**: DLinear, DLinear, NLinear, Informer, Autoformer, FEDformer, Pyraformer, LogTrans  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE  
**Data**: ETT; ETT; ETT; ETT; Traffic; Electricity_ECL; Exchange; Weather; ILI  
**Features**: Trend_Seasonal_Decomposition, Moving_Average_Trend, Lookback_Window, Distribution_Shift_Normalization

- **What they did:**
  - First work to systematically **challenge Transformer-based LTSF solutions**: self-attention is permutation-invariant and "anti-order", causing temporal information loss that positional/timestamp embeddings cannot fully repair — fatal for time series where order is the crucial signal.
  - Introduces **DLinear**: embarrassingly simple one-layer (at most two) direct-multi-step (DMS) linear models — Vanilla Linear, NLinear, DLinear — that beat FEDformer/Autoformer/Informer/Pyraformer/LogTrans on all nine benchmarks, often by **20%–50%**.
  - Diagnostic studies show existing LTSF-Transformers cannot exploit longer look-back windows, barely preserve temporal order under input shuffling, and offer no practical efficiency advantage.
- **Method core:** Problem setup: C variates, look-back $L$, forecast horizon $T$; contrasts iterated multi-step (IMS, error accumulation) vs **direct multi-step (DMS)** strategies; argues prior Transformers' gains largely stem from DMS.
- **Key results:**
  - Multivariate results (Table 2): LTSF-Linear surpasses SOTA FEDformer by **20%–50%** in most settings. Examples (MSE): Electricity T=96 DLinear 0.140 vs FEDformer 0.193, Informer 0.274; T=720 DLinear 0.203 vs FEDformer 0.246. Exchange T=720: DLinear 0.643 vs FEDformer 1.447; naive Repeat beats all Transformers on …
  - **Attention ablation** (Table 4): gradually simplifying Informer (attention→linear→embedding+linear→pure linear) *improves* MSE monotonically (Exchange T=96: 0.847 → 1.003 → 0.173 → 0.084) — self-attention is unnecessary on these benchmarks.
  - **Order preservation** (Table 5): shuffling inputs barely affects Transformers (avg drop −0.12% to +0.09% on Exchange; Informer +1.98% on ETTh1) but severely hurts LTSF-Linear (27–81% drops) → Transformers preserve little temporal order.
- **Gaps/Limitations:**
  - One-layer linear models have limited capacity: they cannot capture temporal dynamics caused by change points; authors position LTSF-Linear as a baseline, not an end model.
  - No cross-variate correlation modeling (weights shared across variates).
  - Findings are specific to existing LTSF benchmarks; authors call for revisiting Transformer validity in other tasks (anomaly detection) and for new model designs, data processing, and benchmarks.
  - Later answered by PatchTST, which shows patched channel-independent Transformers do beat DLinear when long look-backs are exploited.

### 2023_DiffSTG_Probabilistic_ST_Graph_Diffusion
**DiffSTG: Probabilistic Spatio-Temporal Graph Forecasting with Denoising Diffusion Models**  
Wen et al. · ACM conference proceedings (© 2023 ACM); arXiv:2301.13629 (v4, Mar 2024) · 2023
<https://doi.org/10.48550/arXiv.2301.13629>
**Models**: DiffSTG, UGnet  
**Horizon**: Spatial_Temporal_Forecasting  
**Metrics**: CRPS, MAE, RMSE  
**Data**: Traffic; AIR-BJ; AIR-GZ  
**Features**: Traffic, PM2.5_Concentration, Adjacency_Matrix, Noise_Level_Embedding

- **What they did:**
  - First work to generalize Denoising Diffusion Probabilistic Models (DDPM) to **spatio-temporal graphs (STGs)**, yielding **DiffSTG**, a non-autoregressive probabilistic forecasting framework, plus the first DDPM denoising network dedicated to STGs, **UGnet** (Unet-based temporal architecture + GNN spatial modeling). Deterministic STGNNs cannot quantify prediction uncertainty, crippling downstream decision-making; …
- **Method core:** **DDPM background.** *Forward Markov process (Eqs. 1–2)* with variance schedule $\{\beta_1,\dots,\beta_N\}$, $\beta_n \in (0,1)$:  q(\boldsymbol{x}_{1:N}|\boldsymbol{x}_0)=\prod_{n=1}^{N}q(\boldsymbol{x}_n|\boldsymbol{x}_{n-1}), \qquad q(\boldsymbol{x}_n|\boldsymbol{x}_{n-1}) = \mathcal{N}\big(\boldsymbol{x}_n;\sqrt{1-\beta_n}\boldsymbol{x}_{n-1},\beta_n\mathbf{I}\big)  …
- **Key results:**
  - **Probabilistic comparison (Table 2, MAE/RMSE/CRPS), DiffSTG best everywhere:** CRPS reduced by 5.6%, 4.3%, 14.3% vs most competitive baseline per dataset. **Inference speed (Table 3, AIR-GZ, $N=100$):** TimeGrad 9.58 s (S=8) / 128.40 s (S=16) / 672.12 s (S=32); DiffSTG (M=100,k=1) 0.24 / 0.48 / 0.95 s → **40× …
- **Gaps/Limitations:**
  - Explicitly acknowledged: DiffSTG still trails state-of-the-art **deterministic** STGNNs (e.g., GMSDR, STGNCDE) because its variational-inference objective yields an inaccurate posterior when data samples are insufficient — improving this is left as future work.
  - Only vanilla GCN used in UGnet for simplicity; incorporating more powerful GNNs to better capture ST dependencies is open.
  - Future direction: applying DiffSTG to other spatio-temporal tasks such as STG imputation.
  - Diffusion sampling remains multi-step at inference even with acceleration; parameter count larger than TimeGrad/CSDI.

### 2023_MetaProbformer_EV_Load
**MetaProbformer for Charging Load Probabilistic Forecasting of Electric Vehicle Charging Stations**  
Huang et al. · IEEE Transactions on Intelligent Transportation Systems, 24(10), 10445-10455 · 2023
<https://doi.org/10.1109/TITS.2023.3276947>
**Models**: MetaProbformer, MetaProbformer, Reptile, Informer, Transformer, LSTM, DeepAR, Prophet, ARIMA, FPSeq2Q  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, MSE, RMSE, CRPS, Normalized ρ-quantile loss Qρ  
**Data**: D_Palo (City of Palo Alto EV charging usage); D_Boulder; D_NL; D_Perth (Perth & Kinross)  
**Features**: Univariate hourly average charging load (kW), Time-dependent covariates (month of year, etc.)

- **What they did:**
  - First Transformer-based method for **probabilistic charging load forecasting of EV charging stations**, and first to address **newly built stations with scarce historical data** via meta-learning.
  - Proposes **MetaProbformer** — an adaptation of Informer that outputs a **Gaussian predictive distribution** instead of point forecasts — and **MetaProbformer**, combining it with the Reptile meta-learning algorithm to learn a well-generalized initialization adaptable to unseen stations in few gradient steps.
  - Contributions: (I) Probformer architecture (Informer → probabilistic); (II) Reptile-based meta-learning framework for scarce-data charging stations; (III) experiments covering point + probabilistic forecasting, short-term (1 h) + long-term (24/48/168 h), and homogeneous vs heterogeneous tasks.
- **Method core:** Architecture: two-layer encoder + single-layer decoder (Informer setup); encoder input length 96, decoder input 48; generative-style decoder with zero-padded target ($Y_0$); halving distilling replicas mitigate information loss. Base learners optimized with Adam (lr 1e-4); meta-learner with SGD (lr 0.1); hyperparameters tuned by random search; standard normalization; test …
- **Key results:**
  - **Homogeneous task ($D_{Perth2}$)**: improvements of **3.614% MAE, 1.553% MSE, 0.773% RMSE** over the best baseline (MetaTransformer); Informer best among non-meta methods.
  - **Heterogeneous task ($D_{Palo}$)**: lowest errors with **8.479% MAE, 5.834% MSE, 2.950% RMSE** improvement over MetaTransformer; ordering MetaProbformer < MetaTransformer < Informer < LSTM < Transformer < ARIMA.
  - **Short-term probabilistic** (RMSE, Q50, Q90, CRPS; Tables V–VI): outperforms Transformer-P, MetaTransformer-P, DeepAR, FPSeq2Q, Probformer on all metrics for both tasks; average gains up to **3.620%** (homogeneous) and **5.319%** (heterogeneous). MetaTransformer-P best baseline, then Probformer → validates both the …
- **Gaps/Limitations:**
  - **Univariate only** — weather/traffic covariates missing from public datasets; multivariate extension left open.
  - Requires *some* historical data: fails on brand-new stations with zero history — authors propose **zero-shot** generalization across heterogeneous station record systems as future work.
  - Gaussian output assumption may underfit heavy-tailed/multimodal EV load distributions (vs quantile or diffusion models).
  - Theoretical analysis limited to citing PAC-Bayesian bounds; no station-network/spatial modeling (single-station series only).
  - Gap for thesis: combine few-shot adaptation (Reptile) with spatial information from nearby stations or mobility features (cf. 2022_Robust_Deep_Gaussian_Process_Load) for cold-start stations.

### 2023_Multi_Branch_ResTrans_Solar
**Multi-Branch ResNet-Transformer for Short-Term Spatio-Temporal Solar Irradiance Forecasting**  
Ziyabari et al. · IEEE Transactions on Industry Applications, 59(5), 5293-5303 · 2023
<https://doi.org/10.1109/TIA.2023.3285202>
**Models**: Multi-Branch ResNet-Transformer (ResTrans), Transformer, ResLSTM, CNN_LSTM, AttLSTM, ResNet, LSTM, CNN  
**Horizon**: Spatial_Temporal_Forecasting  
**Metrics**: RMSE, MAE, R² score  
**Data**: NSRDB Philadelphia, USA (18 sites, 2000-2017, 30-min, 3,784,320 observations)  
**Features**: GHI, DNI, DHI, Clear-sky GHI/DHI/DNI, Temperature, Humidity, Wind_Speed, Wind_Direction, Pressure, Dew_Point, Solar_Zenith_Angle, Precipitable_Water, Cloud_Type

- **What they did:**
  - Proposes **multi-branch ResTrans**, a hybrid spatio-temporal framework combining a **multi-branch deep residual network (ResNet)** for spatial correlation modeling across neighboring solar sites and a modified **Transformer** (encoder-only + time embedding) for temporal long-sequence modeling.
  - Motivations: RNN/LSTM frameworks forget long sequences and are computationally inefficient; CNNs ignore cross-site spatial correlations; single-resolution architectures miss multi-scale patterns; CNN/RNN overfitting is alleviated via shared multi-branch representations.
  - First work to combine Transformer with multi-branch ResNets for short-term spatio-temporal solar irradiance forecasting; achieves average RMSE 0.049 W/m², MAE 0.031 W/m², R² = 97%, beating single-branch ResTrans, multi/single-branch ResLSTM and CNN-LSTM.
- **Method core:** **Equation 1 — Forecast definition:** $\hat{Y}_{t+\Delta}^{n} = F(X)$, with $F(\cdot)$ implemented by self-attention + ResNet + Transformer over $N$ solar sites. **Equations 2–4 — Attention over RNN hidden states:** $p_t = \tanh(W_h h_t + b_h)$, $a_t = \frac{\exp(p_t)}{\sum_{i=1}^{t}\exp(p_i)}$, $h_t' = a_t \odot h_t$. **Equation 5 — Single-head scaled dot-product attention:** …
- **Key results:**
  - Temporal models on 12 sites, 12-hour horizon (Table II averages): CNN (RMSE 0.19, MAE 0.13, R² 0.63), LSTM (0.14, 0.09, 0.77), AttLSTM (0.12, 0.07, 0.78), ResNet (0.08, 0.05, 0.84), proposed Transformer (**0.06, 0.04, 0.87**) — beats LSTM by **57.14% RMSE / 55.56% MAE / 12.99% R²**; beats ResNet by 25.00% RMSE / …
  - **12 sites**: replacing LSTM with Transformer lowers average RMSE by 8.70% (single-branch) and 14.04% (multi-branch); **multi-branch ResTrans best: RMSE ≈ 0.054, MAE ≈ 0.036, R² ≈ 0.90+**; multi-branch vs single-branch ResTrans improves RMSE **22.22%** and MAE **20.51%** (single-resolution models miss multi-scale …
  - **18 sites (incl. distant)**: overall best remains multi-branch ResTrans with **average RMSE 0.049 W/m², average MAE 0.031 W/m², R² = 97%** (abstract); accuracy slightly degrades with distant sites due to lower spatial correlation — e.g., single-branch ResTrans RMSE/MAE rise 6.3%/17.9% vs 12-site case; negative …
- **Gaps/Limitations:**
  - Accuracy degrades as distance between sites grows — spatial graph construction / distance-aware attention not addressed.
  - Deterministic point forecasts only; no probabilistic uncertainty bands (important for grid integration).
  - Fixed sliding window (24 steps, half-day); horizon sensitivity not systematically ablated.
  - Solar-specific benchmark — but architecture directly transferable to **spatio-temporal EV charging station load forecasting**, where neighboring stations exhibit similar correlated demand patterns.
  - Gap for thesis: combine multi-resolution spatial branches with probabilistic heads (cf. 2023_MetaProbformer_EV_Load) for charging networks.

### 2023_NHiTS_Neural_Hierarchical_Interpolation
**N-HiTS: Neural Hierarchical Interpolation for Time Series Forecasting**  
Challu et al. · AAAI 2023 · 2023
<https://arxiv.org/abs/2201.12886>
**Models**: NHiTS, NBEATS, Autoformer, Informer, FEDformer, Reformer, LogTrans, DilRNN, DeepAR, Prophet, ARIMA  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE  
**Data**: ETT; Exchange; Electricity_ECL; Traffic; Weather; ILI  
**Features**: Univariate lags only (own history y_{t-L:t})

- **What they did:**
  - Tackles **long-horizon forecasting** volatility + computational complexity: attention and fully-connected layers scale quadratically in memory/compute with horizon $H$, and forecast errors inflate with $H$.
  - Proposes **NHiTS**, extending NBEATS with two complementary techniques: (1) **multi-rate input sampling** (MaxPool subsampling per block) and (2) **hierarchical interpolation** (few forecast coefficients upsampled via temporal interpolation).
  - Contributions: multi-rate sampling layers; interpolation-based output synthesis (architecture-agnostic); hierarchically synchronized block specialization into frequency bands; SOTA on six large-scale long-horizon benchmarks — average accuracy improvement of ~20%/14-16% over latest Transformer architectures while reducing compute time by an order of magnitude (~50×).
- **Method core:** MLP stacks ($S$ stacks × $B$ blocks) connected via the doubly-residual stacking principle; each block emits a backcast $\tilde{y}_{t-L:t,\ell}$ (subtracted from the next block's input) and a forecast $\hat{y}_{t+1:t+H,\ell}$ (summed). **Equation 1 — Multi-rate signal sampling (MaxPool with kernel $k_\ell$):**  y_{t-L:t,\ell}^{(p)} = \text{MaxPool}(y_{t-L:t,\ell},\, k_\ell)  …
- **Key results:**
  - Average relative error decrease vs best baseline: **14% MAE, 16% MSE**; at longest horizon (720/60): **11% MAE, 17% MSE** reduction. Example ECL@96: N-HiTS MSE 0.147 vs N-BEATS 0.145, Autoformer 0.201, Informer 0.274; Exchange@720: 0.798 vs Autoformer 1.447, Informer 2.478; TrafficL@96: 0.402 vs FEDformer 0.562; …
  - Vs concurrent ETSformer/Preformer (Table A4): still **11% MAE / 9% MSE** better on average (ETSformer wins only short-horizon Exchange).
  - **Univariate** (ETTm2, Exchange, Table A5): −17% MAE, −25% MSE vs best alternative (e.g., ETTm2@720 MSE 0.157 vs N-BEATS 0.188, DeepAR 0.332).
- **Gaps/Limitations:**
  - Strictly **univariate** (each variable predicted from own history) — cannot exploit cross-variable dependencies common in EV station networks; authors flag multivariate integration as untapped potential.
  - Point forecasts only (MAE loss) — no probabilistic/quantile outputs for downstream uncertainty-aware decisions.
  - Interpolation smoothness assumption may limit abrupt regime shifts (e.g., anomalous events, new-station cold start).
  - Wavelet/multi-resolution-analysis formulations proposed as future work; combining with Transformer-inspired architectures suggested.
  - Gap for thesis: use as efficient long-horizon backbone for day-ahead EV charging demand; combine with RevIN for non-stationarity and probabilistic heads for planning.

### 2023_PatchTST_A_Time_Series_is_Worth_64_Words
**A Time Series is Worth 64 Words: Long-term Forecasting with Transformers**  
Nie et al. · ICLR 2023 · 2023
<https://arxiv.org/abs/2211.14730>
**Models**: PatchTST, Transformer, RevIN, Masked_Autoencoder  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE  
**Data**: Weather; Traffic; Electricity_ECL; ILI; ETT; ETT; ETT; ETT  
**Features**: Multivariate_Time_Series, Patched_Embeddings, Channel_Independence, Positional_Encoding

- **What they did:**
  - Answers the DLinear challenge to Transformers by showing a vanilla-attention Transformer **can** be effective if designed properly. Proposes PatchTST (channel-independent Patch Time Series Transformer) built on two designs: 1. **Patching**: subseries-level patches as input tokens → retains local semantic information in embeddings, quadratically reduces attention compute/memory ($N \approx L/S$ tokens), and enables …
  - Additionally demonstrates SOTA **masked self-supervised representation learning** and cross-dataset transfer learning (pre-train on Electricity → fine-tune elsewhere), outperforming supervised training on large datasets.
- **Method core:** Problem: given multivariate samples with look-back $L$, each channel $x^{(i)}_{1:L} \in \mathbb{R}^{1\times L}$, $i=1,\dots,M$, forecast $T$ future values; each channel fed independently into the Transformer backbone (channel-independence).
- **Key results:**
  - Case study (Traffic, $T=96$): PatchTST $L=336$+patching MSE **0.367**, self-supervised **0.349**, vs DLinear 0.410 and FEDformer 0.597. Patching speedups at $L=336$: Traffic ×22 (464 s vs 10,040 s), Electricity ×19, Weather ×4.
  - Supervised benchmark (Table 3): vs best Transformer baselines, PatchTST/64 achieves overall **21.0% MSE / 16.7% MAE reduction**; PatchTST/42 **20.2% / 16.4%**. Beats DLinear especially on large datasets and ILI. Examples: Electricity T=96 MSE 0.129 (PatchTST/64) vs DLinear 0.140, FEDformer 0.186; Traffic T=720 0.432 …
  - Self-supervised (Table 4): fine-tuned pre-trained PatchTST further improves results — e.g., Electricity T=96 MSE **0.126**, Traffic T=96 **0.352**, beating supervised-from-scratch and all baselines; linear probing alone already beats DLinear.
- **Gaps/Limitations:**
  - Channel-independence ignores explicit cross-channel correlations; authors state modeling cross-channel dependencies properly is an important future step (suggest GNN-based extension).
  - No probabilistic/uncertainty quantification (point forecasts, MSE only).
  - Exchange-rate-type financial series excluded due to weak predictability — generalization claims limited to physical/engineering signals.

### 2023_TimesNet_Temporal_2D_Variation_Modeling
**TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis**  
Wu et al. · ICLR 2023 · 2023
<https://arxiv.org/abs/2210.02186>
**Models**: TimesNet, TimesNet, Inception_2D_CNN, FFT_Periodicity_Detection  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE, SMAPE, MASE, OWA, F1_Score  
**Data**: ETT; ETT; ETT; ETT; Electricity_ECL; Traffic; Weather; Exchange; ILI; M4; UEA_Archive; SMD; MSL; SMAP; SWaT; PSM  
**Features**: Multi_Periodicity, Intraperiod_Variation, Interperiod_Variation, Temporal_2D_Variations

- **What they did:**
  - Proposes TimesNet, a **task-general foundation model** (backbone) for five mainstream time-series tasks — short- and long-term forecasting, imputation, classification, anomaly detection — achieving consistent SOTA across all of them.
  - Core idea: real-world series exhibit **multi-periodicity** (e.g., daily + weekly cycles in electricity consumption). Each period induces two coupled variation types: **intraperiod-variation** (within a period, short-term patterns) and **interperiod-variation** (across consecutive periods, long-term trends).
  - Key innovation: transform the 1D series into a set of **2D tensors** based on discovered periods so both variation types are simultaneously representable (columns = intraperiod, rows = interperiod) and processable by mature 2D vision backbones (Inception_2D_CNN), bridging 1D time-series analysis with computer vision.
- **Method core:** Modular architecture: stacked TimesNets in residual fashion. Input embedding $X^0_{1D} = \text{Embed}(X_{1D}) \in \mathbb{R}^{T \times d_{model}}$; layer update:
- **Key results:**
  - **Long-term forecasting** (Table 2/13, look-back 96; ILI 36; avg over T∈{96,192,336,720}): SOTA in >80% of cases (40 first-place counts vs 14 DLinear, 6 FEDformer, 4 ETSformer). Examples (avg MSE/MAE): ETTm1 0.400/0.406 (vs DLinear 0.403/0.407, FEDformer 0.448/0.452); ETTm2 0.291/0.333; Electricity 0.192/0.295 (vs …
  - **Short-term M4** (Table 3/14, horizon 6–48): weighted average SMAPE **11.829**, MASE **1.585**, OWA **0.851** — beats N-HiTS (11.927/1.613/0.861) and non-ensembled N-BEATS (11.851/1.599/0.855).
  - **Imputation**: best on all datasets, e.g., ETTm1 avg MSE 0.027 vs FEDformer 0.062, DLinear 0.093; Electricity avg 0.092 vs Stationary 0.100.
- **Gaps/Limitations:**
  - Point forecasts only; no probabilistic/uncertainty modeling for forecasting.
  - Performance sensitive to top-k frequency count in low-level tasks (forecasting/anomaly detection); robust for high-level tasks.
  - Authors' stated future work: large-scale pre-training methods using TimesNet as general-purpose time-series backbone.
  - No explicit cross-variate dependency mechanism (each variate enters via channel dimension C of the 2D tensor; interactions learned only through convolutions).

### 2023_Transformer_EV_Demand
**Prediction of Electric Vehicles Charging Demand: A Transformer-Based Deep Learning Approach**  
Koohfar et al. · Sustainability 2023, 15(3), 2105 · 2023
<https://doi.org/10.3390/su15032105>
**Models**: Transformer, LSTM, RNN, ARIMA, SARIMA  
**Horizon**: Long_Term_Forecasting  
**Metrics**: RMSE, MAE, MSE  
**Data**: Boulder_Colorado; Weather  
**Features**: Historical_Load, Binary_Weekend_Indicator, Temperature, Snowfall, Precipitation

- **What they did:**
  - One of the first applications of the Transformer architecture to EV charging demand forecasting, benchmarked against LSTM, RNN, ARIMA, and SARIMA on real-world public charging data.
  - Evaluates multi-step forecasts at K = 7 (short-term), 30, 60, and 90 days ahead (long-term) using daily aggregated charging demand.
  - Key finding: Transformer is comparable to LSTM at K=7 but outperforms the next-best model by 62%, 78%, and 84% for 30, 60, and 90 days ahead respectively; statistical baselines collapse to near flat-line mean predictions.
- **Method core:** Five models implemented (Keras for LSTM/RNN, PyTorch for Transformer); deep hyperparameters: hidden dim 128, 1 layer, 8 attention heads, batch size 64, 100 epochs; 80/20 chronological train/test split (first 38 months train / last ~9 months test); min-max normalization.
- **Key results:**
  - Transformer best model at K=30/60/90; LSTM marginally better only at K=7 (RMSE 0.036 vs 0.055).
- **Gaps/Limitations:**
  - Daily aggregation only — cannot forecast sub-hourly steps (15 min, 1 h); authors recommend larger datasets with finer resolution (e.g., residential charging).
  - Small sample size (1,425 points) limits deep model training.
  - No traffic distribution features despite their influence on charging behavior; suggested for future work.
  - Only single-layer networks tested; other regression/DL/neural architectures recommended for future analysis.

### 2023_Treatment_Effects_Continuous_Time_Hidden_Confounders
**Estimating Treatment Effects in Continuous Time with Hidden Confounders**  
Cao et al. · arXiv preprint arXiv:2302.09446 (cs.LG), University of Southern California · 2023
<https://doi.org/10.48550/arXiv.2302.09446>
**Models**: LipSCDE, Neural_SDE, Neural_CDE, Lipschitz_RNN, LSTM, MSM, RMSN, TSD, DTA, SeqDec  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE  
**Data**: MIMIC-III; COVID-19_German_Districts; Synthetic_Irregular_Time_Series  
**Features**: Covariates, Treatments, Hidden_Confounders, High_Frequency_Components, Low_Frequency_Components, Brownian_Motion

- **What they did:**
  - Estimates individual/average treatment effects (ITE/ATE) in **continuous-time longitudinal settings with multi-cause hidden confounders** and irregularly sampled observations. Prior deconfounding works (TSD, SeqConf/SeqDec, DTA) either cannot handle irregular/sparse/intermittent time series or impose strong assumptions (e.g., multivariate Gaussian on irregular samples). Contributions: 1. **LipSCDE** — a …
- **Method core:** Two branches: **(a) Hidden Confounders Boundary Branch**: History trajectories $h_t$ are converted to the frequency domain via the Fourier transform $\mathcal{F}$; Gaussian high-pass filter $G_h$ and low-pass filter $G_l$ extract fast-changing boundary components vs. smooth trend components. Lipschitz-constrained convolutional operators + inverse Fourier transform …
- **Key results:**
  - All numbers are RMSE (%) — lower is better. **Real-world data (Table 1)**: (DTA/TSD rows reported under both MSM and RMSN outcome-model variants.) LipSCDE outperforms the TSD baseline by **27.2% on blood pressure** and **7.2% on COVID case prediction**; ties SeqDec at 4.19 on oxygen saturation. **Synthetic irregular …
- **Gaps/Limitations:**
  - Evaluation is one-step-ahead estimation; long-horizon counterfactual rollout is not addressed.
  - Hidden-confounder recovery relies on frequency-domain filtering + Lipschitz bounding heuristics; identifiability of the latent factor model is not formally proven.
  - Synthetic experiments are small-scale; only two real-world datasets (both clinical/epidemiological), no public-benchmark treatment-effect suites.
  - IPTW outcome correction inherits the usual propensity-weighting variance issues under extreme treatment probabilities.
  - **Relevance to EV charging load forecasting**: provides the causal/deconfounding machinery for **price-elasticity modeling of charging demand** — directly complements the PIML price-elasticity line of 2024_Physics_Informed_GAT_EV_Load and the price-elasticity-mechanism (PEM) module of 2026_TriModal_Causal_EV_Demand; LipSCDE's continuous-time treatment-effect framing maps naturally to modeling tariff changes …

### 2023_VMD_Prophet_LSTM
**Electric vehicle charging load prediction based on variational mode decomposition and Prophet-LSTM**  
Cheng et al. · Frontiers in Energy Research, Vol. 11, Article 1297849 · 2023
<https://doi.org/10.3389/fenrg.2023.1297849>
**Models**: VMD, Prophet, LSTM, Prophet-LSTM  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, R_squared  
**Data**: Fujian_Province_EV_Charging_Station_Data  
**Features**: Historical_Load, VMD, Zero_Crossing_Rate

- **What they did:**
  - Accurate EV charging load prediction is a prerequisite for grid planning and economic operation; real loads are highly volatile due to electricity prices, temperature, dates, etc.
  - Proposes a **VMD-Prophet-LSTM combined model**: VMD decomposes the charging load into $k$ Intrinsic Mode Functions (IMFs); IMFs are split by over-zero (zero-crossing) rate into **low-frequency** (stable, periodic) and **high-frequency** (volatile) reconstructed sequences; Prophet forecasts the low-frequency part while LSTM forecasts the high-frequency part; results are summed to the final forecast.
  - Reported average absolute error reductions of **7.57% vs ARIMA**, **8.73% vs LSTM**, and **46.02% vs Prophet**.
  - Motivation vs prior work: single-model deep predictors ignore component characteristics; prior VMD hybrids (GRU+TCN (Cai et al. 2022), GRU+ARIMA (Yu et al. 2022)) either use complex ARIMA tuning or one model for all components — Prophet avoids ARIMA's missing-data handling and parameter-tuning burden for medium-scale series.
- **Method core:** Architecture: **96-dimensional input layer, 1-dimensional output, 2 LSTM layers, 4 fully connected layers (128, 64, 32, 16 neurons)**, tanh activations, Adam optimizer. Implemented in Python 3.9 / TensorFlow / Keras / Prophet framework on an Intel i5-8300H + NVIDIA GTX 1050Ti (16 GB RAM).
- **Key results:**
  - Average absolute error lower than ARIMA by **7.57%**, LSTM by **8.73%**, Prophet by **46.02%**.
  - $R^2 = 0.8411 > 0.8$ indicates a good fit; proposed curve tracks real load best, especially through volatile segments.
  - Ablation insight: VMD enables Prophet to handle volatile sequences (raw Prophet alone collapses to R² ≈ 0.49).
- **Gaps/Limitations:**
  - Only univariate historical load; no explicit integration of external drivers (electricity prices, temperature, weather) into Prophet/LSTM inputs.
  - Single-station case study; no spatial/multi-station or transfer evaluation; no probabilistic/uncertainty quantification.
  - Fixed zero-crossing threshold (0.05) heuristic; k-selection via energy-jump rule is empirical.
  - Future work stated by authors: extend combined method to other domains (e.g., photovoltaic power prediction) to verify generalization.
  - Gap for thesis: deterministic point forecast only — motivates quantile/distributional hybrids and federated extensions across stations.

### 2022_GCN_TRN_EV_Availability
**GCN-TRN: Efficient Transformer based Electric Vehicle Charging Demand Forecasting System**  
Zhang et al. · 2022 5th International Conference on Computer Science and Software Engineering (CSSE … · 2022
<https://doi.org/10.1145/3569966.3570101>
**Models**: GCN-TRN, GCN, Transformer, GRU, GCN-GRU, SVR, HA  
**Horizon**: Spatial_Temporal_Forecasting  
**Metrics**: Accuracy, RMSE, MAE, R² Score, R_squared  
**Data**: Dundee_EV  
**Features**: Spatial Adjacency Matrix A_ij (true path distances), Availability p_n, Station_Occupancy, Latitude/Longitude, 30-min Occupancy Slots

- **What they did:**
  - **Core problem**: EV charging station (CS) availability forecasting must capture both **spatial relations** (correlations between neighboring stations via non-Euclidean road topology — ARIMA/SVR/KNN cannot mine spatio-temporal relations; CNN only handles Euclidean data) and **temporal dependence** (rush-hour-like charging periodicity). RNNs lose spatial info; GNNs can't process time series; Transformers aggregate …
  - **Primary contribution**: **GCN-TRN** — combines a GCN (spatial extraction from station graph $G=(V,E,A)$) with a Transformer (global-view temporal modeling, no sequential information loss) for long-term multi-step EV CS availability prediction.
  - Result: >80% accuracy at 30- and 60-min horizons on the Dundee City dataset; beats all baselines including vanilla Transformer (+14.3% accuracy at 30 min).
- **Method core:** Input: historical availability $X_s = \{x_{s-L-1},\ldots,x_s\} \in \mathbb{R}^{N\times L}$ plus station locations/connectivity; output $y_{s+W}$ = predicted availability $W$ steps ahead.
- **Key results:**
  - Baselines: HA, SVR, GRU, GCN-GRU, vanilla Transformer. Predictions for next **30-, 60-, 90-minute** intervals (Table 1):
  - GCN-TRN vs vanilla Transformer accuracy gains: **+14.3% (30 min)**, +13.4% (60 min), +13.3% (90 min) → demonstrates necessity of GCN spatial extraction layer.
  - GCN-GRU vs GRU accuracy gains: +2.1% (30 min), +6.1% (60 min), +10.6% (90 min).
- **Gaps/Limitations:**
  - Very small dataset: single city, ~15 days, 23 stations, 2746 sessions — limited generalization evidence; no train/test split details or hyperparameters reported.
  - Only availability magnitude $p_n$ modeled; no exogenous features (weather, POI/events mentioned qualitatively as factors but not included).
  - Short horizons only (≤90 min); "long-term" claim modest relative to day-ahead needs.
  - Metrics reported as raw numbers without variance/confidence intervals; no probabilistic/uncertainty output.
  - Gap for thesis: motivates richer spatial-temporal architectures (GCN + Transformer) on larger multi-city datasets with weather/calendar covariates and longer horizons.

### 2022_RevIN_Reversible_Instance_Normalization
**Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift**  
Kim et al. · ICLR 2022 · 2022
<https://openreview.net/forum?id=cGDAkQo1C0p>
**Models**: RevIN, Informer, NBEATS, SCINet  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE, DTW, TDI  
**Data**: ETT; Electricity_ECL; UCI_Air_Quality; Nasdaq_CNNpred; M4  
**Features**: Multivariate historical series (power load, oil temperature), Instance mean μ and standard deviation σ per input window, Learnable affine parameters γ, β

- **What they did:**
  - Addresses the **distribution shift problem** in time-series forecasting: statistical properties (mean/variance) of training vs. test data diverge because train/test splits are made at a point in time, degrading model accuracy — especially for long horizons.
  - Proposes **RevIN**: a simple, generally-applicable, end-to-end trainable **normalization-and-denormalization** layer with learnable affine transformation, symmetrically structured to *remove* non-stationary statistics (instance mean μ, variance σ²) at the input layer and *restore* them at the output layer.
  - Contributions: (1) model-agnostic plug-in layer applicable to any DNN with negligible cost; (2) state-of-the-art on seven large-scale real-world datasets by adding RevIN to Informer/N-BEATS/SCINet; (3) quantitative + qualitative analyses showing reduced train-test distribution discrepancy.
- **Method core:** RevIN consists of two symmetric layers placed at virtually symmetric positions of an encoder-decoder structure (input and output layers; can also be added to intermediate layers). **Equation 1 — Instance statistics (per variable k, instance i):**  \mathbb{E}_t[x_{kt}^{(i)}] = \frac{1}{T_x}\sum_{j=1}^{T_x} x_{kj}^{(i)}, \qquad \text{Var}[x_{kt}^{(i)}] = …
- **Key results:**
  - **ETTh1 @720**: SCINet 0.596/0.571 → **0.507/0.505**; N-BEATS 1.389/0.926 → 0.576/0.534; Informer 1.357/0.945 → 0.926/0.717.
  - **ETTh2 @960**: N-BEATS MSE 6.408 → **0.471**; Informer 2.972 → 0.600; SCINet 1.862 → **0.438**.
  - **ECL @960**: SCINet 0.235/0.330 → **0.200/0.292**; N-BEATS 0.399 → 0.325; Informer 0.930 → 0.894.
- **Gaps/Limitations:**
  - Purely point forecasts — no uncertainty quantification; no EV-specific evaluation despite direct relevance (EV charging load is strongly non-stationary across station lifecycle).
  - Assumes future window statistics ≈ input-window statistics plus a small offset (Eq. 9 assumption) — may fail under abrupt regime changes longer than the input window.
  - Evaluated mostly on generic benchmarks; no spatio-temporal modeling (each variable treated independently).
  - Gap for thesis: apply RevIN to EV charging load models (MetaProbformer, NHiTS) under distribution shift from new stations / anomalous events.

### 2022_Robust_Deep_Gaussian_Process_Load
**Robust Deep Gaussian Process-Based Probabilistic Electrical Load Forecasting Against Anomalous Events**  
Cao et al. · IEEE Transactions on Industrial Informatics, 18(2), 1142-1153 · 2022
<https://doi.org/10.1109/TII.2021.3081531>
**Models**: Deep_Gaussian_Process, Sparse_GP, VAE_DGP, SVR, BPNN  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: MAPE, Pinball_Loss  
**Data**: COVID19_US_City_Load; Weather; Google/Apple Mobility Data  
**Features**: Past 24h load (Italy case), Temperature, Humidity, Cloud_Cover, Precipitation, Air_Pressure, Timing features (month/day/hour index, weekday/holiday), Google mobility: parks, workplaces, residential, retail & recreation, grocery & pharmacy, …

- **What they did:**
  - Casts load forecasting at the **onset of anomalous events** (COVID-19 lockdowns) as a **regression problem with limited training samples**, solved by an enhanced **double stochastic variational inference Deep_Gaussian_Process (DGP)**.
  - Motivation: during COVID-19 the Northern Italy day-ahead MAPE of the system operator rose 61% (max MAPE +40%); mean absolute error grew from 329.5 to 428.2 MW (+30%) vs. 2019; French operator's adaptive-model MAPE was 5× normal during lockdown.
  - Contributions: (1) DGP with "self-tuning" covariance via hierarchical input-space warping — no manual kernel design, works with only days of data; (2) full uncertainty quantification enabling uncertainty-aware operations; (3) benchmarks on city-level and country-level datasets vs SVR/BPNN/SGP/VAE-DGP.
- **Method core:** **Equations (1)–(3) — GP prior with homoscedastic Gaussian noise:**  f(X) \sim \mathcal{GP}(m(X), K(X,X')), \qquad Y = f(X) + \epsilon,\; \epsilon \sim \mathcal{N}(0,\sigma_n^2 I), \qquad Y \sim \mathcal{GP}(m(X), K(X,X')+\sigma_n^2 I)  **Equation (5) — joint distribution of training outputs $Y$ and test latent $f_*$:**  \begin{bmatrix} Y \\ f_* \end{bmatrix} \sim …
- **Key results:**
  - **Small-scale (3 days training)**: proposed DGP best in most cases; beats one-layer Sparse_GP in 5/6 regions and both SVR and VAE_DGP; parametric BPNN overfits severely (large validation/test gaps). Max MAPE reduction vs other methods: **70.9%**.
  - **Middle-scale (~75 days)**: outperforms SVR/BPNN/VAE-DGP in all cases and SGP in 5 cases; max MAPE reduction **50.7%**.
  - **Probabilistic**: Pinball loss up to **46.6%** (small-scale) and **39.7%** (middle-scale) lower than SGP/VAE-DGP; at least 23.0% lower than SGP/VAE-DGP with more data. The proposed 95% CI covers almost all actual loads where SGP/VAE-DGP miss large stretches (Seattle t=50–70 etc.); peak/valley values well predicted; …
- **Gaps/Limitations:**
  - Gaussian posterior assumption per layer partially relaxed only by sampling; still GP-based (kernel stationarity assumptions).
  - Demonstrated on aggregate zonal/city load, not EV charging stations; authors state future work targets other low-data power-system applications.
  - Mobility features are pandemic-specific proxies — analog for EV would be e.g. traffic/events data for new or disrupted charging stations.
  - Gap for thesis: nonparametric few-shot probabilistic forecasting is directly transferable to newly commissioned EV_Charging_Station load prediction (compare with 2023_MetaProbformer_EV_Load).

### 2021_Autoformer_Decomposition_Transformers_AutoCorrelation
**Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting**  
Wu et al. · NeurIPS 2021 (35th Conference on Neural Information Processing Systems) · 2021
<https://arxiv.org/abs/2106.13008>
**Models**: Autoformer, Auto-Correlation Mechanism, Series_Decomposition_Block, Informer, LogTrans, Reformer, LSTNet, DeepAR, NBEATS, Prophet  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE  
**Data**: ETT; Electricity_ECL; Exchange; Traffic; Weather; ILI; COVID19_Dashboard  
**Features**: Trend-cyclical Component, Seasonal_Component, Autocorrelation_Time_Delay, Moving_Average_Decomposition

- **What they did:**
  - **Core problem**: In long-term forecasting (input-I-predict-O with large O), intricate/entangled temporal patterns make point-wise dependency discovery unreliable, and quadratic-complexity self-attention is prohibitive; sparse point-wise attention variants (Informer ProbSparse, LogTrans LogSparse, Reformer LSH) sacrifice information utilization.
  - **Primary contribution**: **Autoformer** — a decomposition architecture that (1) embeds a **series decomposition block as an inner operator** for *progressive* decomposition of intermediate hidden variables during forecasting (breaking the pre-processing convention of Prophet/N-BEATS/DeepGLO), and (2) an **Auto-Correlation mechanism** based on series periodicity performing sub-series-level (series-wise) dependencies …
  - Result: 38% average relative MSE improvement over previous SOTA across six benchmarks covering energy, traffic, economics, weather and disease.
- **Method core:** **Series decomposition block** (Eq. 1) — moving-average smoothing extracting trend-cyclical $X_t$ from length-$L$ input $X \in \mathbb{R}^{L\times d}$:  X_t = \text{AvgPool}(\text{Padding}(X)), \qquad X_s = X - X_t  summarized as $X_s, X_t = \text{SeriesDecomp}(X)$; adopted from classic decomposition but used as inner block throughout encoder/decoder.
- **Key results:**
  - **Overall**: 38% averaged MSE reduction under long-term settings across six benchmarks.
  - **Multivariate, input-96-predict-336 vs previous best**: 74% ETT (1.334→0.339), 18% Electricity (0.280→0.231), 61% Exchange (1.357→0.509), 15% Traffic (0.733→0.622), 21% Weather (0.455→0.359); ILI input-36-predict-60: 43% (4.882→2.770).
  - **ETT full benchmark (Appendix A)**: input-96-predict-336: 55% ETTh1 (Informer 1.128→0.505) and 80% ETTh2 (2.544→0.471) reduction; predict-288: 40% ETTm1 (1.056→0.634), 66% ETTm2 (0.969→0.342); ~60% average MSE reduction over prior SOTA on ETT. Example ETTm2 predict-96: Autoformer 0.255/0.339 (MSE/MAE) vs Informer …
- **Gaps/Limitations:**
  - Performance degrades on data with extremely weak temporal coherence/randomness (Exchange still works, but authors note poor-predictability series degenerate all models).
  - Hyper-parameter $c$ trades off performance vs efficiency and needs tuning; datasets without obvious periodicity (ILI) can suffer from large $c$ (noise).
  - Input-length sensitivity is dataset-specific (periodic data saturates at I=96; aperiodic ILI benefits from longer inputs).
  - Decoder past-information attachment ($\frac{I}{2}+O$) trades accuracy vs memory cost (3029 MB without past vs 3599 MB full past).
  - Gap for EV charging load forecasting: decomposition architecture + period-based Auto-Correlation directly applicable to strongly periodic station-level load series.

### 2021_CSDI_Conditional_Diffusion_Forecasting
**CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation**  
Tashiro et al. · NeurIPS 2021 (35th Conference on Neural Information Processing Systems) · 2021
<https://arxiv.org/abs/2107.03502>
**Models**: CSDI, Conditional Score-based Diffusion Model, DDPM, DDPM, Transformer, TimeGrad  
**Horizon**: Short_Term_Forecasting  
**Metrics**: CRPS, CRPS, MAE, RMSE, MSE, NLL  
**Data**: PhysioNet_2012_Healthcare; Beijing_PM25_Air_Quality; Solar_Alabama; Electricity_ECL; Traffic; NYC_Taxi; Wiki_Pageviews  
**Features**: Observation_Mask, Conditional_Mask, Timestamps, Temporal_Embedding, Feature_Embedding, Diffusion_Step_Embedding

- **What they did:**
  - **Core problem**: Probabilistic imputation of missing values in multivariate time series. Prior score-based approaches (Song et al. SDE; repainting-style methods) *approximate* the conditional reverse process by noising the observations, which destroys useful information in $x^{co}_0$ and does not correspond to the exact conditional distribution. Autoregressive/RNN imputation methods (BRITS, GLIMA) struggle with …
  - **Primary contribution**: **CSDI** — a conditional score-based DDPM trained *directly* on the conditional distribution $q(x^{ta}_0 \mid x^{co}_0)$ via a self-supervised masked-training scheme (inspired by masked language modeling / BERT), with a 2D (temporal + feature) Transformer denoiser based on DDPM.
  - Results: CRPS improved **40–65%** over existing probabilistic imputation baselines; deterministic MAE improved **5–20%** over SOTA deterministic methods; also competitive at interpolation and probabilistic forecasting.
- **Method core:** **Denoiser architecture**: DiffWave-based residual network, adapted: diffusion steps $T=50$; DiffWave's dilated convolutions replaced by **2D attention** — temporal Transformer layer (input shape $(1,L,C)$, per-feature temporal dependency) + feature Transformer layer (shape $(K,1,C)$, per-timestep cross-feature dependency), each a 1-layer PyTorch TransformerEncoder (8 heads). …
- **Key results:**
  - **Probabilistic imputation (CRPS, lower better)**: healthcare CSDI 0.238 / 0.330 / 0.522 (10/50/90% missing) vs GP-VAE 0.574 / 0.774 / 0.998, Multitask GP 0.489 / 0.581 / 0.942, V-RIN 0.808 / 0.831 / 0.922; air quality CSDI **0.108** vs GP-VAE 0.397 → 40–65% CRPS reduction; unconditional diffusion clearly worse (e.g., …
  - **Deterministic imputation (MAE, median of 100 samples)**: healthcare 10% missing CSDI **0.217** vs BRITS 0.284, GLIMA* 0.265, V-RIN 0.271, RDIS 0.319; air quality CSDI **9.60** vs GLIMA* 10.54, BRITS 11.56–14.11 → 5–20% improvement. RMSE similarly best (healthcare 10%: CSDI 0.498 vs SSGAN* 0.598, BRITS 0.619; air …
  - **Interpolation (irregularly sampled healthcare)**: CRPS CSDI 0.380 / 0.418 / 0.556 vs mTANs 0.526 / 0.567 / 0.689 and Latent ODE 0.700+; MAE/RMSE consistent.
- **Gaps/Limitations:**
  - Sampling speed: iterative reverse diffusion (50 steps × network evals) slower than other generative models — authors suggest ODE solvers (DDIM etc.) for acceleration; relevant gap for real-time EV load forecasting deployment.
  - Forecasting advantage smaller than imputation advantage since benchmark forecasting datasets have few missing values and suit RNN encoders.
  - Historical strategy can underperform when train/test missing patterns differ.
  - ELBO unsuitable as evaluation metric for noisy time series.
  - Future work: joint training of imputation with downstream tasks (classification); extension to other modalities.

### 2021_Conformal_Time_Series_Forecasting
**Conformal Time-Series Forecasting**  
Stankevičiūtė et al. · NeurIPS 2021 (35th Conference on Neural Information Processing Systems) · 2021
<https://proceedings.neurips.cc/paper/2021/file/9232fe81225bcaef853ae32870a2b0fe-Paper.pdf>
**Models**: CF-RNN, Conformal_Prediction, ICP, LSTM, BJ-RNN, MQ-RNN, DP-RNN  
**Horizon**: Short_Term_Forecasting  
**Metrics**: Joint_Coverage, MPIW  
**Data**: MIMIC-III; UCI_EEG; COVID19_UK_Dataset; Synthetic_AR_Noise  
**Features**: Conformal_Prediction, Conformal_Prediction, Multi_Horizon_Forecast, Direct_Forecasting_Strategy

- **What they did:**
  - **Core problem**: RNN-based multi-horizon forecasts issue point estimates only; existing uncertainty methods (Bayesian RNNs, quantile RNNs like MQ-RNN, ensembles/bootstrapping like BJ-RNN) require architecture changes, are hard to calibrate, scale poorly (BJ-RNN exact inference is $O(P^3)$ in parameters $P$), and lack finite-sample frequentist coverage guarantees.
  - **Primary contribution**: Extends **inductive conformal prediction (ICP)** to the multi-horizon time-series setup → **Conformal Forecasting RNN (CF-RNN)**: a lightweight post-hoc wrapper around *any* direct multi-horizon point forecaster producing distribution-free prediction intervals with theoretical $(1-\alpha)$ joint coverage over the whole trajectory — no retraining of the base model.
  - Key insight: time-steps within a series are non-exchangeable, but the dataset is treated as a set of **exchangeable whole-series observations** $(y_{1:T}, y_{T+1:T+H})$.
- **Method core:** Wrapper around a direct-strategy LSTM (all $H$ steps predicted simultaneously from one embedding — robust to error accumulation and gives conditionally independent predictions needed for the guarantee).
- **Key results:**
  - **Synthetic data (90% target joint coverage)**: CF-RNN achieves 90.6–94.6% coverage across all static/time-dependent noise profiles vs MQ-RNN ~57–67% and DP-RNN ~0–5%; BJ-RNN hits 97–100% but with far wider intervals (e.g. width 98.45 ± 25.95 vs CF-RNN's 16.45 ± 3.69 at static $n=1$) and prohibitive compute ($O(P^3)$).
  - CF-RNN intervals adapt to noise: nearly constant width under static noise (16.45–17.34), widening monotonically under time-dependent noise (19.80 → 49.00 as variance accumulates).
  - MIMIC-III: joint coverage 94.0 ± 1.2% (MQ-RNN 89.3 ± 1.2%, DP-RNN 40.2 ± 13.9%); CI length 20.59 ± 3.10
- **Gaps/Limitations:**
  - Univariate focus ($d=1$); multivariate extension left as future work.
  - Intervals are widest among compared models (conservative efficiency); future work targets narrower, more adaptive per-observation intervals.
  - Relies on exchangeability of whole-series observations; adaptation lag possible under strong non-stationarity.
  - Direct (not recursive) forecasting strategy required for the theory.
  - Relevant gap for EV load forecasting: cheap post-hoc $(1-\alpha)$ trajectory guarantees for any point forecaster without retraining.

### 2021_Day_Ahead_EV_Demand
**Day-Ahead Forecast of Electric Vehicle Charging Demand with Deep Neural Networks**  
Kriekinge et al. · World Electric Vehicle Journal, 12(4), 178 · 2021
<https://doi.org/10.3390/wevj12040178>
**Models**: LSTM, LSTM_B, LSTM_C, LSTM_W, RNN  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: RMSE, MAE, MSE  
**Data**: Hospital_Semi_Public_Charging_Site_Dataset  
**Features**: EV_Charging_Demand, EV_Charging_Demand, Cyclical_Quarter_Hour_Features, Cyclical_Day_Number_Features, Holiday_Flag, Holiday_Flag, Temperature, Daily_Rainfall

- **What they did:**
  - Enhances a state-of-the-art deep neural network to forecast the **day-ahead aggregated EV charging demand** at **15-min resolution** (96 timesteps/day) for a **small, highly stochastic EV fleet** — a use case underrepresented in the literature (most work targets large fleets or super-short-term horizons).
  - New contributions over the reference forecaster (LSTM_B, from Zhu et al.): additional calendar and weather input features, a **variable learning rate function**, and **forecast post-processing** rules; plus a feature-importance analysis.
  - Main achievement: day-ahead forecast of high-stochasticity demand with **MAE < 1 kW**; MAE reduced by up to **28.8%** and RMSE by **19.22%** thanks to calendar/weather features. Extended version of the authors' EVS34 paper.
- **Method core:** Raw individual charging sessions (RFID, arrival/departure times, kWh energy) → individual EV charging profiles via average power (**Average Power Equation**):  P_{avg} = \frac{\text{Energy consumed [kWh]}}{\text{Parking time [h]}} \tag{1}  Individual profiles are stacked into the aggregated EV charging demand time series. This indirectly encodes user charging flexibility …
- **Key results:**
  - Metrics: RMSE $= \sqrt{\frac{1}{N}\sum_{t=1}^{N}(\hat{P}_t - P_t)^2}$ (Eq. 14), MAE $= \frac{1}{N}\sum_{t=1}^{N}|\hat{P}_t - P_t|$ (Eq. 15), N = 96 timesteps per day-ahead forecast. Test-subset results:
  - Two-week example: on 13 & 15 July, LSTM-W reduced RMSE by up to **92.7%** and MAE by up to **92.5%** vs LSTM-B (correctly forecasting Saturday as non-working day).
  - Feature importance (VIANN weight analysis): past-24-h demand dominant for both; binary holiday most important calendar feature for LSTM-C; weather features carry large weights in LSTM-W. Leave-One-Feature-Out: removing the binary holiday feature raises that day's MAE **5.78×** and RMSE **6.11×** (15 Aug, Belgian …
- **Gaps/Limitations:**
  - Average-power profile construction yields discrete steps in the real aggregated demand curve that the networks cannot accurately predict.
  - Poor weekend forecasts due to stochastic non-commuter behavior.
  - Dataset private (RFID privacy) — no public benchmark reproducibility.
  - Single use case only; authors call for testing across different sites to check whether behavioral patterns generalize and to guide forecaster selection per application.
  - Point forecast only — no probabilistic/uncertainty output despite high stochasticity.

### 2021_Hierarchical_Probabilistic_EV_Load
**An ensemble methodology for hierarchical probabilistic electric vehicle load forecasting at regular charging stations**  
Buzna et al. · Applied Energy, 283, 116337 · 2021
<https://doi.org/10.1016/j.apenergy.2020.116337>
**Models**: GBRT, QRF, QRNN, PLQR, PCA  
**Horizon**: Short_Term_Forecasting  
**Metrics**: Pinball_Loss, AACE  
**Data**: ElaadNL; Weather; COROP_Regions  
**Features**: Historical_Load, Weather_Forecast_Features, Super_User_Features, Calendar_Features, PCA, Historical_Load

- **What they did:**
  - First application ever of a **hierarchical approach to probabilistic EV load forecasting (PEVLF)**: forecast EV energy consumption of a high-level geographic region by exploiting baseline probabilistic forecasts of its constituent low-level regions.
  - Contributions: (i) hierarchical probabilistic forecasting framework; (ii) evaluation of **PCA dimensionality reduction** in preprocessing; (iii) comparative proof that hierarchy beats direct non-hierarchical forecasting regardless of the underlying model; (iv) extensive validation on real multi-year charging data.
  - Result: hierarchical approaches increase the skill of probabilistic forecasts by **up to 9.5%** vs non-hierarchical ones.
- **Method core:** Three units: input pre-processing (incl. PCA) → baseline probabilistic models per low-level region → l1-penalized linear quantile regression (PLQR) ensemble at the high level. Forecasts are Q = 9 quantiles at coverages α = 0.1,…,0.9; hourly resolution. Function estimation $P_i = f_i(x_i)$ minimized via a proper score (**Loss Minimization**):  \hat{f}_i(x_i) = …
- **Key results:**
  - Metrics: averaged **PS** (kWh, negatively oriented; Eq. 20) and **AACE%** reliability (100/Q · Σ|αq − α̂q|; Eq. 21–22), Q = 9 quantiles.
  - Hour-ahead baselines (PS kWh): GBRT best on average — Noordoost 18.07, Rijnmond 22.30, Utrecht 14.47, Zuidoost 17.51 vs BPersB 28.34/38.84/22.85/30.75 (36–43% improvement). PCA improves PS by ~1–11% in 3 of 4 regions and cuts training time by >78%.
  - Hour-ahead hierarchical (high-level, test set): **PLQR proposal PS 41.35–42.13 kWh** depending on base model (GBRT: 41.57/AACE 1.07%; QRF: 41.35/0.36%; QRNN: 42.13/1.75%) vs Direct 42.91–45.29, SaS 44.92–48.92 (AACE >7%), NPLQR 42.68–44.18, HPersB 89.87 → **~54% better than persistence**, **3.5–8% better than direct**.
- **Gaps/Limitations:**
  - Short-term focus: time-varying predictors such as number of circulating EVs or # stations excluded (limited short-term impact; relevant at medium term).
  - Single-model baseline per region; authors propose extending to **multi-model ensemble frameworks** in future work.
  - Future work: apply the hierarchical PEVLF system to optimal distribution grid operation (bi-level optimization, market participation).
  - Hierarchical merging is generally a nonlinear non-convex problem without global optimality guarantees (motivating their simple penalized-linear approach).

### 2021_Informer_Beyond_Efficient_Transformer
**Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting**  
Zhou et al. · AAAI 2021 (Best Paper Award) · 2021
<https://arxiv.org/abs/2012.07436>
**Models**: Informer, ProbSparse Self-Attention, Self-Attention_Distilling, Generative Style Decoder, LogTrans, Reformer, LSTMa, LSTnet, DeepAR  
**Horizon**: Long_Term_Forecasting  
**Metrics**: MSE, MAE  
**Data**: ETT; Electricity_ECL; Weather  
**Features**: Oil Temperature (target), 6 Power Load Features, Wet Bulb (target), 11 Climate Features, Global/Local Timestamp Embeddings, ProbSparse_Attention

- **What they did:**
  - **Core problem**: Long sequence time-series forecasting (Long_Term_Forecasting) — vanilla Transformer has three LSTF limitations: (1) quadratic $O(L^2)$ self-attention time/memory per layer; (2) memory bottleneck $O(J \cdot L^2)$ when stacking $J$ layers for long inputs; (3) speed plunge of step-by-step dynamic decoding for long outputs.
  - **Primary contribution**: **Informer** with three distinctive characteristics:
  - **ProbSparse self-attention**: $O(L\log L)$ time and memory via KL-divergence-based query sparsity measurement selecting only Top-$u$ dominant queries.
  - **Self-attention distilling**: halves cascading layer input via conv + max-pooling, total space complexity $O((2-\epsilon)L\log L)$.
  - **Generative style decoder**: predicts the whole long output in ONE forward pass (no autoregressive dynamic decoding), avoiding cumulative error spreading.
- **Method core:** **LSTF problem setup**: rolling forecasting with fixed window; input $X^t = \{x_1^t,\ldots,x_{L_x}^t \mid x_i^t \in \mathbb{R}^{d_x}\}$, output $Y^t = \{y_1^t,\ldots,y_{L_y}^t \mid y_i^t \in \mathbb{R}^{d_y}\}$, $L_y \gg$ prior works.
- **Key results:**
  - **Multivariate (Table 2)**: Informer wins 33/48 cases vs Informer† 14. Example ETTh1 predict-168: Informer 0.931 MSE vs LogTrans 1.002, Reformer 1.824, LSTMa 1.212; ECL predict-720: 0.406/0.443 (MSE/MAE) vs Reformer 2.009/1.170. MSE decreases vs RNN-based LSTMa/LSTnet by **26.6% (at 168)**, **28.2% (at 336)**, **34.3% …
  - **Univariate (Table 1)**: Informer wins 32 cases vs Informer† 12. MSE decrease vs LSTMa: **26.8% (168)**, **52.4% (336)**, **60.1% (720)**; vs DeepAR/ARIMA/Prophet average: **49.3% (168)**, **61.1% (336)**, **65.1% (720)**. DeepAR better only on ECL short horizons (≤336).
  - **Prediction capacity**: error rises smoothly/slowly with growing horizon (vs LSTM failing beyond length 48, Fig. 1b); granularity experiment shows ETTm1 minute-level results aligned with ETTh1 hour-level hold across granularities.
- **Gaps/Limitations:**
  - Multivariate advantage shrinks vs univariate — attributed to anisotropy of feature dimensions' prediction capacity ("beyond the scope of this paper").
  - ProbSparse relies on the long-tail sparsity assumption and max-mean approximation (Lemma 1/Proposition 1 are probabilistic, not exact).
  - Dynamic decoding baselines (Reformer) perform poorly in LSTF — architecture choice (generative decoder) matters more than attention alone.
  - Gap for EV charging load forecasting: Informer's $O(L\log L)$ attention + single-forward multi-step decoder directly applicable to long-horizon station/load series; serves as key baseline in EV forecasting benchmarks.

### 2021_Probabilistic_Queuing_EV_Load
**Deep-Learning-Based Probabilistic Forecasting of Electric Vehicle Charging Load With a Novel Queuing Model**  
Zhang et al. · IEEE Transactions on Cybernetics, Vol. 51, No. 6, pp. 3157-3170 · 2021
<https://doi.org/10.1109/TCYB.2020.2975134>
**Models**: CNN, Discrete Wavelet Transform (WT), Gaussian Mixture Model, M/M/C/K Markov Queuing Model, CNN Ensemble PIs, BPNN, SVM, Stacked Autoencoder (SAE)  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, RMSE, MAPE, PICP, ACE, IS, PL  
**Data**: M42_Motorway_Traffic_Flow; UK_National_Travel_Survey; 2009 US National Household Travel Survey  
**Features**: Traffic, Daily_Travel_Distance, EV_Arrival_Rate, State of Charge (SOC), Driver_Behavior

- **What they did:**
  - First framework to forecast **EV charging station load probabilistically** by chaining: (1) deep-learning Traffic prediction with prediction intervals (PIs), (2) mixture-model-based EV arrival rate estimation, (3) a novel capacity-constrained $M/M/C/K$ Queuing_Model that converts TF → charging power while modeling **charging service limitations and three driver behaviors** (forced leave, refuse to join, impatient …
  - Quantifies both **model uncertainty** ($\sigma_m^2$) and **data uncertainty** ($\sigma_d^2$) via a CNN ensemble to build reliable PIs at PINC = 90%, 95%, 99%.
  - Supports multiple horizons: 1-h ahead (main), plus 6-h, 12-h, 18-h, and 24-h (Day_Ahead_Forecasting) multi-output forecasting.
- **Method core:** Pipeline (Algorithm 1): normalize TF → wavelet decomposition per frequency → per-frequency CNN training → wavelet reconstruction → deterministic point forecast → PI construction from model+data uncertainty → arrival rate estimation → queuing-model load conversion.  y_j^l = f\left(\sum_{i \in M_j} x_i^{l-1} \otimes k_{ij}^l + b_j^l\right) \tag{Convolution}  with sigmoid …
- **Key results:**
  - Deterministic 1-h ahead TF forecast (spring): **WT-CNN: MAE = 93.42, RMSE = 118.32, MAPE = 3.29%** vs BPNN (296.59 / 416.69 / 10.56%), SVM-RBF (229.81 / 341.55 / 8.18%), SAE (265.67 / 382.40 / 9.46%) — errors roughly half those of all six benchmarks (also TDNN, growing DBN, RNN). Probabilistic 1-h ahead (PINC = 95%): …
- **Gaps/Limitations:**
  - Charging load validated on a **simulated FCS** driven by real TF — no measured charging-session data; queuing parameters ($\sigma$, $\delta$, $\varsigma$) assumed rather than empirically fitted.
  - Single-station scope (one motorway segment); no spatial generalization across networks.
  - Driver behavior modeled via stylized exponential/logarithmic heuristics; no price-responsive or dynamic behavioral adaptation.
  - PI construction assumes Gaussian error structure via $z_{1-\alpha/2}$ critical values; no nonparametric quantile learning.
  - Gap for thesis: combining this traffic-to-power physical conversion with end-to-end probabilistic deep models (TimeGrad, Temporal_Fusion_Transformer) remains open.

### 2021_RL_Q_Learning_EV_Load
**Reinforcement Learning-Based Load Forecasting of Electric Vehicle Charging Station Using Q-Learning Technique**  
Dabbaghjamanesh et al. · IEEE Transactions on Industrial Informatics, Vol. 17, No. 6, pp. 4229-4237 · 2021
<https://doi.org/10.1109/TII.2020.2990397>
**Models**: Q-Learning (off-policy RL), ANN, RNN  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MSE, Training_Epochs  
**Data**: MATLAB-simulated PHEV charging scenarios (uncoordinated / coordinated / smart)  
**Features**: Previous 24-h PHEV loads, Charging_Start_Time, State of Charge (SOC), Battery_Capacity, AER, Daily_Driven_Miles, DOD

- **What they did:**
  - **First RL-based framework covering all three PHEV charging regimes** — uncoordinated, coordinated, and smart charging — for EV charging station load forecasting.
  - Proposes an **off-policy Q_Learning ensemble selector**: an agent learns hour-by-hour which base model (ANN vs RNN) to trust for each of the next 24 hourly steps, using an exponential error-based reward with a randomized exploration factor $\lambda$ around candidate predictions.
  - Claims >50% accuracy improvement (MSE reduction) over standalone ANN/RNN under the hardest regime (smart charging), where price incentives cause sharp non-stationary load shifts.
- **Method core:** Charging start-time PDFs per scenario:  f(t_s)=\frac{1}{b-a},\ b=19,\ a=18,\ a\le t_s\le b \quad \text{(Uncoordinated: evening plug-in ~6 PM)}   f(t_s)=\frac{1}{b-a},\ a=21,\ b=24,\ a\le t_s\le b \quad \text{(Coordinated: off-peak ~9 PM)}   f(t_s)=\frac{1}{\psi\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{t_s-\mu}{\psi}\right)^2},\ \mu=1,\ \psi=3 \quad \text{(Smart: SOC + price …
- **Key results:**
  - MSE comparison across scenarios at 30%/50% penetration (Table IV; best in bold):
  - Paper's stated headline result: under the worst scenario (smart charging), Q-learning achieves **more than 50% improvement** over conventional ANN/RNN techniques (Conclusion, Sec. VI).
  - Deeper/wider networks improve all models (sensitivity analysis Figs 10–12): 3 hidden layers × 500 nodes outperform 2×200/300/400 for ANN, RNN, and Q-learning alike.
- **Gaps/Limitations:**
  - **Entirely synthetic evaluation**: loads generated from stylized parametric PDFs; no empirical validation against measured charging-station sessions, no confidence intervals or statistical tests on reported MSEs.
  - Action space limited to selecting between only two base models (ANN/RNN) — no richer ensemble, no continuous blending weight, no modern sequence models (LSTM/GRU/TFT variants) as candidates despite being mentioned in the related work.
  - Reward requires ground truth during learning — formulation is closer to adaptive model weighting than true online forecasting without labels.
  - Only residential level-1/2 charging modeled (public DC fast charging excluded); single aggregation-level station load, no spatial/network dimension.
  - Fairness caveat: Q-learning used 10,000 iterations vs 500–3,000 for baselines, so part of the gain is compute rather than methodology.
  - Gap for thesis: combining RL model selection with probabilistic forecasts (TimeGrad, Temporal_Fusion_Transformer) or applying it as a meta-learner over deep ensembles on real EV session data remains untested.

### 2021_TFT_Temporal_Fusion_Transformers
**Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting**  
Lim et al. · International Journal of Forecasting, Vol. 37, No. 4, pp. 1374-1389 · 2021
<https://doi.org/10.1016/j.ijforecast.2021.03.012>
**Models**: Temporal Fusion Transformer, Gated Residual Network, Variable Selection Network, LSTM, Interpretable_Multi_Head_Attention, Quantile_Regression  
**Horizon**: Multi_Horizon  
**Metrics**: Pinball_Loss, Pinball_Loss, q-Risk  
**Data**: UCI Electricity Load Diagrams (ECL); UCI PEM-SF Traffic; Favorita Grocery Sales; OMI Realized Volatility  
**Features**: Static_Covariates, Past_Observed_Inputs, Known_Future_Inputs, Calendar_Features, Entity_Embeddings

- **What they did:**
  - Proposes the **Temporal Fusion Transformer**: an attention-based architecture for **multi-horizon forecasting** that natively handles heterogeneous inputs — Static_Covariates, Past_Observed_Inputs, and Known_Future_Inputs — which autoregressive models (DeepAR, DSSM, ConvTrans) and prior direct methods (MQRNN, Seq2Seq) mishandle or treat as black boxes.
  - Five architectural novelties: (1) gating mechanisms for adaptive depth, (2) instance-wise variable selection networks, (3) static covariate encoders producing context vectors, (4) LSTM sequence-to-sequence local processing + interpretable multi-head self-attention decoder, (5) quantile outputs for prediction intervals.
  - Three interpretability use cases demonstrated on whole datasets: global variable importance, persistent temporal patterns (seasonality/lags from raw data), and regime/event identification (S&P 500 2008 crisis detected via attention-distance metric).
- **Method core:** Problem setup (Eq. 1): entity $i$ has static covariates $s_i$, observed inputs $z_{i,t}$ (unknown in advance), known inputs $x_{i,t}$ (predetermined); quantile forecast over look-back window $k$ and horizons $\tau\in\{1,\dots,\tau_{max}\}$:  \hat{y}_i(q,t,\tau) = f_q(\tau,\; y_{i,t-k:t},\; z_{i,t-k:t},\; x_{i,t-k:t+\tau},\; s_i) \tag{Quantile Forecast Form}  …
- **Key results:**
  - **Outperforms all benchmarks on every dataset** (Table 2), improving on the next-best method by **3%–26%**; average **7% lower P50 and 9% lower P90** losses vs next best model.
  - Electricity P50/P90: TFT **0.055 / 0.027** vs ConvTrans 0.059 (+7%) / 0.034 (+26%), DeepAR 0.075 (+36%) / 0.040 (+48%), TRMF 0.084 (+53%), DSSM 0.083 (+51%), ETS 0.102 (+85%), ARIMA 0.154 (+180%), MQRNN 0.077 (+40%), Seq2Seq 0.067 (+22%).
  - Traffic P50/P90: TFT **0.095 / 0.070** vs ConvTrans 0.122 (+28%) / 0.081 (+15%), Seq2Seq 0.105 (+11%) / 0.075 (+6%), DeepAR 0.161 (+69%) / 0.099 (+40%).
- **Gaps/Limitations:**
  - Single interpretable attention layer only; quadratic attention cost limits very long look-back windows.
  - Iterative baselines required imputation of unknown future inputs (last-value carry-forward), an artificial handicap whose realism varies by application.
  - Static enrichment assumes informative metadata; datasets lacking rich static covariates (Electricity/Traffic use only entity ID) limit that pathway's evaluation.
  - Quantiles fixed at {0.1, 0.5, 0.9}; no full predictive density or joint multivariate sampling across entities.
  - Gap for thesis: TFT's point/quantile forecasts are not calibrated probabilistically (vs conformal methods like 2021_Conformal_Time_Series_Forecasting) and its attention cost motivates efficient variants (2021_Informer_Beyond_Efficient_Transformer) — both relevant to EV charging load forecasting where station-level static metadata and calendar features abound.

### 2021_TimeGrad_Diffusion_Forecasting
**Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting**  
Rasul et al. · ICML 2021 (International Conference on Machine Learning), Zalando Research · 2021
<https://arxiv.org/abs/2101.12072>
**Models**: TimeGrad, Denoising Diffusion Probabilistic Model, 2-layer LSTM RNN, Conditional Dilated ConvNet (εθ), Score_Matching  
**Horizon**: Short_Term_Forecasting  
**Metrics**: CRPS, CRPS  
**Data**: Exchange; Solar; Electricity (UCI Load Diagrams); PEM-SF Traffic; NYC_Taxi; Wikipedia_Pageviews  
**Features**: Multivariate_Time_Series, Historical_Load, Calendar_Features, Lag_Features, Mean_Scaling

- **What they did:**
  - Introduces **TimeGrad**: an autoregressive energy-based model that samples from the **full joint multivariate predictive distribution at each time step** via denoising diffusion (DDPM), avoiding restrictive parametric emission families (Gaussian / negative binomial / low-rank copulas / normalizing flows).
  - Combines autoregressive extrapolation strength with EBM flexibility: diffusion head conditioned on an LSTM hidden state estimates the **score** of the data distribution; sampling proceeds by annealed Langevin-style reverse Markov chain from white noise.
  - New state-of-the-art multivariate probabilistic forecasting on benchmarks with up to thousands of correlated dimensions (963 traffic sensors, 2,000 Wikipedia pages).
- **Method core:** Fixed forward process adding Gaussian noise along variance schedule $\beta_1,\dots,\beta_N$:  q(x_n|x_{n-1}) := \mathcal{N}(x_n;\sqrt{1-\beta_n}\,x_{n-1},\ \beta_n\mathbf{I})  Learned reverse process with Gaussian transitions starting at $p(x^N)=\mathcal{N}(0,\mathbf{I})$:  p_\theta(x_{n-1}|x_n) := \mathcal{N}(x_{n-1};\ \mu_\theta(x_n,n),\ \Sigma_\theta(x_n,n)\mathbf{I}) …
- **Key results:**
  - Test-set CRPS (lower better; TimeGrad = mean ± SE over 10 retraining runs, Table 2):
  - New SOTA on all datasets except the smallest (Exchange, where VAR/VES/Transformer-MAF tie at 0.005): ~21% lower CRPSsum than Transformer-MAF on Traffic, ~21% on Wikipedia, ~36% on Taxi vs GP methods.
  - **Ablation on diffusion length $N$** (Electricity): performance already good at $N\approx10$, optimal at $N\approx100$; larger $N$ not beneficial. Linear schedule $\beta_1=10^{-4}\to\beta_N=0.1$, $N=100$ used throughout.
- **Gaps/Limitations:**
  - **Inference latency**: sampling loops $N=100$ times over $\epsilon_\theta$ per autoregressive timestep × $S=100$ trajectory samples — costly for large-scale or near-real-time EV forecasting (mitigations noted: WaveGrad-style L1 loss/fewer steps; DDIM non-Markovian processes, Song et al. 2021).
  - RNN conditioning limits very long sequences — authors propose Transformer encoders as replacement conditioning backbone.
  - No explicit modeling of discrete distributions (flows need dequantization; EBMs do not — left as future work).
  - No spatial inductive bias: suggests graph neural networks when inter-entity relationships are known (e.g., road networks between charging stations).
  - Future work flagged by authors: anomaly/OOD detection exploiting EBM likelihood behavior.
  - Gap for thesis: unconditional-per-step diffusion cost vs 2021_CSDI_Conditional_Diffusion_Forecasting's joint temporal diffusion for EV charging applications.

### 2020_DeepAR_Probabilistic_Forecasting
**DeepAR: Probabilistic Forecasting with Autoregressive Recurrent Networks**  
Salinas et al. · International Journal of Forecasting, 36(3), 1181-1191 · 2020
<https://doi.org/10.1016/j.ijforecast.2019.11.003>
**Models**: DeepAR, LSTM  
**Horizon**: Short_Term_Forecasting  
**Metrics**: Pinball_Loss, ND, RMSE  
**Data**: Parts_Dataset; Electricity_ECL; Traffic; Amazon_EC_Dataset; Amazon_EC_Dataset  
**Features**: Age_Feature, Calendar_Features, Item_Embedding, Scale_Factor

- **What they did:**
  - Introduces **DeepAR**, a methodology for probabilistic forecasting based on training an **autoregressive recurrent network** (multi-layer LSTM) as a **global model** across a large number of related time series.
  - Key contributions: 1. An RNN architecture for probabilistic forecasting incorporating a **negative-binomial likelihood** for count data plus special treatment for **power-law scale heterogeneity** across series (item-dependent rescaling + velocity-weighted sampling). 2. Empirical demonstration of ~**15% accuracy improvement** over state-of-the-art methods on several real-world datasets.
  - Advantages over classical per-series methods: minimal manual feature engineering; Monte Carlo samples yield consistent quantile estimates for all sub-ranges; forecasts for items with **little or no history**; flexible likelihood choice (no Gaussian-noise assumption).
- **Method core:** where $h$ is a multi-layer RNN with LSTM cells (3 layers); encoder and decoder share weights (same architecture for conditioning and prediction ranges). Initial state $h_{i,0}$ and $z_{i,0}$ are zero-initialized.
- **Key results:**
  - Metrics: **ρ-risk** (normalized quantile loss, $\rho \in \{0.5, 0.9\}$) over spans $[L, L+S)$, ND (normalized deviation), RMSE. Quantile loss definition: $\mathcal{L}_\rho(Z, \hat{Z}^\rho) = 2(\hat{Z}-Z)\big(\rho\,\mathbb{I}_{\hat{Z}^\rho > Z} - (1-\rho)\,\mathbb{I}_{\hat{Z}^\rho \leq Z}\big)$; ρ-risk = $\big(\sum_i …
  - parts (baseline Snyder): DeepAR avg 0.5-risk **0.94**, 0.9-risk **0.94** vs ISSM 1.08/1.01, ETS 1.23/1.08, rnn-negbin 0.99/0.99.
  - ec-sub (baseline ISSM): DeepAR **0.77** avg (0.5-risk all spans) and **0.57** (0.9-risk) — large gains vs ETS 1.07, rnn-gaussian 1.21.
- **Gaps/Limitations:**
  - Autoregressive teacher-forcing mismatch between training and prediction (exposure bias); scheduled sampling did not help here but remains a known issue in other domains.
  - Scale factor choice ($\nu_i$) is a heuristic; challenging with missing data or large within-series variance.
  - Marginal independence across time steps in some settings; correlations only via sampled paths.
  - Hyper-parameter tuning could overfit the validation split; authors suggest non-overlapping time intervals for tuning.
  - Evaluation with missing prediction-range data requires adjusted metrics not comparable across studies (not addressed experimentally).

### 2020_Ensemble_EV_Load
**Ensemble Learning for Charging Load Forecasting of Electric Vehicle Charging Stations**  
Huang et al. · 2020 IEEE Electric Power and Energy Conference (EPEC) · 2020
<https://doi.org/10.1109/EPEC48502.2020.9319916>
**Models**: Ensemble_Stacking, ANN, RNN, LSTM, Linear_Regression  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, MAE, MSE  
**Data**: Boulder_Colorado  
**Features**: Historical_Load, Arrival_Departure_Time, Charging_Duration, Energy_Consumption, Hourly_Aggregated_Load

- **What they did:**
  - Proposes a novel **ensemble learning-based forecasting model** for EV charging station load, combining three base learners — ANN, RNN, and LSTM — via **weighted averaging**, where the weights are learned by a Linear_Regression (LR) meta-learner.
  - Motivation: most prior work uses only one ML model per forecaster; ensemble learning was not well studied for EV charging load forecasting. The forecast serves as a reference for grid energy dispatching and mitigates peak/valley fluctuations from disordered charging.
  - Demonstrated on a real-world dataset with comparisons against 4 baselines (LR, ANN, RNN, LSTM).
- **Method core:** where $a_j^l$ is the output of the $j$-th node in layer $l$, $\sigma_j^l$ the activation function (ReLU), $\omega_{ij}$ and $b_j^l$ weight and bias. Architecture: 1 input layer, 3 hidden layers, 1 output layer.
- **Key results:**
  - Metrics: RMSE $= \sqrt{\frac{1}{N}\sum_{i=1}^{N}(y_i^p - y_i)^2}$ and MAE $= \frac{1}{N}\sum_{i=1}^{N}|y_i^p - y_i|$ (Eq. 10 and Eq. 9).
  - Test set results, look-back = 24:
  - Ensemble improves RMSE accuracy by **1.79%, 0.26%, 1.83%, 1.57%** vs LR, ANN, RNN, LSTM respectively; MAE improvements of **5.79%, 2.48%, 0.83%** vs LR, ANN, RNN, tied with LSTM (2.42).
- **Gaps/Limitations:**
  - Authors explicitly note: **only limited data is used** and only **one-step-ahead forecasting** is considered; future work targets wider-range data and multi-step forecasting methods.
  - No calendar/weather covariates beyond historical load; single-station aggregation level (all Boulder city stations pooled).
  - Modest gains (~1–2% RMSE over best base learner) suggest headroom via richer ensembling or probabilistic outputs.

### 2020_NBEATS_Interpretable_Time_Series_Forecasting
**N-BEATS: Neural Basis Expansion Analysis for Interpretable Time Series Forecasting**  
Oreshkin et al. · ICLR 2020 · 2020
<https://arxiv.org/abs/1905.10437>
**Models**: NBEATS, NBEATS-G, NBEATS-I  
**Horizon**: Long_Term_Forecasting  
**Metrics**: sMAPE, MAPE, MASE, OWA, ND  
**Data**: M4; M3; Tourism; Electricity_ECL; Traffic  
**Features**: Lookback_Window, Learned_Basis, Polynomial_Trend_Basis, Fourier_Seasonality_Basis

- **What they did:**
  - Pure deep learning architecture for **univariate point forecasting**: deep stack of fully connected layers with **backward (backcast) and forward (forecast) residual links** — no time-series-specific components, no feature engineering, no input scaling.
  - First empirical proof that pure DL outperforms well-established statistical approaches on M4, M3, and Tourism: on M4 by **11% over the statistical benchmark**, 7% over the best statistical entry, and **3% over the M4 competition winner** (Smyl's DL/TS hybrid).
  - Second contribution: an **interpretable configuration** whose outputs decompose into human-readable trend and seasonality components (like STL / X-13ARIMA) with negligible accuracy loss.
- **Method core:** Architecture: trend stack followed by seasonality stack, 3 residual blocks each, basis functions shared per stack, all weights shared within stack (best validation performance). Trend is removed from the input before the seasonality stack sees it. — Ensemble diversity via: 3 losses (sMAPE, MASE, MAPE; MAPE-only for TOURISM), 6 lookback window lengths ($2H,\dots,7H$), and bagging over random initializations — **180 models**, median aggregation. Ensembling proved a stronger regularizer than dropout or L2. Trained in TensorFlow with Adam (lr = 0.001), batch size 1024, early stopping; gradient flow stopped through sMAPE …
- **Key results:**
  - **M4 (100k series)**: N-BEATS-I+G sMAPE **11.135**, OWA **0.795** vs M4 winner DL/TS hybrid 11.374/0.821, best ML/TS combination (FFORMA) 11.720/0.838, best statistical 11.986/0.861, best pure ML 12.894/0.915. N-BEATS-G alone: 11.168/0.797. Statistically significant improvement over Smyl in 18/31 frequency×type …
  - **M3**: average sMAPE **12.37** (I+G) vs EXP 12.71 (prior SOTA), DOTM 12.90, Theta 13.01, ARIMA 14.01.
  - **TOURISM**: average MAPE **18.47** (G) vs LeeCBaker 19.35, Stratometrics 19.52, Theta/ETS 20.88 → gains of **4.2% over best-known** and 11.5% over auto-ARIMA.
- **Gaps/Limitations:**
  - Univariate **point** forecasting only — no native probabilistic distributions/uncertainty quantification.
  - Generic-model basis waveforms lack inherent structure (non-interpretable); interpretability requires hand-imposed inductive bias.
  - No exogenous covariates supported in main experiments; meta-learning connection speculative ("should be the subject of future work").
  - Ensemble of 180 models is computationally heavy for deployment, though results degrade <0.5% with 18 models.
  - Reproducibility concerns raised about other works' split points (esp. TRAFFIC date reconstruction required heuristics).

### 2019_ApplSci_EV_Load_Forecasting
**Short-Term Load Forecasting for Electric Vehicle Charging Stations Based on Deep Learning Approaches**  
Zhu et al. · Applied Sciences 2019, 9(9), 1723 (MDPI) · 2019
<https://doi.org/10.3390/app9091723>
**Models**: ANN, RNN, LSTM, GRU  
**Horizon**: Short_Term_Forecasting  
**Metrics**: NRMSE, NMAE, MSE  
**Data**: Liuyue_Charging_Station_Dataset  
**Features**: Historical_Load, Charging_Duration, Real-Time Electricity Price (TOU), One-Hot Encoded Holiday Marks

- **What they did:**
  - Applies and compares four deep learning models — ANN, RNN, LSTM, GRU — for **hourly-based short-term (1 hour to 1 day/week ahead) EV charging station load forecasting** on real-world Shenzhen charging station data.
  - Incorporates multi-dimensional contextual inputs beyond historical load: charging time sequence, real-time peak/valley electricity price, one-hot encoded holiday marks.
  - Key finding: the **single-hidden-layer GRU achieves the best accuracy** (Test-NRMSE 2.89%, Test-NMAE 0.77%) with fewer parameters than LSTM; adding hidden layers degrades accuracy and training speed.
  - Companion minute-level study: 2019_EV_Load_Forecasting.
- **Method core:** **Vanilla RNN** (Eqs. 1–4):  S_t = \phi(U x_t + W S_{t-1} + b_1),\qquad o_t = \phi(V S_t + b_2),\qquad \hat{y}_t = \phi(o_t),\qquad \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} 
- **Key results:**
  - Best model overall: **1-hidden-layer GRU** (Train-NRMSE 1.48%, Test-NRMSE 2.89%, Train-NMAE 0.47%, Test-NMAE 0.77%).
  - **Depth counter-intuition**: multi-hidden-layer models performed worst — more layers without tuning other parameters lowered both training speed and accuracy (over-fitting); DNN trained fastest at 68.88 s but least accurate.
  - Peak loads (17:00 training stage, 11:00 test stage) have largest real error points (REP) for all models; GRU keeps lowest REP at peaks.
- **Gaps/Limitations:**
  - Only a single charging station's limited data used; number of covered EVs is a small fraction of actual vehicle population → results cannot prove absolute superiority of any model.
  - Point forecasts only (no probabilistic output); no weather/spatial covariates; peak-hour errors remain large for all four models.
  - Authors' future work: incorporate more influencing factors and larger datasets as EV adoption grows; improve both prediction speed and accuracy; new models needed.
  - Thesis relevance: validates GRU > LSTM at hourly resolution and the importance of TOU price + holiday features for day-ahead EV forecasting.

### 2019_Deep_Probabilistic_Scheduling_Power_Markets
**Deep Learning-Based Multivariate Probabilistic Forecasting for Short-Term Scheduling in Power Markets**  
Toubeau et al. · IEEE Transactions on Power Systems, Vol. 34, No. 2 (March 2019), pp. 1203-1215 · 2019
<https://doi.org/10.1109/TPWRS.2018.2870041>
**Models**: Bidirectional LSTM (BLSTM), LSTM, MLP, ARIMA, SVR, RF, Empirical_Copula  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: RMSE, Quantile (Pinball) Loss, Autocorrelation Function Deviation, Pearson_Correlation, Spearman_Correlation  
**Data**: ELIA_Belgian_Grid; NWP_Belgium  
**Features**: Electricity_Load, Wind_Power, Solar_Power, Day-Ahead Electricity Price, NWP: temperature, wind speed, cloud cover, solar radiation, Mutually exclusive binary hour/day/month + holiday index, Lag_Features

- **What they did:**
  - Generates **short-term multivariate probabilistic forecasts and predictive scenarios** for day-ahead operational scheduling of electricity aggregators/VPPs in power markets (predictions issued daily at 12:00 for hours m = 12–36 ahead).
  - Four contributions: 1. Tailored architectural variations exploiting the structure of day-ahead planning: **bidirectional LSTM (BiLSTM)** since all 24 hourly predictions are needed simultaneously; bidirectional processing lowers forecast error and avoids the error accumulation of recursive unidirectional strategies. 2. Compares **two uncertainty characterizations** trained on the same BLSTM: parametric Gaussian …
- **Method core:** Implementation in Matlab; ~1 min/train MLP vs ~5 min LSTM architectures (parallelizable, done once); real-time inference < 1 s.
- **Key results:**
  - **Point forecasts (Table I, RMSE)**: ranking BLSTM < unidirectional LSTM < MLP < RF/SVR < ARIMA ≈ TSO tool; recurrent models beat the system operator's tool. Best topologies: 3-layer BLSTM for wind, load, and prices; 4-hidden-layer BLSTM for PV; optimal capacity small (10–20 neurons/layer) due to limited historical …
  - **Parametric vs non-parametric (Table III)**: non-parametric quantile regression slightly outperforms the Gaussian assumption (better-calibrated, tighter intervals across q ∈ {1..99}%); Gaussian errors acceptable especially for PV.
  - **Decision value (Fig. 9, month-long simulation)**: replacing independent sampling with copula-based scenarios in the stochastic optimization raised retailer profit by ≈ **4×10⁵ € (>10% relative increase)**; upgrading MLP → BLSTM forecasts added ≈ **0.5×10⁵ €**, avoiding overly conservative policies.
- **Gaps/Limitations:**
  - Optimal architecture is dataset-size-dependent: limited history forces shallow networks (10–20 neurons), so accuracy should grow as more data accumulates; retraining extent (how much to modify prior optimum with new data) left outside scope.
  - Data-driven models ignore structural/market constraints (acceptable for zonal European day-ahead clearing, but noted as future work to combine data-driven models with physically-based market rules).
  - Empirical copula suffers curse of dimensionality (mitigated only via hash/sparse storage, not vine copulas); scenario count/tractability trade-off remains.
  - Quantile loss kink requires numerical gradient handling; no EV-specific modeling (load is aggregate non-shiftable) — gap for thesis: applying BLSTM+copula pipelines to EV charging station probabilistic scenarios.

### 2019_EV_Load_Forecasting
**Electric Vehicle Charging Load Forecasting: A Comparative Study of Deep Learning Approaches**  
Zhu et al. · Energies 2019, 12(14), 2692 (MDPI) · 2019
<https://doi.org/10.3390/en12142692>
**Models**: ANN, RNN, LSTM, BiLSTM, GRU, SAEs  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, RMSE, R² Score  
**Data**: Shenzhen_ST_EVCDP; Shenzhen_ST_EVCDP  
**Features**: Historical_Load, Historical_Load, Rainy/Dry_Season_Indicator, Holiday_Flag, Lookback_Window

- **What they did:**
  - First study to use **real-world super-short-term (minute-level) EV charging data** (rather than simulation) for multi-time-step extra-short-term PEV charging load forecasting.
  - Proposes a **super-short-term multi-step forecasting framework** comparing six models — ANN, RNN, canonical LSTM, GRU, SAEs, BiLSTM — across three look-back time steps ($T_{\text{step}} = 1, 5, 15$ minutes).
  - Headline result: LSTM performs best, reducing forecasting error by **over 30%** on all index criteria vs. the best counterparts (and ~80% MAE reduction vs. ANN).
  - Claims univariate historical-load input suffices: deep sequence models capture nonlinear features and temporal correlations without exogenous variables.
- **Method core:** **Vanilla RNN** (Eqs. 1–3): hidden state recurrence and output mapping  S_t = \phi(U x_t + W S_{t-1} + b_1),\qquad o_t = \phi(V S_t + b_2),\qquad \hat{y}_t = \phi(o_t)  suffers from vanishing gradient with long sequences.
- **Key results:**
  - Final training losses (epoch 30): LSTM 0.0068/0.0065/0.0064 for 1/5/15 steps; validation loss 0.0031/0.0043/0.0034 — minimum among all six models at every setting.
  - **Efficiency**: Bi-LSTM needed **58 s/epoch** at 15 time steps vs. **8 s/epoch** for LSTM.
  - Sequence insight: RMSE of RNN/GRU/Bi-LSTM/LSTM decreases going 1→5 steps (sequence models prefer longer inputs); only LSTM and Bi-LSTM keep improving 5→15 steps.
- **Gaps/Limitations:**
  - MAPE unusable due to zero-load periods — motivates alternative relative-error metrics for sparse EV data.
  - Interpolation repair (Eq. 14) only effective for minor outliers; heavy sensor error requires more specific handling.
  - Univariate model ignores weather, calendar, price, and spatial context; no probabilistic/interval output; fixed shallow architecture (≤4 layers, 16 nodes) not optimized systematically.
  - Aggregator case shows degraded accuracy vs. periodic station case — highly stochastic commercial profiles remain hard.
  - Gap for thesis: minute-level point forecasts only; extension to multi-station spatio-temporal and probabilistic settings left open.

### 2019_Graph_WaveNet_Spatial_Temporal_Modeling
**Graph WaveNet for Deep Spatial-Temporal Graph Modeling**  
Wu et al. · IJCAI 2019 (28th International Joint Conference on Artificial Intelligence), pp. 1907-1913 · 2019
<https://doi.org/10.48550/arXiv.1906.00121>
**Models**: Graph_WaveNet  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, RMSE, MAPE  
**Data**: Traffic; Traffic  
**Features**: Traffic_Speed, Sensor_Time_Series, Adjacency_Matrix

- **What they did:**
  - Propose **Graph WaveNet**, a CNN-based deep spatial-temporal graph architecture that combines (i) a novel **self-adaptive adjacency matrix** learned end-to-end through node embeddings (capturing *hidden* spatial dependencies without prior knowledge, fixing cases where explicit graphs miss true dependencies) and (ii) **stacked dilated causal convolutions** whose receptive field grows exponentially with depth, …
- **Method core:** **Problem definition (Eq. 1)** — given graph $\mathcal{G}=(V,E)$, adjacency $A \in \mathbb{R}^{N\times N}$, dynamic feature matrix $X^{(t)}\in\mathbb{R}^{N\times D}$, learn $f$ mapping $S$ historical steps to $T$ future steps:  [\boldsymbol{X}^{(t-S):t}, \mathcal{G}] \xrightarrow{f} \boldsymbol{X}^{(t+1):(t+T)}  **Graph convolution layer (GCN).** *Baseline GCN (Eq. 2)* (Kipf …
- **Key results:**
  - **Main comparison (Table 2)** — Graph WaveNet best on both datasets (MAE/RMSE/MAPE): Gains over second-best GGRU grow with horizon (larger at 60 min than 15 min), attributed to separate GCN parameters per temporal stage vs shared recurrent GCN weights. **Adjacency-matrix ablation (Table 3, means over 12 horizons):** …
- **Gaps/Limitations:**
  - Future work stated by authors: scalable methods for large-scale datasets, and learning **dynamic** (time-varying) spatial dependencies — the adaptive adjacency is static once trained.
  - Evaluation limited to highway traffic speed; no probabilistic/uncertainty quantification (point forecasts only).
  - Receptive field must be artificially engineered to equal input length for one-shot multi-step output.

### 2019_LogSparse_Enhancing_Locality_Transformer
**Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting**  
Li et al. · NeurIPS 2019 (33rd Conference on Neural Information Processing Systems, Vancouver) · 2019
<https://arxiv.org/abs/1907.00235>
**Models**: LogSparse_Transformer, Convolutional_Self_Attention, Transformer, DeepAR, DeepState, TRMF, ARIMA, ETS  
**Horizon**: Short_Term_Forecasting  
**Metrics**: R0.5/R0.9 quantile loss, Negative Log-Likelihood  
**Data**: electricity-f / electricity-c; traffic-f / traffic-c; solar; Wind_Speed; M4; Synthetic_Sinusoidal  
**Features**: Historical_Load, Time_Based_Covariates, Positional_Embedding, Series_ID_Embedding, Age_Feature

- **What they did:**
  - Applies the Transformer to multivariate time series forecasting and identifies two canonical weaknesses: **(1) locality-agnosticism** — point-wise dot-product self-attention ignores local context/shape, making models prone to anomalies; **(2) memory bottleneck** — $O(L^2)$ attention space complexity blocks fine-grained long-sequence modeling.
  - Three contributions: 1. Validates Transformer's superiority over RNN-based models for long-term dependencies on synthetic + real data. 2. Proposes **convolutional self-attention**: causal convolutions (kernel $k$, stride 1) generate queries/keys so query-key matching uses local shape context; lowers training loss and improves accuracy. 3. Proposes **LogSparse_Transformer** with only $O(L(\log L)^2)$ memory, enabling …
- **Method core:** **Problem definition**: for $N$ related univariate series $\{z_{i,1:t_0}\}_{i=1}^N$ with time covariates $\{x_{i,1:t_0+\tau}\}$, model the conditional distribution:  p(z_{i,t_0+1:t_0+\tau} \mid z_{i,1:t_0},\ x_{i,1:t_0+\tau};\ \Phi) = \prod_{t=t_0+1}^{t_0+\tau} p(z_{i,t} \mid z_{i,1:t-1},\ x_{i,1:t};\ \Phi) \tag{Conditional forecasting objective}  reduced to one-step-ahead …
- **Key results:**
  - **Metric**: $\rho$-quantile loss  R_\rho(x, \hat{x}) = \frac{2\sum_{i,t} D_\rho(x_t^{(i)}, \hat{x}_t^{(i)})}{\sum_{i,t}|x_t^{(i)}|},\qquad D_\rho(x,\hat{x}) = (\rho - I\{x \le \hat{x}\})(x - \hat{x}) \tag{Quantile loss} 
  - **Synthetic (Fig. 4b)**: at $t_0=24$ both Transformer and DeepAR (3-layer LSTM baseline, hidden sizes 20→200) are accurate; for $t_0 \ge 96$ DeepAR degrades sharply while canonical Transformer keeps accuracy — LSTM cannot capture these long-term dependencies.
  - **Coarse datasets (Table 1, R0.5/R0.9)**:
- **Gaps/Limitations:**
  - Training on electricity-f/traffic-f unstable with vanilla Adam — required BERTAdam workaround.
  - With identical input lengths, full attention still mostly outperforms sparse (except strong-long-dependency traffic-f) — sparsity trades capacity for feasibility.
  - Covariate-rich easy datasets (electricity-c) leave little room for locality gains.
  - Authors' future directions: better sparsity strategies in self-attention; better fit to small datasets.
  - Thesis relevance: LogSparse attention is a direct precursor of efficient EV-charging forecasters (cf. 2021_Informer_Beyond_Efficient_Transformer); convolutional self-attention motivates locality-aware attention for minute-level charging load sequences.

### 2018_Empirical_TCN_Sequence_Modeling
**An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling**  
Bai et al. · arXiv preprint arXiv:1803.01271 (presented as a generic-architecture evaluation; CMU / … · 2018
<https://arxiv.org/abs/1803.01271>
**Models**: TCN, LSTM, GRU, RNN, EURNN, TCN+Gating  
**Horizon**: Short_Term_Forecasting  
**Metrics**: Accuracy, MSE, NLL, Perplexity, bpc  
**Data**: Adding_Problem; MNIST; MNIST; Copy_Memory; JSB_Chorales; Nottingham; Penn_Treebank; Wikitext-103; LAMBADA; text8  
**Features**: Raw_Sequence_Input, Dilation_Factor, Transformer, Weight_Normalization, Spatial_Dropout

- **What they did:**
  - The most extensive systematic comparison of **generic convolutional vs. recurrent architectures** for sequence modeling, run on RNNs' "home turf": the standard stress tests and music/language benchmarks used to evaluate LSTM/GRU variants themselves.
  - Introduces a deliberately simple generic **Temporal Convolutional Network (TCN)**: `TCN = 1D fully-convolutional network + causal convolutions`, augmented with dilated convolutions for exponentially large receptive fields and residual blocks.
  - Central findings: TCNs **convincingly outperform canonical LSTMs/GRUs across a diverse task suite**, exhibit **substantially longer effective memory** in practice (the "infinite memory" advantage of RNNs is largely absent), are simpler, parallelizable, and have stable gradients — concluding that convolutional networks should be the default starting point for sequence modeling.
  - Directly motivates TCN-based EV charging load forecasters (e.g., 2024_MQ_TCN_Transfer_Learning_EV).
- **Method core:** **Sequence modeling formalism (Equation 1):** any network $f: \mathbb{X}^{T+1} \rightarrow \mathbb{Y}^{T+1}$ producing  \hat{y}_0, \dots, \hat{y}_T = f(x_0, \dots, x_T)  subject to the **causal constraint**: $y_t$ may depend only on $x_0,\dots,x_t$, never on future inputs $x_{t+1},\dots,x_T$. Trained by minimizing expected loss $L(y_0,\dots,y_T, f(x_0,\dots,x_T))$. **Causal …
- **Key results:**
  - **Seq. MNIST accuracy**: TCN **99.0** vs GRU 96.2, LSTM 87.2, RNN 21.5. **P-MNIST**: TCN **97.2** vs GRU 87.3, LSTM 85.7 — beats recurrent SoTA (95.9%, Zoneout + Recurrent BatchNorm).
  - **Adding problem (T=600 loss)**: TCN **5.8e-5** ≈ regularized GRU 5.3e-5; LSTM fails at 0.164.
  - **Copy memory (T=1000 loss)**: TCN **3.5e-5** vs EURNN 0.011 (SoTA recurrent), LSTM 0.0204, GRU 0.0197 (both collapse to the all-zeros guess); TCN holds **100% recall accuracy at all T**, while LSTM drops below 20% accuracy for T < 50 and GRU below 20% for T < 200.
- **Gaps/Limitations:**
  - On small corpora (word PTB, JSB Chorales), specialized heavily-tuned LSTM variants still win; authors attribute this to regularization/generative tricks orthogonal to the TCN-vs-RNN axis and call for equivalent community investment in TCN tuning.
  - TCNs must retain raw history up to receptive-field length during evaluation — potentially higher inference memory than an RNN's fixed hidden state.
  - Receptive field (k, d) is domain-dependent: transferring a short-memory configuration to a long-memory domain degrades performance — precisely the gap later addressed by adaptive-receptive-field EV forecasting models (2024_MQ_TCN_Transfer_Learning_EV, multi-quantile transfer).
  - No probabilistic outputs, no covariates, no multi-horizon forecasting protocol — pure sequence-modeling benchmark; adoption for day-ahead EV load forecasting required later architectural extensions (dilated skip connections, quantile heads).

### 2018_Reptile_First_Order_Meta_Learning
**On First-Order Meta-Learning Algorithms**  
Nichol et al. · arXiv preprint (OpenAI), arXiv:1803.02999 · 2018
<https://arxiv.org/abs/1803.02999>
**Models**: Reptile, MAML, FOMAML  
**Horizon**: MAML  
**Metrics**: Accuracy  
**Data**: Omniglot; MiniImageNet; Sine_Wave_Regression  
**Features**: Task_Sampling, K-Shot_N-Way_Classification, Transductive_Batch_Normalization, Weight_Interpolation

- **What they did:**
  - **Problem**: MAML requires second-order derivatives (Hessian-vector products via differentiating through the inner-loop SGD) for its outer-loop update — computationally expensive and memory-heavy, and unsuited to problems needing many inner gradient steps.
  - **Contributions**: 1. Shows **first-order MAML (FOMAML)** is far simpler to implement than widely recognized (treat inner-loop gradients as constants → outer gradient is just $g_{\text{FOMAML}} = L'_{\tau,B}(\tilde{\phi})$). 2. Introduces **Reptile**, a new first-order algorithm closely related to FOMAML and to joint training / fast-weights-slow-weights: repeatedly sample a task, train on it for $k$ steps, move the …
- **Method core:** **Implementation details**: same CNN architectures/preprocessing as Finn et al.; Adam ($\beta_1=0$ — momentum hurts, since it lets one minibatch influence subsequent steps) inner loop, vanilla SGD outer loop; Adam moment statistics backed up/reset at evaluation.
- **Key results:**
  - **Omniglot (Table 2)**: MAML+Transd. 98.7/99.9/95.8/98.9% (1-shot 5-way / 5-shot 5-way / 1-shot 20-way / 5-shot 20-way); FOMAML+Transd. 98.3/99.2/89.4/97.9%; Reptile 95.39/98.90/88.14/96.65%; Reptile+Transd. 97.68/99.48/89.43/97.12%. Reptile slightly worse than MAML on Omniglot, slightly better on Mini-ImageNet; …
  - **Gradient-combination ablation (Sec. 6.2, 5-shot 5-way Omniglot)**: using only first gradient $g_1$ (= joint training) is ineffective; two-step Reptile ($g_1+g_2$) slightly worse than two-step FOMAML ($g_2$); performance improves monotonically as more inner minibatch gradients are summed — Reptile benefits from many …
  - **Mini-batch overlap ablation (Sec. 6.3)**: shared-tail FOMAML degrades sharply once the final minibatch overlaps earlier ones (≥5 cycling iterations or batch size >25); separate-tail FOMAML and Reptile are insensitive to inner-loop hyperparameters.
- **Gaps/Limitations:**
  - Taylor approximation valid only for small $\alpha k$; theory informal in parts (solution-manifold argument explicitly "should be taken much less seriously").
  - Negative results applying Reptile to RL so far (joint training is a strong baseline there).
  - Large gap between training and testing error in few-shot classification; regularization unexplored.
  - Open questions posed by authors: whether SGD's automatic generalization effect can be amplified outside meta-learning; deeper classifier architectures; few-shot density modeling.
  - Thesis relevance: first-order adaptation (no Hessians) is attractive for quickly adapting EV charging forecasters to new stations/sites with scarce history — but this paper validates only on vision benchmarks, not time series.

### 2017_Attention_Is_All_You_Need
**Attention Is All You Need**  
Vaswani et al. · Advances in Neural Information Processing Systems 30 (NIPS 2017), Long Beach, CA · 2017
<https://arxiv.org/abs/1706.03762>
**Models**: Transformer, Multi_Head_Attention, Multi_Head_Attention, ByteNet, ConvS2S  
**Horizon**: Short_Term_Forecasting  
**Metrics**: BLEU, Perplexity, F1_Score  
**Data**: WMT_2014_EN-DE; WMT_2014_EN-FR; WSJ_Penn_Treebank; BerkleyParser_Corpus  
**Features**: Token_Embeddings, Sinusoidal_Positional_Encoding, Byte_Pair_Encoding

- **What they did:**
  - Introduces the **Transformer**: the first sequence transduction model relying **entirely on self-attention**, dispensing with recurrence (LSTM, GRU) and convolutions entirely.
  - Removes the inherent sequential bottleneck of RNNs (hidden state $h_t$ as a function of $h_{t-1}$), enabling full parallelization within training examples — training to SOTA in as little as 12 hours on 8 P100 GPUs.
  - Reduces path length between any two positions to $O(1)$ (vs $O(n)$ recurrent, $O(\log_k(n))$ dilated convolutional) at per-layer complexity $O(n^2 \cdot d)$, counteracting attention averaging with multi-head attention.
  - Establishes new single-model state-of-the-art on WMT 2014 EN→DE and EN→FR and generalizes to English constituency parsing; the architectural foundation for all subsequent forecasting transformers (Informer, Autoformer, PatchTST, Temporal_Fusion_Transformer).
- **Method core:** **Overall structure:** encoder-decoder. Encoder maps $(x_1,...,x_n)$ to continuous representations $z=(z_1,...,z_n)$; auto-regressive decoder emits $(y_1,...,y_m)$ one element at a time. Both are stacks of $N=6$ identical layers with residual connections + layer normalization: output of each sub-layer is $\text{LayerNorm}(x + \text{Sublayer}(x))$, all outputs dimension …
- **Key results:**
  - **EN→DE (newstest2014): Transformer (big) 28.4 BLEU**, beating the best prior result *including ensembles* by >2 BLEU (GNMT+RL ensemble 26.30, ConvS2S ensemble 26.36). Base model already 27.3.
  - **EN→FR: Transformer (big) 41.8 BLEU** vs GNMT+RL ensemble 41.16, ConvS2S ensemble 41.29, at 2.3×10¹⁹ FLOPs (< 1/4 of competitors' training cost).
  - Ablations (newstest2013 dev): single head −0.9 BLEU vs h=8; too many heads also hurts; reducing $d_k$ hurts quality; bigger models help (d_model=1024/d_ff=4096 → PPL 4.66, BLEU 26.0); dropout essential (P_drop 0.0 → PPL 5.77); sinusoidal ≈ learned positional embeddings (4.92 PPL both).
- **Gaps/Limitations:**
  - Self-attention cost is quadratic $O(n^2 \cdot d)$ in sequence length; authors propose restricted neighborhood self-attention of size $r$ (path length $O(n/r)$) as future work — later realized by Informer/sparse attention for long EV load windows.
  - Attention averaging reduces effective resolution; multi-head attention is the mitigation but raises parameter/compute cost.
  - Generation remains sequential/auto-regressive at inference; authors list making generation less sequential and extension to image/audio/video modalities as open goals.
  - Not a time-series or load-forecasting paper: no exogenous covariates, probabilistic outputs, or calendar features — adaptation to load forecasting required later work (decomposition, frequency encodings, quantile heads).

### 2017_MAML_Model_Agnostic_Meta_Learning
**Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks**  
Finn et al. · Proceedings of the 34th International Conference on Machine Learning (ICML 2017), Sydney, … · 2017
<https://arxiv.org/abs/1703.03400>
**Models**: MAML, FOMAML, MLP, CNN, TRPO, REINFORCE  
**Horizon**: Short_Term_Forecasting  
**Metrics**: Accuracy, MSE, Average_Return  
**Data**: Sinusoid_Regression; Omniglot; miniImageNet; rllab_2D_Navigation; MuJoCo_Half_Cheetah; MuJoCo_Ant  
**Features**: Task_Distribution, K_Shot_Support_Set, Meta_Gradient, Hessian_Vector_Products

- **What they did:**
  - Proposes **MAML**, a model- and task-agnostic meta-learning algorithm that trains an initialization $\theta$ such that **one or a few gradient steps on a new task's data yields maximal generalization** — in effect "training the model to be easy to fine-tune."
  - Unlike prior meta-learners (learned update rules, recurrent MANN, Siamese/matching/metric networks), MAML adds **no extra learned parameters** and imposes **no architectural constraints**: works with fully connected, convolutional, or recurrent networks and any differentiable loss, including non-differentiable RL objectives.
  - Interpretable two ways: (a) feature learning — building a representation broadly suitable for many tasks so light fine-tuning suffices; (b) dynamical systems — explicitly maximizing the sensitivity of new-task losses to the parameters.
  - State-of-the-art on few-shot image classification benchmarks, strong few-shot regression, and accelerated policy-gradient RL adaptation; foundational for transfer/meta-learning approaches to EV charging station forecasting with scarce data.
- **Method core:** **Architectures used:** sinusoid regressor = 2 hidden layers × 40 ReLU units; classifier = 4 conv modules (3×3, 64 filters, BN, ReLU, 2×2 max-pool; 32 filters on miniImageNet; strided convs on Omniglot) plus a non-conv 4-hidden-layer net (256-128-64-64); RL policy = 2 hidden layers × 100 ReLU units.
- **Key results:**
  - **Omniglot 5-way**: 98.7 ± 0.4% (1-shot), 99.9 ± 0.1% (5-shot); 20-way: 95.8 ± 0.3% / 98.9 ± 0.2% — beats matching nets (98.1/98.9; 93.8/98.5), memory module (98.4/99.6; 95.0/98.6), Siamese nets, and non-conv MAML beats non-conv MANN (89.7 vs 82.8% 1-shot).
  - **miniImageNet 5-way**: 48.70 ± 1.84% (1-shot) and 63.11 ± 0.92% (5-shot) vs matching nets 43.56/55.31, meta-learner LSTM 43.44/60.60, nearest-neighbor 41.08/51.04, fine-tuning baseline 28.86/49.79. First-order approximation essentially ties full MAML (48.07 ± 1.75% / 63.15 ± 0.91%).
  - **Sinusoid regression (5-shot MSE)**: MAML 0.67 after 1 gradient step → 0.35 after 10, vs pretrain-on-all-tasks 2.41→2.19, multi-task parameter averaging 2.91→2.71 (reg-to-mean variant), showing MAML learns more than the mean optimal parameter vector; MAML infers amplitude/phase from one half of the input range and …
- **Gaps/Limitations:**
  - Meta-gradient requires differentiating through the inner gradient update (second-order information); although the first-order surrogate works surprisingly well (ReLU networks are locally almost linear), the authors leave principled analysis open — later formalized by Reptile-style methods 2018_Reptile_First_Order_Meta_Learning.
  - On-policy RL adaptation requires fresh trajectory samples for every additional inner-loop gradient step.
  - Performance depends on the choice of task distribution $p(\mathcal{T})$; no mechanism proposed for task-distribution shift.
  - Not applied to time series/load forecasting: extension to probabilistic EV charging demand forecasting (e.g., 2023_MetaProbformer_EV_Load, 2026_Decomposition_Stacked_Meta_Learning_EV_Load, 2024_MQ_TCN_Transfer_Learning_EV) is left as future work by successor literature.

### 2017_QRA_Sister_Forecasts_Probabilistic_Load
**Probabilistic Load Forecasting via Quantile Regression Averaging on Sister Forecasts**  
Liu et al. · IEEE Transactions on Smart Grid, vol. 8, no. 2, pp. 730-737 · 2017
<https://doi.org/10.1109/TSG.2015.2437877>
**Models**: QRA, Quantile_Regression, Recency_Effect_Regression, Taos_Vanilla_Benchmark  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: Pinball_Loss, Winkler_Score, MAE  
**Data**: GEFCom2014  
**Features**: Sister_Point_Forecasts, Temperature, Calendar_Features, Calendar_Features, Calendar_Features, Temperature, Temperature

- **What they did:**
  - First formal study of **forecast-combination-based probabilistic load forecasting**: applies **Quantile Regression Averaging (QRA)** — previously used only for electricity *price* forecasting and by a top GEFCom2014 price-track entry — to a set of **sister point forecasts** to produce prediction intervals (PIs).
  - **Sister forecasts** = point forecasts from the same family of models ("sister models") differing only in variable-selection choices (training-set length 2 vs. 3 years, calibration/partition scheme, number of lagged temperature terms). Much easier to generate than independent expert forecasts and transparent to manage.
  - Practical value: QRA leverages decades of point load forecasting literature as direct input (no need for high-quality expert forecasts), and the case study uses fully public data so results are reproducible.
  - Dominantly outperforms two naïve benchmarks and nine advanced empirical benchmarks on both the pinball loss function and Winkler scores.
- **Method core:** Two-step methodology: (1) generate sister point forecasts, (2) run quantile regression on them. **Step 1 — Sister models.** Base model is Tao's Vanilla benchmark (Equation 1):  \hat{y} = \beta_0 + \beta_1 M_t + \beta_2 W_t + \beta_3 H_t + \beta_4 W_t H_t + f(T_t) \tag{1}  with piecewise temperature response (Equation 2):  f(T_t) = \beta_5 T_t + \beta_6 T_t^2 + \beta_7 T_t^3 …
- **Key results:**
  - **Validation period (2010)**: for every one of the three scores (pinball, 50% Winkler, 90% Winkler) and every window length, the **worst QRA model still beat the best individual sister model and the BI model** — dominance across all configurations.
  - Selected pairs: pinball → QRA(8) with 183-day calibration, i.e., $(S,L)=(8,183)$ vs. Ind(1,91) and BI(–,365).
  - **Test period (2011)**: QRA(8,183) PIs are consistently narrower than individual-model PIs at similar coverage (90% PI shown for winter/summer weeks); QRA is dominantly better than **all eleven benchmarks** (Vanilla, Direct, nine residual-based advanced benchmarks) on all three scores.
- **Gaps/Limitations:**
  - Linear QRA weights must be re-estimated in a rolling scheme; performance relies on calibration windows that track non-stationary forecast-error distributions.
  - Ex-post evaluation uses actual observed temperatures rather than operational temperature forecasts (gap shrinks only as horizon grows).
  - Extensions proposed by authors: apply QRA to independent expert forecasts; generate sister forecasts from other techniques (ANN, SVM, fuzzy regression, holiday-effect models); extend beyond short-term to long-term point forecasts; optimize sister generation and (S,L) selection on **daily peak** errors instead of all-hours scores.
  - Future-work direction relevant to this vault: probabilistic forecasting of renewable generation and EV charging demand via QRA-style combination (cf. 2025_QR_LSTM_Attention_EV_Load).

### 2015_Review_AI_Load_Demand
**A review on artificial intelligence based load demand forecasting techniques for smart grid and buildings**  
Raza et al. · Renewable and Sustainable Energy Reviews, vol. 50, pp. 1352-1372 · 2015
<https://doi.org/10.1016/j.rser.2015.04.065>
**Models**: ANN, MLP, ANN, Fuzzy_Logic, ANFIS, SVM, SVR, WNN, AIS, GA, PSO, ACO  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAPE, RMSE, MAE, MSE  
**Data**: ISO_New_England_Grid; California_Grid; New_York_Grid; Singapore_Grid; ELIA_Belgian_Grid; Ontario_Grid; Victoria_Australia_Grid; UK_National_Grid  
**Features**: Historical_Load, Temperature, Dew_Point, Temperature, Humidity, Calendar_Features, Calendar_Features, Holiday_Flag, Electricity_Tariff

- **What they did:**
  - Comprehensive, systematic literature review of **AI-based short-term load forecasting (STLF)** techniques for smart grids and smart buildings (RSER 2015; ~1,760+ citations).
  - Classifies STLF techniques into **parametric/statistical** (time series, linear regression, ARMA/ARIMA, general exponential smoothing) vs. **non-parametric/AI** (ANN, fuzzy logic, SVM), then surveys six families of **hybrid ANN** techniques.
  - Key thesis: ANN forecast accuracy is governed by network architecture, input combination, activation function, training algorithm, and exogenous variables; hybrid/population-based training consistently outperforms plain gradient-descent backpropagation.
  - Establishes a taxonomy of load forecasting horizons: long-term (1–10 yr), medium-term (1 month–1 yr), short-term (1 h to 1 week ahead); STLF dominates the literature due to unit commitment, spinning reserve, and contract evaluation applications.
- **Method core:** **Architecture taxonomy:** feedforward vs. feedback (recurrent) networks; supervised vs. unsupervised learning; MLP with hidden layers as the workhorse for STLF. Documented BP pathologies: local minima, network paralysis, temporal instability, poor generalization/overfitting. Also describes a 3-level microgrid control hierarchy (primary/secondary/tertiary per IEC/ISO 62264).
- **Key results:**
  - Representative quantitative findings compiled across ~60 surveyed studies:
  - Hooshmand et al. WT+ANN+ANFIS hybrid (24 h horizon): **MAPE 1.703%**.
  - LOFY expert system: MAPE 1.86% (daily), 1.64% (ordinary days), 2.0% (weekdays).
- **Gaps/Limitations:**
  - Backpropagation-trained ANNs suffer dependence on initial weights, slow convergence, high computational cost, local minima, and weak generalization.
  - Statistical/time-series methods degrade sharply under abrupt weather or calendar changes.
  - Identified gaps: richer meteorological inputs (humidity, wind, rainfall, body index); heuristic/evolutionary hybrid training; automated optimization of architecture and transfer function selection; electricity price as an exogenous input; dynamic fuzzy-driven input selection per horizon; integration into smart-grid/building demand-side management. Notes power systems contribute ~32% of total CO₂ emissions, …
  - Pre-dates deep learning and EV-specific forecasting entirely — no sequence models, probabilistic outputs, or charging-station studies.

### 2014_Kingma_Adam_Optimization
**Adam: A Method for Stochastic Optimization**  
Kingma et al. · ICLR 2015 (arXiv:1412.6980) · 2014
<https://arxiv.org/abs/1412.6980>
**Models**: Adam, Adam, SGD, AdaGrad, RMSProp, Adam, SFO_Optimizer  
**Horizon**: Short_Term_Forecasting  
**Metrics**: NLL, Regret_Bound, Convergence_Iterations, Wall_Clock_Time  
**Data**: MNIST; CIFAR-10; IMDB_Movie_Reviews; Synthetic_VAE_Objective  
**Features**: Adam, Adam, Adam, Signal_to_Noise_Ratio, Dropout_Noise, Bag_of_Words_Features

- **What they did:**
  - Introduces **Adam (Adaptive Moment Estimation)**, a first-order gradient-based stochastic optimization algorithm that computes **individual adaptive learning rates** from estimates of the first and second moments of the gradients.
  - Combines the advantages of **AdaGrad** (works well with sparse gradients) and **RMSProp** (works well in online/non-stationary settings), adding a novel **initialization bias-correction** term.
  - Key properties: parameter-update magnitudes **invariant to diagonal rescaling of gradients**; stepsizes approximately bounded by the stepsize hyperparameter α ("trust region"); no stationary objective required; handles noisy/sparse gradients; natural step-size annealing via the signal-to-noise ratio.
  - Provides an $O(\sqrt{T})$ regret bound under the online convex optimization framework — comparable to the best known results — plus the **AdaMax** variant based on the infinity norm.
- **Method core:** Objective: minimize $\mathbb{E}[f(\theta)]$ for stochastic differentiable $f$; gradient $\mathbf{g}_t = \nabla_\theta f_t(\theta_{t-1})$.
- **Key results:**
  - **Multi-layer NNs (MNIST)**: vs. quasi-Newton SFO, Adam makes faster progress per iteration AND wall-clock time; SFO is **5–10× slower per iteration** (curvature updates) with memory linear in #minibatches; SFO fails to converge entirely with dropout noise, while Adam shows best convergence among …
  - **CNNs (CIFAR-10)**: rapid early progress; Adam and SGD eventually converge considerably faster than AdaGrad; second-moment estimate $\hat v_t$ vanishes toward zero after a few epochs (dominated by ε) so CNN speedup comes mainly from first-moment minibatch-variance reduction; Adam adapts per-layer learning-rate scale …
  - **Bias-correction ablation (VAE)**: without bias correction (= momentum-RMSProp), β₂ close to 1 causes instabilities especially in early epochs and late training when gradients grow sparse; with bias correction, small $(1-\beta_2)$ values perform best; Adam ≥ RMSProp across ALL tested hyper-parameter settings.
- **Gaps/Limitations:**
  - Theoretical regret guarantee applies only to **convex** objectives; deep-learning experiments are non-convex and purely empirical.
  - In CNNs the second-moment estimate becomes a poor approximation of cost-function geometry (collapses to ε-dominated values) — adaptive geometry less effective for weight-shared architectures.
  - Adam requires learning-rate decay schedules ($\alpha/\sqrt t$) and exponentially decayed β₁ₜ for the strongest theoretical guarantees — practical training usually omits these; decaying β₁ₜ toward zero is noted as important (matches Sutskever et al. momentum-reduction findings).
  - Memory overhead: stores two moment vectors per parameter (vs. one for plain SGD) — relevant for memory-constrained GPU settings (contrast SFO's linear-in-minibatches memory).
  - Later research gaps (not in paper): generalization gap vs. SGD on image tasks, AdamW-style decoupled weight decay, and warm-up schedules — all post-hoc fixes beyond this paper's scope.

### 2014_Scalable_Stochastic_EV_Demand
**A Scalable Stochastic Model for the Electricity Demand of Electric and Plug-In Hybrid Vehicles**  
Alizadeh et al. · IEEE Transactions on Smart Grid, 5(2), 848-860 · 2014
<https://doi.org/10.1109/TSG.2013.2275988>
**Models**: Queuing_Model, Queuing_Model, Factor_Model, ARIMA, Kalman_Filter, EM_Algorithm, ARIMA, Persistence_Model  
**Horizon**: Short_Term_Forecasting  
**Metrics**: MAE, Absolute_Error_kW, Kolmogorov_Smirnov_Test, Log_Likelihood  
**Data**: UC_Davis_PH_EV_Center_Data; NHTS_2009  
**Features**: EV_Arrival_Rate, Charging_Duration, Charging_Power, Laxity_Slack_Time, EV_Arrival_Rate, Daily_Mileage, Calendar_Features, Submetering_Triplets

- **What they did:**
  - Proposes a **queueing-theoretic stochastic model** (M/G/∞ queueing model) for aggregate EV/PHEV charging demand that yields: (1) more accurate **short-term forecasts with uncertainty** when real-time sub-metering data is available; (2) a mathematical description of load **plus demand flexibility** at wholesale level, useful for Demand_Response and dynamic pricing design.
  - Answers four essential behavioral questions from real data: when vehicles arrive at chargers, how often parked customers request charge, energy required per charge event, and flexibility (laxity) per request.
  - Adds **scalability**: quantized ("digital") sub-metering classifies each charge request into $L\times K$ service classes so only class counts per epoch need storage/communication, independent of vehicle-population size.
  - Validates statistics on real PHEV home-charging data and shows the resulting forecasting method beats classical univariate load prediction.
- **Method core:** $L$ parallel $M_t/G_t/\infty$ service systems (one per charging rate $r$, e.g., 1.1 kW level-1, 3.3/6.6 kW level-2); arrivals are **non-homogeneous Poisson processes** with time-varying rate $\lambda^{(r)}(t)$; service times (charge durations) i.i.d. with CDF $F^{(r)}(t,\tau)$; no queue ever forms.
- **Key results:**
  - **Fitted statistics**: charge duration best fit by a **clipped lognormal distribution (Eq. 20)** with expected value **207 minutes** (clip at 320 min improves q-q fit); laxity bimodal — daytime requests: **exponential, mean 1.089 (hours)**; nighttime: lognormal; duration and laxity acknowledged correlated but joint …
  - **Plug-in behavior**: with mileage-dependent plug-in probability (Eq. 23), a two-sample Kolmogorov–Smirnov test does **not reject** (5% significance) that the 620 real samples and 150,000 NHTS-derived charges share one distribution; constant-probability alternative (geometric $D$, Eq. 24) fitted by maximizing …
  - **Poisson validation**: conditional-uniformity (Barnard/Lewis) tests via one-sample KS on normalized arrival times per half-hour interval — null hypothesis never rejected (e.g., Monday 13:30–14:00 q-q plot uniform).
- **Gaps/Limitations:**
  - Model valid only for **large populations** (rate-function assumption breaks at single-feeder/few-house scale); suitable for substations and charging stations, not individual dwellings.
  - No **geographical/spatial information** (grid topology, transformer limits, location-based CO₂ accounting) — explicitly deferred to future work.
  - Arrival statistics could not be learned from the small (620-sample) real dataset — NHTS mapping needed; NHTS entries cover only one travel day per household and cannot encode expectation-of-next-day-travel charging decisions; ICEV-derived behavior may diverge further as EV adoption changes household activity/travel patterns.
  - Charge-duration PDF treated stationary though real data suggest non-stationarity (night vs. day); tapering charging power ignored (constant average rate assumed); serial correlation of daily mileage ignored.
  - V2G discharge scheduling within the queuing framework sketched but left open; aggregator control functions $\beta$ must be learned from historical data.
  - Authors stress all parameter estimates should be re-evaluated as larger multi-day EV datasets emerge — the gap later filled by data-driven deep-learning forecasters.

### 2013_Gaussian_Processes_Time_Series
**Gaussian processes for time-series modelling**  
Roberts et al. · Philosophical Transactions of the Royal Society A, 371, 20110550 · 2013
<https://doi.org/10.1098/rsta.2011.0550>
**Models**: Gaussian_Process, Bayesian_Nonparametric_Regression, Kalman_Filter, Bayesian_Quadrature, Markov_Chain_Monte_Carlo  
**Horizon**: Short_Term_Forecasting  
**Metrics**: RMSE, NRMSE, Log_Marginal_Likelihood  
**Data**: Bramblemet_Sensor_Network; Nile_River_Water_Levels; Dow_Jones_1972_1975; HD_189733_Photometry  
**Features**: Covariance_Function, Squared_Exponential_Kernel, Rational_Quadratic_Kernel, Matern_Kernel, Periodic_Kernel, Changepoint_Kernel, Mean_Function, Hyperparameters

- **What they did:**
  - Tutorial/review presenting **Bayesian non-parametric Gaussian_Process (GP) modelling** as a principled framework for time-series analysis, forecasting under uncertainty, interpolation AND extrapolation in continuous time.
  - Shows how **domain knowledge enters through covariance/mean function design**: kernels for periodicity, delays, noise, long-term drift, quasi-periodicity, changepoints, sensor faults; sums/products of valid kernels are valid kernels.
  - Demonstrates **multi-output GPs** with cross-series correlations (spherical decomposition over series labels), **active data selection** (uncertainty-driven sampling), sequential/changepoint prediction, and **Bayesian quadrature** for hyperparameter marginalization.
  - Foundation reference for probabilistic load forecasting lines later used in EV charging demand (Gaussian_Process → deep GP / robust GP forecasting).
- **Method core:** Regression setting: $y(x) = f(x) + \eta$ with additive noise; inference targets $p(y^*|x^*)$. A set of function values at locations $\mathbf{x}$ is a multivariate Gaussian (**GP prior**):  p(y(\mathbf{x})) = \mathcal{N}(\boldsymbol{\mu}(\mathbf{x}), K(\mathbf{x},\mathbf{x})) \quad \text{(Eq. 3.2)}  with covariance matrix built element-wise from a kernel $k(x_i,x_j)$ …
- **Key results:**
  - **Bramblemet tide-height (5-day test, Table 1)**: naive persistence RMSE $7.5\times10^{-1}$ m (−2.1 dB NMSE); Kalman filter (best history length 16) $1.7\times10^{-1}$ m (−15.2 dB); independent per-sensor GPs $8.7\times10^{-2}$ m (−20.3 dB); **multi-output GP $3.8\times10^{-2}$ m (−27.6 dB)** — ~4.5× better than …
  - Learned structure: tide period $T\approx$ half a day; disturbance Matérn ($\nu=5/2$) time scale ≈ 2.5 h; all four sensors inferred near-perfectly correlated (spherical decomposition ≈ 1); inter-sensor tidal delays ≈ 10 min (Cambermet/Chimet lag Bramblemet/Sotonmet, consistent with west→east high-tide timing); weather …
  - **Active selection**: keeping tide uncertainty below 10 cm needed only **119 observations** (multi-output) vs. **358** (independent GPs); GP preferentially samples undelayed Sotonmet/Bramblemet yet Chimet predictions remain accurate.
- **Gaps/Limitations:**
  - Computational cost dominated by covariance-matrix inversion, scaling as $O(n^3)$ with retained samples → motivates sparse/inducing-point approximations and adaptive sample retention.
  - Kernel/mean choice is subjective-looking; paper argues domain knowledge mitigates this, but automated kernel composition/search is left open.
  - Maximum-likelihood hyperparameter fits ignore integrand width ("potentially problematic"); full Bayesian marginalization is expensive — Bayesian quadrature itself needs tractable sub-fits.
  - Algorithmic rather than theoretical hurdles (implementation) explicitly not covered due to space.
  - Future directions flagged: latent force models coupling GPs with differential equations, GPs inside larger probabilistic models, numerical integration, mixture-of-experts, unsupervised learning — relevant gaps for scalable probabilistic EV-load forecasting.

### 2001_Neural_Networks_STLF_Review
**Neural Networks for Short-Term Load Forecasting: A Review and Evaluation**  
Hippert et al. · IEEE Transactions on Power Systems, 16(1), 44-55 · 2001
<https://doi.org/10.1109/59.912452>
**Models**: MLP, ANN, ARIMA, Linear_Regression, Kohonen_SOM, RNN, Fuzzy_Neural_Network, Projection_Pursuit_Regression, Adaline  
**Horizon**: Day_Ahead_Forecasting  
**Metrics**: MAPE, RMSE, MSPE, MAE, Standard_Deviation_Errors  
**Data**: Utility_Load_Data_1990s; Taiwan_Power_System; Greek_Power_System; Autonomous_Island_System_Crete  
**Features**: Historical_Load, Temperature, Humidity, Calendar_Features, Calendar_Features, Nonlinear_Temperature_Functions, Weather_Forecast

- **What they did:**
  - Critical review of **40 papers (1991–1999, leading EE journals only)** applying ANNs to short-term load forecasting (Short_Term_Forecasting), written to explain researcher skepticism about NN forecasting claims.
  - **Two major findings**: (a) most proposed MLPs — especially profile forecasters with 24 output nodes — were **overparameterized** (more weights than training samples → expected overfitting); (b) models were **not systematically tested** against standard benchmarks and error analysis bypassed standard forecasting practice.
  - Establishes methodological protocols still cited today: compare vs. naïve + standard statistical baselines, report in-sample AND out-of-sample errors, use multiple error metrics and error-distribution diagnostics.
  - Economic motivation quoted from Bunn & Farmer [10]: a 1% increase in forecast error implied ~£10 million/year extra operating cost (1984 estimate).
- **Method core:** **Canonical architecture reviewed**: two-layer feed-forward MLP; neuron = weighted linear sum + nondecreasing differentiable activation (logistic/identity/tanh/sinusoidal). With logistic hidden layer and linear output, the network implements the **nonlinear regression model**: — Alternative architectures surveyed: projection pursuit regression [95], frequency-domain decomposition into Adalines [71], single-neuron functional-link network (Fourier + polynomial components) [24], Kohonen SOM classification of profiles [20], [54], [84], recurrent NNs [15], [16], [86].
- **Key results:**
  - **Overparameterization evidence (Table III)**: computed parameter counts show most profile-forecasting MLPs had **more weights than training points** (hundreds–thousands of parameters vs. ≤ a few hundred profile samples); e.g., 24-output MLPs fed 24–48 lagged-load inputs run into thousands of parameters.
  - Only 10 of the 40 papers ([14], [15], [53], [55], [56], [61], [63], [66], [68], [83]) compared against standard **linear regression/ARIMA** baselines; only [23] found linear models actually beat its NNs; almost none reported naïve-persistence baselines or in-sample fits (only [52], [61]).
  - **Error reporting critique**: nearly all papers reported only MAPE (~1–4% typical claims); few reported error SD ([2], [17], [55], [70], [86]), cumulative distributions, percentiles, max errors, histograms, correlograms, or portmanteau tests; authors argue squared-error measures (RMSE, MSPE) better reflect the …
- **Gaps/Limitations:**
  - No adequate rate between #training points and #weights has been established ("how many parameters are too many" remains open).
  - Comparisons to other NNs/fuzzy engines deemed invalid baselines; ARMAX/regression fitting effort discouraged fair benchmarking — a persistent evaluation gap.
  - Treating a day as a 24-dim vector starves training sets; multi-model and iterative approaches underexplored; chaotic behavior of iterated MLP outputs noted ([19], [20]).
  - Weather-forecast uncertainty ignored in simulations (real deployment errors will be larger) — cf. [27], [75].
  - Calls for rigorous reporting standards: full error-distribution analysis, graphical diagnostics, significance of comparisons — directly relevant to modern EV-charging forecasting benchmarking practice.

### 1997_Long_Short_Term_Memory
**Long Short-Term Memory**  
Hochreiter et al. · Neural Computation, 9(8), 1735-1780 · 1997
<https://doi.org/10.1162/neco.1997.9.8.1735>
**Models**: LSTM, RNN, BPTT, RTRL, RNN, Recurrent_Cascade_Correlation  
**Horizon**: Long_Term_Forecasting  
**Metrics**: Classification_Error, MSE, Absolute_Error  
**Data**: Embedded_Reber_Grammar; Synthetic_Long_Time_Lag_Benchmarks; Adding_Problem; Multiplication_Problem; Temporal_Order_Problem  
**Features**: LSTM, LSTM, LSTM, LSTM, LSTM

- **What they did:**
  - Introduces **Long Short-Term Memory (LSTM)**, a novel recurrent architecture + gradient-based learning algorithm that overcomes the **vanishing/exploding gradient** problem of BPTT and RTRL (error signals flowing backward in time blow up or vanish exponentially depending on weight magnitudes; Hochreiter 1991 analysis).
  - Enables bridging **minimal time lags in excess of 1000 discrete-time steps**, even with noisy, incompressible input sequences, by enforcing **constant error flow** through **constant error carousels (CEC)** inside special memory cells; multiplicative **gate units** learn to open/close access to the CEC.
  - Complexity per time step and weight is $O(1)$ (update complexity $O(W)$); LSTM is **local in space and time**. Solves artificial long-time-lag tasks never solved by prior RNN algorithms; outperforms RTRL, BPTT, recurrent cascade-correlation, Elman nets, and neural sequence chunking in success rate and speed.
- **Method core:** ### LSTM architecture (Section 4)
- **Key results:**
  - **Exp. 1 (Embedded Reber)**: LSTM 100% success after 8,440–39,740 sequence presentations (best 8,440 @ lr 0.5, 276 weights); RTRL only partial success after ≥25,000; RCC 50% after 182,000; ELM >200,000. Only 2 failures out of 150 LSTM trials.
  - **Exp. 2a (delay $p=100$)**: LSTM 100% success after 5,040 presentations vs. chunker (CH) 33% after 32,400; RTRL/BPTT **0%** within 5M presentations. Task 2b (no local regularities): LSTM always successful, mean 5,680 presentations.
  - **Exp. 2c (lag 1000)**: LSTM solves all $(p,q)$ configurations (30,000–203,000 sequences; e.g., $p{=}q{=}1000$: 6064 weights, 49,000 sequences); BPTT/RTRL have no chance beyond lags ≈10 steps.
- **Gaps/Limitations:**
  - Truncated LSTM struggles with **nondecomposable tasks** (strongly delayed XOR / parity-like problems where storing single inputs doesn't reduce error incrementally); full-gradient variant increases complexity but showed no significant benefit.
  - Each memory cell block costs 2 extra gate units (≤ factor-of-9 weight increase vs. standard RNN hidden unit).
  - Like feedforward nets seeing the whole string, CEC-based LSTM behaves similarly to a BP-trained feedforward net on the full input — problematic for e.g. 500-bit parity.
  - Gradient-based methods (incl. LSTM) cannot precisely count discrete time steps (99 vs. 100 steps); needs auxiliary counting mechanisms; simple decays/counting differences (3 vs. 11) are fine.
  - Experiments are purely artificial small-scale tasks; authors explicitly propose applying LSTM to **real-world data: time-series prediction, music composition, speech processing** — the gap later filled by load/EV-demand forecasting models.
  - No forget gate, peephole connections, or bidirectionality (added by later work).

### 2014_A_Method_for_Stochastic_Optimization
**2014_A_Method_for_Stochastic_Optimization**  
????


### 2014_Adam_Stochastic_Optimization
**2014_Adam_Stochastic_Optimization**  
????


### 2019_EV_Charging_Load_Forecasting_Comparative_DL
**2019_EV_Charging_Load_Forecasting_Comparative_DL**  
????


### 2019_STLF_EVCS_Deep_Learning
**2019_STLF_EVCS_Deep_Learning**  
????


### 2021_APLF_Adaptive_Probabilistic_Load
**2021_APLF_Adaptive_Probabilistic_Load**  
????


### 2021_Day_Ahead_Forecast_EV_Demand_DNN
**2021_Day_Ahead_Forecast_EV_Demand_DNN**  
????


### 2021_Ensemble_Hierarchical_Probabilistic_EV_Load
**2021_Ensemble_Hierarchical_Probabilistic_EV_Load**  
????


### 2021_Kalman_COVID_France
**2021_Kalman_COVID_France**  
????


### 2021_Regional_Netload
**2021_Regional_Netload**  
????


### 2022_State_Space_PostCOVID
**2022_State_Space_PostCOVID**  
????


### 2023_Prediction_EV_Charging_Demand_Transformer
**2023_Prediction_EV_Charging_Demand_Transformer**  
????


### 2024_Physics_Informed_Attention_Graph_Regional_EV_Demand
**2024_Physics_Informed_Attention_Graph_Regional_EV_Demand**  
????

