---
type: paper
title: "Forwardformer: Efficient Transformer With Multi-Scale Forward Self-Attention for Day-Ahead Load Forecasting"
authors: [Kai Qu, Gangquan Si, Zihan Shan, Qianyue Wang, Xiaoliang Liu, Chen Yang]
year: 2024
journal_conference: "IEEE Transactions on Power Systems, Vol. 39, No. 1, pp. 1421-1433, January 2024"
doi_url: "https://doi.org/10.1109/TPWRS.2023.3266369"
models_used: ["[[2024_Qu_Forwardformer_Day_Ahead_Load]]", "[[Transformer]]", "[[Autoformer]]", "[[FEDformer]]", "[[Informer]]", "[[LogTrans]]", "[[LSTMa]]", "[[Prophet]]", "[[SARIMA]]"]
datasets_used: ["[[CEL_NW_China_Electric_Load]]", "[[CEL_SE_China_Electric_Load]]", "[[AEL_CNYS_America_Electric_Load]]", "[[AEL_NNYS_America_Electric_Load]]", "[[AEL_WNYS_America_Electric_Load]]"]
features_used: ["[[Historical_Load]]", "[[Calendar_Features]]", "[[Holiday_Flag]]", "[[Temperature]]", "[[Humidity]]", "[[Rainfall]]", "[[Pressure]]", "[[Temperature]]"]
forecasting_horizon: "[[Day_Ahead_Forecasting]]"
metrics: ["[[MSE]]", "[[MAE]]", "[[Accuracy]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Forwardformer: Efficient Transformer With Multi-Scale Forward Self-Attention for Day-Ahead Load Forecasting

## 🎯 Main Objective & Contribution
Design a Transformer purpose-built for **day-ahead load forecasting (DALF)** that (i) removes sequential computation and captures long-term dependence between distant special days, and (ii) explicitly targets the under-served problem of forecasting **special days (weekends and holidays)**. Contributions:
1. A **correction structure based on an encoder-dual decoder** improving DALF accuracy.
2. **Multi-scale forward self-attention (MSFSA)** — attention computed only between a token and its *forward* tokens with three patterns (forward sliding window, forward dilated sliding window, forward global sliding window) — capturing local + global dependencies while scaling complexity down to $O(lw/n)$.
3. Input representation injecting timestamps and information embeddings; the whole day-ahead curve is obtained in **one inference** (no error accumulation).
4. State-of-the-art accuracy on special days (weekends, holidays), validated on datasets from China and America.

## 🧠 Methodology & Model Architecture
**Input representation:** one day of load = one token ("token definition equation"):

$$\begin{bmatrix}\text{token}_1\\ \text{token}_2\\ \vdots\\ \text{token}_l\end{bmatrix} = \begin{pmatrix}P_1\\ P_2\\ \vdots\\ P_l\end{pmatrix} = \begin{pmatrix}p_1^1 & p_2^1 & \cdots & p_n^1\\ p_1^2 & p_2^2 & \cdots & p_n^2\\ \vdots & \vdots & & \vdots\\ p_1^l & p_2^l & \cdots & p_n^l\end{pmatrix} \tag{1}$$

($l$ = input sequence length in days, $n$ = sampling points per day). The i-th input vector sums three embeddings ("input embedding equation"):

$$X_{\text{feed}}[i] = VE(P_i) + \sum_{j=1}^{NTE}\big[TE(P_i)\big]_j + \sum_{k=1}^{NIE}\big[IE(P_i)\big]_k \tag{2}$$

- VE = value embedding via 1D convolution (kernel width 5, stride 1);
- TE = timestamp embeddings (Day/Week/Month; positional sine-cosine encodings);
- IE = information embeddings (Holiday, Temperature, Pressure, Humidity) via separate linear layers.

**Encoder-dual-decoder architecture:** Encoder ($N=4$ layers) with multi-head MSFSA sublayer + FFN sublayer:

$$\text{FFN}(x) = \text{ReLU}(w_1 x + b_1)\, w_2 + b_2 \tag{3}$$

Each sublayer wrapped with residual connection, layer norm, dropout ($p=0.1$):

$$y = \text{Dropout}\big(\text{LayerNorm}(x + \text{Sublayer}(x))\big) \tag{4}$$

Decoder-1 = simple fully connected layer producing the initial prediction; Decoder-2 ($M=2$ standard Transformer decoding layers with an inserted cross-attention sublayer over the encoder output) takes initial prediction + additional information (holiday/weather of predicted day) and outputs the corrected final prediction.

**Multi-head attention with mixed patterns** ("multi-head combination"):

$$\text{MultiHead} = \text{Concat}\big(\text{head}_s,\; \text{head}_d,\; \dots,\; \text{head}_g\big)^h \cdot W^O \tag{5}$$

each head being scaled dot-product attention ("scaled dot-product attention"):

$$\text{head}_i = A\Big(QW_i^Q,\; KW_i^K,\; VW_i^V\Big) = \text{Softmax}\!\left(\frac{QW_i^Q \cdot (KW_i^K)^T}{\sqrt{d_k}}\right)\cdot VW_i^V \tag{6}$$

**MSFSA patterns:** (1) *forward sliding window* — attention only to the current token's forward $w$ tokens, complexity/memory $O(lw/n)$, top-layer receptive field $N\times w$; (2) *forward dilated sliding window* (gap parameter $d$, receptive field $N\times d\times w$) — targets fixed-distance dependencies such as consecutive weekends; (3) *forward global sliding window* on holiday tokens only — relates rare holidays to past holidays at unfixed long distances, negligible cost. Head split at $h=16$: 8 sliding-window + 4 dilated + 4 global heads.

**Holiday-aware loss function** ("dual MSE loss"):

$$L_{total} = \frac{1}{N_\alpha}\sum_{j\in\alpha}(\hat{x}_i - x_i)^2 + \frac{1}{N_\beta}\sum_{j\in\beta}(\hat{x}_j - x_j)^2 \tag{8}$$

where $\alpha$ = all days, $\beta$ = holidays; converges faster and more accurately than plain MSELoss (Appendix B).

Hyperparameters: $d_{model}=512$, $N=4$, $M=2$, $w=20$, $d=7$ (weekly periodicity), $h=16$, Adam lr $10^{-4}$, batch size 128; PyTorch on PC with 3.0 GHz 12-core CPU + 4 NVIDIA TITAN GPUs (48 GB). MSFSA implemented with a CUDA kernel via TVM.

## 📊 Dataset & Input Features
5 datasets from China and America (**no public download URLs given in the text**):
- **China Electric Load (CEL)**: CEL-NW (Northwest district) and CEL-SE (Southeast district); wide-area, smooth curves (low high-frequency components); duration **5 years, 2016-01-01 to 2020-12-31**, hourly sampling → 24 load points/day; **5 weather features**: max/min/average temperature, relative humidity, rainfall; train/validation/test = **36/12/12 months**.
- **America Electric Load (AEL)**: AEL-CNYS (Capital of New York State), AEL-NNYS (North of New York State), AEL-WNYS (West of New York State); small-area, unsmooth curves (high high-frequency components); duration **4 years, 2016-01-01 to 2019-12-31**, 5-minute sampling → 288 load points/day; **4 weather features**: max/min temperature, max/min wet-bulb temperature; train/validation/test = **30/6/12 months**.
- Calendar features injected as timestamp embeddings (Day/Week/Month) and holiday flags as information embeddings; Chinese holidays covered: New Year's Day, Spring Festival, Tomb-sweeping Day, Labour Day, Dragon Boat Festival, Mid-autumn Festival, National Day.

## 📈 Performance & Results
Metrics ("MSE / MAE / ACC definitions"; MSE/MAE computed on zero-mean-normalized values $y_i^*=(y_i-\mu)/\sigma$, ACC on original magnitudes):

$$\begin{cases}
\text{MSE} = \frac{1}{n}\sum_{i=1}^{n}(y_i^* - \hat{y}_i^*)^2\\[4pt]
\text{MAE} = \frac{1}{n}\sum_{i=1}^{n}|y_i^* - \hat{y}_i^*|\\[4pt]
\text{ACC} = \frac{1}{n}\sum_{i=1}^{n}\left[1 - |(y_i - \hat{y}_i)/y_i|\right]
\end{cases} \tag{7}$$

Baselines: Autoformer, PEDformer (= FEDformer), Informer, LogTrans, LSTMa, Prophet, SARIMA $(1,0,1)\times(1,0,1)_S$.
Key results:
- Overall best ACC across all methods: **Forwardformer 98.51% (China) and 96.94% (America)**; smallest errors in most cases (full per-dataset Table I values **not extractable** from text).
- Best baseline: PED/FEDformer with ACC **97.71% / 95.87%**, second to Forwardformer everywhere.
- LSTMa beats Informer and LogTrans in most cases but needs tens of times longer computation; SARIMA surprisingly outperforms Informer and LogTrans in accuracy.
- Informer/LogTrans/LSTMa/Prophet/SARIMA degrade sharply on the three high-frequency AEL datasets; Forwardformer and PEDformer stay stable.
- **Non-workdays**: Forwardformer achieves smallest MAE on CEL and AEL (**0.112 and 0.138**) and highest ACC (**96.59% and 95.08%**) (Fig. 7); baselines' accuracy fluctuates strongly across countries' different holiday calendars. Per-holiday Table II shows all models are worst on Chinese Spring Festival (long duration, non-fixed date) and Christmas (US), where Forwardformer leads substantially.
- Parameter study on CEL-NW: increasing $w$ helps until saturation ($w=20$ chosen, no gain at 25); $d=7$ minimizes MSE/MAE (weekly periodicity); $h=16$ best (too many heads reduce accuracy).
- Mutual-information analysis (Eq. 9: $I(X;Y)=H(X)-H(X|Y)$) confirms strong interval correlation between same-weekday tokens (supports dilation $d=7$) and weak correlation of holiday tokens (supports global attention).
- Ablation (Table IV): model **with MSFSA is more accurate and faster** than without (exact values **not extractable**). Correction structure: final (corrected) predictions consistently more accurate than Decoder-1 initial predictions (Fig. 10).
- Efficiency (Table V): per-layer complexity reduced to **O(lw/n)**, optimal inference steps and lowest runtime per core layer vs all baselines (competitors several times slower).

## 💡 Limitations & Identified Research Gaps
- Hyperparameters chosen by grid search balancing accuracy vs runtime, not guaranteed globally optimal (e.g., N=6 might be slightly more accurate than N=4 but too slow).
- MSFSA efficiency relies on a custom CUDA/TVM kernel requiring low-level GPU programming knowledge.
- Future work stated by authors: day-ahead **load peak forecasting under special events**; transferring MSFSA to wind power and photovoltaic forecasting with targeted improvements.
- Point forecasts only — no probabilistic/uncertainty quantification.
- Datasets not released via public links in the paper (reproducibility gap).

## 📚 BibTeX & Citation Reference
```bibtex
@article{Qu2024Forwardformer,
  author  = {Qu, Kai and Si, Gangquan and Shan, Zihan and Wang, Qianyue and Liu, Xiaoliang and Yang, Chen},
  title   = {Forwardformer: Efficient Transformer With Multi-Scale Forward Self-Attention for Day-Ahead Load Forecasting},
  journal = {IEEE Transactions on Power Systems},
  year    = {2024},
  volume  = {39},
  number  = {1},
  pages   = {1421--1433},
  month   = jan,
  doi     = {10.1109/TPWRS.2023.3266369}
}
```

## 🔗 Key References & Citation Graph
- [[2017_Attention_Is_All_You_Need]] [7] — base Transformer architecture.
- Beltagy2020_Longformer [26] — source of sliding-window/dilated/global attention patterns reused by MSFSA.
- [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]] [27], [[FEDformer]] [28], [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] [29], [[2019_Li_LogSparse_Enhancing_Locality_Transformer]] [37] — Transformer baselines compared experimentally.
- [[Prophet]] [12] and Bahdanau2016_LSTMa_Attention [6] — classical/deep baselines.
- [[2026_MoghadamDost_TFT_Conformal_Environmental_EV_Load]] — related line of attention-based (Temporal Fusion Transformer) day-ahead EV/load forecasting with environmental covariates; complementary since Forwardformer is point-only whereas TFT work adds conformal uncertainty.
- [[Day_Ahead_Forecasting]] — the target horizon; one inference produces the full next-day profile.
