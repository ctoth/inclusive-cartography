---
title: "Language Models (Mostly) Know What They Know"
authors: "Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez, Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-Johnson, Scott Johnston, Sheer El-Showk, Andy Jones, Nelson Elhage, Tristan Hume, Anna Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, Deep Ganguli, Danny Hernandez, Josh Jacobson, Jackson Kernion, Shauna Kravec, Liane Lovitt, Kamal Ndousse, Catherine Olsson, Sam Ringer, Dario Amodei, Tom Brown, Jack Clark, Nicholas Joseph, Ben Mann, Sam McCandlish, Chris Olah, Jared Kaplan"
year: 2022
venue: "arXiv preprint (arXiv:2207.05221)"
doi_url: "https://arxiv.org/abs/2207.05221"
---

# Language Models (Mostly) Know What They Know

## One-Sentence Summary
Large language models can (a) produce well-calibrated answer probabilities on multiple-choice and True/False questions when choices are presented in a favorable format, (b) self-evaluate the validity of their own free-form samples via a P(True) probe that improves when shown several T=1 comparison samples, and (c) be fine-tuned with a value head to predict P(IK) — the probability that "I know" the answer — which generalizes imperfectly but nontrivially across tasks and updates appropriately when given hints or source material. *(p.1, p.3-5)*

## Problem Addressed
Honesty in language models requires both that they not generate falsehoods AND that they know the limits of their own knowledge, so they can reliably convey calibrated uncertainty. Prior work leaves open: (1) whether LMs' answer probabilities are calibrated, (2) whether they can introspect on the correctness of their own generated responses, and (3) whether models can be trained to predict whether they "know" an answer in a way that generalizes out-of-distribution and accounts for context, retrieval, and hints. *(p.3-4)*

## Key Contributions
- **Calibration on MC/TF:** Large (52B) LMs are well-calibrated on BIG-Bench, MMLU, TruthfulQA (with visible choices), QuALITY, LogiQA in multiple choice and True/False formats, achieving RMS calibration error ≲ 0.04 with lettered-choices presentation and 5-shot prompting. *(p.4, p.7-10)*
- **Format sensitivity:** Replacing option (D) with "None of the Above" in MMLU significantly *harms both accuracy and calibration*; models become strongly biased against selecting that option. *(p.4, p.8-9, Fig 7)*
- **RLHF miscalibration:** Anthropic's RLHF policy is miscalibrated on BIG-Bench; it can be remediated by temperature-rescaling the RLHF policy (T > 1) without retraining, while preserving sampling behavior. *(p.4, p.11, Fig 9)*
- **P(True) self-evaluation:** Ask the model whether its own sampled answer is True/False and read P(True). Base accuracy (and thus thresholding by P(True) > 0.5) is improved over unfiltered sampling. *(p.4, p.11-13)*
- **Multi-sample improves self-eval:** Showing the model multiple T=1 samples it itself generated for the same question before eliciting P(True) significantly improves self-evaluation AUROC and Brier score, approaching calibration. *(p.4-5, p.12-13, p.33-36, Fig 10-11, Fig 30-32)*
- **P(IK) value-head:** Attach a linear value head to the model and fine-tune to predict, from just the question, the probability the model will answer correctly when sampled. On TriviaQA training, P(IK) is well-calibrated in-distribution and larger classifiers have higher AUROC. *(p.5, p.14, p.24, Fig 12-13)*
- **P(IK) OOD generalization:** P(IK) trained only on TriviaQA transfers nontrivially to Arithmetic, Lambada, Python Function Synthesis, and GSM8k/Codex HumanEval — and training on a 4-task mixture substantially improves OOD generalization, with small calibration degradation on GSM8k (slight overconfidence). *(p.14-17, p.20, Fig 14-17)*
- **P(IK) attends to context:** Prepending a Wikipedia article relevant to a TriviaQA question raises P(IK) for that question, and more relevant/longer articles produce larger increases. P(IK) for GSM8k rises when a partial-solution "hint" is given, scaling with hint size. *(p.18-19, Fig 18-19)*
- **Pretraining-distribution dependence:** Two 52B models trained on distinct pretraining distributions give partially overlapping but noticeably different P(IK) for the same TriviaQA subsets — i.e., "I know" signals are somewhat distribution-specific. *(p.20-21, Fig 20, Table 2-3)*

## Study Design (empirical)
- **Type:** Empirical probing/evaluation of large autoregressive language models; no human subjects.
- **Models:** Anthropic pretrained decoder-only LMs at roughly 800M, 2.7B, 12B (13B), and 52B parameters; one RLHF policy derived from the 52B base; one separately pretrained 52B model with a different pretraining distribution. *(p.5, p.20)*
- **Evaluation datasets (calibration + MC/TF):** BIG-Bench multiple choice + True/False (Srivastava 2022), MMLU (Hendrycks 2020), TruthfulQA (Lin 2021) with visible choices, QuALITY (Pang 2021), LogiQA (Liu 2020). *(p.5, p.7)*
- **Evaluation datasets (P(True) / P(IK)):** TriviaQA (open-book and closed-book), Lambada, Arithmetic (custom mixed-arithmetic, 10-shot), Python Function Synthesis (custom, 0-shot, 8000 functions 6000/2000 split from open-source GitHub), Codex HumanEval (Chen 2021), GSM8k (Cobbe 2021, 10-shot with chain-of-thought scored after `####`), MBPP. *(p.5, p.14, p.26-27, p.30-31, p.41)*
- **Primary metrics:** Expected Calibration Error (ECE), RMS Calibration Error, Brier Score, Area Under the ROC Curve (AUROC) for P(IK)/P(True), calibration curves (binned frequency vs. probability). *(p.24-25)*
- **Scale:** Most calibration experiments use 5-shot prompting; P(True) uses 0-shot, 1-shot (one human-written prompt), and 20-shot few-shot "comparison examples" variants. *(p.11-13, p.33)*

## Methodology

### Calibration evaluation on multiple choice
Each multiple-choice example is presented in a "lettered choices" format:
```
Question: Who was the first president of the United States?
Choices:
 (A) Barack Obama
 (B) George Washington
 (C) Michael Jackson
Answer:
```
The model's predicted probability for each choice is read from the letter token that follows "Answer:". Calibration is measured by comparing bin-averaged P(letter) to empirical accuracy. *(p.7, p.25)*

### True/False reformulation
MC questions are converted to True/False: a random candidate answer is presented and the model must output `(A) True` or `(B) False`. This tests whether models that aren't presented with choices can still produce calibrated correctness judgments. Calibration on BIG-Bench True/False is achieved with enough scale, and improves with 5-shot prompting. *(p.10, p.25, Fig 8)*

### "None of the Above" stress test
Option (D) on MMLU is replaced with "none of the above" (in some questions, the correct answer). Accuracy drops sharply across all scales, and calibration on the (D) token is especially poor: models become biased against picking "none of the above" even when it is correct. *(p.8-9, Fig 7, p.39 Fig 36)*

### RLHF temperature fix
Given a base LM with temperature T, an RLHF policy trained from it, the paper shows that simply *rescaling* the RLHF policy's logits by T > 1 recovers calibration on BIG-Bench MC, using only three distinct temperature settings. Observable accuracy is preserved because argmax at T=1 is unchanged. *(p.11, Fig 9)*

### P(True) self-evaluation protocols
Three variants, each reading the probability of the `True` token after a prompt templating:
1. **Basic self-eval (0-shot):** `Question: ...\nProposed Answer: ...\nIs the proposed answer:\n(A) True\n(B) False\nThe proposed answer is:` *(p.11)*
2. **One-example self-eval:** Prepend a human-written prompt with six worked examples from arithmetic, trivia, fill-in-the-blank types. *(p.25 A.5)*
3. **Comparison-example self-eval (20-shot):** Show the model five (or twenty) T=1 samples it just generated for the same question, then ask whether a specific candidate is true. The exposure to alternative samples improves discrimination. *(p.12-13, p.25-26, Fig 10-11)*

### P(IK) training
Attach an additional *value head* (linear projection from the final transformer hidden state, same shape as the LM head but outputting one scalar through a sigmoid) to the pretrained LM. Train with binary-cross-entropy against ground-truth labels: *(p.14, p.24)*
- For each training question, generate 30 samples (T=1) from the original pre-trained LM, grade each for correctness, and label the question with the ground-truth P(IK) = (# correct / 30). Binarize via the indicator 1{P(IK) > 0.5} when needed. *(p.14, p.25)*
- Freeze most of the model or fine-tune with the value head active — paper reports training "a few epochs" on TriviaQA with both classifier output and language-model loss. *(p.14, A.1)*
- For TriviaQA training runs, 45,000 TriviaQA questions are sampled.

### Source-material conditioning
P(IK) is evaluated with and without a background Wikipedia article prepended to the question. For relevant articles, P(IK) increases; for irrelevant articles, it does not. For GSM8k, partial solutions ("hints") of increasing length are prepended; P(IK) increases with hint length, indicating P(IK) tracks the model's updated belief state. *(p.18-19, Fig 18-19)*

### Model-model cross-evaluation
Samples generated by a small model are evaluated by a large model and vice versa. Finding: smaller-model samples are easier to evaluate (more obviously wrong), and larger evaluators are always better, even when evaluating their own samples. *(p.37 Fig 33)*

## Key Equations / Statistical Models

$$
E_{ECE} = \sum_{i=1}^{N} \frac{|B_i|}{N}\,|p_i - c_i|
$$
Expected Calibration Error over $N$ equal-mass bins; $p_i$ is the average predicted probability and $c_i$ the empirical accuracy within bin $i$. *(p.24, Eq A.1)*

$$
E_{RMS} = \sqrt{\sum_{i=1}^{N} \frac{|B_i|}{N}\,(p_i - c_i)^2}
$$
RMS Calibration Error; the paper reports this as the preferred scalar summary because it is a "sounder theoretical score." *(p.24, Eq A.2)*

$$
B = \frac{1}{N}\sum_{i=1}^{N}(p_i - c_i)^2
$$
Brier score over samples; $p_i = P(\text{True})$ for each sample, $c_i \in \{0,1\}$ is the sample correctness. For P(IK) evaluation, ground truth is binarized as $\mathbb{1}\{\text{Ground-Truth P(IK)} > 0.5\}$. *(p.25, Eq A.3)*

Entropy and loss as alternative correctness discriminators are also mentioned (Appendix B): average token loss of a sample, entropy of the answer distribution under the model, conditioning-free entropy. *(p.28-29, B.1–B.3)*

## Parameters

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Model size (LM family) | — | params | 52B | 800M–52B | 5 | 800M, 2.7B, 13B (~12B), 52B Anthropic LMs |
| Sampling temperature (base) | T | — | 1 | — | 12 | Used for generating comparison samples & P(True) evaluation |
| RLHF calibration rescale | T_fix | — | >1 | 1–2 | 11 | Three distinct values reported sufficient to restore calibration |
| Few-shot count (MMLU, TruthfulQA, LogiQA) | — | shots | 5 | 0/5 | 7, 39 | 0-shot used for QuALITY |
| Few-shot count (arithmetic) | — | shots | 10 | — | 26 | |
| Few-shot count (GSM8k) | — | shots | 10 | — | 27 | With chain-of-thought, scored after `####` |
| Few-shot count (Python Function Synthesis) | — | shots | 0 | — | 27, 30 | |
| Samples per question for P(IK) labels | — | samples | 30 | — | 14, 25 | T=1 samples used to compute ground-truth P(IK) |
| Ground-truth P(IK) binarization threshold | — | — | 0.5 | — | 25 | $\mathbb{1}\{\text{P(IK)} > 0.5\}$ for Brier/classification |
| Comparison samples in P(True) prompt | — | samples | 5 or 20 | — | 12, 33 | Five (Fig 10-11) and twenty shown as effective variants |
| TriviaQA P(IK) training set size | — | questions | 45,000 | — | 14, A.1 | |
| Python Function Synth dataset | — | functions | 8000 | — | 31 | 6000/2000 train/test split |
| Target calibration error (achieved) | E_RMS | — | ≈0.01 | <0.04 | 6, 10 | Claim about 52B on large number of BIG-Bench questions |
| Threshold used for P(True) > 0.5 filtering | — | — | 0.5 | — | 33, Fig 29 | Filtering samples with P(True) > 0.5 increases accuracy vs. unfiltered |

## Effect Sizes / Key Quantitative Results

| Outcome | Measure | Value | Population/Context | Page |
|---------|---------|-------|--------------------|------|
| Calibration on MMLU (52B, 5-shot, lettered choices) | RMS ECE | ≈0.03 (visual) | 5-shot lettered | 9, Fig 6 |
| Calibration on TruthfulQA visible-choices (52B, 5-shot) | RMS ECE | ≈0.04 | 5-shot | 9, Fig 6 |
| Calibration on BIG-Bench True/False (52B, 5-shot) | RMS ECE | Near-diagonal, improves w/ 5-shot over 0-shot | BIG-Bench TF | 10, Fig 8 |
| P(IK) AUROC (TriviaQA in-distribution, 52B) | AUROC | ≈0.88 | Train & test both TriviaQA | 16, Fig 14 |
| P(IK) AUROC (Mixed-Arith OOD, trained on TriviaQA only) | AUROC | ≈0.92 | OOD, 52B | 16, Fig 14 |
| P(IK) AUROC (Lambada OOD, trained on TriviaQA only) | AUROC | ≈0.61 | OOD, 52B | 16, Fig 14 |
| P(IK) AUROC (Python Func Synth OOD) | AUROC | ≈0.69 | OOD, 52B | 16, Fig 14 |
| P(IK) Brier score on TriviaQA (trained on all 4 tasks vs. TriviaQA only) | Brier | ≈0.063 vs ≈0.064 | 52B | 18, Table 1 |
| P(IK) Brier score on Codex HumanEval (trained on TriviaQA only) | Brier | 0.847 → 0.185 with all 4 datasets | OOD, 52B | 18, Table 1 |
| P(IK) cross-pretraining agreement | AUROC | Model A P(IK) used to predict B's correctness: 0.463 / 0.408 | 52B models from distinct pretraining dists | 21, Table 2 |
| P(True) filtered accuracy gain (52B TriviaQA) | Δ accuracy | P(True) > 0.5 filtering boosts accuracy | 20-shot comparison prompt | 33, Fig 29 |
| Codex HumanEval P(True) AUROC (52B, 20-shot) | AUROC | ≈0.82 | — | 35, Fig 31 |
| MMLU with "None of the Above": accuracy | Δ accuracy | Large decrease across scales | 5-shot replacement | 9, Fig 7 |

(Approximate values read from figures; the paper does not always tabulate exact numbers — see reproduced figures for precise readings.)

## Methods & Implementation Details
- **Probability reading:** For multiple choice, probabilities are the softmax over the single letter tokens `A`, `B`, `C`, `D` immediately after the "Answer:" token. No normalization over the full vocabulary is used. *(p.7, p.25)*
- **True/False token reading:** Use `(A)` for True and `(B)` for False, to avoid tokenizer quirks and to match training-time bias. *(p.10)*
- **Prompt format is load-bearing:** Calibration on MC depends critically on presenting options as lettered choices and asking for a single letter. Reformulating MMLU into True/False degrades accuracy and calibration. *(p.39 Fig 36-37)*
- **P(IK) classifier architecture:** A linear value head on top of the final hidden state, analogous to the LM head, outputs a single logit for P(IK) via sigmoid. Trained by binary-cross-entropy against the empirical P(IK) on sampled data. *(p.24, A.1)*
- **P(IK) training joint loss:** Mix classifier BCE loss with continuing LM loss on the same data (to keep the backbone language-modeling competent). *(p.14, A.1)*
- **P(IK) OOD generalization strategy:** Training on TriviaQA + Lambada + Mixed-Arith + Python Function Synthesis rather than any single dataset. Larger classifiers generalize more (AUROC increases with scale). *(p.14-17)*
- **Answer-sample counts for P(IK) labels:** 30 samples per question from the base LM at T=1; any sample marked correct contributes 1/30 to the ground-truth P(IK). *(p.14, p.25)*
- **Wikipedia conditioning construction:** For each TriviaQA question, the paired Wikipedia article used in the open-book split is prepended as context and P(IK) is re-evaluated. *(p.18, Fig 18)*
- **GSM8k hint construction:** For each GSM8k problem, take the chain-of-thought solution, truncate at a fraction of characters, prepend as "hint," then query P(IK). Number of hint points / characters is the independent variable. *(p.19, Fig 19)*
- **Comparison-example P(True) format:** The 20-shot comparison prompt is a human-written few-shot format; five comparison samples from the model are included along with the candidate to be judged. *(p.25-26, p.33 Fig 29)*
- **Brier-score pitfall:** Smaller models may appear to have very low Brier scores on GSM8k/Codex/HumanEval because they are almost always wrong and predict P(True) ≈ 0 uniformly — so low Brier doesn't indicate skill for small models. *(p.34, Fig 30)*

## Figures of Interest
- **Fig 1 (p.2):** Top-level summary — 52B RMS calibration on BIG-Bench (visible choices) vs. various tasks; accuracy improvement after P(True) > 0.5 filtering.
- **Fig 6 (p.9):** Calibration curves for MMLU, TruthfulQA, QuALITY, LogiQA across model sizes — large models hug the diagonal.
- **Fig 7 (p.9):** "None of the Above" stress test on MMLU — calibration collapses for the (D) token.
- **Fig 8 (p.10):** BIG-Bench True/False calibration by model size.
- **Fig 9 (p.11):** RLHF miscalibration + temperature rescaling fix.
- **Fig 10–11 (p.12-13):** Self-evaluation with comparison examples; Brier score drops with sample-showing.
- **Fig 12 (p.15):** P(IK) training histograms (correct vs incorrect separation).
- **Fig 13 (p.15):** P(IK) calibration curves on TriviaQA.
- **Fig 14 (p.16):** P(IK) AUROC vs. model size across in-dist and three OOD tasks.
- **Fig 15 (p.16):** GSM8k P(IK) calibration when training on TriviaQA only vs. 4-task mixture (4-task mixture becomes *overconfident* rather than underconfident).
- **Fig 16 (p.17):** Full P(IK) distributions across all OOD tasks for TriviaQA-only vs. 4-task training.
- **Fig 18 (p.19):** P(IK) vs. Wikipedia article relevance / length — positive slope.
- **Fig 19 (p.19):** P(IK) on GSM8k vs. number of hint points provided.
- **Fig 20 (p.20):** P(IK) scatter across two 52B models with distinct pretraining distributions.
- **Fig 28–34 (p.32-38):** Extensive appendix P(True) histograms and calibration curves across model sizes and prompting modes.
- **Fig 37 (p.39):** Accuracy on QuALITY, LogiQA, TruthfulQA, MMLU for the lettered-choices format + MMLU True/False-reformulation accuracy and AUROC.

## Results Summary
- Large (52B) LMs are well-calibrated on diverse MC tasks when choices are visible and lettered; RMS ECE can reach ≈0.01 for favorable formats. *(p.7-10)*
- Calibration requires the "natural" format: "none of the above" breaks it and True/False reformulation degrades it. Few-shot prompting helps recover. *(p.8-10)*
- RLHF policies are miscalibrated; temperature rescaling (T>1) is a simple remedy. *(p.11)*
- P(True) self-evaluation is a useful but imperfect signal: with one-shot prompts it's only moderately calibrated, but showing additional T=1 samples before asking P(True) substantially improves both AUROC and Brier score. For 20-shot comparison examples, discrimination becomes usable across Arithmetic, Lambada, TriviaQA, Codex, GSM8k. *(p.12-13, p.32-36)*
- P(IK) is well-calibrated in-distribution, with AUROC rising with model size. *(p.14-16)*
- OOD generalization is partial: some tasks (Mixed-Arithmetic, Lambada) transfer well from TriviaQA; others (Codex, Python Func Synth) require training on a mixture to reach useful AUROC; absolute calibration on fully out-of-distribution tasks (GSM8k) remains imperfect and can flip from underconfidence to overconfidence with more data diversity. *(p.16-17, Fig 15-16)*
- P(IK) updates appropriately when given relevant context (Wikipedia articles) or partial solutions (GSM8k hints). *(p.18-19)*
- Models with different pretraining distributions show different, only-partially-overlapping P(IK) on the same TriviaQA questions, suggesting knowledge state is distribution-specific and P(IK) is not a universal feature. *(p.20-21)*

## Limitations
- **Honesty vs. calibration gap:** Calibration is a weaker notion than honesty. A model might be calibrated as a frequentist without genuinely introspecting on facts; conversely a model may "know" something but be miscalibrated. *(p.22)*
- **Task format sensitivity:** Calibration is brittle under prompt reformulation — "none of the above," True/False rephrasings, or reformatting BIG-Bench questions can destroy calibration. This means simple deployments may not benefit without careful format engineering. *(p.22, p.8-10)*
- **P(IK) calibration OOD:** Although P(IK) classifiers discriminate well OOD (good AUROC), they are often miscalibrated OOD, including flipping from underconfident (TriviaQA-only training) to overconfident (4-task training) on GSM8k. *(p.17, p.22)*
- **P(IK) dependence on pretraining distribution:** P(IK) is not invariant across models with different pretraining data, so it is not a single "objective" knowledge signal. *(p.20-22)*
- **Source-material effect requires relevant material:** Irrelevant material does not increase P(IK), but the paper does not study adversarial or distracting context in depth. *(p.22)*
- **Scaling to honesty in new training regimes:** The paper studies imitation-trained LMs; it is not known whether honesty-calibration results transfer to models trained from non-imitation objectives (RL-from-scratch, world-model pretraining, etc.). *(p.22-23)*
- **Human-level comparisons not run:** The paper does not compare LM calibration to human expert calibration on the same tasks.
- **P(True) is worse than reading multiple-choice probabilities** when applicable: reformulating a task as MC with visible lettered choices generally gives better calibration than free-form sampling + P(True). *(p.10)*

## Arguments Against Prior Work
- **Against simple "entropy of answer distribution" as a knowledge signal:** The paper evaluates loss/entropy discriminators (Appendix B) and finds them less effective than either direct P(letter) reading or a trained P(IK) value head. *(p.28-29)*
- **Against naive use of multiple-choice accuracy to infer calibration:** If the format is wrong (e.g., "none of the above"), even high-accuracy models can be poorly calibrated. *(p.8-9, p.39)*
- **Against RLHF-as-calibrated:** Against assumptions that RLHF policies are "aligned" probabilistically — Anthropic's RLHF policy is noticeably miscalibrated; remediation requires temperature rescaling. *(p.11)*
- **Against reliance on single-sample P(True) for high-stakes use:** Zero-shot P(True) is poorly calibrated; at minimum a few-shot, preferably comparison-example, setup is required. *(p.12-13, p.38)*
- **Against assuming P(IK) is distribution-invariant:** Cross-pretraining experiments show P(IK) reflects an individual model's knowledge, not a ground-truth "knowability" signal. *(p.20-21)*

## Design Rationale
- **Lettered choices over free-form answers:** Reduces ambiguity in probability reading and aligns with RLHF/imitation training objectives. Single-token probabilities are a clean calibration signal. *(p.7, p.25)*
- **P(IK) as a separate classifier head, not prompt-based:** Allows training with clean supervision (sampled accuracy) without depending on prompt engineering or few-shot ordering. Enables direct AUROC/Brier evaluation. *(p.14, A.1)*
- **Mixing several training datasets for P(IK):** Improves OOD AUROC across tasks despite some calibration degradation; the trade-off is explicit. *(p.16-17)*
- **Comparison-example few-shot for P(True):** Lets the model "see its own uncertainty" by sampling alternatives before judging, which is the rationale for why showing T=1 samples improves self-eval. *(p.12-13)*
- **Temperature rescaling for RLHF:** Minimal intervention, preserves argmax, is post-hoc — preferable to retraining the policy. *(p.11)*
- **Choice of Brier + ECE + AUROC:** Complementary measures — Brier captures accuracy+calibration jointly, ECE/RMS capture probabilistic match, AUROC captures discrimination independent of calibration. *(p.5, p.24-25)*

## Testable Properties
- **TP1:** RMS calibration error on lettered-choice MMLU 5-shot decreases monotonically with model size up to 52B. *(p.9)*
- **TP2:** Replacing any MC option with "None of the Above" decreases accuracy *and* increases RMS ECE on that task across all tested model sizes. *(p.8-9)*
- **TP3:** For an RLHF policy trained on a base LM, there exists T > 1 such that rescaling logits by T reduces RMS ECE on BIG-Bench without changing argmax accuracy. *(p.11)*
- **TP4:** Zero-shot P(True) calibration is strictly worse than 20-shot comparison-example P(True) on Arithmetic, Lambada, Codex, GSM8k, TriviaQA at 52B. *(p.32-35)*
- **TP5:** P(IK) AUROC on the P(IK) training distribution is ≥ 0.85 at 52B. *(p.16, Fig 14)*
- **TP6:** P(IK) AUROC on OOD Mixed-Arithmetic is higher than on OOD Lambada for a 52B classifier. *(p.16, Fig 14)*
- **TP7:** Training P(IK) on a 4-task mixture improves AUROC on each held-in task compared to TriviaQA-only training, but changes GSM8k calibration from underconfident to overconfident. *(p.17 Fig 15-16)*
- **TP8:** P(IK) on a TriviaQA question monotonically increases with the length of a relevant Wikipedia article prepended; irrelevant articles do not raise P(IK). *(p.19 Fig 18)*
- **TP9:** P(IK) on a GSM8k problem monotonically increases with the number of chain-of-thought hint points provided. *(p.19 Fig 19)*
- **TP10:** Two distinct pretraining distributions give rise to P(IK) disagreement on TriviaQA subsets: neither model's P(IK) is strictly better than the other's at predicting the other's correctness. *(p.21 Table 2-3)*
- **TP11:** Large evaluators are always ≥ small evaluators on P(True) AUROC when grading the same samples, including their own. *(p.37 Fig 33)*
- **TP12:** Brier score for P(True) can be low for small models due to uniform near-zero predictions, so Brier alone cannot be used as a skill signal without conditioning on base accuracy. *(p.34 Fig 30)*

## Relevance to This Project
The Wabiski 2026 protocol (the systematic-review protocol this paper directory was retrieved to critique) uses LLM-confidence thresholds as part of its screening/triage. This paper is the canonical Anthropic reference showing:
1. Model *probabilities* are calibrated only under specific prompt formats — RMS ECE of 0.04 is best-case, not default.
2. Raw P(True)/P(IK) scores from a single-shot prompt are substantially worse than comparison-example or few-shot prompts; a naive threshold on zero-shot self-reported confidence can be misleading.
3. P(IK) generalization *drops* OOD: a confidence threshold tuned on one distribution (training) produces over/under-confident outputs on another (deployment), e.g., GSM8k.
4. Format changes (replacing options with "none of the above") collapse calibration — so any protocol that prompts models with questions that don't have canonical lettered-option formats is operating in the low-calibration regime.

These are the concrete mechanisms that undermine a fixed-threshold rule: any blanket "skip screening if LLM confidence > X" is suspect absent (a) format control, (b) at-deployment calibration, and (c) per-distribution validation. Kadavath supplies direct evidence for each of these failure modes, which is exactly what the author-feedback critique needs. *(p.4, p.8-9, p.11, p.17, p.22)*

## Open Questions
- [ ] How well does P(IK) transfer to non-English or domain-specialized corpora? (Paper only evaluates English, mostly trivia/math/code.)
- [ ] Is there a format-agnostic P(IK) probe that survives adversarial prompt rewriting?
- [ ] Can the temperature-rescaling fix for RLHF be extended to instruction-tuned or DPO-trained policies?
- [ ] How do P(IK) values evolve during multi-turn dialogue as the model accumulates context?
- [ ] What is the exact architecture and training schedule of the value head? (Paper gives a schematic; full hyperparameters are not disclosed in the main text.)

## Collection Cross-References

### Already in Collection
- [[Lin_2022_TeachingModelsExpressUncertainty]] — Complementary finetuning-based approach to verbalized uncertainty. Lin et al. supervise-finetune GPT-3 to emit verbalized confidence and show it generalizes under distribution shift; Kadavath et al. trained a dedicated P(IK) value head instead. Both papers show that a learned self-knowledge signal is distinct from raw answer-token probability.
- [[Tian_2023_JustAskCalibrationStrategies]] — Tian et al. use Kadavath's P(True) self-evaluation as a direct baseline and show that plain verbalized numeric probability outperforms it on RLHF-LMs; Kadavath's finding that RLHF policies are miscalibrated (p.11) is what Tian et al. then route around.
- [[Xiong_2024_LLMUncertaintyConfidenceElicitation]] — Xiong et al. extend Kadavath's black-box question to a full prompting × sampling × aggregation framework and argue that Kadavath-style token-likelihood methods capture next-token uncertainty rather than semantic-level uncertainty (Xiong p.1-2).
- [[Wabiski_2026_CognitiveReviewProtocol]] — Direct critique target. See `papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md` §2.2(g) for the specific use of Kadavath's format-sensitivity and RLHF-miscalibration results against the protocol's `>0.90 auto-include` rule.

### Cited By (in Collection)
- [[Tian_2023_JustAskCalibrationStrategies]] — Uses P(True) self-evaluation (from this paper) as a calibration baseline.
- [[Xiong_2024_LLMUncertaintyConfidenceElicitation]] — Cites Kadavath as canonical token-likelihood self-evaluation work.
- [[Lin_2022_TeachingModelsExpressUncertainty]] — Cites Kadavath as complementary probing-the-model line of work.

### Conceptual Links (not citation-based)
- [[Brock_2015_InteractiveMapsUsability]] — Strong. Brock provides the human analogue of Kadavath's LLM self-knowledge question: blind users' self-reported confidence after tactile map exploration correlates with spatial scores short-term but NOT long-term (landmarks decay ~45% while confidence holds). Cross-species replication of "confidence is a noisy proxy for retained knowledge" — both papers support the Wabiski_2026 critique that confidence-based screening thresholds need empirical validation, not face validity.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Moderate. Wabinski 2022 is the tactile-map design guideline the 2026 protocol builds on; Kadavath's format-sensitivity findings argue that any LLM-based extraction of Wabinski's parameters would be format-fragile.

## Related Work Worth Reading
- Lin et al. 2022, "Teaching Models to Express Uncertainty in Words" — complementary work on verbalized uncertainty (already in this collection). → NOW IN COLLECTION: [[Lin_2022_TeachingModelsExpressUncertainty]]
- Guo et al. 2017, "On Calibration of Modern Neural Networks" — temperature-scaling baseline.
- Desai & Durrett 2020 — calibration of pretrained transformers on NLP tasks.
- Jiang et al. 2021 — calibration of generative QA models.
- Srivastava et al. 2022 — BIG-Bench paper, for the dataset used throughout.
- Hendrycks et al. 2020/2021 — MMLU and related benchmarks.
- Christiano et al. 2017 / Bai et al. 2022 — RLHF / HH background.
- Naeini et al. 2015 — ECE definition.
- Cobbe et al. 2021 — GSM8k, used as a key OOD benchmark here.
