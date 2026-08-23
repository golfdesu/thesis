---
type: dataset
name: Caltech Adaptive Charging Network (ACN-Data)
location: Pasadena, California, USA
data_type: Real-world workplace EV charging sessions
url: "https://ev.caltech.edu/dataset"
code_url: "https://github.com/zach401/acnportal"
tags:
  - dataset
  - acn
  - open-source
---

# 📁 Caltech Adaptive Charging Network (ACN-Data)

## 🔗 Access Links & Repositories
- **Caltech ACN Data Portal**: [https://ev.caltech.edu/dataset](https://ev.caltech.edu/dataset)
- **ACN-Portal Python Library & API**: [https://github.com/zach401/acnportal](https://github.com/zach401/acnportal)

## Overview
ACN-Data is a public open-source dataset of EV charging sessions collected from workplace charging facilities at **Caltech (54 dual-head chargers)**, **JPL (~50 chargers)**, and the **Office-1 site (8 chargers)** — all published under one portal, so vault references to "ACN_Data", "ACN_Dataset", "Caltech_ACN_Dataset" or "JPL_ACN_Dataset" resolve here. It provides session-level details including connection time, disconnect time, energy delivered, and user-input estimated duration/SOC.

## Key Features Provided
- `connectionTime`: Timestamp EV plugged in.
- `disconnectTime`: Timestamp EV unplugged.
- `doneChargingTime`: Timestamp battery reached 100%.
- `kWhDelivered`: Total energy consumed (kWh).
- `userInputs`: Requested energy and expected departure.

## Papers Using This Dataset

| Paper | How Used |
|-------|----------|
| [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] | Source-domain quantile TCN transfer learning with NREL workplace data |
| [[2024_Huo_Data_Driven_EVCS_Demand_Forecasting]] | Jan 2019–Mar 2020 sessions at JPL + Caltech converted to hourly average power for Rao-1-tuned ANN/SVR/BRT comparison (ANN best: JPL RMSE 6.93 kW) |
| [[2024_Bampos_EV_Load_Forecasting_DAM]] | Day-ahead-market load-curve forecasting benchmark |
| [[2024_Qu_Physics_Informed_GAT_EV_Load]] | Caltech (54), JPL (50) & Office-1 (8) sites for transferable PAG demand prediction |
| [[2025_Hussain_Hybrid_LSTM_Transformer_Demand]] | Caltech + JPL hybrid LSTM-Transformer day-ahead benchmark |
| [[2025_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] | XGBoost-BiLSTM stacking ensemble evaluation |
| [[2025_Zheng_Coherent_Hierarchical_EV_Load]] | Coherent hierarchical probabilistic forecasting with Meteostat weather |
| [[2026_Chen_PC_M3_Mamba_EV_Clusters]] | ACN-Data sessions + ACN-Sim for physics-constrained Mamba cluster EM |
| [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] | Attention-enhanced CNN-LSTM fast-charging load forecast |
| [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] | STL decomposition + stacked meta-learning 4-dataset benchmark |
| [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] | MAML-Informer per-station meta-learning: best RMSE/MAE/CRPS/PICP of all baselines |

## Related Pages
- [[Palo_Alto_EV]]
- [[Boulder_Colorado]]
- [[ElaadNL]]
