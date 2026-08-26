---
type: paper
title: "TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis"
authors: [Haixu Wu, Tengge Hu, Yong Liu, Hang Zhou, Jianmin Wang, Mingsheng Long]
year: 2023
journal_conference: "ICLR 2023"
doi_url: "https://arxiv.org/abs/2210.02186"
models_used: ["[[TimesNet]]", "[[TimesNet]]", "[[Inception_2D_CNN]]", "[[FFT_Periodicity_Detection]]"]
datasets_used: ["[[ETT]]", "[[ETT]]", "[[ETT]]", "[[ETT]]", "[[Electricity_ECL]]", "[[Traffic]]", "[[Weather]]", "[[Exchange]]", "[[ILI]]", "[[M4]]", "[[UEA_Archive]]", "[[SMD]]", "[[MSL]]", "[[SMAP]]", "[[SWaT]]", "[[PSM]]"]
features_used: ["[[Multi_Periodicity]]", "[[Intraperiod_Variation]]", "[[Interperiod_Variation]]", "[[Temporal_2D_Variations]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MSE]]", "[[MAE]]", "[[SMAPE]]", "[[MASE]]", "[[OWA]]", "[[F1_Score]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis

## 🎯 Main Objective & Contribution
- Proposes [[TimesNet]], a **task-general foundation model** (backbone) for five mainstream time-series tasks — short- and long-term forecasting, imputation, classification, anomaly detection — achieving consistent SOTA across all of them.
- Core idea: real-world series exhibit **multi-periodicity** (e.g., daily + weekly cycles in electricity consumption). Each period induces two coupled variation types: **intraperiod-variation** (within a period, short-term patterns) and **interperiod-variation** (across consecutive periods, long-term trends).
- Key innovation: transform the 1D series into a set of **2D tensors** based on discovered periods so both variation types are simultaneously representable (columns = intraperiod, rows = interperiod) and processable by mature 2D vision backbones ([[Inception_2D_CNN]]), bridging 1D time-series analysis with computer vision.

## 🧠 Methodology & Model Architecture
- Modular architecture: stacked [[TimesNet]]s in residual fashion. Input embedding $X^0_{1D} = \text{Embed}(X_{1D}) \in \mathbb{R}^{T \times d_{model}}$; layer update:
$$X^l_{1D} = \text{TimesBlock}\left(X^{l-1}_{1D}\right) + X^{l-1}_{1D}$$
- **Period discovery via FFT (Eq. 1–2)** — amplitude averaged over variates, top-$k$ frequencies selected within $\{1,\dots,\lfloor T/2\rfloor\}$ (conjugacy), periods as $\lceil T/f_i \rceil$:
$$A = \text{Avg}\left(\text{Amp}\left(\text{FFT}(X_{1D})\right)\right), \quad \{f_1,\dots,f_k\} = \arg\text{Top}_k\left(A\right), \quad p_i = \left\lceil \frac{T}{f_i} \right\rceil$$
$$A, \{f_1,\dots,f_k\}, \{p_1,\dots,p_k\} = \text{Period}(X_{1D})$$
- **1D→2D reshaping (Eq. 3)** — zero-padding to length compatible with $(p_i, f_i)$; columns capture intraperiod-, rows interperiod-variation:
$$X^i_{2D} = \text{Reshape}_{p_i,f_i}\left(\text{Padding}(X_{1D})\right), \quad i \in \{1,\dots,k\}$$
- **TimesBlock inner computation (Eq. 5)** — period estimation on deep features, shared parameter-efficient Inception block (multi-scale 2D kernels), reshape back and truncate padding:
$$A^{l-1}, \{f_1,\dots,f_k\}, \{p_1,\dots,p_k\} = \text{Period}\left(X^{l-1}_{1D}\right)$$
$$X^{l,i}_{2D} = \text{Reshape}_{p_i,f_i}\left(\text{Padding}\left(X^{l-1}_{1D}\right)\right), \quad \tilde{X}^{l,i}_{2D} = \text{Inception}\left(X^{l,i}_{2D}\right)$$
$$\tilde{X}^{l,i}_{1D} = \text{Trunc}\left(\text{Reshape}_{1,(p_i\times f_i)}\left(\tilde{X}^{l,i}_{2D}\right)\right)$$
- **Adaptive amplitude-weighted aggregation (Eq. 6)** — Softmax-normalized FFT amplitudes weight the k period-specific representations (inspired by Auto-Correlation):
$$\tilde{A}^{l-1}_{f_1},\dots,\tilde{A}^{l-1}_{f_k} = \text{Softmax}\left(A^{l-1}_{f_1},\dots,A^{l-1}_{f_k}\right), \qquad X^l_{1D} = \sum_{i=1}^{k} \tilde{A}^{l-1}_{f_i} \times \tilde{X}^{l,i}_{1D}$$
- Generality: Inception is replaceable by ResNet/ResNeXt/ConvNeXt/Swin Transformer; shared weights across the k tensors keep model size invariant to $k$. Series stationarization from Non-stationary Transformer applied to handle distribution shift.
- Config (Table 7): ADAM ($\beta_1=0.9,\beta_2=0.999$); $d_{model}=\min\{\max\{2^{\lceil \log C\rceil}, d_{min}\}, d_{max}\}$; k=5 / 2 layers / LR 10⁻⁴ for long-term forecasting; PyTorch, single NVIDIA TITAN RTX 24GB.

## 📊 Dataset & Input Features
Long-term forecasting benchmarks (dim | train/val/test | frequency): ETTm1/m2 7 | 34,465/11,521/11,521 (15-min electricity transformer); ETTh1/h2 7 | 8,545/2,881/2,881 (hourly); Electricity 321 | 18,317/2,633/5,261 (hourly UCI); Traffic 862 | 12,185/1,757/3,509 (hourly PeMS); Weather 21 | 36,792/5,271/10,540 (10-min Wetterstation); Exchange 8 | 5,120/665/1,422 (daily); ILI 7 | 617/74/170 (weekly CDC). Short-term: M4 (~100,000 univariate marketing series; Yearly 23,000, Quarterly 24,000, Monthly 48,000, Weekly 359, Daily 4,227, Hourly 414). Imputation: ETT/Electricity/Weather at mask ratios {12.5%, 25%, 37.5%, 50%}. Classification: 10 UEA subsets (incl. PEMS-SF transportation, 963-dim daily). Anomaly detection: SMD (38-dim server machine), MSL/SMAP (spacecraft), SWaT (water treatment), PSM (server machine), window length 100.
Data URLs (references):
- Code repository: https://github.com/thuml/TimesNet
- M4 dataset: https://github.com/M4Competition/M4-methods/tree/master/Dataset
- Electricity (UCI): https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
- Traffic (PeMS): http://pems.dot.ca.gov/
- Weather (Wetterstation, Max Planck): https://www.bgc-jena.mpg.de/wetter/
- ILI (CDC FluView): https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html
- Paper: https://arxiv.org/abs/2210.02186

## 📈 Performance & Results
- **Long-term forecasting** (Table 2/13, look-back 96; ILI 36; avg over T∈{96,192,336,720}): SOTA in >80% of cases (40 first-place counts vs 14 DLinear, 6 FEDformer, 4 ETSformer). Examples (avg MSE/MAE): ETTm1 0.400/0.406 (vs DLinear 0.403/0.407, FEDformer 0.448/0.452); ETTm2 0.291/0.333; Electricity 0.192/0.295 (vs Stationary 0.193/0.296, Informer 0.311/0.397); Traffic 0.620/0.336; Weather 0.259/0.287; ILI 2.139/0.931 (vs Stationary 2.077/0.914).
- **Short-term M4** (Table 3/14, horizon 6–48): weighted average SMAPE **11.829**, MASE **1.585**, OWA **0.851** — beats N-HiTS (11.927/1.613/0.861) and non-ensembled N-BEATS (11.851/1.599/0.855).
- **Imputation**: best on all datasets, e.g., ETTm1 avg MSE 0.027 vs FEDformer 0.062, DLinear 0.093; Electricity avg 0.092 vs Stationary 0.100.
- **Classification** (10 UEA subsets): average accuracy **73.6%** > Rocket 72.5%, Flowformer 73.0%; DLinear collapses to 67.5% (fixed temporal parameters cannot learn hierarchical representations).
- **Anomaly detection** (reconstruction-error criterion): avg F1 **85.49%** (Inception) / **86.34%** (ResNeXt) vs Anomaly Transformer 80.50%, Autoformer 84.26%; vanilla Transformer only 76.88%.
- **Efficiency** (Table 11, imputation ETTh1): smallest params (0.067 MB constant across lengths 384–3072), best GPU memory/time among top-ranked models; baselines such as FEDformer (2.901 MB, 0.807 s/iter) or Non-stationary Transformer OOM at length 1536+.
- Ablations: stronger vision backbones further improve results (ConvNeXt avg F1 86.89%); adding Autoformer-style decomposition does not help (85.49→85.29) since periodicity already captured; transforming raw data instead of deep features degrades performance (85.49→84.85); amplitude-weighted aggregation beats direct-sum (84.57) and unnormalized-amplitude weighting (85.25); unified training on mixed hourly/15-min ETT data improves all four subsets only for TimesNet — evidence of pre-training backbone potential.

## 💡 Limitations & Identified Research Gaps
- Point forecasts only; no probabilistic/uncertainty modeling for forecasting.
- Performance sensitive to top-k frequency count in low-level tasks (forecasting/anomaly detection); robust for high-level tasks.
- Authors' stated future work: large-scale pre-training methods using TimesNet as general-purpose time-series backbone.
- No explicit cross-variate dependency mechanism (each variate enters via channel dimension C of the 2D tensor; interactions learned only through convolutions).

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{wu2023timesnet,
  title     = {TimesNet: Temporal 2D-Variation Modeling for General Time Series Analysis},
  author    = {Wu, Haixu and Hu, Tengge and Liu, Yong and Zhou, Hang and Wang, Jianmin and Long, Mingsheng},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2023}
}
```

## 🔗 Key References & Citation Graph
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — Auto-Correlation inspiration for amplitude-weighted aggregation; benchmark/dataset provider
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — baseline; ETT dataset source
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — MLP baseline that fails classification/imputation but strong at fixed-dependency autoregression
- [[2020_Oreshkin_NBEATS_Interpretable_Time_Series_Forecasting]] — short-term M4 baseline & metric protocol (SMAPE/MASE/OWA)
- [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]] — short-term forecasting SOTA baseline
