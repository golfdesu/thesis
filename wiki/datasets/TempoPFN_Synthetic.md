---
type: dataset
name: "TempoPFN Synthetic Time Series"
location: "Synthetic (PFN prior — Moroshan et al. 2025)"
resolution: "4096-step contexts, patch 32"
access: "via Moroshan et al. 2025 - arXiv:2510.25502 (TempoPFN); PFN framework Muller et al. 2022"
tags: [dataset, synthetic, pfn, toto]
---

# TempoPFN Synthetic Time Series

Synthetic series from the TempoPFN prior (Moroshan et al. 2025) built on the Prior-Data Fitted Network (PFN) framework (Muller et al. 2022). Prior is rich with nonstationary trends, abrupt changepoints and long-range dependencies. Hand-crafted prior sampled by a transformer. 2.90T points in Toto 2.0 large mix (57.5%% of 5.04T); nearly 4x Toto 1.0 synthetic.

## Literature Usage
- [[2026_Khwaja_Toto_2_Scaling_Era]] — Second pretraining source (with Datadog observability). Proxy sweep optimum: 57.5%% synthetic / 42.5%% observability (public data excluded entirely for base models).
