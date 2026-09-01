---
type: paper
title: "Deep-Learning-Based Probabilistic Forecasting of Electric Vehicle Charging Load With a Novel Queuing Model"
authors: [Xian Zhang, Ka Wing Chan, Hairong Li, Huaizhi Wang, Jing Qiu, Guibin Wang]
year: 2021
journal_conference: "IEEE Transactions on Cybernetics, Vol. 51, No. 6, pp. 3157-3170"
doi_url: "https://doi.org/10.1109/TCYB.2020.2975134"
models_used: ["[[CNN]]", "[[Wavelet_Decomposition|Discrete Wavelet Transform (WT)]]", "[[GMM|Gaussian Mixture Model]]", "[[Queuing_Model|M/M/C/K Markov Queuing Model]]", "[[Ensemble_Stacking|CNN Ensemble PIs]]", "[[BPNN]]", "[[SVM]]", "[[SAE|Stacked Autoencoder (SAE)]]"]
datasets_used: ["[[M42_Motorway_Traffic_Flow]]", "[[UK_National_Travel_Survey]]", "[[NHTS_2009|2009 US National Household Travel Survey]]"]
features_used: ["[[Traffic]]", "[[Daily_Travel_Distance]]", "[[EV_Arrival_Rate]]", "[[State_of_Charge|State of Charge (SOC)]]", "[[Driver_Behavior]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAE]]", "[[RMSE]]", "[[MAPE]]", "[[PICP]]", "[[ACE]]", "[[Interval_Sharpness|IS]]", "[[Pinball_Loss|PL]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Deep-Learning-Based Probabilistic Forecasting of Electric Vehicle Charging Load With a Novel Queuing Model

## 🎯 Main Objective & Contribution
- First framework to forecast **EV charging station load probabilistically** by chaining: (1) deep-learning [[Traffic]] prediction with [[Prediction_Intervals|prediction intervals (PIs)]], (2) mixture-model-based EV arrival rate estimation, (3) a novel capacity-constrained $M/M/C/K$ [[Queuing_Model]] that converts TF → charging power while modeling **charging service limitations and three driver behaviors** (forced leave, refuse to join, impatient leave).
- Quantifies both **model uncertainty** ($\sigma_m^2$) and **data uncertainty** ($\sigma_d^2$) via a CNN ensemble to build reliable PIs at PINC = 90%, 95%, 99%.
- Supports multiple horizons: 1-h ahead (main), plus 6-h, 12-h, 18-h, and 24-h ([[Day_Ahead_Forecasting]]) multi-output forecasting.

## 🧠 Methodology & Model Architecture
Pipeline (Algorithm 1): normalize TF → wavelet decomposition per frequency → per-frequency CNN training → wavelet reconstruction → deterministic point forecast → PI construction from model+data uncertainty → arrival rate estimation → queuing-model load conversion.

### 1. Convolution Layer
$$y_j^l = f\left(\sum_{i \in M_j} x_i^{l-1} \otimes k_{ij}^l + b_j^l\right) \tag{Convolution}$$
with sigmoid activation $S(x)=1/(1+e^{-x})$, trained by backpropagation.

### 2. Pooling Layer (average pooling)
$$z_j^{l+1} = f\left(\beta_j^{l+1}\,\text{down}(y_j^l) + c_j^{l+1}\right), \qquad z_{i,j,k} = \sum_{p,q} \alpha_{p,q}\, y_{i+p,j+q,k} \tag{Pooling}$$

### 3. Wavelet Decomposition of TF signal $g(t)$ w.r.t. mother wavelet $\phi(x)$
$$W(m,n) = 2^{-(m/2)} \sum_{t=0}^{T-1} g(t)\,\phi\!\left(\frac{t - n2^m}{2^m}\right) \tag{DWT}$$
Decomposition into 1 approximation + 3 detail frequencies; each frequency gets its own CNN (4 conv layers, 2 pooling layers, 1 FC layer $y^l = K^l x^{l-1} + b^l$, 1 output layer); 36-h TF history is the input window.

### 4. Ensemble Regression & Uncertainty Decomposition
Estimated regression (ensemble mean over $N_E$ CNNs):
$$\hat{y}(x_i) = E[t_i|x_i] = \frac{1}{N_E}\sum_{q=1}^{N_E} \hat{y}_q(x_i) \tag{Ensemble Regression}$$
Model uncertainty variance:
$$\sigma_m^2(x_i) = \frac{1}{N_E-1}\sum_{q=1}^{N_E}\left(\hat{y}_q(x_i)-\hat{y}(x_i)\right)^2 \tag{Model Uncertainty}$$
Data uncertainty: a second set of $N_S$ CNNs regresses squared residuals $\hat{r}(x_i) = E[(\hat{y}(x_i)-t_i)^2|x_i]$; estimated noise variance and its own model variance:
$$\hat{\sigma}_d^2(t_i|x_i) = \frac{1}{N_S}\sum_{l=1}^{N_S}\hat{r}_l(x_i), \qquad \sigma_{\hat{r}}^2(x_i) = \frac{1}{N_S-1}\sum_{l=1}^{N_S}\left(\hat{r}_l(x_i)-\hat{r}(x_i)\right)^2$$
$$\sigma_d^2(x_i) = \hat{\sigma}_d^2(t_i|x_i) + \sigma_{\hat{r}}^2(x_i), \qquad \sigma_p^2(x_i) = \sigma_m^2(x_i) + \sigma_d^2(x_i) \tag{Total Variance}$$
PI bounds at nominal confidence PINC $=100(1-\alpha)\%$:
$$L^\alpha(x_i) = \hat{y}(x_i) - z_{1-\alpha/2}\sqrt{\sigma_p^2(x_i)}, \qquad U^\alpha(x_i) = \hat{y}(x_i) + z_{1-\alpha/2}\sqrt{\sigma_p^2(x_i)} \tag{PI Bounds}$$

### 5. GMM Arrival Rate Estimation
Mixture PDF with EM (K-means init; $M$ selected by AIC/BIC):
$$p(X|\Theta) = \sum_{m=1}^{M} \pi_m p_m(x_i|\theta_m), \quad 0\le\pi_m\le1,\;\sum_m\pi_m=1$$
$$\mathcal{L}(\Theta|X,Y) = \prod_{i=1}^N \sum_{m=1}^M y_{m,i}\pi_m p_m(x_i|\theta_m)$$
$$\text{AIC} = 2M - 2\ln\arg\max_\Theta \mathcal{L}(\Theta|X), \qquad \text{BIC} = M\ln(N) - 2\ln\arg\max_\Theta \mathcal{L}(\Theta|X)$$
EM steps: $Q(\Theta|\Theta^{(q)}) = E[\ln\mathcal{L}(\Theta|X,Y)\,|\,Y,\Theta^{(q)}]$, then $\Theta^{(q+1)}=\arg\max_\Theta Q(\Theta|\Theta^{(q)})$. Normal PDFs used as components.

SOC / travel-distance chain:
$$\text{SOC} = 1 - \frac{p_{ev} D_{ev}}{E_{ev}}, \qquad D_{ev,t}^T = \frac{E_{ev}(1-\text{SOC}_m)}{p_{ev}}\int_{t_0}^{t} g(h)\,dh$$
Probability of choosing to charge and arrival rate:
$$P_t = \int_{D_{ev,t-1}^T}^{D_{ev,t}^T} p(x)\,dx, \qquad \lambda_t = \varsigma P_t f_t$$
where $\varsigma$ is the EV penetration rate and $f_t$ the forecasted TF.

### 6. $M/M/C/K$ Queuing Model with Driver Behaviors
Poisson arrivals and exponential charging times:
$$P(n) = e^{-\lambda}\frac{\lambda^n}{n!}, \qquad f(t_c) = \mu e^{-\mu t_c}$$
- Refuse-to-join probability: $\alpha_w = 1$ if $w<C$; $\alpha_w = e^{-(w-C)\sigma}$ ($\sigma\ge0$) if $C\le w<K$; $0$ if $w=K$.
- Impatient-leave rate: $b_w = 0$ if $w\le C$; $b_w = \delta\ln(w-C+1)$ ($\delta\ge0$) if $C<w\le K$.
Adjusted rates: $\lambda_w = \alpha_w\lambda$, $\mu_w = \mu - b_w$.
Markov balance equation $(\lambda_w+\mu_w)P_w = \lambda_{w-1}P_{w-1} + \mu_{w+1}P_{w+1}$ yields steady-state probabilities ($\rho=\lambda/\mu$, $\eta=\delta/\mu$):
$$P_w = \begin{cases} \dfrac{\rho^w}{w!}P_0, & 0 < w \le C \\ \dfrac{e^{-\frac{(w-C)(w-C-1)}{2}\sigma}\rho^w}{C!\prod_{i=1}^{w-C}[C+\eta\ln(i+1)]}P_0, & C < w \le K \end{cases}$$
Number charging and FCS load:
$$N_{ch} = \sum_{w=0}^{C} wP_w + C\sum_{w=C+1}^{K} P_w, \qquad P_{\text{FCS}} = N_{ch}\, p^{EV}$$

## 📊 Dataset & Input Features
- **[[M42_Motorway_Traffic_Flow]]**: real TF between sites J5–J6 (GPS Ref: 417049:278576–419805:283048), M42 motorway, England, U.K.; **15-min resolution**, Jan–Dec 2014; first 2 months of each season = training, remaining month = testing; 36-h TF input window; hourly averages of four 15-min intervals used.
  - Data URL: http://tris.highwaysengland.co.uk/download/721b4186-feab-4691-94a0-2ded8f3ea94f (Highways England Traffic Flow Data)
- **[[UK_National_Travel_Survey]]**: trips-in-progress distribution $g(t)$ by time of day (U.K. Dept for Transport).
  - URL: https://www.gov.uk/government/uploads/system/uploads/attachment_data/file/79153/nts0501.xls
- **[[NHTS_2009|2009 National Household Travel Survey]]**: daily travel distance distribution source (U.S. DOT, Rep. FHWA-PL-11022).
- Simulated FCS parameters: rated power $P_{\text{FCS}}^r = 0.88$ MW, $C=22$ chargers @ $p^{EV}=40$ kW, capacity $K=30$ EVs, mean charging time $t_c=20$ min, penetration $\varsigma=20\%$, $\sigma=1$, $\delta=1$.
- Features: raw TF series, daily travel distance $D_{ev}^T$, SOC condition, driver-behavior parameters.

## 📈 Performance & Results
Deterministic 1-h ahead TF forecast (spring): **WT-CNN: MAE = 93.42, RMSE = 118.32, MAPE = 3.29%** vs BPNN (296.59 / 416.69 / 10.56%), SVM-RBF (229.81 / 341.55 / 8.18%), SAE (265.67 / 382.40 / 9.46%) — errors roughly half those of all six benchmarks (also TDNN, growing DBN, RNN).
Probabilistic 1-h ahead (PINC = 95%): CNN PICPs of **95.49%, 95.24%, 95.47%, 95.24%** across four seasons; ACE < 1% in all seasons (~half of QR benchmark, e.g., QR ACE = 3.89%); smallest absolute IS (28.64 spring / 23.91 summer at PINC 99%) and lowest [[Pinball_Loss|PL]] among all methods and vs quantile regression at PINC 90/95/99%.
Multi-horizon: reliable 6-h/12-h/18-h/**24-h ahead** PIs (Table IV) via single-output→24-output CNN adjustment.
Charging load: strong Pearson/Kendall/Spearman correlation with TF (all coefficients 0.8–1) but nonlinear queuing transformation means trend differences must not be neglected; load increases with $C$/$K$ and decreases with larger refuse-to-join $\sigma$ or impatient-leave $\delta$ (most pronounced at rush hour).

## 💡 Limitations & Identified Research Gaps
- Charging load validated on a **simulated FCS** driven by real TF — no measured charging-session data; queuing parameters ($\sigma$, $\delta$, $\varsigma$) assumed rather than empirically fitted.
- Single-station scope (one motorway segment); no spatial generalization across networks.
- Driver behavior modeled via stylized exponential/logarithmic heuristics; no price-responsive or dynamic behavioral adaptation.
- PI construction assumes Gaussian error structure via $z_{1-\alpha/2}$ critical values; no nonparametric quantile learning.
- Gap for thesis: combining this traffic-to-power physical conversion with end-to-end probabilistic deep models ([[TimeGrad]], [[Temporal_Fusion_Transformer]]) remains open.

## 📚 BibTeX & Citation Reference
```bibtex
@article{zhang2021probabilistic,
  title={Deep-Learning-Based Probabilistic Forecasting of Electric Vehicle Charging Load With a Novel Queuing Model},
  author={Zhang, Xian and Chan, Ka Wing and Li, Hairong and Wang, Huaizhi and Qiu, Jing and Wang, Guibin},
  journal={IEEE Transactions on Cybernetics},
  volume={51},
  number={6},
  pages={3157--3170},
  year={2021},
  doi={10.1109/TCYB.2020.2975134}
}
```

## 🔗 Key References & Citation Graph
- Foundation: Mallat's multiresolution wavelet theory [26]; Dempster–Laird–Rubin EM algorithm [31]; Kendall queuing notation via Khinchine [8].
- Related vault concepts: [[Queuing_Model]], [[Prediction_Intervals]], [[Traffic]], [[GMM]], [[PICP]]
- Comparable baselines in vault: [[2017_Attention_Is_All_You_Need]] (attention alternatives to CNN ensembles)
- Follow-up direction: probabilistic EV load forecasting feeding [[Short_Term_Forecasting]] dispatch decisions.

## Extracted Reference Dump
Full extracted bibliography for this paper: [[2021_Zhang_Probabilistic_Queuing_EV_Load_refs]]
