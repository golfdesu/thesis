---
type: dataset
name: "CICEVSE2024 EV Charging Station Security Dataset"
location: "Testbed EV charging station (Level 2 EVSE, lab testbed)"
resolution: "5 s (HPC/kernel event sampling)"
access: "on-request"
tags: [dataset, ev-charging]
---

# CICEVSE2024 EV Charging Station Security Dataset

## 📊 Overview
Multi-dimensional cyber-security dataset for EV charging stations (Buedi et al., IFIP DBSec 2024). Real-world testbed with a Level 2 EVSE: **EVSE-A** talks OCPP to a remote CSMS; **EVSE-B** is a Raspberry Pi interfacing the EVCC (ISO 15118) and CSMS. PERF2 collects ~900 kernel/hardware-performance-counter events every 5 s, yielding **8,465 log series**, each recording **907 low-level microarchitecture events**. Preprocessing reduces these to 47 selected features (Pearson correlation filtering, threshold 0.3). **18-class labels**: benign (54.36%), cryptojacking (21.18%), DoS/DDoS floods, scans, MitM-adjacent probes, etc.

## 🔗 Access Links
- "Data will be made available on request" (no public download).
- Reference: Buedi et al., *Enhancing EV charging station security using a multi-dimensional dataset: CICEVSE2024*, IFIP DBSec 2024, pp. 171–190.

## 📚 Used By
- [[2025_Li_Multi_View_Graph_Intrusion_Detection_EV]] — MVGCRL multi-view graph contrastive learning; F1 97.20% (SL) / 97.11% (SSL) vs GNN and classical baselines.
