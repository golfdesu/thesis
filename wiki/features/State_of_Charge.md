---
title: State of Charge (SOC)
type: feature
name: "State of Charge (SOC)"
feature: State of Charge (SOC)
category: vehicle-feature
data_type: continuous (0–100%) or (0–1 normalized)
last_updated: 2026-08-02
tags: [feature, SOC, battery, vehicle-level]
---

# 🔋 State of Charge (SOC)

## Definition

**State of Charge (SOC)** represents the remaining energy in an EV battery as a percentage of its total capacity:

$$\text{SOC}(t) = \frac{E_{\text{remaining}}(t)}{E_{\text{capacity}}} \times 100\%$$

SOC is a fundamental variable for EV charging demand modeling because it determines *how much energy* an EV needs to charge, which in turn determines session duration and power draw profile.

## Types

| Type | Description | Use Case |
|------|-------------|----------|
| **Initial SOC** ($\text{SOC}_0$) | Battery level at plug-in | Predicting session energy demand |
| **Target SOC** ($\text{SOC}_{\text{target}}$) | Desired charge level at departure | Scheduling, EVSC computation |
| **SOC trajectory** ($\text{SOC}(t)$) | Real-time SOC during charging | Real-time power profile prediction |
| **SOC at departure** ($\text{SOC}_{\text{dep}}$) | Battery level when unplugging | Evaluating session completion |

## SOC Dynamics

The SOC evolution during charging follows Ampere-Hour (Ah) integration:

$$\text{SOC}(t+1) = \text{SOC}(t) + \frac{\eta_c \cdot P(t) \cdot \Delta t}{E_{\text{capacity}}}$$

where $\eta_c$ is charging efficiency, $P(t)$ is charging power (kW), and $\Delta t$ is the time step.

As used in [[2024_LSTM_Transformer_EV_Consumption]]:
$$\text{SOC}_{t+1} = \text{SOC}_t + \frac{\int I \, dt}{C}$$

## Role in Key Papers

| Paper | How SOC Is Used |
|-------|----------------|
| [[2024_LSTM_Transformer_EV_Consumption]] | LSTM-Transformer predicts real-time SOC trajectory; 3D K-Means driving clustering |
| [[2024_Day_Ahead_EVCB_EVSC_Parking_Lot]] | Initial SOC and target SOC define the EV Scheduling Feasible Domain (EVSFD) |
| [[2021_Probabilistic_Queuing_EV_Load]] | SOC determines energy demand per session in queuing model |
| [[2025_Stochastic_MPC_Microgrid_EV]] | SOC state variable in individual EV battery dynamics for MPC dispatch |
| [[2024_V2G_SVE_Evaluation_Metric]] | SOC bounds constrain V2G fleet dispatch feasibility |

## Citing Literature

- 2021 — [[2021_RL_Q_Learning_EV_Load]] : SOC, battery capacity, depth-of-discharge and daily driven miles parameterize the RL charging model.
- 2025 — [[2025_DC_Charging_Profiles_TFT]] : Starting SOC is a key TFT input for DC fast-charging session profile prediction (NW Europe DCFC + ERA5 data).
- 2026 — [[2026_PC_M3_Mamba_EV_Clusters]] : SOC at arrival/departure defines per-EV energy requirement and flexibility polytopes in PC-M3 fleet clustering.

## Practical Challenges

- **Not directly observed**: Most public charging stations do not record SOC; it must be inferred from session energy and vehicle specifications.
- **Vehicle heterogeneity**: Different vehicle models have different capacities, efficiencies, and charging curves.
- **Estimation error**: SOC sensors have ±2–5% uncertainty; Ah integration accumulates error over time.
- **Privacy**: Some operators consider SOC data commercially sensitive.

## Datasets with SOC Data

- [[Caltech_ACN]] — Includes estimated SOC and requested energy for workplace charging sessions.
- [[Pecan_Street]] — Indirect SOC inference from residential charging power draw.

## Related Pages

- [[Historical_Load]]
- [[Arrival_Departure_Time]]
- [[Electricity_Tariff]]
- [[EVSFD]]
