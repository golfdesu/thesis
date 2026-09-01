---
type: dataset
name: "BOOM (Observability Benchmark)"
location: "Datadog internal observability metrics"
resolution: "10s / 60s / 5m+ (rebalanced in Toto 2.0)"
access: "via Cohen et al. 2025 - https://arxiv.org/abs/2510.00000 (BOOM paper)"
tags: [dataset, benchmark, observability, toto]
---

# BOOM — Observability Benchmark

Introduced in Cohen et al. (2025) *This time is different*. Evaluates forecasting on **Datadog observability metrics** (CPU utilization, memory, request latency, error rates). Context 2048. Metrics: CRPS rank / CRPS / MASE.

## Literature Usage
- [[2026_Khwaja_Toto_2_Scaling_Era]] — Primary benchmark. All 5 Toto 2.0 sizes on Pareto frontier: CRPS ranks 3.88 (2.5B) / 3.96 (1B) / 4.26 (313M) / 5.53 (22M) / 7.17 (4M) vs Toto 1.0 6.94, Chronos-2 7.39. 22M matches Toto 1.0 with 7x fewer params; 4M competitive with Chronos-2 at 38x smaller.
