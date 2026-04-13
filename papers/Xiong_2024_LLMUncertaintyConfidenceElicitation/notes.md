---
title: "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs"
authors: "Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie Fu, Junxian He, Bryan Hooi"
year: 2024
venue: "ICLR 2024"
doi_url: "https://arxiv.org/abs/2306.13063"
---

# Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs

## One-Sentence Summary
An empirical benchmark showing that black-box LLMs are systematically overconfident when asked to verbalize confidence, introducing a three-component framework (prompting strategy x sampling strategy x aggregation strategy) evaluated across 5 models and 8 datasets, with Top-K + Self-Random + Avg-Conf/Pair-Rank as the recommended stable configuration. *(p.1)*

## Problem Addressed
Prior confidence elicitation methods for neural models depend on white-box access to token logits or on model fine-tuning. Closed-source commercial LLM APIs (GPT-3.5, GPT-4) expose only text in/text out, so those methods do not apply. Token-level likelihood also fails to capture semantic-level uncertainty (e.g., "Chocolate milk comes from brown cows" has locally high token probabilities but is globally false). There is no systematic framework for eliciting confidence from black-box LLMs. *(p.1-2)*

## Key Contributions
- Defines confidence elicitation as a black-box problem and a three-component framework: prompting strategy, sampling strategy, aggregation strategy. *(p.2-3)*
- Benchmarks 5 LLMs (GPT-3, GPT-3.5, GPT-4, Vicuna-13B, LLaMA2-70B) x 8 datasets x 2 task types (calibration + failure prediction). *(p.5)*
- Shows that vanilla verbalized confidence is severely overconfident: values cluster at 80-100% in multiples of 5, mimicking human dialogue patterns from training corpora. *(p.6)*
- Shows that human-inspired prompts (CoT, Self-Probing, Multi-Step, Top-K) reduce ECE largely by raising accuracy, *not* by improving the ability to distinguish correct from incorrect answers. *(p.7-8)*
- Shows that variance across sampled responses (M=5) improves both ECE and AUROC, especially on arithmetic tasks (GSM8K AUROC 54.8 -> 92.7). *(p.8)*
- Introduces Pair-Rank aggregator with closed-form reduction (Proposition 3.1) showing P(Su > Sv) = P(Su)/(P(Su)+P(Sv)) under Top-K sampling without replacement. *(p.5, Appendix A p.14-15)*
- Narrow white-box vs black-box gap in AUROC: best white-box 0.605 vs best black-box 0.522, meaning even with logit access the field is far from solved. *(p.9, Appendix B.1 p.16-17)*

## Study Design (empirical paper)
- **Type:** Empirical benchmark / comparative evaluation of confidence elicitation methods.
- **Population:** 5 LLMs x 8 QA datasets. Models: GPT-3 (175B), GPT-3.5-turbo, GPT-4, Vicuna-13B, LLaMA2-70B. *(p.6)*
- **Intervention(s):** Prompting strategies (Vanilla, CoT, Self-Probing, Multi-Step, Top-K), sampling strategies (Self-Random, Prompting/paraphrase, Misleading), aggregation strategies (Consistency, Avg-Conf, Pair-Rank). *(p.3-5)*
- **Comparator(s):** Vanilla verbalized confidence as baseline; also white-box token-probability methods (seq-prob, len-norm-prob, token-prob). *(p.16-17)*
- **Primary endpoint(s):** Expected Calibration Error (ECE) for calibration; AUROC for failure prediction. *(p.6)*
- **Secondary endpoint(s):** AUPRC-Positive (PR-P), AUPRC-Negative (PR-N). *(p.6)*
- **Follow-up:** N/A (static benchmark).

## Methodology
Three-component framework:

1. **Prompting strategy** elicits verbalized confidence in different ways.
2. **Sampling strategy** generates multiple responses per question (temperature 0.7, M = 5 typical, swept 1-13).
3. **Aggregation strategy** combines multiple responses into a single confidence score.

Every prompt is appended with the clarification: *"Note: The confidence indicates how likely you think your answer is true."* *(p.3-4, p.27)*

Sampling uses temperature = 0.7 per Wang et al. 2022. Candidate set size K default = 4 (balances efficiency and information gain). *(p.20, p.25)*

## Key Equations / Statistical Models

### Multi-Step aggregation (product of per-step confidences)
$$
C_{\text{multi-step}} = \prod_{i=1}^{n} C_i
$$
Where $n$ is the number of reasoning steps and $C_i$ is the verbalized confidence in step $i$. *(p.4)*

### Consistency aggregation
$$
C_{\text{consistency}} = \frac{1}{M} \sum_{i=1}^{M} \mathbb{I}\{\hat{Y}_i = \tilde{Y}\}
$$
Where $\tilde{Y}$ is the reference answer, $\hat{Y}_i$ is the $i$-th sampled answer, $M$ is the number of samples, $\mathbb{I}$ is the indicator. *(p.4, eq 1)*

### Avg-Conf aggregation
$$
C_{\text{conf}} = \frac{\sum_{i=1}^{M} \mathbb{I}\{\hat{Y}_i = \tilde{Y}\} \cdot C_i}{\sum_{i=1}^{M} C_i}
$$
Where $C_i$ is the verbalized confidence for sample $i$. Weights consistency by model-reported confidence. *(p.5, eq 2)*

### Pair-Rank MLE objective
$$
\min_{P} -\sum_{i=1}^{N} \sum_{S_u \in A}\sum_{S_v \in A} \mathbb{I}\{S_u \succ^{(i)} S_v\} \cdot \log \frac{P(S_u)}{P(S_u) + P(S_v)} \quad \text{s.t.} \quad \sum_{S_u \in A} P(S_u) = 1
$$
Where $A$ is the set of unique answers across all $N$ Top-K responses, $S_u \succ^{(i)} S_v$ means $S_u$ appears before $S_v$ in the $i$-th Top-K generation, and $P$ is a categorical distribution over answers. Solved by softmax reparameterization + gradient descent. *(p.5, eq 3-4; proof p.14-15)*

### Pair-Rank conditional probability (Proposition 3.1)
$$
P(S_u \succ S_v \mid P, E^{(i)}_{uv}) = \frac{P(S_u)}{P(S_u) + P(S_v)}
$$
Holds when Top-K answers are drawn from categorical $P$ without replacement. Proof uses Law of Total Probability over the earliest position $j$ where either $S_u$ or $S_v$ first appears. *(p.14-15)*

## Parameters

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Sampling temperature | T | - | 0.7 | - | 25 | Self-Random sampling; per Wang et al. 2022 |
| Number of sampled responses | M | - | 5 | 1-13 | 8,20 | Diminishing returns past ~5 |
| Candidate answer set size | K | - | 4 | 1-13 | 20 | Top-K sampling; balances efficiency vs info |
| ECE significance threshold | ECE | - | 0.25 | - | 7 | Values > 0.25 flagged as significant deviation (Srivastava et al. 2023) |
| AUROC significance threshold | AUROC | - | 0.6 | - | 7 | < 0.6 flagged as significant deviation |
| AUPRC significance threshold | AUPRC | - | 0.6 | - | 7 | < 0.6 flagged as significant deviation |
| Verbalized confidence range (observed) | - | % | 80-100 | 0-100 | 6 | Typically in multiples of 5 |

## Effect Sizes / Key Quantitative Results

All metrics reported as x10^2 (so "54.8" = 0.548). *(p.7)*

### Vanilla verbalized confidence headline (Table 2, p.7)

| Model | Avg ECE | Avg AUROC | Avg PR-N | Avg PR-P |
|-------|---------|-----------|----------|----------|
| GPT-3 | 52.0 | 51.3 | 54.7 | 46.9 |
| GPT-3.5 | 43.6 | 56.4 | 62.0 | 47.2 |
| GPT-4 | 18.0 | 62.7 | 34.2 | 78.4 |
| Vicuna | 37.7 | 55.1 | 48.1 | 60.2 |
| LLaMA2 | (varies) | (varies) | (varies) | (varies) |

GPT-4's AUROC averages only 62.7, meaning verbalized confidence is only marginally better than random guess (50) at distinguishing correct from incorrect. *(p.7)*

### Sampling strategy effect (GPT-3.5, M=5, CoT + Consistency) (Table 3, p.8)

| Method | GSM8K ECE | GSM8K AUROC | Avg ECE | Avg AUROC |
|--------|-----------|-------------|---------|-----------|
| Misleading (M=5) | 8.03 | 88.6 | 17.3 | 69.6 |
| Self-Random (M=5) | 6.28 | 92.7 | 18.7 | 73.0 |
| Prompt (M=5) | 35.2 | 74.4 | 24.3 | 69.2 |
| CoT (M=1) | 10.1 | 54.8 | 25.0 | 56.4 |
| Top-K (M=1) | 19.6 | 58.5 | 17.8 | 65.2 |

Headline: GSM8K AUROC rises from 54.8 (CoT M=1, near random) to 92.7 (Self-Random M=5 + Consistency). *(p.8)*

### Aggregation strategy effect (GPT-4, Top-K prompt, Self-Random sampling) (Table 4, p.9)

| Aggregator | Avg ECE (+/- var) | Avg AUROC (+/- var) | Notes |
|------------|-------------------|---------------------|-------|
| Consistency | 12.0 +/- 0.3 | 66.9 +/- 0.8 | Answers only |
| Avg-Conf | 14.8 +/- 0.7 | 66.9 +/- 1.7 | Confidence-weighted; best AUROC on 5/6 datasets |
| Pair-Rank | 6.90 +/- 0.2 | 67.6 +/- 0.4 | Best ECE on half of datasets; as low as 0.028 |

### White-box vs black-box AUROC gap (Tables 5-6, p.16-17)
- Best black-box verbalized AUROC ~ 0.522 average; best white-box (len-norm-prob, token-prob) ~ 0.605 average.
- Gap is narrow. Neither reaches satisfactory performance. *(p.9, p.16-17)*

### Full method comparison (Table 13, p.22)

| Method | Avg ECE | Avg AUROC | Avg PR-P | Avg PR-N |
|--------|---------|-----------|----------|----------|
| Top-K (M=1) | 24.6 | 65.9 | 58.1 | 62.5 |
| CoT (M=1) | 25.0 | 56.4 | 68.9 | 38.4 |
| Self-Random + Consistency (M=5) | 18.7 | 73.0 | 78.7 | 58.2 |
| Misleading + Consistency (M=5) | 17.3 | 69.6 | 76.5 | 54.1 |
| Self-Random + Avg-Conf (M=5) | 14.8 | 74.5 | 80.6 | 61.9 |
| Misleading + Avg-Conf (M=5) | 14.2 | 70.2 | 78.1 | 55.9 |

### Role-play persona effect (Table 7, p.18)
| Role | ACC | ECE | AUROC | PR-P | PR-N |
|------|-----|-----|-------|------|------|
| "Confident GPT" (chatgpt-0613) | 0.7103 | 0.2741 | 0.5679 | 0.7398 | 0.3635 |
| "Cautious GPT" (chatgpt-0613) | 0.6983 | 0.2812 | 0.5946 | 0.7415 | 0.4009 |

Minimal effect: persona framing does not meaningfully shift verbalized confidence. *(p.18)*

## Methods & Implementation Details

### Prompting strategies (Table 1, p.4; full prompts Tables 14-18, p.27-29)
- **Vanilla** *(p.4, 27)*: "Read the question, provide your answer and your confidence in this answer." Output format: `Answer and Confidence (0-100): [answer], [0-100]%`.
- **Chain-of-Thought (CoT)** *(p.4, 28)*: Zero-shot CoT (Kojima 2022). "Read the question, analyze step by step..." Output includes `Explanation: [step-by-step]` then answer + confidence.
- **Self-Probing** *(p.4, 28)*: Two chat sessions. Generate answer in session 1; in session 2 ask "How likely is the above answer to be correct?" Motivated by the observation that humans find errors easier to spot in others' answers.
- **Multi-Step** *(p.4, 29)*: Decompose into K steps, give per-step confidence, aggregate by product.
- **Top-K** *(p.4, 29)*: "Provide your K best guesses and the probability that each is correct (0% to 100%) for the following question." Outputs G1,P1,...,Gk,Pk format. From Tian et al. 2023.

### Sampling strategies (p.4, Table 11 p.21)
- **Self-Random**: Same prompt, different random seeds (temperature = 0.7).
- **Prompting**: Paraphrase the question M ways.
- **Misleading**: Inject misleading hints of three categories:
  - **Weak Claim**: "I think the answer should be...", "I vaguely remember the answer is...", "I read online the answer is..."
  - **Strong Claim**: "I am pretty sure...", "I am 80% sure...", "Undoubtedly the answer is...", "With my 100% confidence..."
  - **External Source**: "Wikipedia claims...", "Latest research shows...", "My teacher tells me...", "The textbook shows...", "An expert says..."
- Weak Claim performs best (Table 12, p.22): ECE 19.7/18.2, AUROC 62.0/65.4 on StrategyQA GPT-3.5.

### Aggregation strategies
- **Consistency**: Indicator agreement, eq 1. *(p.4)*
- **Avg-Conf**: Confidence-weighted indicator agreement, eq 2. *(p.5)*
- **Pair-Rank**: MLE on pairwise rank events extracted from Top-K lists, eq 3-4. Uses softmax reparameterization to remove simplex constraint, then gradient descent. Closed-form conditional from Proposition 3.1. *(p.5, proof p.14-15)*

### Evaluation metrics (p.6, p.25)
- **ECE**: Expected Calibration Error. Bins confidence and measures |avg confidence - avg accuracy| per bin.
- **AUROC**: Area under ROC curve, treating "correct" as positive class using confidence as score.
- **AUPRC-Positive**: PR curve with correct answers as positive.
- **AUPRC-Negative**: PR curve with incorrect answers as positive.

### Thresholds for "significant deviation" (Srivastava et al. 2023) *(p.7)*
- ECE > 0.25: calibration is poor.
- AUROC / AUPRC-P / AUPRC-N < 0.60: discrimination is poor.

### Datasets (p.5, p.24)
- **Commonsense**: SportUND (BigBench), StrategyQA (BigBench). StrategyQA chosen as primary.
- **Arithmetic**: GSM8K, SVAMP. GSM8K chosen as primary.
- **Symbolic**: Date Understanding (DateUnd), Object Counting (ObjectCou) from BigBench. DateUnd chosen (harder).
- **Professional Knowledge**: Professional Law (Prf-Law) from MMLU.
- **Ethical Knowledge**: Business Ethics (Biz-Ethics) from MMLU.

### Models (p.6, p.25)
- Vicuna (13B, fine-tuned from LLaMA)
- GPT-3 (175B)
- GPT-3.5-turbo
- GPT-4
- LLaMA2 (70B Chat)

### Pair-Rank implementation details (p.5, p.15)
- Change of variables via softmax to escape simplex constraint.
- Train P with gradient descent over the MLE loss.

## Figures of Interest
- **Fig 1 (p.3):** Overall framework diagram: prompt strategy x sampling strategy (M responses) x aggregator -> (answer, confidence). Example shows Vanilla + Self-Random M=3 + Avg-Conf with answers {100, 20, 25} and confidences {100%, 90%, 80%} aggregating to answer=100, confidence=37%.
- **Fig 2 (p.6):** Empirical distribution and reliability diagram of vanilla verbalized confidence on GSM8K for GPT-3, GPT-3.5, GPT-4, Vicuna. Shows mass concentrated 80-100%, multiples of 5, accuracy much lower than confidence per bin.
- **Fig 3 (p.8):** ECE and AUROC across 5 prompting strategies x 5 datasets for GPT-3.5 and GPT-4. Shows mean-ECE reduction with prompting; AUROC stays near 0.5-0.6.
- **Fig 4 (p.18):** Distribution of verbalized confidence under "confident GPT" vs "cautious GPT" personas. Minimal difference.
- **Fig 5 (p.19):** Empirical distribution of vanilla verbalized confidence across 4 models x 5 datasets. Confirms 80-100% clustering universally.
- **Fig 6 (p.19):** ECE/AUROC diff of CoT, Multi-Step, Top-K vs Vanilla on 5 datasets for GPT-3.5. Top-K best among prompts.
- **Fig 7 (p.21):** Impact of number of misleading hints (K=1..13) on ECE and AUROC. Diminishing returns.
- **Fig 8 (p.25):** Example full prompt and model output ("A robe takes 2 bolts of blue fiber and half that much white fiber... -> 3, 85%").

## Results Summary

1. **LLMs are overconfident when verbalizing confidence.** Verbalized confidence clusters in 80-100% in multiples of 5, closely mirroring human patterns (Zhou et al. 2023). Accuracy within each high-confidence bin is much lower than the confidence value, producing large ECE. *(p.6)*
2. **Scale improves calibration but not enough.** GPT-3 -> GPT-4 gives ~22.2% AUROC improvement, but GPT-4 still averages AUROC 62.7. *(p.7)*
3. **CoT reduces ECE by raising accuracy, not by improving discrimination.** Example: CoT GPT-4 on GSM8K achieves near-optimal ECE=0.064 by assigning 100% confidence to all samples (93.6% accuracy) - but AUROC is near random because all samples receive identical confidence. *(p.7-8)*
4. **Sampling + Consistency dramatically improves failure prediction on arithmetic.** GSM8K AUROC: 54.8 (CoT M=1) -> 92.7 (Self-Random M=5 + Consistency). *(p.8)*
5. **Pair-Rank is best for calibration (lowest ECE, down to 0.028); Avg-Conf is best for failure prediction (highest AUROC).** Introducing verbalized confidence into aggregation beats consistency-only aggregation, especially when M is budget-limited. *(p.8-9)*
6. **White-box vs black-box gap is narrow:** ~0.522 vs ~0.605 average AUROC. Uncertainty estimation in LLMs is unresolved for both paradigms. *(p.9, p.16-17)*
7. **Persona framing has minimal effect.** "Confident" vs "Cautious" persona does not shift ECE/AUROC meaningfully. *(p.18)*
8. **Weak-Claim misleading hints work better than Strong-Claim or External-Source.** *(p.19-22)*

## Limitations
- **Scope of datasets**: Only fixed-form and free-form QA with unique ground truth. No summarization, no open-ended generation. *(p.9)*
- **Black-box setting is suboptimal**: White-box access to model logits (where available, e.g., GPT-3) may be more promising. *(p.9)*
- **Verbalized confidence is fundamentally constrained by the training corpus**: LLMs learned human expressions of uncertainty which are themselves biased/inaccurate (Garthwaite et al. 2005b). *(p.23)*
- **Professional-knowledge tasks remain hard**: All methods struggle on Prf-Law (MMLU). *(p.9)*
- **Sampling cost is linear in M**: Trade-off between compute and accuracy of uncertainty estimate. *(p.8)*

## Arguments Against Prior Work
- **Token-likelihood methods (Malinin & Gales 2020; Kadavath et al. 2022) fail for closed-source LLMs** because commercial APIs expose only text, not logits. *(p.1-2)*
- **Token-likelihood captures the wrong thing**: It measures next-token uncertainty, not semantic-level uncertainty. Example: "Chocolate milk comes from brown cows" has high per-token probability but is false. *(p.2, citing Kuhn et al. 2023)*
- **Fine-tuning-based methods (Lin et al. 2022) demand compute that researchers with low resources cannot afford**. Their evaluation is also tailored to pretrained LMs and leaves zero-shot verbalized confidence unexplored. *(p.2, p.23)*
- **Mielke et al. 2022 external calibrator depends on internal model representations** - not accessible for closed APIs. *(p.2, p.23)*
- **Zhou et al. 2023** examines the impact of confidence in prompts but does not provide confidence scores to users. *(p.2, p.23)*
- **Tian et al. 2023** (closest concurrent work) focuses narrowly on prompting strategies; this paper argues the space is broader (prompting x sampling x aggregation) and evaluates RLHF-LMs *and* non-RLHF models. *(p.2, p.23)*
- **Criticism of "just use prompting strategies"**: ECE reduction from CoT/Multi-Step/Top-K comes mainly from accuracy gains, not from better discrimination. AUROC barely moves. *(p.7-8, p.24)*
- **Criticism of consistency-only aggregation**: Coarse-grained output (only 6 distinct values at M=5: {0, 0.2, 0.4, 0.6, 0.8, 1.0}) produces poor calibration. Adding verbalized confidence gives finer granularity. *(p.23)*

## Design Rationale
- **Why Top-K prompting**: Requesting multiple guesses nudges the model to acknowledge alternatives, acting as a normalization on the confidence distribution. Top-K alone doesn't improve accuracy like CoT does, but ensemble methods compensate. *(p.4, p.22)*
- **Why Self-Probing**: Humans find errors easier to spot in others' answers than their own; running evaluation in a separate chat session approximates this. *(p.4)*
- **Why Multi-Step**: Per-step confidence gives finer-grained uncertainty; product aggregation surfaces compounded doubt. *(p.4)*
- **Why Avg-Conf over Consistency**: Uses *both* answer agreement *and* verbalized confidence - finer granularity enables better calibration when M is small. *(p.9, p.23)*
- **Why Pair-Rank for ECE**: MLE over pairwise ranking directly learns the categorical distribution P(answer), which aligns with the calibration objective. *(p.9)*
- **Why Avg-Conf for AUROC**: Accurate samples tend to produce consistent answers while incorrect samples yield varied ones; weighting by verbalized confidence amplifies this signal, which matches the failure-prediction objective. *(p.9)*
- **Why K=4 candidates**: Marginal gain past ~4 on datasets like Biz-Ethics (which only has 4 misleading-info variants). *(p.20)*
- **Why Self-Random over other sampling**: Performance differences between sampling strategies are minimal; Self-Random is simplest and most common. *(p.22)*

## Recommendation for Practitioners *(p.9, p.22)*
**Top-K prompt + Self-Random sampling + Avg-Conf or Pair-Rank aggregation.**
- Use **Pair-Rank** if the downstream task needs accurate confidence *values* (e.g., expected-risk calculation).
- Use **Avg-Conf** if the downstream task is failure prediction (e.g., factual-error detection, selective abstention).

## Considerations When Using Black-Box Confidence Elicitation *(p.23)*
1. **Never trust a single metric.** Low ECE does not imply the model can distinguish correct from incorrect. Always report both ECE and AUROC, plus confidence distribution plots.
2. **LLMs are not explicitly modeled to express uncertainty.** Their uncertainty vocabulary is inherited from human training data, which itself exaggerates confidence (Garthwaite et al. 2005a).

## Testable Properties
- Verbalized confidence from vanilla prompting clusters in [80%, 100%] in 5% increments for all tested LLMs. *(p.6, p.19)*
- ECE > 0.25 for vanilla verbalized confidence on GPT-3/GPT-3.5/Vicuna across most datasets. *(p.7)*
- AUROC ~ 0.5 for CoT (M=1) verbalized confidence on GSM8K; rises to ~0.92 with Self-Random M=5 + Consistency. *(p.8)*
- Pair-Rank aggregation achieves ECE as low as 0.028 on Sport, Strategy, and Ethics datasets (GPT-4 Top-K Self-Random). *(p.9)*
- Avg-Conf AUROC > Consistency AUROC in 5/6 tested datasets for failure prediction. *(p.9)*
- White-box vs black-box AUROC gap remains < 0.10 on average. *(p.9, p.16-17)*
- Persona prompts ("confident" vs "cautious") shift AUROC by < 0.03. *(p.18)*
- Weak Claim > Strong Claim > External Source for misleading hint category in failure prediction. *(p.22)*
- ECE/AUROC improvements from larger M (number of sampled responses) saturate by M ~ 5-7. *(p.8, p.20)*
- Under Top-K without-replacement sampling, P(S_u before S_v | P) = P(S_u) / (P(S_u) + P(S_v)). *(p.14-15)*

## Relevance to Project
This paper is being retrieved to back the Wabiski LLM-confidence critique in the inclusive-cartography systematic-review protocol (§3.3 seed selection & scoping). Key findings directly load the critique:

1. **Verbalized confidence is not calibrated out-of-the-box.** Any protocol that uses raw LLM-reported confidence thresholds is on shaky ground: confidence clusters 80-100% regardless of ground truth.
2. **ECE alone is not enough.** A pipeline that gates on ECE while ignoring AUROC can pass even when the LLM assigns 100% confidence to every answer. Any confidence-threshold protocol must track both calibration and discrimination metrics.
3. **Distribution shift / professional knowledge**: Even the best methods (Pair-Rank ECE ~0.069 avg) fail on Prf-Law. If the cartography protocol uses LLMs in specialist domains (e.g., tactile-map standards), confidence scores are likely unreliable.
4. **The persona trick doesn't help.** Prompting the LLM to "be cautious" does not meaningfully improve calibration. Any protocol relying on instructed calibration (rather than measured calibration) is unsupported by evidence.
5. **Recommended stable config** (Top-K + Self-Random M=5 + Avg-Conf / Pair-Rank) is a concrete alternative that the critique can propose instead of naive single-query verbalized confidence.
6. **The white-box / black-box gap is narrow** - so there is no easy fix by switching to a logit-exposing model.

## Open Questions
- [ ] Does Xiong's framework generalize to open-ended generation (summarization, long-form QA)?
- [ ] How do these findings change with newer models (GPT-4o, Claude 3.5 Sonnet, Llama 3)?
- [ ] Are there domain-specific calibration strategies for professional knowledge where all methods struggle?
- [ ] Can semantic uncertainty (Kuhn et al. 2023) be combined with Pair-Rank to improve the black-box ceiling?

## Collection Cross-References

### Already in Collection
- [[Tian_2023_JustAskCalibrationStrategies]] — Closest concurrent work. Tian et al. focus narrowly on prompting strategies (Top-K, verbalized numeric, verbalized linguistic, two-step) for RLHF-finetuned models on TriviaQA/SciQ/TruthfulQA. Xiong et al. argue the design space is broader (prompting × sampling × aggregation), evaluate on both RLHF and non-RLHF models, and include a wider benchmark (8 datasets, 5 models, calibration + failure-prediction). Where Tian et al. report best-case ECE ≈ 0.03-0.04 on in-distribution factoid QA, Xiong et al. show this is achieved partly by assigning 100% confidence to every answer (ECE 0.064 via uniform-100 on GSM8K) and that AUROC is often near random — Xiong's finding directly nuances Tian's positive result. *(Xiong p.2, p.7-8, p.23)*
- [[Lin_2022_TeachingModelsExpressUncertainty]] — Supervised-finetuning baseline for verbalized confidence. Xiong et al. point out that fine-tuning-based methods (Lin 2022) demand compute that low-resource researchers cannot afford (p.2). Their black-box framework is designed to work without Lin's finetuning step.
- [[Kadavath_2022_LanguageModelsMostlyKnow]] — Canonical white-box self-evaluation reference. Xiong et al. argue that Kadavath-style token-likelihood methods fail for closed-source LLMs (no logit access) and also capture next-token uncertainty rather than semantic-level uncertainty (Xiong p.1-2, citing Kuhn et al. 2023).
- [[Wabiski_2026_CognitiveReviewProtocol]] — Direct critique target. See `papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md` §2.2(h) for the specific use of Xiong et al.'s 80-100% multiples-of-5 clustering finding and the "ECE 0.064 with AUROC near random by assigning 100% to everything" counter-example against the protocol's `>0.90 auto-include` rule. This is the strongest direct empirical refutation of Wabiski's threshold rule in the current literature.

### Cited By (in Collection)
- [[Tian_2023_JustAskCalibrationStrategies]] — Brock_2015 reconciliation pass flagged Xiong 2024 as a conceptual follow-up to Tian; Tian's own "New Leads" section explicitly named Xiong 2024 as the fourth paper in the "can we trust LLM-reported confidence" cluster (now resolved).

### Conceptual Links (not citation-based)
- [[Brock_2015_InteractiveMapsUsability]] — Strong. Brock provides a human analogue of Xiong's LLM clustering finding: human self-reported confidence ratings after tactile map exploration also fail to track long-term spatial accuracy (landmarks decay ~45% while confidence holds). Brock's 2015 empirical result is the non-LLM replication of the core Xiong observation that confidence is a poor proxy for correctness, and directly supports the Wabiski_2026 threshold-rule critique from the human-rater side.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Moderate. Wabinski 2022 is the tactile-map design guideline underlying the 2026 protocol; Xiong's 80-100% multiples-of-5 clustering finding argues that any LLM-based extraction of Wabinski's parameters at the 2026 protocol's thresholds would be dominated by verbalization noise.

## Related Work Worth Reading
- Lin, Hilton, Evans 2022 - Teaching models to express uncertainty in words (fine-tuning route, already in collection) → NOW IN COLLECTION: [[Lin_2022_TeachingModelsExpressUncertainty]]
- Kadavath et al. 2022 - Language Models (Mostly) Know What They Know (white-box self-eval, already in collection) → NOW IN COLLECTION: [[Kadavath_2022_LanguageModelsMostlyKnow]]
- Tian et al. 2023 - Just Ask for Calibration (closest prior work, already in collection) → NOW IN COLLECTION: [[Tian_2023_JustAskCalibrationStrategies]]
- Kuhn, Gal, Farquhar 2023 - Semantic Uncertainty (semantic-level calibration)
- Zhou, Jurafsky, Hashimoto 2023 - Navigating the Grey Area: Expressions of Overconfidence and Uncertainty in Language Models
- Guo, Pleiss, Sun, Weinberger 2017 - On Calibration of Modern Neural Networks (foundational calibration)
- Mielke, Szlam, Dinan, Boureau 2022 - Reducing conversational agents' overconfidence through linguistic calibration
- Xiong et al. 2023 - Proximity-Informed Calibration for Deep Neural Networks (same first author, white-box)
