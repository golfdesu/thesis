---
type: model
name: "Moirai-MoE"
category: model
tags: [model, moirai-moe]
---

# Moirai-MoE

## Overview

Sparse Mixture-of-Experts variant of Moirai (Liu et al. 2024) that routes tokens to experts for capacity scaling.

## Literature Usage

- [[2026_Moirai_2_When_Less_Is_More]] — Mentioned as decoder-only MoE predecessor to Moirai 2.0 (cf. §2 related work); Moirai 2.0 opts for single dense backbone with quantile head instead of MoE.
