---
type: paper
title: "Long-term Forecasting with TiDE: Time-series Dense Encoder"
authors: [Abhimanyu Das, Weihao Kong, Andrew Leach, Shaan Mathur, Rajat Sen, Rose Yu]
year: 2024
journal_conference: "arXiv:2304.08424v5 [stat.ML] (Google Research / Google Cloud / UC San Diego)"
doi_url: "https://arxiv.org/abs/2304.08424"
models_used: ["[[TiDE]]", "[[DLinear]]", "[[PatchTST]]", "[[NHiTS]]", "[[DeepAR]]", "[[S4]]", "FEDformer", "[[Autoformer]]", "[[Informer]]", "Pyraformer", "LogTrans", "[[LSTM]]"]
datasets_used: ["[[Electricity_ECL]]", "[[Traffic]]", "[[Weather_Dataset]]", "[[ETT]]", "[[ETT]]", "[[ETT]]", "[[ETT]]", "[[M5_Dataset]]", "Synthetic LDS Dataset"]
features_used: ["[[Lookback_Window]]", "[[Dynamic_Covariates]]", "[[Static_Attributes]]", "[[Time_Derived_Features]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[MSE]]", "[[MAE]]", "WRMSSE"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Long-term Forecasting with TiDE: Time-series Dense Encoder

## 🎯 Main Objective & Contribution
- Motivated by [[DLinear]] showing simple linear models beat Transformer-based long-term forecasters, proposes **[[TiDE]] (Time-series Dense Encoder)**: an MLP-based encoder-decoder with the simplicity/speed of linear models plus the ability to handle covariates and non-linear dependencies — no self-attention, recurrence, or convolution.
- Theory: proves the simplest linear analogue of TiDE achieves **near-optimal error rate for [[Linear_Dynamical_Systems]] (LDS)** when the design matrix's maximum singular value is bounded away from 1; empirically validated on synthetic LDS data where Linear beats LSTM and Transformer.
- Empirics: matches or outperforms prior neural approaches on standard benchmarks (>10% lower MSE on the largest dataset), while being **5x faster at inference and >10x faster in training** than the best Transformer baseline ([[PatchTST]]).

## 🧠 Methodology & Model Architecture
Problem (**Eq. 1, forecaster mapping**): channel-independent mapping of one series' look-back $y^{(i)}_{1:L}$, dynamic covariates $x^{(i)}_{1:L+H} \in \mathbb{R}^r$, and static attributes $a^{(i)}$ to horizon predictions:
$$f: \left\{y^{(i)}_{1:L}\}_{i=1}^N,\ \{x^{(i)}_{1:L+H}\}_{i=1}^N,\ \{a^{(i)}\}_{i=1}^N\right\} \longrightarrow \left\{\hat{y}^{(i)}_{L+1:L+H}\right\}_{i=1}^N$$
Evaluated by MSE over all $NH$ points (**Eq. 2**). Weights trained globally on the whole dataset (global univariate style).

**Residual block**: MLP with one ReLU hidden layer, fully linear skip connection, dropout on the output linear layer, layer norm at output.

### Encoding
- **Feature projection** per time-step to dimension $\tilde{r} \ll r$ (`temporalWidth`), reducing flattened covariate input size from $(L+H)r$ to $(L+H)\tilde{r}$ (**Eq. 3**):
$$\tilde{x}^{(i)}_t = \text{ResidualBlock}(x^{(i)}_t)$$
- **Dense encoder**: stack/flatten projected covariates, concatenate static attributes and past series, map through $n_e$ residual blocks of hidden size `hiddenSize` (**Eq. 4**):
$$e^{(i)} = \text{Encoder}\left(y^{(i)}_{1:L};\ \tilde{x}^{(i)}_{1:L+H};\ a^{(i)}\right)$$

### Decoding
- **Dense decoder** ($n_d$ residual blocks): maps encoding $e^{(i)}$ to vector $g^{(i)} \in \mathbb{R}^{pH}$ ($p$ = `decoderOutputDim`), reshaped to $D^{(i)} \in \mathbb{R}^{p\times H}$ whose $t$-th column $d^{(i)}_t$ decodes time-step $t$:
$$g^{(i)} = \text{Decoder}(e^{(i)}) \in \mathbb{R}^{pH}, \qquad D^{(i)} = \text{Reshape}(g^{(i)}) \in \mathbb{R}^{p\times H}$$
- **Temporal decoder**: per-horizon-step residual block creating a "highway" from future covariates directly to each prediction (useful when a covariate strongly affects a specific step, e.g., holidays):
$$\hat{y}^{(i)}_{L+t} = \text{TemporalDecoder}\left(d^{(i)}_t;\ \tilde{x}^{(i)}_{L+t}\right) \quad \forall t \in [H]$$
- **Global residual connection**: linear map from look-back to horizon added to predictions, guaranteeing DLinear-style pure linear models are a subclass.

Training: mini-batch gradient descent, MSE loss, rolling validation; inference scales as $\tilde{O}(n_e h^2 + hL)$ vs PatchTST's $\tilde{O}(Kn_a L^2/P^2)$ quadratic-in-$L$ encoder cost. Batch size 512, `temporalWidth` 4, Adam with cosine-decay LR schedule, optional reversible instance normalization ([RevIN]); tuned hyperparameters per dataset (hiddenSize ∈ {256,512,1024}, layers ∈ {1,2,3}, etc.).

### Theoretical Analysis (Appendix A)
LDS definition (**Eqs. 5-6**):
$$h_{t+1} = Ah_t + Bx_t + \eta_t, \qquad y_t = Ch_t + Dx_t + \xi_t$$
LDS predictor (**Eq. 7**):
$$\hat{y}_t = y_{t-1} + (CB+D)x_t - Dx_{t-1} + \sum_{i=1}^{t-1}C(A^i - A^{i-1})Bx_{t-i}$$
**Proposition A.4 (LDS approximation)**: with look-back $k = \Omega(\log(1/\epsilon))$ and blocks $M^{(j)} = C(A^{j+1}-A^j)B$, $M^{(x')} = C(A-I)B - D$, $M^{(x)} = CB+D$, $M^{(y)} = I$: $\|M_\Theta\tilde{X}_t - y_T\|_2 \le \|M_\Theta\tilde{X}_t - \hat{y}_T\|_2 + O(\gamma^{k+2} + \frac{\gamma^{2k+4}}{1-\gamma}) \le \|M_\Theta\tilde{X}_t-\hat{y}_t\|+\epsilon$ for $0 \preceq A \preceq \gamma I,\ \gamma<1$.
**Proposition A.3 (generalization bound)** via Rademacher complexity: with probability $\ge 1-\delta$,
$$\ell_{\mathcal{D}}(\hat{h}) - \min_{h\in H}\ell_{\mathcal{D}}(h) \le \epsilon + O\!\left(\frac{\log(1/\epsilon)\sqrt{\log 1/\delta}}{\sqrt{N}}\right)$$

## 📊 Dataset & Input Features
| Dataset | #Time-Series | #Time-Points | Frequency |
| :--- | :---: | :---: | :--- |
| Electricity | 321 | 26,304 | 1 hour |
| Traffic | 862 | 17,544 | 1 hour |
| Weather | 21 | 52,696 | 10 min |
| ETTh1 / ETTh2 | 7 | 17,420 | 1 hour |
| ETTm1 / ETTm2 | 7 | 69,680 | 15 min |

- Train:val:test = 7:1:2 (standard normalized datasets); look-backs tuned in {24,48,96,192,336,720}, horizons {96,192,336,720}; TiDE uses context length 720 throughout.
- Covariates: 8 time-derived features (minute-of-hour, hour-of-day, day-of-week etc.) normalized to [−0.5, 0.5] à la GluonTS (these hurt DLinear but help TiDE).
- **M5 demand forecasting**: >30k Walmart sales series; dynamic features snap_CA/snap_TX/snap_WI, event_type_1/2 + date features; static attributes category_id/store_id/department_id/item_id embedded; zero-inflated negative binomial loss; ≤100 epochs, early-stop patience 5.
- Synthetic LDS dataset: 30×30 Wishart matrix scaled to operator norm 0.95, Gaussian noise, 5-dim observed inputs, hidden seasonality of 6 periodicities; 4 series; look-back/horizon 320.
- Links: paper https://arxiv.org/abs/2304.08424 ; M5 GluonTS setup https://github.com/awslabs/gluonts/blob/dev/examples/m5_gluonts_template.ipynb ; implementation "provided in the supplementary" (TensorFlow).

## 📈 Performance & Results
- Benchmarks (MSE, selected): Traffic-720 **0.386 vs PatchTST 0.432 (10.6% better)**; Electricity-720 0.196 vs PatchTST 0.197; ETTh2-96 0.270 vs 0.274; ETTm2-96 0.161 vs 0.166; best or statistically-tied-with-best in nearly all settings except Weather horizons 96-336 where PatchTST wins (TiDE wins Weather-720: 0.313 vs 0.314). Beats DLinear significantly everywhere except ETTh1-192 (tie).
- Sub-quadratic attention approximations (FEDformer/Autoformer/Informer/Pyraformer/LogTrans) far behind, e.g., Informer Traffic-96 MSE 0.733 vs TiDE 0.336.
- vs S4: vastly better, e.g., ETTh2-720 MSE 0.419 vs 2.650; Electricity-720 0.196 vs 0.578.
- **M5 (WRMSSE, private test set)**: TiDE w/ static+dynamic covariates **0.611 ± 0.009**; TiDE date-only 0.637 ± 0.005; DeepAR 0.789 ± 0.025 (≈20% worse); PatchTST (no covariates) 0.976 ± 0.014.
- **Efficiency** (Electricity, batch 8×321×L, single NVIDIA T4): order-of-magnitude faster inference than PatchTST; training-time gap grows with L; PatchTST runs out of GPU memory for L ≥ 1440.
- **Ablations**: temporal decoder learns event-covariate effects after just 1 epoch on a modified Electricity dataset (Type A ×[3,3.2] increase, Type B ÷[2,2.2] decrease events, noisy Gaussian indicator covariates); removing residual connections degrades Electricity MSE (e.g., 96: 0.136→0.235); accuracy improves monotonically with context size (unlike FEDformer/Informer).
- Synthetic LDS: Linear MSE **0.510 ± 0.001** < Transformer 0.731 ± 0.041 < LSTM 1.455 ± 0.455.

## 💡 Limitations & Identified Research Gaps
- Self attention may still be unnecessary only for these long-term benchmarks; rigorous analysis of MLPs/Transformers under models with varying seasonality/trend levels remains open.
- Transformers are more parameter-efficient than MLPs despite higher memory/compute intensity — a limitation for extremely large-scale pre-trained forecasting models.
- Point forecasts with MSE loss only; no probabilistic outputs; no EV-specific evaluation (Electricity/Traffic are proxy domains).

## 📚 BibTeX & Citation Reference
```bibtex
@article{das2024tide,
  author  = {Das, Abhimanyu and Kong, Weihao and Leach, Andrew and Mathur, Shaan and Sen, Rajat and Yu, Rose},
  title   = {Long-term Forecasting with {TiDE}: Time-series Dense Encoder},
  journal = {arXiv preprint arXiv:2304.08424},
  year    = {2024},
  url     = {https://arxiv.org/abs/2304.08424}
}
```

## 🔗 Key References & Citation Graph
- [[2023_DLinear_Are_Transformers_Effective_LTSF]] — linear-model motivation; DLinear subclass of TiDE
- [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]] — strongest baseline; source of reported numbers
- [[2021_Autoformer_Decomposition_Transformers_AutoCorrelation]] — benchmark baselines + dataset protocol
- [[2021_Informer_Beyond_Efficient_Transformer]] — ProbSparse attention baseline
- [[2019_LogSparse_Enhancing_Locality_Transformer]] — LogTrans baseline
- [[2023_NHiTS_Neural_Hierarchical_Interpolation]] — N-HiTS MLP-based baseline
- [[2020_DeepAR_Probabilistic_Forecasting]] — M5 comparison baseline
- Gu et al., S4 (ICLR) — structured state-space comparison
- [[2017_Attention_Is_All_You_Need]] — Transformer origin
- [[1997_Long_Short_Term_Memory]] — LSTM baseline
- Kalman 1963 — linear dynamical systems theory foundation
- Kim et al. ICLR 2021 — [[RevIN]] reversible instance normalization (optional component)
- Alexandrov et al. 2020 — GluonTS covariate normalization convention
