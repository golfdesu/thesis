---
type: paper
title: "Longformer: The Long-Document Transformer"
authors: [Iz Beltagy, Matthew E. Peters, Arman Cohan]
year: 2020
journal_conference: "arXiv preprint arXiv:2004.05150"
doi_url: "https://arxiv.org/abs/2004.05150"
status: metadata-verified-2026-08
tags:
  - paper
---
## 🎯 Main Objective & Contribution
- Solves the quadratic cost of full self-attention for long documents by introducing **Longformer**: a Transformer whose attention is a mixture of **local sliding-window, dilated sliding-window, and small global attention** patterns, scaling linearly with sequence length up to **4,096 tokens** (vs 512 for BERT).

## 🧠 Methodology & Model Architecture
- Sliding-window attention attends to $w$ neighbours per layer so information propagates across layers like a CNN stack; dilation widens receptive field without cost growth; a handful of task tokens (e.g., CLS, question tokens) receive **global** attention.
- Initialized from RoBERTa checkpoints and continued pretraining on long documents, making it drop-in for downstream NLP tasks; the attention implementation uses custom CUDA/Triton kernels.

## 📈 Performance & Results
- Matches or exceeds RoBERTa on character-level language modelling and long-document classification/QA benchmarks (arXiv, Hyperpartisan, TriviaQA, HotpotQA) while handling sequences up to 8x longer.

## 💡 Limitations & Identified Research Gaps
- Attention-pattern choice is task-specific (which tokens get global attention requires design); kernel engineering burden; motivated later efficient-attention lines relevant to long-sequence time-series Transformers (cf. [[FlashAttention]]).

## 📚 BibTeX & Citation Reference
- I. Beltagy, M. E. Peters, A. Cohan, "Longformer: The Long-Document Transformer," arXiv:2004.05150, 2020. Code: github.com/allenai/longformer
