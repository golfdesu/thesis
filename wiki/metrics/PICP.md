---
metric: Prediction Interval Coverage Probability (PICP)
category: probabilistic-forecast-metric
formula: "PICP = (1/N) Σ 1{y_i ∈ [L_i, U_i]}"
unit: Percentage (%)
last_updated: 2026-08-23
tags: [metric, picp, coverage, prediction-interval, probabilistic-forecast]
---

# 📐 Prediction Interval Coverage Probability (PICP)

## Definition

**PICP** measures the empirical fraction of observations falling inside the predicted intervals:

$$\text{PICP} = \frac{1}{N}\sum_{i=1}^{N} \varepsilon_i, \quad \varepsilon_i = \begin{cases}1 & y_i \in [L_{i}, U_{i}]\\ 0 & \text{else}\end{cases}$$

It should match the nominal coverage (PINC); deviations are quantified by the **Average Coverage Error** $\text{ACE} = \text{PICP} - \text{PINC}$.

## Properties

| Property | Description |
|----------|-------------|
| **Unit** | Percentage (%) |
| **Higher is better** | ⚠️ Only up to the nominal level — trivially maximized by huge intervals |
| **Must pair with sharpness** | ✅ Report with interval width ([[AIW]]), [[Interval_Sharpness]], or [[Winkler_Score]] |
| **Conformal variant** | Distribution-free finite-sample guarantees via [[Conformal_Prediction]] / ICP; joint trajectory-level coverage needs Bonferroni correction |

## Usage in EV / Load Forecasting Papers

| Paper | Result |
|-------|--------|
| 2021 — [[2021_Zhang_Probabilistic_Queuing_EV_Load]] | CNN seasonal PICPs of 95.49%/95.24%/95.47%/95.24% at PINC 95%; ACE < 1% (~half of QR benchmark's 3.89%). |
| 2024 — [[2024_Ali_MQ_TCN_Transfer_Learning_EV]] | MQ-TCN PICP **93.62%** at JPL (+28.93% over XGBoost); **96.88%** at NREL with only 2 weeks of transfer data. |
| 2025 — [[2025_Matrone_QR_LSTM_Attention_EV_Load]] | QR-LSTM-Attention raised PICP to **78.60%** vs persistence 51.78% (+26.82 pp). |
| Related coverage metrics | [[2024_Zhou_Conformal_Prediction_DER]] (Coverage_Rate + Interval_Size for hierarchical DER conformal sets); [[2021_Stankeviciute_Conformal_Time_Series_Forecasting]] (**joint** trajectory coverage: CF-RNN 90.6–94.6% vs MQ-RNN ~57–67% at 90% target). |
| 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] | Raw TFT quantile intervals overconfident (PICP 64.47% at 80% nominal); after CQR conformal calibration **PICP = 96.2%** with NPIW ≈ 0.74 — conservative but sharp relative to σ_y. |
| 2026 — [[2026_Singh_MetaLearning_Informer_Probabilistic_EV]] | MAML-Informer PICP ≈100% on ACN (99.82%) with narrow MPIW ≈0.148–0.164 kWh; ~17% PICP rise vs baselines. |
| 2023 — [[2023_Wen_DiffSTG_Probabilistic_ST_Graph_Diffusion]] | Diffusion samplers like DiffSTG emit full predictive samples (S trajectories per node-step) evaluated via [[CRPS]]/RMSE rather than PICP — interval coverage is unreported; PICP for such models requires post-hoc sample-to-quantile extraction (e.g., S ≥ 32 samples before gains plateau). |
| 2024 — [[2024_Shi_Naihao_Prediction_Interval_EV_Loads]] | GPR feeder forecasts with EV charging-habit feature CH(t): CI-95% PICP improves 84.6% → **93.8%** (ideal 95%) vs 84.6% without CH(t); CI-68% reaches 73.6% vs ideal 68, with far shorter intervals ([[NMPIL]]) than the EV-loaded no-CH case. |
| 2025 — [[2025_FernandezZapico_Stochastic_MPC_Conformal_Hub]] | EnbPI conformal intervals (α=0.1): EV/PV coverage ≈ **0.90/0.91** but price coverage collapses to **0.60 overall (0.22 Autumn)** under the 2021 gas-price regime shift — static calibration fails under drift; contrast [[2026_Yu_EnergyMamba_Graph_Mamba_ASCQR]], whose AS-CQR targets exactly this failure mode via online feedback with a long-run coverage guarantee. |

> [!WARNING]
> High PICP alone is meaningless without sharpness: e.g., high NREL Winkler Scores despite 96.88% PICP revealed over-wide intervals ([[2024_Ali_MQ_TCN_Transfer_Learning_EV]]).

## Related Pages

- [[Winkler_Score]]
- [[CRPS]]
- [[Pinball_Loss]]
