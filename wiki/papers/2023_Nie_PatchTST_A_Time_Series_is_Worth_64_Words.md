---
type: paper
title: "A Time Series is Worth 64 Words: Long-term Forecasting with Transformers"
authors: [Yuqi Nie, Nam H. Nguyen, Phanwadee Sinthong, Jayant Kalagnanam]
year: 2023
journal_conference: "ICLR 2023"
doi_url: "https://arxiv.org/abs/2211.14730"
models_used: ["[[PatchTST]]", "[[Transformer_Encoder]]", "[[RevIN]]", "[[Masked_Autoencoder]]"]
datasets_used: ["[[Weather]]", "[[Traffic_PEMS]]", "[[Electricity_ECL]]", "[[ILI]]", "[[ETTh1]]", "[[ETTh2]]", "[[ETTm1]]", "[[ETTm2]]"]
features_used: ["[[Multivariate_Time_Series]]", "[[Patched_Embeddings]]", "[[Channel_Independence]]", "[[Positional_Encoding]]"]
forecasting_horizon: "[[Long_Term]]"
metrics: ["[[MSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Time Series is Worth 64 Words: Long-term Forecasting with Transformers

## 🎯 Main Objective & Contribution
- Answers the [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF|DLinear challenge]] to Transformers by showing a vanilla-attention Transformer **can** be effective if designed properly. Proposes [[PatchTST]] (channel-independent Patch Time Series Transformer) built on two designs:
  1. **Patching**: subseries-level patches as input tokens → retains local semantic information in embeddings, quadratically reduces attention compute/memory ($N \approx L/S$ tokens), and enables attending over much longer look-back windows.
  2. **Channel-independence (CI)**: each univariate series processed separately through shared embedding + Transformer weights.
- Additionally demonstrates SOTA **masked self-supervised representation learning** and cross-dataset transfer learning (pre-train on Electricity → fine-tune elsewhere), outperforming supervised training on large datasets.

## 🧠 Methodology & Model Architecture
- Problem: given multivariate samples with look-back $L$, each channel $x^{(i)}_{1:L} \in \mathbb{R}^{1\times L}$, $i=1,\dots,M$, forecast $T$ future values; each channel fed independently into the Transformer backbone (channel-independence).
- **Patching equation** — number of patches with patch length $P$, stride $S$ (last value padded $S$ times):
$$N = \left\lfloor \frac{L-P}{S} \right\rfloor + 2$$
- **Patch embedding + learnable positional encoding** ($W_p \in \mathbb{R}^{D\times P}$, $W_{pos} \in \mathbb{R}^{D\times N}$):
$$x_d^{(i)} = W_p x_p^{(i)} + W_{pos}$$
- **Multi-head scaled dot-product attention** per head $h = 1,\dots,H$:
$$\left(O_h^{(i)}\right)^T = \text{Attention}\left(Q_h^{(i)}, K_h^{(i)}, V_h^{(i)}\right) = \text{Softmax}\left(\frac{Q_h^{(i)} \left(K_h^{(i)}\right)^T}{\sqrt{d_k}}\right)V_h^{(i)}$$
with $Q_h^{(i)} = (x_d^{(i)})^T W^Q_h$, $K_h^{(i)} = (x_d^{(i)})^T W^K_h$, $V_h^{(i)} = (x_d^{(i)})^T W^V_h$. Encoder blocks use BatchNorm (shown superior to LayerNorm for time-series Transformers) + FFN with residual connections; flatten + linear head outputs $\hat{x}^{(i)} \in \mathbb{R}^{1\times T}$.
- **MSE training loss** averaged over channels:
$$\mathcal{L} = \mathbb{E}_x \frac{1}{M}\sum_{i=1}^{M} \left\| \hat{x}_{L+1:L+T}^{(i)} - x_{L+1:L+T}^{(i)} \right\|_2^2$$
- **Instance normalization** ([[RevIN]]-style): normalize each instance to zero mean/unit std before patching; statistics added back to output.
- Variants: **PatchTST/42** ($L=336$, 42 patches) and **PatchTST/64** ($L=512$, 64 patches), both $P=16, S=8$. Default: 3 encoder layers, $H=16$, $D=128$, FFN hidden $F=256$ with GELU, dropout 0.2; reduced config ($H=4, D=16, F=128$) for small datasets (ILI, ETTh1/h2).
- **Self-supervised masked pretraining**: non-overlapping patches ($L=512$, $P=12$ → 42 patches), 40% of patches masked with zeros, model reconstructs via MSE loss; downstream linear probing then end-to-end fine-tuning.

## 📊 Dataset & Input Features
8 popular benchmarks (from Autoformer repo), statistics (#features / #timesteps): Weather 21/52,696; Traffic 862/17,544; Electricity 321/26,304; ILI 7/966; ETTh1 & ETTh2 7/17,420 (hourly); ETTm1 & ETTm2 7/69,680 (15-min).
Data URLs (appendix footnotes):
- Weather (Max Planck Biogeochemistry, Germany): https://www.bgc-jena.mpg.de/wetter/
- Traffic (SF freeway occupancy, Caltrans PeMS): https://pems.dot.ca.gov/
- Electricity (UCI, 321 clients hourly kWh): https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
- ILI (CDC FluView): https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html
- ETT (electricity transformer temperature): https://github.com/zhouhaoyi/ETDataset
- Exchange-rate dataset deliberately excluded: https://github.com/laiguokun/multivariate-time-series-data (near-random-walk; last-value repetition is competitive)
Paper: https://arxiv.org/abs/2211.14730 ; code stated to be made publicly available.
Prediction lengths $T \in \{96,192,336,720\}$ (ILI: $\{24,36,48,60\}$); baselines re-run with $L \in \{24,48,96,192,336,720\}$ for fairness.

## 📈 Performance & Results
- Case study (Traffic, $T=96$): PatchTST $L=336$+patching MSE **0.367**, self-supervised **0.349**, vs DLinear 0.410 and FEDformer 0.597. Patching speedups at $L=336$: Traffic ×22 (464 s vs 10,040 s), Electricity ×19, Weather ×4.
- Supervised benchmark (Table 3): vs best Transformer baselines, PatchTST/64 achieves overall **21.0% MSE / 16.7% MAE reduction**; PatchTST/42 **20.2% / 16.4%**. Beats DLinear especially on large datasets and ILI. Examples: Electricity T=96 MSE 0.129 (PatchTST/64) vs DLinear 0.140, FEDformer 0.186; Traffic T=720 0.432 vs DLinear 0.466.
- Self-supervised (Table 4): fine-tuned pre-trained PatchTST further improves results — e.g., Electricity T=96 MSE **0.126**, Traffic T=96 **0.352**, beating supervised-from-scratch and all baselines; linear probing alone already beats DLinear.
- Transfer learning (Table 5): pre-train on Electricity → fine-tune on other datasets still outperforms other models on most tasks.
- Representation-learning comparison (Table 6, ETTh1 linear probing): improvements of **34.5%–48.8%** over BTSF, TS2Vec, TNC, TS-TCC (e.g., T=48 MSE 0.339 vs BTSF 0.354).
- Ablations: both patching and CI individually improve accuracy (Table 7/10; original point-wise TST OOMs on Traffic/Electricity on an A40 48GB GPU); longer look-back consistently improves PatchTST but not baselines (Fig. 2/Table 9); performance robust to patch length $P \in \{4..40\}$ and model size; instance normalization helps slightly (e.g., ILI T=24: 1.522 vs 3.489 without). Applying CI to Informer/Autoformer/FEDformer improves them too, yet none beat PatchTST (Table 15).

## 💡 Limitations & Identified Research Gaps
- Channel-independence ignores explicit cross-channel correlations; authors state modeling cross-channel dependencies properly is an important future step (suggest GNN-based extension).
- No probabilistic/uncertainty quantification (point forecasts, MSE only).
- Exchange-rate-type financial series excluded due to weak predictability — generalization claims limited to physical/engineering signals.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{nie2023patchtst,
  title     = {A Time Series is Worth 64 Words: Long-term Forecasting with Transformers},
  author    = {Nie, Yuqi and Nguyen, Nam H. and Sinthong, Phanwadee and Kalagnanam, Jayant},
  booktitle = {International Conference on Learning Representations (ICLR)},
  year      = {2023}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] — vanilla Transformer encoder backbone
- [[2023_Zeng_DLinear_Are_Transformers_Effective_LTSF]] — the linear-model critique PatchTST answers; also supplies baseline numbers
- [[2022_Kim_RevIN_Reversible_Instance_Normalization]] — instance normalization against distribution shift
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — ProbSparse baseline
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] — decomposition/auto-correlation baseline and dataset provider
- [[2019_Li_LogSparse_Enhancing_Locality_Transformer]] — LogTrans convolutional self-attention baseline
