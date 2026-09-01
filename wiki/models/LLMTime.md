---
type: model
name: "LLMTime"
category: Deep Learning / LLM-as-Forecaster (Prompting)
tags:
  - model
  - llm
  - foundation-model
  - zero-shot
---

# LLMTime

## Overview
LLMTime (Gruver et al., NeurIPS 2023, arXiv:2310.07820) repurposes frozen LLMs (GPT-3 / GPT-3.5-Turbo, LLaMA-2) as zero-shot time-series forecasters via tokenization + prompting. No time-series pretraining — relies on LLM text pretraining. Used as key zero-shot baseline in [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]].

## Literature Usage
- [[2024_Das_TimesFM_Decoder_Only_Foundation_Model]] — Baseline beaten by TimesFM by >25% on Monash (GM scaled MAE 0.9715 vs 0.6846), significantly worse on ETT, and within significance only on small Darts; also noted as potentially data-contaminated on public series. Illustrates that foundation models trained from scratch on time-series data outperform LLM prompting at a tiny fraction of cost.
- [[2025_Meyer_Benchmark_Foundation_Models]] — Discussed as LLM-based forecasting precedessor category.

- [[2025_Liu_Sundial_Highly_Capable_Time_Series_Foundation_Models]]
