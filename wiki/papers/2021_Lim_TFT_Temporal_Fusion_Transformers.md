---
type: paper
title: "Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting"
authors: [Bryan Lim, Sercan Ö. Arık, Nicolas Loeff, Tomas Pfister]
year: 2021
journal_conference: "International Journal of Forecasting, Vol. 37, No. 4, pp. 1374-1389"
doi_url: "https://doi.org/10.1016/j.ijforecast.2021.03.012"
models_used: ["[[Temporal_Fusion_Transformer|Temporal Fusion Transformer]]", "[[GRN|Gated Residual Network]]", "[[VSN|Variable Selection Network]]", "[[LSTM]]", "[[Interpretable_Multi_Head_Attention]]", "[[Quantile_Regression]]"]
datasets_used: ["[[Electricity_ECL|UCI Electricity Load Diagrams (ECL)]]", "[[Traffic|UCI PEM-SF Traffic]]", "[[Favorita_Retail|Favorita Grocery Sales]]", "[[Oxford_Man_Realized_Library|OMI Realized Volatility]]"]
features_used: ["[[Static_Covariates]]", "[[Past_Observed_Inputs]]", "[[Known_Future_Inputs]]", "[[Calendar_Features]]", "[[Entity_Embeddings]]"]
forecasting_horizon: "[[Multi_Horizon]]"
metrics: ["[[Pinball_Loss]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting

## 🎯 Main Objective & Contribution
- Proposes the **[[Temporal_Fusion_Transformer|Temporal Fusion Transformer]]**: an attention-based architecture for **multi-horizon forecasting** that natively handles heterogeneous inputs — [[Static_Covariates]], [[Past_Observed_Inputs]], and [[Known_Future_Inputs]] — which autoregressive models (DeepAR, DSSM, ConvTrans) and prior direct methods (MQRNN, Seq2Seq) mishandle or treat as black boxes.
- Five architectural novelties: (1) gating mechanisms for adaptive depth, (2) instance-wise variable selection networks, (3) static covariate encoders producing context vectors, (4) LSTM sequence-to-sequence local processing + interpretable multi-head self-attention decoder, (5) quantile outputs for prediction intervals.
- Three interpretability use cases demonstrated on whole datasets: global variable importance, persistent temporal patterns (seasonality/lags from raw data), and regime/event identification (S&P 500 2008 crisis detected via attention-distance metric).

## 🧠 Methodology & Model Architecture
Problem setup (Eq. 1): entity $i$ has static covariates $s_i$, observed inputs $z_{i,t}$ (unknown in advance), known inputs $x_{i,t}$ (predetermined); quantile forecast over look-back window $k$ and horizons $\tau\in\{1,\dots,\tau_{max}\}$:
$$\hat{y}_i(q,t,\tau) = f_q(\tau,\; y_{i,t-k:t},\; z_{i,t-k:t},\; x_{i,t-k:t+\tau},\; s_i) \tag{Quantile Forecast Form}$$

### Gated Residual Network (GRN)
$$\text{GRN}_{\omega}(a,c) = \text{LayerNorm}(a + \text{GLU}_{\omega}(\eta_1)),\quad \eta_1 = W_{1,\omega}\eta_2 + b_{1,\omega},\quad \eta_2 = \text{ELU}(W_{2,\omega}a + W_{3,\omega}c + b_{2,\omega})$$
with Gated Linear Unit enabling component suppression (adaptive depth):
$$\text{GLU}_{\omega}(\gamma) = \sigma(W_{4,\omega}\gamma + b_{4,\omega}) \odot (W_{5,\omega}\gamma + b_{5,\omega})$$

### Variable Selection Networks (instance-wise)
$$v_{\chi_t} = \text{Softmax}(\text{GRN}_{v_\chi}(\Xi_t, c_s)) \tag{Selection Weights}$$
$$\tilde{\xi}_t = \sum_{j=1}^{m_\chi} v_{\chi_t}^{(j)}\,\tilde{\xi}_t^{(j)}, \qquad \tilde{\xi}_t^{(j)} = \text{GRN}_{\tilde{\xi}^{(j)}}(\xi_t^{(j)}) \tag{Weighted Combination}$$

### Static Covariate Encoders
Four context vectors $c_s, c_e, c_c, c_h$ via separate GRNs on static features, e.g. $c_s=\text{GRN}_{c_s}(\zeta)$ — conditioning variable selection ($c_s$), LSTM cell/hidden states ($c_c, c_h$), and temporal feature enrichment ($c_e$).

### Interpretable Multi-Head Attention
Shares values across heads with additive aggregation (ensemble of attention weight matrices $\tilde{A}(Q,K)$), keeping weights directly interpretable:
$$\tilde{H} = \tilde{A}(Q,K)\,V W_V = \frac{1}{H}\sum_{h=1}^{m_H} \text{Attention}(QW_Q^{(h)}, KW_K^{(h)}, VW_V)$$

### Temporal Fusion Decoder
1. **Locality / seq2seq layer**: LSTM encoder–decoder over past/future inputs (replaces positional encoding; cell/hidden state initialized by $c_c,c_h$):
   $$\tilde{\phi}(t,n) = \text{LayerNorm}(\tilde{\xi}_{t+n} + \text{GLU}_{\tilde{\phi}}(\phi(t,n)))$$
2. **Static enrichment**: $\theta(t,n) = \text{GRN}_\theta(\tilde{\phi}(t,n), c_e)$
3. **Temporal self-attention** (causal decoder masking): $B(t) = \text{InterpretableMultiHead}(\Theta(t),\Theta(t),\Theta(t))$, then $\delta(t,n)=\text{LayerNorm}(\theta(t,n)+\text{GLU}_\delta(\beta(t,n)))$
4. **Position-wise feed-forward** with gated skip over the entire transformer block:
   $$\psi(t,n)=\text{GRN}_\psi(\delta(t,n)), \qquad \tilde{\psi}(t,n)=\text{LayerNorm}(\tilde{\phi}(t,n)+\text{GLU}_{\tilde{\psi}}(\psi(t,n)))$$
5. **Quantile outputs**: $\hat{y}(q,t,\tau) = W_q\tilde{\psi}(t,\tau)+b_q$

### Training Loss & Evaluation
Joint quantile (pinball) loss over $Q=\{0.1, 0.5, 0.9\}$:
$$\mathcal{L}(\Omega,W) = \sum_{y_t\in\Omega}\sum_{q\in Q}\sum_{\tau=1}^{\tau_{max}} \frac{QL(y_t,\hat{y}(q,t-\tau,\tau),q)}{M_{\tau_{max}}}, \qquad QL(y,\hat{y},q) = q(y-\hat{y})_+ + (1-q)(\hat{y}-y)_+$$
Normalized out-of-sample metric:
$$\text{q-Risk} = \frac{2\sum_{y_t\in\tilde\Omega}\sum_{\tau=1}^{\tau_{max}} QL(y_t,\hat{y}(q,t-\tau,\tau),q)}{\sum_{y_t\in\tilde\Omega}\sum_{\tau=1}^{\tau_{max}} |y_t|}$$
Interpretability math: horizon decomposition $\beta(t,\tau)=\sum_{n=-k}^{\tau_{max}}\alpha(t,n,\tau)\tilde\theta(t,n)$; regime detection via Bhattacharyya-based distance $\kappa(p,q)=\sqrt{1-\rho(p,q)}$, $\text{dist}(t)=\sum_\tau \kappa(\bar\alpha(\tau),\alpha(t,\tau))/\tau_{max}$ (threshold 0.3).

## 📊 Dataset & Input Features
| Dataset | Entities | Samples | Resolution | Look-back $k$ | Horizon $\tau_{max}$ |
| :-- | :--: | :--: | :--: | :--: | :--: |
| [[Electricity_ECL]] (UCI Load Diagrams) | 370 customers | 500k | hourly | 168 h (1 week) | 24 h |
| [[Traffic]] (UCI PEM-SF, SF Bay Area freeways) | 440 sensors | 500k | hourly | 168 h | 24 h |
| [[Favorita_Retail]] (Kaggle) | ~135k product-store pairs | 450k train + 50k val | daily | 90 d | 30 d |
| [[Volatility]] (Oxford-Man realized library, rv5_ss) | 31 stock indices (41 regions) | ~100k | daily | 252 d (1 yr) | 5 d |

- Data/code links found in text:
  - TFT open-source implementation: https://github.com/google-research/google-research/tree/master/tft
  - Retail dataset: https://www.kaggle.com/c/favorita-grocery-sales-forecasting/
  - Volatility dataset: https://realized.oxford-man.ox.ac.uk/
- Electricity split per DeepAR protocol: 2014-01-01→2014-09-01, first 90% train, last 10% validation, test on following 7 days; z-score normalization per entity. Inputs: target + day-of-week, hour-of-day, time index, categorical entity ID.
- Optimal configs (Table 1): Electricity dropout 0.1/state size 160/4 heads; Traffic 0.3/320/4; Retail 0.1/240/4; Volatility 0.3/160/1 head; single interpretable attention layer throughout.
- Compute: one NVIDIA Tesla V100; ~6 h training (52 min/epoch) on Electricity; batched inference of 50k samples in 8 min.

## 📈 Performance & Results
- **Outperforms all benchmarks on every dataset** (Table 2), improving on the next-best method by **3%–26%**; average **7% lower P50 and 9% lower P90** losses vs next best model.
  - Electricity P50/P90: TFT **0.055 / 0.027** vs ConvTrans 0.059 (+7%) / 0.034 (+26%), DeepAR 0.075 (+36%) / 0.040 (+48%), TRMF 0.084 (+53%), DSSM 0.083 (+51%), ETS 0.102 (+85%), ARIMA 0.154 (+180%), MQRNN 0.077 (+40%), Seq2Seq 0.067 (+22%).
  - Traffic P50/P90: TFT **0.095 / 0.070** vs ConvTrans 0.122 (+28%) / 0.081 (+15%), Seq2Seq 0.105 (+11%) / 0.075 (+6%), DeepAR 0.161 (+69%) / 0.099 (+40%).
  - Retail P50/P90: TFT **0.354 / 0.147** vs MQRNN 0.379 (+7%) / 0.152 (+3%), ConvTrans 0.429 (+21%) / 0.192 (+30%), DeepAR 0.574 (+62%) / 0.230 (+56%).
  - Volatility P50/P90: TFT **0.039 / 0.020** vs ConvTrans 0.047 (+20%) / 0.024 (+22%), DeepAR 0.050 (+28%) / 0.024 (+21%).
- **Ablations** (all components contribute): removing local processing or self-attention raises P90 loss >6% on average (>20% on some datasets); variable selection +4.1% avg P90; static covariate encoders +2.6% avg; gating layers +1.9% avg (4.1% on noisy small Volatility). Local processing is even detrimental on Electricity (dominant persistent daily seasonality better captured by direct attention).
- Interpretability findings: hour-of-day has the highest variable importance on Electricity/Traffic (future hour-of-day weight ≈0.74/0.78, exceeding the target itself); attention spikes reveal daily seasonality (Electricity/Traffic), weekly pattern + recency decay (Retail), uniform moving-average-like attention (Volatility); dist(t) peaks flag high-volatility regimes incl. the 2008 financial crisis.

## 💡 Limitations & Identified Research Gaps
- Single interpretable attention layer only; quadratic attention cost limits very long look-back windows.
- Iterative baselines required imputation of unknown future inputs (last-value carry-forward), an artificial handicap whose realism varies by application.
- Static enrichment assumes informative metadata; datasets lacking rich static covariates (Electricity/Traffic use only entity ID) limit that pathway's evaluation.
- Quantiles fixed at {0.1, 0.5, 0.9}; no full predictive density or joint multivariate sampling across entities.
- Gap for thesis: TFT's point/quantile forecasts are not calibrated probabilistically (vs conformal methods like [[2021_Stankeviciute_Conformal_Time_Series_Forecasting]]) and its attention cost motivates efficient variants ([[2021_Zhou_Informer_Beyond_Efficient_Transformer]]) — both relevant to EV charging load forecasting where station-level static metadata and calendar features abound.

## 📚 BibTeX & Citation Reference
```bibtex
@article{lim2021temporal,
  title={Temporal Fusion Transformers for Interpretable Multi-horizon Time Series Forecasting},
  author={Lim, Bryan and Ar{\i}k, Sercan {\"O}. and Loeff, Nicolas and Pfister, Tomas},
  journal={International Journal of Forecasting},
  volume={37},
  number={4},
  pages={1374--1389},
  year={2021},
  doi={10.1016/j.ijforecast.2021.03.012}
}
```

## 🔗 Key References & Citation Graph
- Foundation: [[2017_Attention_Is_All_You_Need]] (Vaswani et al., scaled dot-product & multi-head attention [17]); GLU gating (Dauphin et al.) ; LayerNorm; ELU.
- Benchmarks compared: DeepAR ([[2020_Salinas_DeepAR_Probabilistic_Forecasting]]), DSSM, ConvTrans (Li et al. LogTrans), MQRNN, TRMF, Seq2Seq, ARIMA, ETS.
- Related vault papers: [[2021_Rasul_TimeGrad_Diffusion_Forecasting]], [[2021_Zhou_Informer_Beyond_Efficient_Transformer]], [[2021_Wu_Autoformer_Decomposition_Transformers_AutoCorrelation]], [[2021_Stankeviciute_Conformal_Time_Series_Forecasting]]
- Shared benchmark datasets with EV relevance: [[Electricity_ECL]], [[Traffic]]
