---
type: model
name: Mamba (Selective State-Space Family)
category: Deep Learning / Selective State-Space Sequence Models (SSM)
tags:
  - model
  - deep-learning
  - state-space-models
  - sequence-modeling
---

# 🐍 Mamba / SSM Family

## Overview
The Mamba family comprises **selective state-space models** — sub-quadratic sequence models with constant memory and linear compute that compete with Transformers while decoding far faster. The continuous SSM $\dot{h}(t) = A(t)h(t) + B(t)x(t),\ y(t) = C(t)^\top h(t)$ is discretized into a recurrence $h_t = \alpha_t h_{t-1} + \gamma_t B_t x_t,\ y_t = C_t^\top h_t$ with **input-dependent (selective)** transitions.

- **[[Mamba]]** (Gu & Dao, 2023): selective scan + hardware-aware parallelization; the original linear-time architecture.
- **[[Mamba-2]]** (Dao & Gu, ICML 2024): Structured State-Space Duality (SSD); fails state-tracking tasks like parity.
- **[[Mamba-3]]** (Lahoti et al., 2026): three SSM-principled improvements —
  1. **Exponential-trapezoidal discretization** acting as an implicit width-2 convolution inside the recurrence:
$$h_t = e^{\Delta_t A_t} h_{t-1} + (1-\lambda_t)\Delta_t e^{\Delta_t A_t} B_{t-1} x_{t-1} + \lambda_t \Delta_t B_t x_t \equiv \alpha_t h_{t-1} + \beta_t B_{t-1}x_{t-1} + \gamma_t B_t x_t$$
  obviating the short causal conv.
  2. **Complex-valued state transitions** via data-dependent RoPE, restoring rotational dynamics for state tracking (parity: 100.0 vs Mamba-2's 0.90).
  3. **Multi-Input Multi-Output (MIMO)** formulation raising decode FLOPs up to 4× at fixed state size without wall-clock latency increase ($H_t = a_t H_{t-1} + B_t X_t^\top$, arithmetic intensity Θ(R)).
  
At 1.5B scale Mamba-3 reaches 57.6 avg downstream accuracy (vs Transformer 55.4, Mamba-2, GDN) and matches Mamba-2 perplexity at half the state size → half decode latency.

EV-domain derivatives:
- **[[HyKANet]]** (Hao & Ren, ICASSP 2026): Graph-aware MambaBlocks + HydraMamba multi-scale routing (short/medium/long-term branches) + KAN decoder for station-level charging demand; best avg RMSE 4.67 vs PAG 5.48 (−14.8%).
- **[[PC-M3]]** (Tang et al., Electronics 2026): Physics-Constrained Mamba-3 MIMO aggregator with vehicle-as-channel tokens and differentiable in-loop feasibility projection for V2G cluster flexibility envelopes; zero polytope violations, 0.34 s inference for 10,000 EVs.

## Typical Usage in EV Load Forecasting
- **Input**: multivariate spatiotemporal sequences (HyKANet: 5-min demand + weather/price/calendar; PC-M3: per-vehicle status channels).
- **Forecasting Horizon**: [[Short_Term]] (15–60 min HyKANet) to [[Day_Ahead]] flexibility envelopes (PC-M3, T=96 @ 15 min).
- **Strengths**: linear-time long-range modeling; fastest decode latency of all sub-quadratic baselines; selective memory adapts to input.
- **Weaknesses**: weaker than exact attention on semi/unstructured extraction tasks (hybrids needed); fixed-state limits on very high channel counts (vehicle-as-channel beyond validated rank range carries no guarantees).

## Literature Usage
- [[2026_Lahoti_Mamba_3_Sequence_Modeling]] — Mamba-3 foundational paper: exponential-trapezoidal discretization, complex/RoPE transitions, MIMO; beats GDN/Transformer/Mamba-2 at all scales on 100B-token pretraining.
- [[2026_Hao_Mamba_KAN_HyKANet_EV]] — HyKANet: three parallel Mamba branches + dynamic graph learning + bidirectional cross-attention + KAN decoder; RMSE −14.8% and MAE −12.2% vs best baseline PAG on real-world EV charging data.
- [[2026_Chen_PC_M3_Mamba_EV_Clusters]] — PC-M3: Mamba-3 MIMO backbone with physics-constrained projection inside the recurrence; Hausdorff envelope error 3.4% vs PowerMamba 9.7 / Informer 11.8; zero feasibility violations across 20,214 test sessions.
- [[2026_Liu_MFT_Multi_Scale_Fusion_Transformer]] — Identifies absence of SSM/Mamba comparisons as a gap for multi-scale EV station-load forecasting Transformers.
- [[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]] — TimeMachine: quadruple-Mamba LTSF architecture unifying channel-mixing and channel-independence via transposition (two outer Mambas at fine scale $n_1$, two inner at coarse scale $n_2$); Electricity T=96 MSE 0.142/MAE 0.236 vs iTransformer 0.148/0.240 with DLinear-level memory on 862-channel Traffic.
- [[2024_Liang_BiMamba_Bidirectional_Mamba_Forecasting]] — Bi-Mamba+: forget-gated Mamba+ block run forward AND backward over time plus a Spearman-based Series-Relation-Aware decider that auto-selects channel-independent vs channel-mixing tokenization per dataset; critiques TimeMachine's heuristic channel-strategy choice (−4.72% avg MSE vs iTransformer; Electricity T=96 MSE 0.140).
