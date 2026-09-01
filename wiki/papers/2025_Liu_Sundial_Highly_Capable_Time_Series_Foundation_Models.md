---
type: paper
title: "Sundial: A Family of Highly Capable Time Series Foundation Models"
authors: [Yong Liu, Guo Qin, Zhiyuan Shi, Zhi Chen, Caiyin Yang, Xiangdong Huang, Jianmin Wang, Mingsheng Long]
year: 2025
journal_conference: "Proceedings of the 42nd International Conference on Machine Learning (ICML 2025), PMLR 267"
doi_url: "https://arxiv.org/abs/2502.00816"
models_used: ["[[Sundial]]", "[[Transformer]]", "[[TimeFlow]]", "[[TimesFM]]", "[[Timer]]", "[[Timer-XL]]", "[[Time-MoE]]", "[[Moirai]]", "[[Chronos]]", "[[LLMTime]]", "[[PatchTST]]", "[[N-BEATS]]", "[[DeepAR]]", "[[TiDE]]"]
datasets_used: ["[[TimeBench]]", "[[GIFT-Eval]]", "[[Chronos_Corpus]]", "[[Electricity]]", "[[Traffic]]", "[[Weather]]", "[[ETTh1]]", "[[ETTh2]]", "[[ETTm1]]", "[[ETTm2]]", "[[ECL]]"]
features_used: ["[[Historical_Load]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MSE]]", "[[MAE]]", "[[MASE]]", "[[CRPS]]", "[[WQL]]"]
tags: [paper, foundation-model, generative-forecasting, flow-matching, continuous-tokenization, zero-shot, time-series]
---

# Summary: Sundial: A Family of Highly Capable Time Series Foundation Models

## 🎯 Main Objective & Contribution
- **Research gap**: Existing time series foundation models (TSFMs) fall into two limited regimes: (1) continuous-token models fitting unimodal parametric densities via MSE/quantile loss (TimesFM, Timer, Time-MoE) which risk mode collapse on heterogeneous data and cannot convey confidence, or (2) discrete-token language-modeling models with cross-entropy (Chronos, LLMTime) which suffer quantization error, large vocabularies and point-wise long contexts. What is missing is a **native, flexible generative** TSFM that learns arbitrary continuous-valued distributions without specifying a prior parametric family and without discrete tokenization.
- **Core contribution — [[Sundial]] family**: First family of **native, flexible, scalable generative** TSFMs built on minimal-but-crucial Transformer adaptations and a new **TimeFlow Loss** (flow-matching) that trains autoregressively on continuous patches and samples multiple plausible futures via an ODE push-forward.
- **Three pillars**:
  1. **TimeFlow Loss**: Parameterized flow-matching objective conditioned on per-patch Transformer representations; mitigates mode collapse, enables patch-level generation and fast inference with shared lookback representation.
  2. **Enhanced decoder-only Transformer**: Re-normalization (stationarization), patch embedding with binary padding mask, Pre-LN, causal self-attention with RoPE, FlashAttention + KV Cache, multi-patch prediction (F > P) to reduce AR steps.
  3. **[[TimeBench]]**: Curated trillion-scale pre-training corpus — **1,032B time points (381 GB)** from real-world public sets + 0.05% KernelSynth synthetic + massive ERA5 meteorological data, covering 12 sources, many frequencies and variate counts.
- **Empirical claim**: Sundial (Small 32M / Base 128M / Large 444M) achieves **SOTA zero-shot** on both point (TSLib long-term) and probabilistic (GIFT-Eval, FEV) benchmarks, scales monotonically with size/data, and infers in **milliseconds** with ~35× speedup over Chronos on FEV while matching N-BEATS latency. Validates that generative modeling unlocks capacity (15.38% training-loss reduction Large vs Small).

## 🧠 Methodology & Model Architecture
- **Model Type**: Decoder-only patched Transformer + conditional flow-matching head (FM-Net). Pipeline: Re-Normalization → Patch Embedding (shared MLP on concat of patch + mask) → N-layer Transformer decoder (causal, Pre-LN, RoPE) → per-token condition $h_i$ → small MLP **FM-Net** that predicts the velocity field for flow-matching and generates future patch via K-step ODE integration. Training jointly optimizes Transformer and FM-Net; inference reuses lookback $h_i$ for repeated sampling from different Gaussian noises.

- **Key Equations** (verbatim, §3–4):

  **Eq. 1 — Conditional OT Flow-Matching (Gaussian path)** ($t\sim\mathcal{U}[0,1]$, $x_0\sim\mathcal{N}(0,1)$, $x_t = t x_1 + (1-t)\epsilon$):
  $$\mathcal{L}^{\text{Gauss}}_{\text{CFM}}(\theta) = \mathbb{E}_{t,\epsilon,x_1}\left\lVert u^{\theta}_{t}(x_t) - (x_1 - x_0)\right\rVert^{2} \tag{1}$$

  **Eq. 2 — Push-forward sampling** (Euler step $\Delta t$):
  $$x_{t+\Delta t} - x_{t} = u^{\theta}_{t}(x_t)\Delta t,\quad x_0\sim\mathcal{N}(0,I),\; t\in[0,1] \tag{2}$$

  **Eq. 3 — Generative probabilistic forecasting** ($h_t = f_{\phi}(x_{1:t})$, $g_{\theta}$ = conditional generative network):
  $$p_{\theta}(x_{t+1:t+f}\mid h_t) = g_{\theta}\!\left(f_{\phi}(x_{1:t})\right) \tag{3}$$

  **Eq. 4 — Patch embedding** ($X=\{x_1,\dots,x_T\}$, $x_i = x_{1+(i-1)P:iP}$, mask $m_i\in\mathbb{R}^{P}$, $N=\lceil T/P\rceil$, shared MLP $\mathbb{R}^{2P}\!\to\!\mathbb{R}^{D}$):
  $$h_i = \text{PatchEmbed}\!\left(\text{Concat}(x_i, m_i)\right) \tag{4}$$

  **Eq. 5 — Causal attention with RoPE** ($W_q,W_k,W_v\in\mathbb{R}^{D\times d}$, rotary $R_{\Theta,t}$):
  $$A_{ij}=h_i^{\top}W_q R_{\Theta,i-j}W_k^{\top}h_j,\quad \text{Attention}(H)=\text{Softmax}\!\left(\frac{\text{Mask}(A)}{\sqrt{d}}\right) H W_v \tag{5}$$

  **Eq. 6 — TimeFlow per-position loss** ($y_i\in\mathbb{R}^{F}$ ground truth, $y^{(0)}_i\sim\mathcal{N}(0,I)$, $y^{(t)}_i = t y_i + (1-t)y^{(0)}_i$):
  $$\mathcal{L}(\theta, h_i)=\mathbb{E}_{t,\epsilon,y_i}\left\lVert u^{\theta}_{t}\!\left(y^{(t)}_i\mid h_i\right) - (y_i - y^{(0)}_i)\right\rVert^{2} \tag{6}$$

  **Eq. 7 — FM-Net parameterization** (AdaLN conditioning on $h_i$):
  $$u^{\theta}_{t}\!\left(y^{(t)}_i\mid h_i\right)=\text{FM-Net}\!\left(y^{(t)}_i, t, h_i\right) \tag{7}$$

  **Eq. 8 — TimeFlow Loss (autoregressive, $N$ patches)**:
  $$\mathcal{L}_{\text{TimeFlow}}=\sum_{i=1}^{N}\left\lVert \text{FM-Net}\!\left(y^{(t)}_i, t, h_i\right) - (y_i - y^{(0)}_i)\right\rVert^{2} \tag{8}$$

  **Eq. 9 — Inference push-forward** ($K$-step uniform trajectory, $\Delta t=1/K$):
  $$y^{(t+\Delta t)}_i = y^{(t)}_i + u^{\theta}_{t}\!\left(y^{(t)}_i\mid h_i\right)\Delta t \tag{9}$$

- **Design principles**:
  - *Continuous vs discrete tokenization*: Patch tokens keep raw continuous values (no quantization) and cut token count by factor $P$; point-wise quantization (Chronos) lengthens context and is sensitive to bucketing.
  - *Re-normalization*: Two-stage instance normalization (stationarization, Liu et al. 2022) per sample mitigates distribution shift and outliers → better zero-shot generalization.
  - *RoPE + Pre-LN*: RoPE gives relative position for arbitrary-length patches; Pre-LN stabilizes large-scale pre-training (Post-LN degrades with more iterations, Fig. 9b).
  - *Multi-patch prediction* $F>P$ (F=720 for long-term, F=16 for FEV short-term): Fewer AR steps and better accommodates varied frequencies; small $P=16$ chosen for flexibility, large $F$ for efficiency.
  - *Efficient inference*: FlashAttention → -14.8% memory; KV Cache → -43.6% inference time; shared $h_i$ reused across 20–100 samples (median/quantiles estimated from samples).
  - *S3 univariate format* (Timer): Handles multivariate by per-variable normalization and variable-independent sampling; max context 2880.

- **Training**: PyTorch on 32× A100, AdamW, S3 format, global shuffle via parquet, per-variable normalization, domain-balanced sampling. Configs: Small (P=16, T=2880, F={16,720}, L=6, D=512/Dff=2048, H=8, FM (512,3), 32M) / Base (12 layers, 768/3072, 12 heads, FM 768/3, 128M) / Large (24 layers, 1024/4096, 16 heads, FM 1024/6, 444M). Sampling $K=50$ steps.

## 📊 Dataset & Input Features
- **Pretraining corpus — [[TimeBench]]** (Fig. 3, Table 4, §4.2 + Appendix A; total **1,032B points**):

| Source | # Points | Share | Notes |
|---|---|---|---|
| Chronos (Ansari et al. 2024) | 94B | 9.11% | Real-world public collection |
| ECG (Goldberger et al. 2000) | 48B | 4.65% | Healthcare |
| Finance (ours) | 10.5B | 1.02% | Financial series |
| IoT (ours) | 5.8B | 0.56% | IoT sensors |
| LOTSA (Woo et al. 2024) | 230B | 22.29% | Large open time-series archive |
| Synthetic (KernelSynth) | 0.5B | 0.05% | Diverse patterns |
| ERA5 3h (Hersbach et al. 2020) | 129B | 12.50% | Meteorological reanalysis |
| ERA5 12h | 32B | 3.10% | — |
| ERA5 Daily | 406B | 39.35% | Dominant source |
| ERA5 Weekly | 58B | 5.62% | — |
| ERA5 Monthly | 13.5B | 1.31% | — |
| ERA5 Quarterly | 4.5B | 0.44% | — |

  All evaluation datasets excluded from pretraining to ensure zero-shot. Curation included imputation, abnormality filtering, per-variable normalization, and diagnostics on non-stationarity/forecastability/seasonality.

- **Evaluation benchmarks (all zero-shot unless noted)**:
  - **TSLib long-term** (Wu et al. 2022) — ETTm1, ETTm2, ETTh1, ETTh2, ECL (Electricity), Weather; horizons {96,192,336,720}, context 2880, metrics MSE/MAE. Traffic (PEMS) excluded because it appears in pretraining.
  - **[[GIFT-Eval]]** (Aksu et al. 2024) — 97 configs from 23 datasets (energy, retail, weather, finance), horizons 6–900; metrics MASE/CRPS/Rank with 100 samples.
  - **FEV leaderboard** (Ansari et al. 2024, AutoGluon) — 27 unseen short-term probabilistic datasets; metrics MASE/WQL with 20 samples.

- **Data Availability & Links**:
  - Code: https://github.com/thuml/Sundial
  - Weights (Hugging Face, 3 sizes): https://huggingface.co/thuml/sundial-base-128m (also Small/Large variants)
  - TimeBench composition visualized in Fig. 3; ERA5 via Hersbach et al. 2020 / Muñoz-Sabater et al. 2021

- **Features**: Purely **univariate** — past values $y_{1:L}$ + binary padding mask $m_i$; no exogenous covariates (S3 univariate pre-training handles multivariate via channel independence).

- **Preprocessing**: Context-level re-normalization (stationarization) per sample; patching with $P=16$ and binary mask for non-divisible lengths; variable-wise normalization; truncate model output if required horizon < $F$, rolling forecast if horizon > $F$.

## 📈 Performance & Results
- **TSLib zero-shot long-term (Table 1/9, avg over 4 horizons; lower is better, context 2880, patch 16)** — Sundial consistently #1 vs 12 TSFMs:

| Dataset | Sundial-S (MSE/MAE) | Sundial-B | Sundial-L | Best competitor | TimesFM | Chronos-L |
|---|---|---|---|---|---|---|
| ETTm1 | **0.354/0.388** | 0.336/0.377 | **0.331/0.369** | Time-MoE-U 0.356/0.391 | 0.433/0.418 | 0.555/0.465 |
| ETTm2 | 0.265/0.324 | 0.258/0.320 | **0.254/0.315** | Timer-XL 0.273/0.336 | 0.328/0.346 | 0.295/0.338 |
| ETTh1 | **0.390/0.418** | 0.411/0.434 | 0.395/0.420 | Time-MoE-L 0.394/0.419 | 0.473/0.443 | 0.588/0.466 |
| ETTh2 | 0.340/0.387 | **0.333/0.387** | 0.334/0.387 | Timer-XL 0.347/0.388 | 0.392/0.406 | 0.455/0.427 |
| ECL | **0.169/0.265** | 0.169/0.265 | **0.166/0.262** | Timer-XL 0.174/0.278 | — | 0.204/0.273 |
| Weather | **0.233/0.271** | 0.234/0.270 | 0.238/0.275 | Timer-XL 0.256/0.294 | — | 0.279/0.306 |
| **1st Count** (wins over all horizons×datasets) | 7 / 2 | **8 / 5** | **16 / 16** | 2/1 (Timer-XL) | 0 | 0 |

  Sundial-L achieves **-7.57% MSE / -4.71% MAE** vs previous SOTA Time-MoE with fewer parameters; continuous patch tokenization avoids the long contexts and horizon sensitivity of point-wise Chronos (Chronos-L MSE 0.645 on ETTm1 vs 0.331 Sundial-L). Scaling: Larger → better (Fig. 6 training curves; Large -15.38% converged loss vs Small).

- **[[GIFT-Eval]] probabilistic zero-shot (Table 2, 97 configs, 100 samples, lower better)** — Sundial **#1 MASE / #2 CRPS** among all:

| Model | MASE | CRPS | Rank | Notes |
|---|---|---|---|---|
| **[[Sundial]] (Ours)** | **0.673** | 0.472 | **9.06** | Best MASE, 2nd CRPS |
| [[PatchTST]] (supervised, per-dataset tuned) | 0.762 | 0.496 | 10.05 | Exhaustively tuned supervised upper bound |
| [[N-BEATS]] | 0.842 | 0.689 | 21.38 | — |
| [[TimesFM]] | 0.802 | 0.524 | 11.32 | — |
| [[TabPFN-TS]] | 0.680 | **0.465** | **8.24** | Only model beating Sundial on CRPS |
| [[Chronos]] | 0.748 | 0.480 | 8.27 | — |
| [[Moirai]] | 0.786 | 0.551 | 14.31 | Mixture prior less flexible |

  Sundial calculates median/quantiles from samples **without** quantile-loss pretraining.

- **FEV leaderboard (Fig. 4–5, 27 datasets, 20 samples, AutoGluon)** — Sundial zero-shot beats >70% of statistical + supervised deep models trained in-distribution; ranks **2nd among zero-shot FMs** after Chronos but with **35× inference speedup** (Fig. 5, log-scale): Sundial ~ near N-BEATS latency via patch-wise + multi-patch, vs Chronos point-wise AR.

- **Ablations — training objective (Table 3/7, same backbone & TimeBench)**:

| Objective | ETTm1 MSE | ETTh1 MSE | Weather MSE | Avg MSE | GIFT-Eval CRPS |
|---|---|---|---|---|---|
| **TimeFlow** | **0.336** | **0.411** | **0.234** | **0.290** | **0.5050** |
| Diffusion | 0.362 | 0.444 | 0.252 | 0.314 | 0.5340 |
| MSE (deterministic) | 0.360 | 0.404 | 0.231 | 0.296 | 0.6420 |

  Deterministic MSE gives over-smooth, mode-collapsed predictions (Appendix D Fig. 14–15); diffusion is notably worse.

- **Ablations — architecture (Fig. 9, TSLib avg)**:
  - RoPE improves avg MSE/MAE vs no RoPE.
  - Pre-LN + longer training (30k vs 15k iter) improves; Post-LN degrades — Pre-LN crucial for large TSFMs.
  - FlashAttention -14.8% memory, KV Cache -43.6% inference time, no accuracy loss.

- **Test-time calibration (Fig. 7, FEV MASE/WQL)**: More samples (central limit) and more push-forward steps $K$ → better MASE/WQL; 20 samples × $K=50$ ≈ 1 sec on CPU; generation of multiple samples reuses shared $h_i$.

- **Model adaptation (Fig. 8, fine-tune once on all FEV datasets)**: Fine-tuned Sundial-B > zero-shot > train-from-scratch (scratch worse → pre-training transfers).

- **Scaling with data (Table 8, same horizons)** — larger TimeBench → better; even at 94B/230B subsets Sundial beats Chronos/Moirai trained on same scale (e.g., Weather MSE 0.254 Sundial-94B vs 0.292 Chronos-94B).

- **Inference efficiency**: Patch-level + multi-patch + KV Cache; 20 preds × $K=50$ ≈ 1s CPU; FEV latency near N-BEATS despite generative sampling.

## 💡 Limitations & Identified Research Gaps
- **Univariate-only pre-training** (S3 format, per-variable normalization): No explicit cross-variate / covariate modeling; multivariate dependencies and exogenous covariates (arrival/departure, SoC, tariff, weather) left as future multivariate pretraining (increasingly studied for domain-specific TSFMs).
- **Very high-frequency data not guaranteed**: TimeBench dominated by middle/low frequencies (ERA5 daily etc.); performance on tick/10s-level series untested — multi-scale generalization needs work (§E).
- **Naïve sampling**: Starts from $\mathcal{N}(0,I)$ with uniform $K=50$ Euler steps; frequency normalization / advanced samplers and post-processing unexplored.
- **Long-context high-frequency gap**: Max context 2880 patches but still may need stronger long-context capability for high-frequency series (Fig. 10: optimum lookback depends on task periodicity/horizon).
- **Potential hallucinations** despite mode-collapse mitigation; autoregressive rolling for horizons > $F$ may yield over-smooth/unreliable tails.
- **Probabilistic calibration limited to sample statistics**: Direct quantile optimization not used; future work could co-train TimeFlow with quantile objectives.
- **Domain gap for EV load**: All benchmarks generic (energy/weather/synthetic), no EV charging datasets (ACN, ElaadNL, Boulder) evaluated — transfer to sparse, spiky EV loads unproven; covariate-free design is an open gap for thesis.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{liu2025sundial,
  title        = {Sundial: A Family of Highly Capable Time Series Foundation Models},
  author       = {Liu, Yong and Qin, Guo and Shi, Zhiyuan and Chen, Zhi and Yang, Caiyin and Huang, Xiangdong and Wang, Jianmin and Long, Mingsheng},
  booktitle    = {Proceedings of the 42nd International Conference on Machine Learning},
  series       = {PMLR 267},
  year         = {2025},
  url          = {https://arxiv.org/abs/2502.00816},
  eprint       = {2502.00816},
  archivePrefix= {arXiv},
  primaryClass = {cs.LG}
}
```

## 🔗 Key References & Citation Graph
- Cited Foundations in Vault: [[2017_Attention_Is_All_You_Need]] [VSP+17] — Transformer base; [[2022_Kim_RevIN_Reversible_Instance_Normalization]]-adjacent stationarization [KKT+21]; [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] [NNSK22] — patching precedent; Su et al. 2024 (RoFormer/RoPE) [Su et al. 2024] — RoPE; Dao et al. 2022 (FlashAttention) [Dao et al. 2022] — FlashAttention; Pope et al. 2023 (Efficient Transformer Inference, KV Cache) [Pope et al. 2023] — KV Cache; Xiong et al. 2020 (LayerNorm in Transformers) [Xiong et al. 2020] — Pre-LN vs Post-LN; Lipman et al. 2022 (Flow Matching) [Lipman et al. 2022] — flow-matching theory (Eq. 1–2); Lipman et al. 2024 (Flow Matching Guide); Tong et al. 2023 (Improving Flow-Based Generative Models); Peebles & Xie 2023 (Scalable Diffusion Transformers, AdaLN) [Peebles & Xie 2023] — AdaLN; Esser et al. 2024 (Scaling Rectified Flow Transformers); Liang et al. 2024 (Foundation Models for Time Series Survey)
- Time Series Foundation Models Compared: [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — decoder-only patched predecessor beaten on all TSLib sets; Woo et al. 2024 (Moirai, Unified Training) — mixture-density prior; Ansari et al. 2024 (Chronos, Learning the Language of Time Series) — discrete tokenization; Rasul et al. 2024 (Lag-Llama); Shi et al. 2024 (Time-MoE, Billion-Scale MoE) — SOTA point forecaster beaten by Sundial (-7.57% MSE); Liu et al. 2024 (Timer, Generative Pretrained Transformers) / Liu et al. 2024 (Timer-XL, Long-Context Transformers) — Timer family; [[2025_Ansari_Chronos_2_Univariate_to_Universal]]
- Related Vault Papers: [[2025_Meyer_Benchmark_Foundation_Models]] — benchmarks [[Sundial]] zero-shot on household STLF (Sundial competitive on Lower Saxony/REFIT/S.Germany but behind Chronos-Bolt/TimesFM 2.0); [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — TimesFM vs Sundial on Monash/Darts/ETT; [[2026_Khwaja_Toto_2_Scaling_Era]] — Toto 2.0 scaling TSFM that also uses GIFT-Eval/TIME/BOOM
- Generative / Diffusion Line: [[2021_Rasul_TimeGrad_Diffusion_Forecasting]]; [[2021_Tashiro_CSDI_Conditional_Diffusion_Forecasting]]; Shen & Kwok 2023 (Non-Autoregressive Conditional Diffusion); Kollovieh et al. 2024 (Flow Matching with GP Priors)

> [!IMPORTANT]
> **For Thesis Use**: First TSFM to marry **continuous patch tokenization + generative flow-matching** without discrete quantization or parametric-mixture priors — directly addresses thesis gap on generative probabilistic forecasting for heterogeneous EV-like loads. **TimeFlow (Eq. 6–9) + Pre-LN + RoPE + FlashAttention/KV Cache + multi-patch $F>P$** is the recipe that beats Time-MoE/Chronos/Moirai on both MSE/MAE and CRPS/MASE. Open thesis extensions: multivariate/covariate-aware fine-tuning (arrival/departure, SoC, tariff, weather+traffic via cross-attention), high-frequency multi-scale adaptation, and EV-specific FEV/GIFT-Eval-style evaluation — see [[research_gaps]].

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2025_Liu_Sundial_Highly_Capable_Time_Series_Foundation_Models_refs]]
