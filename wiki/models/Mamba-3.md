---
type: model
name: "Mamba-3"
category: "State Space Model / Sequence Modeling"
status: verified-2026-08
tags:
  - model
  - mamba-3
---

doi_url: "https://arxiv.org/abs/2603.15569"

## Overview
Third-generation selective state-space sequence model from Lahoti et al. (CMU / Princeton / Together AI / Cartesia), extending [[Mamba_SSM]] (Mamba-2) with three SSM-principled changes:
1. **Exponential-trapezoidal discretization** for a more expressive recurrence,
2. **Complex-valued state update** (RoPE-style parameterization) enabling stronger state tracking,
3. **MIMO formulation** improving decode-time arithmetic intensity without extra latency.

Accepted at ICLR 2026. At 1.5B scale it beats Mamba-2 and Gated DeltaNet on downstream accuracy and matches Mamba-2 perplexity with half the state size.

## Key References
- [[2026_Lahoti_Mamba_3_Sequence_Modeling]] (arXiv:2603.15569, ICLR 2026)
- Code: https://github.com/state-spaces/mamba
