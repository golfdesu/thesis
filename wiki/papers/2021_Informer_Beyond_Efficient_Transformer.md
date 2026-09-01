---
type: paper
title: "Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting"
authors: [Haoyi Zhou, Shanghang Zhang, Jieqi Peng, Shuai Zhang, Jianxin Li, Hui Xiong, Wancai Zhang]
year: 2021
journal_conference: "AAAI 2021 (Best Paper Award)"
doi_url: "https://arxiv.org/abs/2012.07436"
models_used: ["[[Informer]]", "[[ProbSparse_Attention|ProbSparse Self-Attention]]", "[[Self-Attention_Distilling]]", "[[Generative_Decoder|Generative Style Decoder]]", "[[LogTrans]]", "[[Reformer]]", "[[LSTMa]]", "[[LSTnet]]", "[[DeepAR]]"]
datasets_used: ["[[ETT]]", "[[Electricity_ECL]]", "[[Weather]]"]
features_used: ["[[Oil_Temperature|Oil Temperature (target)]]", "[[Power_Load_Features|6 Power Load Features]]", "[[Temperature|Wet Bulb (target)]]", "[[Climate_Features|11 Climate Features]]", "[[Uniform_Input_Representation|Global/Local Timestamp Embeddings]]", "[[ProbSparse_Attention]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting

## 🎯 Main Objective & Contribution
- **Core problem**: Long sequence time-series forecasting ([[Long_Term_Forecasting]]) — vanilla [[Transformer]] has three LSTF limitations: (1) quadratic $O(L^2)$ self-attention time/memory per layer; (2) memory bottleneck $O(J \cdot L^2)$ when stacking $J$ layers for long inputs; (3) speed plunge of step-by-step dynamic decoding for long outputs.
- **Primary contribution**: **[[Informer]]** with three distinctive characteristics:
  - **[[ProbSparse_Attention|ProbSparse self-attention]]**: $O(L\log L)$ time and memory via KL-divergence-based query sparsity measurement selecting only Top-$u$ dominant queries.
  - **Self-attention distilling**: halves cascading layer input via conv + max-pooling, total space complexity $O((2-\epsilon)L\log L)$.
  - **[[Generative_Decoder|Generative style decoder]]**: predicts the whole long output in ONE forward pass (no autoregressive dynamic decoding), avoiding cumulative error spreading.

## 🧠 Methodology & Model Architecture
- **LSTF problem setup**: rolling forecasting with fixed window; input $X^t = \{x_1^t,\ldots,x_{L_x}^t \mid x_i^t \in \mathbb{R}^{d_x}\}$, output $Y^t = \{y_1^t,\ldots,y_{L_y}^t \mid y_i^t \in \mathbb{R}^{d_y}\}$, $L_y \gg$ prior works.
- **Canonical self-attention as kernel smoother** (Eq. 1):
$$A(q_i, K, V) = \sum_j \frac{k(q_i,k_j)}{\sum_l k(q_i,k_l)} v_j = \mathbb{E}_{p(k_j|q_i)}[v_j]$$
where $p(k_j|q_i) = k(q_i,k_j)/\sum_l k(q_i,k_l)$ and $k(q_i,k_j)$ is the asymmetric exponential kernel $\exp(q_i k_j^\top/\sqrt{d})$. Attention scores form a **long tail distribution** (Appendix C) — few dot-product pairs dominate.
- **Query sparsity measurement** (Eq. 2), KL divergence between attention distribution $p$ and uniform $q$ (dropping constants):
$$M(q_i, K) = \ln\sum_{j=1}^{L_K} e^{\frac{q_i k_j^\top}{\sqrt{d}}} - \frac{1}{L_K}\sum_{j=1}^{L_K} \frac{q_i k_j^\top}{\sqrt{d}}$$
(first term = Log-Sum-Exp of $q_i$ on all keys; second = arithmetic mean). Larger $M$ → more "diverse"/dominant query.
- **ProbSparse self-attention** (Eq. 3): each key attends only to $u = c \cdot \ln L_Q$ dominant queries ($c$ = sampling factor):
$$A(Q, K, V) = \text{Softmax}\left(\frac{\bar{Q}K^\top}{\sqrt{d}}\right)V$$
where $\bar{Q}$ contains only the Top-$u$ queries under $M(q,K)$; layer memory $O(L_K \ln L_Q)$.
- **Max-mean measurement approximation** (Lemma 1 + Eq. 4) avoiding quadratic traversal and LSE instability:
$$M(q_i, K) = \max_j\left\{\frac{q_i k_j^\top}{\sqrt{d}}\right\} - \frac{1}{L_K}\sum_{j=1}^{L_K}\frac{q_i k_j^\top}{\sqrt{d}}$$
Only $U = L_K \ln L_Q$ random dot-product pairs sampled to compute $M$; total ProbSparse complexity $O(L\ln L)$ (Algorithm 1 pseudo-code in Appendix E.2).
- **Self-Attention Distilling** (Eq. 5), forwarding from $j$-th into $(j+1)$-th layer:
$$X_{j+1}^t = \text{MaxPool}\Big(\text{ELU}\big(\text{Conv1d}([X_j^t]_{AB})\big)\Big)$$
where $[\cdot]_{AB}$ = attention block; Conv1d kernel width 3 + ELU activation; max-pooling stride 2 downsamples to half → memory $O((2-\epsilon)L\log L)$. Pyramid replicas of stacks with halved inputs; all stack feature maps concatenated as encoder output.
- **Generative decoder** (Eq. 6):
$$X_{de}^t = \text{Concat}(X_{token}^t, X_0^t) \in \mathbb{R}^{(L_{token}+L_y)\times d_{model}}$$
start token $X_{token}^t$ (e.g., earlier known slice before target, e.g. 5 days for a 7-day prediction) + zero placeholder $X_0^t$ containing target timestamps; masked multi-head ProbSparse attention (masked dot-products set to $-\infty$, prevents attending to future positions); FCN outputs full horizon in one forward pass. Predictions rely solely on timestamps → can predict with offsets without error accumulation (Table 6).
- **Uniform input representation** (Appendix B, Eqs. 7–8): position embedding + learnable global timestamp stamp embeddings (minutes/hours/week/month/holiday, vocab ≤60) + 1-D conv scalar projection:
$$PE(pos,2j)=\sin(pos/(2L_x)^{2j/d_{model}}),\quad PE(pos,2j+1)=\cos(pos/(2L_x)^{2j/d_{model}})$$
$$X_{feed}^t[i]=\alpha u_i^t + PE(L_x\times(t-1)+i,\cdot)+\sum_p [SE(L_x\times(t-1)+i)]_p$$
- **Loss**: MSE on predictions w.r.t. target sequences.
- Implementation (Table 7): encoder embedding $d=512$, main stack N=4 ProbSparse blocks (multi-head h=16, d=32; FFN inner dim 2048, GELU; dropout p=0.1) + distilling (conv1d ELU, maxpool stride 2), replica stack at 1/4 input; decoder N=2 layers (masked PSB + standard multi-head attention h=8, d=64); Adam lr $10^{-4}$ decaying ×½ per epoch, 8 epochs w/ early stopping, batch size 32, grid search over hyperparameters; Nvidia V100 32GB; results averaged over 5 random train/val shifts (10% validation).

## 📊 Dataset & Input Features
Four datasets (2 collected real-world + 2 public benchmarks):
- **[[ETT]]** (Electricity Transformer Temperature, authors' own release): 2-year data from two separated counties in China; hourly [[ETT]], [[ETT]] and 15-min-level [[ETT]]; each point = target "oil temperature" + 6 power load features; train/val/test = 12/4/4 months — https://github.com/zhouhaoyi/ETDataset
- **[[Electricity_ECL]]** (Electricity Consuming Load): electricity consumption (Kwh) of 321 clients; converted to hourly consumption of 2 years due to missing data; 'MT 320' as target; train/val/test = 15/3/4 months — https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
- **[[Weather]]**: local climatological data for ~1600 U.S. locations, 2010–2013, hourly; target "wet bulb" + 11 climate features; train/val/test = 28/10/10 months — https://www.ncei.noaa.gov/data/local-climatological-data/
- Prediction windows prolonged progressively: {1d, 2d, 7d, 14d, 30d, 40d} in {ETTh, ECL, Weather}, {6h, 12h, 24h, 72h, 168h} in ETTm; rolling evaluation with stride = 1; inputs zero-mean normalized.
- Code: https://github.com/zhouhaoyi/Informer2020

## 📈 Performance & Results
Baselines: Informer† (canonical self-attention variant), LogTrans, Reformer, LSTMa, LSTnet, DeepAR, ARIMA, Prophet.
- **Multivariate (Table 2)**: Informer wins 33/48 cases vs Informer† 14. Example ETTh1 predict-168: Informer 0.931 MSE vs LogTrans 1.002, Reformer 1.824, LSTMa 1.212; ECL predict-720: 0.406/0.443 (MSE/MAE) vs Reformer 2.009/1.170. MSE decreases vs RNN-based LSTMa/LSTnet by **26.6% (at 168)**, **28.2% (at 336)**, **34.3% (at 720)** on average.
- **Univariate (Table 1)**: Informer wins 32 cases vs Informer† 12. MSE decrease vs LSTMa: **26.8% (168)**, **52.4% (336)**, **60.1% (720)**; vs DeepAR/ARIMA/Prophet average: **49.3% (168)**, **61.1% (336)**, **65.1% (720)**. DeepAR better only on ECL short horizons (≤336).
- **Prediction capacity**: error rises smoothly/slowly with growing horizon (vs LSTM failing beyond length 48, Fig. 1b); granularity experiment shows ETTm1 minute-level results aligned with ETTh1 hour-level hold across granularities.
- **Complexity comparison (Table 4)**: Informer train/test both $O(L\log L)$, 1 decoding step vs Transformer $O(L^2)$/L steps, LogTrans test $O(L^2)$, Reformer L steps.
- **ProbSparse ablation (Table 3)**: extreme long-input setting {batch=8, heads=8, dim=64}: Informer reaches encoder input 1440 (predict-1440 MSE 0.216) where LogTrans OOMs; Reformer degrades badly (1.861–2.243 MSE).
- **Distilling ablation (Table 5)**: removing distilling (Informer‡) OOMs with inputs >720; distilled model benefits from longer inputs.
- **Generative decoder ablation (Table 6)**: prediction robust to temporal offsets (+0…+168) while dynamic-decoding counterpart fails/unacceptable metrics.
- **Efficiency (Fig. 5)**: best training efficiency among Transformer-based methods; much faster inference via one-step generative decoding.
- Sensitivity (Fig. 4): sampling factor c stabilized ≥5 (c=5 used in practice); joining L and L/4 stacks most robust.

## 💡 Limitations & Identified Research Gaps
- Multivariate advantage shrinks vs univariate — attributed to anisotropy of feature dimensions' prediction capacity ("beyond the scope of this paper").
- ProbSparse relies on the long-tail sparsity assumption and max-mean approximation (Lemma 1/Proposition 1 are probabilistic, not exact).
- Dynamic decoding baselines (Reformer) perform poorly in LSTF — architecture choice (generative decoder) matters more than attention alone.
- Gap for EV charging load forecasting: Informer's $O(L\log L)$ attention + single-forward multi-step decoder directly applicable to long-horizon station/load series; serves as key baseline in EV forecasting benchmarks.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{zhou2021informer,
  title={Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting},
  author={Zhou, Haoyi and Zhang, Shanghang and Peng, Jieqi and Zhang, Shuai and Li, Jianxin and Xiong, Hui and Zhang, Wancai},
  booktitle={Proceedings of the AAAI Conference on Artificial Intelligence},
  volume={35},
  number={12},
  pages={11106--11115},
  year={2021}
}
```

## 🔗 Key References & Citation Graph
- Vault papers: [[2017_Attention_Is_All_You_Need]] (vanilla Transformer base), [[2021_Autoformer_Decomposition_Transformers_AutoCorrelation]] (successor using ETT benchmark + Informer baseline), [[1997_Long_Short_Term_Memory]] (LSTM/LSTMa baseline), [[2020_DeepAR_Probabilistic_Forecasting]] (DeepAR baseline)
- Cited-in-text foundations: LogSparse Transformer / LogTrans (Li et al. 2019), Reformer LSH attention (Kitaev et al. 2019), Sparse Transformer (Child et al. 2019), Longformer (Beltagy et al. 2020), Linformer (Wang et al. 2020), Transformer-XL (Dai et al. 2019), Compressive Transformer (Rae et al. 2019), Prophet (Taylor & Letham 2018), ARIMA (Ariyo et al. 2014), LSTNet (Lai et al. 2018), dilated convolutions (Yu et al. 2017), kernel-smoother attention formulation (Tsai et al. 2019)
