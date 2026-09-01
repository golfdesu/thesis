---
type: model
name: Convolutional Neural Network (CNN)
category: Deep Learning / Feature Extraction
tags:
  - model
  - cnn
  - deep-learning
  - spatial-features
---

# 🧠 Convolutional Neural Network (CNN)

## Overview
CNNs use parameter-sharing 1D/2D convolution kernels and pooling layers to automatically extract spatial and local receptive field features from non-stationary inputs (e.g., traffic flow, spatial station networks).

## Key Mathematical Equations
- **Convolution Layer**:
  $$y_j^l = f\left(\sum_{i \in M_j} x_i^{l-1} \otimes k_{ij}^l + b_j^l\right)$$
- **Pooling Downsampling Layer**:
  $$z_j^{l+1} = f\left(\beta_j^{l+1} \text{down}(y_j^l) + c_j^{l+1}\right)$$

## Application in EV Charging Load Forecasting
- **Traffic-Flow-to-Load Conversion**: Extracts multi-frequency features from traffic flow data (when combined with Discrete Wavelet Transform) to predict vehicle arrival rates at charging stations ([[2021_Zhang_Probabilistic_Queuing_EV_Load]]).
- **Spatial Feature Representation**: Combined with LSTMs (CNN-LSTM) or Graph networks to capture spatial-temporal dependencies across charging hubs.

## Literature Usage
- [[2021_Zhang_Probabilistic_Queuing_EV_Load]] - Wavelet-CNN Ensemble for traffic flow prediction intervals and fast-charging station load.
- [[2023_Ziyabari_Multi_Branch_ResTrans_Solar]] - CNN used as temporal baseline in multi-branch ResNet-Transformer spatio-temporal framework; standalone CNN weakest temporal model (avg RMSE 0.19 vs Transformer 0.06 on 12 sites).
- [[2025_Alghamdi_REST_Network_Port_EV]] - RESTNet ensemble couples a ResNet branch (spatial skip-connection feature extraction) with SENet + Transformer for artificial-port EV charging load: MAPE 6.5%, RMSE 9.8 kW.
- [[2025_Khan_Transformer_BiLSTM_Price_Forecasting]] - CNN benchmarked as baseline for day-ahead price forecasting on NYISO; CNN clearly worst deep model (MAE $6.83/MWh vs Transformer-BiLSTM $2.78).
- [[2025_Li_Multi_View_Graph_Intrusion_Detection_EV]] - CNN baseline in multi-view graph contrastive learning for EV charging-station intrusion detection (weighted F1 94.30% vs MVGCRL 97.20%).
- [[2026_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] - CNN among 24 baselines for hourly station-level EV load forecasting; XGBoost-BiLSTM stacking ensemble best on outlier-retained data (MAE 3.54 kWh).
- 2024 — [[2024_Li_TOU_Price_Meteorology_EV_Charging_Load]] : CNN feature-extraction front-end over TOU-price/temperature/weekday inputs feeds a two-layer GRU; CNN-GRU posts lowest MAE/RMSE at every 4–168 h horizon (4 h MAE 36.33 vs GRU 49.04, ≈26% lower).
