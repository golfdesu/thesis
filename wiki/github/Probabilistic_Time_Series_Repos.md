---
type: github
name: Probabilistic & Diffusion Forecasting Repositories
category: Advanced Probabilistic Time Series Frameworks
tags:
  - github
  - probabilistic-forecasting
  - diffusion-models
  - quantile-regression
---

# 🐙 Probabilistic & Diffusion Forecasting Repositories

## Overview
This note collects open-source repositories implementing probabilistic time series models, score-based diffusion frameworks, normalizing flows, and convex quantile networks.

## Repositories & Citation Graph

### 1. CSDI (Conditional Score-Based Diffusion Models)
- **Repository URL**: `https://github.com/ermongroup/CSDI`
- **Description**: Official NeurIPS 2021 implementation of CSDI for probabilistic time series imputation and forecasting via score matching.
- **Cited Paper**: [[2021_CSDI_Conditional_Diffusion_Forecasting]]

### 2. TimeGrad (Autoregressive Denoising Diffusion Models)
- **Repository URL**: `https://github.com/zalanborsos/timegrad`
- **Description**: ICML 2021 implementation of TimeGrad combining autoregressive RNNs with denoising diffusion probabilistic models (DDPM).
- **Cited Paper**: [[2021_TimeGrad_Diffusion_Forecasting]]

### 3. GluonTS (AWS Probabilistic Time Series Modeling Library)
- **Repository URL**: `https://github.com/awslabs/gluonts` *(URL corrected during [2026-08-23] re-ingestion; was `gluon-ts`)*
- **Description**: Open-source Python library for deep learning probabilistic time series models (DeepAR, MQ-CNN, Transformer).
- **Cited Paper**: [[2021_CSDI_Conditional_Diffusion_Forecasting]] ; also cited by [[2021_TimeGrad_Diffusion_Forecasting]]

### 4. Cvxpylayers (Convex Neural Networks for Monotonic Quantiles)
- **Repository URL**: `https://github.com/cvxgrp/cvxpylayers`
- **Description**: PyTorch/TensorFlow layer library for convex optimization layers used in PICNN to prevent quantile crossing.
- **Cited Paper**: [[2025_Coherent_Hierarchical_EV_Load]]

### 5. CP-Flow (Conformal Prediction & Normalizing Flows)
- **Repository URL**: `https://github.com/CW-Huang/CP-Flow` *(alias `cvxgrp/CP-Flow` listed in [2026-08-23] re-ingestion table)*
- **Description**: Normalizing flow framework providing distribution-free uncertainty estimation and valid coverage guarantees.
- **Cited Paper**: [[2025_Coherent_Hierarchical_EV_Load]]

### 6. Conformal RNN (CF-RNN, Conformal Time Series Forecasting) — *added in [2026-08-23] re-ingestion*
- **Repository URL**: `https://github.com/kamilest/conformal-rnn`
- **Description**: Official NeurIPS 2021 implementation of conformalized quantile regression (MQR baseline) wrapped around recurrent forecasters for valid, adaptive prediction intervals.
- **Cited Paper**: [[2021_Conformal_Time_Series_Forecasting]]

### 7. ChargingEnergyHubs_MPC (Stochastic MPC with Conformal Prediction) — *added in [2026-08-23] ingestion pass*
- **Repository URL**: `https://github.com/diegofz/ChargingEnergyHubs_MPC`
- **Description**: IEEE CDC 2025 code for an EV+PV+BESS charging energy hub EMS: GBT point forecasters wrapped by EnbPI conformal intervals (MAPIE) feeding scenario-based stochastic/recourse SOCP-MPC, evaluated closed-loop over 280 days.
- **Cited Paper**: [[2025_Stochastic_MPC_Conformal_Hub]]
