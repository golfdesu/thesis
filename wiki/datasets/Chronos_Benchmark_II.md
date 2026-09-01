---
type: dataset
name: "Chronos Benchmark II"
benchmark: true
tasks: 27
tags: [dataset, benchmark, short-history]
---

# Chronos Benchmark II

## Overview
Benchmark from Ansari et al. 2024 (Chronos) — 27 tasks, mostly short histories (<300 steps avg). None included in Chronos-2 training corpus.

## Literature Usage
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — Evaluation (Table 5): WQL W 79.8 S 46.6 and MASE W 81.5 S 26.5 for Chronos-2 (vs TiRex 70.4/41.7, TimesFM-2.5 70.0/42.4, Toto-1.0 60.9/41.9); shows strongest ICL gain on short histories (cross learning compensates limited context, Fig.3c/9c).

## Data Availability
- Ansari et al. 2024 (TMLR).
