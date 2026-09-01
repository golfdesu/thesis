---
type: paper
title: "Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting"
authors: [Haixu Wu, Jiehui Xu, Jianmin Wang, Mingsheng Long]
year: 2021
journal_conference: "NeurIPS 2021 (35th Conference on Neural Information Processing Systems)"
doi_url: "https://arxiv.org/abs/2106.13008"
models_used: ["[[Autoformer]]", "[[Auto_Correlation|Auto-Correlation Mechanism]]", "[[Series_Decomposition_Block]]", "[[Informer]]", "[[LogTrans]]", "[[Reformer]]", "[[LSTNet]]", "[[DeepAR]]", "[[NBEATS]]", "[[Prophet]]"]
datasets_used: ["[[ETT]]", "[[Electricity_ECL]]", "[[Exchange]]", "[[Traffic]]", "[[Weather]]", "[[ILI]]", "[[COVID19_Dashboard]]"]
features_used: ["[[Trend_Component|Trend-cyclical Component]]", "[[Seasonal_Component]]", "[[Autocorrelation_Time_Delay]]", "[[Moving_Average_Decomposition]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MSE]]", "[[MAE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting

## 🎯 Main Objective & Contribution
- **Core problem**: In long-term forecasting (input-I-predict-O with large O), intricate/entangled temporal patterns make point-wise dependency discovery unreliable, and quadratic-complexity self-attention is prohibitive; sparse point-wise attention variants ([[Informer]] ProbSparse, LogTrans LogSparse, Reformer LSH) sacrifice information utilization.
- **Primary contribution**: **[[Autoformer]]** — a decomposition architecture that (1) embeds a **series decomposition block as an inner operator** for *progressive* decomposition of intermediate hidden variables during forecasting (breaking the pre-processing convention of Prophet/N-BEATS/DeepGLO), and (2) an **[[Auto_Correlation|Auto-Correlation]] mechanism** based on series periodicity performing sub-series-level (series-wise) dependencies discovery and aggregation at $O(L \log L)$ complexity.
- Result: 38% average relative MSE improvement over previous SOTA across six benchmarks covering energy, traffic, economics, weather and disease.

## 🧠 Methodology & Model Architecture
- **Series decomposition block** (Eq. 1) — moving-average smoothing extracting trend-cyclical $X_t$ from length-$L$ input $X \in \mathbb{R}^{L\times d}$:
$$X_t = \text{AvgPool}(\text{Padding}(X)), \qquad X_s = X - X_t$$
summarized as $X_s, X_t = \text{SeriesDecomp}(X)$; adopted from classic decomposition but used as inner block throughout encoder/decoder.
- **Decoder input initialization** (Eq. 2): seasonal part initialized from latter half of encoder input + zero placeholders; trend part + mean placeholders:
$$X_{en}^s, X_{en}^t = \text{SeriesDecomp}(X_{\frac{I}{2}:I}), \quad X_{des} = \text{Concat}(X_{en}^s, X_0), \quad X_{det} = \text{Concat}(X_{en}^t, X_{Mean})$$
- **Encoder** (Eq. 3), $l$-th of $N$ layers — trend eliminated via decomposition after each sublayer, output keeps only seasonal component:
$$S_{en}^{l,1},\_ = \text{SeriesDecomp}\big(\text{Auto-Correlation}(X_{en}^{l-1}) + X_{en}^{l-1}\big); \qquad S_{en}^{l,2},\_ = \text{SeriesDecomp}\big(\text{FeedForward}(S_{en}^{l,1}) + S_{en}^{l,1}\big)$$
with $X_{en}^l = S_{en}^{l,2}$.
- **Decoder** (Eq. 4), $l$-th of $M$ layers — three decomposition blocks per layer plus trend accumulation with projectors $W^{l,i}$:
$$\begin{aligned} S_{de}^{l,1}, T_{de}^{l,1} &= \text{SeriesDecomp}(\text{Auto-Correlation}(X_{de}^{l-1}) + X_{de}^{l-1}) \\ S_{de}^{l,2}, T_{de}^{l,2} &= \text{SeriesDecomp}(\text{Auto-Correlation}(S_{de}^{l,1}, X_{en}^N) + S_{de}^{l,1}) \\ S_{de}^{l,3}, T_{de}^{l,3} &= \text{SeriesDecomp}(\text{FeedForward}(S_{de}^{l,2}) + S_{de}^{l,2}) \\ T_{de}^l &= T_{de}^{l-1} + W^{l,1}*T_{de}^{l,1} + W^{l,2}*T_{de}^{l,2} + W^{l,3}*T_{de}^{l,3} \end{aligned}$$
Final prediction: $W_S * X_{de}^M + T_{de}^M$ (seasonal projection + accumulated trend).
- **Period-based dependencies / stochastic process autocorrelation** (Eq. 5):
$$R_{XX}(\tau) = \lim_{L\to\infty}\frac{1}{L}\sum_{t=1}^{L} X_t X_{t-\tau}$$
$R_{XX}(\tau)$ reflects time-delay similarity between $\{X_t\}$ and its $\tau$-lag series; used as unnormalized confidence of estimated period length $\tau$.
- **Auto-Correlation mechanism** (Eq. 6) — top-$k$ period selection by autocorrelation, softmax-normalized time delay aggregation via Roll:
$$\begin{aligned} &\tau_1,\cdots,\tau_k = \arg\underset{\tau\in\{1,\cdots,\bar{L}\}}{\text{Topk}}\big(R_{Q,K}(\tau)\big) \\ &\hat{R}_{Q,K}(\tau_1),\cdots,\hat{R}_{Q,K}(\tau_k) = \text{SoftMax}\big(R_{Q,K}(\tau_1),\cdots,R_{Q,K}(\tau_k)\big) \\ &\text{Auto-Correlation}(Q,K,V) = \sum_{i=1}^{k} \text{Roll}(V, \tau_i)\ \hat{R}_{Q,K}(\tau_i) \end{aligned}$$
where $k = \lfloor c \times \log L\rfloor$ ($c \in [1,3]$ hyper-parameter), $\bar{L}=\{1,\cdots,L\}$, and Roll shifts elements circularly.
- **Multi-head version** (Eq. 7): $\text{MultiHead}(Q,K,V) = W_{output}*\text{Concat}(\text{head}_1,\cdots,\text{head}_h)$ where $\text{head}_i = \text{Auto-Correlation}(Q_i, K_i, V_i)$.
- **Efficient computation** (Eq. 8, Wiener–Khinchin theorem) — all lags computed at once via FFT:
$$S_{XX}(f) = F(X_t)F^*(X_t) = \int_{-\infty}^{\infty} X_t e^{-i2\pi tf}dt \int_{-\infty}^{\infty} X_t e^{-i2\pi tf}dt, \qquad R_{XX}(\tau) = F^{-1}(S_{XX}(f)) = \int_{-\infty}^{\infty} S_{XX}(f)e^{i2\pi f\tau}df$$
giving overall $O(L\log L)$ complexity in both memory and time (vs full attention $O(L^2)$).
- Implementation: $d_{model}=512$, 8 heads, $N=2$ encoder layers, $M=1$ decoder layer, moving-average kernel $k=25$; speedup batch-norm-style Auto-Correlation variant (batch-averaged lags during training); no position embedding (only value + timestamp embedding). Training: L2 loss, Adam lr $10^{-4}$, batch size 32, early stopping within 10 epochs, single NVIDIA TITAN RTX 24GB, each experiment repeated 3×.

## 📊 Dataset & Input Features
Six real-world benchmarks (multivariate), chronological splits 6:2:2 for ETT and 7:1:2 for others:
- **[[ETT]]** (Zhou et al., Informer): electricity transformer load + oil temperature, recorded every 15 minutes, July 2016–July 2018; four subsets [[ETT|ETTh1]], [[ETT|ETTh2]] (hourly) and [[ETT|ETTm1]], [[ETT|ETTm2]] (15-min).
- **[[Electricity_ECL]]**: hourly electricity consumption of 321 customers, 2012–2014 — https://archive.ics.uci.edu/ml/datasets/ElectricityLoadDiagrams20112014
- **[[Exchange]]**: daily exchange rates of 8 countries, 1990–2016 (from LSTNet).
- **[[Traffic]]**: hourly road occupancy rates, San Francisco Bay Area freeways (CalTrans sensors) — http://pems.dot.ca.gov
- **[[Weather]]**: 21 meteorological indicators (air temperature, humidity, etc.), every 10 minutes, whole year 2020 — https://www.bgc-jena.mpg.de/wetter/
- **[[ILI]]**: weekly influenza-like-illness patient ratio, US CDC, 2002–2021 — https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html
- **Case study [[COVID19_Dashboard]]**: daily confirmed deaths/recoveries, Jan 22 2020–May 20 2021, two anonymous European countries (Dong et al., Lancet Infect. Dis.) — split 7:1:2.
- Features: past window $X_{en} \in \mathbb{R}^{I\times d}$ (input length $I=96$ standard, $I=36$ for ILI); decomposed seasonal/trend-cyclical components; prediction lengths $O \in \{96,192,336,720\}$ (ILI: {24,36,48,60}; COVID-19: {7,15,30}).
- Code: https://github.com/thuml/Autoformer

## 📈 Performance & Results
Baselines (multivariate): [[Informer]], Reformer (LSH), LogTrans (LogSparse), LSTNet, LSTM, TCN; univariate adds N-BEATS, DeepAR, Prophet, ARIMA.
- **Overall**: 38% averaged MSE reduction under long-term settings across six benchmarks.
- **Multivariate, input-96-predict-336 vs previous best**: 74% ETT (1.334→0.339), 18% Electricity (0.280→0.231), 61% Exchange (1.357→0.509), 15% Traffic (0.733→0.622), 21% Weather (0.455→0.359); ILI input-36-predict-60: 43% (4.882→2.770).
- **ETT full benchmark (Appendix A)**: input-96-predict-336: 55% ETTh1 (Informer 1.128→0.505) and 80% ETTh2 (2.544→0.471) reduction; predict-288: 40% ETTm1 (1.056→0.634), 66% ETTm2 (0.969→0.342); ~60% average MSE reduction over prior SOTA on ETT. Example ETTm2 predict-96: Autoformer 0.255/0.339 (MSE/MAE) vs Informer 0.365/0.453.
- **Univariate**: state-of-the-art too; e.g. ETT predict-336: Autoformer 0.154 vs Informer 0.180, N-BEATS 0.226; Exchange predict-336: 0.508 vs N-BEATS 0.611 (17%). ARIMA wins only short-term Exchange (predict-96) but fails long-term.
- **Decomposition ablation (Table 3)**: plugging progressive decomposition into Transformer/Informer/LogTrans/Reformer gives consistent gains (e.g., Transformer predict-720: 2.672→0.537), beating separate pre-decomposed prediction despite larger models.
- **Attention ablation (Table 4)**: Auto-Correlation beats Full/LogSparse/LSH/ProbSparse attention at all input/prediction lengths; only it handles input-336-predict-1440 without OOM.
- **Pre-decomposition comparison (Table 9)**: progressive decomposition beats STL, Hodrick-Prescott, Christiano-Fitzgerald, Baxter-King filter pre-processing + dual Transformers by large margins (predict-720: 0.422 vs ≥2.150).
- Learned lags recover interpretable seasonality: 24h/168h periods in Traffic, monthly/quarterly/yearly in Exchange → human-interpretable predictions.

## 💡 Limitations & Identified Research Gaps
- Performance degrades on data with extremely weak temporal coherence/randomness (Exchange still works, but authors note poor-predictability series degenerate all models).
- Hyper-parameter $c$ trades off performance vs efficiency and needs tuning; datasets without obvious periodicity (ILI) can suffer from large $c$ (noise).
- Input-length sensitivity is dataset-specific (periodic data saturates at I=96; aperiodic ILI benefits from longer inputs).
- Decoder past-information attachment ($\frac{I}{2}+O$) trades accuracy vs memory cost (3029 MB without past vs 3599 MB full past).
- Gap for EV charging load forecasting: decomposition architecture + period-based Auto-Correlation directly applicable to strongly periodic station-level load series.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{wu2021autoformer,
  title={Autoformer: Decomposition Transformers with Auto-Correlation for Long-Term Series Forecasting},
  author={Wu, Haixu and Xu, Jiehui and Wang, Jianmin and Long, Mingsheng},
  booktitle={Advances in Neural Information Processing Systems},
  volume={34},
  pages={22419--22430},
  year={2021}
}
```

## 🔗 Key References & Citation Graph
- Vault papers: [[2021_Zhou_Informer_Beyond_Efficient_Transformer]] (direct predecessor; ETT benchmark source, ProbSparse baseline), [[2017_Attention_Is_All_You_Need]] (Transformer base), [[2020_Salinas_DeepAR_Probabilistic_Forecasting]], [[1997_Hochreiter_Long_Short_Term_Memory]] (LSTM baseline)
- Cited-in-text foundations: Transformer/Vaswani et al. 2017, LogTrans (Li et al. 2019), Reformer (Kitaev et al. 2020), LSTNet (Lai et al. 2018), N-BEATS (Oreshkin et al. 2019), Prophet (Taylor & Letham 2018), STL decomposition (Cleveland et al. 1990), Wiener–Khinchin theorem (Wiener 1930), stochastic process theory (Chatfield 1981; Papoulis 1989), TCN (Bai et al. 2018), DeepGLO (Sen et al. 2019), Adam (Kingma & Ba 2015), PyTorch (Paszke et al. 2019)
