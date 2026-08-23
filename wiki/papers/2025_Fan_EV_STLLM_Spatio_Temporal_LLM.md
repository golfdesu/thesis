---
type: paper
title: "EV-STLLM: Electric vehicle charging forecasting based on spatio-temporal large language models with multi-frequency and multi-scale information fusion"
authors: [Hang Fan, Yunze Chai, Chenxi Liu, Weican Liu, Zuhan Zhang, Wencai Run, Dunnan Liu]
year: 2025
journal_conference: "arXiv preprint (arXiv:2507.09527), preprint submitted to Elsevier"
doi_url: "https://doi.org/10.48550/arXiv.2507.09527"
models_used: ["[[EV-STLLM]]", "[[GPT-2]]", "[[PFGA]]", "[[QLoRA]]", "[[VMD]]", "[[ICEEMDAN]]", "[[FIG]]", "[[ReliefF]]", "[[GCN]]", "[[LSTM]]"]
datasets_used: ["[[UrbanEV_Dataset]]", "[[Shenzhen_EV_Charging_Dataset]]"]
features_used: ["[[Charging_Volume]]", "[[Station_Occupancy]]", "[[Holiday_Indicator]]", "[[Adjacency_Matrix]]", "[[Spatio_Temporal_Frequency_Embeddings]]", "[[Electricity_Price]]", "[[Weather]]"]
forecasting_horizon: "[[Short_Term]]"
metrics: ["[[RMSE]]", "[[MAE]]", "[[MAPE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: EV-STLLM: Electric vehicle charging forecasting based on spatio-temporal large language models with multi-frequency and multi-scale information fusion

## 🎯 Main Objective & Contribution
- Forecast EV **charging volume (kWh)** and **station occupancy rate (%)** across a spatial network of charging stations, capturing complex spatio-temporal dependencies and multi-frequency/multi-scale dynamics that small-parameter models cannot learn from large datasets.
- Contributions:
  - **EV-STLLM**: a two-module framework — (1) data preprocessing module fusing multi-frequency ([[VMD]]-[[ICEEMDAN]] + Multi-Scale Sample Entropy) and multi-scale ([[FIG]]) information with [[ReliefF]] feature selection; (2) a customized spatio-temporal LLM with the **Partially Frozen Graph Attention (PFGA)** module that injects station-network topology into a pre-trained LLM ([[GPT-2]] backbone) via adjacency-matrix attention masks, fine-tuned with [[QLoRA]] (4-bit NF4 quantization).
  - Customized **time-frequency domain fusion loss** combining time-domain [[MAE]] with an FFT-based frequency-domain term to suppress label autocorrelation issues in direct multi-step forecasting.
  - Validated on real-world Shenzhen data against traditional (GCN/LSTM/PAG) and LLM-based baselines ([[ChatEV]], GCNGPT, GATGPT, GPT4TS); strong few-shot and critical-day (Chinese Spring Festival) robustness.

## 🧠 Methodology & Model Architecture
- **Pipeline**: VMD denoising (drop highest-frequency IMF) → ICEEMDAN secondary decomposition of the most complex component (guided by MSSE) → recombine sub-components into high/mid/low-frequency series by MSSE similarity → FIG multi-scale granulation → ReliefF feature selection → Spatio-Temporal-Frequency Embedding layer → fusion convolution → PFGA LLM (F frozen + U graph-attention layers) → regression convolution → time-frequency loss.
- **Problem formulation** (Definition 3): given historical data $X_P \in \mathbb{R}^{P \times N \times C}$ and charging network $G=(V,E,A)$,
  $$ [x_{t-P+1}, x_{t-P+2}, \ldots, x_t, G] \xrightarrow[\theta]{f(\cdot)} [y_{t+1}, y_{t+2}, \ldots, y_{t+S}]. \tag{Eq. 1} $$
- **Key equations**:
  - **VMD constrained variational problem** (find modes $\{u_k\}$ and center frequencies $\{w_k\}$ reconstructing signal $f$):
    $$ \min_{\{u_k\},\{w_k\}} \left( \sum_{k=1}^{K} \left\| \partial_t \left[ \left( \delta(t) + \frac{j}{\pi t} \right) * u_k(t) \right] e^{-j w_k t} \right\|_2^2 \right), \quad \text{s.t.} \sum_{k=1}^{K} u_k = f, \tag{Eq. 2} $$
    solved via the **Augmented Lagrangian** (optimized by ADMM):
    $$ \mathcal{L}(\{u_k\},\{w_k\},\lambda) = \alpha \sum_{k=1}^{K} \left\| \partial_t [(\delta(t)+j/\pi t) * u_k(t)] e^{-j w_k t} \right\|_2^2 + \left\| f(t) - \sum_{k=1}^{K} u_k(t) \right\|_2^2 + \langle \lambda(t), f(t) - \textstyle\sum_{k=1}^{K} u(t) \rangle. \tag{Eq. 3} $$
  - **ICEEMDAN**: EMD on noise-assisted signal:
    $$ x_n(t) = \sum_{i=1}^{M_n} IMF_{i,n}(t) + r_{M_n,n}(t), \tag{Eq. 4} $$
    reconstruction over $N$ noise iterations:
    $$ x(t) = \sum_{i=1}^{K} \left( \frac{1}{N} \sum_{n=1}^{N} IMF_{i,n}(t) \right) + r_K(t). \tag{Eq. 5} $$
  - **MSSE coarse-grained series** at scale factor $\tau$:
    $$ y_j^{(\tau)} = \frac{1}{\tau} \sum_{i=(j-1)\tau+1}^{j\tau} x_i, \quad j = 1,\ldots,\lfloor N/\tau \rfloor. \tag{Eq. 6} $$
  - **FIG triangular fuzzy membership function** (endpoints $a,b$, peak $m$):
    $$ A(x,a,m,b) = \begin{cases} 0, & x < a \\ \frac{x-a}{m-a}, & a \le x \le m \\ \frac{b-x}{b-m}, & m < x \le b \\ 0, & x > b \end{cases}. \tag{Eq. 7} $$
  - **ReliefF weight update** for feature $A$ ($R$: random instance, $H_j$: same-class nearest neighbor/"hit", $M_j^{(C)}$: different-class neighbor/"miss"):
    $$ W(A) = W(A) - \sum_{j=1}^{k} \frac{\text{diff}(A,R,H_j)}{m_k} + \sum_{C \neq \text{class}(R)} \left[ \frac{P(C)}{1-P(\text{class}(R))} \sum_{j=1}^{k} \frac{\text{diff}(A,R,M_j^{(C)})}{m_k} \right], \tag{Eq. 8} $$
    with difference function
    $$ \text{diff}(A,R_1,R_2) = \begin{cases} \frac{|R_1[A]-R_2[A]|}{\max(A)-\min(A)}, & A \text{ continuous} \\ 0, & A \text{ discrete}, R_1[A]=R_2[A] \\ 1, & A \text{ discrete}, R_1[A] \ne R_2[A] \end{cases}. \tag{Eq. 9} $$
  - **Embeddings**: token $E_P = \text{PConv}(X_P;\theta_p)$ (1×1 convolution, Eq. 10); temporal $E_T^d = W_d(X_{day})$, $E_T^w = W_w(X_{week})$, $E_T = E_T^d + E_T^w$ (Eqs. 11–13); spatial $E_S = \sigma(W_S \cdot X_P + b_S)$ (Eq. 14); fusion $H_F = \text{FConv}(E_P \| E_S \| E_T;\theta_f) \in \mathbb{R}^{N \times 3D}$ (Eq. 15).
  - **PFGA frozen layers** ($i = 1..F-1$, preserving pre-trained knowledge):
    $$ \bar{H}^i = \text{MHA}(\text{LN}(H^i)) + H^i, \qquad H^{i+1} = \text{FFN}(\text{LN}(\bar{H}^i)) + \bar{H}^i, \tag{Eq. 16} $$
    where
    $$ \text{LN}(H^i) = \gamma \odot \frac{H^i - \mu}{\sigma} + \beta, \quad \text{MHA}(\tilde{H}^i) = W^O(head_1 \| \cdots \| head_h), $$
    $$ head_i = \text{Attention}(W_i^Q \tilde{H}^i, W_i^K \tilde{H}^i, W_i^V \tilde{H}^i), \quad \text{Attention}(\tilde{H}^i) = \text{softmax}\!\left( \frac{\tilde{H}^i \tilde{H}^{iT}}{\sqrt{d_k}} \right)\tilde{H}^i, \quad \text{FFN}(\hat{H}^i) = \max(0, W_1 \hat{H}^P_i + b_1) W_2 + b_2. \tag{Eq. 17} $$
  - **PFGA unfrozen (graph attention) layers** — adjacency matrix $A$ used as attention mask restricting attention to temporal predecessors and spatial neighbors:
    $$ \bar{H}^{F+U-1} = \text{MHA}(\text{LN}(H^{F+U-1}), A) + H^{F+U-1}, \qquad H^{F+U} = \text{FFN}(\text{LN}(\bar{H}^{F+U-1})) + \bar{H}^{F+U-1}. \tag{Eq. 18} $$
  - **QLoRA low-rank adaptation** ($r \ll d_k$):
    $$ \Delta W_i^Q = L_i^Q M_i^Q, \qquad \Delta W_i^V = L_i^V M_i^V, \tag{Eq. 19} $$
    effective weights via 4-bit→BFloat16 dequantization $d_Q(\cdot)$:
    $$ W_{i,Q}' = d_Q(W_{i,\text{quant}}^Q) + \Delta W_i^Q, \qquad W_{i,V}' = d_Q(W_{i,\text{quant}}^V) + \Delta W_i^V, \tag{Eq. 20} $$
    adapted attention heads:
    $$ head_i^{qlora} = \text{Attention}(W_i^{Q'} \tilde{H}^i,\; d_Q(W_{i,\text{quant}}^K)\tilde{H}^i,\; W_i^{V'} \tilde{H}^i). \tag{Eq. 21} $$
  - **Time-domain loss** ([[MAE]]):
    $$ MAELoss = \frac{1}{m}\sum_{i=1}^{m} |\hat{Y}_i - Y_i|. \tag{Eq. 22} $$
  - **Discrete Fourier transform**:
    $$ x_k^{(F)} = \sum_{t=0}^{T-1} x_t \exp(-j(2\pi/T)kt), \quad 0 \le k \le T-1. \tag{Eq. 23} $$
  - **Frequency-domain loss** (FFT spectra difference):
    $$ FrequencyLoss = \frac{1}{m}\sum_{i=1}^{m} \left| \mathcal{F}(\hat{Y}_i) - \mathcal{F}(Y_i) \right|. \tag{Eq. 24} $$
  - **Customized Time-Frequency Fusion Loss**:
    $$ CustomizedLoss = MAELoss + \lambda \cdot FrequencyLoss, \tag{Eq. 25} $$
    with tunable weight $\lambda$.
  - Metrics: $MAE = \frac{1}{n}\sum|\hat{f}_{mi}-f_{mi}|$ (Eq. 26), $RMSE = \sqrt{\frac{1}{n}\sum(\hat{f}_{mi}-f_{mi})^2}$ (Eq. 27), $MAPE = \frac{1}{n}\sum|\frac{f_{mi}-\hat{f}_{mi}}{f_{mi}}| \times 100\%$ (Eq. 28).
- **Training setup**: look-back window 12, target length {1, 3, 6, 9}, hidden dimension 768, learning rate 0.01, **Ranger21** optimizer, batch size 64, max 300 epochs; VMD: $\alpha$=100, $\tau$=0, N=8 decomposition layers, Tol 1e−7; ICEEMDAN: ensemble number 100, noise amplitude 0.2; FIG (FCM): c=5 granules, fuzziness m=2; ReliefF: K=70 neighbors, Euclidean distance. Hardware: Intel i7-9700, 16 GB RAM, NVIDIA RTX 3090; MATLAB 2022a preprocessing, PyTorch implementation.

## 📊 Dataset & Input Features
- **Dataset**: public EV charging records from **Shenzhen, China** (source: [[UrbanEV_Dataset]] benchmark, ref. [28], DOI: https://doi.org/10.1038/s41597-025-04874-4). Raw data: **1,682 public charging stations (24,798 piles)**, September 2022 – February 2023, **5-minute resolution**. Refined version used here: aggregated to **1-hour intervals**, curated set of **1,362 stations with 17,532 piles**.
  - Targets: charging volume and occupancy per station. Additional dynamic factors: time-varying electricity price, service price, weather conditions. Spatial attributes: coordinates, adjacency, distances; static features: pile number, station number.
  - Experiment subsets: two randomly selected zones (**Data 1** and **Data 2**), each 4,345 hourly data points, split 80%/10%/10% train/valid/test. Data 1 volume mean 198.02 kWh (std 98.78); Data 2 volume mean 528.99 (std 225.88).
  - Critical-day experiment: training to Jan 16 2023, validation Jan 17–21, test on five Chinese Spring Festival holiday days (2023-01-22–26) plus subsequent workdays.
- **Features**: [[Historical_Charging_Volume]], [[Station_Occupancy]], binary [[Holiday_Indicator]] (holiday=1, ordinary day=0, selected via ReliefF), hour-of-day/day-of-week temporal features, high/mid/low-frequency components from VMD-ICEEMDAN, multi-scale (daily/weekly) FIG granules, station adjacency matrix from network topology.
- No dedicated code/data repository URL stated in the paper beyond the UrbanEV dataset citation above.

## 📈 Performance & Results
- **Main comparison (Table 5)**:
  - Data 1, 3-step volume: EV-STLLM **RMSE 26.42 / MAPE 0.14 / MAE 19.49** — 44.26% RMSE reduction vs GCN (47.40), 40.81% MAE improvement vs ChatEV (32.93), beats GPT4TS (29.27/0.16/21.85).
  - Data 1, 6-step volume: RMSE 27.78 — 53.12% lower than GATGPT (59.26).
  - Data 2, 3-step volume: RMSE 58.89 / MAPE 0.09 / MAE 42.85 — 51.56% RMSE cut vs GCN (120.95), 46.30% MAE cut vs GCNGPT (79.80), 46.23% RMSE cut vs ChatEV (109.53), 9.75% RMSE cut vs GPT4TS (65.25), 50% MAPE cut vs both (0.18→0.09, 0.12→0.09).
  - Occupancy: consistently best, e.g. Data 1 3-step RMSE 0.04/MAE 0.03.
- **Ablation (3-step)**: every component matters; largest degradation from removing the **customized loss** (Data 2 volume RMSE 60.36→63.55, MAE 46.76→49.93); removing VMD-ICEEMDAN multi-frequency extraction raised Data 1 MAE 21.96→22.58; removing FIG, partial freezing, or graph attention also degraded results (e.g., Data 1 RMSE 27.78→28.33 without graph attention); Full Tuning and Full Graph Attention underperform the partial strategy.
- **Few-shot (1-step)**: Data 2 volume MAE 37.51 — 45.24% better than GPT4TS (68.51) and **62.15% better than ChatEV** (99.10); Data 1 volume MAE 17.35, 59.89% lower than GCN (43.25); Data 2 RMSE 47.92 vs LSTM 98.82 (51.50% lower).
- **Critical days (Spring Festival, 1-step)**: Data 1 volume MAE 8.49 — 37.97% better than next-best PAG (13.69) and 56.02% better than GPT4TS (19.30); Data 2 volume MAE 20.81 — 26.83% better than PAG (28.44), 48.19% better than GPT4TS (40.15).

## 💡 Limitations & Identified Research Gaps
- Framework is heavy (LLM-based); authors propose **knowledge distillation** to build lighter-weight models suitable for localized deployment at individual stations.
- Predictions not yet coupled to downstream action — future work should integrate forecasts with scheduling strategies for electricity-market transactions of charging stations/EV aggregators.
- Only two randomly selected zones evaluated; generalization across many zones/cities untested. Prompt-free topology injection relies on proximity-based adjacency only (no semantic/road-network graphs).

## 📚 BibTeX & Citation Reference
```bibtex
@article{fan2025evstllm,
  title   = {EV-STLLM: Electric vehicle charging forecasting based on spatio-temporal large language models with multi-frequency and multi-scale information fusion},
  author  = {Fan, Hang and Chai, Yunze and Liu, Chenxi and Liu, Weican and Zhang, Zuhan and Run, Wencai and Liu, Dunnan},
  journal = {arXiv preprint arXiv:2507.09527},
  year    = {2025},
  doi     = {10.48550/arXiv.2507.09527}
}
```

## 🔗 Key References & Citation Graph
- [[2024_A_Physics_Informed_and_Attention_Based_Graph_Learning_Approach_for_Regional_Electric_Vehicle_Charging_Demand_Prediction]] — PAG baseline (ref. [27])
- ChatEV (Qu et al., 2024, Transp. Res. Part D, doi:10.1016/j.trd.2024.104470) — LLM-based EV demand prediction baseline (ref. [31])
- UrbanEV open benchmark (Li et al., 2025, Scientific Data, doi:10.1038/s41597-025-04874-4) — source dataset (ref. [28])
- ST-LLM / ST-LLM+ (Liu et al., 2024 MDM; 2025 TKDE) — spatio-temporal LLM foundation (refs. [29], [32])
- GPT4TS / One-Fits-All (Zhou et al., NeurIPS 2023) — pretrained-LM time-series baseline (ref. [42])
- [[2023_Cheng_VMD_Prophet_LSTM]] — related VMD+LSTM federated EV load forecasting line (ref. [25])
