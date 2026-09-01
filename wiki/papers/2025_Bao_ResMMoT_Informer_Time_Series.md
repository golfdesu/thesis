---
type: paper
title: "Long Short-Term Financial Time Series Forecasting Based on Residual Multiscale TCN Sparse Expert Network and Informer"
authors: [Wuzhida Bao, Yuting Cao, Yin Yang, Shiping Wen]
year: 2025
journal_conference: "IEEE Transactions on Neural Networks and Learning Systems, vol. 36, no. 10, pp. 19200-19209"
doi_url: "https://doi.org/10.1109/TNNLS.2025.3584369"
models_used: ["[[ResMMoT_Informer]]", "[[Sparse_Mixture_of_Experts]]", "[[TCN]]", "[[Informer]]", "[[LSTM]]"]
datasets_used: ["[[NASDAQ100_Stock_Price_Dataset]]", "[[Cryptocurrency_Dataset]]", "[[Forex_Dataset]]"]
features_used: ["[[Wavelet_Decomposition]]", "[[TCN]]", "[[Top_K_Gating_Routing]]", "[[Positional_Encoding]]", "[[Cyclical_Encodings]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[R_squared]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Long Short-Term Financial Time Series Forecasting Based on Residual Multiscale TCN Sparse Expert Network and Informer

## 🎯 Main Objective & Contribution
- Address the gap that most stock-forecasting models handle only short-term horizons and fail to capture long-term trends, global dependencies, multiscale features, and noise robustness in highly volatile financial series.
- Contributions:
  - **ResMMoT-Informer**: couples a **residual multiscale TCN sparse expert network (ResMMoT)** — capturing multiscale local features + long-term dependencies — with an **[[Informer]]** module for global dependencies via [[ProbSparse_Attention]].
  - **Structurally heterogeneous TCN experts** with **Top-K sparse activation routing**, dynamically selecting/fusing features across temporal scales (unlike conventional TCNs and static expert networks).
  - **Wavelet Noise Reduction (WNR)** as a data-augmentation strategy: both denoised (smooth) and raw data are fed to the network.
  - State-of-the-art results on NASDAQ100 at horizons of 1/5/10/20 steps; ~30–40% average improvement in RMSE/MAE/R² over baselines including iTransformer, PatchTST, N-HiTS.

## 🧠 Methodology & Model Architecture
- **Framework pipeline**: raw prices → WNR preprocessing → min–max normalization → sliding windows (**input length = 3× forecast horizon**) → Informer-style embedding (temporal feature encoding + positional encoding + value/numerical encoding) → ResMMoT module → Informer module (encoder–decoder) → **Forecasting Head** (stacked 1D-CNN + LSTM layers refining/dimension-reducing high-level features) → fully connected output.
- **Key Equations**:
  - **Eq. (1) — Min–max normalization**:
    $$ X_{scaled} = \frac{X - X_{min}}{X_{max} - X_{min}} $$
  - **Eq. (2) — ResNet residual connection** ($\mathcal{F}(x,\{W_i\})$: residual mapping; skip input $x$):
    $$ y = \mathcal{F}(x, \{W_i\}) + x $$
    In ResMMoT, the residual branch is a 1×1 1D-CNN used only for dimension alignment so its features can be concatenated with MMoT outputs.
  - **Eq. (3) — Mixture of Experts** (dense gating; $g_i(x)$ gate weight, $f_i(x)$ expert output, $N$ experts):
    $$ y = \sum_{i=1}^{N} g_i(x)\cdot f_i(x) $$
  - **Eq. (4) — Sparse MoE** (Top-K selection; only experts in set $S$ activated, weights redistributed to sum to 1):
    $$ y = \sum_{i \in S} g_i(x)\cdot f_i(x), \qquad S = \text{TopK}(\text{Softmax}(W_g x), K),\ K=2 $$
  - **WNR — Wavelet denoising**: DWT with Daubechies-4 (db4) wavelet decomposes the signal into low-frequency trend and high-frequency noise components; a VisuShrink threshold suppresses high-frequency coefficients via soft thresholding, then inverse DWT reconstructs a smoothed series:
    $$ X_{denoised} = \text{IDWT}\left(\text{SoftThreshold}(\text{DWT}(X),\ \tau)\right) $$
  - **Eq. (5) — ProbSparse self-attention** (only top-$N$ dominant queries computed via sparse query matrix $\bar{Q}$; complexity reduced from $\mathcal{O}(L^2)$ to $\mathcal{O}(N \cdot L)$ with $N = \mathcal{O}(L\log L)$, i.e., overall $\mathcal{O}(L\log L)$):
    $$ \mathcal{A}(Q,K,V) = \text{Softmax}\!\left(\frac{\bar{Q}K^\top}{\sqrt{d}}\right)V $$
  - **Eq. (6) — Self-Attention Distilling** ([·]$_{AB}$: multi-head ProbSparse attention block; Conv1d kernel size 3; ELU activation; MaxPool stride 2 halves sequence length per layer):
    $$ X_{j+1}^t = \text{MaxPool}\left(\text{ELU}\left(\text{Conv1d}\left([X_j^t]_{AB}\right)\right)\right) $$
  - **Metrics Eqs. (7)–(9)**:
    $$ RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^n (y_i-\hat{y}_i)^2}, \quad MAE = \frac{1}{n}\sum_{i=1}^n |y_i-\hat{y}_i|, \quad R^2 = 1-\frac{\sum_{i=1}^n(y_i-\hat{y}_i)^2}{\sum_{i=1}^n(y_i-\bar{y})^2} $$

## 📊 Dataset & Input Features
- **Dataset**: [[NASDAQ100_Stock_Price_Dataset]] from Kaggle (ref. [33]): daily stock prices of **102 largest non-financial companies by market capitalization** on Nasdaq; accessed Sep. 14, 2024.
  - URL: https://www.kaggle.com/datasets/kalilurrahman/nasdaq100-stock-price-data
- **Cross-market validation datasets** (Appendix H): cryptocurrency and foreign exchange datasets (details in supplementary material available via https://doi.org/10.1109/TNNLS.2025.3584369).
- **Features**: historical price series (closing prices); WNR db4-denoised variant fed alongside raw series as augmentation; min–max scaled to [0,1]; sliding-window inputs with lookback = 3× prediction horizon (steps ahead: 1, 5, 10, 20). Qualitative evaluation on VRTX, MSFT, CTAS, INTC across four industries.
- Supplementary downloadable material available at https://doi.org/10.1109/TNNLS.2025.3584369 (Appendices A–H: WNR details, TCN details, implementation details, full figures, Top-K ablation, cross-market results).

## 📈 Performance & Results
- **Main benchmark (Table I, NASDAQ100)**:
  | Model | 1-step MAE / RMSE / R² | 20-step MAE / RMSE / R² |
  |---|---|---|
  | **ResMMoT-Informer** | **2.6791 / 4.0161 / 0.9682** | **4.7171 / 7.2784 / 0.9605** |
  | iTransformer | 2.9982 / 4.7850 / 0.9671 | 5.3984 / 7.7469 / 0.9580 |
  | PatchTST | 3.0405 / 4.5001 / 0.9669 | 5.0683 / 7.5132 / 0.9586 |
  | N-HiTS | 3.0462 / 4.5331 / 0.9660 | 6.5983 / 8.6225 / 0.9563 |
  | Informer | 3.9495 / 5.0960 / 0.9645 | 6.7540 / 8.9097 / 0.9548 |
  | TCN | 4.0512 / 5.2644 / 0.9637 | 8.0328 / 9.6716 / 0.9507 |
  | BiLSTM | 4.2586 / 6.0302 / 0.9639 | 8.8778 / 12.2709 / 0.9399 |
  | CNN-LSTM | 5.2141 / 6.9520 / 0.9615 | 8.5757 / 12.0488 / 0.9411 |
  - Best at all horizons (1, 5, 10, 20 steps); R² > 96% everywhere; ~30–40% average improvement in RMSE/MAE/R² vs other models.
- **Ablation (Table II)**: TCN < Informer < TCN-Informer < ResMMoT-Informer; replacing plain TCN with ResMMoT improves accuracy further; WNR preprocessing positively impacts accuracy. Top-K routing ablation: **K = 2 gives the best accuracy/compute trade-off (highest energy efficiency)**.
- **Qualitative**: accurate forecasts even under high volatility across four sectors (biopharma, technology, business services, semiconductors); Transformer baseline underperforms on noisy financial data; PatchTST weak at long-term dependencies; iTransformer less stable under noise/volatility.

## 💡 Limitations & Identified Research Gaps
- The multi-expert structure of ResMMoT introduces **parameter redundancy** — future work targets parameter sharing and module compression for lighter deployment.
- Currently univariate price-based; authors plan to add multimodal exogenous context (macroeconomic indicators, social-media sentiment).
- Financial-domain validation only; no energy/EV experiments (transferable architecture for volatile multi-resolution load/price forecasting remains untested).
- Sliding-window design ties input length to horizon (3× rule), not evaluated against fixed-window alternatives.

## 📚 BibTeX & Citation Reference
```bibtex
@article{bao2025resmmot,
  title   = {Long Short-Term Financial Time Series Forecasting Based on Residual Multiscale TCN Sparse Expert Network and Informer},
  author  = {Bao, Wuzhida and Cao, Yuting and Yang, Yin and Wen, Shiping},
  journal = {IEEE Transactions on Neural Networks and Learning Systems},
  volume  = {36},
  number  = {10},
  pages   = {19200--19209},
  year    = {2025},
  doi     = {10.1109/TNNLS.2025.3584369}
}
```

## 🔗 Key References & Citation Graph
- [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] — Zhou et al., Informer / ProbSparse attention / distilling (ref. [26])
- [[2018_Bai_Empirical_TCN_Sequence_Modeling]] — Bai et al., TCN architecture used as experts (ref. [24])
- [[2023_Zhang_Crossformer_Cross_Dimension_Dependency]] / related Transformer line — Vaswani et al., Attention Is All You Need (ref. [17], cf. [[2017_Attention_Is_All_You_Need]])
- [[2023_Challu_NHiTS_Neural_Hierarchical_Interpolation]] — N-HiTS baseline (ref. [40])
- [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]] — PatchTST baseline (ref. [41])
- [[2024_Liu_iTransformer_Inverted_Transformers_Effective_Time_Series]] — iTransformer baseline (ref. [42])
- He et al., Deep Residual Learning (ResNet), CVPR 2016 — residual structure (ref. [21])
- Jacobs et al., Adaptive Mixtures of Local Experts, Neural Comput. 1991 — original MoE (ref. [30]); Fedus et al., Sparse expert models review (ref. [38])
- Kaggle NASDAQ100 dataset — https://www.kaggle.com/datasets/kalilurrahman/nasdaq100-stock-price-data (ref. [33])

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2025_Bao_ResMMoT_Informer_Time_Series_refs]]
