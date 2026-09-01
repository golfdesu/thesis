---
title: Unit Scaling
type: hyperparameter
category: parametrization
last_updated: 2026-09-01
tags: [hyperparameter, unit-scaling, low-precision]
---

# Unit Scaling

Technique (Blake et al. 2023) maintaining unit variance through network operations for stable low-precision training. Combined with µP as **u-µP** for hyperparameter transfer.

## Literature Usage
- [[2026_Toto_2_Scaling_Era]] — Unit-scaled variant chosen for Toto 2.0 (simplicity, better decoder-only transfer); unit-scaling disabled in attention/MLP activations to preserve KV-cache ($lpha_{	ext{res-attn-ratio}}=\sqrt{S/\log S}$ fix).
