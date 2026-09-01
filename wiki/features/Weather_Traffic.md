---
title: Weather & Traffic Conditions
type: feature
name: "Weather & Traffic Conditions"
feature: Weather & Traffic Conditions
category: external-contextual-feature
data_type: continuous (temperature °C, precipitation mm, wind speed m/s) + categorical (traffic density)
last_updated: 2026-08-02
tags: [feature, weather, traffic, contextual, external]
---

# 🌤️ Weather & Traffic Conditions

## Definition

**Weather and traffic conditions** are external contextual features that influence EV charging demand but are not directly controlled by the station operator. Weather affects EV range (battery performance degrades in cold/hot temperatures), driving patterns, and the likelihood of charging. Traffic conditions affect EV arrival rates at stations.

## Weather Features

| Feature | Unit | Impact on EV Demand |
|---------|------|---------------------|
| **Temperature** | °C | Cold reduces battery range → increases charging frequency; heat increases HVAC load |
| **Precipitation** | mm/hour | Rain/snow reduces driving → lower demand; affects travel patterns |
| **Wind speed** | m/s | Affects aerodynamic drag → range anxiety during high winds |
| **Solar irradiance** | W/m² | Relevant for solar-integrated V2G and solar-EV coordination |
| **Humidity** | % | Secondary effect on battery chemistry |
| **Visibility** | km | Affects driving safety and willingness to travel |

## Traffic Features

| Feature | Description | Impact |
|---------|-------------|--------|
| **Traffic volume** | Vehicles/hour on nearby roads | Proxy for EV arrival rate at stations |
| **Traffic density** | Vehicles/km | Congestion increases charging session probability |
| **Road segment speed** | km/hour | Indicates congestion level |
| **Point of Interest (POI) proximity** | Distance to shopping, office, etc. | Explains station utilization patterns |

## Role in Key Papers

| Paper | Weather/Traffic Features Used |
|-------|-------------------------------|
| [[2021_VanKriekinge_Day_Ahead_EV_Demand]] | Temperature, precipitation — LOFO feature importance analysis |
| [[2025_Hussain_CAT_Former_Short_Term_EV]] | Contextual vector: $X_{\text{context}} = [S_{\text{lat}}, S_{\text{long}}, W_{\text{temp}}, W_{\text{precip}}, W_{\text{wind}}]$ |
| [[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]] | Weather included in Pearson correlation prior feature reweighting |
| [[2024_Qu_Physics_Informed_GAT_EV_Load]] | Traffic volume as part of spatial-temporal graph features |
| [[2025_Tian_MSSTGAN_City_EV_Load]] | Spatial traffic density as graph node feature in MSSTGAN |
| [[2025_Fan_EV_STLLM_Spatio_Temporal_LLM]] | Weather and POI context encoded in EV-STLLM spatio-temporal LLM |

## Citing Literature

- 2001 — [[2001_Hippert_Neural_Networks_STLF_Review]] : Canonical review of temperature/humidity as the dominant weather inputs in ANN-based STLF.
- 2015 — [[2015_Raza_Review_AI_Load_Demand]] : Catalogues dry-bulb temperature, dew point and relative humidity among standard AI forecasting inputs.
- 2017 — [[2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load]] : Lagged temperature and daily moving-average temperature drive sister point forecasts later combined by QRA.
- 2021 — [[2021_Zhang_Probabilistic_Queuing_EV_Load]] : M42 motorway traffic flow + wavelet decomposition feed probabilistic queuing EV load model.
- 2022 — [[2022_Cao_Robust_Deep_Gaussian_Process_Load]] : Cloud cover, precipitation, air pressure + Google/Apple mobility indices for COVID-era city load.
- 2023 — [[2023_Koohfar_Transformer_EV_Demand]] : NOAA-derived temperature max/min, snowfall and precipitation as Transformer exogenous features.
- 2023 — [[2023_Ziyabari_Multi_Branch_ResTrans_Solar]] : Full NSRDB meteorological suite (GHI/DNI/DHI, wind, pressure, solar zenith) in multi-branch ResTrans.
- 2024 — [[2024_Shi_Attention_Spatiotemporal_MultiGraph_EV_Load]] : Temperature/humidity/wind-speed node features in attention multigraph network (Beijing).
- 2025 — [[2026_Mansour_Hybrid_XGBoost_BiLSTM_EV_Load]] : Adding synthetic temperature/humidity and retraining only the meta-learner improved cross-site MAE from 4.16 → **2.94 kWh** (29.3%).
- 2025 — [[2025_Han_Vertical_Federated_EGAT_LSTM]] : Traffic flow as vertically-held private feature fused with grid-side data via federated EGAT-LSTM.
- 2026 — [[2026_Romia_CNN_LSTM_Attention_Fast_Charging]] : Temperature/humidity/wind speed + NREL SAM irradiance features for DC fast-charging forecasting.
- 2026 — [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] : Open-Meteo temperature/rainfall/solar radiation as TFT known future inputs; VSN flags them as comparatively low-importance vs temporal features on Palo Alto data.
- 2026 — [[2026_Wang_Xu_Similar_Day_Selection_EV_Load]] : 6-D weather state vectors (temperature, station/sea-level pressure, humidity, rainfall intensity, dew point) aligned across days via Multi-DTW for similar-day matching.
- 2024 — [[2024_Li_TOU_Price_Meteorology_EV_Charging_Load]] : Temperature retained after Pearson/MIC screening (Pearson 0.4738, MIC 0.5698) while rain/wind rejected (MIC < 0.22) — screened meteorological factors spliced into CNN-GRU inputs.
- 2024 — [[2024_Qu_Forwardformer_Day_Ahead_Load]] : Weather information embeddings (max/min temperature + pressure/humidity on CEL; wet-bulb temperature on AEL) injected in Decoder-2 to correct the predicted day's load across five China/US datasets.
- 2026 — [[2026_Hong_SSM_Transformer_LSTM_Grid_Benchmark]] : Grid-level hourly weather-covariate reversal finding — thermal-lag-aligned temperature/humidity/wind/GHI/cloud features invert the load-only model ranking (iTransformer gains 3× more MAPE than PatchTST; SSMs win 5/7 grids); caveat: reanalysis weather, not operational NWP forecasts.

## Feature Engineering Approaches

- **Forecast-integrated**: Use NWP (Numerical Weather Prediction) forecast for next 24–48 hours as exogenous input (standard for day-ahead models).
- **Lag features**: $T_{t-1}, T_{t-24}$ (temperature 1-step and 1-day ago).
- **Interaction features**: Temperature × Historical Load (heat wave effect).
- **Location embedding**: $[S_{\text{lat}}, S_{\text{long}}]$ as geographic context vector (CAT-Former).
- **Pearson pre-filtering**: Only include weather features with statistically significant correlation to load ([[2024_Cao_Feature_Enhanced_Probabilistic_EV_Load]]).

## Key Insight: Context-Aware Architecture

> [!TIP]
> [[2025_Hussain_CAT_Former_Short_Term_EV]] demonstrates that fusing weather and location context as a **separate contextual vector** (rather than concatenating with the temporal sequence) improves model performance. The CAT-Former architecture uses cross-attention between temporal and contextual streams.

## Related Pages

- [[Historical_Load]]
- [[Cyclical_Encodings]]
- [[Arrival_Departure_Time]]
- [[Electricity_Tariff]]
- [[CAT_Former]]
