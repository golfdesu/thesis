---
type: paper
title: "Optimal learning with Bernstein Online Aggregation"
authors: [Olivier Wintenberger]
year: 2017
journal_conference: "Machine Learning 106(1):119-141"
doi_url: "https://doi.org/10.1007/s10994-016-5592-6"
status: metadata-verified-2026-08
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Formalises **Bernstein Online Aggregation (BOA)**: exponentially weighted aggregation of experts whose weights depend on cumulative losses **and their variance**, yielding sharp second-order regret bounds of Bernstein type rather than the looser first-order/Hoeffding bounds of classical exponential-weights forecaster.

## 🧠 Methodology & Model Architecture
- Given experts' sequential predictions, BOA mixes them with weights proportional to $\exp(-\eta \sum \ell + \nu \sum \ell^2)$-type quantities, adaptively balancing each expert's cumulative loss and its variability; works under exp-concave, convex, and bounded losses with appropriate learning-rate schedules.
- Implemented in the R package **`opera`** (Gaillard et al.), the standard toolkit behind French load forecasting aggregations (GEFCom lineage).

## 📈 Performance & Results
- Proves optimal second-order regret rates and demonstrates on synthetic + real sequences that variance-aware weighting adapts faster to changing expert quality than uniform exponential weights.

## 💡 Limitations & Identified Research Gaps
- Bound constants depend on loss curvature/exp-concavity assumptions; extension to fully adversarial heavy-tailed losses and to quantile-loss-specific variants (used in [[Gaillard2016_GEFCOM2014_Aggregation]]) required bespoke analysis.

## 📚 BibTeX & Citation Reference
- O. Wintenberger, "Optimal learning with Bernstein Online Aggregation," *Machine Learning*, 106(1):119-141, 2017. DOI:10.1007/s10994-016-5592-6
