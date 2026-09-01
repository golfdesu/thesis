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
- [[2026_Khwaja_Toto_2_Scaling_Era]] — 45%% of 2.5B-FT finetuning mix (10k steps from decayed checkpoint); combined with GIFT-Eval train (15%%, official train splits), Datadog 5+m (25%%), synthetic (10%%), 10s/60s (2.5%% each).
- [[2025_Ansari_Chronos_2_Univariate_to_Universal]] — GIFT-Eval pretraining corpus (Aksu et al. 2024) partially in Chronos-2 real-univariate mix; test portions carefully excluded.
