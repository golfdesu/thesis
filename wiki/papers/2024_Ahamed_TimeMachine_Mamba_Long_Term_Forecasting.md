---
type: paper
title: "TimeMachine: A Time Series is Worth 4 Mambas for Long-term Forecasting"
authors: [Md Atik Ahamed, Qiang Cheng]
year: 2024
journal_conference: "arXiv preprint (arXiv:2403.09898v2, cs.LG, 22 Aug 2024), University of Kentucky"
doi_url: "https://doi.org/10.48550/arXiv.2403.09898"
models_used: ["[[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]]", "[[Mamba_SSM]]"]
datasets_used: ["[[Weather_Dataset]]", "[[Traffic]]", "[[Electricity_ECL]]", "[[ETT]]", "[[ETT]]", "[[ETT]]", "[[ETT]]"]
features_used: ["[[Historical_Load]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: TimeMachine: A Time Series is Worth 4 Mambas for Long-term Forecasting

## 🎯 Main Objective & Contribution
- Introduce **TimeMachine**, a model built on the selective-scan state-space model **Mamba** for long-term time-series forecasting (LTSF) that captures long-range dependencies in multivariate time series (MTS) with **linear scalability** and a **small memory footprint**.
- Three stated contributions:
	1. First model to leverage purely SSM modules for context-aware LTSF prediction with linear scalability and small memory footprints superior/comparable to linear models.
	2. An innovative architecture unifying **channel-mixing and channel-independence** handling via an integrated **quadruple-Mamba** design, selecting contents against global and local contexts at multiple scales.
	3. Superior experimental performance in accuracy, scalability, and memory efficiency vs. 11 SOTA baselines, with rigorous ablations.

## 🧠 Methodology & Model Architecture
- **Normalization**: input MTS $x=[x_1,\dots,x_L]$ ($x_t \in \mathbb{R}^M$, look-back $L$) normalized via RevIN or Z-score; RevIN empirically more helpful.
- **Two-stage embedding** with MLPs $E_1:\mathbb{R}^{M\times L}\to\mathbb{R}^{M\times n_1}$, $E_2:\mathbb{R}^{M\times n_1}\to\mathbb{R}^{M\times n_2}$ and dropout:
$$x^{(1)} = E_1(x^{(0)}), \quad x^{(2)} = E_2(DO(x^{(1)}))$$
(Equation 1: Two-stage embedded representation; $n_1,n_2 \in \{512,256,128,64,32\}$, $n_1>n_2$.)
- **Quadruple Mamba architecture**: two outer Mambas on $DO(x^{(1)})$ (high resolution, fine scale) and two inner Mambas on $DO(x^{(2)})$ (low resolution, coarse scale). Channel independence reshapes input $\mathrm{BML} \mapsto (\mathrm{B}\times \mathrm{M})\,1\mathrm{L}$; one Mamba per pair sees token length $n_i$ / dim 1 (global context), the other dim $n_j$ / token length 1 (local context). Channel mixing transposes the tensor so each whole channel sequence is a token — switching is done simply by transposing the input.
- **Continuous-time SSM inside each Mamba block**:
$$dh(t)/dt = A\, h(t) + B\, u(t), \qquad v(t) = C\, h(t)$$
(Equation 2: Continuous-time state-space dynamics; $h(t)$ N-dimensional state, $u(t)$ D-dimensional input.)
- **Discretized SSM** at time samples $\{k\Delta\}$:
$$h_k = \bar{A}\, h_{k-1} + \bar{B}\, u_k, \qquad v_k = C\, h_k$$
(Equation 3: Discrete SSM state evolution and output.)
$$\bar{A} = \exp(\Delta A), \qquad \bar{B} = (\Delta A)^{-1}(\exp(\Delta A) - I)\,\Delta B$$
(Equation 4: Zero-order-hold discretization coefficients.) Mamba makes $B, C, \Delta$ linear time-varying functions of the input ($B,C \leftarrow \text{Linear}_N(u)$, $\Delta \leftarrow \text{softplus}(\text{parameter} + \text{Linear}_D(\text{Linear}_1(u))$)), giving input/context selectivity.
- **Output projection**: MLPs $P_1:\mathbb{R}^{M\times n_2}\to\mathbb{R}^{M\times n_1}$, $P_2:\mathbb{R}^{M\times 2n_1}\to\mathbb{R}^{M\times T}$, with two residual connections; outputs concatenated as $x^{(6)} = x^{(5)} \| (x^{(4)}\,\llcorner\, x^{(1)})$, then $y = P_2(x^{(6)})$.
- Default hyperparameters: D=256, d_conv=2, N=256, expand factor E=1, dropout 0.7 on ETTs, ADAM optimizer, L2 loss, 100 epochs, 4×V100 GPUs.

## 📊 Dataset & Input Features
Seven standard LTSF benchmarks (no external URLs given in paper; code/baselines links below):
| Dataset | Channels (M) | Time Points | Frequency |
|---|---|---|---|
| Weather | 21 | 52,696 | 10 min |
| Traffic | 862 | 17,544 | Hourly |
| Electricity | 321 | 26,304 | Hourly |
| ETTh1 | 7 | 17,420 | Hourly |
| ETTh2 | 7 | 17,420 | Hourly |
| ETTm1 | 7 | 69,680 | 15 min |
| ETTm2 | 7 | 69,680 | 15 min |

- ILI excluded (short horizon). Details referenced from Wu et al. (Autoformer) and Zhou et al. (Informer).
- Input features: raw historical multivariate values per channel (look-back window L); no exogenous features.
- Links found in text: Code — https://github.com/Atik-Ahamed/TimeMachine ; baseline code — https://github.com/yuqinie98/PatchTST , https://github.com/thuml/iTransformer

## 📈 Performance & Results
- Protocol: L=96 fixed for all models, T ∈ {96,192,336,720}; MSE/MAE metrics; baseline numbers taken from iTransformer paper.
- Selected TimeMachine results (MSE/MAE):
	- Electricity: T=96 → 0.142/0.236 (iTransformer 0.148/0.240); T=720 → 0.207/0.298 (iTransformer 0.225/0.317).
	- Traffic: essentially tied with iTransformer (e.g., T=96: 0.397/0.268 both; T=720: 0.467/0.300 both).
	- Weather: T=96 → 0.164/0.208 (second to Crossformer's 0.158/0.230 MSE-wise best 0.164 vs iTransformer 0.174/0.214); ranks second on Weather at small T.
	- ETTh1: T=96 → 0.364/0.387 vs iTransformer 0.386/0.405; T=720 → 0.458/0.453 vs 0.503/0.491.
	- ETTh2: T=96 → 0.275/0.334 vs iTransformer 0.297/0.349; T=720 → 0.411/0.433 vs 0.427/0.445.
	- ETTm1: T=96 → 0.317/0.355 vs PatchTST 0.329/0.367; T=720 → 0.445/0.436.
	- ETTm2: T=96 → 0.175/0.256; T=720 → 0.371/0.385.
- Longer look-backs improve results: e.g., Electricity T=96 MSE drops 0.142 (L=96) → 0.133 (L=720); Traffic T=96 0.397 → 0.348; ETTm2 T=720 0.371 → 0.336.
- Memory footprint near DLinear-level on Traffic (862 channels); learnable parameters grow roughly linearly with look-back window.
- Ablations: residual connections improve MSE (ETTh1 T=720: 0.474→0.458); d_conv=2 better than 4; larger state expansion factor helps (default N set to 256); dimension expansion factor kept at 1; two levels outperform one level.

## 💡 Limitations & Identified Research Gaps
- Ranks second on Weather dataset at small prediction lengths — an area for future improvement.
- Qualitative alignment with ground truth could still be enhanced (Figure 3).
- Future work: extending TimeMachine to self-supervised learning settings.
- Only supervised LTSF on generic benchmarks; no domain-specific evaluation (e.g., EV charging) or probabilistic forecasts.

**Relevance to EV charging load forecasting:** This is a foundational method paper in the Mamba line — it established multi-scale quadruple-Mamba architectures and unified channel-mixing/channel-independence handling for long-horizon forecasting, directly informing the SSM-based EV forecasting designs in [[2026_Lahoti_Mamba_3_Sequence_Modeling]], [[2026_Hao_Mamba_KAN_HyKANet_EV]], and [[2026_Chen_PC_M3_Mamba_EV_Clusters]]; its Electricity/Traffic benchmarks are close proxies for station-level EV charging demand series.

## 📚 BibTeX & Citation Reference
```bibtex
@article{ahamed2024timemachine,
  title   = {TimeMachine: A Time Series is Worth 4 Mambas for Long-term Forecasting},
  author  = {Ahamed, Md Atik and Cheng, Qiang},
  journal = {arXiv preprint arXiv:2403.09898},
  year    = {2024},
  url     = {https://doi.org/10.48550/arXiv.2403.09898}
}
```

## 🔗 Key References & Citation Graph
- [[Mamba_SSM]] — Gu & Dao 2023 (arXiv:2312.00752): selective scan SSM, core inference engine of TimeMachine.
- [[S4]] — Gu et al.: structured state spaces; not compared since TiDE already outperformed it.
- [[PatchTST]] (ICLR 2023), [[iTransformer]] (ICLR 2024), [[DLinear]] (AAAI 2023), [[TiDE]] (TMLR 2023), [[Autoformer]] (NeurIPS 2021), [[Informer]] (AAAI 2021), [[Crossformer]] (ICLR 2022), [[FEDformer]] (ICML 2022), [[TimesNet]] (ICLR 2022), [[SCINet]] (NeurIPS 2022), [[Stationary_Transformer|Stationary / Non-stationary Transformers]] (NeurIPS 2022), [[RLinear]] — main baselines.
- [[RevIN]] — Kim et al., ICLR 2022: reversible instance normalization used for normalization.
- [[MambaTab]] — Ahamed & Cheng 2024 (arXiv:2401.08867): same authors' prior tabular Mamba work.
- Cited-by relation: [[2024_Liang_BiMamba_Bidirectional_Mamba_Forecasting]] critiques and builds upon TimeMachine's channel strategy selection.
