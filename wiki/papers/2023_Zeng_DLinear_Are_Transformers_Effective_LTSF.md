---
type: paper
title: "Are Transformers Effective for Time Series Forecasting?"
authors: [Ailing Zeng, Muxi Chen, Lei Zhang, Qiang Xu]
year: 2023
journal_conference: "AAAI 2023"
doi_url: "https://arxiv.org/abs/2205.13504"
models_used: ["[[DLinear]]", "[[NLinear]]", "[[Informer]]", "[[Autoformer]]", "[[FEDformer]]", "[[Pyraformer]]", "[[LogTrans]]"]
datasets_used: ["[[ETT]]", "[[Traffic]]", "[[Electricity_ECL]]", "[[Exchange]]", "[[Weather]]", "[[ILI]]"]
features_used: ["[[Trend_Seasonal_Decomposition]]", "[[Moving_Average_Trend]]", "[[Lookback_Window]]", "[[Distribution_Shift_Normalization]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Are Transformers Effective for Time Series Forecasting?

## 🎯 Main Objective & Contribution
- First work to systematically **challenge Transformer-based LTSF solutions**: self-attention is permutation-invariant and "anti-order", causing temporal information loss that positional/timestamp embeddings cannot fully repair — fatal for time series where order is the crucial signal.
- Introduces **[[DLinear]]**: embarrassingly simple one-layer (at most two) direct-multi-step (DMS) linear models — Vanilla Linear, [[NLinear]], [[DLinear]] — that beat FEDformer/Autoformer/Informer/Pyraformer/LogTrans on all nine benchmarks, often by **20%–50%**.
- Diagnostic studies show existing LTSF-Transformers cannot exploit longer look-back windows, barely preserve temporal order under input shuffling, and offer no practical efficiency advantage.

## 🧠 Methodology & Model Architecture
- Problem setup: C variates, look-back $L$, forecast horizon $T$; contrasts iterated multi-step (IMS, error accumulation) vs **direct multi-step (DMS)** strategies; argues prior Transformers' gains largely stem from DMS.
- **Core LTSF-Linear formulation** — one temporal linear layer shared across variates, no cross-variate/spatial modeling:
$$\hat{X}_i = W X_i, \qquad W \in \mathbb{R}^{T \times L}$$
- **[[DLinear]] (Decomposition Linear)** — Autoformer-style moving-average decomposition into trend + seasonal (remainder), separate one-layer linear heads per component summed at output; moving-average kernel size 25:
$$\hat{X} = \text{Linear}_{trend}(X_{trend}) + \text{Linear}_{seasonal}(X_{seasonal})$$
- **[[NLinear]] (Normalized Linear)** — subtracts last value of sequence before the linear layer, adds it back after prediction; a simple shift combating train/test distribution shift (prominent in ETTh1/h2, ILI):
$$\hat{X} = W\left(X - x_L\right) + x_L$$
- Properties: $O(1)$ maximum signal traversing path length (best for dependency capture), ≤ 2TL parameters (vanilla/NLinear) or 2TL total (DLinear = 2 × TL), interpretable weights revealing learned periodicity (e.g., daily + weekly cycles in Traffic).
- Diagnostics designed: look-back scaling ($L \in \{24,\dots,720\}$), close-vs-far input windows, Informer→Linear gradual simplification, input shuffling (Shuf./Half-Ex.), embedding ablations, training-data-size test, practical efficiency benchmarking.

## 📊 Dataset & Input Features
Nine multivariate benchmarks (variates | timesteps | granularity): ETTh1 & ETTh2 7 | 17,420 | 1 h; ETTm1 & ETTm2 7 | 69,680 | 5 min (oil temperature + load of electricity transformers, Jul 2016–Jul 2018); Traffic 862 | 17,544 | 1 h (SF freeway occupancy 2015–2016); Electricity 321 | 26,304 | 1 h (client consumption 2012–2014); Exchange-Rate 8 | 7,588 | 1 day (1990–2016); Weather 21 | 52,696 | 10 min (Germany 2020); ILI 7 | 966 | 1 week (CDC 2002–2021). Horizons $T \in \{96,192,336,720\}$ (ILI: {24,36,48,60}); default L=96 for Transformers, L=336 for LTSF-Linear.
Data URLs (footnotes):
- Code: https://github.com/cure-lab/LTSF-Linear
- ETT: https://github.com/zhouhaoyi/ETDataset
- Traffic (PeMS): http://pems.dot.ca.gov
- Electricity (UCI): https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
- Exchange-Rate: https://github.com/laiguokun/multivariate-time-series-data
- Weather: https://www.bgc-jena.mpg.de/wetter/
- ILI (CDC FluView): https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html
- Paper: https://arxiv.org/abs/2205.13504

## 📈 Performance & Results
- Multivariate results (Table 2): LTSF-Linear surpasses SOTA FEDformer by **20%–50%** in most settings. Examples (MSE): Electricity T=96 DLinear 0.140 vs FEDformer 0.193, Informer 0.274; T=720 DLinear 0.203 vs FEDformer 0.246. Exchange T=720: DLinear 0.643 vs FEDformer 1.447; naive Repeat beats all Transformers on Exchange by ~45% (Transformers mispredict aperiodic trends). ILI T=24: NLinear 1.683 vs FEDformer 2.215. Univariate ETT results (Table 9) confirm the conclusion (e.g., ETTh1 T=96 NLinear MSE 0.056 vs FEDformer-f 0.079).
- **Look-back window** (Fig. 4/Fig. 6): all LTSF-Linear improve markedly with larger L; Transformers stay flat or worsen → they overfit temporal noise instead of extracting temporal relations.
- **Close vs Far inputs** (Table 3): Transformer accuracy barely drops when the look-back window is moved far from the forecast target → they only capture adjacent-sequence information; long-term forecasting depends mainly on trend/periodicity, capturable with few parameters.
- **Attention ablation** (Table 4): gradually simplifying Informer (attention→linear→embedding+linear→pure linear) *improves* MSE monotonically (Exchange T=96: 0.847 → 1.003 → 0.173 → 0.084) — self-attention is unnecessary on these benchmarks.
- **Order preservation** (Table 5): shuffling inputs barely affects Transformers (avg drop −0.12% to +0.09% on Exchange; Informer +1.98% on ETTh1) but severely hurts LTSF-Linear (27–81% drops) → Transformers preserve little temporal order.
- **Embeddings** (Table 6): removing positional embeddings badly damages Informer (Traffic T=720: 0.864 → 1.472); timestamp embeddings matter for Autoformer; FEDformer's frequency module provides inductive bias making it robust to removals.
- **Efficiency** (Table 8, Electricity L=96/T=720): DLinear 0.04G MACs, 139.7K params, 0.4 ms, 687 MiB vs Informer 3.93G / 14.39M / 49.3 ms / 3869 MiB and vanilla Transformer 6091 MiB — memory-efficiency claims of efficient-Transformer variants are practically moot.
- Training data size (Table 7): shortening Traffic training data to exactly one year slightly improves Transformers → small benchmarks are not the limiting factor.

## 💡 Limitations & Identified Research Gaps
- One-layer linear models have limited capacity: they cannot capture temporal dynamics caused by change points; authors position LTSF-Linear as a baseline, not an end model.
- No cross-variate correlation modeling (weights shared across variates).
- Findings are specific to existing LTSF benchmarks; authors call for revisiting Transformer validity in other tasks (anomaly detection) and for new model designs, data processing, and benchmarks.
- Later answered by [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words|PatchTST]], which shows patched channel-independent Transformers do beat DLinear when long look-backs are exploited.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{zeng2023transformers,
  title     = {Are Transformers Effective for Time Series Forecasting?},
  author    = {Zeng, Ailing and Chen, Muxi and Zhang, Lei and Xu, Qiang},
  booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
  year      = {2023}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — permutation-invariant self-attention under critique
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — ProbSparse baseline; ETT dataset source
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — decomposition scheme reused in DLinear; baseline
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]] — LogTrans baseline
- [[2023_Wu_TimesNet_Temporal_2D_Variation_Modeling]] — follow-up showing linear models fail on classification/imputation but TimesNet still beats them at forecasting
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — rebuttal demonstrating effective Transformer design
