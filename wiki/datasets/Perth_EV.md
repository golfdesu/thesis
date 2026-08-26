---
type: dataset
name: Perth & Kinross EV Charging Dataset
location: Perth, Scotland / UK
resolution: Session-level transactions (hourly/15-min aggregates derived in papers)
access: open
data_type: Public EV charging station load time series
url: "https://data.pkc.gov.uk/dataset/ev-charging-data"
tags:
  - dataset
  - ev-charging
  - perth
  - open-data
---

# 📁 Perth & Kinross EV Charging Dataset

## 🔗 Access Links & Repositories
- **Perth & Kinross Open Data (verified 2026-08-23)**: [EV Charging Data](https://data.pkc.gov.uk/dataset/ev-charging-data)
- **ChargePlace Scotland feed** (source of the underlying session records; used by Ullah et al. 2026)
- **4-city preprocessed benchmark repo**: [github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand](https://github.com/fbohu/Deep-Spatio-Temporal-Forecasting-of-Electrical-Vehicle-Charging-Demand)

## Overview
Public EV charging station dataset from Perth & Kinross (Scotland, UK) capturing multi-station spatio-temporal charging demand.

## 📚 Used By
- [[2023_Huang_MetaProbformer_EV_Load]] — Few-shot MetaProbformer evaluation (Perth as one of 4 benchmark stations).
- [[2025_Tian_MSSTGAN_City_EV_Load]] — MS-STGAN spatio-temporal graph evaluation.
- [[2026_Ullah_Decomposition_Stacked_Meta_Learning_EV_Load]] — Stacked meta-learning benchmark via ChargePlace Scotland data.
- [[2026_Wang_Shengyou_ML_Geographical_Transferability_EV]] — Perth one of 12 cities in the ML/DL transferability benchmark (6 stations, 29.4 events/day/station; plus 7 Perthshire towns Crieff/Aberfeldy/Pitlochry/Kinross/Auchterarder/Blairgowrie/Dunkeld).
- [[2026_Zhang_Jinlai_DualDirection_Transformer_EV_Charging]] — USDT probabilistic forecasting on 4 months / 2953 hourly points (RMSE 13.837 vs Informer 14.319); also zero-shot cross-domain target.
- [[2026_Kyriakopoulos_ML_Comparison_EV_Charging_Forecasting]] — One of four cities (36 stations, 66,664 sessions, Jan 2016–Dec 2019); LSTM best everywhere short-term (station MAE 0.43–0.46), GRU lowest MAE at all mid/long-term levels (city MAE 8.17→6.54).
- [[2026_Bouaachra_INLA_Spatio_Temporal_EV_Demand]] — Sibling Scottish dataset: the ChargePlace Scotland corpus (Oct 2022–Apr 2025, incl. Perth & Kinross territory) extends Perth's records into the 2022–2025 era with tariff-break annotations; see [[ChargePlace_Scotland]].
