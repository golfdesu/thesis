---
dataset: ElaadNL Dataset
source: ElaadNL (Dutch National EV Charging Infrastructure Foundation)
location: Netherlands
charger_type: Public Level 2 AC
stations: "~3,000+ public charging points"
time_period: "2012–present"
resolution: Session-level and 15-minute aggregated
last_updated: 2026-08-02
url: "https://platform.elaad.io/analyses/ElaadNL_opendata.php"
website: "https://www.elaad.nl"
tags: [dataset, public-charging, netherlands, hierarchical, elaadnl]
name: "ElaadNL Dataset"
access: "open data dashboard / research request"
license: "Free to use and share per ElaadNL Open Data Dashboard statement; no formal license document"
commercial_use: allowed
data_type: "Public EV charging sessions (kWh, max power, connector type) + derived 15-min station load"
---

# 📁 ElaadNL Dataset

## 🔗 Access Links & Repositories
- **ElaadNL Open Data Portal**: [https://platform.elaad.io/analyses/ElaadNL_opendata.php](https://platform.elaad.io/analyses/ElaadNL_opendata.php)
- **ElaadNL Official Website**: [https://www.elaad.nl](https://www.elaad.nl)

## Overview

The **ElaadNL dataset** is a large-scale public EV charging dataset from the **Netherlands** collected by ElaadNL, the national knowledge and innovation center for EV charging infrastructure in the Netherlands. It covers thousands of public Level 2 charging points across the Dutch national charging network, making it one of the largest and most geographically diverse public EV charging datasets in Europe.

## Key Statistics

| Attribute | Value |
|-----------|-------|
| Location | Netherlands (nationwide) |
| Charging Points | 3,000+ public AC charging points |
| Charger Type | Public Level 2 AC (3.7 kW and 11 kW) |
| Temporal Resolution | Session-level + 15-minute aggregated time series |
| Data Period | 2013–present |
| Network Topology | Hierarchical (city → district → charging point) |
| Access | Research partnership / request-based |

## Available Features

- Session start/end timestamps
- Energy delivered per session (kWh)
- Maximum power per session (kW)
- Station ID, geographic coordinates
- Connector type (Type 2)
- Anonymized user/card ID
- 15-minute aggregated load per station (derived)

## Unique Advantages

- **Hierarchical structure**: Data naturally organized at city, district, and station levels — ideal for hierarchical probabilistic forecasting research.
- **Large geographic coverage**: Hundreds of cities across the Netherlands.
- **Long history**: 10+ years of data captures EV adoption growth curves.
- **Network-level data**: Can construct realistic spatial graphs for GNN models.

## Limitations

- **No vehicle-level data**: No SOC, vehicle model, or user behavior attributes.
- **Dominated by overnight sessions**: Dutch public charging patterns differ from US workplace/fast-charging.
- **Access complexity**: Requires formal data-sharing agreement with ElaadNL.
- **Level 2 only**: No DC fast charging sessions in the primary dataset.

## Papers Using This Dataset

| Paper | How Used |
|-------|----------|
| [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]] | Hierarchical probabilistic forecasting across the ElaadNL network (EVnetNL open data) |
| [[2023_Huang_MetaProbformer_EV_Load]] | One of four meta-learning benchmark stations (with Palo Alto, Boulder, Perth) |
| [[2026_Tang_PC_M3_Mamba_EV_Clusters]] | Charging-behavior priors for physics-constrained Mamba cluster EM |
| [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] | EVnetNL open data as primary USDT benchmark (12 months, 8760 hourly points): RMSE 8.781 vs Informer 9.866; zero-shot transfer source |

> [!WARNING] Corrected 2026-08-23: [[2025_Matrone_QR_LSTM_Attention_EV_Load]] was previously listed here in error — it uses the [[Utrecht_SmoothEMS]] office parking-lot data, not ElaadNL.

## Relevance to Hierarchical Forecasting

> [!TIP]
> ElaadNL is the primary benchmark for **hierarchical probabilistic EV load forecasting** research. The natural city→district→station hierarchy makes it ideal for testing coherent reconciliation methods like PICNN ([[2025_Zheng_Coherent_Hierarchical_EV_Load]]) and conformal prediction ([[2024_Zhou_Conformal_Prediction_DER]]).

## Related Pages

- [[Caltech_ACN]]
- [[Boulder_Colorado]]
- [[Pecan_Street]]
- [[Spatial_Temporal_Forecasting]]
- [[2021_Buzna_Hierarchical_Probabilistic_EV_Load]]
