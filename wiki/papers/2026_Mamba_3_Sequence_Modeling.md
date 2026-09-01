---
type: paper
title: "Mamba-3: Improved Sequence Modeling using State Space Principles"
authors: [Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu]
year: 2026
journal_conference: "arXiv preprint (arXiv:2603.15569); CMU / Princeton / Together AI / Cartesia AI"
doi_url: "https://arxiv.org/abs/2603.15569"
models_used: ["[[Mamba-3]]", "[[Mamba_SSM]]", "[[Mamba_SSM]]", "[[Gated_DeltaNet]]", "[[Transformer]]", "[[S4]]"]
datasets_used: ["[[FineWeb-Edu]]", "[[LAMBADA]]", "[[HellaSwag]]", "[[PIQA]]", "[[ARC]]", "[[WinoGrande]]", "[[OpenBookQA]]", "[[RULER_NIAH]]"]
features_used: ["[[Text_Tokens]]"]
forecasting_horizon: ""
metrics: ["[[Perplexity]]", "[[Accuracy]]", "[[Decode_Latency]]", "[[Arithmetic_Intensity]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Mamba-3: Improved Sequence Modeling using State Space Principles

## 🎯 Main Objective & Contribution
- From an **inference-first** perspective: sub-quadratic linear models (SSMs, linear attention) have constant memory/linear compute but trade off model quality and state-tracking capability for efficiency (e.g., Mamba-2 fails parity), and their decoding algorithms are memory-bound with low arithmetic intensity (~2.5 ops/byte vs ~295 for bf16 matmul on H100).
- **[[Mamba-3]]** introduces three SSM-principled improvements: (1) **exponential-trapezoidal discretization** → more expressive recurrence that acts as an implicit width-2 convolution inside the core recurrence, obviating the short causal conv; (2) **complex-valued state transitions**, implemented efficiently via *data-dependent RoPE*, restoring rotational dynamics needed for state tracking (TC0 tasks like parity); (3) **Multi-Input Multi-Output (MIMO)** formulation raising decoding FLOPs up to 4× at fixed state size without increasing wall-clock decode latency.
- Results: at 1.5B scale, +0.6 avg downstream accuracy over GDN (SISO) and +1.8 total with MIMO; matches Mamba-2 perplexity with half the state size. Code/kernels: https://github.com/state-spaces/mamba

## 🧠 Methodology & Model Architecture
- **Continuous SSM ODE**: $\dot{h}(t) = A(t)\,h(t) + B(t)\,x(t), \quad y(t) = C(t)^\top h(t)$; Mamba-2's exponential-Euler recurrence ($\alpha_t := e^{\Delta_t A_t}$):
$$ h_t = \alpha_t h_{t-1} + \gamma_t B_t x_t, \qquad y_t = C_t^\top h_t \tag{1} $$
- **State Space Duality parallel form**: $Y = (L \odot C B^\top) X$ with structured mask $L \in \mathbb{R}^{T\times T}$ (Eq. 2); Mamba-2's mask $L = [\alpha^{i-j}]\cdot\text{Diag}(\gamma)$ (Eq. 3).
- **Proposition 1 (Exponential-Trapezoidal Discretization)** — second-order approximation of the state-input integral with data-dependent convex combination $\lambda_t \in [0,1]$ of endpoints:
$$ h_t = e^{\Delta_t A_t} h_{t-1} + (1-\lambda_t)\Delta_t e^{\Delta_t A_t} B_{t-1} x_{t-1} + \lambda_t \Delta_t B_t x_t \tag{5} $$
$$ \equiv \alpha_t h_{t-1} + \beta_t B_{t-1}x_{t-1} + \gamma_t B_t x_t,\quad \alpha_t := e^{\Delta_t A_t},\ \beta_t := (1-\lambda_t)\Delta_t e^{\Delta_t A_t},\ \gamma_t := \lambda_t\Delta_t \tag{6} $$
Generalizes classical trapezoid ($\lambda_t=\frac{1}{2}$) and Mamba-2's Euler rule ($\lambda_t=1$); local truncation error $O(\Delta_t^3)$ if $\lambda_t = \frac{1}{2}+O(\Delta_t)$; default uses learned gate $\lambda_t = \sigma(u_t)$. Induced SSD mask (Eq. 7) is a 1-semiseparable matrix composed with a 2-band matrix — equivalent to a data-dependent size-2 convolution on the state-input within the recurrence.
- **Complex-valued SSM**:
$$ \dot{h}(t) = \text{Diag}\big(A(t) + i\theta(t)\big)\,h(t) + \big(B(t) + i\hat{B}(t)\big)x(t), \quad y(t) = \text{Re}\big((C(t)+i\hat{C}(t))^\top h(t)\big) \tag{8} $$
- **Proposition 2 (Complex-to-Real Equivalence)** — under exponential-Euler discretization becomes real SSM with block-diagonal rotation transition:
$$ h_t = e^{\Delta_t A_t} R_t h_{t-1} + \Delta_t B_t x_t, \qquad y_t = C_t^\top h_t \tag{9} $$
with $R_t := \text{Block}(\{R(\Delta_t\theta_t[i])\}_{i=1}^{N/2})$, $R(\theta)=\begin{bmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{bmatrix}$.
- **Proposition 3 (Data-Dependent RoPE Equivalence)** — rotations absorbed into $B,C$ via cumulative products ("RoPE trick"):
$$ h_t = e^{\Delta_t A_t} h_{t-1} + \Big(\prod_{i=0}^{t} R_i^\top\Big)\Delta_t B_t x_t, \qquad y_t = \Big[\Big(\prod_{i=0}^{t} R_i^\top\Big) C_t\Big]^\top h_t \tag{10} $$
- **Proposition 4 (Rotary Equivalence with Exponential-Trapezoidal Discretization)** — full Mamba-3 recurrence:
$$ h_t = \alpha_t h_{t-1} + \beta_t\Big(\prod_{i=0}^{t-1} R_i^\top\Big)B_{t-1}x_{t-1} + \gamma_t\Big(\prod_{i=0}^{t} R_i^\top\Big)B_t x_t, \qquad y_t = \Big[\Big(\prod_{i=0}^{t} R_i^\top\Big) C_t\Big]^\top h_t \tag{11} $$
- **MIMO SSM state update** (rank $R$, head dim $P$; arithmetic intensity $\Theta(R)$ vs $\Theta(1)$ for SISO):
$$ H_t = a_t H_{t-1} + B_t X_t^\top \in \mathbb{R}^{N\times P}, \qquad Y_t = H_t^\top C_t \in \mathbb{R}^{P\times R} $$
Trained via chunked SSD algorithm with MIMO chunk size $C_{\text{MIMO}} \leftarrow \frac{1}{R}C_{\text{SISO}}$ giving $O(8TRN^2)$ FLOPs ($R$× increase, not $R^2$); Triton forward kernels ~on par with Mamba-2, MIMO only 2× slower at $R=4$. Parameter-matched by reducing MLP inner dim (e.g., 4096→3824 at 1.5B).
- **Architecture**: Llama-style alternating Mamba-3 + SwiGLU blocks, pre-norm; adds BC/QK RMSNorm after $B,C$ projections (removes post-gate RMSNorm in pure models; reintroduced pre-gate grouped RMSNorm for hybrid long-context extrapolation), learnable head-specific channel-wise $B,C$ biases, no short causal conv.

## 📊 Dataset & Input Features
- Pretraining: 100B tokens of [[FineWeb-Edu]] (Penedo et al. 2024, https://arxiv.org/abs/2406.17557), Llama-3.1 tokenizer (https://arxiv.org/abs/2407.21783), 2K context, bfloat16; scales 180M/440M/880M/1.5B; expand factor 2, $d_{\text{state}}=128$, head dim 64. Pareto experiments: 440M trained to 2× Chinchilla tokens sweeping $d_{\text{state}}\in\{16,32,64,128\}$.
- Evaluation: LM Evaluation Harness v0.4.3 (https://zenodo.org/records/12608602) zero-shot on LAMBADA, HellaSwag, PIQA, ARC-Easy/Challenge, WinoGrande, OpenBookQA; retrieval suite SWDE/SQuAD/FDA/TriviaQA/NQ/DROP in cloze format (truncated 2K); synthetic NIAH from RULER (https://arxiv.org/abs/2404.06654); Chomsky-hierarchy state-tracking synthetics (Parity, Modular Arithmetic ± brackets).
- No EV charging data; this is the foundational sequence-modeling architecture paper underlying [[PC-M3]]-style EV applications.

## 📈 Performance & Results
- **Downstream average accuracy** (100B FineWeb-Edu): Mamba-3-SISO beats all baselines at every scale (43.4 vs GDN 43.2 @180M; 49.8 vs 49.7 @440M; 54.4 vs 53.7 @880M; **56.4 vs GDN 55.8, Transformer 55.4 @1.5B**). MIMO ($R=4$) adds ~+1.2 pts over SISO (**57.6 @1.5B**; +2.2 over Transformer, +1.9 over Mamba-2, +1.8 over GDN). Validation ppl 10.24 (MIMO 1.5B) vs 10.35 (SISO), 10.45 (GDN), 10.47 (Mamba-2), 10.51 (Transformer).
- **State-size Pareto**: Mamba-3 MIMO at $d_{\text{state}}=64$ matches Mamba-2 at $d_{\text{state}}=128$ → same quality at half decode latency; downward Pareto shift also vs GDN.
- **State tracking** (scaled acc): Parity 100.00 / Arith w/o brackets 98.51 / w/ brackets 87.75 for Mamba-3 vs Mamba-3 w/o RoPE 2.27/1.49/0.72, standard-RoPE 1.56/20.70/2.62, Mamba-2 0.90/47.81/0.88; competitive with state-tracking-enabled GDN [-1,1] (100/99.25/93.50).
- **Retrieval** (1.5B): competitive on associative recall/QA (TQA 64.5, SQuAD 41.7 MIMO) but weaker than Transformer (48.9→58.4 range) on semi/unstructured extraction (SWDE 28.5–36.3, FDA 23.4–29.3); markedly better OOD length generalization on NIAH than Mamba-2 (e.g., NIAH-Single-3@4096: SISO 34.2 vs Mamba-2 13.4). Hybrid 5:1 linear:attention with pre-gate grouped RMSNorm reaches near-perfect NIAH (100.0/97.2/56.8) and beats Transformer on LM avg (56.1–56.4 vs 55.4).
- **Component ablation** (440M, Chinchilla): −bias −trap 16.68 → full (bias+trap) 15.72; adding short conv back hurts slightly (15.85) → bias+trap makes conv redundant. $\lambda_t$ ablation: learned σ(u_t) 15.72 < fixed ½ 15.76 < Euler 15.81.
- **Kernel latency** (H100, batch 128, bf16, 1.5B): decode per-token Mamba-3 SISO 0.156 ms ($d_{state}=128$) — fastest vs Mamba-2 0.203, GDN 0.257; MIMO 0.179 ms still faster than Mamba-2 while computing 4× decode FLOPs. Prefill+decode @16K: SISO 140.61 s vs GDN 145.87, Mamba-2 149.02, vLLM Llama-3.2-1B 976.50 s.

## 💡 Limitations & Identified Research Gaps
- Fixed-state linear models remain weak at extracting information from semi-structured/unstructured data (SWDE, FDA) versus exact attention; hybrids with interleaved self-attention are needed to close long-context retrieval gaps.
- Ideal norm type/placement for hybrids (grouped vs default RMS, pre- vs post-gate) involves unintuitive competing tradeoffs.
- Second-order error bound of trapezoidal rule only holds if $\lambda_t=\frac{1}{2}+O(\Delta_t)$, which empirically is *not* enforced (learned $\sigma(u_t)$ performs better) — theory-practice gap.
- MIMO training costs up to $R\times$ more FLOPs (moderate prefill overhead); vehicle-as-channel-style reuse at ranks far beyond validated $R\in\{4,8,16\}$ carries no quality guarantees (as noted by downstream users).

## 📚 BibTeX & Citation Reference
```bibtex
@article{lahoti2026mamba3,
  author  = {Lahoti, Aakash and Li, Kevin Y. and Chen, Berlin and Wang, Caitlin and Bick, Aviv and Kolter, J. Zico and Dao, Tri and Gu, Albert},
  title   = {{Mamba-3}: Improved Sequence Modeling using State Space Principles},
  journal = {arXiv preprint arXiv:2603.15569},
  year    = {2026}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] (Vaswani et al., NeurIPS 2017) — Transformer baseline lineage [53]
- [[Mamba_SSM]] selective SSMs (Gu & Dao, arXiv:2312.00752) [18]; [[Mamba_SSM]] / Structured State Space Duality (Dao & Gu, ICML 2024) [11]; [[S4]] (Gu et al., ICLR 2022) [19]; S5 [44]; LRU [37]
- [[Gated_DeltaNet]] (Yang, Kautz & Hatamizadeh, arXiv:2412.06464) [60]; Gated Linear Attention [61]; DeltaNet parallelization [62]
- RoPE/RoFormer (Su et al., arXiv:2104.09864) [46] — basis of the data-dependent "RoPE trick"
- State tracking theory: Grazzi et al. negative eigenvalues [17]; Merrill, Petty & Sabharwal "Illusion of State" [32]; Sarrof et al. formal-language capacity [42]; Block-Biased Mamba universal approximation (Yu & Erichson) [63]
- Linear attention (Katharopoulos et al.) [26]; fast weight programmers (Schlag et al.) [43]; RetNet [49]; test-time training/regression line [48,50,55]
- Hybrid Mamba LM studies (Waleffe et al.) [54]; Nemotron-H [35]; Kimi Linear [27]; Qwen3 [58]
- Applied in EV domain by [[2026_PC_M3_Mamba_EV_Clusters]] ([[PC-M3]]) and cited by [[2026_Mamba_KAN_HyKANet_EV]]
