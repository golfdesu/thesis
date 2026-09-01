# 📜 Research Wiki Operation Log

Append-only log recording all ingestion, synthesis, and maintenance operations.

---

## [2026-08-24] maintenance | Added gen_paper_digest.py + digest rule to AGENTS.md
- Moved the digest generator into the vault root as `gen_paper_digest.py` (vault-relative paths, auto date).
- Updated `AGENTS.md`: Step 4 now includes mandatory regeneration of `paper_digest.md` (item 13) + new section "One-File Paper Digest" defining purpose, generation rule, and no-hand-edit policy.

## [2026-08-24] synthesis | paper_digest.md (one-file AI digest)
- Generated `paper_digest.md` at vault root: a single-file digest of ALL 108 papers in `wiki/papers/`.
- Purpose: let an AI agent read ONE file and immediately know what every paper did, for fast research-gap identification.
- Each entry keeps: title / venue / year / DOI, models-horizon-metrics-data-features line, full contribution bullets ("What they did"), method-core line, key numeric results, and the complete limitations/gaps section.
- Wikilinks flattened to plain text; equations and BibTeX omitted (remain in the linked per-paper notes). Ordered newest-first with a quick-scan table + corpus snapshot at top.
- Source of truth unchanged: `wiki/papers/*.md`; regenerate by re-running the digest script if many new papers are ingested.

## [2026-08-10] maintenance | Created wiki/github/
- Created dedicated `wiki/github/` folder with repository notes (`EV_Load_Forecasting_Repos.md`, `Probabilistic_Time_Series_Repos.md`, `Time_Series_Foundation_Models_Repos.md`).
- Linked repository URLs and cross-referenced with paper summaries across the vault.
- Updated `schema.md` and `index.md` catalog.

## [2026-08-10] maintenance | Created wiki/hyperparameters/
- Created dedicated `wiki/hyperparameters/` folder with method-specific notes (`Optuna_TPE.md`, `Grid_Search.md`, `Bayesian_Optimization.md`, `Meta_Learning_Hyperparameters.md`, `Heuristic_Optimization.md`, `Manual_Empirical_Tuning.md`).
- Cross-referenced all papers in the vault using each hyperparameter optimization technique.
- Updated `schema.md` and `index.md` catalog.

## [2026-07-31] system | Init Wiki Architecture
- Initialized LLM Research Wiki structure for EV Charging Load Forecasting.

## [2026-07-31] ingest | 2017_Attention_Is_All_You_Need
- Ingested foundational Transformer paper by Vaswani et al.
- Extracted mathematical equations: Scaled Dot-Product Attention, Multi-Head Attention, Sinusoidal Positional Encoding, Warmup Learning Rate Schedule.
- Created `wiki/papers/2017_Attention_Is_All_You_Need.md` and updated `wiki/models/Transformer.md`.

## [2026-07-31] ingest | 2019_Zhu_EV_Load_Forecasting
- Ingested paper by Zhu et al. (Energies 2019).
- Extracted mathematical equations: Threshold Outlier Detection, Linear Temporal Interpolation, Min-Max Normalization, LSTM Gated Equations, MAE Loss Function, RMSE, R2 Score.
- Created `wiki/papers/2019_Zhu_EV_Load_Forecasting.md` and updated `wiki/metrics/MAE.md`.

## [2026-07-31] ingest | 2019_Zhu_ApplSci_EV_Load_Forecasting
- Ingested paper by Zhu et al. (Applied Sciences 2019).
- Extracted mathematical equations: Multi-Dimensional Feature Vectors $\vec{X}_t$, GRU Reset/Update Gate Equations, NRMSE, NMAE.
- Created `wiki/papers/2019_Zhu_ApplSci_EV_Load_Forecasting.md` and updated `wiki/models/GRU.md`.

## [2026-07-31] ingest | 2020_Huang_Ensemble_EV_Load
- Ingested paper by Huang et al. (IEEE EPEC 2020).
- Extracted mathematical equations: Ensemble Stacking Meta-Learner $\hat{y}_t = w_0 + \sum w_i P_t^i$, ANN Layer Equations, MSE Loss.
- Created `wiki/papers/2020_Huang_Ensemble_EV_Load.md` and updated `wiki/models/Ensemble_Stacking.md`.

## [2026-07-31] ingest | 2021_VanKriekinge_Day_Ahead_EV_Demand
- Ingested paper by Van Kriekinge et al. (WEVJ 2021).
- Extracted mathematical equations: Cyclical Sin/Cos Encodings ($\Delta T_{\sin/\cos}, D_{\sin/\cos}$), Average Power Conversion $P_{\text{avg}}$, Variable LR Schedule, Post-Processing rules, VIANN & LOFO Feature Importance.
- Created `wiki/papers/2021_VanKriekinge_Day_Ahead_EV_Demand.md` and updated `wiki/features/Cyclical_Encodings.md`.

## [2026-07-31] ingest | 2021_Zhang_Probabilistic_Queuing_EV_Load
- Ingested paper by Zhang et al. (IEEE TCYB 2021).
- Extracted mathematical equations: Discrete Wavelet Transform + 2D CNN, Model/Data Uncertainty Variance $\sigma_p^2$, Prediction Interval Bounds $L^\alpha, U^\alpha$, GMM EM algorithm, $M/M/C/K$ Markov Queuing Model with driver refuse/impatient probabilities ($\alpha_w, b_w$).
- Created `wiki/papers/2021_Zhang_Probabilistic_Queuing_EV_Load.md` and updated `wiki/models/CNN.md`.

## [2026-07-31] ingest | 2021_Huang_Lyapunov_EV_Scheduling
- Ingested paper by Huang et al. (2021).
- Extracted mathematical equations: Virtual Demand Queue $q_g(t)$, Virtual Delay Queue $z_g(t)$, Drift-Plus-Penalty Minimization P5', Maximum Delay Bound $D_g < O(w)$, Optimality Cost Gap $O(1/wV)$.
- Created `wiki/papers/2021_Huang_Lyapunov_EV_Scheduling.md` and updated `wiki/models/Lyapunov_Optimization.md`.

## [2026-07-31] ingest | 2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load
- Ingested paper by Dabbaghjamanesh et al. (IEEE TII 2021).
- Extracted mathematical equations: PHEV SOC & Charging Duration $t_D$, Q-learning Value Update, Exponential Error Reward Function $r_t(\lambda_i)$.
- Created `wiki/papers/2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load.md` and updated `wiki/models/Q_Learning.md`.

## [2026-07-31] ingest | 2022_Zhang_GCN_TRN_EV_Availability
- Ingested paper by Zhang & Wang (ACM CSSE 2022).
- Extracted mathematical equations: Gaussian Distance Adjacency Matrix $A_{ij}$, 1st-Order Chebyshev Graph Convolution $H^{l+1}$, Station Availability Normalization $p_n$.
- Created `wiki/papers/2022_Zhang_GCN_TRN_EV_Availability.md` and updated `wiki/models/GCN.md`.

## [2026-07-31] ingest | 2022_Cao_Robust_Deep_Gaussian_Process_Load
- Ingested paper by Cao et al. (IEEE TII 2022).
- Extracted mathematical equations: Gaussian Process Posterior Distribution, Doubly Stochastic Variational Inference Deep GP ELBO $\mathcal{L}_{\text{DGP}}$, Reparameterization Layer Sampling, Pinball Loss.
- Created `wiki/papers/2022_Cao_Robust_Deep_Gaussian_Process_Load.md` and updated `wiki/models/Deep_Gaussian_Process.md`.

## [2026-07-31] ingest | 2023_Huang_MetaProbformer_EV_Load
- Ingested paper by Huang et al. (IEEE TITS 2023).
- Extracted mathematical equations: ProbSparse Self-Attention Sparsity $\bar{S}(q_l, K)$, Gaussian Likelihood Output, Reptile Meta-Update Rule, CRPS score.
- Created `wiki/papers/2023_Huang_MetaProbformer_EV_Load.md` and updated `wiki/models/MetaProbformer.md`.

## [2026-07-31] ingest | 2023_Ziyabari_Multi_Branch_ResTrans_Solar
- Ingested paper by Ziyabari et al. (IEEE TIA 2023).
- Extracted mathematical equations: Time Embedding Layer $C(\tau)[j]$, Multi-Branch ResNet Spatial Layer $Z_D$, Gradient Identity Backpropagation $\frac{\partial \mathcal{L}}{\partial Z_0}$.
- Created `wiki/papers/2023_Ziyabari_Multi_Branch_ResTrans_Solar.md` and updated `wiki/models/ResTrans.md`.

## [2026-07-31] ingest | 2023_Koohfar_Transformer_EV_Demand
- Ingested paper by Koohfar et al. (Sustainability 2023).
- Extracted mathematical equations: Multi-step Transformer Self-Attention, ARIMA/SARIMA Lag Polynomials $\Phi(L^s)\phi(L)$.
- Created `wiki/papers/2023_Koohfar_Transformer_EV_Demand.md`.

## [2026-07-31] ingest | 2024_Qu_Physics_Informed_GAT_EV_Load
- Ingested paper by Qu et al. (IEEE TITS 2024).
- Extracted mathematical equations: GAT Spatial Attention $\alpha_{ij}$, Momentum Residual Connections $\mathbf{x}_i''$, TPA-LSTM Decoder $\tilde{\alpha}_m$, PIML Price Elasticity Pseudo-Sampling $\Delta y_i$, FOMAML Pre-training.
- Created `wiki/papers/2024_Qu_Physics_Informed_GAT_EV_Load.md` and updated `wiki/models/PAG.md`.

## [2026-07-31] ingest | 2024_Zhong_V2G_SVE_Evaluation_Metric
- Ingested paper by Zhong et al. (IEEE TSG 2024).
- Extracted mathematical equations: Three Key Findings on Forecast Quality vs Value, Aggregate EV Fleet Model ($E_t^+, E_t^-, P_t^+, P_t^-$), V2G-SVE Metric $\frac{V_2 - V_1}{V_1}$, Constant 0.20s Computation Time.
- Created `wiki/papers/2024_Zhong_V2G_SVE_Evaluation_Metric.md` and updated `wiki/metrics/V2G_SVE.md`.

## [2026-07-31] ingest | 2024_Xu_Day_Ahead_EVCB_EVSC_Parking_Lot
- Ingested paper by Xu et al. (Energy 2024).
- Extracted mathematical equations: EVCB Feature Vector $EV_n$, ADMM Augmented Lagrangian Neural Network Training, TOU K-Means++ Clustering, EVSFD Feasible Domain Boundaries, Schedulable Capacity $p_{n,t}^{sc}$.
- Created `wiki/papers/2024_Xu_Day_Ahead_EVCB_EVSC_Parking_Lot.md` and updated `wiki/models/EVSFD.md`.

## [2026-07-31] ingest | 2024_Bampos_EV_Load_Forecasting_DAM
- Ingested paper by Bampos et al. (Applied Energy 2024).
- Extracted mathematical equations: Session power calculation $P_i = E_i / t_i$, Multiplicative Trend-Residual Decomposition $\frac{\text{EVLC}_t}{\text{Average}(\text{EVLC trend})}$, 36-hour DAM rolling evaluation across 4 public EV datasets.
- Created `wiki/papers/2024_Bampos_EV_Load_Forecasting_DAM.md` and updated `wiki/models/XGBoost.md`.

## [2026-07-31] ingest | 2024_Feng_LSTM_Transformer_EV_Consumption
- Ingested paper by Feng et al. (SSRN 2024).
- Extracted mathematical equations: Ampere-Hour (Ah) Continuous SOC Reconfiguration $\text{SOC}_{t+1} = \text{SOC}_t + \frac{\int I dt}{C}$, 3D K-Means Driving Condition Clustering $E = \sum \|x - \bar{x}_i\|^2$, LSTM-Transformer Hybrid Architecture $h_t = o_t \cdot \tanh(C_{t-1} f_t + i_t \tilde{C}_t)$.
- Created `wiki/papers/2024_Feng_LSTM_Transformer_EV_Consumption.md` and updated `wiki/models/LSTM_Transformer.md`.

## [2026-07-31] ingest | 2024_Cao_Feature_Enhanced_Probabilistic_EV_Load
- Ingested paper by Cao et al. (Applied Energy 2024).
- Extracted mathematical equations: Two-Stage Pearson Correlation Prior Reweighting $\mu_X = \text{Softmax}(\text{GRN}(\tilde{X}, r_X))$, Gated Residual Network $\text{Norm}(Y + \text{GLU}(d_1))$, Winkler Score $S_W^{(\beta)}$.
- Created `wiki/papers/2024_Cao_Feature_Enhanced_Probabilistic_EV_Load.md` and updated `wiki/models/FEDM.md`.

## [2026-07-31] ingest | 2024_Ali_MQ_TCN_Transfer_Learning_EV
- Ingested paper by Ali et al. (arXiv 2024).
- Extracted mathematical equations: Dilated Causal Convolution $G(s)$, Pinball Loss $L_{\text{PB}}$, Inductive Transfer Learning Head Replacement, DTW Similarity Matching.
- Created `wiki/papers/2024_Ali_MQ_TCN_Transfer_Learning_EV.md` and updated `wiki/models/MQ_TCN.md`.

## [2026-07-31] ingest | 2025_Yang_Stochastic_MPC_Microgrid_EV
- Ingested paper by Yang et al. (IEEE TTE 2025).
- Extracted mathematical equations: Individual EV Battery Dynamics $e_{\text{EV}}^i(t)$, Aggregator State Equation $E_{\text{agg}}(t)$, Upper-Layer Multi-Scenario MPC (MS-MPC), Lower-Layer Individual Power Allocation, Two-Stage Backward Scenario Reduction.
- Created `wiki/papers/2025_Yang_Stochastic_MPC_Microgrid_EV.md` and updated `wiki/models/MS_MPC.md`.

## [2026-07-31] ingest | 2025_Hussain_Hybrid_LSTM_Transformer_Demand
- Ingested paper by Hussain et al. (Scientific Reports 2025).
- Extracted mathematical equations: Hybrid LSTM Encoder-Decoder + Multi-Head Self-Attention, Global Average Pooling 1D $h_{\text{pool}} = \frac{1}{n}\sum h_i$, Multi-horizon medium/long-term forecasting (30, 120, 240 days).
- Created `wiki/papers/2025_Hussain_Hybrid_LSTM_Transformer_Demand.md`.

## [2026-07-31] ingest | 2025_Zheng_Coherent_Hierarchical_EV_Load
- Ingested paper by Zheng et al. (IEEE TIA 2025).
- Extracted mathematical equations: Partial Input Convex Neural Network (PICNN) Quantile Gradient $q(\alpha|h) = \nabla_\alpha f(\alpha, h)$, Multivariate Energy Score Loss $L_{\text{ES}}$, Differentiable Convex Optimization Layers (DCL) Reconciliation $x_t^* = \arg\min (\hat{x}_t - x)^T Q (\hat{x}_t - x)$.
- Created `wiki/papers/2025_Zheng_Coherent_Hierarchical_EV_Load.md` and updated `wiki/models/PICNN.md`.

## [2026-07-31] ingest | 2025_Weqar_LTLM_LSTM_EV_Load
- Ingested paper by Weqar et al. (IEEE DELCON 2025).
- Extracted mathematical equations: Long-Term Load Memory (LTLM) LSTM Gating Cells, 200-day lookback for 100-day long-term multi-month forecast.
- Created `wiki/papers/2025_Weqar_LTLM_LSTM_EV_Load.md`.

## [2026-07-31] ingest | 2025_Khan_Transformer_BiLSTM_Price_Forecasting
- Ingested paper by Khan et al. (IEEE TIA 2025).
- Extracted mathematical equations: Transformer Positional Encoding $PE$, Multi-Head Attention, BiLSTM Forward ($\vec{h}_t$) and Backward ($\overleftarrow{h}_t$) hidden states, NYISO/PJM/MISO Day-Ahead market evaluation.
- Created `wiki/papers/2025_Khan_Transformer_BiLSTM_Price_Forecasting.md` and updated `wiki/models/Transformer_BiLSTM.md`.

## [2026-07-31] ingest | 2025_Bao_ResMMoT_Informer_Time_Series
- Ingested paper by Bao et al. (IEEE TNNLS 2025).
- Extracted mathematical equations: Wavelet Noise Reduction (WNR) db4 DWT, ResMMoT Top-$K$ Sparse MoE Routing $y = \sum_{i \in S} g_i(x) f_i(x)$, Informer ProbSparse Attention $\mathcal{A}(Q, K, V)$.
- Created `wiki/papers/2025_Bao_ResMMoT_Informer_Time_Series.md` and updated `wiki/models/ResMMoT_Informer.md`.

## [2026-07-31] ingest | 2025_Tian_MSSTGAN_City_EV_Load
- Ingested paper by Tian et al. (IEEE Access 2025).
- Extracted mathematical equations: Spatio-Temporal Embedding $X_{\text{STE}}$, Pyramid Split Spatial Attention $H_S^{(l)} = \text{Softmax}(X_q X_k^T / \sqrt{D}) X_v$, Adaptive Gated Fusion $H^{(l)} = z \odot H_S + (1-z) \odot H_T$.
- Created `wiki/papers/2025_Tian_MSSTGAN_City_EV_Load.md` and updated `wiki/models/MSSTGAN.md`.

## [2026-07-31] ingest | 2025_Matrone_QR_LSTM_Attention_EV_Load
- Ingested paper by Matrone et al. (ACM E-Energy 2025).
- Extracted mathematical equations: LSTM Encoder-Decoder with Attention, Pinball Loss $L_\tau(y, \hat{y})$, Continuous Ranked Probability Score $\text{CRPS}(\hat{F}, y)$.
- Created `wiki/papers/2025_Matrone_QR_LSTM_Attention_EV_Load.md` and updated `wiki/models/QR_LSTM_Attention.md`.

## [2026-07-31] ingest | 2025_Hussain_CAT_Former_Short_Term_EV
- Ingested paper by Hussain et al. (Scientific Reports 2025).
- Extracted mathematical equations: Temporal Vector $X_{\text{temporal}}$, Contextual Vector $X_{\text{context}} = [S_{\text{lat}}, S_{\text{long}}, W_{\text{temp}}, W_{\text{percip}}, W_{\text{wind}}]$, Multi-Head Self-Attention Decoder Output.
- Created `wiki/papers/2025_Hussain_CAT_Former_Short_Term_EV.md` and updated `wiki/models/CAT_Former.md`.

## [2026-07-31] ingest | 2026_Romia_CNN_LSTM_Attention_Fast_Charging
- Ingested paper by Romia & Huang (IEEE TIA 2026).
- Extracted mathematical equations: Single-Head Attention $\text{score}(Q, K) = Q^T K$, CNN-LSTM-Transformer Encoder $\hat{H} = \text{Norm}(H + \text{MHA}(Q, K, V))$, Optuna TPE Hyperparameter Tuning.
- Created `wiki/papers/2026_Romia_CNN_LSTM_Attention_Fast_Charging.md` and updated `wiki/models/CNN_LSTM_Attention.md` and `wiki/models/CNN_LSTM_Transformer.md`.

## [2026-07-31] ingest | 2026_Liu_MFT_Multi_Scale_Fusion_Transformer
- Ingested paper by Liu et al. (Scientific Reports 2026).
- Extracted mathematical equations: Scale Masked Attention $m_n^{a,b}$, Pearson Correlation Base Weight $w_i = \text{Softmax}(\rho_i)$, Multi-variable Fusion Module (MFM) Sample-Level Cross-Attention Reweighting $\tilde{w}_i = w_i + \sigma_i^w$.
- Created `wiki/papers/2026_Liu_MFT_Multi_Scale_Fusion_Transformer.md` and updated `wiki/models/MFT.md`.

---

## [2026-08-02] lint | Wiki Health Check & Fixes
- **Issues found:** 3 empty horizon files, 3 missing dataset pages, 5 missing feature pages, 2 missing metric pages, 1 orphan root file, 16 stub papers not in log, research_gaps.md outdated (33 vs 54 papers).
- **Fixed — Horizons created (3):**
  - `wiki/horizons/Short_Term_Forecasting.md`
  - `wiki/horizons/Day_Ahead_Forecasting.md`
  - `wiki/horizons/Spatial_Temporal_Forecasting.md`
- **Fixed — Datasets created (3):**
  - `wiki/datasets/Boulder_Colorado.md`
  - `wiki/datasets/Pecan_Street.md`
  - `wiki/datasets/ElaadNL.md`
- **Fixed — Features created (5):**
  - `wiki/features/Historical_Load.md`
  - `wiki/features/Arrival_Departure_Time.md`
  - `wiki/features/State_of_Charge.md`
  - `wiki/features/Electricity_Tariff.md`
  - `wiki/features/Weather_Traffic.md`
- **Fixed — Metrics created (2):**
  - `wiki/metrics/RMSE.md`
  - `wiki/metrics/MAPE.md`
- **Fixed — MLP orphan:** `MLP.md` (root, empty) → moved to `wiki/models/MLP.md` with full content.
- **Remaining:** 16 stub papers require re-ingest from PDF; `research_gaps.md` needs synthesis update to cover 54 papers.

---

## [2026-08-02] ingest | Auto-ingest 8 papers
- Ingested 8 papers requested by the user:
  - 2024_Helmy_Autoformer_EV_Charging
  - 2024_Ke_Divide_Conquer_Transformer_EV
  - 2024_Li_DiffPLF_Conditional_Diffusion_EV
  - 2024_Zhou_Conformal_Prediction_DER
  - 2025_Alghamdi_REST_Network_Port_EV
  - 2025_Fan_EV_STLLM_Spatio_Temporal_LLM
  - 2025_Meyer_Benchmark_Foundation_Models
  - 2025_Zheng_BWO_ICEEMDAN_iTransformer
- Extracted methods, datasets, equations, and forecasting horizons.
- Replaced stub wiki pages with fully structured markdown pages according to schema.

## [2026-08-02] ingest | Auto-ingest 8 new papers
- Ingested 8 papers requested by the user:
  - 2023_Cheng_VMD_Prophet_LSTM
  - 2025_Han_Vertical_Federated_EGAT_LSTM
  - 2025_Li_DC_Charging_Profiles_TFT
  - 2025_Li_Multi_View_Graph_Intrusion_Detection_EV
  - 2025_Zhu_Personalized_Federated_Learning
  - 2026_Chen_PC_M3_Mamba_EV_Clusters
  - 2026_Hao_Mamba_KAN_HyKANet_EV
  - 2026_Lahoti_Mamba_3_Sequence_Modeling
- Wrote a python extraction script using pymupdf to extract text.
- Created full structured wiki pages for each paper, extracting methodology, datasets, features, horizons, and key equations.
- Replaced stub wiki pages with fully structured markdown pages according to schema.

## [2026-08-07] ingest | 2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load
- Ingested PDF paper: Decomposition and Stacked Meta-Learning for Short-Term Electric Vehicle Load Forecasting.
- Added structured note `wiki/papers/2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load.md` and copied PDF to `raw_sources/2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load.pdf`.

## [2026-08-07] ingest | 2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load
- Ingested PDF paper: Load Forecasting of Electric Vehicle Charging Stations: Attention Based Spatiotemporal MultiGraph Convolutional Networks.
- Added structured note `wiki/papers/2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load.md` and copied PDF to `raw_sources/2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load.pdf`.

## [2026-08-07] ingest | 2025_Wu_Meta_Learning_Physics_Informed_GACN_Power_System
- Ingested PDF paper: Meta-Learning Enhanced Physics-Informed Graph Attention Convolutional Network for Distribution Power System State Estimation.
- Added structured note `wiki/papers/2025_Wu_Meta_Learning_Physics_Informed_GACN_Power_System.md` and copied PDF to `raw_sources/2025_Wu_Meta_Learning_Physics_Informed_GACN_Power_System.pdf`.


## [2026-08-07] ingest | 2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load
- Ingested PDF paper: Electric vehicles charging stations load forecasting based on hybrid XGBoost-BiLSTM model.
- Added structured note `wiki/papers/2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load.md` and copied PDF to `raw_sources/2025_Electric_Vehicles_Charging_Stations_Load_Forecasting_Based_on_Hybrid_XGBoost_BiLSTM_Model.pdf`.

## [2026-08-09] ingest | 2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words
- Ingested foundational paper: A Time Series is Worth 64 Words: Long-term Forecasting with Transformers.
- Created `wiki/papers/2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words.md` and copied PDF to `raw_sources/2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words.pdf`.

## [2026-08-09] ingest | 2022_Kim_RevIN_Reversible_Instance_Normalization
- Ingested foundational paper: Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift.
- Created `wiki/papers/2022_Kim_RevIN_Reversible_Instance_Normalization.md` and copied PDF to `raw_sources/2022_Kim_RevIN_Reversible_Instance_Normalization.pdf`.

## [2026-08-09] ingest | 2021_Lim_TFT_Temporal_Fusion_Transformers
- Ingested foundational paper: Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting.
- Created `wiki/papers/2021_Lim_TFT_Temporal_Fusion_Transformers.md` and copied PDF to `raw_sources/2021_Lim_TFT_Temporal_Fusion_Transformers.pdf`.

## [2026-08-09] ingest | 2023_Zhang_Crossformer_Cross_Dimension_Dependency
- Ingested foundational paper: Crossformer: Transformer Utilizing Cross-Dimension Dependency for Multivariate Time Series Forecasting.
- Created `wiki/papers/2023_Zhang_Crossformer_Cross_Dimension_Dependency.md` and copied PDF to `raw_sources/2023_Zhang_Crossformer_Cross_Dimension_Dependency.pdf`.

## [2026-08-09] ingest | 2023_Zeng_DLinear_Are_Transformers_Effective_LTSF
- Ingested foundational paper: Are Transformers Effective for Time Series Forecasting?.
- Created `wiki/papers/2023_Zeng_DLinear_Are_Transformers_Effective_LTSF.md` and copied PDF to `raw_sources/2023_Zeng_DLinear_Are_Transformers_Effective_LTSF.pdf`.

## [2026-08-09] ingest | 2023_Wu_TimesNet_Temporal_2D_Variation_Modeling
- Ingested foundational paper: TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis.
- Created `wiki/papers/2023_Wu_TimesNet_Temporal_2D_Variation_Modeling.md` and copied PDF to `raw_sources/2023_Wu_TimesNet_Temporal_2D_Variation_Modeling.pdf`.

## [2026-08-09] ingest | 2019_Li_LogSparse_Enhancing_Locality_Transformer
- Ingested foundational paper: Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting.
- Created `wiki/papers/2019_Li_LogSparse_Enhancing_Locality_Transformer.md` and copied PDF to `raw_sources/2019_Li_LogSparse_Enhancing_Locality_Transformer.pdf`.

## [2026-08-09] ingest | 2017_Finn_MAML_Model_Agnostic_Meta_Learning
- Ingested foundational paper: Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks.
- Created `wiki/papers/2017_Finn_MAML_Model_Agnostic_Meta_Learning.md` and copied PDF to `raw_sources/2017_Finn_MAML_Model_Agnostic_Meta_Learning.pdf`.

## [2026-08-09] ingest | 2018_Nichol_Reptile_First_Order_Meta_Learning
- Ingested foundational paper: On First-Order Meta-Learning Algorithms.
- Created `wiki/papers/2018_Nichol_Reptile_First_Order_Meta_Learning.md` and copied PDF to `raw_sources/2018_Nichol_Reptile_First_Order_Meta_Learning.pdf`.


## [2026-08-09] ingest | 2021_Zhou_Informer_Beyond_Efficient_Transformer
- Ingested core benchmark paper: Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting.
- Created `wiki/papers/2021_Zhou_Informer_Beyond_Efficient_Transformer.md` and copied PDF to `raw_sources/2021_Zhou_Informer_Beyond_Efficient_Transformer.pdf`.

## [2026-08-09] ingest | 2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation
- Ingested core benchmark paper: Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting.
- Created `wiki/papers/2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation.md` and copied PDF to `raw_sources/2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation.pdf`.

## [2026-08-09] ingest | 2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series
- Ingested core benchmark paper: iTransformer: Inverted Transformers Are Effective for Time Series Forecasting.
- Created `wiki/papers/2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series.md` and copied PDF to `raw_sources/2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series.pdf`.


## [2026-08-09] dataset-extraction | 70_Papers_Dataset_Mining
- Extracted and audited datasets, long URLs, repositories, open data portals, and data availability notes across all 70 paper PDFs in `raw_sources/`.
- Generated comprehensive report note `dataset_extraction_report.md`.
- Created wiki dataset notes: `[[Real_World_EV_DC_Charging]]`, `[[FEDQR_Dataset]]`, `[[DiffPLF_Dataset]]`, `[[Paris_Belib_EV]]`, `[[Hourly_EV_Load]]`.

## [2026-08-09] dataset-audit | Palo_Alto_and_Global_Datasets
- Conducted deep scan regex search across all 70 raw paper PDFs for `Palo Alto`, `Dundee`, `Perth`, `CrowdCharge`, and additional datasets.
- Identified 5 papers utilizing the City of Palo Alto EV Dataset with exact URLs: `https://data.paloalto.gov/datasets/194693/electric-vehicle-charging-`
- Created dataset wiki notes: `[[Palo_Alto_EV]]`, `[[Dundee_EV]]`, `[[Perth_EV]]`, `[[CrowdCharge_EV]]`.
- Updated paper summary notes and master `dataset_extraction_report.md`.

## [2026-08-10] synthesis | Probabilistic_Research_Gaps_P1_P5
- Synthesized 5 deep Probabilistic Research Gaps (P-1 to P-5) across statistical learning theory and EV charging load literature.
- Updated `research_gaps.md` with dedicated Probabilistic Deep-Dive section and priority matrix.
- Integrated Gaps P-1 to P-5 into `progress_summary_and_research_gaps.md`, `proposed_architectures.md`, and `transformer_research_ideas.md`.
- Formulated novelty combination: Mamba Backbone + Cross-Attention + Conformalized PICNN Head for Q1 publication strategy.


## [2026-08-10] ingest | 2021_Rasul_TimeGrad_Diffusion_Forecasting
- Ingested landmark paper: Autoregressive Denoising Diffusion Models for Multivariate Probabilistic Time Series Forecasting (TimeGrad, ICML 2021).
- Created `wiki/papers/2021_Rasul_TimeGrad_Diffusion_Forecasting.md` and updated `raw_sources/`.

## [2026-08-10] ingest | 2021_Tashiro_CSDI_Conditional_Diffusion_Forecasting
- Ingested landmark paper: CSDI: Conditional Score-based Diffusion Models for Probabilistic Time Series Imputation and Forecasting (NeurIPS 2021).
- Created `wiki/papers/2021_Tashiro_CSDI_Conditional_Diffusion_Forecasting.md` and updated `raw_sources/`.

## [2026-08-10] ingest | 2019_Toubeau_Deep_Probabilistic_Scheduling_Power_Markets
- Ingested landmark paper: Deep Learning-Based Multivariate Probabilistic Forecasting for Short-Term Scheduling in Power Markets (IEEE TPWRS).
- Created `wiki/papers/2019_Toubeau_Deep_Probabilistic_Scheduling_Power_Markets.md` and updated `raw_sources/`.

## [2026-08-10] ingest | 2013_Roberts_Gaussian_Processes_Time_Series
- Ingested landmark paper: Gaussian processes for time-series modelling (Royal Society).
- Created `wiki/papers/2013_Roberts_Gaussian_Processes_Time_Series.md` and updated `raw_sources/`.

## [2026-08-10] ingest | 2021_Stankeviciute_Conformal_Time_Series_Forecasting
- Ingested landmark paper: Conformal Time-Series Forecasting (NeurIPS 2021).
- Created `wiki/papers/2021_Stankeviciute_Conformal_Time_Series_Forecasting.md` and updated `raw_sources/`.

## [2026-08-10] ingest | 2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load
- Ingested landmark paper: Probabilistic Load Forecasting via Quantile Regression Averaging on Sister Forecasts (IEEE TSG).
- Created `wiki/papers/2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load.md` and updated `raw_sources/`.

## [2026-08-10] catalog | GitHub_Repositories_Index
- Extracted and indexed 22 official GitHub Repositories across all papers in the vault.
- Created master note `wiki/references/github_repositories_index.md` and linked to `index.md`.

## [2026-08-20] ingest | 2018_Bai, 2020_Oreshkin, 2023_Challu, 2024_Das | Added papers, models, datasets, raw sources and index links

## [2026-08-23] ingest | Full Thorough Re-Ingestion of All 80 Raw PDFs
- Extracted full text from all 80 PDFs in `raw_sources/` to `scratch/txt/` (pymupdf).
- Rewrote all 80 notes in `wiki/papers/` to the complete schema: verified YAML frontmatter, methodology with verbatim equations in LaTeX, dataset details (location, size, resolution), performance numbers vs baselines, limitations, BibTeX, and citation-graph wikilinks.
- Confirmed PDF-to-note mapping for all ambiguous filenames (e.g., 2019 Zhu Energies/ApplSci pair, 2025 Hussain Hybrid LSTM-Transformer, 2025 Weqar LTLM).
- Discovered and appended ~40 new/corrected dataset & code URLs to `dataset_extraction_report.md` (Boulder direct links, ST-EVCDP Shenzhen repo, MSSTGAN 4-city repo, Dallas port Kaggle DOI, FEDQR dataset, PC-M3 dsgrid-TEMPO, Norway Hourly_EV repo, etc.).
- Metadata corrections: Cheng VMD-Prophet-LSTM re-dated to 2023; Lyapunov paper identified as arXiv:2604.16873 (2026); DOIs fixed for Alizadeh (10.1109/TSG.2013.2275988), Shi STMGCN (10.1109/TSG.2023.3321116), Wu Meta-PIGACN (10.1109/TNSE.2025.3525625); removed fabricated results from Toubeau and Yang notes (replaced with text-verifiable figures); corrected TimeGrad CRPS values and Roberts GP author list.
- Updated `index.md` catalog entry for the Cheng paper.

## [2026-08-23] maintenance | Renamed 2025_Cheng_VMD_Prophet_LSTM_Federated ? 2023_Cheng_VMD_Prophet_LSTM
- Paper is Cheng et al. 2023 (Front. Energy Res., doi:10.3389/fenrg.2023.1297849) and contains no federated learning despite the legacy PDF filename.
- Renamed note and refs note; replaced all wikilinks across vault (index, research_gaps, features, papers, references data).
- Corrected FL misattributions in research_gaps.md: mermaid nodes re-labeled to "VMD + Prophet-LSTM Hybrid (Cheng 2023)", Gap 11 FL bullet reframed as an open gap, Cheng removed from FL paper list in Gap 5.
- Source PDF left untouched per raw_sources immutability rule.

## [2026-08-23] maintenance | Renamed source PDF to 2023_Cheng_VMD_Prophet_LSTM.pdf
- Renamed `raw_sources/2025_Federated_Learning_VMD_LSTM_Electric_Vehicle_Charging_Load_Prediction.pdf` ? `raw_sources/2023_Cheng_VMD_Prophet_LSTM.pdf` for consistency with the wiki note; updated stale filename references in extract.py, dataset_extraction_report.md, and scan_results.json.

## [2026-08-23] maintenance | Renamed source PDF to 2023_Cheng_VMD_Prophet_LSTM.pdf
- Renamed raw_sources/2025_Federated_Learning_VMD_LSTM_Electric_Vehicle_Charging_Load_Prediction.pdf to raw_sources/2023_Cheng_VMD_Prophet_LSTM.pdf for consistency with the wiki note.
- Updated stale filename references in extract.py, dataset_extraction_report.md, and scan_results.json.

## [2026-08-23] synthesis | Concept-Page Propagation & Synthesis Refresh (Re-Ingestion Pass 2)
- Aggregated verified frontmatter of all 80 paper notes into scratch/concept_aggregation.json (318 models / 210 datasets / 330 features references).
- wiki/models/: updated Literature Usage for LSTM (+37), Transformer (+18), GCN/GRU/CNN/MLP/TCN/XGBoost/NBEATS/NHiTS/TiDE/PAG and others; created 16 new architecture pages (Informer, Autoformer, DeepAR, PatchTST, DLinear, iTransformer, TimesNet, TFT, TimeGrad, CSDI, DiffPLF, Crossformer, LogSparse_Transformer, Mamba_SSM, RevIN, VMD_Prophet_LSTM).
- wiki/datasets/: updated EV dataset pages with verified URLs; created Dallas_Port_EV, Shenzhen_ST_EVCDP, Fujian_Province_EV_Charging_Station_Data, Utrecht_SmoothEMS, CICEVSE2024, REFIT, Beijing_Fast_Charging, NHTS_2008/2009; folded Norway Hourly_EV + ACN JPL/Office into existing pages.
- wiki/metrics/: updated MAE/MAPE/RMSE; created CRPS, Pinball_Loss, Winkler_Score, PICP, R_squared, NRMSE.
- wiki/features/: updated Historical_Load, Electricity_Tariff, State_of_Charge, Arrival_Departure_Time, Cyclical_Encodings, Weather_Traffic.
- wiki/horizons/: updated Short_Term/Day_Ahead/Spatial_Temporal; created Long_Term_Forecasting (19 papers).
- wiki/github/ + references/github_repositories_index.md: appended newly discovered official repos in 3 new sections; updated TSFM & Probabilistic repo notes.
- Refreshed progress_summary_and_research_gaps.md (80-paper counts), proposed_architectures.md (Proposals 8-9 from 2026 Mamba/KAN lines; refined novelty claim to full Mamba+cross-attention+conformalized-PICNN combo), transformer_research_ideas.md (resolved count inconsistencies; metadata corrections).

## [2026-08-23] ingest | 6 New Papers from raw_sources/new (Elsevier 2026 batch)
- Renamed opaque Elsevier filenames to convention and moved PDFs from raw_sources/new/ to raw_sources/:
  - 2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load (Computers and Electrical Engineering)
  - 2026_Wang_Xiaoping_TriModal_Causal_EV_Demand (Pattern Recognition Letters) - TriCast
  - 2026_Wang_Xu_Similar_Day_Selection_EV_Load (Applied Energy)
  - 2026_Singh_MetaLearning_Informer_Probabilistic_EV (Applied Soft Computing) - MAML-Informer
  - 2026_Wang_Shengyou_ML_Geographical_Transferability_EV (J. Energy Storage)
  - 2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging (Sustainable Energy, Grids and Networks) - USDT
- Extracted full texts to scratch/txt/; created full-schema paper notes with verbatim equations, dataset URLs, results, BibTeX.
- Propagated citations to models/metrics/horizons/features/datasets pages; created wiki/models/TriCast.md, wiki/models/USDT.md, wiki/datasets/UrbanEV_Dataset.md.
- Corpus now 86 papers. Updated index.md and dataset_extraction_report.md.


## [2026-08-23] maintenance | Encoding corruption in dataset_extraction_report.md detected & repaired
- Cause: PowerShell Add-Content appended text using ANSI encoding, breaking UTF-8 (affects Thai text and unicode symbols).
- Repaired via cp1252-to-UTF8 byte reversal + wildcard brute-force repair + manual rewrite of the Thai intro line; residual PDF glyph-ID junk removed.
- Minor unrecoverable artifacts may remain inside long quoted PDF snippets (low-value extraction noise); all tables, URLs, and structure intact.
- RULE going forward: always append to vault files with Python (encoding=utf-8), never PowerShell Add-Content.


## [2026-08-23] ingest | 6 arXiv Foundational Papers from raw_sources/new
- Renamed and moved PDFs to raw_sources/: Graph WaveNet (2019 IJCAI), DiffSTG (2023), LipSCDE treatment effects (2023), TimeMachine (2024), Bi-Mamba+ (2024), KAN (2024).
- Full-schema paper notes created; propagated to models/metrics/horizons/github; created wiki/models/Graph_WaveNet.md, DiffSTG.md, KAN.md.
- Corpus now 92 papers. Flagged 2405.13843v1.pdf (hyperspectral chick embryo imaging) as off-topic - pending user decision.
- Removed off-topic 2405.13843v1.pdf (hyperspectral chick embryo imaging) per user decision; raw_sources/new emptied.


## [2026-08-23] ingest | Batch 3: 11 Papers (He/Xiong carryover + 9 new from raw_sources/new)
- Ingested: Forwardformer (TPWRS 2024), DeVilmarest adaptive net-load (TPWRS 2024), He JointPGM robust MTS (arXiv 2407.13194), Xiong combined DL (APET 2023), Huo ACN demand (2024), Li CNN-GRU TOU (2024), Ma LASSO-BPNN mid-term (2024), Shi Naihao PI evaluation (2024), Zhou MixerInformer transfer (2025), Kyriakopoulos ML comparison (2026), Jia EVformer (WEVJ 2026).
- Propagated to models/metrics/horizons/datasets/github; created wiki/models/EVformer.md.
- Removed duplicate Elsevier PDF re-download (S0045790626002739 = already-ingested MoghadamDost TFT-Conformal).
- Corpus now 103 papers.


## [2026-08-23] synthesis | Corpus Refresh to 103 Papers + BibTeX Export
- Refreshed research_gaps.md, progress_summary_and_research_gaps.md, proposed_architectures.md, transformer_research_ideas.md against the full 103-paper corpus.
- Novelty re-validation: flagship combo (Mamba + cross-attention exogenous fusion + conformalized PICNN head) remains unexplored; refuted sub-claims recorded (USDT = first probabilistic EV Transformer; MoghadamDost = first conformalized EV Transformer; EVformer = dynamic-graph pure Transformer).
- Exported thesis_references.bib with all 103 BibTeX entries.


## [2026-08-23] ingest | Batch 4: 5 Gap-Targeted Papers (web-discovered)

- Downloaded PDFs to raw_sources/ (arXiv / KDD '26 / CDC) and extracted full texts to scratch/txt/:
  - 2026_Yu_EnergyMamba_Graph_Mamba_ASCQR (KDD '26): GE-Mamba (GCN-conditioned bidirectional selective SSM in U-Net) + AS-CQR adaptive conformalized quantile regression (width-normalized nonconformity + online feedback); Florida CBG / NYISO / CAISO energy datasets.
  - 2026_Hong_SSM_Transformer_LSTM_Grid_Benchmark (arXiv 2602.21415): S-Mamba & PowerMamba vs PatchTST & iTransformer vs LSTM across six US ISO grids, 24-168 h; weather-covariate ranking reversal confirmed architecture-driven (parameter-controlled).
  - 2024_Menati_PowerMamba_Power_Systems_SSM (arXiv 2412.06112): dual-path standard/inverse Mamba with trend-seasonal decomposition + external-forecast token module; releases ERCOT GridSet (5-year hourly).
  - 2026_Bouaachra_INLA_Spatio_Temporal_EV_Demand (arXiv 2604.19841): Bayesian latent Gaussian model (SPDE-RW2 / ICAR-RW2) via INLA on new open ChargePlace Scotland station-level dataset (Oct 2022 - Apr 2025; Glasgow subset 96 CPIDs, 104,041 sessions); dominance vs per-station XGBoost/Poisson GLM on MAE at 70-77% of stations.
  - 2025_FernandezZapico_Stochastic_MPC_Conformal_Hub (CDC 2025): GBT point forecasts wrapped by EnbPI conformal intervals feeding scenario-based stochastic MPC of a charging energy hub (280-day closed loop).
- Created full-schema wiki/papers/ notes (verbatim equations, BibTeX, citation-graph links); created new concept pages ([[EnergyMamba]], [[AS_CQR]], [[EnbPI]], [[S_Mamba]], [[PowerMamba]], [[INLA_Latent_Gaussian_Model]] plus datasets/metrics) and propagated Literature-Usage bullets across wiki/.
- Corpus now **108 papers**. BibTeX appended to thesis_references.bib.
- Gap impact:
  - P-3 narrowed but OPEN: AS-CQR already does online width-normalized conformal recalibration under shift - but aggregate regional load, non-EV, scalar (non-covariate-conditioned) update; EnbPI hub experiment shows price-interval coverage collapse (CPI 0.60 overall, 0.22 in Autumn gas-crisis) = direct empirical evidence for adaptive recalibration need.
  - T-7 three-way benchmark CLOSED for grid-level hourly load (Hong & Lee), still OPEN for EV station-level sub-hourly probabilistic forecasting.
  - Flagship novelty repositioned: EnergyMamba refutes any bare "no Mamba+conformal combination" claim at aggregate granularity; surviving composition = EV-station-level loads + cross-attention exogenous fusion + monotone PICNN head + adaptive conformal guarantees. See research_gaps.md refresh.


## [2026-08-23] synthesis | NEW Methodology & System-Level Gaps (M-1..M-5)
- Added cross-cutting gap section to research_gaps.md, derived from Batch-4 refresh + full-corpus synthesis; no new PDFs ingested:
  - M-1 Benchmark aging / temporal validity drift (rolling-origin accuracy-vs-data-age curves across Palo Alto/Boulder/ElaadNL/ChargePlace Scotland).
  - M-2 Leakage audit + unified probabilistic benchmark protocol (CRPS/PICP/Winkler + peak-zone WAPE, fixed rolling origins).
  - M-3 Continual season-adaptive station models with jointly-guaranteed calibration (backbone updates + online quantile recalibration without forgetting rare regimes).
  - M-4 Adversarial/poisoning robustness of probabilistic EV forecasts (interval distortion under manipulated history; attack-aware recalibration).
  - M-5 Task-oriented calibration targets (calibration level x sharpness -> cost/CO2 per downstream operation).
- Priority matrix added; positioning notes: M-2 = thesis-defensibility infrastructure, M-1 = standalone analysis chapter.


## [2026-08-23] synthesis | Point-Forecast Track positioning added
- Added dedicated section to research_gaps.md recording that the thesis core remains DL point forecasting:
  - PF-1 peak-zone accuracy via asymmetric/peak-weighted loss (own benchmark: Peak-Zone WAPE 24-37%).
  - PF-2 multi-horizon Transformer (answer Kyriakopoulos: Transformers currently win short-term only).
  - PF-3 tokenization & exogenous-fusion mechanism benchmark for EV (T-2/T-3 sharpened).
  - PF-4 DC fast-charging point forecasting (remaining sliver of primary Gap 3).
  - M-1/M-2 reused as model-agnostic methodology infrastructure.
- Thesis formula recorded: RevIN + series decomposition + multi-scale patching + asymmetric peak-loss, evaluated under M-2 protocol with horizon-split reporting; probabilistic head demoted to optional extension axis (not identity change).

## [2026-08-26] audit | Synthesis consistency audit (guides + root synthesis docs)
- Verified vault state: 118 paper notes in wiki/papers/ vs 108 PDFs in raw_sources/ (10 web-discovered notes beyond last logged batch: 2021_Alvarez_APLF, 2021_Browell_Fasiolo, 2021_Obst_Vilmarest_Goude, 2022_Vilmarest_Goude_State_Space_PostCOVID, Bahdanau2016_LSTMa, Beltagy2020_Longformer, Berrisch_Ziel_CRPS_Learning, Gaillard2016_GEFCOM2014, Wintenberger2017_BOA, Zaffran2022_Adaptive_Conformal).
- Fixed 19 dead wikilinks across index.md / research_gaps.md / progress_summary_and_research_gaps.md / proposed_architectures.md / transformer_research_ideas.md: renamed-note targets updated (Lyapunov 2021->2026_Huang, Mansour 2025->2026, PC-M3 Chen->Tang, Vaswani link variant, Koohfar/Feng/Ke/Shi/Helmy/Meyer/CAT-Former/Khan/Matrone/Alghamdi/Hussain legacy names, Mamba-3 -> Lahoti).
- Refreshed stale corpus counts 103/108/70 -> 118 papers (108 PDFs) in index.md, research_gaps.md, progress_summary_and_research_gaps.md, proposed_architectures.md, transformer_research_ideas.md with 2026-08-26 date stamps.
- Regenerated paper_digest.py output (paper_digest.md): now covers all 118 papers.
- All 14 wiki/guides/*.md stubs checked: every wiki-link resolves; no count claims inside guides.

## [2026-08-31] system | Agent Customizations & Modular Skills Initialization (.agents/skills/)
- **Infrastructure Created:**
  - Initialized workspace customizations root: `.agents/skills/`
  - Created 4 modular agent skills adhering to Antigravity Progressive Disclosure schema:
    1. `.agents/skills/ingest-paper/SKILL.md` (End-to-end PDF extraction and knowledge graph propagation)
    2. `.agents/skills/extract-datasets/SKILL.md` (Deep scanning for datasets, DOIs, and GitHub links)
    3. `.agents/skills/thesis-query/SKILL.md` (Answering questions via paper_digest.md and maintaining wikilinks)
    4. `.agents/skills/refresh-synthesis/SKILL.md` (Running gen_paper_digest.py and updating gap metrics)
- **Pages Updated:**
  - [[AGENTS.md]] (Added Agent Skills Architecture section mapping workflows to runbooks)
- **Status:** All agent skills operational and compliant with the schema instructions.

## [2026-09-01] ingest | 2024_Das_TimesFM_Decoder_Only_Foundation_Model
- Source: raw_sources/New/2310.10688v4.pdf (arXiv:2310.10688v4, Das et al., Google, April 2024) -> copied to raw_sources/2024_Das_TimesFM_Decoder_Only_Foundation_Model.pdf and scratch/txt/2310.10688v4.txt (+ canonical txt).
- Created wiki/papers/2024_Das_TimesFM_Decoder_Only_Foundation_Model.md (full schema: 8 equations Eq.1-8, Table 1 corpus, Table 2/3/4/5 results, A.1 limitations, BibTeX, citation graph).
- Created wiki/references/2024_Das_TimesFM_Decoder_Only_Foundation_Model_refs.md (44 refs).
- Propagated: wiki/models/TimesFM.md (rewritten from stub, Overview + Literature Usage + Related Models), LLMTime.md (new), PatchTST/NBEATS/DeepAR/Transformer/Informer/Autoformer/FEDFormer/TimesNet/DLinear/ARIMA/ETS/CatBoost/TiDE + stubs WaveNet/TBATS/Theta/TimeGPT-1; wiki/metrics/msMAPE.md (new) + MAE/MSE/MAPE; wiki/features/Historical_Load.md; wiki/horizons/Long_Term/Short_Term/Day_Ahead; wiki/datasets/Google_Trends (new), Monash_Archive (new), Darts (new), LibCity (new) + Electricity_ECL/Wikipedia_Pageviews/ETC updates; wiki/github/Time_Series_Foundation_Models_Repos.md + github_repositories_index.md (TimesFM repo entry).
- Updated raw_sources/paper_index.md (#81), index.md (119 papers / 109 PDFs, added paper line), thesis_references.bib (+1, now 109), dataset_extraction_report.md (appended TimesFM breakdown).
- Regenerated paper_digest.md (119 papers, 369 KB, 2026-09-01).
- Duplicate check: no prior PDF with same name; content-uniq vs 2024_Das_TiDE (different paper, same first author) and vs Meyer benchmark (only referencing TimesFM).
## [2026-09-01] ingest | 2026_Khwaja_Toto_2_Scaling_Era
- Source: raw_sources/New/2605.20119v2.pdf (arXiv:2605.20119v2, Khwaja et al., Datadog AI Research + CMU, June 2026) -> copied to raw_sources/2026_Khwaja_Toto_2_Scaling_Era.pdf and scratch/txt/2605.20119v2.txt (+ canonical 2026_Khwaja_Toto_2_Scaling_Era.txt; 68705 chars, 19 pages, fitz extraction).
- Created wiki/papers/2026_Khwaja_Toto_2_Scaling_Era.md (full schema: 8 equations Eq.1-8 (CPM Eq.1, pinball Eq.2, quantile head Eq.3, pinball gradient Eq.4, NorMuon Eq.5, arcsinh scaler Eq.6, u-muP Eq.7, OWA Eq.8), Tables 1/Figs 5-10 results, BibTeX, citation graph).
- Created wiki/references/2026_Khwaja_Toto_2_Scaling_Era_refs.md (62 refs) and wiki/models/Toto.md (full: overview + CPM/quantile/NorMuon/u-muP + Literature Usage + Related Models).
- Propagated: wiki/models/Toto.md (new) + PatchTST/Transformer/Moirai/Chronos/Chronos-Bolt/Sundial/Time-MoE/TimesFM/TimesFM_2.0 (updated) + FlowState/Xihe/Timer/TiRex/Granite/TTM/xLSTM/Muon/NorMuon/Migas/Reverso (new stubs); wiki/datasets/BOOM (new), GIFT-Eval (new), TIME_Benchmark (new), Datadog_Observability (new), TempoPFN_Synthetic (new), GIFT_Eval_Pretrain (new); wiki/metrics/CRPS/MASE/Pinball_Loss/OWA (updated); wiki/features/Historical_Load.md (updated); wiki/horizons/Long_Term/Short_Term/Day_Ahead (updated); wiki/hyperparameters/Optuna_TPE (updated) + u-muP/Unit_Scaling/WSD_Schedule (new); wiki/github/Time_Series_Foundation_Models_Repos.md + github_repositories_index.md (Toto 2.0 + dd_unit_scaling entries).
- Updated raw_sources/paper_index.md (#82), index.md (120 papers / 110 PDFs, added paper line), thesis_references.bib (+1, now 110), dataset_extraction_report.md (appended 5 datasets + 6 URLs).
- Regenerated paper_digest.md (120 papers, 374 KB, 2026-09-01).
- Duplicate check: no prior wiki/papers/*Toto* or wiki/models/*Toto*; 2604.19841v1 duplicate of existing 2026_Bouaachra_INLA skipped; content-uniq vs TimesFM and other TSFMs in corpus.
## [2026-09-01] ingest | 2025_Ansari_Chronos_2_Univariate_to_Universal
- Source: raw_sources/New/2510.15821v1.pdf (arXiv:2510.15821v1, Ansari et al., Amazon Web Services, Oct 2025, 31 pages) -> copied to raw_sources/2025_Ansari_Chronos_2_Univariate_to_Universal.pdf and scratch/txt/2510.15821v1.txt (+ canonical 2025_Ansari_Chronos_2_Univariate_to_Universal.txt; 115264 chars, fitz extraction).
- Created wiki/papers/2025_Ansari_Chronos_2_Univariate_to_Universal.md (full schema: 5 equations Eq.1-5 (robust sinh-asinh scaling Eq.1-2, patch embedding Eq.3, quantile regression Eq.4, denormalization Eq.5), Tables 1-6/Figs 1-8 results, BibTeX, citation graph).
- Created wiki/references/2025_Ansari_Chronos_2_Univariate_to_Universal_refs.md (~70 refs dump, pp.15-19).
- Created wiki/models/Chronos-2.md (new, universal group-attention overview); updated wiki/models/Chronos.md, Chronos-Bolt.md, TimesFM.md, TiRex.md, Toto.md, COSMIC (new), Moirai.md, Sundial.md, TabPFN-TS (new), AutoARIMA/ETS/Theta (new), PatchTST/TFT/DeepAR/N-BEATS/Transformer/Covariates.
- Created wiki/datasets/fev-bench.md (100 tasks), Chronos_Benchmark_II.md (27 tasks), Chronos_Corpus.md; updated GIFT-Eval.md, GIFT_Eval_Pretrain.md, Electricity_ECL.md, M4.md, Solar_Dataset.md, Traffic.md, Weather.md, Wiki_Pageviews.md, Buildings_900K.md (new).
- Created wiki/metrics/SQL.md, WQL.md, Win_Rate.md, Skill_Score.md; updated CRPS.md, MASE.md, Pinball_Loss.md.
- Created wiki/features/Known_Covariates.md, Past_Only_Covariates.md, Categorical_Covariates.md, Categorical_Features.md; updated Historical_Load.md, Known_Future_Inputs.md.
- Updated wiki/horizons/Long_Term_Forecasting.md, Short_Term_Forecasting.md, Day_Ahead_Forecasting.md, Spatial_Temporal_Forecasting.md.
- Updated wiki/github/Time_Series_Foundation_Models_Repos.md (#25 Chronos-2, https://github.com/amazon-science/chronos-forecasting, 120M base / 28M small) and wiki/references/github_repositories_index.md.
- Updated raw_sources/paper_index.md (#83), index.md (121 papers / 111 PDFs, added paper line), thesis_references.bib (+1, now 111, ansari2025chronos2), dataset_extraction_report.md (appended 9 datasets/URLs, benchmarks + Table 6 + multivariatizers).
- Regenerated paper_digest.md (121 papers, 388 KB, 2026-09-01) via python gen_paper_digest.py.
- Duplicate check: no prior wiki/papers/*Chronos-2* or *2025_Ansari*; no raw_sources/*Chronos*; raw_sources/New/2510.15821v1.pdf content-uniq vs Chronos/Bolt/Chronos Benchmark II; 2510.15821v1 is the canonical Chronos-2 tech report.

