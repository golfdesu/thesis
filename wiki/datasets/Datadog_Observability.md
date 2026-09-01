---
type: dataset
name: "Datadog Internal Observability Metrics"
location: "Datadog internal telemetry (CPU, memory, latency, error rates etc.)"
resolution: "10s (47.1%% within subset) / 60s (17.6%%) / 5m+ (35.3%%)"
access: "private (Datadog internal; no customer data used)"
tags: [dataset, observability, private, toto]
---

# Datadog Internal Observability Metrics

Real-world telemetry from Datadog internal infrastructure: CPU utilization, memory usage, request latency, error rates and similar signals. Used exclusively (with synthetic) for Toto 2.0 base pretraining — **no public time series**. Rebalanced from Toto 1.0 (10s was 78.5%%) toward longer intervals (5m+ 35.3%%). 2.14T points in large mix (42.5%% of 5.04T).

## Literature Usage
- [[2026_Toto_2_Scaling_Era]] — Core pretraining source (with TempoPFN synthetic). Base models see only this + synthetic; still leads public benchmarks (cross-domain generalization test).
