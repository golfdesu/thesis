---
type: paper
title: "Chronos-2: From Univariate to Universal Forecasting"
authors: [Abdul Fatir Ansari, Oleksandr Shchur, Jaris Küken, Andreas Auer, Boran Han, Pedro Mercado, Syama Sundar Rangapuram, Huibin Shen, Lorenzo Stella, Xiyuan Zhang, Mononito Goswami, Shubham Kapoor, Danielle C. Maddix, Pablo Guerron, Tony Hu, Junming Yin, Nick Erickson, Prateek Mutalik Desai, Hao Wang, Huzefa Rangwala, George Karypis, Yuyang Wang, Michael Bohlke-Schneider]
year: 2025
journal_conference: "arXiv preprint arXiv:2510.15821v1 [cs.LG] — Technical Report of Chronos-2 (Amazon Web Services)"
doi_url: "https://arxiv.org/abs/2510.15821"
models_used: ["[[Chronos-2]]", "[[Chronos]]", "[[Chronos-Bolt]]", "[[TimesFM]]", "[[TiRex]]", "[[Toto]]", "[[COSMIC]]", "[[Moirai]]", "[[Sundial]]", "[[TabPFN-TS]]", "[[AutoARIMA]]", "[[AutoETS]]", "[[AutoTheta]]", "[[PatchTST]]", "[[TFT]]", "[[DeepAR]]", "[[N-BEATS]]", "[[Transformer]]"]
datasets_used: ["[[fev-bench]]", "[[GIFT-Eval]]", "[[Chronos_Benchmark_II]]", "[[GIFT_Eval_Pretrain]]", "[[Chronos_Corpus]]", "[[Electricity]]", "[[M4]]", "[[Solar]]", "[[Traffic]]", "[[Weatherbench]]", "[[Wiki_Pageviews]]", "[[Buildings_900K]]"]
features_used: ["[[Historical_Load]]", "[[Known_Covariates]]", "[[Past_Only_Covariates]]", "[[Categorical_Covariates]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[SQL]]", "[[WQL]]", "[[MASE]]", "[[CRPS]]", "[[Win_Rate]]", "[[Skill_Score]]"]
tags: [paper, foundation-model, universal-forecasting, multivariate, covariate-informed, in-context-learning, group-attention, zero-shot, encoder-only]
---

# Summary: Chronos-2: From Univariate to Universal Forecasting

## 🎯 Main Objective & Contribution
- **Research question**: Can a single pretrained model handle the full spectrum of real-world forecasting tasks — univariate, multivariate, and covariate-informed (past-only / known-future, real-valued / categorical) — in a zero-shot manner without task-specific training or architectural changes?
- **Core contribution — [[Chronos-2]] (120M base; 28M small)**: First **universal** pretrained forecaster that replaces task-specific heads with **group attention** enabling in-context learning (ICL) across arbitrarily grouped time series. A single inference pipeline solves all four task families (Table 1, Table 2) via group-ID + future-input masking alone. State-of-the-art on all three comprehensive benchmarks — **fev-bench (100 tasks), GIFT-Eval (97 tasks / 55 datasets), Chronos Benchmark II (27 tasks)** — with the largest gains on covariate-informed tasks that prior TSFMs mostly ignore.
- **Two pillars**:
  1. **Group attention architecture** (encoder-only T5 + RoPE) that alternates **time attention** (self-attention along patches within one series) and **group attention** (attention across series at the same patch index within a group ID). Groups flexibly represent related series / multivariate variates / targets+covariates; memory scales **O(V)** vs O(V²) for flattened baselines (Table 1). 21-quantile direct multi-patch head, sinh-asinh robust scaling, patching with REG token.
  2. **Synthetic multivariate pretraining**: real univariate data (Table 6 select Chronos + GIFT-Eval corpora + TSI/TCM generators) + **entirely synthetic multivariate/covariate data** via **multivariatizers** (contemporaneous + sequential) that impose multivariate structure on univariate base generators (AR, ETS, TSI, KernelSynth). Enables universal ICL without scarce real multivariate data. Two-stage training: 2048 ctx → 8192 ctx post-training for long seasonalities / long horizons.
- **Empirical claim**: Chronos-2 beats every prior TSFM on all three benchmarks and beats **Chronos-Bolt** (its direct predecessor) decisively. On **fev-bench** (the only benchmark covering covariates) win rate **90.7%, skill 47.3%** SQL, statistically significant vs TiRex/TimesFM-2.5/Toto-1.0; inference **~3.6 s median, 300 series/s on single A10G**. Ablations: 28M small loses ≤1 pt skill, synthetic-only model nearly matches real+synthetic, long-context post-training helps GIFT-Eval.

## 🧠 Methodology & Model Architecture
- **Model Type**: Encoder-only Transformer (T5 encoder backbone). Pipeline (Fig. 1): Robust Scaling → Meta Features (time index + mask) → Patching → Patch Embedding (residual network) → REG separator token → Alternating Time/Group Attention stack → Residual block on future-patch embeddings of D targets → **Quantile Head** (direct multi-patch, 21 quantiles). Inference-only; zero-shot via group IDs + future inputs.

- **Key Equations** (verbatim, Section 3):

  **Eq. 1 — Robust scaling (historical)** (Section 3.1; standardize then sinh^{-1} to stabilize variance / dampen outliers; Burbidge et al. 1988; Uniejewski & Weron 2018):
  $$\tilde{v}_{t,d} = \sinh^{-1}\!\left(\frac{v_{t,d} - \mu_d}{\sigma_d}\right) \quad \text{for } t \in \{1,\dots,T\} \tag{1}$$
  where $\mu_d,\sigma_d$ are mean/std of observed historical values $[v_{1,d},\dots,v_{T,d}]$ (missing values excluded).

  **Eq. 2 — Robust scaling (future known covariates)**:
  $$\tilde{w}_{t,d} = \sinh^{-1}\!\left(\frac{w_{t,d} - \mu_d}{\sigma_d}\right) \quad \text{for } t \in \{T+1,\dots,T+H\} \tag{2}$$
  Same $\mu_d,\sigma_d$ as Eq. 1 (future normalized with historical stats). Concatenated as $U=[\tilde{V},\tilde{W}] \in \mathbb{R}^{(T+H)\times(D+M)}$.

  **Eq. 3 — Patching and embedding** (Section 3.1; non-overlapping patches length $P$, context and future patched separately with left/right zero-padding if needed; $u_p,j_p,m_p$ = p-th patches of input / time-index / mask; $D_{\text{model}}$ = hidden dim):
  $$h_p = f^{\phi}_{\text{in}}\!\left([u_p, j_p, m_p]\right),\quad \phi: \mathbb{R}^{3P} \to \mathbb{R}^{D_{\text{model}}} \tag{3}$$
  where $f^{\phi}_{\text{in}}$ is a residual network, $[u_p,j_p,m_p]$ denotes concatenation. Between context and future patch embeddings a special **REG token** is inserted (separator + attention sink, Xiao et al. 2024).

  Meta features appended per dimension: **time index** $j=[-T/C,-(T-1)/C,\dots,0,\dots,(H-1)/C]$ ($C$ = max context length; gives explicit temporal ordering under patching) and **binary mask** $m_d \in \{0,1\}$ (1=observed; indicates missing history and which future dims are known covariates; missing $u_d$ replaced by 0 after mask construction).

  Input construction (Section 3.1): $V=[v_1,\dots,v_T],\, v_t\in\mathbb{R}^{D+M}$ (targets $y_t$ + covariates $x_t$ concatenated); $W=[w_{T+1},\dots,w_{T+H}]$ (known future covariates $x_t$ when available, else missing). **Categorical covariates**: univariate targets → **target encoding** (Micci-Barreca 2001); multivariate targets → **ordinal encoding**.

  Architecture (Section 3.2): **Time Attention** = standard self-attention along temporal axis with **RoPE** (Su et al. 2024, replaces T5 relative embeddings). **Group Attention** = attention across all series within same group at each patch index; groups identified by vector $g$ of length batch size $B$ mapped to 2D attention mask (within-group only); **no positional embeddings** (series within group unordered). **Quantile Head**: after alternating stack, future-patch embeddings of $D$ target dims passed through residual block → $\hat{Z}\in\mathbb{R}^{H\times D\times|Q|}$, $|Q|=21$, $Q=\{0.01,0.05,0.1,\dots,0.9,0.95,0.99\}$ (vs 9-level grid in prior work; extremes improve anomaly/risk coverage).

  **Eq. 4 — Quantile regression objective** (Section 3.3; loss averaged over forecast steps + batch; only target dims contribute; known-covariate/missing entries excluded; number of output patches randomly sampled per batch):
  $$\mathcal{L} = \sum_{q\in Q}\big(q\cdot\max(z-\hat{z}_q,0)+(1-q)\cdot\max(\hat{z}_q-z,0)\big) \tag{4}$$
  where $z$ is target normalized as in Eq. 1, $\hat{z}_q$ is predicted quantile $q$ forecast.

  **Eq. 5 — Inference denormalization** (Section 3.4; invert Eq. 1):
  $$\hat{y}^q_{t,d} = \mu_d + \sigma_d\cdot\sinh(\hat{z}^q_{t,d}) \tag{5}$$
  Quantile predictions for horizon $H$ produced in one forward pass (direct multi-step, multi-patch output; no autoregressive rollout).

  **Grouping for inference** (Table 2, Section 3.4): univariate → each item unique group ID, $W=$ all missing ($*$); multivariate → all variates of same multivariate series share one ID; covariate-informed → target(s)+past-only+known covariates share one ID with known futures in $W$; **full cross learning** → entire batch one group. Training batches are heterogeneous mixtures of the three task types. Two-stage training: Stage 1 max ctx 2048 / few output patches; Stage 2 extend to **8192 ctx** + more output patches (captures long seasonalities in high-frequency data, long horizons without heuristics).

## 📊 Dataset & Input Features
- **Pretraining corpus** (Section 4, Table 6 Appendix):
  - **Real univariate** (select Chronos + GIFT-Eval corpora; full list Table 6 — e.g. Electricity 370 series, KDD Cup, M4 Daily/Hourly/Monthly/Weekly, Mexico City Bikes, Pedestrian Counts, Solar 5166, Taxi 2428, Uber TLC 262, USHCN 225280, Weatherbench 225280, Wiki 100000, Wind Farms, Temperature-Rain, London Smart Meters 5560, Alibaba/Azure/Borg cluster traces 100000 each, LargeST 8196, Q-Traffic 45148, Buildings 900K 100000; multiple frequencies per dataset — 5min/10min/15min/30min/1H/1D/1W/1M).
  - **Synthetic univariate**: **TSI** (Trend-Seasonality-Irregularity; Bahrpeyma et al. 2021) + **TCM** (Temporal Causal Model; Runge et al. 2023, random causal graphs → autoregression) + AR/ETS/KernelSynth base generators.
  - **Synthetic multivariate/covariate — entirely synthetic**: **Multivariatizers** sampling from base univariate generators and imposing dependencies: **contemporaneous** (linear/nonlinear same-timestep transforms → instantaneous correlations) + **sequential** (cross-time dependencies → lead-lag, cointegration). Random subset of variates designated as known covariates to create covariate-informed tasks.

- **Evaluation benchmarks** (Section 5.1; none of the test portions seen during training):
  - **[[fev-bench]]** (Shchur et al. 2025) — **100 tasks**, the benchmark for universal forecasting: univariate (32) / multivariate (26) / covariate-informed (42, past-only + known). Metric **SQL** (Scaled Quantile Loss). Leakage and failure counts reported.
  - **[[GIFT-Eval]]** (Aksu et al. 2024) — **97 tasks / 55 datasets**, emphasis high-frequency + long horizons. Metrics **WQL** (Weighted Quantile Loss) + **MASE**. Pretraining corpus excluded test portions; partial overlap with train portions exists (strictly zero-shot synthetic-only variant also reported).
  - **[[Chronos_Benchmark_II]]** (Ansari et al. 2024) — **27 tasks**, mostly short histories (<300 steps avg). Metrics WQL + MASE.
  - **Domain case studies** (Section 5.3): 16 energy tasks + 17 retail tasks from fev-bench with dynamic covariates; illustrated with **EPF-DE** (German energy price, hourly day-ahead with load + solar/wind covariates, Fig. 6) and **Rossmann** weekly store sales (promotion/holiday features, Fig. 7).

- **Data Availability & Links**:
  - Code: https://github.com/amazon-science/chronos-forecasting
  - Paper: https://arxiv.org/abs/2510.15821
  - GluonTS: https://github.com/awslabs/gluonts
  - AutoGluon: https://auto.gluon.ai
  - Benchmarks: fev-bench (Shchur et al. 2025), GIFT-Eval (https://huggingface.co/datasets/Salesforce/GiftEval), Chronos Benchmark II (Ansari et al. 2024)

- **Features**: Historical values $Y_{1:T}$ plus covariates $X_{1:T+H}$ (real-valued + categorical; past-only and known-future distinguished via mask/future inputs $W$). Meta features: time index $j$ + binary mask $m_d$.

- **Preprocessing**: Robust scaling Eq. 1-2 (standardize → $\sinh^{-1}$), categorical target/ordinal encoding, patching $P$ with REG token, per-dimension independent processing.

## 📈 Performance & Results
- **fev-bench — SQL (Table 3; win rate W / skill S vs Seasonal Naive; median runtime, leakage, failures)** — lower SQL is better, higher W/S is better:
  - Chronos-2: **W 90.7%, S 47.3%, 3.6s, 0% leakage, 0 failures**
  - Next best: TiRex 80.8/42.6/1.4s, TimesFM-2.5 75.9/42.3/16.9s, Toto-1.0 66.6/40.7/90.7s, COSMIC 65.6/39.0/34.4s, Moirai-2.0 61.1/39.3/2.5s, Chronos-Bolt 60.3/38.9/1.0s, TabPFN-TS 59.3/39.6/305.5s, Sundial 41.0/33.4/35.6s
  - Pairwise 95% CIs (bootstrap, Fig. 2) confirm Chronos-2 statistically significantly outperforms every baseline on both W and S (CIs exclude 50% and 0% respectively).

- **GIFT-Eval** (Table 4):
  - WQL — W/S: Chronos-2 **81.9/51.4**, TimesFM-2.5 77.5/51.0, TiRex 76.5/50.2, Toto-1.0 67.4/48.6, Moirai-2.0 64.4/48.4, COSMIC 56.4/44.5, Chronos-Bolt 53.8/42.6, Sundial 49.1/44.1
  - MASE — W/S: Chronos-2 **83.8/30.2**, TimesFM-2.5 77.7/29.5, TiRex 71.9/27.6, Moirai-2.0 64.3/27.2

- **Chronos Benchmark II** (Table 5):
  - WQL — W/S: Chronos-2 **79.8/46.6**, TiRex 70.4/41.7, TimesFM-2.5 70.0/42.4, Toto-1.0 60.9/41.9
  - MASE — W/S: Chronos-2 **81.5/26.5**, TimesFM-2.5 71.6/23.3, TiRex 67.1/22.2

- **ICL gains over univariate mode** (Section 5.2, Fig. 3-4):
  - Univariate tasks: ICL adds stacked-bar gain on SQL (fev-bench uni subset: 36.0→37.0 skill etc.) and WQL/MASE; strongest on **Chronos Benchmark II** (short histories — cross learning compensates limited context).
  - Multivariate subset (fev-bench 26 tasks): **modest** ICL gains; univariate Chronos-2 already beats multivariate Toto-1.0; discussion invokes Takens embedding theorem — long histories may make univariate strong.
  - Covariate-informed subset (42 tasks): **largest ICL gains** — Chronos-2 uni→ICL 40.0→47.0 skill SQL (fev-bench), far ahead of TabPFN-TS/COSMIC (the only baselines with covariate support). Energy and retail case studies (Fig. 5): Chronos-2 ICL 51.3 vs TiRex 38.6 on energy-SQL; 48.6 vs TabPFN-TS 42.1 on retail-WQL; Figs. 6-7 show covariate-aware forecasts sharply track price/sales dynamics.

- **Ablations** (Fig. 8, Section 5.4):
  - **Model size**: Chronos-2-Small **28M** vs 120M base — near-parity on GIFT-Eval (50.4 vs 51.4 skill WQL), ~2× faster, ideal for CPU/low-resource.
  - **Synthetic-only**: Chronos-2-Synth (only synthetic data) — only slightly below real+synthetic on GIFT-Eval/Chronos Bench II (50.4 vs 51.4 WQL GIFT, 46.4 vs 46.6); larger gap on fev-bench (45.9 vs 47.3 SQL) but still strong → evidence synthetic data may eventually suffice.
  - **Long-context post-training** (2048→8192): gains especially on GIFT-Eval high-frequency seasonalities (51.4 vs 50.1 WQL; fev-bench 47.3 vs 46.9 SQL).

## 💡 Limitations & Identified Research Gaps
- **Covariate scope**: Only numeric + categorical covariates; **multimodal (e.g. text) covariates** not supported — noted as promising future direction (Zhang et al. 2025).
- **ICL limited on multivariate**: Gains smallest on multivariate subset; suggests current multivariate leverage may not yet exploit cross-variate structure as effectively as covariate usage — room for stronger multivariate ICL.
- **No EV-specific evaluation**: Benchmarks are general time-series; performance on **EV charging load** with its specific covariates (ToU price, weather, SoC, arrival/departure) not evaluated — direct thesis transfer gap.
- **Synthetic gap on fev-bench**: Synthetic-only variant shows meaningful gap on the most diverse/covariate-heavy benchmark, implying synthetic multivariatizers not yet fully capturing real-world dependency diversity.
- **Context vs horizon trade-offs not ablated for forecasting horizons relevant to EV** (day-ahead vs ultra-long); long-context post-training gains are aggregate, not broken out by horizon frequency.
- **Scalability upper bound** not explored beyond 120M; whether group attention scales to hundreds of variates / very large groups untested.

## 📚 BibTeX & Citation Reference
```bibtex
@misc{ansari2025chronos2,
  author       = {Ansari, Abdul Fatir and Shchur, Oleksandr and K{\"{u}}ken, Jaris and Auer, Andreas and Han, Boran and Mercado, Pedro and Rangapuram, Syama Sundar and Shen, Huibin and Stella, Lorenzo and Zhang, Xiyuan and Goswami, Mononito and Kapoor, Shubham and Maddix, Danielle C. and Guerron, Pablo and Hu, Tony and Yin, Junming and Erickson, Nick and Desai, Prateek Mutalik and Wang, Hao and Rangwala, Huzefa and Karypis, George and Wang, Yuyang and Bohlke-Schneider, Michael},
  title        = {Chronos-2: From Univariate to Universal Forecasting},
  year         = {2025},
  howpublished = {arXiv preprint arXiv:2510.15821v1 [cs.LG]},
  eprint       = {2510.15821},
  archivePrefix= {arXiv},
  primaryClass = {cs.LG},
  url          = {https://arxiv.org/abs/2510.15821}
}
```

## 🔗 Key References & Citation Graph
- Cited Foundations in Vault (representative; full list 70+ refs pp.15-19, see companion _refs.md):
  - [[2024_Ansari_Chronos_Learning_Language_Time_Series]] [Ansari et al. TMLR 2024 — Chronos] — direct predecessor; Chronos-2 extends it with universal capabilities.
  - [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] [Das et al. ICML 2024 — TimesFM] — contemporaneous TSFM baseline beaten on all 3 benchmarks.
  - [[2025_Auer_TiRex_Zero_Shot_Forecasting]] [Auer et al. NeurIPS 2025 — TiRex] — strong baseline on fev-bench, 2nd place.
  - [[2025_Cohen_Toto_Observability_Perspective]] [Cohen et al. NeurIPS 2025 — Toto 1.0] — multivariate baseline; Chronos-2 uni-mode already beats Toto.
  - [[2024_Woo_Unified_Training_Universal_Forecasting]] [Woo et al. ICML 2024 — Moirai] — multivariate-flattened baseline, O(V squared).
  - [[2025_Liu_Sundial_Family_Time_Series_Foundation_Models]] [Liu et al. ICML 2025 — Sundial] — univariate baseline.
  - [[2025_Hoo_TabPFN_TS_Tables_to_Time]] [Hoo et al. 2025 — TabPFN-TS] — tabular-to-TS adaptation; only other model with known-covariate support; 2nd on fev-bench covariates subset.
  - [[2025_Auer_COSMIC_Zero_Shot_Covariates_ICL]] [Auer et al. 2025a — COSMIC] — covariate-informed via synthetic augmentations, univariate target only.
  - [[2024_Aksu_GIFT_Eval_Benchmark]] [Aksu et al. 2024 — GIFT-Eval] — evaluation benchmark.
  - [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] / [[2021_Lim_TFT_Temporal_Fusion_Transformers]] / [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] — patching / TFT / probabilistic heritage.
  - Position/method: [[2017_Attention_Is_All_You_Need]] [Vaswani et al. 2017], [[2020_Raffel_T5_Exploring_Limits]] [Raffel et al. 2020 — T5 encoder], [[2024_Su_RoFormer_Rotary_Position_Embedding]] [Su et al. 2024 — RoPE].

> [!IMPORTANT]
> **For Thesis Use**: First **universal** TSFM proving **group attention + synthetic multivariatizers** can solve multivariate + covariate-informed tasks zero-shot with **O(V) memory** and no architectural change per task. Direct relevance to thesis gap on **covariate-aware EV load forecasting** (ToU, weather, SoC, arrival/departure as past-only/known covariates). Strong evidence that **synthetic-only** pretraining is viable (ablation nearly matches real+synthetic) — supports synthetic augmentation for scarce EV data. ICL cross-learning gains are largest where thesis needs them (covariates) and portable to short-history stations (cold-start). Open gap: extend Chronos-2 to **EV benchmarks** and **multimodal covariates** (text/schedule).

## Extracted Reference Dump
> 70+ references (pp.15-19); full dump in [[2025_Ansari_Chronos_2_Univariate_to_Universal_refs]].
