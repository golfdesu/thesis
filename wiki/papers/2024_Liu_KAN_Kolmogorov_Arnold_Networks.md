---
type: paper
title: "KAN: Kolmogorov-Arnold Networks"
authors: [Ziming Liu, Yixuan Wang, Sachin Vaidya, Fabian Ruehle, James Halverson, Marin Soljacic, Thomas Y. Hou, Max Tegmark]
year: 2024
journal_conference: "arXiv:2404.19756 (accepted at ICLR 2025); MIT / Caltech / Northeastern / IAIFI"
doi_url: "https://doi.org/10.48550/arXiv.2404.19756"
models_used: ["[[KAN]]", "[[MLP]]", "[[LAN]]"]
datasets_used: ["[[Toy_Synthetic_Functions]]", "[[Special_Functions_Dataset]]", "[[Feynman_Dataset]]", "[[Knot_Theory_Dataset]]", "[[Anderson_Localization_Synthetic_Data]]"]
features_used: ["[[B-Spline_Basis_Functions]]", "[[Learnable_Edge_Activations]]", "[[Silu_Basis_Function]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[RMSE]]", "[[MSE]]", "[[L2_Error]]", "[[H1_Error]]", "[[Accuracy]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: KAN: Kolmogorov-Arnold Networks

## 🎯 Main Objective & Contribution
Proposes Kolmogorov-Arnold Networks (KANs) as alternatives to Multi-Layer Perceptrons (MLPs). While MLPs have **fixed activation functions on nodes** ("neurons"), KANs have **learnable activation functions on edges** ("weights") — every linear weight parameter is replaced by a univariate function parametrized as a B-spline. Contributions:
1. Generalization of the original depth-2 width-(2n+1) Kolmogorov-Arnold representation to **arbitrary widths and depths**, trainable with backpropagation.
2. Theoretical approximation guarantees (Theorem 2.1, "KAT") showing KANs can beat the curse of dimensionality via faster neural scaling laws ($\ell \propto N^{-(k+1)}$, i.e., $\alpha = k+1 = 4$ for cubic splines) vs. MLPs.
3. **Grid extension** technique for refining spline grids to improve accuracy without retraining from scratch.
4. Simplification techniques (sparsification, pruning, symbolification) making KANs interpretable "collaborators" for scientific discovery (knot theory, Anderson localization).

**Relevance to EV charging load forecasting:** This is THE foundational method paper of [[2026_Hao_Mamba_KAN_HyKANet_EV]], which adopts a Kolmogorov-Arnold decoder for EV demand prediction — the learnable spline activations on edges are precisely the mechanism HyKANet exploits for accurate, interpretable nonlinear mapping of exogenous drivers (temperature, price, calendar effects) onto charging load.

## 🧠 Methodology & Model Architecture

### Kolmogorov-Arnold Representation Theorem (Eq. 2.1)
For a smooth $f : [0,1]^n \to \mathbb{R}$:

$$f(\mathbf{x}) = f(x_1,\cdots,x_n) = \sum_{q=1}^{2n+1} \Phi_q \left( \sum_{p=1}^{n} \phi_{q,p}(x_p) \right),$$

where $\phi_{q,p} : [0,1] \to \mathbb{R}$ and $\Phi_q : \mathbb{R} \to \mathbb{R}$ are univariate continuous functions ("the only true multivariate function is addition").

### KAN Layer & Network
A KAN layer with $n_{in}$ inputs and $n_{out}$ outputs is a matrix of 1D functions $\Phi = \{\phi_{q,p}\}$, $p = 1,\dots,n_{in}$, $q = 1,\dots,n_{out}$ (Eq. 2.2). Activation values propagate as (Eq. 2.5):

$$x_{l+1,j} = \sum_{i=1}^{n_l} \tilde{x}_{l,j,i} = \sum_{i=1}^{n_l} \phi_{l,j,i}(x_{l,i}), \quad j = 1,\dots,n_{l+1}.$$

A general KAN is the composition of $L$ layers (Eq. 2.7):

$$\mathrm{KAN}(\mathbf{x}) = (\Phi_{L-1} \circ \Phi_{L-2} \circ \cdots \circ \Phi_1 \circ \Phi_0)\,\mathbf{x},$$

vs. an MLP: $\mathrm{MLP}(\mathbf{x}) = (W_{L-1} \circ \sigma \circ W_{L-2} \circ \sigma \circ \cdots \circ W_1 \circ \sigma \circ W_0)\mathbf{x}$ (Eq. 2.9). Shape notation: $[n_0, n_1, \cdots, n_L]$ (Eq. 2.3). Parameter count: $\mathcal{O}(N^2 L (G+k))$ vs. $\mathcal{O}(N^2 L)$ for MLPs (depth $L$, width $N$, spline order $k$, grid intervals $G$).

### Learnable Activation Function (Eq. 2.10-2.12)
Residual activation: basis function + spline:

$$\phi(x) = w_b\, b(x) + w_s\, \mathrm{spline}(x), \qquad b(x) = \mathrm{silu}(x) = \frac{x}{1+e^{-x}}, \qquad \mathrm{spline}(x) = \sum_i c_i B_i(x),$$

where $c_i$ are trainable B-spline coefficients ($c_i \sim \mathcal{N}(0,\sigma^2)$, $\sigma = 0.1$ at init; $w_s$ initialized to 1, $w_b$ Xavier-initialized). Spline grids are updated on the fly according to input activation ranges.

### Approximation Theory (Theorem 2.1, Eq. 2.15)
If $f = (\Phi_{L-1} \circ \cdots \circ \Phi_0)\mathbf{x}$ with each $\Phi_{l,i,j}$ being $(k+1)$-times continuously differentiable, then $k$-th order B-spline KANs satisfy, for any $0 \le m \le k$:

$$\left\| f - (\Phi^G_{L-1} \circ \Phi^G_{L-2} \circ \cdots \circ \Phi^G_0)\mathbf{x} \right\|_{C^m} \le C\, G^{-k-1+m},$$

i.e., residue rate **independent of dimension** → beats curse of dimensionality; predicted scaling exponent $\alpha = k+1 = 4$ (cubic splines), vs. Sharma & Kaplan $\alpha = (k+1)/d$ and Michaud et al. $\alpha = (k+1)/d^\ast = (k+1)/2$ for MLPs.

### Grid Extension / Refinement (Eq. 2.16)
Refine a coarse-grid spline (order $k$, $G_1$ intervals, grid points $\{t_0=a,\dots,t_{G_1}=b\}$ augmented by $k$ knots on each side, $G_1+k$ basis functions) to a finer grid ($G_2$ intervals) by least-squares fitting new coefficients to the old coarse spline:

$$\{c'_j\} = \operatorname*{argmin}_{\{c'_j\}} \mathop{\mathbb{E}}_{x\sim p(x)} \left( \sum_{j=0}^{G_2+k-1} c'_j B'_j(x) - \sum_{i=0}^{G_1+k-1} c_i B_i(x) \right)^2,$$

implemented by least squares; performed independently for all splines in a KAN. Produces **staircase-like loss curves**: training loss drops sharply after each refinement; test loss is U-shaped with optimum near the interpolation threshold (e.g., $[2,5,1]$ KAN with $15G$ params on 1000 samples predicts threshold $G \approx 67$, observed $G \sim 50$).

### Interpretability Pipeline (Eq. 2.17-2.23)
- **Sparsification**: L1 norm of activation $|\phi|_1 = \frac{1}{N_p}\sum_{s=1}^{N_p} |\phi(x^{(s)})|$; layer entropy $S(\Phi) = -\sum_{i,j} \frac{|\phi_{i,j}|_1}{|\Phi|_1}\log\frac{|\phi_{i,j}|_1}{|\Phi|_1}$; total objective:

$$\ell_{\text{total}} = \ell_{\text{pred}} + \lambda\left( \mu_1 \sum_{l=0}^{L-1}|\Phi_l|_1 + \mu_2 \sum_{l=0}^{L-1} S(\Phi_l) \right),$$

with typically $\mu_1 = \mu_2 = 1$ and $\lambda \in \{10^{-2}, 10^{-3}\}$ controlling overall sparsity.
- **Pruning**: node importance scores $I_{l,i} = \max_k(|\phi_{l-1,i,k}|_1)$, $O_{l,i} = \max_j(|\phi_{l+1,j,i}|_1)$; prune nodes whose scores fall below threshold $\theta = 10^{-2}$.
- **Symbolification**: `fix_symbolic(l,i,j,f)` fits affine parameters so that $y \approx c\,f(ax+b)+d$ (iterative grid search over $a,b$ + linear regression). Example: pruned $[2,1,1]$ KAN recovers $f(x,y)=\exp(\sin(\pi x)+y^2)$ to machine precision.
- **Continual learning**: locality of B-spline bases avoids catastrophic forgetting in sequential 1D regression (5 Gaussian peaks presented phase-wise), unlike global MLP activations.

## 📊 Dataset & Input Features
All datasets are synthetic/simulated (no dataset URLs in the paper besides the code repository):
1. **Toy synthetic functions** — five functions with known smooth KA representations, incl. $f(x,y)=\exp(\sin(\pi x)+y^2)$, $f(x)=J_0(20x)$ (Bessel), $f(x,y)=xy$, 100-dim $\exp\big(\frac{1}{100}\sum_i \sin^2(\frac{\pi x_i}{2})\big)$, and 4-dim compositions; 1000 training samples, LBFGS 1800 steps, grids $G \in \{3,5,10,20,50,100,200,500,1000\}$.
2. **Special functions dataset** — 15 scipy.special functions (ellipj, ellipkinc, ellipeinc, jv, yv, kv, iv, lpmv m=0/1/2, sph_harm variants).
3. **Feynman dataset** — Feynman_no_units variant, equations with ≥2 variables from Feynman's textbooks (per AI Feynman, Udrescu & Tegmark 2020); inputs drawn randomly from $(-1,1)$.
4. **Knot theory dataset** — 17 topological invariants as inputs, signature (even integers, one-hot over 14 classes) as output; unsupervised mode uses all 18 variables; setup follows DeepMind (Davies et al., Nature 2021).
5. **Anderson localization synthetic data** — numerically generated eigenvalue/fractal-dimension data from quasiperiodic tight-binding models: Mosaic Model (MM), generalized Aubry-André model (GAAM), modified Aubry-André model (MAAM); quasiperiodicity via golden ratio $b = \frac{1+\sqrt{5}}{2}$.

Input features are simply the function variables ($x_p$) fed to edge spline activations; code: https://github.com/KindXiaoming/pykan (`pip install pykan`).

## 📈 Performance & Results
- **Scaling laws (Fig. 3.1)**: KANs nearly saturate the theoretical $\alpha = 4$ exponent (test RMSE $\propto N^{-4}$) on all five toy tasks including the 100-dim example; MLPs scale slowly (≈ $N^{-2}$ or worse) and plateau quickly.
- **Grid extension**: $[2,1,1]$ KAN test RMSE scales roughly $\propto G^{-3}$ (mean) / closer to $G^{-4}$ (median of squared losses; boundary effects).
- **Special functions (Table 1)**: KANs Pareto-dominate MLPs on all 15 functions; examples — ellipj: best KAN RMSE $1.33\times10^{-4}$ vs MLP $6.48\times10^{-4}$; lpmv(0,x,y): KAN $5.25\times10^{-5}$ vs MLP $1.74\times10^{-2}$; sph_harm(0,1): KAN $2.21\times10^{-7}$ vs MLP $1.25\times10^{-6}$.
- **Feynman (Table 2)**: MLPs and KANs behave comparably on average ("too simple" for KANs); auto-discovered (pruned) KAN shapes usually **smaller than human-constructed** ones (e.g., relativistic velocity addition realized by a 2-layer KAN via rapidity addition).
- **PDE solving (Poisson, PINN framework, Eq. 3.2)**: a 2-layer width-10 KAN is **100× more accurate** than a 4-layer width-100 MLP ($10^{-7}$ vs $10^{-5}$ MSE) with **100× fewer parameters** ($10^2$ vs $10^4$); steeper scaling laws in both L2 and H1 norms; but KAN training ≈10× slower.
- **Knot signature classification (Table 3)**: $[17,1,14]$ KAN ($G=3$, $k=3$, ≈200 params) achieves **81.6%** test accuracy vs DeepMind's 4-layer width-300 MLP (**78.0%**, ≈$3\times10^5$ params). Ablations: $\mu_r$ alone 65.0% vs $\mu_i$ alone 43.8%; a symbolic formula using only $\mu_r,\lambda$ reaches 77.8%; best KAN-derived formula D reaches 84.0%.
- **Unsupervised knot relations**: rediscovered $V = \mu_r \lambda$ (cusp volume) and the linear bound $2r$ upper-bounding short geodesic $g_r$, plus the signature–$(\mu_r,\mu_i,\lambda)$ dependence, without prior labeling.
- **Mobility edges (Table 5)**: GAAM KAN-auto formula 99.0% accuracy vs theory 99.2%; MAAM KAN-auto 97.1%, manual+auto refinement up to 97.7% (theory 98.6%).

## 💡 Limitations & Identified Research Gaps
- **Slow training**: KANs are typically **10× slower than MLPs** for the same parameter count (no batch computation across distinct activations); authors deem it an engineering problem (multi-head/grouped activations proposed).
- No generalized "deep" Kolmogorov-Arnold theorem exists; mathematical understanding of deeper KANs and dimension-dependence of constant $C$ left as future work.
- Results demonstrated only on **small-scale AI + Science tasks**; unclear whether fast scaling holds for large tasks (e.g., language modeling).
- Grid-size updates near the number of training points cause sudden performance drops (Appendix E); interpretability can be subtle since pruning may squash information into smaller graphs; unsupervised relation discovery relies on random seeds.
- For EV forecasting ([[2026_Hao_Mamba_KAN_HyKANet_EV]] context): vanilla KANs' computational cost motivates hybrid architectures combining KAN decoders with efficient sequence backbones rather than pure KAN stacks.

## 📚 BibTeX & Citation Reference
```bibtex
@article{liu2024kan,
  title   = {KAN: Kolmogorov-Arnold Networks},
  author  = {Liu, Ziming and Wang, Yixuan and Vaidya, Sachin and Ruehle, Fabian and Halverson, James and Solja{\v c}i{'c}, Marin and Hou, Thomas Y. and Tegmark, Max},
  journal = {arXiv preprint arXiv:2404.19756},
  year    = {2024},
  note    = {Accepted at ICLR 2025. DOI: 10.48550/arXiv.2404.19756}
}
```

## 🔗 Key References & Citation Graph
- Kolmogorov [Dokl. Akad. Nauk 1956/1957] & Arnold — original representation theorem; Braun & Griebel 2009 (constructive proof).
- Lai & Shen 2021 (arXiv:2112.09963) — depth-2 KA breaking curse of dimensionality.
- De Boor 1978 — B-spline theory underlying Theorem 2.1.
- Sharma & Kaplan 2020; Michaud et al. 2023 (Precision machine learning); Poggio et al. 2020 — competing neural scaling law theories.
- Raissi et al. 2019 (PINNs); Karniadakis et al. 2021 — PINN framework used for the Poisson experiment.
- Davies et al., Nature 600:70–74, 2021 — DeepMind knot-theory dataset/benchmark.
- Udrescu & Tegmark 2020 (AI Feynman) — source of Feynman equations.
- Wang et al. 2020 / Ganeshan et al. 2015 / Biddle & Das Sarma 2010 — quasiperiodic models (MM/GAAM/MAAM) for Anderson localization.
- **Forward link**: foundational architecture for [[2026_Hao_Mamba_KAN_HyKANet_EV]] (Kolmogorov-Arnold decoder for EV demand prediction).

