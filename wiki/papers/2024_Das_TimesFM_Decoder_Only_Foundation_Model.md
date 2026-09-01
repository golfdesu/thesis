---
type: paper
title: "A Decoder-Only Foundation Model for Time-Series Forecasting"
authors: [Abhimanyu Das, Weihao Kong, Rajat Sen, Yichen Zhou]
year: 2024
journal_conference: "arXiv preprint arXiv:2310.10688v4 [cs.CL]"
doi_url: "https://arxiv.org/abs/2310.10688"
models_used: ["[[TimesFM]]", "[[PatchTST]]", "[[N-BEATS]]", "[[DeepAR]]", "[[WaveNet]]", "[[Transformer]]", "[[Informer]]", "[[Autoformer]]", "[[FEDFormer]]", "[[TimesNet]]", "[[DLinear]]", "[[ARIMA]]", "[[ETS]]", "[[TBATS]]", "[[Theta]]", "[[CatBoost]]", "[[LLMTime]]", "[[TimeGPT-1]]"]
datasets_used: ["[[Google_Trends]]", "[[Wikipedia_Pageviews]]", "[[M4]]", "[[Electricity]]", "[[Traffic]]", "[[Weather]]", "[[Favorita_Retail]]", "[[LibCity]]", "[[Monash_Archive]]", "[[Darts]]", "[[ETT]]"]
features_used: ["[[Historical_Load]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[msMAPE]]", "[[MSE]]"]
tags: [paper, foundation-model, decoder-only, zero-shot, time-series-forecasting]
---

# Summary: A Decoder-Only Foundation Model for Time-Series Forecasting (TimesFM)

## 🎯 Main Objective & Contribution
- **Research question**: Can a single decoder-only Transformer pretrained on massive time-series data achieve strong zero-shot forecasting across diverse unseen datasets, domains, horizons and granularities — analogous to LLMs in NLP?
- **Core contribution — [[TimesFM]] (Time-series Foundation Model)**: First practical **decoder-only** patched foundation model (200M params, up to ~100B time-points pretraining) with **input patching + causal attention + longer output patches + patch masking** enabling variable context/horizon/granularity zero-shot inference. Out-of-the-box accuracy comes close to SOTA supervised models trained per-dataset.
- **Two pillars**:
  1. Large-scale pretraining corpus from **Google Trends (~0.5B pts, 22k head queries)** + **Wiki Pageviews (~300B pts, 5.6M hourly series)** + **3M synthetic series (6.1B pts, ARMA + seasonal + trend + step)** + M4/Electricity/Traffic/Weather/Favorita/LibCity (Table 1, ~100B total after mixing; 80% real / 20% synthetic with equal weight to hourly+sub-hourly / daily / weekly / monthly groups).
  2. Decoder-only architecture that predicts the **next output patch (longer than input patch)** conditioned on all past patches in parallel — supports any context length via random first-patch fractional masking.
- **Empirical claim**: Single TimesFM model is **SOTA or within significance of SOTA** zero-shot on held-out **Monash (18 datasets)**, **Darts (8 series)**, and **ETT (4 datasets × 2 horizons)** — beating LLM-based forecaster [[LLMTime]] (GPT-3) by >25% on Monash and beating most supervised long-horizon baselines, despite being orders of magnitude smaller than LLMs. Follow-up FINETUNING on only 10% of ETT data (tuning only Input/Output Residual Blocks) still beats GPT4TS and full-data supervised baselines (Table 2).

## 🧠 Methodology & Model Architecture
- **Model Type**: Decoder-only Transformer with patching. Three stages: Input Residual Block → Stacked Causal Transformer → Output Residual Block. Three model scales ablated: **17M (10 layers, d=512)**, **70M (10 layers, d=1024)**, **200M (20 layers, d=1280, 16 heads, input_patch_len=32, output_patch_len=128, dropout 0.2)**.

- **Key Equations** (verbatim, §3-4 and Appendix A.2/A.7):

  **Eq. 1 — Zero-shot forecasting task**:
  $$f: (y_{1:L}) \rightarrow \hat{y}_{L+1:L+H}$$

  **Eq. 2 — Input token from patch + padding mask + positional encoding** (p = input_patch_len, N = ⌊L/p⌋ patches):
  $$t_j = \text{InputResidualBlock}(\tilde{y}_j \odot (1 - \tilde{m}_j)) + PE_j$$
  where $\tilde{y}_j = y_{p(j-1)+1:pj}$, $\tilde{m}_j = m_{p(j-1)+1:pj}$, binary mask $m_{1:L}$, $PE_j$ = sinusoidal PE [VSP+17]. Residual Block = MLP with one hidden layer + skip connection (as in TiDE [DKL+23]); hidden dim = model_dim.

  **Eq. 3 — Stacked causal Transformer** (num_layers transformer layers, causal multi-head SA + FFN, hidden = model_dim, layer-norm; masked patches not attended):
  $$o_j = \text{StackedTransformer}((t_1, \dot{m}_1), \cdots, (t_j, \dot{m}_j)),\quad \forall j \in [N]$$
  where $\dot{m}_j = \min\{m_{p(j-1)+1:pj}\}$ (patch masked only if all points masked).

  **Eq. 4 — Output patch prediction** (output_patch_len = h, can be > p, e.g. p=32, h=128):
  $$\hat{y}_{pj+1:pj+h} = \text{OutputResidualBlock}(o_j)$$

  **Eq. 5 — Decoder-only training loss** (point forecasting MSE, averaged over all patches; probabilistic variant = multiple quantile heads or distribution logits with NLL):
  $$\text{TrainLoss} = \frac{1}{N}\sum_{j=1}^{N} \text{MSE}(\hat{y}_{pj+1:pj+h},\, y_{pj+1:pj+h})$$

  **Eq. 6 — MAE metric** (Monash/Darts/ETT reporting):
  $$\text{MAE}(y_{L+1:L+H}, \hat{y}_{L+1:L+H}) = \frac{1}{H}\|y_{L+1:L+H} - \hat{y}_{L+1:L+H}\|_1$$

  **Eq. 7 — msMAPE** (Monash official, ϵ=0.1):
  $$\text{msMAPE}(y_{L+1:L+H}, \hat{y}_{L+1:L+H}) = \frac{1}{H}\sum_{i=1}^{H} \frac{2|y_{L+i} - \hat{y}_{L+i}|}{\max\{|y_{L+i}| + |\hat{y}_{L+i}| + \epsilon,\, 0.5 + \epsilon\}}$$

  **Eq. 8 — Date-feature extension** (discussed but not used; future work):
  $$f: (y_{1:L}, x_{1:L+H}) \rightarrow \hat{y}_{L+1:L+H}$$
  where $x_t \in \mathbb{R}^r$ = date-derived features (day-of-week, month, etc.).

- **Design principles**:
  - *Patching*: token = contiguous patch (analogous to LLM token); reduces tokens by factor p and improves speed; p=32 chosen as best speed/accuracy tradeoff (Fig. 3c: p=16/32 best, p=32 ~2× faster than p=16).
  - *Decoder-only*: unlike PatchTST encoder-decoder, every prefix of patches predicts next h steps in parallel — enables variable context lengths natively.
  - *Longer output patches* (h=128 vs p=32): middle ground between 1-token AR and one-shot full-horizon prediction [ZCZX23]; e.g. 256-context → 256-horizon needs only 2 AR steps (257-384, 385-512) vs 8 steps if h=32. Monotonic MAE improvement with larger h up to 128 (Fig. 3b, 512-step ETT task).
  - *Patch masking*: random $r \sim U[0,p-1]$ masked in first patch per batch covers all context lengths 1 … max_len (e.g. 512; weekly=256, monthly=64 due to short series). Standard + reversible instance normalization only (mean/std of first patch).

- **Training**: Mini-batch gradient descent, decoder-only over all windows/time-series; cosine decay LR (peak 5e-4), layer-norm in transformer, global batch 4096, 1.5M iterations on TPUv5e 16 cores (~2 days for 200M). Inference = autoregressive decoding concatenating predictions as new context (zero-pad + mask if L not multiple of p).

- **Synthetic data generator** (Appendix A.8, AR p,q∈[1,8] with Gaussian/uniform coeffs, sine/cosine seasonal periods ∈[4, max_len/2], piecewise linear trends 2-8 segments, step functions; randomly enabled and summed with uniform weights, 50% multiplicative trend; each series length 2048).

## 📊 Dataset & Input Features
- **Pretraining corpus composition** (Table 1, §5; total ~100B time-points after mixing):

| Source | Granularity | # Series | # Points |
|---|---|---|---|
| Synthetic | — | 3,000,000 | 6,144,000,000 |
| Wiki hourly | Hourly | 5,608,693 | 239,110,787,496 |
| Wiki daily | Daily | 68,448,204 | 115,143,501,240 |
| Wiki weekly | Weekly | 66,579,850 | 16,414,251,948 |
| Wiki monthly | Monthly | 63,151,306 | 3,789,760,907 |
| Trends hourly | Hourly | 22,435 | 393,043,680 |
| Trends daily/weekly/monthly | D/W/M | 22,435 each | ~143M combined |
| M4 (hourly/daily/monthly/quarterly/yearly) | mixed | ~99k | ~23M |
| Electricity (hourly) | Hourly | 321 | 8,443,584 |
| Traffic (hourly) | Hourly | 862 | 15,122,928 |
| Weather 10-min [ZZP+21] | 10-min | 42 | 2,213,232 |
| Favorita Sales (daily) | Daily | 111,840 | 139,179,538 |
| LibCity 15-min [WJJ+23] | 15-min | 6,159 | 34,253,622 |

- **Evaluation datasets (held-out from pretraining)**:
  - **[[Monash_Archive]]** [GBW+21] — 30 datasets → 18 without missing values used: `australian electricity demand, bitcoin, pedestrian counts, weather, nn5 daily, nn5 weekly, tourism yearly, tourism quarterly, tourism monthly, cif 2016, covid deaths, fred md, traffic hourly, traffic weekly, saugeenday, us births, hospital, solar weekly`. Domains: finance, demand, weather, traffic; granularities minutes → yearly. Evaluated with naive-scaled MAE (geometric mean reporting).
  - **[[Darts]]** [HLP+22] — 8 univariate series: AirPassengers, AusBeer, GasRateCO2, MonthlyMilk, Sunspots, Wine, Wooly, HeartRate. Individual MAE reported.
  - **[[ETT]]** [ZZP+21] — ETTh1, ETTh2 (hourly) + ETTm1, ETTm2 (15-min), electricity transformer temperatures, 2-year span; horizons 96/192 with context 512 (last test window evaluation to save llmtime cost).

- **Other datasets referenced** (baselines / not in eval): ElectricityLoadDiagrams, Ausgrid, London Smart Meters (excluded from other studies due to leakage — not in this paper's eval).

- **Data Availability & Links**:
  - Google Trends: https://trends.google.com (hourly Jan 2018–Dec 2019; daily/weekly/monthly Jan 2007–Dec 2021; 22k head queries, >50% sparsity threshold)
  - Wikimedia Pageviews: https://wikimedia.org/api/rest_v1/ (Jan 2012–Nov 2023, hourly→aggregated)
  - Monash Huggingface mirror: https://huggingface.co/datasets/monash_tsf
  - Darts: https://github.com/unit8/darts
  - Informer/ETT: original datasets from [ZZP+21]
  - M4: https://github.com/Mcompetitions/M4-methods
  - **No public TimesFM weights at publication time** — paper commits to open-weights release with model card [MWZ+19]; code for llmtime baseline at https://github.com/ngruver/llmtime/blob/main/experiments/run_monash.py

- **Features**: Purely **univariate** — only past values $y_{1:L}$ as input; no static/dynamic covariates during pretraining. Date-derived features discussed as future work (Eq. 8) with two proposed covariate handling strategies: (i) zero-shot residual linear regression on covariates, (ii) finetuning with covariate embeddings in residual blocks.

- **Preprocessing**: Standard normalization (RevIN standard part only, per-series mean/std of first input patch). Max context 512 (256 for weekly, 64 for monthly due to short series).

## 📈 Performance & Results
- **Monash (18 datasets, scaled MAE — lower is better, Table 4 & Fig. 2a/4a)**:
  - Geometric mean scaled MAE: **[[TimesFM]] 0.6846** (best), [[N-BEATS]] 0.7005, [[CatBoost]] 0.7044, [[FFNN]] 0.7477, [[WaveNet]] 0.7733, [[PR]] 0.7736, [[DeepAR]] 0.8104, [[Transformer]] 0.9384, [[LLMTime]] (GPT-3 ZS) 0.9715, [[ETS]] 0.9337, ARIMA 0.9449, SES 1.0855. Arithmetic mean: TimesFM 0.8005 vs N-BEATS 0.7844 (within significance of top).
  - TimesFM is **top model overall**, >25% better than [[LLMTime]] (GPT-3) and better than supervised DeepAR/WaveNet/Transformer/CatBoost; within significance of N-BEATS (the strongest supervised baseline on Monash).
  - Per-dataset wins: best on `australian electricity demand` (448.81), `covid deaths` (209.80), `fred md` (947.12), `solar weekly` (1258.27), `traffic hourly` (0.01) among others (see Table 4).

- **Darts (8 series, scaled MAE, Table 3 & Fig. 2b)**:
  - GM scaled MAE: ARIMA 0.5219 (best), [[LLMTime]] 0.4882* (GM) / 0.6045 (AM) — note table shows GP/ARIMA/TCN/etc., TimesFM **0.5767** (GM) / 0.6829 (AM), PatchTST 0.6458/0.7462, N-BEATS 0.7316, TCN 0.7946. TimesFM within significance of top (wide CIs due to n=8 series); competitive with seasonal ARIMA which required manual seasonality tuning. llmtime data-contamination cannot be ruled out (series used in blog posts).

- **ETT — Informer long-horizon (last-window MAE, Table 5 & Fig. 2c)** — context 512, horizons 96/192:
  - Average MAE (8 tasks): **[[TimesFM]] (ZS) 0.36** (best), PatchTST 0.37, PatchTST(ZS) 0.35, [[LLMTime]] 0.45, FEDFormer 0.53, AutoFormer 0.53, Informer 0.99. TimesFM beats or ties SOTA supervised PatchTST and is significantly better than FEDFormer/AutoFormer/Informer and llmtime.
  - Best on ETTm1 (0.19/0.26 vs PatchTST 0.33/0.31) and competitive on ETTh1/ETTh2/ETTm2.

- **Finetuning (10% of ETT training data, only Input/Output Residual Blocks tuned, Table 2, same protocol as GPT4TS [ZNW+23])**:
  - TimesFM(FT) dominates: ETTh1 avg MAE **0.426** vs GPT4TS(FT) 0.525, PatchTST 0.542, DLinear 0.600, FEDFormer 0.561, Autoformer 0.596. ETTh2 avg 0.410 vs GPT4TS 0.421. ETTm1 avg **0.388** vs GPT4TS 0.441, DLinear 0.429. ETTm2 avg **0.334** vs GPT4TS 0.335. Gains: +18% (ETTh1), +3% (ETTh2), +12% (ETTm1) over GPT4TS. 10%-finetuned TimesFM is already comparable/better than most baselines trained on 100% data (Table 14 of [ZNW+23]).

- **Ablations (Fig. 3)**:
  - *Scaling* (Fig. 3a): Monash scaled MAE (GM) decreases monotonically with FLOPs across 17M → 70M → 200M (7 checkpoints); power-law-like improvement.
  - *Output patch length* (Fig. 3b, 512-step ETT): monotonic MAE decrease as h = 8 → 128 (fewer AR steps → better).
  - *Input patch length* (Fig. 3c, 70M Monash): p=16 and 32 best; p=8 slower and worse; p=64/128 worse (shifts toward encoder-decoder regime); p=32 chosen as 2× faster than p=16.
  - *Synthetic data* (Fig. 3d): removing synthetic → clear drop on Monash (under-represented granularities: quarterly/yearly/10-min) and on ETTm (15-min), no difference on ETTh (hourly well-represented).
  - *PatchTST pretraining control* (A.4): same data/FLOPS, 200M PatchTST(ZS) (stride 16) underperforms TimesFM on Monash (wrong context distribution) and similar on ETT (512 context) — encoder-decoder needs exhaustive (context, horizon) pretraining pairs, more expensive.

## 💡 Limitations & Identified Research Gaps
- **Probabilistic forecasting not evaluated**: Only point MSE loss; quantile heads / distribution NLL discussed (§4 Loss, A.1) but left to future work/finetuning. No CRPS/Winkler/PICP reporting.
- **No covariates**: Model is univariate-only at pretraining; multivariate / exogenous handling (weather, price, traffic) unsolved — paper proposes residual regression or finetuning with embeddings but does not test them. Directly relevant gap for EV load forecasting (arrival/departure, SoC, tariff, weather+traffic all unused).
- **Granularity imbalance**: Performance relies on synthetic data to cover rare granularities (quarterly/yearly/weekly); real data dominated by hourly/daily. Monthly/weekly max context shortened (64/256) due to short series.
- **No EV or station-level evaluation**: Benchmarks are generic (Monash/Darts/ETT); no EV charging datasets (ACN, ElaadNL, Palo Alto, etc.) tested — transfer to highly sparse, spiky EV loads unproven.
- **No hyperparameter tuning of pretraining**: Single LR schedule, fixed architecture; authors note MLP [CLY+23] or SSM/Mamba [GD23] alternatives and broader HPO not explored due to compute cost.
- **Data contamination / leakage risk**: Monash/Darts/ETT are public; overlap with web-scale pretraining not rigorously audited (unlike Meyer et al. 2025 contamination controls). TimeGPT-1 comparison omitted (not public).
- **Interpretability**: Deep foundation model less interpretable than statistical baselines; SHAP/LOCO suggested but not demonstrated.
- **Prompt/context tuning**: Context-length selection done via small validation sweep on Monash (32 vs 64 vs 512); systematic prompt-tuning / chain-of-thought analogues for time-series unclear.
- **Compute reporting**: Final 200M run = 16×TPUv5e × 2 days; total experimentation cost higher — equitability concern if weights not released promptly.

## 📚 BibTeX & Citation Reference
```bibtex
@misc{das2024decoderonlyfoundationmodeltimeseries,
  author       = {Abhimanyu Das and Weihao Kong and Rajat Sen and Yichen Zhou},
  title        = {A Decoder-Only Foundation Model for Time-Series Forecasting},
  year         = {2024},
  howpublished = {arXiv preprint arXiv:2310.10688v4 [cs.CL]},
  eprint       = {2310.10688},
  archivePrefix= {arXiv},
  primaryClass = {cs.CL},
  url          = {https://arxiv.org/abs/2310.10688},
  doi          = {10.48550/arXiv.2310.10688}
}
```

## 🔗 Key References & Citation Graph
- Cited Foundations in Vault: [[2017_Attention_Is_All_You_Need]] [VSP+17] — Transformer base; [[2022_Kim_RevIN_Reversible_Instance_Normalization]] [KKT+21] — normalization; [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] [NNSK22] — patching inspiration; [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] [ZCZX23] — one-shot vs AR decoding; [[2024_Das_TiDE_Long_Term_Forecasting]] [DKL+23] — residual block design; [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] [ZZP+21] — ETT benchmark; [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] [WXWL21]; [[2022_Zhang_GCN_TRN_EV_Availability]]-adjacent FEDFormer [ZMW+22]; [[2023_Wu_TimesNet_Temporal_2D_Variation_Modeling]]; [[2018_Bai_Empirical_TCN_Sequence_Modeling]] [BBO17]; [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]] [OCCB19]; [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] [SFGJ20]; [[2023_Cao_Treatment_Effects_Continuous_Time_Hidden_Confounders]]-adjacent TimeGPT-1 [GMC23]; LLMTime [GFQW23]; Scaling laws [KMH+20][HBM+22]; Mamba [GD23]
- Related Vault Papers: [[2025_Meyer_Benchmark_Foundation_Models]] — benchmarks [[TimesFM]] / [[TimesFM_2.0]] zero-shot vs TFS Transformers on household STLF; [[2024_Das_TiDE_Long_Term_Forecasting]] — same first author, TiDE dense encoder alternative; [[2019_Toubeau_Deep_Probabilistic_Scheduling_Power_Markets]] — probabilistic load forecasting context

> [!IMPORTANT]
> **For Thesis Use**: This is the *origin paper* for [[TimesFM]] — the decoder-only TSFM now benchmarked in [[2025_Meyer_Benchmark_Foundation_Models]] and referenced in [[Hong_SSM_Transformer_LSTM_Grid_Benchmark]]. Its univariate, covariate-free design explains why Meyer et al. find TSFMs only competitive with <4 weeks history and why EV-specific extensions (arrival/departure, SoC, tariff, weather+traffic fusion via cross-attention) remain an open gap — see [[research_gaps]] T-2/T-3.

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2024_Das_TimesFM_Decoder_Only_Foundation_Model_refs]]
