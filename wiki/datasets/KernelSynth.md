---
type: dataset
name: "KernelSynth"
category: dataset
tags: [dataset, synthetic, gps]
---

# KernelSynth

## Overview

Synthetic time series generated via Gaussian processes with kernel bank (trend, local change, seasonalities) combined by +/x (Ansari et al. 2024, Chronos).

## Specs

- Size: 1M time series, 1.02B observations (as used in Moirai 2.0 pretrain, §4)
- Generation: Sample kernels from bank, combine with random binary operations
- Availability: Via Chronos/KernelSynth release (Ansari et al. 2024)

## Used-by

- [[2026_Moirai_2_When_Less_Is_More]] — Synthetic augmentation in Moirai 2.0 pretraining corpus (36M/295B total): 1M/1.02B from KernelSynth alongside GIFT-Eval Pretrain (3.25M/230B), GIFT-Eval TrainTest (144K), Chronos-Mixup (30M/63B), and internal Salesforce telemetry (2.15M/1.48B). Contributes to "new corpus" vs GIFT-Eval Pretrain-only ablations (Table 2 v0->v1).

## 📚 Literature Usage
- [[2026_TiRex_2_Multivariate_Streaming_Forecasting]] — Evaluated on multivariate zero-shot forecasting benchmark with past and future covariates.
- [[2026_FlowState_Sampling_Rate_Equivariant_Forecasting]] — Evaluated on zero-shot multi-frequency benchmarks within GIFT-Eval test suite.
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Generates 15 million synthetic time series using Gaussian Process kernel combinations (RBF, Periodic, Linear, Rational Quadratic, Piecewise Polynomial) with continuous periodicity sampling.
