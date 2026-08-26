---
type: paper
title: "A review on artificial intelligence based load demand forecasting techniques for smart grid and buildings"
authors: [Muhammad Qamar Raza, Abbas Khosravi]
year: 2015
journal_conference: "Renewable and Sustainable Energy Reviews, vol. 50, pp. 1352-1372"
doi_url: "https://doi.org/10.1016/j.rser.2015.04.065"
models_used: ["[[ANN]]", "[[MLP]]", "[[ANN]]", "[[Fuzzy_Logic]]", "[[ANFIS]]", "[[SVM]]", "[[SVR]]", "[[Wavelet_Neural_Network|WNN]]", "[[Artificial_Immune_System|AIS]]", "[[Genetic_Algorithm|GA]]", "[[Particle_Swarm_Optimization|PSO]]", "[[Ant_Colony_Optimization|ACO]]"]
datasets_used: ["[[ISO_New_England_Grid]]", "[[California_Grid]]", "[[New_York_Grid]]", "[[Singapore_Grid]]", "[[ELIA_Belgian_Grid]]", "[[Ontario_Grid]]", "[[Victoria_Australia_Grid]]", "[[UK_National_Grid]]"]
features_used: ["[[Historical_Load]]", "[[Temperature]]", "[[Dew_Point]]", "[[Temperature]]", "[[Humidity]]", "[[Calendar_Features]]", "[[Calendar_Features]]", "[[Holiday_Flag]]", "[[Electricity_Tariff]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[MAPE]]", "[[RMSE]]", "[[MAE]]", "[[MSE]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: A Review on AI-Based Load Demand Forecasting Techniques for Smart Grid and Buildings

## 🎯 Main Objective & Contribution
- Comprehensive, systematic literature review of **[[Artificial_Intelligence|AI]]-based short-term load forecasting (STLF)** techniques for [[Smart_Grid|smart grids]] and smart buildings (RSER 2015; ~1,760+ citations).
- Classifies STLF techniques into **parametric/statistical** (time series, linear regression, ARMA/ARIMA, general exponential smoothing) vs. **non-parametric/AI** ([[ANN]], fuzzy logic, SVM), then surveys six families of **hybrid ANN** techniques.
- Key thesis: ANN forecast accuracy is governed by network architecture, input combination, activation function, training algorithm, and exogenous variables; hybrid/population-based training consistently outperforms plain gradient-descent backpropagation.
- Establishes a taxonomy of load forecasting horizons: long-term (1–10 yr), medium-term (1 month–1 yr), short-term (1 h to 1 week ahead); STLF dominates the literature due to unit commitment, spinning reserve, and contract evaluation applications.

## 🧠 Methodology & Model Architecture
Survey covers the full mathematical apparatus of classical neural load forecasters:

**Neuron output (Equation 5)** — weighted sum passed through activation $g$:
$$A_i = g\left(\sum_{i=0}^{n} W_{ij}\, a_j\right)$$

**Normalization formulas (Equations 1–4)** — min-max, sum, max, and mean-based scaling of load inputs:
$$\text{Normalized\_load} = \frac{X - X_{min}}{X_{max} - X_{min}}, \quad \frac{X}{X_{sum}}, \quad \frac{X}{X_{max}}, \quad \frac{X - X_{avg}}{X_{max} - X_{avg}}$$

**Supervised I/O relation (Equation 6):**
$$[\,y_1, y_2, \dots, y_m\,] = [\,x_1, x_2, \dots, x_m\,]^{\eta+\varepsilon}$$
where $\varepsilon$ is the approximation error vector between network output and targets.

**Mean square error objective (Equation 7)** — learning threshold typically set at $1\times10^{-3}$:
$$E(t) = \frac{1}{N}\sum_{i=1}^{N}\left(O_i^T(t) - O_i(t)\right)^2$$

**Back-propagation forward pass (Equations 8–11)** — hidden-layer input/output and output-layer input/output:
$$L_{m_k} = D_{o_j} + \sum_{i=1}^{n} x_i D_{ij}, \qquad L_j = f(L_m)$$
$$G_{in_k} = W_{o_k} + \sum_{j=1}^{p} L_j W_{jk}, \qquad G_k = f(G_{in_k})$$

**Error back-propagation and weight updates (Equations 12–20)** with learning rate $\alpha$:
$$\delta_k = (T_k - G_k)\, f(G_{in_k}), \qquad \Delta W_{jk} = \alpha \delta_k L_j, \qquad \Delta W_{ok} = \alpha \delta_k$$
$$\delta_{in_j} = \sum_{k=1}^{m} \delta W_{jk}, \qquad \delta_j = \delta_{in_j}\, f(L_{m_k}), \qquad \Delta D_{ij} = \alpha \delta_i x_i, \qquad \Delta D_{oj} = \alpha \delta_j$$
$$w_{jk}^{new} = w_{jk}^{old} + \Delta w_{jk}, \qquad o_{ij}^{new} = o_{ij}^{old} + \Delta V_{ij}$$

**Transfer functions surveyed (Table 3):** unipolar/bipolar step, unipolar/bipolar linear, unipolar sigmoid $f(x)=1/(1+e^{-x})$, bipolar sigmoid $\tanh(x)$, Gaussian RBF $f(x)=\exp(-\|x-m\|^2/\sigma^2)$.

**Master control agent objective functions** for the conceptual smart power network:
$$\text{Overall\_Power\_Supply} = \max \sum_{i=1}^{h} w(h)\, n_{power\_supply(h)}, \qquad \text{Overall\_demand} = \min \sum_{i=1}^{h} w(h)\, n_{Demand(h)}$$

**Architecture taxonomy:** feedforward vs. feedback (recurrent) networks; supervised vs. unsupervised learning; MLP with hidden layers as the workhorse for STLF. Documented BP pathologies: local minima, network paralysis, temporal instability, poor generalization/overfitting. Also describes a 3-level microgrid control hierarchy (primary/secondary/tertiary per IEC/ISO 62264).

## 📊 Dataset & Input Features
No single dataset; the review's worked examples and surveyed case studies use public utility grids:
- **ISO New England**: 6 years hourly load (2004–09) shown for seasonality analysis; 4 years (2005–08) hourly load + weather used to train NNs, 2009 held out for testing (per Shamsollahi et al., ISO-NE interim market forecaster). Hourly resolution.
- Surveyed case studies include: California grid and New York load (Sfetsos clustering hybrid), Cyprus grid (similar-shape functional time series), Singapore grid (ARIMA/decomposition, MAPE 3.40%), Belgian ELIA grid >40,000 time-series points (periodic PAR model, 24 h & 168 h ahead), Ontario Canada grid (2004–06 LM-BP NN, 75%/25% train/test split), Victoria Australia grid (GRNN/PNN with price inputs), UK grid profiles (working vs. weekend patterns).
- No data availability URLs are stated in the paper itself; only reference DOI http://dx.doi.org/10.1109/CCECE.2000.849691 (Bashir & El-Hawary WNN paper) appears in the reference list.
- **Input features distilled from the literature**: previous correlated loads $L_d(w,d,h)$, $L_d(w,d,h-1)$, $L_d(w,d-1,h)$, $L_d(w-1,d,h)$; day type (working/off/special); day pointer $D(k)$ and hour pointer $H(k)$; dry-bulb temperature, dew point, relative humidity, wind speed, cloud cover, human body index; electricity price in deregulated markets.

## 📈 Performance & Results
Representative quantitative findings compiled across ~60 surveyed studies:
- Hooshmand et al. WT+ANN+ANFIS hybrid (24 h horizon): **MAPE 1.703%**.
- LOFY expert system: MAPE 1.86% (daily), 1.64% (ordinary days), 2.0% (weekdays).
- Mori & Kosemura MLP + globally optimal regression tree: error reduced **7.17% → 5.20%** vs MLP.
- Heru et al. RBF + fuzzy expert system: max weekly MAPE 2.09%, average 1.58%.
- Sfetsos clustered regression+ANN: **7.54% improvement** (California, 12 clusters), **9.88%** (New York, 8 clusters).
- Wu et al. SEAM + regression: min MAPE 4.88%; Tripathi et al. GRNN/PNN with prices: min MAPE 1.85%.
- Du Tao et al. wavelet multiresolution + ANN: monthly error 1.90–2.24%, daily 1.65–2.17%.
- Abu-El-Magd time series + ANN: MRPE 2.07% incl. holidays; Espinoza periodic PAR (ELIA): min error ~3%.
- Amjady modified ARIMA: holiday MAPE 1.98%; Chen et al. SVR (EUNITE 2001 winner): MAPE 1.95%; DE-SVR: 1.8%; ACO-SVM: 1.98%; Dudek AIS: 1.77%.
- GA vs PSO trained MLP: GA MAPE 3.19% (slow) vs PSO 4.25% (fast); NFN+improved-GA: **1.56%**; GANN: 2.867%; LM-BP peak-load NN: 2.87%; Bashir & El-Hawary WNN converged in **750 epochs vs 2500** for plain ANN.
- Hybrid AIS training converged in **6 iterations / 21 datasets** vs 150 iterations / 36 datasets for GA and PSO.

## 💡 Limitations & Identified Research Gaps
- Backpropagation-trained ANNs suffer dependence on initial weights, slow convergence, high computational cost, local minima, and weak generalization.
- Statistical/time-series methods degrade sharply under abrupt weather or calendar changes.
- Identified gaps: richer meteorological inputs (humidity, wind, rainfall, body index); heuristic/evolutionary hybrid training; automated optimization of architecture and transfer function selection; electricity price as an exogenous input; dynamic fuzzy-driven input selection per horizon; integration into smart-grid/building demand-side management. Notes power systems contribute ~32% of total CO₂ emissions, motivating accurate forecasting.
- Pre-dates deep learning and EV-specific forecasting entirely — no sequence models, probabilistic outputs, or charging-station studies.

## 📚 BibTeX & Citation Reference
```bibtex
@article{raza2015review,
  title={A review on artificial intelligence based load demand forecasting techniques for smart grid and buildings},
  author={Raza, Muhammad Qamar and Khosravi, Abbas},
  journal={Renewable and Sustainable Energy Reviews},
  volume={50},
  pages={1352--1372},
  year={2015},
  publisher={Elsevier},
  doi={10.1016/j.rser.2015.04.065}
}
```

## 🔗 Key References & Citation Graph
- Foundational ANN survey lineage: [[2001_Hippert_Neural_Networks_STLF_Review]]
- Successor probabilistic/combinatorial methods: [[2017_Liu_QRA_Sister_Forecasts_Probabilistic_Load]]
- Modern deep successors replacing shallow ANNs: [[1997_Hochreiter_Long_Short_Term_Memory]], [[2018_Bai_Empirical_TCN_Sequence_Modeling]], [[2017_Attention_Is_All_You_Need]]
