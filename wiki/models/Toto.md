---
type: model
name: "Toto 2.0"
category: Deep Learning / Decoder-Only Patched Foundation Model (Datadog)
tags:
  - model
  - deep-learning
  - foundation-model
  - decoder-only
  - zero-shot
  - scaling-laws
  - probabilistic-forecasting
---

# ⏱️ Toto 2.0

## Overview
Toto 2.0 (Khwaja et al., Datadog AI Research + CMU, arXiv:2605.20119v2, June 2026) is the first TSFM family demonstrating **reliable scaling**: a single recipe (Contiguous Patch Masking + quantile head + NorMuon + u-µP transfer) produces monotonic gains from **4M → 22M → 313M → 1B → 2.5B** params on BOOM, GIFT-Eval and TIME. Five open-weights checkpoints (Apache 2.0) beat every external foundation model on all three benchmarks despite **zero public data in base pretraining** (only Datadog observability + TempoPFN synthetic).

Core architecture (Fig. 2, retained from Toto 1.0 with refinements):

- **Contiguous Patch Masking (CPM)** — variable-length masked spans $c\sim\mathcal{U}\{1:c_{\max}\}$, $p\sim\mathcal{U}(0,p_{\max})$, optimal $c_{\max}=16$, $p_{\max}=0.4$; single forward pass at inference $\hat{p}_i=[f_\theta(p_{1:N},b_{1:N})]_i$, $i\in M$ (Eq. 1); block decoding variant reuses KV cache for long horizons.
- **Quantile output head** — 9 levels $\mathcal{T}=\{0.1,\dots,0.9\}$, pinball loss $\rho_\tau=(y-\hat{q}_\tau)(\tau-\mathbf{1}[y<\hat{q}_\tau])$ (Eq. 2), $\mathcal{L}_{\text{quantile}}=\frac1{|\mathcal{T}|}\sum_\tau \rho_\tau$ (Eq. 3); sorted at inference to prevent crossing; replaces Student-T mixture (SMM) for stability at scale.
- **NorMuon optimizer** — per-neuron row-normalized Muon ($v_t=\beta_2 v_{t-1}+(1-\beta_2)\mathrm{mean_{cols}}(O_t\odot O_t)$, $W_t\leftarrow W_{t-1}-\eta O_t/\sqrt{v_t+\epsilon}$, Eq. 5; $O_t=\mathrm{NS}(B_t)$, $B_t=\mu B_{t-1}+G_t$; Polar Express iteration, Nesterov momentum, cautious weight decay) for sign-valued pinball gradients (Eq. 4); AdamW retained for projections/biases/norms.
- **Robust causal scaler** — $z_t=\operatorname{asinh}((x_t-\mu_t)/\sigma_t)$, $\operatorname{asinh}(z)=\log(z+\sqrt{z^2+1})$ (Eq. 6); preserves sign, compresses large excursions logarithmically.
- **Residual MLP projections** — 2-layer SiLU + skip at both patch embedding and output (vs linear in Toto 1.0); PerDimScale + $1/d_k$ attention for µP; patch size 32 (halved from 64); no dropout.
- **u-µP transfer** — $W=A_W w$, $w_{t+1}=w_t+C_W\Phi_t$, $A_W\propto1/\sqrt{\text{fan\_in}}$, $C_W\propto\eta/\sqrt{\text{fan\_in}}$ (Eq. 7); proxy 10M ($L=12,d=256,h=4$) tuned via 4-round Optuna TPE (architecture → data → optimizer → decay), transferred to all 5 targets (width/depth/heads scaled, $d_{\text{head}}=64$ fixed).

Training: WSD schedule (warmup 6k, linear decay 10.5k / 1.7–2.6% of 400k–600.5k total steps), batch 64×4096 tokens, context 4096 (2048 on BOOM), 32 variates/sample, $\alpha_{\text{res-attn-ratio}}=\sqrt{S/\log S}$ fix for unit-scaling disabled in attention; `dd_unit_scaling` library (FSDP2/torch.compile/DP-TP compatible).

Pretraining mix (proxy optimum): **42.5% Datadog observability** (10s:20%, 60s:7.5%, 5+m:15%) + **57.5% TempoPFN synthetic** (5.04T large / 3.40T small); no public data. FT mix: GIFT-Eval Pretrain 45% + Datadog 5+m 25% + GIFT-Eval train 15% + synthetic 10% + 10s/60s 2.5% each (10k steps, LR ~10× lower).

## Typical Usage in EV Load Forecasting
- **Input**: past window $y_{1:L}$ + missingness mask $b_{1:N}$; 32 variates/sample during training; currently **no exogenous covariates** (weather, tariff, SoC, arrival/departure all future work; metrics modality itself argued as distinct).
- **Forecasting Horizon**: [[Long_Term_Forecasting]] and [[Day_Ahead_Forecasting]]/[[Short_Term_Forecasting]] alike; single-pass stable to ~768 steps, block decoding beyond; evaluated at 2k–8k steps in stability study ($r=0.99$ at 2k for 2.5B, $r=0.818$ at 8k).
- **Strengths**: only TSFM family with reliable scaling; Pareto-frontier on every metric; strong cross-domain generalization from non-public data; fast single-pass inference (313M ≈ Chronos-2 120M latency; 2.5B at 4096 steps still faster than Chronos-2).
- **Weaknesses**: covariate-free; single-pass coherence limit ~768 steps (needs block decoding beyond); even 2.5B degrades at 8k vs classical seasonal model; public-data mix for FT is empirically found, not principled; width scaling validated but depth/data scaling not isolated.

## Literature Usage
- [[2026_Toto_2_Scaling_Era]] — Origin paper. BOOM CRPS ranks **3.88/3.96/4.26/5.53/7.17** (2.5B/1B/313M/22M/4M) vs Toto 1.0 6.94, Chronos-2 7.39; GIFT-Eval (FM-only) CRPS ranks **20.3/21.1/21.4** vs PatchTST-FM r1 23.1, Chronos-2 23.5; TIME CRPS ranks **3.43/3.51/3.86** sweep top-3; FnF ensemble #1 and 2.5B-FT #2 on full GIFT-Eval leaderboard; latency and 2k–8k stability studies included.

## Related Models
- Patched predecessor: [[PatchTST]] (encoder-decoder patching); compared directly in ablations.
- Direct competitors beaten: [[TimesFM]] / [[TimesFM_2.0]], [[Chronos]] / [[Chronos-Bolt]], [[Moirai]], [[TiRex]], [[FlowState]], [[Timer]], [[Time-MoE]], [[Sundial]], [[Granite]], [[TTM]].
- Optimizer family: [[Adam]] / [[Muon]] → [[NorMuon]] (row-normalized Muon + per-neuron $\beta_2$).
- Backbone predecessor: Toto 1.0 (Cohen et al. 2024); xLSTM [Beck et al. 2024] as CPM origin architecture.
- [[2025_Chronos_2_Univariate_to_Universal]] — **Toto-1.0 (Cohen et al. 2025)** beaten on all 3 benchmarks: fev-bench W 66.6/S 40.7 vs 90.7/47.3; GIFT-Eval WQL 67.4/48.6 vs 81.9/51.4; univariate Chronos-2 already beats multivariate Toto on 26-task multivariate subset.
- [[2026_Moirai_2_When_Less_Is_More]] — **Moirai 2.0 (Liu et al., Salesforce 2026)**: Decoder-only quantile TSFM (11.4M small / 87.1M / 305M) with multi-token prediction + recursive multi-quantile decoding. GIFT-Eval 97 tasks: 5th MASE / 6th CRPS among 37 FMs; 30x smaller & 2x faster than Moirai-Large; ablations: quantile loss gives largest gain (v1->v2 MASE 0.85->0.744), Table 2. Negative scaling on same corpus (base/large underperform small), long-horizon rank degrades 4th->8th.
