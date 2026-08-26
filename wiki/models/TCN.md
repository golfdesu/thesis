

## Literature Usage
- [[2018_Bai_Empirical_TCN_Sequence_Modeling]]: Causal dilated 1-D convolutions with residual blocks, normalization and dropout provide a simple TCN with a large receptive field.
- [[2019_Wu_Graph_WaveNet_Spatial_Temporal_Modeling]]: Canonical WaveNet-style **gated TCN** ($h = g(\Theta_1 \star X + b) \odot \sigma(\Theta_2 \star X + c)$) with exponentially growing dilation {1,2,1,2,...} stacked before graph convolution in each spatiotemporal layer; receptive field engineered to equal input length so all 12 horizons decode non-recursively (2.27 s total inference on METR-LA — fastest vs DCRNN/STGCN). UGnet ([[2023_Wen_DiffSTG_Probabilistic_ST_Graph_Diffusion]]) later embeds the same gated temporal convolution inside a diffusion denoiser.
- 2024 — [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] : MQ-TCN extends TCN with multi-quantile pinball heads + inductive transfer learning; 96.88% PICP on data-scarce NREL sites vs XGBoost max 80.21%.
- 2024 — [[2024_Bampos_EV_Load_Forecasting_DAM]] : TCN_sc reached nMAE 6.177%/nRMSE 8.319% on Palo Alto day-ahead forecasts — the only DL model to beat persistence anywhere, yet still behind XGBoost (5.387%) and MLP.
- 2024 — [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] : TCN-only ablation degrades to MAE 61.145 kW / RMSE 90.681 kW vs full STMGCN 53.287/78.831 kW on Beijing fast-charging stations.
- 2025 — [[2025_Bao_ResMMoT_Informer_Time_Series]] : plain TCN was the weakest deep baseline on NASDAQ100 — 20-step MAE 8.0328 vs ResMMoT-Informer 4.7171 (~41% higher error).
- 2025 — [[2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] : TCN proved unstable on outlier-retained Caltech data (train MAE 3246 kWh) and fell outside the top-ranked models.
