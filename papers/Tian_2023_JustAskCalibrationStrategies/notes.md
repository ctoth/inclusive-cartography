---
title: "Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback"
authors: "Katherine Tian, Eric Mitchell, Allan Zhou, Archit Sharma, Rafael Rafailov, Huaxiu Yao, Chelsea Finn, Christopher D. Manning"
year: 2023
venue: "EMNLP 2023"
doi_url: "https://arxiv.org/abs/2305.14975"
arxiv_id: "2305.14975"
---

# Just Ask for Calibration: Strategies for Eliciting Calibrated Confidence Scores from Language Models Fine-Tuned with Human Feedback

## One-Sentence Summary
A systematic empirical study showing that for RLHF-fine-tuned language models (GPT-4, ChatGPT, Claude 1/2, Llama-2-70B-chat), simply asking the model to verbalize its own confidence as a percentage or linguistic expression yields substantially better-calibrated probabilities than either (a) the model's conditional token-level likelihoods or (b) P(True) self-evaluation, reducing Expected Calibration Error (ECE) by roughly 50% on TriviaQA, SciQ, and TruthfulQA without any fine-tuning or labeled calibration data. *(p.0, p.1)*

## Problem Addressed
Well-calibrated confidence is important for the safe and transparent deployment of language models: a calibrated model's stated confidence should match the empirical frequency of being correct. Prior calibration work for LMs (Kadavath 2022 etc.) focused on base, non-RLHF models and used conditional token probabilities or P(True) prompting. Tian et al. observe two problems with this for RLHF-fine-tuned chatbots: *(p.0, p.1)*

1. **RLHF breaks token-probability calibration.** Conditional probabilities of RLHF-LMs are miscalibrated — often overconfident — compared with non-RLHF base models. RLHF training on human preferences pushes probability mass onto preferred sequences in a way that distorts the marginal likelihood of being correct. *(p.0, p.1)*
2. **Many deployed RLHF-LMs (GPT-4, ChatGPT, Claude) do not expose token-level logits at all,** so any calibration approach that needs conditional probabilities is infeasible for these closed-API models. *(p.1, p.2)*

The paper asks whether a purely prompt-based ("just ask") approach — eliciting a probability directly from the model's text output — can recover good calibration on RLHF-LMs even though their logits don't.

## Key Contributions
- Demonstrates empirically that **verbalized probabilities** (the model states a numeric percentage in [0, 1]) from RLHF-LMs are substantially better calibrated than their conditional token probabilities, achieving ~50% lower ECE on average across TriviaQA, SciQ, TruthfulQA, and across GPT-4, ChatGPT, Claude-1, Claude-2, and Llama-2-70B-chat. *(p.0, p.1)*
- Compares several concrete elicitation strategies: (a) verbalized numeric probability in 0/1 format; (b) verbalized linguistic likelihood expressions ("Highly Unlikely" ... "Almost Certain") mapped to numeric buckets; (c) top-k sampling with per-answer confidences (then averaging or taking max). *(p.2, p.3, p.4)*
- Shows that asking for **top-k candidate answers each with a confidence** beats asking for only a single best guess: providing alternatives reduces overconfidence, and the induced distribution over alternatives better calibrates the chosen answer. *(p.3, p.4)*
- Shows that verbalized probabilities are useful even when the accuracy of top-1 selection is worse than picking the argmax of the likelihood model — i.e., the verbalized confidences provide a *calibration signal that is almost orthogonal* to which answer the model would pick greedily. *(p.0, Fig. 1)*
- Provides a simple recipe ("just ask for calibration") that requires **no fine-tuning, no logits access, and no labeled calibration data**, making it applicable to closed-API RLHF-LMs where existing calibration techniques (temperature scaling, fine-tuning-based calibration) cannot be applied. *(p.0, p.1)*

## Study Design (empirical paper)
- **Type:** Empirical benchmark comparison of calibration elicitation methods on RLHF-fine-tuned LMs.
- **Models evaluated:** GPT-4 (`gpt-4-0314`), ChatGPT (`gpt-3.5-turbo-0301`), Claude-1 (`claude-1`), Claude-2 (`claude-2`), Llama-2-70B-chat. *(p.2)* The first four are closed APIs with no logit access; Llama-2-70B-chat is an open-weights RLHF model. *(p.2)*
- **Datasets:** TriviaQA, SciQ, and TruthfulQA. *(p.2, p.3)* These cover open-domain factoid QA (TriviaQA), science QA (SciQ), and adversarially-constructed questions designed to elicit false common misconceptions (TruthfulQA).
- **Primary metrics:** Expected Calibration Error (ECE), accuracy (for top-1 selection quality), and AUC (area under the selective-prediction or confidence-ordering curve). *(p.2, p.3)*
- **Baselines:**
  - **P(True) self-evaluation** (Kadavath et al. 2022): prompt the model to say "True"/"False" about its own answer, take P("True") as the confidence. *(p.1, p.2)*
  - **Conditional probability**: the product over tokens of the model's output distribution for the answer string, applicable only where logits are exposed (i.e., Llama-2-70B-chat; not possible for GPT-4/ChatGPT/Claude). *(p.2)*
  - **Temperature scaling** and fine-tuning-based calibration are discussed as prior work but cannot be applied to closed-API models. *(p.1)*
- **Judging correctness:** Because RLHF-LMs often answer in freeform text, exact-match scoring is unreliable. The authors use GPT-4 as an LLM-as-judge to decide semantic equivalence between a gold answer and a predicted answer via a prompt that asks "Are the following two answers to my question Q semantically equivalent?" *(p.9 — see appendix prompt)* This was calibrated to have reasonable agreement with a human evaluator on TriviaQA.

## Methodology
Three families of "just ask" elicitation strategies are evaluated, each entirely prompt-based and post-hoc:

### 1. Verbalized numeric probability
Ask the model to produce a single best-guess answer together with a probability in [0, 1] (or percentage in [0%, 100%]) representing its confidence that the answer is correct. The numeric probability is parsed out of the response. *(p.2, p.3)*

### 2. Verbalized linguistic likelihood expression
Ask the model to choose from a fixed menu of qualitative likelihood phrases. Each phrase is then mapped to a numeric bucket. *(p.3, p.4, p.7)* The mapping used in this paper: *(p.4)*

| Linguistic expression | Mapped probability |
|---|---|
| Highly Unlikely | 0.1 |
| Unlikely | 0.3 |
| Somewhat Unlikely | 0.4 |
| Uncertain / Somewhat | 0.5 |
| Likely / Somewhat Likely | 0.7 |
| Highly Likely | 0.9 |
| Almost Certain | 0.95 |

The authors observe that models tend to concentrate their output on a subset of expressions — the empirical histogram of linguistic-expression use is non-uniform (appendix Figure 3/4, p.7) — and that some linguistic buckets are nevertheless well-calibrated against empirical correctness. *(p.7)*

### 3. Top-k with verbalized confidences
Prompt the model to list its top-k candidate answers, each with its own confidence. *(p.3, p.4, p.8)* Two variants are evaluated:

- **Average / combined**: the verbalized confidence of the top-1 candidate in the top-k list.
- **Max / normalized**: normalize across top-k to form a distribution, take the confidence of the chosen answer.

Top-k elicitation consistently improves over asking for just the single best answer because it forces the model to apportion belief across alternatives, reducing overconfidence on the single answer. *(p.3, p.4)*

### Two-step ("verbalized 2S") variant
The abstract figure (Fig. 1) highlights a **2-step** protocol: first ask the model for an answer, then in a separate turn ask it to rate the confidence of that answer. This is the headline result: verbalized 2-step confidence is better calibrated than logit-based conditional probability on RLHF-LMs. *(p.0, Fig. 1)*

## Key Equations / Statistical Models

### Expected Calibration Error (ECE)
The primary calibration metric. For a model that outputs (answer, confidence) pairs, partition the predictions into equal-width confidence bins and compare the average confidence in each bin to the accuracy in that bin:

$$
\mathrm{ECE} = \sum_{b=1}^{B} \frac{|S_b|}{N} \big|\, \mathrm{acc}(S_b) - \mathrm{conf}(S_b) \,\big|
$$
Where: $B$ = number of bins, $S_b$ = predictions falling in bin $b$, $N$ = total predictions, $\mathrm{acc}(S_b)$ = empirical accuracy in bin $b$, $\mathrm{conf}(S_b)$ = mean confidence in bin $b$. A perfectly calibrated model has $\mathrm{ECE} = 0$. *(p.1, p.2)*

### Conditional (likelihood) probability baseline
For a tokenized answer $y = (y_1, \ldots, y_T)$ given prompt $x$:

$$
p_{\mathrm{cond}}(y \mid x) = \prod_{t=1}^{T} p_\theta(y_t \mid x, y_{<t})
$$
Where: $p_\theta$ is the model's next-token distribution. Applicable only where token logits are available; for Llama-2-70B-chat in this paper. *(p.2)*

### P(True) baseline
Given a prompt $x$ and a candidate answer $\hat{y}$ produced by the model, construct a second prompt that asks "Is the following answer correct? (True/False)" and take the model's probability of the token "True":

$$
p_{\mathrm{P(True)}}(\hat{y} \mid x) = p_\theta(\text{``True''} \mid \text{eval-prompt}(x, \hat{y}))
$$
Where: eval-prompt is the self-evaluation wrapper from Kadavath et al. 2022. *(p.1, p.2)*

## Parameters

### Evaluation configuration

| Name | Symbol | Units | Default | Range | Page | Notes |
|---|---|---|---|---|---|---|
| Number of calibration bins | B | — | — | — | p.1-2 | Standard ECE binning (authors do not emphasise an unusual choice) |
| Top-k candidates | k | — | — | varied (e.g., 1, 4) | p.3-4 | Asking for more candidates generally improves calibration |
| Sampling temperature (generation) | T | — | 1.0 | — | p.2, p.8 | Standard-for-API generation |

### Linguistic expression → probability mapping

| Name | Symbol | Units | Default | Range | Page | Notes |
|---|---|---|---|---|---|---|
| Highly Unlikely | — | — | 0.1 | — | p.4 | Bottom of verbalization scale |
| Unlikely | — | — | 0.3 | — | p.4 | |
| Somewhat Unlikely | — | — | 0.4 | — | p.4 | |
| Uncertain / Somewhat | — | — | 0.5 | — | p.4 | Chance level |
| Likely / Somewhat Likely | — | — | 0.7 | — | p.4 | |
| Highly Likely | — | — | 0.9 | — | p.4 | |
| Almost Certain | — | — | 0.95 | — | p.4 | Top of verbalization scale |

## Effect Sizes / Key Quantitative Results

### Headline ECE reductions (directional)

| Outcome | Measure | Value | CI | p | Population/Context | Page |
|---|---|---|---|---|---|---|
| Verbalized vs. conditional prob ECE | relative ECE reduction | ~50% | — | — | Average across GPT-4/ChatGPT/Claude-1/Claude-2/Llama-2-70B-chat × TriviaQA/SciQ/TruthfulQA | p.0, p.1 |

### Tables 1-3 patterns (p.2-3)
The paper's tables 1-3 compare elicitation methods across models × datasets on ECE, accuracy, and AUC. Exact numeric cells were read from the page images; representative observations:

- **GPT-4 on TriviaQA:** verbalized numeric 2-step achieves ECE ≈ 0.039 — substantially lower than P(True) and conditional baselines. *(p.2, Table 1)*
- **Claude-2 on SciQ:** verbalized numeric 2-step achieves ECE ≈ 0.028. *(p.3, Table 2)*
- **Llama-2-70B-chat (only model with logit access):** conditional probability is *worse* calibrated than verbalized probability, even though verbalization is text-only. This is the core claim that RLHF specifically breaks logit-based calibration. *(p.2-3)*
- **Top-k with average beats 1-of-1 across the board** — providing alternatives is essential for eliciting useful confidence. *(p.3, p.4)*
- **Linguistic expressions** are competitive with numeric probabilities on some models/datasets but under-use parts of the scale (appendix histograms p.7).

Because Tables 1-3 are dense and the exact per-cell numbers require Table reconstruction, practitioners implementing this paper should consult the originals (p.2, p.3, Tables 1-3).

## Methods & Implementation Details
- **Prompt templates are given verbatim in the appendix (p.8).** The main templates: *(p.8)*
  - **Label prompt (just ask, one-shot):** Provide a question, ask for the answer and a probability in [0, 1], one at a time or as a tuple.
  - **Two-step prompt:** Prompt 1 asks for the answer; Prompt 2 takes that answer as input and asks "Provide the probability that the answer is correct. Give ONLY the probability, between 0.0 and 1.0, no other words or explanation."
  - **Linguistic prompt:** "Provide the likelihood of your answer being correct using the following set: {Highly Unlikely, Unlikely, Somewhat Unlikely, Somewhat Likely, Likely, Highly Likely, Almost Certain}."
  - **Top-k prompt:** "Provide your 4 best guesses along with the probability that each is correct..."
- **Parsing the verbalized response:** Regex/string parsing pulls out the numeric percentage or the linguistic phrase. For top-k, parse k tuples of (answer, probability). *(p.3, p.4)*
- **Correctness judging via GPT-4:** For TriviaQA and other freeform QA, pass (question, gold, predicted) to GPT-4 with the semantic-equivalence template (p.9 appendix) and treat "Yes" as correct. This choice was validated against a human evaluator to confirm reasonable agreement. *(p.5)*
- **Model-specific quirks:** Closed-API RLHF-LMs (GPT-4, ChatGPT, Claude) have no direct logit access → only verbalization-based methods apply. Llama-2-70B-chat is the only model where conditional-probability baseline is directly computable. *(p.1, p.2)*
- **No fine-tuning, no labeled calibration data, no temperature scaling** — calibration comes entirely from the prompt. *(p.0, p.1)*

## Figures of Interest
- **Fig. 1 (p.0):** Headline figure: verbalized 2-step confidence is better calibrated (lower ECE, on average) than conditional probability for RLHF-LMs, across several models and datasets. Also notes that verbalization is useful even when the top-1 answer is worse than the argmax of the likelihood model — confidence and selection quality are partially orthogonal. *(p.0)*
- **Tables 1-3 (p.2, p.3):** Per-(model × dataset) comparison of all elicitation methods on ECE / accuracy / AUC.
- **Fig. 3 / Fig. 4 — linguistic expression histograms (p.7, appendix A):** Usage distribution of the verbalized linguistic phrases by Llama-2-70B-chat (p.7 top) and GPT-4 (p.7 bottom) on SciQ/TriviaQA/TruthfulQA. Models concentrate probability mass on a subset of phrases (the "Likely"/"Highly Likely"/"Almost Certain" end), under-using the unconfident end.
- **Fig. 5 — calibration curves (p.7):** Reliability diagrams for selected methods × datasets after the histogram panel.

## Results Summary
- **Verbalized confidence beats conditional probability for RLHF-LMs.** On average across GPT-4, ChatGPT, Claude-1, Claude-2, and Llama-2-70B-chat × TriviaQA/SciQ/TruthfulQA, verbalized probabilities reduce ECE by approximately 50% relative to conditional probabilities. *(p.0, p.1)*
- **Verbalized confidence beats P(True).** Across models and datasets, prompting for a numeric probability in one or two steps outperforms Kadavath et al.'s P(True) self-evaluation. *(p.2, Tables 1-3)*
- **Top-k elicitation helps across the board.** Asking for multiple candidate answers with individual probabilities improves calibration relative to asking for only one best answer. *(p.3, p.4)*
- **Linguistic expressions are viable.** Despite only using a discrete 7-ish-valued scale, linguistic expressions achieve competitive ECE on several model/dataset combinations, though models concentrate their usage on a subset of phrases. *(p.4, p.7)*
- **Verbalization helps even when accuracy is worse.** Figure 1 specifically flags that verbalized 2-step can deliver better calibration even when, on top-1 accuracy alone, the model is outperformed by picking the argmax of its token distribution. This matters for selective-prediction / abstention decisions. *(p.0)*
- **Claude-2 and GPT-4 are the best-calibrated** under verbalization on the benchmarks reported; Llama-2-70B-chat trails but still benefits substantially from verbalization over its own logits. *(p.2-3)*

## Limitations
- **Datasets are short-form QA.** The paper's benchmarks (TriviaQA, SciQ, TruthfulQA) are factoid-style. It is not directly shown that "just ask" calibration generalizes to long-form generation, multi-step reasoning, code, or dialogue tasks. *(p.4, p.5)*
- **LLM-as-judge for correctness is imperfect.** The correctness labels used to compute ECE/accuracy come from GPT-4 as a judge; human-agreement was measured but is imperfect. Any systematic judging errors propagate into reported calibration numbers. *(p.5, p.9)*
- **Linguistic mapping is arbitrary.** Mapping words to numeric probabilities uses a fixed author-chosen table; different mappings could shift conclusions for the linguistic method. *(p.4, p.7)*
- **Closed-API models' behaviour may change between snapshots.** Results are tied to dated model versions (`gpt-4-0314`, `gpt-3.5-turbo-0301`, `claude-1`, `claude-2`). *(p.2)* Reproducibility over time is uncertain.
- **No labeled calibration data used** is both a strength (cheap, deployment-friendly) and a limitation (no supervised refinement of the mapping from verbalized phrase → probability).
- **Only evaluates in-distribution knowledge questions.** Does not measure calibration under distribution shift, adversarial attacks, or tool-use scenarios.

## Arguments Against Prior Work
- **Kadavath et al. 2022 (P(True), P(IK)):** Established self-evaluation prompts on non-RLHF base LMs. Tian et al. show that (a) P(True) is worse than plain verbalized probability on modern RLHF-LMs and (b) Kadavath's methods don't straightforwardly transfer to RLHF-fine-tuned chatbots whose token distributions have been distorted by preference optimization. *(p.0, p.1)*
- **Use of conditional token probabilities (e.g., Xiao et al. 2022, Kuhn et al. 2022, Mielke et al. 2022, Kadavath et al. 2022):** These approaches assume logit access and a non-distorted token distribution. Tian et al. show that both assumptions fail for deployed RLHF chatbots: GPT-4/ChatGPT/Claude have no logit access at all, and even where logits are available (Llama-2-70B-chat), RLHF breaks their calibration. *(p.1, p.2)*
- **Temperature scaling (Guo et al. 2017) and fine-tuning-based calibration (Jiang et al. 2021, Lin et al. 2022):** Cannot be applied to closed-API RLHF-LMs because they require logit access and/or a held-out calibration set with labels and retraining capacity. *(p.1)*
- **Simple "just ask" intuition without study:** Tian et al. also push back on the implicit assumption that RLHF-LM's verbalized confidences would be useless hallucinations — empirically they are more useful than the base-LM community's preferred logit-based methods. *(p.0)*

## Design Rationale
- **Prompt-only calibration.** Chosen because it is the only viable calibration approach for closed-API RLHF-LMs (no logits, no fine-tuning). Also zero infrastructure cost — no held-out calibration data required. *(p.0, p.1)*
- **Two-step over one-step prompting.** Separating the answer and the confidence into two turns avoids entangling the model's uncertainty expression with its answer generation; the headline result uses this 2-step protocol. *(p.0, Fig. 1)*
- **Top-k over single-best.** Forces the model to spread belief mass across alternatives, reducing overconfidence on the chosen answer. *(p.3, p.4)*
- **Linguistic expressions as an alternative to numerics.** Acknowledges that some users or downstream systems may prefer qualitative labels; shows these can also be calibrated with a fixed mapping. *(p.4, p.7)*
- **GPT-4-as-judge for correctness.** Chosen because exact-match is too strict on freeform RLHF-LM outputs; validated against human labels. *(p.5)*

## Testable Properties
- **Verbalized ECE < conditional-probability ECE for RLHF-LMs on factoid QA.** *(p.0, p.1, Tables 1-3)*
- **Verbalized 2-step ECE < verbalized 1-step ECE (directionally).** *(p.0, Fig. 1)*
- **Top-k with k > 1 reduces ECE compared with single-best on the same model/dataset.** *(p.3, p.4)*
- **Verbalized confidence can provide useful selective-prediction ordering even when top-1 accuracy is below logit-argmax accuracy** (AUC metric in Tables 1-3). *(p.0, p.3)*
- **Linguistic expression histograms are non-uniform** — models prefer the "likely"/"highly likely"/"almost certain" end of the scale. *(p.7 appendix histograms)*
- **Mapping linguistic phrase → probability is stable across TriviaQA/SciQ/TruthfulQA in the sense that a single mapping yields reasonable ECE across all three datasets for GPT-4 / Claude-2.** *(p.4, p.7)*

## Relevance to Project
This paper is retrieved specifically to back the author-feedback critique of Wabinski 2026's confidence-threshold rule. Wabinski 2026 proposes using LLM-reported confidence scores as a gating mechanism for systematic-review screening decisions; Tian et al. 2023 directly characterises what such scores mean when elicited from RLHF-fine-tuned chatbots (GPT-4, ChatGPT, Claude):

1. **Verbalized confidences from RLHF-LMs are not garbage.** Tian et al. provide evidence that, with the right prompt (2-step, or top-k with confidences), verbalized numeric probabilities on factoid QA achieve ECE on the order of 0.03-0.04 for GPT-4 / Claude-2 — i.e., roughly ±3-4 percentage points on average between stated confidence and empirical correctness. This is *non-trivially* calibrated and provides empirical grounding for using a confidence threshold at all. *(p.0, p.2, p.3)*
2. **But the absolute magnitude matters.** Even the best RLHF-LMs have ECE in the 0.03-0.10 range on in-distribution factoid QA. For a threshold rule like "include if confidence ≥ τ", this means the empirical include-rate in the bin near τ can be off by several percentage points — a systematic-review protocol needs to reason about this directly rather than treating the threshold as exact. *(p.2-3, Tables)*
3. **Linguistic expressions are concentrated on the high-confidence end of the scale.** *(p.7)* This matters for Wabinski's protocol if it also uses qualitative confidence labels: models may almost never use "Unlikely" / "Highly Unlikely", so a rule like "reject if LM says Unlikely" would fire essentially never and provide no real filtering.
4. **Distribution shift not evaluated.** Tian et al. only measure calibration on in-distribution factoid QA. Systematic-review screening is out-of-distribution relative to TriviaQA/SciQ/TruthfulQA; calibration could be worse or better there, and Wabinski's protocol should not assume it inherits the ECE numbers from this paper. *(Limitations, p.4)*
5. **Top-k elicitation is a concrete improvement hook.** If Wabinski 2026 asks only for a single include/exclude decision with a confidence, rewriting the prompt to elicit top-k (include + exclude + defer, each with a confidence) is expected to reduce ECE per Tian et al. *(p.3, p.4)*
6. **2-step elicitation is a second concrete improvement hook.** Separating the screening decision from the confidence rating into two turns tends to improve calibration; this is a cheap protocol fix. *(p.0, Fig. 1)*

## Open Questions
- [ ] Does the ECE ≈ 0.03-0.10 range generalize to long-form, multi-paragraph reasoning tasks (e.g., abstract-level inclusion decisions for a systematic review)?
- [ ] Does top-k elicitation help for classification-style prompts (include/exclude) with only 2-3 real classes, or does "top-k" degenerate?
- [ ] What happens to calibration when the RLHF model is explicitly told the cost of a false positive vs. false negative (as might happen in an "inclusive" systematic-review screen)?
- [ ] How stable are these calibration numbers across closed-API model snapshots? *(Ties to the reproducibility concern on p.2)*
- [ ] Can the fixed linguistic-to-probability mapping be fit to a small labeled calibration set to produce model-specific improvements? The authors deliberately don't try this.

## Related Work Worth Reading
- **Kadavath et al. 2022** — "Language Models (Mostly) Know What They Know": the P(True)/P(IK) self-evaluation baseline that Tian et al. beat. *(p.1, p.5-6 refs)*
- **Lin, Hilton & Evans 2022** — "Teaching Models to Express Their Uncertainty in Words": prior work on verbalized uncertainty (already in this project's collection as `Lin_2022_TeachingModelsExpressUncertainty`). *(p.0-1, p.5-6 refs)*
- **Desai & Durrett 2020** — Calibration of pre-trained transformers. *(p.1, p.5-6 refs)*
- **Guo et al. 2017** — "On Calibration of Modern Neural Networks" (temperature scaling). *(p.1, p.5-6 refs)*
- **Xiao et al. 2022; Kuhn et al. 2022; Mielke et al. 2022** — Other prior work on LM uncertainty quantification. *(p.1, p.5-6 refs)*
- **Jiang et al. 2021** — Fine-tuning for calibration. *(p.1, p.5-6 refs)*

## Collection Cross-References

### Already in Collection
- [[Kadavath_2022_LanguageModelsMostlyKnow]] — Tian et al. use Kadavath's **P(True) self-evaluation** as a baseline and show it is outperformed by verbalized numeric / linguistic confidences on RLHF-LMs. Kadavath's work also noted that "RLHF policies are miscalibrated; temperature rescaling (T>1) restores calibration" — Tian et al. extend this by showing that text-level verbalization (no logits, no temperature) restores calibration even better, and specifically for deployed closed-API RLHF-LMs where Kadavath's temperature fix cannot be applied.
- [[Lin_2022_TeachingModelsExpressUncertainty]] — Lin et al. first demonstrated that GPT-3 can be **supervised-finetuned** to emit verbalized numeric or verbalized-word confidence, and that such signals are better calibrated than the answer-logit baseline under distribution shift. Tian et al. show that for RLHF-fine-tuned successors (GPT-4, ChatGPT, Claude-1/2, Llama-2-70B-chat) the **same signal can be elicited without any fine-tuning** — pure prompting suffices, and two-step and top-k elicitation protocols reduce ECE by ~50% vs. conditional probabilities. Lin et al.'s setup required labeled data and model weights; Tian et al.'s is zero-shot and works over closed APIs.

### New Leads (Not Yet in Collection)
- Xiong et al. 2024 — "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs" — flagged in Wabiski_2026/author-feedback.md §2.5 as the fourth paper in the "can we trust LLM-reported confidence" cluster; follow-up study to Tian et al. worth retrieving.
- Kuhn, Gal & Farquhar 2023 — "Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation" — alternative uncertainty-estimation method for generative LMs that operates on meaning rather than tokens; complementary to "just ask".
- Zhou, Jurafsky & Hashimoto 2023 — "Navigating the Grey Area: Expressions of Overconfidence and Uncertainty in Language Models" — characterizes how LMs hedge and express overconfidence; directly relevant to the linguistic-expression histograms in Tian et al.'s appendix.
- Guo, Pleiss, Sun & Weinberger 2017 — "On Calibration of Modern Neural Networks" — canonical ECE / temperature-scaling reference.
- Xiao et al. 2022 — "Uncertainty Quantification with Pre-trained Language Models: A Large-Scale Empirical Analysis" — the Tian et al. paper is a direct conceptual successor.

### Cited By (in Collection)
- [[Brock_2015_InteractiveMapsUsability]] — Brock's own reconciliation pass (done by a peer worker earlier today) flagged Tian et al. as a conceptual link: Brock shows that asking humans for Likert confidence ratings produces a short-term-valid but long-term-invalid signal, which is a human-side parallel to Tian et al.'s observation that RLHF-LM verbalized confidence is useful but imperfectly calibrated. The connection argues that any confidence-threshold screening pipeline needs longitudinal validation of the confidence signal, whether the rater is a human or an LLM.
- [[Xiong_2024_LLMUncertaintyConfidenceElicitation]] — Xiong et al. cite Tian 2023 as the closest concurrent prior work and directly nuance Tian's positive result: where Tian reports best-case ECE ≈ 0.03-0.04 on in-distribution factoid QA, Xiong shows this is partly achieved by assigning 100% confidence to every answer (ECE 0.064 via uniform-100 on GSM8K) while AUROC is near random, and extends the design space to prompting × sampling × aggregation across 8 datasets × 5 models.
- [[Kadavath_2022_LanguageModelsMostlyKnow]] — Kadavath 2022 (Anthropic) is cited by Tian as a baseline; reciprocally Kadavath's Cited By section notes Tian uses P(True) self-evaluation from Kadavath as a calibration baseline.
- [[Lin_2022_TeachingModelsExpressUncertainty]] — Lin 2022's Cited By section notes Tian's zero-shot prompting setup as the natural successor to Lin's supervised-finetuning approach.

### Conceptual Links (not citation-based)
- [[Wabiski_2026_CognitiveReviewProtocol]] — **Direct target of the author-feedback critique.** Wabiski's protocol (§3.5) hardcodes LLM screening thresholds `>0.90 auto-include`, `0.70-0.90 human review`, `<0.70 exclude` *(Wabiski p.6, eq. notes.md line 58)* without citing any LLM-calibration literature. Tian et al. provide the empirical grounding that verbalized confidences from GPT-4 / Claude-2 are *roughly* calibrated (ECE ≈ 0.03-0.04 on in-distribution factoid QA) but (a) only if elicited via two-step or top-k prompting, (b) only on in-distribution tasks — not necessarily systematic-review screening, which is OOD relative to TriviaQA/SciQ/TruthfulQA, and (c) even at best there is a several-percentage-point gap between stated and empirical correctness at any given threshold. This supports the Wabiski_2026/author-feedback.md §2.5 position that the 0.90/0.70 threshold rule is not justified by the literature without a calibration pre-flight step. Tian et al. also suggests two concrete cheap fixes: rewrite the screening prompt as **top-k (include, exclude, defer) with per-class verbalized confidences**, and/or use a **two-step prompt** (first the decision, then the confidence).
- [[Brock_2015_InteractiveMapsUsability]] — See "Cited By" above; the Brock→Tian link was established by Brock's own reconciliation pass and is genuinely conceptual (human-side calibration of self-reported confidence).

