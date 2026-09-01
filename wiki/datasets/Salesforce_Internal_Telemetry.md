---
type: dataset
name: "Salesforce Internal Telemetry"
category: dataset
tags: [dataset, proprietary, cloudops]
---

# Salesforce Internal Telemetry

## Overview

Proprietary univariate daily time series from Salesforce CloudOps telemetry (internal, not publicly distributable).

## Specs

- Size: ~2.15M univariate series, ~1.48B observations at daily granularity (as used in Moirai 2.0, §4)
- Period: ~1 year from Jan 2024
- Preprocessing: Filtered heavy-missing series prior to training
- Availability: Proprietary — not distributable; only described in Moirai 2.0 technical report

## Used-by

- [[2026_Moirai_2_When_Less_Is_More]] — Core pretraining source for Moirai 2.0 (part of 36M/295B corpus): ~2.15M/1.48B daily series alongside GIFT-Eval Pretrain, GIFT-Eval TrainTest, Chronos-Mixup, and KernelSynth. Represents cloud/observability domain; filtered for missingness (p. 6 §4).
