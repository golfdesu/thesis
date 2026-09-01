---
type: paper
title: "Long Short-Term Memory"
authors: [Sepp Hochreiter, Jürgen Schmidhuber]
year: 1997
journal_conference: "Neural Computation, 9(8), 1735-1780"
doi_url: "https://doi.org/10.1162/neco.1997.9.8.1735"
models_used: ["[[LSTM]]", "[[RNN]]", "[[BPTT]]", "[[RTRL]]", "[[RNN]]", "[[Recurrent_Cascade_Correlation]]"]
datasets_used: ["[[Embedded_Reber_Grammar]]", "[[Synthetic_Long_Time_Lag_Benchmarks]]", "[[Adding_Problem]]", "[[Multiplication_Problem]]", "[[Temporal_Order_Problem]]"]
features_used: ["[[LSTM]]", "[[LSTM]]", "[[LSTM]]", "[[LSTM]]", "[[LSTM]]"]
forecasting_horizon: "[[Long_Term_Forecasting]]"
metrics: ["[[Classification_Error]]", "[[MSE]]", "[[Absolute_Error]]"]
tags: [paper, ev-load-forecasting, ml]
---

# Summary: Long Short-Term Memory

## 🎯 Main Objective & Contribution
- Introduces **Long Short-Term Memory ([[LSTM]])**, a novel recurrent architecture + gradient-based learning algorithm that overcomes the **vanishing/exploding gradient** problem of [[BPTT]] and [[RTRL]] (error signals flowing backward in time blow up or vanish exponentially depending on weight magnitudes; Hochreiter 1991 analysis).
- Enables bridging **minimal time lags in excess of 1000 discrete-time steps**, even with noisy, incompressible input sequences, by enforcing **constant error flow** through **constant error carousels (CEC)** inside special memory cells; multiplicative **gate units** learn to open/close access to the CEC.
- Complexity per time step and weight is $O(1)$ (update complexity $O(W)$); LSTM is **local in space and time**. Solves artificial long-time-lag tasks never solved by prior RNN algorithms; outperforms RTRL, BPTT, recurrent cascade-correlation, Elman nets, and neural sequence chunking in success rate and speed.

## 🧠 Methodology & Model Architecture
### Vanishing-error analysis (Section 3)
- Backpropagated error signal of nonoutput unit $j$ (Error Backpropagation Rule):
$$\vartheta_j(t) = f_j'(net_j(t)) \sum_i w_{ij}\,\vartheta_i(t+1), \qquad net_i(t) = \sum_j w_{ij} y_j(t-1)$$
- **Error scaling factor over $q$ steps** (Eq. 3.1 / 3.2):
$$\frac{\partial \vartheta_v(t-q)}{\partial \vartheta_u(t)} = \sum_{l_1=1}^{n}\cdots\sum_{l_{q-1}=1}^{n} \prod_{m=1}^{q} f'_{l_m}(net_{l_m}(t-m))\, w_{l_m l_{m-1}}$$
If all factors exceed 1.0 the error blows up; if below 1.0 it vanishes. With logistic sigmoids ($f'_{max}=0.25$), error flow decays whenever $|w| < 4.0$. Weak upper bound:
$$\left|\frac{\partial \vartheta_v(t-q)}{\partial \vartheta_u(t)}\right| \le n\,(f'_{max}\,\|W\|_A)^q = n\,\tau^q, \quad \tau := \frac{n\,w_{max}}{4.0} < 1$$
- **Naive constant error condition**: require $f_j'(net_j(t))\,w_{jj} = 1.0$, forcing linear activation $f_j(x)=x$ and fixed self-weight $w_{jj}=1.0$ — the **constant error carousel (CEC)**: $y_j(t+1)=y_j(t)$.
- Two conflicts motivate gates: **input weight conflict** (same incoming weight used for storing vs. protecting inputs) and **output weight conflict** (same outgoing weight used for retrieval vs. protection).

### LSTM architecture (Section 4)
- Memory cell $c_j$ = central linear self-connected unit (CEC) plus multiplicative **input gate** $in_j$ and **output gate** $out_j$. Gates:
$$net^{in}_j(t) = \sum_u w^{in}_{ju} y_u(t-1), \qquad net^{out}_j(t) = \sum_u w^{out}_{ju} y_u(t-1), \qquad net_{c_j}(t) = \sum_u w_{c_j u} y_u(t-1)$$
- **Internal state update (CEC / State Update)**:
$$s_{c_j}(0)=0, \qquad s_{c_j}(t) = s_{c_j}(t-1) + y^{in}_j(t)\, g(net_{c_j}(t))$$
- **Cell output (gated read)**:
$$y_{c_j}(t) = y^{out}_j(t)\, h(s_{c_j}(t))$$
- Activation functions used: gate sigmoid (Eq. A.1) $f(x)=\frac{1}{1+e^{-x}}\in[0,1]$; $h$ (Eq. A.2) $\in[-1,1]$; $g$ (Eq. A.3) $\in[-2,2]$. No forget gate in the 1997 version; memory cell blocks of size $S$ share one input/output gate pair.
- **Truncated learning**: errors arriving at memory-cell net inputs are NOT propagated further back in time; only within cells do errors backpropagate through internal states ($s_{c_j}$). Only derivatives $\partial s_{c_j}/\partial w_{lm}$ need storage/update.
- Squared error and weight update (Eqs. A.14–A.16):
$$E(t) = \sum_{k \text{ output}} (t_k(t)-y_k(t))^2, \qquad {}^1w_{lm}(t) = -\alpha\,\frac{\partial E(t)}{\partial w_{lm}}, \qquad e_l(t) := -\frac{\partial E(t)}{\partial net_l(t)}$$
- Internal-state error (Eq. A.21) proving gated constant flow:
$$e_{s_{c_j}}(t) = f_{out_j}(net_{out_j}(t))\, h'(s_{c_j}(t)) \sum_{k} w_{kc_j}\, e_k(t)$$
- **Constant error flow through the CEC** (Eq. A.28/A.33):
$$\frac{\partial s_{c_j}(t-k)}{\partial s_{c_j}(t-k-1)} \approx_{tr} 1 \;\;\Rightarrow\;\; \frac{\partial \vartheta_{s_{c_j}}(t)}{\partial \vartheta_{s_{c_j}}(t+1)} = \frac{\partial s_{c_j}(t+1)}{\partial s_{c_j}(t)} \approx_{tr} 1$$
- Update complexity (Eq. A.27):
$$O(KH + KCS + HI + CSI) = O(W)$$
($K$ outputs, $H$ hidden units, $C$ cell blocks, $S$ block size, $I$ inputs).
- Remedies for practical issues: **abuse problem** → sequential network construction or negative output-gate bias; **internal state drift** → negative initial input-gate bias.

## 📊 Dataset & Input Features
- Entirely **synthetic long-time-lag benchmarks**; no real-world data (authors list time-series prediction as future work):
  - **Experiment 1**: [[Embedded_Reber_Grammar]] — 256 training / 256 test strings, local 7-in/7-out encoding, minimal lags ~9 steps.
  - **Experiment 2a/2b**: noisy & noise-free symbol sequences, delay $p=100$, ~10,500 weights; **Task 2c**: distractor symbols at random positions with minimal lag up to $q{=}1000$ (up to 6,064 weights).
  - **Experiments 3a/3b/3c**: Bengio et al.'s two-sequence problem, $T=100$/$1000$, Gaussian noise (variance 0.2; targets variance 0.1 in 3c), 256/2560-sequence test sets.
  - **Experiment 4**: Adding Problem (pairs of real value ∈ $[-1,1]$ + marker; target $0.5+(X_1+X_2)/4.0$), $T$ up to 1000, minimal lag $T/2=500$.
  - **Experiment 5**: Multiplication Problem (product $X_1 \times X_2$ of marked inputs).
  - **Experiment 6**: Temporal Order classification (2 or 3 widely separated symbols X/Y among distractors, 4 or 8 classes).
- Features: local/distributed, real-valued and noisy pattern representations; online randomly generated sequences; error only at sequence end (except Exp. 1, 2a, 2b).
- Data availability: no external dataset links; author page referenced in bibliography: `http://www7.informatik.tu-muenchen.de/~hochreit` (Hochreiter's 1991 diploma thesis).

## 📈 Performance & Results
- **Exp. 1 (Embedded Reber)**: LSTM 100% success after 8,440–39,740 sequence presentations (best 8,440 @ lr 0.5, 276 weights); RTRL only partial success after ≥25,000; RCC 50% after 182,000; ELM >200,000. Only 2 failures out of 150 LSTM trials.
- **Exp. 2a (delay $p=100$)**: LSTM 100% success after 5,040 presentations vs. chunker (CH) 33% after 32,400; RTRL/BPTT **0%** within 5M presentations. Task 2b (no local regularities): LSTM always successful, mean 5,680 presentations.
- **Exp. 2c (lag 1000)**: LSTM solves all $(p,q)$ configurations (30,000–203,000 sequences; e.g., $p{=}q{=}1000$: 6064 weights, 49,000 sequences); BPTT/RTRL have no chance beyond lags ≈10 steps.
- **Exp. 3a/3b**: solved to ST2 criterion (e.g., $T{=}1000$: stop after 452,460 / 485,080 sequences, misclassification fractions 0.000078 / 0.01207 on 2560 test sequences) — though random weight guessing beats all published methods on 3a. **Exp. 3c** (guessing-infeasible): fraction misclassified 0.00558 / 0.00441, avg deviation to expected target 0.014 / 0.012 (< 0.015 threshold).
- **Exp. 4 (Adding, $T{=}1000$, lag 500)**: ≤1 wrong prediction out of 2560 test sequences; success after 74,000 / 209,000 / 853,000 sequences for $T=100/500/1000$ (93 weights).
- **Exp. 5 (Multiplication)**: test MSE 0.0223 (nseq=140) and 0.0139 (nseq=13), with 139/14 wrong out of 2560.
- **Exp. 6 (Temporal Order)**: task 6a — 1 wrong out of 2560 after 31,390 sequences; task 6b — 2 wrong out of 2560 after 571,100.
- Scaling: learning time grows very slowly as #symbols/weights grow proportionally with the lag; increasing distractor frequency slows learning via weight oscillations.

## 💡 Limitations & Identified Research Gaps
- Truncated LSTM struggles with **nondecomposable tasks** (strongly delayed XOR / parity-like problems where storing single inputs doesn't reduce error incrementally); full-gradient variant increases complexity but showed no significant benefit.
- Each memory cell block costs 2 extra gate units (≤ factor-of-9 weight increase vs. standard RNN hidden unit).
- Like feedforward nets seeing the whole string, CEC-based LSTM behaves similarly to a BP-trained feedforward net on the full input — problematic for e.g. 500-bit parity.
- Gradient-based methods (incl. LSTM) cannot precisely count discrete time steps (99 vs. 100 steps); needs auxiliary counting mechanisms; simple decays/counting differences (3 vs. 11) are fine.
- Experiments are purely artificial small-scale tasks; authors explicitly propose applying LSTM to **real-world data: time-series prediction, music composition, speech processing** — the gap later filled by load/EV-demand forecasting models.
- No forget gate, peephole connections, or bidirectionality (added by later work).

## 📚 BibTeX & Citation Reference
```bibtex
@article{hochreiter1997lstm,
  title   = {Long Short-Term Memory},
  author  = {Hochreiter, Sepp and Schmidhuber, J{\"u}rgen},
  journal = {Neural Computation},
  volume  = {9},
  number  = {8},
  pages   = {1735--1780},
  year    = {1997},
  publisher = {MIT Press},
  doi     = {10.1162/neco.1997.9.8.1735}
}
```

## 🔗 Key References & Citation Graph
- [[RNN]] / [[RNN]] — simple recurrent baselines that fail on long time lags
- [[BPTT]] (Williams & Zipser 1992; Werbos 1988) and [[RTRL]] (Robinson & Fallside 1987) — gradient algorithms whose error flow vanishes/blows up exponentially
- Bengio, Simard & Frasconi (1994), *Learning long-term dependencies with gradient descent is difficult* — motivating analysis; two-sequence/latch problems reused here
- Fahlman (1991) Recurrent Cascade-Correlation; Mozer (1992) time constants; Schmidhuber (1992b, 1993) neural sequence chunkers — competing long-time-lag approaches
- Watrous & Kuhn (1992) second-order nets with multiplicative units — precursor of gating idea
- Downstream vault papers building on [[LSTM]]:
  - [[2001_Neural_Networks_STLF_Review]] — ANN-era context for load forecasting
  - [[2018_Empirical_TCN_Sequence_Modeling]] — empirical TCN vs. LSTM/RNN comparison for sequence modeling
  - [[2024_LSTM_Transformer_EV_Consumption]] and [[2025_Hybrid_LSTM_Transformer_Demand]] — LSTM as EV charging demand backbone
  - [[2025_QR_LSTM_Attention_EV_Load]] — quantile LSTM attention EV load forecasting
