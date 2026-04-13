---
title: "Teaching Models to Express Their Uncertainty in Words"
authors: "Stephanie Lin, Jacob Hilton, Owain Evans"
year: 2022
venue: "Transactions on Machine Learning Research (TMLR); also arXiv:2205.14334"
doi_url: "https://arxiv.org/abs/2205.14334"
---

# Teaching Models to Express Their Uncertainty in Words

## One-Sentence Summary
Demonstrates that GPT-3 can be supervised-finetuned on a mathematics benchmark (CalibratedMath) to emit a *verbalized* confidence estimate (either a numeric percentage or a categorical word such as "lowest"/"low"/"medium"/"high"/"highest") alongside each answer, and that this verbalized calibration is reasonably well-calibrated and generalizes under distribution shift, out-performing an "answer logit" baseline trained on the same finetuning data *(p.0-1, p.5-6)*.

## Problem Addressed
Language-model users want uncertainty estimates, but the existing approach is to read the model's *output token logits*, which conflate "is this the right answer?" with "is this the most likely token given this prompt?" and are inaccessible through many deployed APIs. The authors ask whether a model can instead *say in natural language* how confident it is about its own answer, and whether that verbalized confidence remains calibrated when the task distribution shifts *(p.0-1)*.

## Key Contributions
- Introduce **CalibratedMath**, a suite of 21 arithmetic sub-tasks at multiple difficulty levels, designed so that (a) GPT-3's accuracy on any given sub-task is non-trivially variable (it cannot simply be "always confident" or "always unsure") and (b) train vs. evaluation sets produce content / difficulty distribution shifts *(p.1, p.2, Table 3 p.14)*.
- Define three kinds of uncertainty representation a model could express:
  1. **Verbalized numbers** — model emits a percentage like "Confidence: 61%" *(p.2)*.
  2. **Verbalized words** — model emits one of five categorical labels *(p.2; Appendix B.1 clarifies that they actually use random names "john/sam/matt/dan/tom" with a fixed latent ordering because ordered labels worked slightly worse, p.16)*.
  3. **Answer logit** — model's token-level probability for the answer itself, with a temperature parameter finetuned to calibrate it (not a verbalization — used as the baseline) *(p.2)*.
- Show via supervised finetuning that **verbalized probability (both number and word forms) generalizes under distribution shift better than the answer-logit baseline**, and also outperforms a constant baseline — i.e. GPT-3 learns a transferable meta-cognitive signal about its own reliability, not just a memorized per-subtask average *(p.1, p.5-6, Table 1 p.6)*.
- Show that few-shot (in-context) verbalized calibration does NOT generalize well beyond the fundamentally different context of the training prompt — supervised finetuning is required for robust out-of-distribution calibration *(p.7-8, Fig 6 p.7)*.
- Analyse that the verbalized model is not just "reproducing the answer logit in words" — the two signals are only weakly correlated (Fig 12 p.19), which is evidence that the finetuned calibration is substantively different from temperature-scaled logits *(p.9, p.19)*.

## Study Design
- **Type:** Controlled supervised-finetuning experiment on a single frontier LM (GPT-3, text-davinci via OpenAI API). No human subjects.
- **Model:** GPT-3 175B (OpenAI API, circa 2021-2022 davinci-family base model) *(p.4)*.
- **Benchmark:** CalibratedMath — 21 sub-tasks of arithmetic over integers, with 14 difficulty levels controlled by number of digits and formatting (see Table 3 p.14 for full enumeration: addition, subtraction, multiplication, division, floor division, modulo, remainder, percentages, fraction reduction, rounding, arithmetic sequences, 3-step addition, 3-step multiplication, addition/subtraction (alt wording), and six "Multi[-answer]" operations: less than / greater than / prime / square / two-sum / multiple) *(Table 3, p.14)*.
- **Training distribution:** Add/Sub group of sub-tasks *(p.4, Table 3 p.14)*.
- **Evaluation distributions:** Two held-out shifts:
  - **Multiply-divide** (content shift — different arithmetic operations but still single-answer) *(p.4, p.14)*.
  - **Multi-answer** (format shift — "Name any number smaller than 100?", multiple valid answers) *(p.4, p.14)*.
- **Training objective:** Supervised finetuning of GPT-3 to emit `<question>\nA: <answer>\nConfidence: <value>` where the `<value>` target was computed from the model's own empirical sub-task-level correctness rate p̂_T rather than per-sample ground truth (see Step B.3 p.16) *(p.4-5, p.16)*.
- **Finetuning scale:** ~10k examples (100 per training sub-task), one epoch, learning_rate_multiplier = 0.1, with an **early stopping at n ≈ 2700 examples** because per-sample MSE starts to flatten/increase past that point even though the loss against p̂_T continues to decrease — they use this as a proxy for "the model has now learned the question-level signal and is starting to overfit to the sub-task mean" *(p.16-17, Fig 10 p.17)*.
- **Decoding:** Both *greedy* and *Expected-Value (EV)* decoding over confidence tokens are reported; EV takes the probability-weighted average of possible confidence categories (e.g. 0.5·"High"(70%) + 0.5·"Medium"(50%) = 60%) *(p.18)*.

## Methodology
The core methodology is:

1. **Estimate sub-task accuracy:** For each sub-task T, sample many GPT-3 completions and compute p̂_T = fraction correct. This becomes the *target* confidence for every finetuning example drawn from T *(p.4-5, p.16)*.
2. **Finetune** GPT-3 to emit `Confidence: <p̂_T>` after its answer, using the verbalized-number or verbalized-word format. Training data comes only from the Add/Sub sub-tasks *(p.4-5)*.
3. **Evaluate** the finetuned model on held-out Multiply-divide and Multi-answer questions, computing MSE and MAD between the per-sample emitted confidence and the per-sample correctness indicator {0,1} *(p.3-4, p.5-6)*.
4. **Compare** against:
   - *Indirect logit (finetuned):* use the model's output-token probability for the answer, with a temperature parameter separately finetuned *(p.2, p.5-6)*.
   - *Constant baseline:* emit the sub-task-level p̂_T regardless of question *(p.5-6)*.
5. **Probe generalization** via few-shot variants (5 / 10 / 25 / 50 shots) and a linear-projection UMAP analysis of the model's hidden states to inspect whether the verbalized model uses qualitatively different internal features from the answer-logit model *(p.7-9, Fig 7 p.9)*.

## Key Equations / Statistical Models

**Calibration target (Equation 1).** A probability estimator p is *perfectly calibrated* if, conditional on the estimator outputting value p, the event x_high (the model being correct) occurs with frequency p:

$$
\Pr(x_{\text{high}} \mid p) = p
$$

for p ∈ [0, 1] *(p.2)*.

**Mean squared error (MSE).** Used as the primary calibration score, one index per sample:

$$
\mathrm{MSE} = \frac{1}{N} \sum_{i=1}^{N} (p_i - \mathbb{1}[y_i = y_i^*])^2
$$

Where p_i is the confidence the model emitted on example i, and 𝟙[y_i = y_i*] is 1 if the model's answer matches ground truth, else 0 *(p.3-4)*.

**Mean absolute deviation (MAD) calibration score.** Computed by bucketing predictions into K bins and taking the mean absolute gap between mean predicted probability and empirical accuracy per bucket:

$$
\mathrm{MAD} = \frac{1}{K} \sum_{k=1}^{K} \big| \operatorname{acc}(b_k) - \operatorname{conf}(b_k) \big|
$$

Where conf(b_k) is the mean predicted confidence in bucket k and acc(b_k) is the empirical accuracy in bucket k *(p.3-4)*.

*(Exact bucketing scheme: they state MAD is measured in the same way whether the model outputs a verbalized number, a verbalized word, or an answer-logit score — implicitly implying ≥ ~5 buckets matched to the word-based discretization, but the paper does not give a K value in the main text. p.3-4.)*

**EV decoding over categorical confidence tokens.** When the verbalized form is a word, they extract the probability distribution over the 5 allowed confidence tokens and take the expectation against the nominal mid-points [10%, 30%, 50%, 70%, 90%]:

$$
p_i^{\text{EV}} = \sum_{c \in \{10,30,50,70,90\}} \Pr(\text{token}_i = c) \cdot c
$$

*(derived from p.18 description; paper does not display this in a formal equation but states the procedure explicitly, giving the worked example 0.5·70% + 0.5·50% = 60%.)*

## Parameters

### Benchmark / Training Configuration

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Base language model | — | — | GPT-3 175B (davinci) | — | p.4 | OpenAI API finetuning endpoint |
| CalibratedMath sub-tasks total | — | count | 21 | — | p.2, p.14 | Table 3 enumerates all sub-tasks |
| Difficulty levels per sub-task | — | count | — | 1-24 | p.14 | Add/Sub ops have up to 24 digit-formatting levels; Multi* ops have 2 levels each |
| Finetuning dataset size | n | examples | ~10,000 | 100 per training sub-task | p.16 | |
| Early-stopping point | n* | examples | ~2,700 | — | p.16-17 | Chosen because per-sample MSE on training set flattens past this point (Fig 10 p.17) |
| Training epochs | — | epochs | 1 | — | p.16 | "to prevent overfitting" |
| Learning-rate multiplier | — | — | 0.1 | — | p.16 | OpenAI finetuning API default-family |
| Training distribution | — | — | Add/Sub | — | p.4 | |
| Evaluation distribution 1 | — | — | Multiply-divide | — | p.4 | Content shift |
| Evaluation distribution 2 | — | — | Multi-answer | — | p.4 | Format shift |
| k-shot counts evaluated | k | shots | — | 5, 10, 25, 50 | p.7 | For few-shot generalization (Fig 6 p.7) |
| Verbalized-word categories | — | count | 5 | — | p.16 | lowest / low / medium / high / highest — but implemented via random names john/sam/matt/dan/tom |
| Word → probability midpoints | — | % | — | [10, 30, 50, 70, 90] | p.18 | Used for EV decoding |

### Verbalized-Word Calibration Bins (Appendix B.1 / C.2)

| Word label | Surface form used | Nominal probability | Page |
|------------|-------------------|---------------------|------|
| lowest | "john" | 10% | p.16, p.18 |
| low | "sam" | 30% | p.16, p.18 |
| medium | "matt" | 50% | p.16, p.18 |
| high | "dan" | 70% | p.16, p.18 |
| highest | "tom" | 90% | p.16, p.18 |

## Effect Sizes / Key Quantitative Results

### Table 1 (p.6): Calibration scores on the two evaluation sets (MSE and MAD — LOWER IS BETTER)

| Setup | Multi-answer MSE | Multi-answer MAD | Multiply-divide MSE | Multiply-divide MAD |
|-------|------------------|------------------|---------------------|---------------------|
| **Verbalized numbers (finetuned)** | **22.0** | **16.4** | 15.5 | **19.0** |
| Answer logit (zero-shot) | 37.4 | 33.7 | **10.4** | 9.4 |
| Indirect logit (finetuned) | 33.7 | 38.4 | 11.7 | 7.1 |
| Constant baseline | 34.1 | 31.1 | 15.3 | 8.5 |

Key reading: on **Multi-answer** (format shift) the *verbalized number* model wins cleanly across both metrics; on **Multiply-divide** (content shift) the *answer logit* and *indirect logit* baselines are hard to beat on raw MSE but verbalized numbers still have competitive MAD and beat the constant baseline. *(p.6)*

### Table 2 (p.9): Coarser "is my answer correct" probing — the Verbalized model generalizes with simple information in the input

| Setup | Multi-answer MSE | Multi-answer MAD | Multiply-divide MSE | Multiply-divide MAD |
|-------|------------------|------------------|---------------------|---------------------|
| Verbalized numbers (finetuned) | 29.0 | 24.0 | 12.7 | 10.6 |
| Log. reg. with heuristic input | 29.7 | 31.2 | 17.7 | 18.5 |
| Linear probe on GPT-3 embedding | 31.2 | 30.1 | 14.0 | 14.2 |

*(p.9 — the verbalized-words finetune is competitive with or better than a linear probe on hidden states, indicating the model's meta-knowledge is extractable via language without needing internal access.)*

### Table 4 (Appendix C.2, p.18): Greedy vs EV decoding for finetuned models

| Setup | Multi-answer MSE | Multi-answer MAD | Multiply-divide MSE | Multiply-divide MAD |
|-------|------------------|------------------|---------------------|---------------------|
| Verbalized numbers (greedy) | 22.0 | 16.4 | 15.5 | 19.0 |
| **Verbalized numbers (EV)** | **21.5** | **14.6** | **15.0** | **18.9** |
| Verbalized words (greedy) | 29.0 | 24.0 | **12.7** | **10.6** |
| Verbalized words (EV) | 26.0 | 21.7 | 12.7 | 13.3 |

Key reading: EV decoding is a strict-or-tie improvement over greedy for verbalized *numbers*. For verbalized *words*, EV helps on Multi-answer (coarser word bins gain from interpolation) but ties or *hurts* on Multiply-divide MAD (13.3 vs 10.6). *(p.18)*

### Table 5 (Appendix C.3, p.19): Effect of retraining on Multiply-divide instead of Add-subtract

| Setup | Add-subtract MSE | Add-subtract MAD | Multi-answer MSE | Multi-answer MAD |
|-------|-------------------|-------------------|-------------------|-------------------|
| Verbalized numbers (finetune) | 17.0 | 9.9 | 26.3 | 40.7 |
| Verbalized words (finetune) | 16.4 | 6.8 | 20.5 | 30.2 |
| Answer logit (zero-shot) | 15.5 | 14.3 | 37.4 | 33.7 |
| Indirect logit (finetune) | 17.3 | 15.0 | 43.9 | 49.9 |
| Constant baseline | 20.1 | 8.5 | 40.1 | 39.5 |

*(p.19 — training on a harder sub-distribution and then generalizing "outward" still produces non-trivial calibration transfer, though absolute numbers on the format-shifted Multi-answer set are substantially worse than the Add/Sub→{…} direction used in the main paper.)*

### Few-shot / in-context performance (Fig 6 p.7)

Few-shot prompting alone, even with k ∈ {5, 10, 25, 50}, does NOT reproduce the calibration quality of the finetuned verbalized model. The scatter plots for k = 5 and k = 10 on Multi-answer are essentially uncorrelated with accuracy; k = 25 and k = 50 improve but do not match the finetune. *(p.7-8)*

## Methods & Implementation Details
- **Training prompt format:** Each example is a triple `Q: <question>\nA: <answer>\nConfidence: <value>`. The answer is the model's own greedy answer (correct or incorrect) and the target confidence is the sub-task-level accuracy p̂_T computed in advance, NOT the per-example binary correctness *(p.4-5, p.16)*.
- **Why use p̂_T instead of per-example 0/1 targets:** They argue that if the model perfectly predicted 0/1 correctness per example it would incur worse MSE against p̂_T, and conversely over-fitting p̂_T costs per-sample MSE. The tradeoff is what motivates the early-stopping at n≈2700 *(p.16-17)*.
- **Few-shot prompt** shown in Fig 9 (p.16) — 5 in-context examples with percentages like "Confidence: 19%", "Confidence: 44%", ..., followed by the target query with a blank `Confidence:` for the model to fill.
- **Verbalized words choice:** tried ordered categories {lowest, low, medium, high, highest}; found "using random names without explicit orderings (john, sam, matt, dan, tom) led to very slightly better performance" and used random names throughout. Mapping to probabilities is fixed at {10, 30, 50, 70, 90}% *(p.16)*.
- **Indirect logit baseline:** Fit a single temperature parameter via grid search on a held-out split to calibrate GPT-3's answer-token probability into a probability-of-correct signal *(p.2, p.5-6)*.
- **UMAP linear-projection probe (Fig 7 p.9):** Take GPT-3 embeddings from the last layer of the finetuned model, fit a linear projection into two dimensions, color-code by correctness. The verbalized model's embeddings linearly separate correct from incorrect on held-out distributions; the zero-shot baseline does not *(p.9)*.
- **Correlation analysis (Fig 12 p.19):** Scatter of verbalized confidence vs answer-token logit shows **weak correlation**, supporting the claim that the verbalized signal is not simply reproducing the logit.
- **No retraining per evaluation set:** The model is finetuned once on Add-subtract and evaluated zero-additional-training on the other two. The Appendix C.3 Multiply-divide-trained variant is a separate robustness check *(p.19)*.

## Algorithm / Protocol (reconstructed)

```
INPUT: base LM M (GPT-3), set of sub-tasks T_train (Add/Sub),
       target representation R ∈ {verbalized_number, verbalized_word, answer_logit}

# Step 1: estimate sub-task accuracies
for each sub-task t in T_train:
    sample N answers from M on t
    p̂_t <- empirical correctness rate

# Step 2: build finetuning corpus
D <- empty
for each sub-task t in T_train:
    draw 100 questions q from t
    for each q:
        a <- greedy answer of M on q
        target confidence c_target depends on R:
            verbalized_number: c_target = round(p̂_t, integer percent)
            verbalized_word:   c_target = nearest word bin to p̂_t
            answer_logit:      c_target = tempered prob-of-answer
        append "Q: q\nA: a\nConfidence: c_target" to D

# Step 3: finetune with early stopping
M' <- finetune M on D, one epoch, lr_mult=0.1
monitor per-sample MSE on held-out Add/Sub
stop training at n ≈ 2700 examples (before per-sample MSE flattens/rises)

# Step 4: evaluate zero-additional-training
for each eval sub-task t_eval in {Multiply-divide, Multi-answer}:
    for each q in t_eval:
        a, c <- sample from M' with "Q: q\nA:" prefix
        record (a, c, ground_truth)
    compute MSE and MAD against per-sample correctness
```

## Figures of Interest
- **Fig 1 (p.1):** Visual illustration of verbalized probability and CalibratedMath prompt — shows the exact format "Q: What is the remainder when 23 is divided by 47?\nA: 3\nConfidence: Medium".
- **Fig 2 (p.2):** Comparison of three probability kinds (verbalized number / verbalized word / indirect logit) with definitions, examples, supervised-finetuning objectives, and desirable properties.
- **Fig 3 (p.3):** Concrete training and evaluation examples — shows the shift in difficulty (single-answer harder arithmetic) AND shift in content (multiply-divide format, Multi-answer format).
- **Fig 4 (p.5):** MSE on evaluation sets (bar chart) — Verbalized numbers wins on Multi-answer; Constant baseline / logit baselines win on Multiply-divide but not by much.
- **Fig 5 (p.7):** Calibration scatter curves for training (Add-subtract) and the two evaluation sets, across verbalized features, answer-logit features, and indirect-logit features. Shows the finetuned verbalized calibration is closer to the y=x line for Multi-answer.
- **Fig 6 (p.7):** Few-shot learning calibration curves at k ∈ {5, 10, 25, 50} vs the full finetune — finetune dominates few-shot on Multi-answer, diminishing returns past k=25.
- **Fig 7 (p.9):** Linear projection of GPT-3 embeddings into 2D on the training vs Multi-answer vs Multiply-divide sets, colored by correctness — visualizes that the verbalized finetuned embedding separates more cleanly than the base model.
- **Fig 8 (p.15):** Histogram of GPT-3 per-sub-task accuracies showing the distribution shift from Add-subtract (training) to Multi-answer (right-shifted: GPT-3 does much better) and Multiply-divide (left-shifted: GPT-3 does worse). Motivates why being well-calibrated on Multi-answer requires GPT-3 to produce *higher* confidences on average than on training.
- **Fig 9 (p.16):** Example 5-shot prompt used for k-shot evaluation.
- **Fig 10 (p.17):** Verbalized calibration curves as function of n ∈ {100, 500, 1000, 2700, 10000} — motivates n ≈ 2700 early-stopping choice.
- **Fig 11 (p.18):** Calibration curves using greedy vs EV uncertainty — side-by-side shows EV gives smoother, more continuous probability coverage, greedy collapses to 5 points for words.
- **Fig 12 (p.19):** Scatter of verbalized confidence vs logit-of-answer — weak correlation is the evidence that verbalized signal ≠ logit in disguise.

## Results Summary
- On the **Multi-answer** format-shift evaluation, verbalized numbers achieves MSE = 22.0, MAD = 16.4, beating all non-verbalized baselines by wide margins (next best: Constant 34.1/31.1) *(Table 1 p.6)*.
- On the **Multiply-divide** content-shift evaluation, verbalized numbers achieves MSE = 15.5, MAD = 19.0, NOT the best on MSE (answer logit zero-shot wins at 10.4) but still beats the constant baseline *(Table 1 p.6)*.
- Few-shot in-context learning does not recover the calibration quality; finetuning is qualitatively different *(p.7-8, Fig 6)*.
- EV decoding reliably matches or beats greedy decoding for numbers; for words it helps coarse-bin problems but can mildly hurt sharper-bin problems *(Table 4 p.18)*.
- The verbalized confidence signal is only weakly correlated with the answer-token logit — this is evidence that verbalized calibration is not just a surface reparameterization of the logit *(Fig 12 p.19)*.
- The GPT-3 finetuned verbalized model's last-layer embeddings are linearly separable by correctness on held-out distributions, suggesting learned *self-knowledge features* rather than per-sub-task memorization *(Fig 7 p.9)*.

## Limitations
- Only one model studied (GPT-3 175B davinci family); no ablation on model scale, no test on smaller or larger models, no test on other families (PaLM, Chinchilla, T5) *(stated in §4 Directions for future work, p.10)*.
- Only arithmetic: CalibratedMath is synthetic and short-answer. Generalization to open-ended or long-form generation (summarization, QA, code) is explicitly called out as future work, not demonstrated *(p.10)*.
- Supervised targets depend on p̂_T which is itself a sub-task average. The model does not receive per-example ground-truth correctness as a training signal, and this forces the early-stopping compromise between "learn sub-task mean" and "learn per-sample signal" *(p.16-17)*.
- The best-generalizing setup (verbalized numbers on Multi-answer) is still not perfectly calibrated — curves in Fig 5 lie noticeably off the diagonal at both ends *(p.7)*.
- Verbalized words cannot express fine-grained confidence without EV interpolation over token logits; greedy "verbalized words" is quantized to 5 buckets {10, 30, 50, 70, 90}% *(p.18)*.
- The finetuning data explicitly uses sub-task-level p̂_T as the target, meaning the model is learning something closer to "how hard is this sub-task on average" than "how likely am I right on this specific question" — caveat for anyone quoting this paper as evidence of *per-example* self-knowledge *(p.16-17; see Design Rationale below)*.

## Arguments Against Prior Work
- **Guo et al. 2017** and related calibration literature assume access to output logits, which is unavailable through many deployed LM APIs; verbalized calibration sidesteps this *(p.1, p.10)*.
- **Temperature scaling / Platt scaling**: fine for in-distribution calibration but the paper's answer-logit baseline IS such a method and it visibly fails to generalize to the Multi-answer distribution (MSE 37.4 vs 22.0 for verbalized) *(Table 1 p.6)*.
- **"Just read the model's answer-token probability"**: weakly correlated with the finetuned verbalized signal (Fig 12 p.19), so the verbalized model has learned something logits don't directly encode.
- **Few-shot calibration**: explicitly evaluated in §3.3 and shown insufficient for OOD generalization, countering the implicit prior that in-context examples are a free substitute for finetuning *(p.7-8)*.
- **Ordered verbal labels** ({lowest, low, medium, high, highest}) were tried but *random names* worked slightly better, a small but concrete argument against the intuition that giving the model ordered vocabulary would help it learn a scalar *(p.16)*.

## Design Rationale
- **Why supervise on p̂_T instead of per-example 0/1 correctness?** Using 0/1 would force the model to learn a true per-example difficulty estimator from one supervised signal per example — a much harder problem — and would also make the target noisy. p̂_T gives a denser, less-noisy target at the cost of introducing the sub-task-mean / per-sample-MSE tradeoff that the early stopping addresses *(p.16-17)*.
- **Why verbalized numbers AND verbalized words?** Numbers give continuous fine-grained output (good for EV decoding and standard calibration metrics); words test whether categorical language tokens carry meta-cognitive signal through finetuning. Words also map more naturally to user-facing hedging language *(p.2, p.16)*.
- **Why random names instead of ordered scale words?** Tested empirically and found slightly better generalization — the paper hypothesises that ordered words may leak unwanted pretraining priors about which word is "more confident" *(p.16)*.
- **Why MSE + MAD both?** MSE captures fine-grained calibration at individual probability values; MAD normalizes across buckets and is sensitive to whether the model's confidence histogram *on average* tracks accuracy, which can diverge from MSE on quantized outputs like verbalized words *(p.3-4)*.
- **Why early-stop at n ≈ 2700?** Because beyond that point the loss against p̂_T continues to decrease (model is learning the sub-task mean better) but the per-sample MSE flattens or increases (the model is losing per-question discriminativeness). n ≈ 2700 is where those two curves balance *(p.16-17, Fig 10 p.17)*.
- **Why evaluate both content and format shift?** To distinguish "the model is generalizing a sub-task-level difficulty lookup" (would transfer to format shift well, since same sub-task exists) from "the model is generalizing a per-question self-knowledge feature" (would transfer to content shift). Both shifts show at least partial transfer, suggesting some of each *(p.4, p.6)*.

## Testable Properties
- **Verbalized number finetune MSE on Multi-answer ≤ 22.0**, MAD ≤ 16.4 on CalibratedMath-style held-out Multi-answer distribution *(p.6)*.
- **Verbalized word finetune MSE on Multiply-divide ≤ 12.7**, MAD ≤ 10.6 *(p.6, p.18)*.
- **Constant baseline** (emit only sub-task average) is NOT degenerate on Multiply-divide MSE — verbalized numbers does not outperform it on that single metric, only on Multi-answer and on MAD *(p.6)*. Any "verbalized calibration always wins" framing is too strong; the paper explicitly shows cases where zero-shot logits outperform verbalized on content-shifted evaluation.
- **EV decoding monotonically improves numbers, sometimes hurts words**: MSE(EV, numbers) ≤ MSE(greedy, numbers) on both eval sets, but MAD(EV, words, Multiply-divide) = 13.3 > MAD(greedy, words, Multiply-divide) = 10.6 *(p.18)*.
- **Verbalized confidence and answer-token logit are weakly correlated** (Fig 12 p.19) — this is testable: rerun the experiment and compute Pearson r between the two signals, expect |r| well below 0.5.
- **Few-shot k=25 does not reach finetune calibration quality**: a k-shot experiment at k ∈ {25, 50} on Multi-answer should underperform the finetune *(Fig 6 p.7)*.
- **Early-stopping at n ≈ 2700 beats n = 10000** on per-sample MSE metric *(Fig 10 p.17)*.
- **Last-layer embeddings of the verbalized finetune are more linearly separable by correctness** than the base model on held-out evaluation distributions *(Fig 7 p.9)*.

## Relevance to Project
This paper is retrieved as an authority for the critique of Wabinski 2026's confidence-threshold rule in the inclusive-cartography systematic review protocol. Concretely:

- It is one of the *foundational* studies on whether LMs can produce meaningful self-reported confidence in natural language, and it establishes that with supervised finetuning this works *partially*, with measurable generalization but also explicit failure modes (content-shift MSE parity with logit baselines, quantization artifacts for word-valued outputs, early-stopping tradeoffs).
- It shows that a verbalized confidence from a base LM is **not** the same as a temperature-scaled logit and need not correlate strongly with it — which directly undermines any reviewer protocol that treats a model's emitted "Confidence: 80%" as interchangeable with its token probabilities or as a ground-truth reliability indicator.
- It shows that **no in-context few-shot prompting strategy tested produces calibration quality matching finetuning**, which is a direct problem for any systematic-review protocol that uses a non-finetuned LM with simple prompts to extract calibrated judgments and then thresholds on the emitted confidence.
- The paper's MSE numbers on out-of-distribution tasks (22.0 on Multi-answer, 15.5 on Multiply-divide, best case) correspond to calibration errors in the ~15-20% range for a *finetuned* model on a *synthetic arithmetic* benchmark. Any protocol using a larger LM on a broader out-of-distribution task with no finetuning should expect *worse* than this, not better. A fixed threshold like "trust the model if it says ≥ 0.8" is therefore unsupported by the evidence base this paper establishes.

## Open Questions
- [ ] Does the finetuned verbalized calibration generalize beyond arithmetic — e.g. to open-ended QA, or to judgments about factual claims? (The paper explicitly calls this out in §4 p.10 as future work.)
- [ ] How does the approach scale to larger / more capable models (GPT-4, Claude, etc.)? Not evaluated in this paper.
- [ ] What is the correct K for the MAD bucketing in Section 2.3? Paper does not state it explicitly in the main text and the exact choice affects reported MAD numbers.
- [ ] How sensitive is the ~2700-example early-stopping point to dataset composition — would a different distribution of training sub-tasks shift it?
- [ ] Does the random-name labeling for verbalized words generalize to the setting where the model is expected to *interpret* a user's verbalized confidence, or only to *emit* it?

## Collection Cross-References

### Already in Collection
- [[Kadavath_2022_LanguageModelsMostlyKnow]] — Anthropic complement: probes the model for self-knowledge via P(True) and a trained P(IK) value head rather than through supervised finetuning of verbalized output. Kadavath's finding that RLHF policies are miscalibrated directly motivates the shift to verbalized calibration that Lin et al. initiated.
- [[Tian_2023_JustAskCalibrationStrategies]] — Direct successor. Tian et al. show that for RLHF-finetuned successors (GPT-4, ChatGPT, Claude-1/2, Llama-2-70B-chat), the verbalized signal Lin et al. achieved via supervised finetuning on GPT-3 can be elicited via pure prompting with two-step and top-k elicitation, reducing ECE by ~50% vs conditional probabilities — no finetuning or labeled data required.
- [[Xiong_2024_LLMUncertaintyConfidenceElicitation]] — Xiong et al. argue that fine-tuning-based methods (this paper) demand compute that low-resource researchers cannot afford (Xiong p.2) and extend the confidence-elicitation framework to a pure black-box setting.
- [[Wabiski_2026_CognitiveReviewProtocol]] — Direct critique target. See `papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md` §2.2(f) for the specific use of Lin et al.'s weak-correlation-with-logits and few-shot-does-not-reach-finetune results against the protocol's `>0.90 auto-include` rule.

### Cited By (in Collection)
- [[Tian_2023_JustAskCalibrationStrategies]] — Cites Lin 2022 as prior work on verbalized uncertainty; Tian's zero-shot prompting setup is the natural successor to Lin's supervised-finetuning approach.
- [[Xiong_2024_LLMUncertaintyConfidenceElicitation]] — Cites Lin 2022 as the finetuning-based baseline that the black-box framework is designed to avoid.
- [[Kadavath_2022_LanguageModelsMostlyKnow]] — Cites Lin 2022 as complementary work on verbalized uncertainty from the supervised-finetuning side.

### Conceptual Links (not citation-based)
- [[Brock_2015_InteractiveMapsUsability]] — Strong. Brock's finding that human self-reported confidence is temporally mis-calibrated (tracks short-term scores but decouples at 2-week retention) is exactly the failure mode Lin's supervised-verbalized-confidence method tries to fix in LLMs — mechanism (Brock) ↔ fix (Lin) across domains.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Moderate. Wabinski 2022 is the tactile-map design guideline underlying the 2026 protocol; Lin's verbalized-calibration results bear on whether LLM-assisted extraction of Wabinski's parameters can be trusted at the thresholds the 2026 protocol specifies.

## Related Work Worth Reading
- **Guo et al. 2017** — On calibration of modern neural networks (foundational for the logit-based calibration lineage this paper pushes back against).
- **Desai & Durrett 2020** — Calibration of pre-trained transformers (prior art on transformer logit calibration).
- **Kadavath et al. 2022** (Anthropic) — Language models (mostly) know what they know. Complementary work asking the same question from the probing-the-model side. → NOW IN COLLECTION: [[Kadavath_2022_LanguageModelsMostlyKnow]]
- **Jiang et al. 2021** — How can we know when language models know? QA-focused self-knowledge study.
- **Kuhn, Gal, Farquhar 2023** — Semantic uncertainty for LM generation (later follow-up line that this paper's work enables).
- **Mielke et al. 2022** — Reducing conversational agent overconfidence via linguistic calibration (closest direct relative in the "teach the model to hedge in words" line).
