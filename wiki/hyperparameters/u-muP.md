---
title: u-µP (Unit-Scaled Maximal Update Parametrization)
type: hyperparameter
category: parametrization
last_updated: 2026-09-01
tags: [hyperparameter, muP, unit-scaling, scaling-laws]
---

# u-µP — Unit-Scaled Maximal Update Parametrization

Combines Maximal Update Parametrization (µP, Yang et al. 2021) with Unit Scaling (Blake et al. 2023) to make optimal learning rate **width-independent**. Hidden weights reparametrized as $W = A_W w$, $w_{t+1}=w_t+C_W\Phi_t$, $A_W\propto1/\sqrt{	ext{fan\_in}}$, $C_W\propto\eta/\sqrt{	ext{fan\_in}}$ (Eq.7). Selected for decoder-only models for simplicity and improved transfer.

## Literature Usage
- [[2026_Khwaja_Toto_2_Scaling_Era]] — First application of µP to time series forecasting. Proxy 10M (L=12,d=256,h=4, d_head=64) tuned via 4-round Optuna TPE (30k steps, WSD schedule), transferred to all 5 targets (4M/22M/313M/1B/2.5B) by scaling d_model/h/L with no retuning; dd_unit_scaling library handles torch.compile/FSDP2/DP-TP, disables unit-scaling in attention for KV-cache compatibility (alpha_res 0.75).
