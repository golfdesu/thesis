---
title: EV Arrival & Departure Times
type: feature
name: "EV Arrival & Departure Times"
feature: EV Arrival & Departure Times
category: behavioral-feature
data_type: timestamp / probabilistic distribution
last_updated: 2026-08-02
tags: [feature, behavioral, session, arrival, departure]
---

# 🕐 EV Arrival & Departure Times

## Definition

**EV arrival and departure times** are session-level behavioral features capturing *when* an EV connects to and disconnects from a charger. These are critical inputs for models that must predict not just load magnitude but also session-level charging behavior, schedulable capacity, and parking lot occupancy.

## Forms & Representations

| Form | Description | Example Use |
|------|-------------|-------------|
| Raw timestamps | Datetime of plug-in / plug-out | Session-level models |
| Categorical hour bins | Hour-of-day (0–23) as integer | LSTM classification |
| Cyclical encodings | $\sin/\cos(2\pi t / T)$ — see [[Cyclical_Encodings]] | Continuous time encoding |
| Probability distributions | Gaussian/GMM fit of arrival hour distribution | Stochastic queuing models |
| Duration derived | $\Delta t = t_{\text{dep}} - t_{\text{arr}}$ (minutes) | Session duration prediction |

## Role in Key Papers

| Paper | How Arrival/Departure Is Used |
|-------|-------------------------------|
| [[2021_VanKriekinge_Day_Ahead_EV_Demand]] | Sin/Cos cyclical encoding of arrival time; VIANN feature importance |
| [[2014_Alizadeh_Scalable_Stochastic_EV_Demand]] | Arrival rate $\lambda$ and service rate $\mu$ in $M/G/c$ fluid queues |
| [[2021_Zhang_Probabilistic_Queuing_EV_Load]] | $M/M/C/K$ queuing model with driver refusal probability $\alpha_w$ |
| [[2024_Xu_Day_Ahead_EVCB_EVSC_Parking_Lot]] | Arrival/departure window for schedulable capacity domain (EVSFD) |
| [[2025_Li_DC_Charging_Profiles_TFT]] | TFT prediction of session duration as a direct output |
| [[2024_Ke_Divide_Conquer_Transformer_EV]] | Predicts both EV charging event occurrence and session magnitude |

## Citing Literature

- 2020 — [[2020_Huang_Ensemble_EV_Load]] : Transaction start time used as session-level feature for Boulder ensemble forecasting.
- 2026 — [[2026_Huang_Lyapunov_EV_Scheduling]] : Parking time and required charging energy define delay-tolerant scheduling slack (Shanghai arrival data).
- 2025 — [[2026_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] : Arrival/departure timestamps + charging duration log among top engineered features for stacking ensemble.
- 2025 — [[2025_Yang_Stochastic_MPC_Microgrid_EV]] : Stochastic EV arrival/departure times sampled (Latin Hypercube) for scenario-based MPC microgrid dispatch.
- 2026 — [[2026_Tang_PC_M3_Mamba_EV_Clusters]] : Per-EV arrival/departure times + SOC define flexibility clusters in PC-M3 fleet model.

## Stochastic Modeling

Arrival times are often modeled as non-homogeneous Poisson processes:

$$\lambda(t) = \text{time-varying arrival rate (vehicles/hour)}$$

Departure times are modeled as:
$$f(t_{\text{dep}} | t_{\text{arr}}, \text{SOC}) = \text{conditional on charging need and parking constraints}$$

## Behavioral Patterns

- **Workplace charging**: Arrivals concentrated 7–9 AM, departures 4–6 PM.
- **Residential charging**: Arrivals 5–9 PM (post-commute), overnight sessions.
- **Public fast charging**: Short sessions (20–40 min), highly stochastic throughout the day.
- **Weekend vs. weekday**: Significantly different arrival distributions.

## Related Pages

- [[Historical_Load]]
- [[State_of_Charge]]
- [[Cyclical_Encodings]]
- [[Electricity_Tariff]]
