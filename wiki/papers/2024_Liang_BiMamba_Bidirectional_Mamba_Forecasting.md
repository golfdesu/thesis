---
type: paper
title: "Bi-Mamba+: Bidirectional Mamba for Time Series Forecasting"
authors: [Aobo Liang, Xingguo Jiang, Yan Sun, Xiaohou Shi, Ke Li]
year: 2024
journal_conference: "arXiv preprint (arXiv:2404.15772v3, cs.LG, 27 Jun 2024); BUPT & China Telecom Research Institute"
doi_url: "https://doi.org/10.48550/arXiv.2404.15772"
models_used: ["[[Bi-Mamba+]]", "[[Mamba]]"]
datasets_used: ["[[Weather_Dataset]]", "[[Traffic_Dataset]]", "[[Electricity_Dataset]]", "[[Solar_Dataset]]", "[[ETTh1]]", "[[ETTh2]]", "[[ETTm1]]", "[[ETTm2]]"]
features_used: ["[[Historical_Load]]"]
forecasting_horizon: "[[Long_Term]]"
metrics: ["[[MSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Bi-Mamba+: Bidirectional Mamba for Time Series Forecasting

## 🎯 Main Objective & Contribution
- Propose **Bi-Mamba+** for long-term time-series forecasting (LTSF) with three contributions:
	1. An improved **Mamba+ block** that adds a **forget gate** inside Mamba to selectively combine new features with historical features in a complementary manner, preserving historical information over longer ranges.
	2. A **bidirectional Mamba+ encoder** (forward + backward Mamba+) to comprehensively model interactions among time series elements.
	3. A **Series-Relation-Aware (SRA) decider** based on the Spearman correlation coefficient that automatically selects channel-independent vs. channel-mixing tokenization strategy per dataset, plus patch-wise (dual-scale-aware) tokenization for finer-grained dependency capture.
- Motivation: Transformers have quadratic complexity; existing SSM uses in LTSF are limited; prior unified channel strategies (e.g., TimeMachine) choose based only on look-back length and variable count, overlooking dataset statistics.

## 🧠 Methodology & Model Architecture
- **Task setup**: given $X_{in}=[x_1,\dots,x_L]\in\mathbb{R}^{L\times M}$ predict $X_{out}=[x_{L+1},\dots,x_{L+H}]\in\mathbb{R}^{H\times M}$.
- **Continuous SSM**:
$$h'(t) = Ah(t) + Bx(t), \qquad y(t) = Ch(t)$$
(Equation 1: Continuous-time SSM mapping input through hidden state; $A\in\mathbb{R}^{N\times N}$, $B\in\mathbb{R}^{D\times N}$, $C\in\mathbb{R}^{N\times D}$.)
- **Discretization** (zero-order hold, sampling interval Δ):
$$\bar{A} = \exp(\Delta A), \qquad \bar{B} = (\Delta A)^{-1}(\exp(\Delta A) - I)\cdot\Delta B$$
(Equation 2: ZOH discretized SSM parameters.)
$$h_k = \bar{A}\, h_{k-1} + \bar{B}\, x_k, \qquad y_k = C\, h_k$$
(Equation 3: Discretized recurrent SSM form.)
- **SRA decider**: computes Spearman coefficients $\rho_{i,j}$ between all series pairs on the training set, filters pairs with $\rho_{i,j}\geq\lambda$, counts max related series $\rho^\lambda_{max}, \rho^0_{max}$, relation ratio $r = \rho^\lambda_{max}/\rho^0_{max}$; chooses channel-mixing ($ts=1$) if $r \geq 1-\lambda$, else channel-independent ($ts=0$). λ = 0.6 by default.
- **Spearman coefficient equation**:
$$\rho_{i,j} = 1 - \frac{6\sum_{k=0}^{n}(\text{Rank}(t_i^k)-\text{Rank}(t_j^k))^2}{n(n^2-1)}$$
(Equation: Spearman rank correlation between series $t_i$ and $t_j$ with n observations.)
- **Patching**: each univariate sequence split into patches $p_i\in\mathbb{R}^{J\times P}$ with stride S and $J=\lceil\frac{L-P}{S}+1\rceil$; channel-independent tokens $E_{ind}\in\mathbb{R}^{M\times J\times D}$; channel-mixing groups same-index patches across series → $E_{mix}\in\mathbb{R}^{J\times M\times D}$. Default P = L/4, S = P/2. RevIN instance norm/denorm applied.
- **Mamba+ block** (Alg. 2): standard two-branch Mamba plus a forget gate $gate_f = 1 - gate_{b_2}$; output becomes:
$$output = \text{Linear}_{y'}(y\otimes\text{SiLU}(z) + x'\otimes(1-\sigma(z)))$$
(Equation: Mamba+ gated combination — SSM-filtered new features y plus convolutional features x′ weighted by forget gate, preserving long-range historical information.) Backward pass reprogrammed in CUDA (.cuh files) accordingly (Alg. 4).
- **Bi-Mamba+ encoder** (Alg. 3): two Mamba+ blocks run forward and backward (input flipped along time), outputs summed, then Add&Norm and feed-forward layers as in a Transformer encoder; stacked l ∈ {1,2,3} layers; flatten head + linear projector produce the forecast.
- **Loss function**:
$$L(Y,\hat{Y}) = \frac{1}{|Y|}\sum_{i=1}^{|Y|}(y^{(i)}-\hat{y}^{(i)})^2$$
(Equation 4: Mean Squared Error loss.)

## 📊 Dataset & Input Features
Eight real-world LTSF benchmark datasets:
| Dataset | Variables | Frequency | Length |
|---|---|---|---|
| Weather | 21 | 10 min | 52,696 |
| Electricity | 321 | 1 hour | 26,304 |
| Traffic | 862 | 1 hour | 17,544 |
| ETTh1 | 7 | 1 hour | 17,420 |
| ETTh2 | 7 | 1 hour | 17,420 |
| ETTm1 | 7 | 15 min | 69,680 |
| ETTm2 | 7 | 15 min | 69,680 |
| Solar | 137 | 10 min | 52,179 |

- Input features: raw historical multivariate values (look-back window L=96); no exogenous covariates.
- Links found in text: Code — https://github.com/Leopold2333/Bi-Mamba+
- Experimental platform: Ubuntu 20.04, Intel Xeon E5-2686 v4, 64GB RAM, 2× NVIDIA Tesla V100 32GB, CUDA 11.8, Python 3.10.14, PyTorch 2.1.1.

## 📈 Performance & Results
- Protocol: L=96 for all models, H ∈ {96,192,336,720}; MSE/MAE; ADAM + early stopping, ≤40 epochs; grid-searched LR in [5e-5 … 5e-3].
- Average improvement: **−4.72% MSE / −2.60% MAE vs iTransformer**; **−3.76% MSE / −2.67% MAE vs S-Mamba**.
- Selected Bi-Mamba+ results (MSE/MAE):
	- Electricity: T=96 → 0.140/0.238 (iTransformer 0.148/0.240, S-Mamba 0.142/0.238); T=720 → 0.197/0.293 (iTransformer 0.225/0.317).
	- Traffic: T=96 → 0.375/0.258 (iTransformer 0.395/0.268); T=720 → 0.440/0.288 (iTransformer 0.467/0.302).
	- Weather: T=96 → 0.159/0.205 (best; Crossformer MSE 0.158 but MAE 0.230); T=720 → 0.343/0.344.
	- Solar: T=96 → 0.184/0.222 vs iTransformer 0.203/0.237; T=720 → 0.250/0.273.
	- ETTh1: T=96 → 0.378/0.395; ETTh2: T=96 → 0.291/0.342; ETTm1: T=720 → 0.445/0.437; ETTm2: T=720 → 0.402/0.402.
- SRA decider outcomes: channel-mixing on Weather/Traffic/Electricity/Solar; channel-independent on the four ETT datasets. Removing it degrades average MSE by 3.56% (channel-independent-only) / 0.95% (channel-mixing-only).
- Ablations: removing backward direction worsens MSE/MAE by 3.25%/2.44%; removing residual connections by 4.37%/4.05%; replacing Mamba+ with dot-product Attention degrades performance.
- Efficiency: on large datasets (Traffic), memory grows linearly unlike iTransformer's quadratic growth; faster training than attention at equal embedding size; benefits from longer look-back windows (tested up to L=720) where Autoformer/DLinear degrade or plateau.

## 💡 Limitations & Identified Research Gaps
- Strategy switch threshold λ can change decisions near boundaries (e.g., ts flips between λ=0.6 and λ=0.8 on ETTh2/ETTm2), though impact is small when many highly correlated variables exist.
- Patch-wise tokens retain mostly local information with less global information compared to whole-sequence tokens (mitigated but inherent trade-off).
- Evaluated only on generic LTSF benchmarks; future work targets more diverse/complex scenarios such as network flow forecasting — EV charging load is an untested application domain.
- No probabilistic/uncertainty quantification of forecasts.

**Relevance to EV charging load forecasting:** As a foundational method paper in the Mamba line, its bidirectional selective-SSM encoder, forget-gate history preservation, and Spearman-based automatic channel-strategy selection transfer directly to multi-station EV charging series modeling in [[2026_Lahoti_Mamba_3_Sequence_Modeling]], [[2026_Hao_Mamba_KAN_HyKANet_EV]], and [[2026_Chen_PC_M3_Mamba_EV_Clusters]]; its Electricity (321-client hourly) and Traffic (862-sensor hourly) benchmarks closely proxy aggregate EV charging demand dynamics.

## 📚 BibTeX & Citation Reference
```bibtex
@article{liang2024bimambap,
  title   = {Bi-Mamba+: Bidirectional Mamba for Time Series Forecasting},
  author  = {Liang, Aobo and Jiang, Xingguo and Sun, Yan and Shi, Xiaohou and Li, Ke},
  journal = {arXiv preprint arXiv:2404.15772},
  year    = {2024},
  url     = {https://doi.org/10.48550/arXiv.2404.15772}
}
```

## 🔗 Key References & Citation Graph
- [[Mamba]] — Gu & Dao 2023 (arXiv:2312.00752): base selective SSM extended by the Mamba+ block.
- [[S4]] — Gu et al. 2021: structured SSM with HiPPO-initialized A matrix.
- [[HiPPO]] — Gu et al. 2020: recurrent memory with optimal polynomial projections.
- [[TimeMachine]] — [[2024_Ahamed_TimeMachine_Mamba_Long_Term_Forecasting]] (arXiv:2403.09898): quadruple-Mamba multi-scale model; Bi-Mamba+ critiques its heuristic channel-strategy choice and adopts its hyperparameter conventions (d_conv=2, expand=1).
- [[S-Mamba]] — Wang et al. 2024 (arXiv:2403.11144): MLP embeddings + Mamba for inter-series dependencies; key SSM baseline.
- [[MambaMixer]] — Behrouz et al. 2024 (arXiv:2403.19888): dual token/channel selection; alternative bidirectional design.
- Baselines: [[iTransformer]], [[PatchTST]], [[Crossformer]], [[Autoformer]], [[DLinear]], [[TimesNet]], [[WITRAN]] (NeurIPS 2024), [[CrossGNN]] (NeurIPS 2024).
- [[RevIN]] — Kim et al., ICLR 2022: reversible instance normalization.
- Vision-Mamba/U-Mamba (Zhu et al. 2024; Ma et al. 2024): bidirectional Mamba precedents from computer vision.
