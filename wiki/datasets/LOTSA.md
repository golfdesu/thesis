---
type: dataset
name: "LOTSA"
category: dataset
tags: [dataset, pretraining, archive, time-series-foundation-model]
---

# LOTSA (Large-scale Open Time Series Archive)

## Overview
Curated open-access pretraining archive for Time Series Foundation Models introduced by Salesforce AI Research (Woo et al., ICML 2024). Contains **27,646,462,733 (27.6B)** univariate observations (or **231,082,956,489 (231B)** observations when accounting for target variates) across 105 constituent datasets spanning 9 domains in unified Apache Arrow format.

## Domain Distribution
- **Energy**: 30 datasets, 16.36B obs (59.17%) — BuildingsBench, ProEnFo, Monash energy.
- **Transport**: 23 datasets, 4.90B obs (17.73%) — LargeST, LibCity, GluonTS Taxi/Uber.
- **Climate**: 6 datasets, 4.19B obs (15.15%) — ClimateLearn (ERA5, CMIP6), SubseasonalClimateUSA.
- **CloudOps**: 3 datasets, 1.52B obs (5.49%) — Azure VM 2017, Borg 2011, Alibaba 2018.
- **Web**: 3 datasets, 428M obs (1.55%) — Extended Web Traffic, Wiki-Rolling.
- **Sales**: 6 datasets, 198M obs (0.72%) — Favorita, M5, Car Parts, Restaurant.
- **Nature**: 5 datasets, 28.5M obs (0.09%) — Air Quality, Temperature Rain, Saugeen.
- **Econ/Fin**: 23 datasets, 24.9M obs (0.10%) — M1/M3/M4, Tourism, CIF, FRED-MD.
- **Healthcare**: 6 datasets, 1.59M obs (0.01%) — Project Tycho, CDC Fluview, COVID.

## Used-by
- [[2024_Unified_Training_Universal_Time_Series_Transformers]] — Original pretraining dataset for MOIRAI 1.0 (Small 14M, Base 91M, Large 311M).
- [[2026_Moirai_2_When_Less_Is_More]] — Non-leaking pretraining split (GIFT-Eval Pretrain, 230B observations) forms the base corpus for Moirai 2.0.
