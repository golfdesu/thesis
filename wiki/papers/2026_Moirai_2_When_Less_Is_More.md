---
type: paper
title: "Moirai 2.0: When Less Is More for Time Series Forecasting"
authors: [Chenghao Liu, Taha Aksu, Juncheng Liu, Xu Liu, Hanshu Yan, Quang Pham, Silvio Savarese, Doyen Sahoo, Caiming Xiong, Junnan Li]
year: 2026
journal_conference: "arXiv preprint arXiv:2511.11698v3 [cs.LG] — Salesforce AI Research (2026-02-04)"
doi_url: "https://arxiv.org/abs/2511.11698"
models_used: ["[[Moirai]]", "[[Moirai_MoE]]", "[[Transformer]]", "[[Chronos]]", "[[Chronos-2]]", "[[Chronos-Bolt]]", "[[TimesFM]]", "[[Toto]]", "[[TiRex]]", "[[FlowState]]", "[[Sundial]]", "[[TabPFN-TS]]", "[[PatchTST]]", "[[TTM]]", "[[Lag-Llama]]"]
datasets_used: ["[[GIFT-Eval]]", "[[GIFT_Eval_Pretrain]]", "[[Chronos_Corpus]]", "[[KernelSynth]]", "[[Salesforce_Internal_Telemetry]]"]
features_used: ["[[Historical_Load]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MASE]]", "[[CRPS]]", "[[WQL]]"]
tags: [paper, foundation-model, decoder-only, quantile-forecasting, multi-token-prediction, zero-shot, time-series, GIFT-Eval]
---

# Summary: Moirai 2.0: When Less Is More for Time Series Forecasting

## 🎯 Main Objective & Contribution
- **Research gap**: Scaling time series foundation models (TSFMs) has been ad hoc — Moirai 1.0's masked-encoder design wastes data (1 loss per sampled config, ~15% tokens in loss), multi-patch sizes complicate training, and mixture-of-distributions output adds complexity yet underperforms empirically. Parameter scaling without matched data scaling does not reliably improve GIFT-Eval scores across families.
- **Core contribution — [[Moirai]] 2.0 (small 11.4M / base 87.1M / large 305M)**: A refined decoder-only patched Transformer that pairs **quantile forecasting with multi-token prediction** and is trained on a newly curated **36M series / ~295B observations** corpus — the main empirical message is *less complexity is more*.
- **Three pillars**:
  1. **Architecture simplification**: Decoder-only causal Transformer (from masked encoder), single patch size (from multi-patch), and **quantile loss** (from distribution NLL) with a residual-block output projection `R^d → R^{n_token × n_q × p}` (`n_q=9`).
  2. **Training/inference strategies**: Patch-level random masking (50% patches), statistical anomaly filtering (§3.2), **recursive multi-quantile decoding** (depth-2 expand→collapse beam, Algorithm 1), and multi-token prediction for efficient long horizons; KV-cache gives 4× (1K pred) to 17× (10K pred) speedup with 10K context.
  3. **New pretraining corpus** (36M series): Non-leaking GIFT-EVAL PRETRAIN (3.25M, 230B) + GIFT-EVAL TRAINTEST train split (144K) + Chronos-Mixup/TSMixup (30M, 63B) + KernelSynth (1M, 1.02B) + internal Salesforce CloudOps daily telemetry (2.15M, 1.48B, daily, from Jan 2024) — deliberately excluding / reweighting public leakage.
- **Empirical claim**: On **GIFT-Eval (97 tasks, 55 datasets)** Moirai 2.0 small **ranks 5th (MASE) / 6th (CRPS)** among 37 pretrained FMs (Fig. 2 normalized geometric mean), beating Moirai 1.0-Large while being **≈30× smaller and 2× faster**; ablations show decoder-only + quantile loss + recursive decoding drive most gains (Table 2). Scaling the same Moirai 2.0 to base/large on this corpus **does not help** (Table 1) — small already saturates data, and longer-horizon rank degrades (4th short → 8th long, Fig. 4).

## 🧠 Methodology & Model Architecture
- **Model Type**: Decoder-only patched Transformer for univariate series (multivariate via independent channels). Pipeline (Fig. 1): Instance normalization (stats from first 30% only to avoid leakage) → Non-overlapping patching with missing indicator `m_i` concatenated `x̂_i = x_i || m_i` → Input residual projection → Stacked causal Transformer decoders (RMSNorm, self-attention, FFN/GLU, RoPE, residual) → Descaling → Residual output projection to `n_token` future patches × `n_q=9` quantiles × patch length `p`.

- **Key Equations** (verbatim, §3):

  **Eq. 1 — Input patch projection** (patch size `p_in`, embedding `d`, residual block `R^{2p_in}→R^d`, `x̂_i = x_i || m_i`):
  $$z_i = \text{PatchEmbed}(\hat{x}_i) = \text{SiLU}(W\hat{x}_i + b) + \hat{x}_i \in \mathbb{R}^{d},\; i=1,\dots,T \tag{1}$$

  **Eq. 2 — Quantile (pinball) loss** (`Q={0.1,0.2,\dots,0.9}`, `|Q|=9`, `y_t` truth, `\hat{y}^{(q)}_t` q-quantile):
  $$\ell_q(y_t, \hat{y}^{(q)}_t) = \begin{cases} q\,(y_t - \hat{y}^{(q)}_t) & y_t \geq \hat{y}^{(q)}_t \\ (1-q)\,(\hat{y}^{(q)}_t - y_t) & y_t < \hat{y}^{(q)}_t \end{cases} \tag{2}$$

  **Eq. 3 — Total quantile loss** (`H=K\cdot p` steps over `K` predicted patches, masked/missing targets ignored; weighted variant `w_q` discussed):
  $$\mathcal{L}_{Q} = \frac{1}{H|Q|}\sum_{t=1}^{H}\sum_{q\in Q}\ell_q(y_t,\hat{y}^{(q)}_t) = \frac{1}{H|Q|}\sum_{t=1}^{H}\sum_{q\in Q}\left[ q\max(y_t-\hat{y}^{(q)}_t,0)+(1-q)\max(\hat{y}^{(q)}_t-y_t,0)\right],\; H=Kp \tag{3}$$

  *Note*: Formulations above are as in PDF pp. 4–5; Eq. numbering follows PDF (PatchEmbed is labelled (1) in §3.1 and pinball as (1)/(2)/(3) in §3.1–3.2 — kept as in source). Output projection mapping: `R^{d} → R^{n_{token}\times n_q \times p}`; loss optionally weighted by `w_q` for targeted tail emphasis (§3.3).

- **Inference — Algorithm 1 Autoregressive Multi-Quantile Decoding** (depth-2 expand→collapse, p. 5): From context `Y_{1:c}` predict first-step quantiles `{ŷ^{(q)}_{c+1}}`; for each `t=c+1..c+H-1` expand `m=|Q|=9` histories `→` decode one step ahead per expansion `→` pool `|S_{t+1}|=m^2=81` candidates `{ŷ^{(q_1,q_2)}_{t+1}}` `→` collapse via `Quantile_q(S_{t+1})` back to 9 levels for next step. Patch-level in practice (`n_token` patches/iter). Preserves uncertainty without the dimensional mismatch of feeding all 9 quantiles back directly; median-collapse is explicitly avoided [as in PDF Alg. 1].

- **Design principles**:
  - *Decoder-only vs masked encoder*: Decoder computes `T-1` losses per `T`-token series vs 1 loss / ~15% tokens for masked encoder (15% masking rate) → data-efficient, and KV-cache reuses context across repeated horizon extensions.
  - *Single vs multi patch*: Single `p` improves accuracy and efficiency and simplifies training/inference.
  - *Quantile (9 levels, 0.1–0.9, equal-weighted by default) vs mixture NLL*: Quantile directly optimizes CRPS, handles asymmetry (over/under-penalty), robust to tails vs variance collapse / unstable gradients of NLL.
  - *Multi-token prediction* (`n_token`): `R^d→R^{n_token×n_q×p}` reduces AR steps and error accumulation for long horizons.
  - *Robustness*: 50% patch random masking + z-score anomaly filter (drop samples where last 70% deviates from first 30% normalization window); residual-block input/output projections; `n_q=9` equidistant.

- **Training**: AdamW, 100k steps, batch 256, LR `1e-3`, wd `1e-1`, `β_1=0.9, β_2=0.98`, 10k warmup + cosine, bf16. Normalization from first 30% only; causal pre-training on remaining 70%.

## 📊 Dataset & Input Features
- **Pretraining corpus — 36M series / ~295B observations** (§4, five sources; Leakage: all evaluation sets excluded):

| Source | # Series | # Obs | Share / Notes |
|---|---|---|---|
| GIFT-EVAL PRETRAIN (non-leaking; subset of LOTSA — 27B in Woo et al. counted as multivariate → 230B when counted per-variate [as in PDF p.6 fn1]) | 3.25M | 230B | Diverse curated, avoids benchmark overlap |
| GIFT-EVAL TRAINTEST — train split | 144K | — | Added to pretrain (Aksu et al. 2024) |
| Chronos-Mixup / TSMixup (k∼U{1,K}, l∼U{l_min,l_max}, K=4, L_min=128, L_max=4096, convex mix; non-leaking Chronos subset; following Auer et al. 2025) | 30M | 63B | Synthetic augmentation |
| KernelSynth (GP kernels: trend/local/seasonal, +/×; Ansari et al. 2024) | 1M | 1.02B | Synthetic |
| Internal Salesforce CloudOps telemetry (univariate, daily, from Jan 2024; filtered heavy-missing) | ~2.15M | ~1.48B | Daily granularity |

  App. composition: Hugging Face datasets reused via GIFT-Eval construction; internal telemetry is proprietary filtered daily CloudOps.

- **Evaluation benchmarks (zero-shot unless noted)**:
  - **[[GIFT-Eval]]** — 97 task configs × 55 datasets (Econ/Fin, Energy, Healthcare, Nature, Sales, Transport, Web/CloudOps; frequencies yearly→secondly; horizons short/medium/long); 30 pretrained FMs compared (excluding agentic/finetuned/no-code); metrics **normalized MASE / normalized CRPS** (geometric mean ÷ seasonal-naive).
  - **Other references**: FEV-Bench [Shchur et al. 2025], LOTSA [Woo et al. 2024], Chronos corpus.

- **Data Availability & Links**:
  - Code: `https://github.com/SalesforceAIResearch/uni2ts`
  - Weights (Hugging Face): `https://huggingface.co/Salesforce/moirai-2.0-R-small` (also base/large)
  - GIFT-Eval datasets / pretrain: via Salesforce GIFT-Eval release (cf. `gift-eval` on HF; see also Chronos/KernelSynth sources above)

- **Features**: Purely **univariate** past values `Y_{1:c}` + binary missing indicator `m_i` per step; multivariate handled as independent univariate tasks; no exogenous covariates (dropped due to limited covariate-quality data — future via synthetic generation).

- **Preprocessing**: Per-series instance normalization (first 30% stats), non-overlapping patching with missing concatenation, 50% patch masking (train), residual-block embedding, descaling after projection, quantile outputs.

## 📈 Performance & Results
- **GIFT-Eval overall (Fig. 2 normalized geometric mean; 30 FMs, zero-shot, pretrained only; lower is better)** — Moirai 2.0 small ranks **5th MASE / 6th CRPS** among 37 foundation models (incl. size variants); substantially above Moirai-Large despite fewer params:
  - Normalized MASE (geometric mean ÷ seasonal naive; Fig. 2 left): leaders Chronos-2 / TimesFM-2.5 / TiRex / FlowState-9.1M / granite-flowstate-r1 / **Moirai 2.0** before Kairos/Toto/Sundial/TabPFN-TS/YingLong etc.; exact values from replication code at `https://github.com/SalesforceAIResearch/gift-eval/tree/main/notebooks` (replication-limited reporting).
  - Normalized CRPS (geometric mean; Fig. 2 right): same ordering; Moirai 2.0 6th overall.

- **Domain breakdown (Fig. 3, MASE rank, top-10 per domain)** — Moirai 2.0 appears top-10 in all domains except **Nature** (underrepresented in pretrain); strongest vs Moirai-Large in all domains except Transport where Moirai-Large remains competitive.

- **Horizon breakdown (Fig. 4, MASE rank)** — Moirai 2.0 ranks **4th short / 6th medium / 8th long** → advantage shrinks with longer horizons.

- **Variate / Frequency / Trend / Seasonality / Entropy / Hurst / Stability / Lumpiness (App. Fig. 6–13)** — Consistent top-10 across slices; full plots in PDF pp. 14–16.

- **Efficiency (Fig. 5, 12 representative tasks on 1× H200; x = GPU seconds log, y = params M, annotated by rank)** — Kairos-50M fastest but worse accuracy and ≈5× larger than Moirai 2.0 small; Granite-FlowState-R1 more accurate & smaller than Moirai 2.0 but ≈3× slower; **Moirai 2.0 small ≈30× smaller and 2× faster than Moirai-Large** while more accurate.

- **Scaling with size (Table 1, GIFT-Eval MASE/CRPS; lower better; 12-task efficiency not the same as full 97-task — here full GIFT-Eval)**:

| Model | Params (M) | MASE | CRPS |
|---|---|---|---|
| **Moirai 2.0 small** | **11.4** | **0.728** | **0.516** |
| Moirai 2.0 base | 87.1 | 0.732 | 0.525 |
| Moirai 2.0 large | 305 | 0.743 | 0.530 |

  No scaling benefit on this corpus — small saturates data; consistent with overall GIFT-Eval paper observation that cross-family scaling is not systematic without matched data scaling (cf. Kaplan et al. 2020 [19]).

- **Ablation — Moirai 1.0 → 2.0 (Table 2, GIFT-Eval MASE/CRPS)** — Isolates each change:

| Variant | Pretrain | Loss | Architecture | Projection | Multi-token | Autoreg. quantile dec. | Random mask | MASE | CRPS |
|---|---|---|---|---|---|---|---|---|---|
| Moirai 1.0 small | GIFT-Eval Pretrain | distribution | enc-only | linear | — | — | — | 0.946 | 0.65 |
| v0 | GIFT-Eval Pretrain | distribution | dec-only | linear | — | — | — | 0.9288 | 0.6469 |
| v1 | New Corpus | distribution | dec-only | linear | — | — | — | 0.85 | 0.58 |
| v2 | New Corpus | **quantile** | dec-only | linear | — | — | — | **0.744** | **0.553** |
| v3 | New Corpus | quantile | dec-only | linear | — | ✓ | — | 0.736 | 0.533 |
| v4 | New Corpus | quantile | dec-only | linear | — | ✓ | ✓ | 0.772 | 0.56 |
| v5 | New Corpus | quantile | dec-only | linear | ✓ | ✓ | ✓ | 0.739 | 0.527 |
| **Moirai 2.0** | **New Corpus** | **quantile** | **dec-only** | **residual block** | **✓** | **✓** | **✓** | **0.728** | **0.516** |

  Largest single gain = switch to quantile loss (v1→v2); dec-only + new corpus also substantial; recursive decoding + multi-token + residual projection complete the path; random masking alone (v3→v4) slightly degrades but helps when combined with multi-token.

- **Inference speedup (KV-cache case study, §3.3, p. 6)**: ~10K context → 1K pred ≈ **4×** with KV cache; 10K pred → **17×**; reflects decoder-only reuse vs masked encoder recomputation.

- **Additional notes**: Model plateaus with parameter count and declines at longer horizons (§5.3, Fig. 4) → future work on data scaling & long-horizon modeling; internal telemetry daily only (single frequency for that source).

## 💡 Limitations & Identified Research Gaps
- **No multivariate / covariate support**: Dropped in 2.0 due to limited high-quality covariate data; multivariate tasks treated as independent univariate — sparse, spiky EV regimes (arrival/departure, SoC, tariff, weather) not modeled jointly; future via synthetic causal data prior (§6, cf. Chronos-2 [3] approach).
- **Negative scaling on current corpus**: Base (87M) / Large (305M) underperform Small (11.4M) on same 36M/295B data (Table 1) → architecture-data mismatch; data scale/diversity must grow with params.
- **Long-horizon degradation**: Rank 8th on long horizons vs 4th short (Fig. 4); multi-token + recursive decoding mitigate but do not close gap — architectural innovation and data scaling needed.
- **Domain gap — Nature tasks**: Pretraining underrepresents natural/environmental series → weakest domain (Fig. 3); transport highly competitive suggests uneven domain utility.
- **Probabilistic limited to 9 quantiles**: Fixed `Q={0.1,…,0.9}` (equal-weighted) — no continuous sampling, no tail beyond 0.1/0.9 unless reweighted `w_q`; weighted variant mentioned but not evaluated.
- **Operationalization**: Agentic (LLM+time-series reasoning) and multimodal (text+image+series) future work highlighted; incident reasoning (cf. ARFBench) not addressed.
- **Domain gap for EV load**: No EV charging datasets (ACN, ElaadNL, Boulder, Pecan Street) evaluated — transfer to sparse, bursty EV loads unproven; covariate-free design is an open thesis gap.
- **Replication**: Results anchored to `gift-eval` replication code + Hugging Face release; internal telemetry not distributable (1.48B private obs).

## 📚 BibTeX & Citation Reference
```bibtex
@article{liu2026moirai2,
  title        = {Moirai 2.0: When Less Is More for Time Series Forecasting},
  author       = {Liu, Chenghao and Aksu, Taha and Liu, Juncheng and Liu, Xu and Yan, Hanshu and Pham, Quang and Savarese, Silvio and Sahoo, Doyen and Xiong, Caiming and Li, Junnan},
  journal      = {arXiv preprint arXiv:2511.11698v3 [cs.LG]},
  year         = {2026},
  url          = {https://arxiv.org/abs/2511.11698},
  eprint       = {2511.11698},
  archivePrefix= {arXiv},
  primaryClass = {cs.LG},
  note         = {Salesforce AI Research, 2026-02-04}
}
```

## 🔗 Key References & Citation Graph
- Cited Foundations in Vault: [[2017_Attention_Is_All_You_Need]] [Vaswani et al. 2017] — Transformer backbone; [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] — patching precedent; [[2022_RevIN_Reversible_Instance_Normalization]]-adjacent instance normalization (Kim et al. 2021 [20]); He et al. 2016 [16]-adjacent residual blocks; [[1997_Long_Short_Term_Memory]]-adjacent recurrent context for TTM/R1; Su et al. 2024 RoPE-adjacent (cf. §3 Transformer); Pope et al. 2023 Efficient Transformer Inference (KV-cache [27]).
- Time Series Foundation Models Compared: [[2024_TimesFM_Decoder_Only_Foundation_Model]] — TimesFM 1/2.x; Ansari et al. 2024 Chronos / 2025 Chronos-2 [2,3]; Woo et al. 2024 Moirai 1.0 [34] (masked-encoder predecessor); Liu et al. 2024 Moirai-MoE [21]; Auer et al. 2025 TiRex [4]; Graf et al. 2025 FlowState [15]; Feng et al. 2025 Kairos [11]; Wang et al. 2025 YingLong [32]; Ekambaram et al. 2024 TTM-R1/R2 [10]; Rasul et al. 2023 Lag-Llama [28]; Hoo et al. 2025 TabPFN-TS [17]; Liu et al. 2025 Sundial [22] — all appear in GIFT-Eval 30-model comparators (p. 8 list).
- Related Vault Papers: [[2025_Sundial_Highly_Capable_Time_Series_Foundation_Models]] — Sundial (TimeFlow + decoder-only) evaluated alongside Moirai 2.0 on same GIFT-Eval 30-model protocol (Fig. 2 comparators); [[2026_Toto_2_Scaling_Era]] — Toto 2.0 scaling TSFM that also uses GIFT-Eval-pretrain-adjacent corpora and contrasts scaling conclusions (Toto 2.0 monotonic scaling vs Moirai 2.0 plateau on fixed corpus).
- Generative / Probabilistic Line: Rasul et al. 2021 DeepAR-adjacent [12]; Oreshkin et al. 2019 N-BEATS [26]; Wen et al. 2017 Multi-horizon quantile RNN [33]; Kaplan et al. 2020 Scaling laws [19] — discussed in §5.3.

> [!IMPORTANT]
> **For Thesis Use**: Shows that **simpler = better** for TSFM — decoder-only + quantile loss + single patch + multi-token decoding beats mixture-distribution masked encoders on GIFT-Eval while being 30× smaller / 2× faster. Directly challenges thesis assumption that bigger encoder + richer distribution suffices; **quantile head + recursive multi-quantile beam** is the recipe to test for heterogeneous EV-like loads. Open thesis extensions: multivariate/covariate-aware fine-tuning (arrival/departure, SoC, tariff, weather+traffic via cross-attention on the quantile head), data scaling aligned with model capacity, and long-horizon stabilization — see [[research_gaps]].

## Extracted Reference Dump
Full extracted bibliography for this paper: `wiki/references/2026_Moirai_2_When_Less_Is_More_refs.md` (see refs dump)
