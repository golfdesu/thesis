---
type: model
name: "Sundial"
category: model
tags: [model, sundial]
---

# Sundial

## Overview

Generative flow-matching TSFM (Liu et al. ICML 2025) — decoder-only Transformer with TimeFlow Loss on TimeBench (1T pts); SOTA zero-shot on TSLib/GIFT-Eval/FEV.

## Literature Usage

- [[2025_Chronos_2_Univariate_to_Universal]] — **Sundial (Liu et al. ICML 2025)** univariate baseline beaten: fev-bench W 41.0/S 33.4 vs 90.7/47.3.
- [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]]
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
