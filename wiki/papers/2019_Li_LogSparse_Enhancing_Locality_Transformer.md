---
type: paper
title: "Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting"
authors: [Shiyang Li, Xiaoyong Jin, Yao Xuan, Xiyou Zhou, Wenhu Chen, Yu-Xiang Wang, Xifeng Yan]
year: 2019
journal_conference: "NeurIPS 2019 (33rd Conference on Neural Information Processing Systems, Vancouver)"
doi_url: "https://arxiv.org/abs/1907.00235"
models_used: ["[[LogSparse_Transformer]]", "[[Convolutional_Self_Attention]]", "[[Transformer]]", "[[DeepAR]]", "[[DeepState]]", "[[TRMF]]", "[[ARIMA]]", "[[ETS]]"]
datasets_used: ["[[Electricity_ECL|electricity-f / electricity-c]]", "[[Traffic|traffic-f / traffic-c]]", "[[Solar_Energy|solar]]", "[[Wind_Speed]]", "[[M4]]", "[[Synthetic_Sinusoidal]]"]
features_used: ["[[Historical_Load]]", "[[Time_Based_Covariates]]", "[[Positional_Embedding]]", "[[Series_ID_Embedding]]", "[[Age_Feature]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[Pinball_Loss|R0.5/R0.9 quantile loss]]", "[[NLL|Negative Log-Likelihood]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting

## 🎯 Main Objective & Contribution
- Applies the [[Transformer]] to multivariate time series forecasting and identifies two canonical weaknesses: **(1) locality-agnosticism** — point-wise dot-product self-attention ignores local context/shape, making models prone to anomalies; **(2) memory bottleneck** — $O(L^2)$ attention space complexity blocks fine-grained long-sequence modeling.
- Three contributions:
  1. Validates Transformer's superiority over RNN-based models for long-term dependencies on synthetic + real data.
  2. Proposes **convolutional self-attention**: causal convolutions (kernel $k$, stride 1) generate queries/keys so query-key matching uses local shape context; lowers training loss and improves accuracy.
  3. Proposes **[[LogSparse_Transformer]]** with only $O(L(\log L)^2)$ memory, enabling fine-grained long-series forecasting under GPU memory budgets.

## 🧠 Methodology & Model Architecture
- **Problem definition**: for $N$ related univariate series $\{z_{i,1:t_0}\}_{i=1}^N$ with time covariates $\{x_{i,1:t_0+\tau}\}$, model the conditional distribution:
$$p(z_{i,t_0+1:t_0+\tau} \mid z_{i,1:t_0},\ x_{i,1:t_0+\tau};\ \Phi) = \prod_{t=t_0+1}^{t_0+\tau} p(z_{i,t} \mid z_{i,1:t-1},\ x_{i,1:t};\ \Phi) \tag{Conditional forecasting objective}$$
reduced to one-step-ahead prediction $p(z_t \mid z_{1:t-1}, x_{1:t}; \Phi)$ with parameters $\Phi$ shared across series. Augmented input: $y_t \triangleq [z_{t-1} \circ x_t] \in \mathbb{R}^{d+1}$, $Y_t = [y_1,\dots,y_t]^T \in \mathbb{R}^{t\times(d+1)}$.
- **Canonical masked self-attention**: multi-head projections $Q_h = YW^Q_h$, $K_h = YW^K_h$, $V_h = YW^V_h$ followed by scaled dot-product attention with causal mask $M$:
$$O_h = \text{Attention}(Q_h, K_h, V_h) = \text{softmax}\left(\frac{Q_h K_h^T}{\sqrt{d_k}} \cdot M\right)V_h \tag{Scaled dot-product attention}$$
followed by position-wise feedforward (2 FC layers + ReLU). Decoder-only autoregressive mode; Gaussian likelihood head with softplus for positivity; DeepAR-style scale handling.
- **Convolutional self-attention**: replace kernel-size-1 convolutions (matrix multiplication) producing Q/K with **causal convolutions of kernel size $k$, stride 1** (with proper padding); $k=1$ degrades to canonical attention. Local-context-aware query-key matching enables shape-based matching; larger local context yields faster convergence and lower training NLL.
- **Motivating sparsity evidence**: a 10-layer canonical Transformer trained full-attention on traffic-f shows layer 2 learns global daily patterns but layers 6/10 exhibit pattern-dependent sparsity → sparsity can be introduced without hurting performance.
- **LogSparse self-attention**: each cell attends only to cells at exponential step distances plus itself:
$$I_l^k = \{l - 2^{\lfloor \log_2 l \rfloor},\ l - 2^{\lfloor \log_2 l \rfloor - 1},\ \dots,\ l - 2^0,\ l\} \tag{LogSparse index set}$$
giving $O(\log L)$ dot products per cell per layer.
  - **Theorem 1**: stacking $\lfloor \log_2 L \rfloor + 1$ layers guarantees every cell receives information from all previous cells ($S_l^{\tilde{k}_l} = \{j : j \le l\}$); the number of unique paths from cell $j$ to $l$ grows as $O(\lfloor \log_2(l-j) \rfloor!)$ — super-exponentially rich information flow. Overall memory $O(L(\log_2 L)^2)$ vs. $O(L^2)$.
  - **Local Attention** extension: densely attend within a left window of size $O(\log_2 L)$ before resuming LogSparse strategy.
  - **Restart Attention** extension: split input length $L$ into subsequences of length $L_{sub} \propto L$, apply LogSparse within each; can combine both extensions without changing complexity.
- **Training details** (App. A): learnable position embedding + time-series-ID embedding (dim 20 each, summed then concatenated with covariates); covariates include year/month/day-of-week/hour/minute/age/series-ID normalized to zero mean unit variance; Adam optimizer with early stopping (BERTAdam — warmup + LR annealing — for unstable electricity-f/traffic-f); training windows 500K (electricity-c, traffic-c), 125K/200K (fine variants), 10K/50K/50K (wind/M4/solar); $H=8$ heads; 3 layers (6 for electricity-f, 10 for traffic-f); model selection by validation NLL over 5 seeds; GTX 1080 Ti GPUs.

## 📊 Dataset & Input Features
- **Dataset statistics (Table 5)**:

| Dataset | Length T | #Series M | Sampling |
| :--- | ---: | ---: | :--- |
| electricity-c | 32,304 | 370 | 1 hour |
| electricity-f | 129,120 | 370 | 15 mins |
| traffic-c | 4,049 | 963 | 1 hour |
| traffic-f | 12,435 | 963 | 20 mins |
| wind | 10,957 | 28 | 1 day |
| solar | 5,832 | 137 | 1 hour |
| M4-Hourly | 748/1008 | 414 | 1 hour |

- **electricity-f/c**: electricity consumption of 370 customers recorded every 15 min (coarse = hourly aggregation of every 4 points).
- **traffic-f/c**: occupancy rates of 963 San Francisco bay area freeways recorded every 20 min (coarse = hourly average of 3 points).
- **solar**: solar power production Jan–Aug 2006, hourly from 137 PV plants in Alabama — URL: https://www.nrel.gov/grid/solar-power-data.html
- **wind**: daily estimates of 28 countries' energy potential 1986–2015 as % of plant max output — URL: https://www.kaggle.com/sohier/30-years-of-european-wind-generation
- **M4-Hourly**: 414 hourly series from the M4 competition (train/test provided).
- **Synthetic piece-wise sinusoidal data** with amplitude change requiring long memory: $A_1,A_2,A_3 \sim U([0,60])$, $A_4=\max(A_1,A_2)$, noise $N_x \sim \mathcal{N}(0,1)$; 8 datasets with history $t_0 \in \{24,...,192\}$; 4.5K/0.5K/1K train/val/test instances each.
- **Test splits**: one week from 9/1/2014 00:00 (electricity), 6/15/2008 17:00 (traffic), last 7 days of August (solar), last 210 days of 2015 (wind).
- **Features**: historical values + time-based covariates ([[Time_Based_Covariates]]: year, month, day-of-week, hour-of-day, minute, age feature, time-series ID).
- **Other URLs in text**: BERTAdam implementation https://github.com/nlpdata/mrc_bert_baseline/blob/master/bert/optimization.py ; multi-step latent-state forecaster http://roseyu.com/time-series-workshop/submissions/2019/timeseries-ICML19_paper_19.pdf . No explicit data availability statement beyond dataset URLs above.

## 📈 Performance & Results
- **Metric**: $\rho$-quantile loss
$$R_\rho(x, \hat{x}) = \frac{2\sum_{i,t} D_\rho(x_t^{(i)}, \hat{x}_t^{(i)})}{\sum_{i,t}|x_t^{(i)}|},\qquad D_\rho(x,\hat{x}) = (\rho - I\{x \le \hat{x}\})(x - \hat{x}) \tag{Quantile loss}$$
- **Synthetic (Fig. 4b)**: at $t_0=24$ both Transformer and [[DeepAR]] (3-layer LSTM baseline, hidden sizes 20→200) are accurate; for $t_0 \ge 96$ DeepAR degrades sharply while canonical Transformer keeps accuracy — LSTM cannot capture these long-term dependencies.
- **Coarse datasets (Table 1, R0.5/R0.9)**:

| Dataset | ARIMA | ETS | TRMF | DeepAR | DeepState | **Ours** |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| e-c 1d | 0.154/0.102 | 0.101/0.077 | 0.084/- | 0.075/0.040 | 0.083/0.056 | **0.059/0.034** |
| e-c 7d | 0.283/0.109 | 0.121/0.101 | 0.087/- | 0.082/0.053 | 0.085/0.052 | **0.070/0.044** |
| t-c 1d | 0.223/0.137 | 0.236/0.148 | 0.186/- | 0.161/0.099 | 0.167/0.113 | **0.122/0.081** |
| t-c 7d | 0.492/0.280 | 0.509/0.529 | 0.202/- | 0.179/0.105 | 0.168/0.114 | **0.139/0.094** |

- **Convolutional self-attention ablation (Table 2)**: kernel sizes $k\in\{2..9\}$ give marginal gains on electricity-c (R0.5 0.057–0.059 vs 0.060 at k=1) but consistent gains on challenging traffic-c — up to **9% relative improvement** (R0.9 0.081 at k=9 vs 0.089 at k=1); also converges faster with lower training NLL.
- **Sparse vs full attention (Table 3)**: under equal memory budget, sparse beats full on traffic-f (e.g., Sparse+Conv R0.5/R0.9 = 0.138/0.092 vs Full+Conv 0.149/0.102); with same input length, full attention generally wins except Sparse+Conv on traffic-f slightly outperforms full attention on R0.5 (0.138 vs 0.147).
- **Multi-granularity comparison (Table 4, R0.5/R0.9)**: ours 0.074/0.042 (electricity-f 1d), 0.139/0.090 (traffic-f 1d), 0.210/0.082 (solar 1d), 0.067/0.025 (M4-Hourly 2d), 0.284/0.108 (wind 30d) vs DeepAR 0.082/0.063, 0.230/0.150, 0.222/0.093, 0.090/0.030, 0.286/0.116 and TRMF point forecasts 0.094/0.213/0.241/0.311 — best overall.

## 💡 Limitations & Identified Research Gaps
- Training on electricity-f/traffic-f unstable with vanilla Adam — required BERTAdam workaround.
- With identical input lengths, full attention still mostly outperforms sparse (except strong-long-dependency traffic-f) — sparsity trades capacity for feasibility.
- Covariate-rich easy datasets (electricity-c) leave little room for locality gains.
- Authors' future directions: better sparsity strategies in self-attention; better fit to small datasets.
- Thesis relevance: LogSparse attention is a direct precursor of efficient EV-charging forecasters (cf. [[2021_Zhou_Informer_Beyond_Efficient_Transformer]]); convolutional self-attention motivates locality-aware attention for minute-level charging load sequences.

## 📚 BibTeX & Citation Reference
```bibtex
@inproceedings{li2019logsparse,
  title={Enhancing the Locality and Breaking the Memory Bottleneck of Transformer on Time Series Forecasting},
  author={Li, Shiyang and Jin, Xiaoyong and Xuan, Yao and Zhou, Xiyou and Chen, Wenhu and Wang, Yu-Xiang and Yan, Xifeng},
  booktitle={Advances in Neural Information Processing Systems 32 (NeurIPS)},
  year={2019}
}
```

## 🔗 Key References & Citation Graph
- Foundation architecture: [[2017_Attention_Is_All_You_Need]] (Vaswani et al., NeurIPS 2017)
- Probabilistic baselines: [[2020_Salinas_DeepAR_Probabilistic_Forecasting]] (Flunkert et al.), DeepState (Rangapuram et al., NeurIPS 2018)
- Downstream efficient Transformers in vault: [[2021_Zhou_Informer_Beyond_Efficient_Transformer]], [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]], [[2023_Nie_PatchTST_A_Time_Series_is_Worth_64_Words]]
- Other cited anchors: WaveNet (van den Oord et al., 2016 — causal convolutions), Sparse Transformers (Child et al., arXiv:1904.10509), TRMF (Yu et al., NeurIPS 2016), [[2014_Adam_Adam_Stochastic_Optimization]]
