---
type: dataset
name: "GIFT-Eval Pretrain"
location: "Large companion pretraining corpus (non-overlapping with GIFT-Eval eval)"
resolution: "Mixed"
access: "open - https://huggingface.co/datasets/Salesforce/GiftEvalPretrain"
tags: [dataset, pretraining-corpus, gift-eval]
---

# GIFT-Eval Pretrain

Large companion pretraining corpus curated to not overlap with GIFT-Eval evaluation datasets (Aksu et al. 2024c). Used as 45%% of Toto 2.0 2.5B-FT finetuning mix (with Chronos corpus subset, non-leaking).

## Literature Usage
- [[2025_TiRex_Zero_Shot_Forecasting_In_Context_Learning]] — Included 2.5 million time series from `Salesforce/GiftEvalpre-train` (sampled at 8% rate) in the 47.5M pretraining corpus.
- [[2026_Toto_2_Scaling_Era]] — 45%% of 2.5B-FT finetuning mix (10k steps from decayed checkpoint); combined with GIFT-Eval train (15%%, official train splits), Datadog 5+m (25%%), synthetic (10%%), 10s/60s (2.5%% each).
- [[2025_Chronos_2_Univariate_to_Universal]] — GIFT-Eval pretraining corpus (Aksu et al. 2024) partially in Chronos-2 real-univariate mix; test portions carefully excluded.
- [[2026_Moirai_2_When_Less_Is_More]] — Used as pretraining/evaluation data (Moirai 2.0): see paper §4 & Fig. 2–5, Table 1–2. GIFT-Eval 97 tasks (55 datasets) for evaluation; GIFT-Eval Pretrain (3.25M/230B) as pretrain foundation; Chronos-Mixup (30M/63B) & KernelSynth (1M/1.02B) as synthetic augmentation; internal Salesforce telemetry (2.15M/1.48B daily) as proprietary source. Normalized MASE/CRPS via gift-eval replication code.
