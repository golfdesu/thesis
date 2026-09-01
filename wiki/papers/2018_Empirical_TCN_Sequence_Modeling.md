---
type: paper
title: "An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling"
authors: [Shaojie Bai, J. Zico Kolter, Vladlen Koltun]
year: 2018
journal_conference: "arXiv preprint arXiv:1803.01271 (presented as a generic-architecture evaluation; CMU / Intel Labs)"
doi_url: "https://arxiv.org/abs/1803.01271"
models_used: ["[[TCN]]", "[[LSTM]]", "[[GRU]]", "[[RNN]]", "[[EURNN]]", "[[TCN|TCN+Gating]]"]
datasets_used: ["[[Adding_Problem]]", "[[MNIST]]", "[[MNIST]]", "[[Copy_Memory]]", "[[JSB_Chorales]]", "[[Nottingham]]", "[[Penn_Treebank]]", "[[Wikitext-103]]", "[[LAMBADA]]", "[[text8]]"]
features_used: ["[[Raw_Sequence_Input]]", "[[Dilation_Factor]]", "[[Transformer]]", "[[Weight_Normalization]]", "[[Spatial_Dropout]]"]
forecasting_horizon: "[[Short_Term_Forecasting]]"
metrics: ["[[Accuracy]]", "[[MSE]]", "[[NLL|NLL]]", "[[Perplexity]]", "[[Bits_Per_Character|bpc]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling

## 🎯 Main Objective & Contribution
- The most extensive systematic comparison of **generic convolutional vs. recurrent architectures** for sequence modeling, run on RNNs' "home turf": the standard stress tests and music/language benchmarks used to evaluate LSTM/GRU variants themselves.
- Introduces a deliberately simple generic **[[TCN|Temporal Convolutional Network (TCN)]]**: `TCN = 1D fully-convolutional network + causal convolutions`, augmented with dilated convolutions for exponentially large receptive fields and residual blocks.
- Central findings: TCNs **convincingly outperform canonical LSTMs/GRUs across a diverse task suite**, exhibit **substantially longer effective memory** in practice (the "infinite memory" advantage of RNNs is largely absent), are simpler, parallelizable, and have stable gradients — concluding that convolutional networks should be the default starting point for sequence modeling.
- Directly motivates TCN-based EV charging load forecasters (e.g., [[2024_MQ_TCN_Transfer_Learning_EV]]).

## 🧠 Methodology & Model Architecture
**Sequence modeling formalism (Equation 1):** any network $f: \mathbb{X}^{T+1} \rightarrow \mathbb{Y}^{T+1}$ producing
$$\hat{y}_0, \dots, \hat{y}_T = f(x_0, \dots, x_T)$$
subject to the **causal constraint**: $y_t$ may depend only on $x_0,\dots,x_t$, never on future inputs $x_{t+1},\dots,x_T$. Trained by minimizing expected loss $L(y_0,\dots,y_T, f(x_0,\dots,x_T))$.

**Causal convolutions:** output at time $t$ convolves only with elements from time $t$ and earlier in the previous layer; zero padding of length (kernel size − 1) keeps all hidden layers the same length as the input.

**Dilated causal convolution (Equation 2)** — for 1-D input sequence $\mathbf{x} \in \mathbb{R}^n$ and filter $f:\{0,\dots,k-1\}\rightarrow\mathbb{R}$:
$$F(s) = (\mathbf{x} *_d f)(s) = \sum_{i=0}^{k-1} f(i) \cdot \mathbf{x}_{s-d\cdot i}$$
where $d$ is the dilation factor and $k$ the filter size; effective history per layer is $(k-1)d$. Dilation increases exponentially with depth ($d = O(2^i)$ at level $i$), yielding an exponentially large receptive field with depth $n$.

**Residual block (Equation 3)** — each block contains two layers of dilated causal convolution + ReLU, weight normalization on filters, and spatial dropout (whole channel zeroed per training step); a 1×1 convolution aligns input/output widths:
$$\mathbf{o} = \text{Activation}(\mathbf{x} + F(\mathbf{x}))$$

**Training setup:** identical generic TCN across all tasks, varying only depth $n$ and occasionally kernel $k$ to cover required context; Adam optimizer, learning rate 0.002, exponential dilation $d = 2^i$; gradient clipping threshold picked from [0.3, 1] (helped convergence on large tasks); weights initialized from $\mathcal{N}(0, 0.01)$; RNN baselines grid-searched over optimizer ∈ {SGD, Adam, RMSprop, Adagrad}, dropout p ∈ [0.05, 0.5], learning rate, clipping, forget-gate bias at matched model sizes.

**Claimed advantages:** full train/test parallelism (vs. sequential RNN steps), flexible receptive field via k/d/depth, stable gradients (backprop path not along time axis → no exploding/vanishing gradients), low training memory, variable-length inputs. **Disadvantages:** raw-sequence storage needed at evaluation (RNNs keep only fixed-length state $h_t$); receptive field may need re-tuning when transferring across domains.

## 📊 Dataset & Input Features
All inputs are raw sequences (targets = shifted inputs for autoregressive tasks); no exogenous covariates.
- **Synthetic stress tests**: Adding problem (length-$n$ depth-2 sequences in [0,1]; trivial MSE baseline ≈ 0.1767); Sequential MNIST (784×1 pixel sequences) and P-MNIST (permuted order); Copy memory (length $T+20$, recall 10 digits after delimiter; T up to 2000).
- **Polyphonic music**: JSB Chorales (entire corpus of **382 four-part Bach chorales**, 88-bit piano-roll encoding); Nottingham (**1,200** British/American folk tunes). Scored by NLL.
- **Word-level language modeling**: Penn Treebank (**888K train / 70K val / 79K test words**, 10K vocab); Wikitext-103 (~110× PTB: **103M words**, 268K vocab, 28K Wikipedia articles train); LAMBADA (10K novel passages, avg 4.6 context sentences + target word; training text of **2,662 novels > 200M words**, ~93K vocab). Scored by perplexity.
- **Character-level language modeling**: PTB char (**5,059K train chars**, alphabet 50); text8 (**100M characters** from Wikipedia, 90M/5M/5M split, 27 symbols). Scored in bpc.
- **Code availability (stated in paper)**: http://github.com/locuslab/TCN ; preprint https://arxiv.org/abs/1803.01271

## 📈 Performance & Results
Synopsis table (TCN vs LSTM / GRU / vanilla RNN, matched sizes):
- **Seq. MNIST accuracy**: TCN **99.0** vs GRU 96.2, LSTM 87.2, RNN 21.5. **P-MNIST**: TCN **97.2** vs GRU 87.3, LSTM 85.7 — beats recurrent SoTA (95.9%, Zoneout + Recurrent BatchNorm).
- **Adding problem (T=600 loss)**: TCN **5.8e-5** ≈ regularized GRU 5.3e-5; LSTM fails at 0.164.
- **Copy memory (T=1000 loss)**: TCN **3.5e-5** vs EURNN 0.011 (SoTA recurrent), LSTM 0.0204, GRU 0.0197 (both collapse to the all-zeros guess); TCN holds **100% recall accuracy at all T**, while LSTM drops below 20% accuracy for T < 50 and GRU below 20% for T < 200.
- **Music NLL**: JSB Chorales TCN **8.10** vs GRU 8.43, LSTM 8.45; Nottingham TCN **3.07** vs LSTM 3.29.
- **Language modeling**: Wiki-103 ppl TCN **45.19** < Grave et al. LSTM 48.4; LAMBADA ppl TCN **1279** vs LSTM 4186 (with smaller network, no tuning); word-level PTB is the exception where an optimized AWD-LSTM (78.93 ppl) beats the untuned TCN (88.68); char-level PTB bpc TCN **1.31** vs LSTM 1.36, text8 **1.45** vs 1.50.
- **Ablations**: larger kernels help memory-heavy tasks (copy memory/P-MNIST; k ≤ 3 converges to random guessing on copy memory) while k=3 is best for local-context word-level PTB; residual connections stabilize training and substantially improve final results everywhere; gating (GLU) only helps slightly on some language tasks (PTB ppl 87.94 vs 88.68) and *hurts* long-memory tasks (copy memory 0.00508 vs 3.5e-5).

## 💡 Limitations & Identified Research Gaps
- On small corpora (word PTB, JSB Chorales), specialized heavily-tuned LSTM variants still win; authors attribute this to regularization/generative tricks orthogonal to the TCN-vs-RNN axis and call for equivalent community investment in TCN tuning.
- TCNs must retain raw history up to receptive-field length during evaluation — potentially higher inference memory than an RNN's fixed hidden state.
- Receptive field (k, d) is domain-dependent: transferring a short-memory configuration to a long-memory domain degrades performance — precisely the gap later addressed by adaptive-receptive-field EV forecasting models ([[2024_MQ_TCN_Transfer_Learning_EV]], multi-quantile transfer).
- No probabilistic outputs, no covariates, no multi-horizon forecasting protocol — pure sequence-modeling benchmark; adoption for day-ahead EV load forecasting required later architectural extensions (dilated skip connections, quantile heads).

## 📚 BibTeX & Citation Reference
```bibtex
@article{bai2018tcn,
  title={An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling},
  author={Bai, Shaojie and Kolter, J. Zico and Koltun, Vladlen},
  journal={arXiv preprint arXiv:1803.01271},
  year={2018},
  url={https://arxiv.org/abs/1803.01271}
}
```

## 🔗 Key References & Citation Graph
- Recurrent baselines built on [[1997_Long_Short_Term_Memory]]
- Convolutional-vs-attention alternative for sequences: [[2017_Attention_Is_All_You_Need]]
- Transformer-era successors questioning both families: [[2023_DLinear_Are_Transformers_Effective_LTSF]], [[2023_PatchTST_A_Time_Series_is_Worth_64_Words]]
- EV-charging descendants in vault: [[2024_MQ_TCN_Transfer_Learning_EV]]
