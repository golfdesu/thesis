---
type: paper
title: "Deep learning predicts real-world electric vehicle direct current charging profiles and durations"
authors: [Siyi Li, Mingrui Zhang, Robert Doel, Benjamin Ross, Matthew D. Piggott]
year: 2025
journal_conference: "Nature Communications 16:10921"
doi_url: "https://doi.org/10.1038/s41467-025-65970-y"
models_used: ["[[Temporal_Fusion_Transformer]]", "[[beta-VAE]]", "[[LSTM]]"]
datasets_used: ["[[NW_Europe_DCFC_Dataset]]", "[[Weather]]"]
features_used: ["[[Charging_Power]]", "[[Battery_SOC]]", "[[State_of_Charge]]", "[[Temperature]]", "[[Connector_Power_Rating]]", "[[Connector_Type]]", "[[Estimated_Battery_Capacity]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[Relative_Accuracy]]", "[[Pinball_Loss]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Deep learning predicts real-world electric vehicle direct current charging profiles and durations

## 🎯 Main Objective & Contribution
- Predict real-world EV [[Direct_Current_Fast_Charging|DCFC (direct current fast charging)]] power–SoC charging profiles and charging **durations** from as little as a **single data point**, updating predictions in real time (event-driven) as new SoC readings arrive.
- Contributions:
  - Two-stage deep learning workflow on **909,135 real-world DCFC sessions** (612 chargers, NW Europe, Nov 2021–Jul 2024): a β-VAE anomaly detector + a probabilistic profile prediction model ([[Temporal_Fusion_Transformer]]-based).
  - Self-supervised training with random masking enables operation on partial profiles of arbitrary length; quantile outputs give calibrated uncertainty.
  - Demonstrated operational accuracy: **90% relative accuracy** from 1 point; **95% relative accuracy and <1 min absolute error from six points within five minutes**.
  - Real-time capable: forward pass over 1024 sessions in ~100 ms (>10,000 sessions/s).

## 🧠 Methodology & Model Architecture
- **Stage 1 – Anomaly detection**: β-Variational Autoencoder (β-VAE) with [[RevIN]] layers (handles distributional shift / scale-invariance), VSNs, GRNs, and seq2seq LSTM encoder/decoder (3 LSTM layers each, state size 128, latent size 6, ~1.5M params). Trained on 810,765 sessions, validated on 90,086; converged in ~250 epochs, batch size 512, max LR 10⁻³, AdamW, ~40 A100 GPU-hours (~250 epochs).
- **Stage 2 – Profile prediction**: TFT-style architecture — feature projection layer (linear projections for numeric series; trainable embedding for categorical connector type), variable selection networks (VSNs), gated residual networks (GRNs), gated linear units (GLUs), layer norm, 5 LSTM layers + 3 multi-head attention layers (4 heads each), state size 256, ~9.8M params. Static covariates also serve as context vectors for VSN/GRN and initialize LSTM cell/hidden states. Trained ~350 epochs, batch size 1024, max LR 5×10⁻⁴, AdamW, ~72 A100 GPU-hours per run; deployed as an ensemble (weighted mean of three independently trained instances with different seeds/data splits). Causal (past+present only); trained self-supervised by masking 10–99% of each profile.
- **Key Equations**:
  - **Eq. 1 — β-VAE total loss** (reconstruction + weighted KL divergence):
    $$ \mathcal{L}(\mathbf{W}; \mathbf{y}) = \mathcal{L}_{\text{recon}}(\mathbf{W}; \mathbf{y}) + \beta \cdot \mathcal{L}_{\text{KL}}(\mathbf{W}; \mathbf{y}), $$
    where $\mathbf{W}$ are model weights and $\beta$ controls the KL term contribution.
  - **Eq. 2 — MSE reconstruction loss & KL divergence loss** (with padding mask $m_{pad}$):
    $$ \mathcal{L}_{\text{recon}}(\mathbf{W}; \mathbf{y}) = \frac{1}{\sum_j m_{pad,j}} \sum_k m_{pad} \odot (\mathbf{y} - \hat{\mathbf{y}})_k^2, $$
    $$ \mathcal{L}_{\text{KL}}(\mathbf{W}; \mathbf{y}) = \frac{1}{2} \sum_{k=1}^{K} \left( \mu_k^2 + \sigma_k^2 - 1 - \log(\sigma_k^2) \right), $$
    where $K$ is latent dimensionality, $\mu_k$, $\sigma_k$ the encoded latent mean/std, $\odot$ the Hadamard product.
  - **Eq. 3 — Logistic beta-annealing schedule** (prevents posterior collapse; steepness $k=0.1$, $t_0=90$, $\beta_0=10^{-5}$):
    $$ \beta = \frac{1}{1 + \exp(-k \cdot (t - t_0))} \cdot \beta_0, $$
  - **Eq. 4 — Total quantile loss** over quantiles $q \in \{0.1, 0.25, 0.5, 0.75, 0.9\}$:
    $$ \mathcal{L}_{\text{quantile}}(\mathbf{W}; \mathbf{y}) = \sum_q \mathcal{L}_q(\mathbf{W}; \mathbf{y}). $$
  - **Eq. 5 — Quantile-specific loss** (masked, pinball loss):
    $$ \mathcal{L}_q(\mathbf{W}; \mathbf{y}) = \frac{1}{\sum |m|} \left[ m \odot \left( q\,(\mathbf{y} - \hat{\mathbf{y}}_q)^+ + (1-q)(\hat{\mathbf{y}}_q - \mathbf{y})^+ \right) \right], $$
    with $(\cdot)^+ = \max(0,\cdot)$.
  - **Eq. 6 — Masking term** ($m_{pad}$: real vs padded positions; $m_{hidden}$: predicted positions; $m_{train}$: input positions; $\alpha=0.1$):
    $$ m = m_{pad} \odot \left( m_{hidden} + \alpha m_{train} \right). $$
  - **Eq. 7 — Charging duration from predicted profile**:
    $$ T_{\text{session}} = \int_{s_{start}}^{s_{stop}} \frac{\hat{c}}{p(s)}\, ds, $$
    where $\hat{c}$ is estimated battery capacity (kWh) and $p(s)$ is power (kW) vs SoC $s$.

## 📊 Dataset & Input Features
- **Dataset**: proprietary Shell dataset of **909,135 high-quality DCFC sessions** from **612 chargers in northwestern Europe** (Great Britain 77.1%, Germany 22%, Netherlands 0.9%), Nov 2021 – Jul 2024; connectors rated **50–360 kW** (CCS and CHAdeMO); ambient temperature range −14 °C to 35 °C via ERA5 proxy. Sessions with <10% SoC change excluded from analysis; 9334 anomalous sessions (1.02%) removed after anomaly detection.
  - Splits: anomaly model train 810,765 / val 90,086; prediction model train 713,213 (Nov 2021–16 Jun 2024), test set one = 44,575 contemporaneous sessions, test set two = 44,578 sessions from 17 Jun–9 Jul 2024 (operational near-future scenario).
- **Data availability**: proprietary, under NDA with Shell; access restricted upon approved NDA — contact R.D. Source data provided with paper.
- **Code availability**: https://github.com/acses-l420/ev_charging_ml ; archived snapshot on Zenodo: https://doi.org/10.5281/zenodo.17183022 ; pretrained models on Zenodo: https://doi.org/10.5281/zenodo.17183746
- **Input features**: time series of [[Charging_Power]] and [[Battery_SOC]]; static covariates = starting SoC, [[Connector_Power_Rating]], [[Connector_Type]] (CCS/CHAdeMO, trainable embedding), estimated EV battery capacity (from energy delivered ÷ ΔSoC), ambient temperature from [[Weather]]. Logging at 60 s intervals; updates event-driven when reported SoC rises ≥1% (OCPP integer precision).

## 📈 Performance & Results
- **Duration prediction**: ~90% average relative accuracy from a single input point (MAE < 2.5 min); explains 91% of variance at n=1. With 6 points (≤5 min): >90% accuracy for 90% of sessions; headline result **95% relative accuracy, absolute error < 1 min**. At n=15 points only 1.45% of sessions fall below 90% accuracy, 0.79% below 80%. Errors converge to within ±5% relative / <1 min absolute.
- **Uncertainty**: share of high-uncertainty sessions (P10–P90 duration gap >20 min or >50% of median) drops from 15% (n=1) to <2% (n≥5). Persistent uncertainty flags residual anomalies at inference time.
- **Baselines/ablations (normalized MAE, combined test sets)**: TFT beats RNN, GRU, [[LSTM]], vanilla Transformer; also beats reduced variants VSN-LSTM (no attention/FFN) and pure Transformer (no recurrence) → attention and recurrence are complementary.
- **Feature ablations**: removing estimated capacity or ambient temperature degrades early-session accuracy most (capacity most influential per VSN importance, then connector power rating; temperature and connector type least but non-trivial). Binned capacity (4 classes) underperforms continuous capacity.
- **Generalisation**: comparable performance on held-out Netherlands data (no capacity covariate) vs UK/Germany test sets → robustness to geographic shift within W. Europe.

## 💡 Limitations & Identified Research Gaps
- Proprietary NDA-restricted dataset limits external replication; generalization beyond northwestern Europe / other climates may need new training data or transfer learning.
- 60-s charger logging interval and OCPP integer SoC precision bound effective temporal resolution; updates become sparse late in sessions.
- No cross-session user modelling/personalization (privacy constraints); future work suggests differential privacy or federated learning for user-level modelling.
- Potential extensions: forward simulator inside reinforcement-learning smart-charging control, charger assignment/load scheduling/dynamic pricing optimisation, more advanced uncertainty quantification for safety/cost-sensitive uses.

## 📚 BibTeX & Citation Reference
```bibtex
@article{li2025deep,
  title   = {Deep learning predicts real-world electric vehicle direct current charging profiles and durations},
  author  = {Li, Siyi and Zhang, Mingrui and Doel, Robert and Ross, Benjamin and Piggott, Matthew D.},
  journal = {Nature Communications},
  volume  = {16},
  pages   = {10921},
  year    = {2025},
  doi     = {10.1038/s41467-025-65970-y}
}
```

## 🔗 Key References & Citation Graph
- [[2021_TFT_Temporal_Fusion_Transformers]] — TFT architecture the workflow builds on (ref. 40)
- [[2022_RevIN_Reversible_Instance_Normalization]] — RevIN layers against distribution shift (ref. 41)
- [[2017_Attention_Is_All_You_Need]] — multi-head attention (ref. 31)
- [[2014_A_Method_for_Stochastic_Optimization]] — AdamW optimizer lineage (ref. 42)
