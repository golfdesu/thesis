---
type: dataset
name: "TIME Benchmark"
location: "50 fresh datasets (never/rarely benchmarked), 98 tasks"
resolution: "Per-task prescribed context/horizon (operational requirements)"
access: "via Qiao et al. 2026 - arXiv:2602.12147"
tags: [dataset, benchmark, time, contamination-resistant]
---

# TIME — Towards the Next Generation of Time Series Forecasting Benchmarks

98 tasks from 50 *fresh* datasets curated human-in-the-loop (Qiao et al. 2026). Deliberately avoids legacy ETTh1/Electricity/Traffic/Weather to mitigate pretraining contamination; horizons aligned to operational requirements. Per-task prescribed context lengths. Metrics: CRPS rank / MASE rank / CRPS / MASE.

## Literature Usage
- [[2026_Toto_2_Scaling_Era]] — Toto 2.0 sweeps top-3 on every metric: CRPS ranks 3.43 (2.5B) / 3.51 (313M) / 3.86 (1B); MASE ranks 3.54/3.65/3.71; CRPS 0.532/0.535/0.537. Only scaling inversion in family (313M edges 1B on ranks). 4M still beats Toto 1.0.
