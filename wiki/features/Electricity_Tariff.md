---
title: Electricity Tariff & Time-of-Use (TOU) Pricing
type: feature
name: "Electricity Tariff & Time-of-Use (TOU) Pricing"
feature: Electricity Tariff & Time-of-Use (TOU) Pricing
category: economic-feature
data_type: continuous ($/kWh) or categorical (peak/off-peak/shoulder)
last_updated: 2026-08-02
tags: [feature, pricing, TOU, electricity-tariff, demand-response]
---

# 💰 Electricity Tariff & Time-of-Use (TOU) Pricing

## Definition

**Electricity tariff** and **Time-of-Use (TOU) pricing** signals represent the time-varying cost of electricity, which directly influences EV user charging behavior. Under TOU pricing, users face higher prices during peak demand hours and lower prices during off-peak periods — creating incentives to shift charging demand.

## Types of Pricing Signals

| Type | Description | Forecasting Impact |
|------|-------------|-------------------|
| **Flat rate** | Constant $/kWh regardless of time | Minimal behavioral response |
| **TOU pricing** | Fixed peak/off-peak tiers (e.g., 2–3 rate periods per day) | Users shift charging to off-peak windows |
| **Real-Time Pricing (RTP)** | Hourly market price (e.g., day-ahead LMP) | High price elasticity; complex modeling |
| **Critical Peak Pricing (CPP)** | Extreme prices during grid stress events | Demand response activation |
| **Dynamic pricing** | Algorithm-driven real-time price optimization | Smart charging coordination |

## Price Elasticity & Causal Modeling Challenge

> [!WARNING]
> **Price Misinterpretation Problem**: Standard deep learning models (LSTM, Transformer) learn *spurious positive correlations* between price and demand — because high prices occur during peak hours when demand is already high. This is not causal.
>
> [[2024_Qu_Physics_Informed_GAT_EV_Load]] (PAG) addresses this with PIML pseudo-sampling to enforce correct *negative* price elasticity: higher price → lower demand.

The correct causal relationship is:

$$\frac{\partial D}{\partial P} < 0 \quad \text{(demand decreases as price increases)}$$

## Role in Key Papers

| Paper | How Tariff/TOU Is Used |
|-------|------------------------|
| [[2024_Xu_Day_Ahead_EVCB_EVSC_Parking_Lot]] | TOU K-Means++ clustering of user behavior by price period |
| [[2024_Qu_Physics_Informed_GAT_EV_Load]] | PIML pseudo-sampling to correct spurious price elasticity in GAT |
| [[2021_Dabbaghjamanesh_RL_Q_Learning_EV_Load]] | TOU signals as part of RL state space for model selection |
| [[2024_Bampos_EV_Load_Forecasting_DAM]] | Day-ahead market (DAM) price as target variable input |
| [[2025_Khan_Transformer_BiLSTM_Price_Forecasting]] | Electricity market price is the *target* to forecast (NYISO, PJM, MISO) |

## Citing Literature (Electricity Price as Input Feature)

- 2015 — [[2015_Raza_Review_AI_Load_Demand]] : Review lists electricity price among standard exogenous inputs for AI load forecasting.
- 2019 — [[2019_Toubeau_Deep_Probabilistic_Scheduling_Power_Markets]] : Market prices jointly forecast with load/wind/solar via probabilistic BLSTMs for scheduling.
- 2026 — [[2026_Huang_Lyapunov_EV_Scheduling]] : CAISO real-time prices drive Lyapunov-based online EV charging scheduling cost.
- 2024 — [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] : TOU electricity price reweighted by Pearson correlation prior in FEDM feature-enhanced network.
- 2024 — [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] : Charging price included in multigraph node features for Beijing fast-charging stations.
- 2024 — [[2024_Zhou_Conformal_Prediction_DER]] : Price signals among feeder-level covariates for conformal DER adoption forecasting.
- 2025 — [[2025_Alghamdi_REST_Network_Port_EV]] : Grid demand/price context in RESTNet port EV charging ensemble (custom cost metrics CPE).
- 2025 — [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] : Price + weather + POI context encoded in EV-STLLM spatio-temporal LLM inputs.
- 2025 — [[2025_Han_Vertical_Federated_EGAT_LSTM]] : Grid-side features (voltage, power flows, congestion rate) shared via vertical federated EGAT-LSTM.
- 2025 — [[2025_Yang_Stochastic_MPC_Microgrid_EV]] : Price + wind/solar forecasts feed stochastic MPC operating-cost minimization for microgrid EV dispatch.
- 2025 — [[2025_Zheng_BWO_ICEEMDAN_iTransformer]] : Price series decomposed by ICEEMDAN and forecast with BWO-tuned iTransformer (Singapore market).
- 2026 — [[2026_Hao_Mamba_KAN_HyKANet_EV]] : External encoding includes price/weather; removing it degrades MAPE by +35.7% relative.
- 2026 — [[2026_Wang_Xiaoping_TriModal_Causal_EV_Demand]] : Electricity price elevated to a core modeling modality in TriCast's PEM module (random-walk-smoothed, behavior-modulated price with elasticity gating) on UrbanEV Shenzhen; only 57/247 zones have dynamic pricing.
- 2024 — [[2024_Li_TOU_Price_Meteorology_EV_Charging_Load]] : TOU price tops Pearson/MIC factor screening (r = 0.7259, MIC = 0.5946) as a CNN-GRU input at a Chinese mall station; users shift charging into off-peak windows (peak 1.1526 / flat 0.6703 / off-peak 0.2805 Yuan/kWh).
- 2026 — [[2026_Bouaachra_INLA_Spatio_Temporal_EV_Demand]] : Free→paid tariff introduction at 12 Scottish local authorities caused sharp lasting session drops (−66% AC / −47% rapid) with an early-2023 structural break cleanly absorbed by the RW2 latent trend — a natural experiment in price elasticity (AC more price-sensitive than Rapid).

## Feature Engineering

- **Binary peak indicator**: $\mathbb{1}[\text{peak hour}] \in \{0, 1\}$
- **Normalized price**: $(P_t - P_{\min}) / (P_{\max} - P_{\min})$
- **Price lag features**: $P_{t-1}, P_{t-24}$ (previous day same hour)
- **Price forecast integration**: Use day-ahead price forecast as exogenous input
- **TOU cluster labels**: K-Means++ cluster assignment based on price profile shape

## Related Pages

- [[Historical_Load]]
- [[Arrival_Departure_Time]]
- [[State_of_Charge]]
- [[Weather_Traffic]]
- [[PAG]]
- [[EVSFD]]
