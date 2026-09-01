---
title: Warmup-Stable-Decay (WSD) Learning Rate Schedule
type: hyperparameter
category: schedule
last_updated: 2026-09-01
tags: [hyperparameter, schedule, wsd]
---

# Warmup-Stable-Decay (WSD) Schedule

Learning-rate schedule with warmup → stable → decay phases (Hu et al. 2024, MiniCPM). Enables proxy tuning on stable phase then short decay tail.

## Literature Usage
- [[2026_Khwaja_Toto_2_Scaling_Era]] — Proxy trains 30k steps under WSD; R4 sweep finds optimal linear decay over 10.5k steps (1.7-2.6% of 400k-600.5k total); same 10.5k decay used for all 5 target models; warmup 6k, clip 7.0.
