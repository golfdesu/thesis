---
type: dataset
name: "TimeBench"
location: "Multi-domain (Chronos, LOTSA, ERA5, ECG, Finance, IoT + Synthetic)"
time_points: "1,032B (1 trillion)"
period: "Various (up to 2024)"
tags: [dataset, pretraining-corpus, time-series, foundation-model]
---

# TimeBench

Trillion-scale pretraining corpus for Sundial (Liu et al. ICML 2025) — 1,032B time points across 12 sources (Chronos 94B, LOTSA 230B, ERA5 3h/daily/weekly/monthly/quarterly, ECG, Finance, IoT, 0.5B synthetic via KernelSynth). Dominant source ERA5 Daily (406B, 39.35%). Excludes all evaluation datasets to ensure zero-shot.

| Source | Points | Share |
|---|---|---|
| Chronos | 94B | 9.11% |
| ECG | 48B | 4.65% |
| Finance | 10.5B | 1.02% |
| IoT | 5.8B | 0.56% |
| LOTSA | 230B | 22.29% |
| Synthetic | 0.5B | 0.05% |
| ERA5 3h | 129B | 12.50% |
| ERA5 12h | 32B | 3.10% |
| ERA5 Daily | 406B | 39.35% |
| ERA5 Weekly | 58B | 5.62% |
| ERA5 Monthly | 13.5B | 1.31% |
| ERA5 Quarterly | 4.5B | 0.44% |

- **Code / Weights**: https://github.com/thuml/Sundial · https://huggingface.co/thuml/sundial-base-128m
- **Paper**: [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]]

## Literature Usage

- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — Pretraining corpus for Sundial family (Small 32M / Base 128M / Large 444M); enables SOTA zero-shot on TSLib, GIFT-Eval, FEV.

## Related Pages

- [[GIFT-Eval]]
- [[Chronos_Corpus]]
- [[Electricity_ECL]]
