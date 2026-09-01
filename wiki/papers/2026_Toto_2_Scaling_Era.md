---
type: paper
title: "Toto 2.0: Time Series Forecasting Enters the Scaling Era"
authors: [Emaad Khwaja, Chris Lettieri, Gerald Woo, Eden Belouadah, Marc Cenac, Guillaume Jarry, Enguerrand Paquin, Xunyi Zhao, Viktoriya Zhukova, Othmane Abou-Amal, Chenghao Liu, Ameet Talwalkar, David Asker]
year: 2026
journal_conference: "arXiv preprint arXiv:2605.20119v2 [cs.LG]"
doi_url: "https://arxiv.org/abs/2605.20119v2"
models_used: ["[[Toto]]", "[[TimesFM]]", "[[Chronos]]", "[[Moirai]]", "[[TiRex]]", "[[PatchTST]]", "[[FlowState]]", "[[Xihe]]", "[[Timer]]", "[[Time-MoE]]", "[[Sundial]]", "[[Granite]]", "[[TTM]]", "[[Transformer]]", "[[xLSTM]]", "[[Migas]]", "[[Reverso]]"]
datasets_used: ["[[BOOM]]", "[[GIFT-Eval]]", "[[TIME_Benchmark]]", "[[Datadog_Observability]]", "[[TempoPFN_Synthetic]]", "[[GIFT_Eval_Pretrain]]"]
features_used: ["[[Historical_Load]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[CRPS]]", "[[MASE]]", "[[Pinball_Loss]]", "[[OWA]]"]
tags: [paper, foundation-model, scaling-laws, decoder-only, zero-shot, time-series-forecasting, u-muP, NorMuon]
---

# Summary: Toto 2.0: Time Series Forecasting Enters the Scaling Era

## 🎯 Main Objective & Contribution
- **Research question**: Do time series foundation models (TSFMs) scale reliably — can a single training recipe applied at successively larger widths and token budgets produce predictable returns, as in NLP/vision (Kaplan et al. 2020; Radford et al. 2019)?
- **Core contribution — [[Toto]] 2.0 family**: Five open-weights decoder-only patched transformers **4M / 22M / 313M / 1B / 2.5B params** trained under ONE recipe that shows **monotonic scaling**: every size improves on the one below on BOOM, GIFT-Eval and TIME. First TSFM demonstration of reliable scaling.
- **Three design pillars**:
  1. **Architecture refinements over [[Toto]] 1.0 (Cohen et al. 2024)**: Contiguous Patch Masking (CPM) for single-pass parallel decoding; quantile output head (9 levels) replacing Student-T mixture (SMM); **NorMuon** optimizer replacing AdamW to handle sign-valued pinball gradients; patch size 32 (from 64), robust causal scaler with `arcsinh`, residual MLP patch projections, PerDimScale attention.
  2. **Training data**: Base models see **NO public time series during pretraining** — exclusively **Datadog internal observability metrics** (CPU/memory/latency/error rates) + **TempoPFN synthetic** (PFN prior with nonstationary trends, changepoints, long-range dependencies). 5.04T points for 313M/1B/2.5B; 3.40T for 4M/22M (vs 2.36T Toto 1.0). Mix = 42.5% observability / 57.5% synthetic after proxy sweep (public data excluded; 10 s:20%, 60 s:7.5%, 5+m:15%). Public data only enters **finetuning** (45% of FT mix).
  3. **u-µP hyperparameter transfer pipeline**: Tune once on a **10M proxy** (L=12, d=256, h=4, 30k steps, WSD schedule), transfer to all 5 targets by scaling `d_model`/depth/head count with unit-scaled Maximal Update Parametrization (u-µP, Blake et al. 2025) — makes optimal LR width-independent. Structured 4-round Optuna TPE search (architecture → data mixture → optimizer → decay). First application of µP to time series.
- **Empirical claim**: Toto 2.0 sets **new SOTA zero-shot** on all three benchmarks — **BOOM** (observability), **GIFT-Eval** (97 tasks, 23 datasets; top-3 CRPS ranks 20.3/21.1/21.4), **TIME** (98 fresh tasks, 50 datasets; top-3 on every metric). Finetuned 2.5B-FT and FnF ensemble additionally take #1/#2 on full GIFT-Eval leaderboard (all tiers). Every size sits on/near Pareto frontier; 22M matches Toto 1.0 (151M) quality with 7× fewer params; 4M competitive with Chronos-2 despite 38× smaller. Dramatically faster inference at long horizons (single-pass vs 16-step AR).

## 🧠 Methodology & Model Architecture
- **Model Type**: Decoder-only patched Transformer with **alternating time-axis (causal) and variate-axis (full) attention** retained from Toto 1.0. Pipeline (Fig. 2): Robust Causal Scaler → Patch Embedding + CPM (binary mask channel) → Input Residual MLP → Variate-Time Transformer Decoder → Output Residual MLP → **Quantile Output Head** (9 levels). Context 4096 timesteps (2048 on BOOM), patch 32, 32 variates/sample, batch 64.

- **Key Equations** (verbatim, §2–4):

  **Eq. 1 — Contiguous Patch Masking forward** (CPM; $P$=patch size, $M \subseteq \{1,\dots,N\}$ masked positions, binary mask channel $b_i \in \{0,1\}^P$, $b_{i,k}=1$ at unobserved entries):
  $$\hat{p}_i = \left[f_\theta(p_{1:N}, b_{1:N})\right]_i,\quad i \in M \tag{1}$$
  Loss averaged over all $N$ positions. Train: $M$ = random contiguous spans length $c \sim \mathcal{U}\{1:c_{\max}\}$ with prob $p \sim \mathcal{U}(0,p_{\max})$; Inference: $M=\{N+1,\dots,N+K\}$, $K=H/P$. One call to $f_\theta$ on transformer vs $|M|$ on SSM. Optimal sweep: $c_{\max}=16$, $p_{\max}=0.4$ (vs TiRex $5/0.25$). Block decoding variant commits $p_i \leftarrow \mathrm{median}(\hat{p}_i)$, $b_i \leftarrow 0$ per block of $B$ patches, reusing KV cache.

  **Eq. 2 — Pinball (quantile) loss** per level $\tau$ (Koenker & Bassett 1978; $\mathcal{T}=\{0.1,\dots,0.9\}$, 9 levels):
  $$\rho_\tau(y - \hat{q}_\tau) = (y - \hat{q}_\tau)\left(\tau - \mathbf{1}[y < \hat{q}_\tau]\right) \tag{2}$$

  **Eq. 3 — Quantile head loss** (averaged over 9 levels):
  $$\mathcal{L}_{\text{quantile}} = \frac{1}{|\mathcal{T}|}\sum_{\tau \in \mathcal{T}} \rho_\tau(y - \hat{q}_\tau) \tag{3}$$
  Predicted quantiles sorted at inference to prevent crossing.

  **Eq. 4 — Pinball gradient** (sign-valued; magnitude-free):
  $$\frac{\partial \rho_\tau(y - \hat{q})}{\partial \hat{q}} = g_\tau = \begin{cases} -\tau & y > \hat{q} \\ 0 & y = \hat{q} \\ 1 - \tau & y < \hat{q} \end{cases} \tag{4}$$
  Contrast MSE gradient $-2(y-\hat{q})$ whose magnitude scales with error; pinball gives only direction, so optimizer must infer step size internally.

  **Eq. 5 — NorMuon row-normalized update** (all matrix-shaped hidden weights; Li et al. 2025; Nesterov momentum; Polar Express quintic Newton-Schulz; input/output/bias/norms use AdamW):
  $$v_t = \beta_2 v_{t-1} + (1-\beta_2)\cdot \mathrm{mean_{cols}}(O_t \odot O_t),\quad W_t \leftarrow W_{t-1} - \eta\, O_t / \sqrt{v_t + \epsilon} \tag{5}$$
  where $B_t = \mu B_{t-1}+G_t$, $O_t = \mathrm{NS}(B_t)$ orthogonalized (singular values →1), $\odot$ Hadamard, $\mathrm{mean_{cols}}$ per-row column-mean (per-neuron scalar), division/sqrt broadcast row-wise. Reinstates $\beta_2$ variance mechanism per-neuron vs Adam's per-parameter. Cautious weight decay only where sign aligns.

  **Eq. 6 — Robust causal scaling** (input scaler):
  $$z_t = \operatorname{asinh}((x_t - \mu_t)/\sigma_t),\quad \operatorname{asinh}(z) = \log\!\left(z + \sqrt{z^2+1}\right) \tag{6}$$
  Behaves as $z$ for $|z|\ll1$, as $\mathrm{sign}(z)\log(2|z|)$ for $|z|\gg1$; preserves sign, compresses large excursions logarithmically. Predictions unscaled for final forecast. Interior missing values forward-filled; location/scale backfilled when leading patch <8 obs; outputs clamped to $[\min - 10^4\sigma_{\text{anchor}}, \max + 10^4\sigma_{\text{anchor}}]$.

  **Eq. 7 — u-µP reparametrization** (Blake et al. 2025; hidden weights; $A_W \propto 1/\sqrt{\text{fan\_in}}$, $C_W \propto \eta/\sqrt{\text{fan\_in}}$; input/output/depth variants per Table 2 of Blake et al.):
  $$W = A_W \cdot w,\; w_0 \sim \mathcal{N}(0,1),\quad w_{t+1} = w_t + C_W\cdot \Phi_t \tag{7}$$
  Makes optimal $\eta$ invariant across widths. Proxy optimum $\eta_{\text{NorMuon}}=0.652$, $\mu=0.96$, $\beta_2=0.999$, wd $2\times10^{-8}$; warmup 6000, clip 7.0; linear decay 10500 steps (1.7–2.6% of total).

  **Eq. 8 — Overall Weighted Average (OWA) for ensemble training** (Makridakis et al. 2020; seasonal-naive normalized; $j$ = window, $s$ = dataset):
  $$\mathrm{OWA}_{f,j} = \tfrac12\left(\frac{\mathrm{MASE}_{f,j}}{\mathrm{MASE}_{s\text{Naive}}} + \frac{\mathrm{CRPS}_{f,j}}{\mathrm{CRPS}_{s\text{Naive}}}\right) \tag{8}$$
  Used to train FFORMA-style XGBoost meta-learner (20 heads by frequency×horizon bucket) emitting softmax weights over 10-model pool for Toto 2.0 FnF ensemble.

- **Design principles**:
  - *Patching*: P=32 (halved from 64) doubles sequence length, finer within-patch dynamics, longer attention.
  - *Residual MLP projections*: Two-layer SiLU + skip at both patch embedding and output (vs linear in Toto 1.0).
  - *Attention changes*: PerDimScale (learned per-dim query scaling, also TimesFM 2.5) + $1/d_k$ scaling for µP; fully-missing patches masked from attention; bias on attention projections only; no dropout.
  - *Why NorMuon over AdamW/Muon*: Pinball sign-valued gradients leave AdamW's per-parameter $v_t$ as only magnitude source (limited dynamic range); Muon discards $v_t$ entirely (2× compute-efficiency on smooth losses but loses remaining adaptation); NorMuon row-normalization balances per-neuron contributions AND reinstates $\beta_2$ per-neuron.
  - *Scaling recipe*: Proxy $d_{\text{head}}=64$ fixed; targets scale $d_{\text{model}}/h/L$ as (256/4/4→512/8/6→1024/16/24→1536/24/36→2048/32/48); Norm $\epsilon$ $10^{-4}$ except $5\times10^{-4}$ for 1B/2.5B; steps 400k (4M/22M) or 600.5k (larger, still improving past 400k).

- **Training**: WSD (warmup-stable-decay) LR; global batch 64×4096 = 262k tokens/step; $\alpha_{\text{res-attn-ratio}}=\sqrt{S/\log S}$ ($S$=context/patch), $\alpha_{\text{res}}=0.75$ to fix variance mismatch from disabling unit-scaling in attention/MLP activations (KV-cache compatibility); FSDP2 + torch.compile + DP/TP handling via `dd_unit_scaling` library (Apache 2.0); loss multiplied by world_size to undo DDP averaging.

## 📊 Dataset & Input Features
- **Pretraining corpus — base models (no public data)** (Fig. 3, §3; total 5.04T for large / 3.40T for small):

| Source | Points (large mix) | Share | Notes |
|---|---|---|---|
| Datadog internal observability (CPU/memory/latency/error rates etc.) | 2.14T | 42.5% | 10 s: 20% (47.1% within observability), 60 s: 7.5% (17.6%), 5+m: 15% (35.3%); rebalanced from Toto 1.0 (10 s was 78.5%); no customer data |
| TempoPFN synthetic (PFN prior; Moroshan et al. 2025; Müller et al. 2022) | 2.90T | 57.5% | Nonstationary trends, abrupt changepoints, long-range dependencies; hand-crafted prior |

  Toto 1.0 comparison: 1.00T internal + 0.78T synthetic + 0.58T public = 2.36T (public dropped entirely in Toto 2.0; internal ~2×, synthetic ~4×).

- **Finetuning corpus — Toto 2.0 2.5B-FT** (10k steps from fully-decayed checkpoint; §5.3):
  GIFT-Eval Pretrain 45% (from Toto 1.0 pool: GIFT-Eval Pretrain + Chronos corpus, non-leaking) + Datadog 5+m 25% + GIFT-Eval train (eval datasets' official train splits) 15% + synthetic 10% + Datadog 10 s/60 s 2.5% each. LR reduced ~10× (NorMuon 0.05, AdamW 0.001).

- **Evaluation benchmarks (all zero-shot unless noted)**:
  - **[[BOOM]]** [Cohen et al. 2025] — Datadog observability benchmark: CPU/memory/latency/error-rate metrics; context 2048; metrics CRPS rank / CRPS / MASE.
  - **[[GIFT-Eval]]** [Aksu et al. 2024a] — 97 evaluation tasks (dataset×frequency×horizon) from 23 base datasets (energy, retail, weather, finance); context 4096; Pretrain corpus (Aksu et al. 2024c) and train splits (2024b) are distinct artifacts. Metrics CRPS rank / MASE rank / CRPS / MASE.
  - **[[TIME_Benchmark|TIME]]** [Qiao et al. 2026] — 98 tasks from 50 *fresh* datasets (never/rarely benchmarked), human-in-the-loop curation, horizons aligned to operational requirements; deliberately avoids legacy ETTh1/Electricity/Traffic/Weather; per-task prescribed context lengths; metrics same 4.

- **Other datasets referenced**: ETTh1/ETTh2/ETTm1/ETTm2, Electricity, Traffic, Weather (as legacy datasets TIME avoids); Monash excluded; ARFBench (Xie et al. 2026) multimodal incident benchmark mentioned as future direction.

- **Data Availability & Links**:
  - Code: https://www.github.com/DataDog/toto
  - Weights (Apache 2.0): https://www.huggingface.co/collections/Datadog/toto-20 (all 5 sizes)
  - Distributed u-µP library: `dd_unit_scaling` (Apache 2.0, open-source)
  - GIFT-Eval dataset: https://huggingface.co/datasets/Salesforce/GiftEval
  - GIFT-Eval Pretrain: https://huggingface.co/datasets/Salesforce/GiftEvalPretrain
  - Chronos pretraining corpus (Ansari et al. 2024) — non-leaking subset used in FT
  - **No public eval domains seen during base pretraining** — strengthens cross-domain generalization claim

- **Features**: Past values $y_{1:L}$ + binary missingness mask $b_{1:N}$ + quantile levels; 32 variates/sample during training; no exogenous covariates (text/traces/logs/topology all noted as future multimodal direction; metrics modality itself argued as distinct, §6).

- **Preprocessing**: Robust causal scaler (§2.4) + arcsinh; 4096-timestep contexts, patch 32, 32 variates/sample; forward-fill interior gaps; backfill scaler stats when <8 obs; sort quantiles; clamp outputs.

## 📈 Performance & Results
- **BOOM (Fig. 5, §5.1)** — CRPS rank / CRPS / MASE; lower is better; all 5 Toto 2.0 on Pareto frontier; every size beats every external FM:
  - CRPS rank: **2.5B 3.88**, **1B 3.96**, **313M 4.26**, **22M 5.53**, **4M 7.17** vs Toto 1.0 (151M) 6.94, Chronos-2 7.39, TimesFM 2.5 10.7, Moirai 2 11.9, TimesFM 2.0 11.3, Chronos Bolt 12.3, Time-MoE/Timer s1 ~17.5.
  - CRPS: 2.5B/1B 0.349, 313M 0.351 … Toto 1.0 0.375, Chronos-2 0.382 etc.
  - MASE: 2.5B 0.581, 1B 0.582 … Toto 1.0 0.617.
  - **22M matches/beats Toto 1.0 with ~7× fewer params; 4M (~38× smaller) competitive with Toto 1.0/Chronos-2.**

- **GIFT-Eval — foundation models only (Fig. 6, §5.2)** — Toto 2.0 top-3 despite no public pretraining:
  - CRPS rank: **2.5B 20.3**, **1B 21.1**, **313M 21.4** vs next best PatchTST-FM r1 23.1, Chronos-2 23.5, TiRex 23.9; gap 313M→next = 1.7 pts.
  - MASE rank: **2.5B 21.0** (sole leader), 1B 21.3, 313M 22.2.
  - CRPS: 2.5B 0.476 … Toto 2.0 22M 0.496 vs Toto 1.0 0.516.
  - MASE: Timer s1 0.693 best raw, but Toto 2.5B 0.696 close; rank metrics favor Toto 2.0.
  - **Monotonic size→quality on rank metrics; 22M beats Toto 1.0 (35.1) by >8 pts.**

- **GIFT-Eval — finetuned & ensemble (Fig. 7, §5.3)** — Full leaderboard (all tiers):
  - **Toto 2.0 FnF (FFORMA ensemble over 10 FMs) ranks #1 on every metric** (tied raw CRPS 0.463 with TSOrchestra): CRPS rank 12.8, MASE rank 13.5, CRPS 0.463, MASE 0.676 vs TSOrchestra 13.5/14.9/0.463/0.677, DeOSAlpha 13.8/14.9/0.466/0.682.
  - **Toto 2.0 2.5B-FT ranks #2 on rank metrics, #3 on raw**: CRPS rank 13.4, MASE rank 14.7, CRPS 0.463, MASE 0.679.
  - Pool weights (meta-learner softmax, avg): Toto 2.0 family **39%** > Chronos-2 32% > remaining 4 externals combined — ensemble confirms Toto 2.0 as most valuable source.
  - Zero-shot 2.5B/1B/313M already sit at ranks 20.3–21.4 among FMs; FT/ensemble close gap to agentic systems.

- **TIME (Fig. 8, §5.4)** — 98 fresh tasks; Toto 2.0 sweeps top-3 on every metric:
  - CRPS rank: **2.5B 3.43**, 313M 3.51, 1B 3.86 vs PatchTST-FM TsMix10M 4.38, Chronos-2 4.03 (4th); only inversion: 313M edges 1B on rank metrics (sole scaling inversion in family).
  - MASE rank: **2.5B 3.54**, 313M 3.65, 1B 3.71.
  - CRPS: 2.5B 0.532, 313M 0.535, 1B 0.537 vs PatchTST-FM TsMix 0.549, Chronos-2 0.549.
  - MASE: 2.5B 0.640 … 4M 0.689 still beats Toto 1.0 0.696. Every size including 4M beats Toto 1.0; external best (PatchTST-FM, Chronos-2) trail top-3 on all metrics.

- **Inference latency (Fig. 9, §5.5)** — CPM single-pass vs block vs AR:
  - 1024-step horizon: Toto 1.0 needs 16 AR steps; Toto 2.0 single-pass = 1 forward pass — every Toto 2.0 size significantly faster than Toto 1.0; 313M latency ≈ Chronos-2 (120M params).
  - Flat latency in single-pass up to ~768 steps (found stable on synthetic); at 4096 steps, 2.5B single-pass still faster than Chronos-2 despite >20× params. Block decoding adds B−1 passes but mitigates drift; KV cache reused.

- **Long-horizon stability — synthetic multi-scale sinusoids (periods 500/100/20; Fig. 10, §5.6, block decoding, horizons 2048/4096/8192 ≫ 4096 training context)** — Pearson r vs ground truth:
  - 2.5B: r 0.990 / 0.979 / 0.818; 1B: 0.984/0.945/0.643; 313M: 0.986/0.947/0.681; 22M: 0.805/0.484/0.315; 4M: 0.538/0.371/0.173; Toto 1.0: 0.816/0.627/0.333; Chronos-2: 0.663/0.457/0.310.
  - Larger sizes retain coherent multi-scale structure at 8192 steps; smaller/previous-gen collapse past training context. Demonstrates capacity-dependent extrapolation; even 2.5B degrades at 8192 (classical seasonal model would extrapolate cleanly).

## 💡 Limitations & Identified Research Gaps
- **Long-horizon coherent extrapolation still lags classical baselines**: Even 2.5B loses structure at 8192 steps where a well-specified seasonal ARIMA/ETS would extrapolate cleanly; tail behavior, regime shifts, far-OOD signals remain open (§6). Suggests need for architectural changes + scaling + post-training objectives.
- **Data curation ad hoc**: Proportions chosen by sweep rather than principled filtering/dedup/annotation/curriculum (contrast LLM curation). Optimal mix excluding public data for pretraining yet requiring 45% public for FT is non-intuitive and empirically found, not explained.
- **Evaluation tracks forecast error, not downstream value**: CRPS/MASE ≠ production value (cf. V2G-SVE [Zhong et al. 2024]); ARFBench multimodal incident reasoning and observability world-model (metrics+traces+logs+topology+code+events) remain future.
- **Metrics as distinct modality ignored**: Compressing Datadog metrics into generic time-series discards structure; heterogeneous frequencies, extremely high dimensionality (context selection), histogram/distribution metric types, complex/multiple/non-integer/uneven seasonalities all unsolved.
- **No EV or power-systems evaluation**: All benchmarks are generic/observability; transfer to sparse, spiky EV charging loads (ACN, ElaadNL, Boulder, Pecan Street) unproven; covariate-free design leaves arrival/departure, SoC, tariff, weather+traffic fusion via cross-attention as open gap.
- **Inference-time coherence horizon ~768 steps single-pass**: Beyond that requires block decoding (mitigates drift but not perfectly); zero-shot beyond 2× training context degrades even for largest model.
- **Width scaling validated, depth/data scaling not isolated**: Recipe scales width/depth/heads jointly; compute-optimal frontier vs Hoffmann et al. not mapped; total training cost (600k steps × 64 batch × 4096 length) and carbon not reported beyond step counts.
- **Weight decay not guaranteed to transfer under u-µP**: Held fixed from proxy; theory guarantees LR only.

## 📚 BibTeX & Citation Reference
```bibtex
@misc{khwaja2026toto2scaling,
  author       = {Emaad Khwaja and Chris Lettieri and Gerald Woo and Eden Belouadah and Marc Cenac and Guillaume Jarry and Enguerrand Paquin and Xunyi Zhao and Viktoriya Zhukova and Othmane Abou-Amal and Chenghao Liu and Ameet Talwalkar and David Asker},
  title        = {Toto 2.0: Time Series Forecasting Enters the Scaling Era},
  year         = {2026},
  howpublished = {arXiv preprint arXiv:2605.20119v2 [cs.LG]},
  eprint       = {2605.20119},
  archivePrefix= {arXiv},
  primaryClass = {cs.LG},
  url          = {https://arxiv.org/abs/2605.20119},
  doi          = {10.48550/arXiv.2605.20119}
}
```

## 🔗 Key References & Citation Graph
- Cited Foundations in Vault: [[2017_Attention_Is_All_You_Need]] [VSP+17]; [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] [NNSK22] (patched predecessor); [[2022_RevIN_Reversible_Instance_Normalization]]-adjacent robust scaling; [[2014_Kingma_Adam_Optimization]] [Kingma & Ba 2017] / 2022_Liu_KAN_Kolmogorov_Arnold_Networks-adjacent; [[2020_DeepAR_Probabilistic_Forecasting]]-adjacent SMM; [[2024_TimesFM_Decoder_Only_Foundation_Model]] as contemporaneous TSFM; [[2024_TimeMachine_Mamba_Long_Term_Forecasting]]/[[2024_BiMamba_Bidirectional_Mamba_Forecasting]]/[[2026_Mamba_3_Sequence_Modeling]] (xLSTM/SSM context for CPM origin).
- Related Vault Papers: [[2024_TimesFM_Decoder_Only_Foundation_Model]] — decoder-only patched predecessor beaten on all 3 benchmarks; direct comparison in Fig. 1 (TimesFM-2.5/2.0 vs Toto 2.0 family Pareto); [[2025_Benchmark_Foundation_Models]] — benchmarks TimesFM/Chronos/Moirai on household STLF (Toto not yet included); [[2024_TimeMachine_Mamba_Long_Term_Forecasting]] / [[2026_Mamba_3_Sequence_Modeling]] — SSM alternatives to Transformer backbone; [[2024_V2G_SVE_Evaluation_Metric]] — downstream value metric vs CRPS/MASE gap highlighted in Toto 2.0 §6.

> [!IMPORTANT]
> **For Thesis Use**: First TSFM family demonstrating **reliable scaling** (4M→2.5B monotonic) via **u-µP transfer** — directly addresses thesis gap on scaling foundation models for load forecasting. Strongest evidence that base models trained with **zero public data** can still lead public benchmarks (cross-domain generalization). **CPM + quantile head + NorMuon** is the current SOTA recipe to beat for EV-adapted TSFMs. Open gaps for thesis: covariate-free, no EV evaluation, ~768-step single-pass coherence limit, and metric-vs-value evaluation — all align with proposed extensions (EV covariates, station-level finetuning, 96h horizons, V2G-SVE).

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2026_Toto_2_Scaling_Era_refs]]
