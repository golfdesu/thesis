---
type: dataset
name: ChargePlace Scotland EV Charging Sessions
location: Scotland, UK (nationwide; Glasgow case study)
resolution: Session-level transactions (daily counts aggregated in models)
access: open (Transport Scotland open-access portal; exact Zenodo/Git mirrors pending — see warning)
data_type: Public charge-point session logs Oct 2022 – Apr 2025 with charger metadata enrichment
urls:
  - https://www.chargeplace.org.uk/
tags:
  - dataset
  - ev-charging
  - open-data
  - scotland
  - spatio-temporal
---

# 📁 ChargePlace Scotland

## Overview
Open-access public EV **charge-point session data from the ChargePlace Scotland (CPS) network** (Transport Scotland), spanning **October 2022 – April 2025**. Monthly session logs are enriched with charger metadata (CPID → connector specs, postcodes; Davies et al. 2024), community-council boundaries (Open Data Scotland), and meteorological covariates (`riem` package). Positioned explicitly as a **modern replacement for stale legacy benchmarks such as [[Palo_Alto_EV]]** that fail to reflect the scale and behavioral diversity of modern charging networks.

## Curation
Removed zero-duration/zero-kWh sessions (failed handshakes), implausible battery-capacity sessions, overstay-penalty billing artifacts; re-parsed inconsistent DD/MM vs MM/DD dates; dropped systematic reporting-failure windows (Oct 2022, Mar & Jun 2023, early 2024).

## Network-Wide EDA Highlights
- **12 local authorities switched free→paid tariffs** during the window → sharp lasting session declines ([[Electricity_Tariff]] natural experiment): post-tariff −66.1% (AC) vs −46.6% (Rapid); early-2023 structural break.
- Rapid chargers active 83% of days vs 59% AC; weekday>weekend demand (Friday peak, Sunday lowest).

## Central Glasgow Benchmark Subset
| Stat | Value |
|------|-------|
| Neighbourhoods | 18 |
| Charge points (CPIDs) | 96 |
| Days | 879 (Oct 2022–Apr 2025) |
| Total sessions | 104,041 |
| Mean / sd per CPID-day | 2.37 / 2.01 (max 32) |
| AC vs Rapid | 92 (95.8%) vs 4 (4.2%) |

Seven anomalous CPIDs excluded (62201–62203, 62266, 62261, 50433, 62123).

> [!WARNING] Mirror URLs pending
> The paper's extracted text contains only hyperlink placeholders ("Git repository.", "Zenodo repository.") for code/data — no literal URLs appear anywhere. Portal: **chargeplace.org.uk**; exact Zenodo/GitHub mirror URLs must be recovered from the arXiv HTML/PDF source before citing them.

## 📚 Used By
- [[2026_INLA_Spatio_Temporal_EV_Demand]] — Nationwide EDA + Central-Glasgow spatio-temporal case study ([[INLA_Latent_Gaussian_Model]], ICAR/SPDE + RW2); proposed as the modern Scottish open benchmark alongside sibling portals [[Dundee_EV]] and [[Perth_EV]].

## Related Pages
- [[Dundee_EV]]
- [[Perth_EV]]
- [[Palo_Alto_EV]]
- [[Electricity_Tariff]]
