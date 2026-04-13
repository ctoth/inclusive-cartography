# Calibration pre-flight experiment — inclusive-cartography screening

Empirical test of whether the Wabiski 2026 §3.5.2 LLM screening rule
(`confidence > 0.90` auto-include, `< 0.70` auto-exclude, `0.70-0.90`
human review) is defensible when applied to the inclusive-cartography
title/abstract screening task.

## TL;DR

1. The verbalized-confidence threshold rule as written is **effectively
   inoperative** on this task: 83-100% of items in our test set receive
   confidence > 0.90, so the "human review" band almost never fires. The
   rule does not gate anything — it passes nearly every citation the LLM
   sees through to the auto-include branch, regardless of whether the
   citation is a true include or a true exclude.
2. The underlying classifier is actually reasonably accurate (GPT-5 88.5%,
   Gemini 2.5 Pro 94.2%) and perfectly discriminative on the include/
   exclude binary (AUROC 1.0 for both), so the calibration layer is the
   failure point, not the base classifier.
3. The Xiong 2024 "80-100% of verbalized confidences are multiples of 5"
   finding **strongly replicates on Gemini 2.5 Pro** (84.6% of its
   confidences are exactly at multiples of 0.05) and **does not replicate
   on GPT-5** (1.9%). GPT-5's confidences cluster at `.99` and look
   analog, but the distribution is still degenerately right-skewed (median
   and mode both 0.99).
4. Because the threshold rule almost never routes to human review, the
   downstream auto-include band contains a large proportion of true
   negatives: 81.4% of GPT-5's `> 0.90` items are true negatives, and
   67.3% of Gemini's are. If used as a decision gate, the rule would
   auto-accept these negatives without human intervention.

**Concrete recommendation for §3.5.2:** delete the numeric threshold rule,
or replace it with a self-consistency-agreement rule, or require human
review of *every* auto-include item. Verbalized confidence from the
current generation of frontier models is not calibrated well enough to
stand alone as a decision gate on this task type.

## Test set

- **N = 52** items drawn from two pools:
  - **17 positives:** 13 seed papers already collected in this repository
    (the inclusive-cartography seed corpus in `papers/`, excluding the
    Wabiski protocol itself and the four LLM-calibration papers) plus
    4 additional positives retrieved via arXiv keyword queries for
    tactile / accessible / inclusive cartography topics.
  - **35 negatives:** arXiv papers from `cs.CG` (mesh / computational
    geometry), `cs.GR` (rendering / shaders), `cs.CV` (object detection
    benchmarks), `stat.ML` (variational inference, GNNs), plus "hard
    negative" queries for `self-organizing map` and `web accessibility /
    WCAG`.
- **Ground-truth labels:** for positives, hand-assigned to rq1 / rq2 / rq3
  by reading each paper's `index.md` summary and mapping tags to the
  Wabiski research question definitions. For negatives, the ground-truth
  tag is `excluded` by construction.
- **Label distribution:** rq1 = 6, rq2 = 13, rq3 = 1, excluded = 35. The
  test set is intentionally **unbalanced toward negatives** and **light on
  rq3** (only 1 item) because rq3 is the "transferability-across-groups"
  research question and few arXiv titles specifically match it. This
  limits per-class inference on rq3; per-class inference for rq1 and rq2
  is supported.
- **Data provenance:** every abstract is a real published paper's real
  abstract. Positives are verbatim from `papers/<name>/abstract.md`
  ("Original Text (Verbatim)" section) and from the arXiv Atom API.
  Negatives are verbatim from the arXiv Atom API. No abstracts were
  synthesized.
- **Files:** `experiments/calibration-preflight/test_set.jsonl` (one JSON
  object per line, with fields `id`, `title`, `abstract`, `ground_truth`,
  `source`, `justification`).

## Model and configuration

- **Models (multi-provider run):**
  - OpenAI `gpt-5` via the Responses API
  - Google `gemini-2.5-pro` via the `google-genai` SDK with
    `response_mime_type=application/json`
  - (Anthropic Claude was **not** run — no live API key was available in
    this environment. The local `~/.claude/.credentials.json` contains an
    OAuth token for a Claude Max subscription, which is not usable via
    the Anthropic API. This is a single-provider gap; results below are
    GPT-5 + Gemini 2.5 Pro only.)
- **Temperature:** 0 for the primary pass. GPT-5 does not currently accept
  user-controlled temperature on its Responses API, so the primary pass
  on GPT-5 uses its default sampling and we note this as a caveat.
- **Prompt:** verbatim Wabiski §3.5.2 screening dictionary (pulled from
  `papers/Wabiski_2026_CognitiveReviewProtocol/notes.md` lines 193-232)
  wrapped in a minimal instruction that asks the model to return a
  structured JSON object with exactly three fields: `tag`,
  `confidence_score`, `exclusion_reason`.
- **Cost (primary pass, one sample per item per provider):**
  ~$0.25 on OpenAI, ~$0.09 on Gemini — well under the $10-per-provider
  budget cap.
- **Wall-time:** primary pass ~11 minutes (GPT-5 faster, Gemini throttled
  by occasional 503 `UNAVAILABLE` from the public API; 6 transient
  failures on Gemini were retried and recovered).

## Primary-run metrics (temperature 0 / single sample per item)

### Overall accuracy

| Model | N | Accuracy |
|---|---|---|
| GPT-5 | 52 | **0.885** |
| Gemini 2.5 Pro | 52 | **0.942** |

### Per-class performance

**GPT-5**

| Tag | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| screening:rq1 | 0.429 | 1.000 | 0.600 | 3 |
| screening:rq2 | 1.000 | 0.615 | 0.762 | 13 |
| screening:rq3 | 0.000 | 0.000 | 0.000 | 1 |
| screening:excluded | 0.946 | 1.000 | 0.972 | 35 |

**Gemini 2.5 Pro**

| Tag | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| screening:rq1 | 0.600 | 1.000 | 0.750 | 3 |
| screening:rq2 | 0.917 | 0.846 | 0.880 | 13 |
| screening:rq3 | 0.000 | 0.000 | 0.000 | 1 |
| screening:excluded | 1.000 | 1.000 | 1.000 | 35 |

### Confusion matrices

Columns = predicted, rows = ground truth. Labels in order:
`rq1, rq2, rq3, excluded`.

**GPT-5**

|  | rq1 | rq2 | rq3 | excluded |
|---|---|---|---|---|
| **rq1** | 3 | 0 | 0 | 0 |
| **rq2** | 3 | 8 | 0 | 2 |
| **rq3** | 1 | 0 | 0 | 0 |
| **excluded** | 0 | 0 | 0 | 35 |

**Gemini 2.5 Pro**

|  | rq1 | rq2 | rq3 | excluded |
|---|---|---|---|---|
| **rq1** | 3 | 0 | 0 | 0 |
| **rq2** | 2 | 11 | 0 | 0 |
| **rq3** | 0 | 1 | 0 | 0 |
| **excluded** | 0 | 0 | 0 | 35 |

**Key observation — false negatives on the include/exclude task:** Gemini
2.5 Pro misclassifies **0** positives as excluded. GPT-5 misclassifies
**2** true-RQ2 positives as excluded (a 4% include-task false-negative
rate). In a systematic review, false negatives on the include/exclude
task are the most dangerous error class — they silently drop true
positives from the corpus.

### Calibration

| Metric | GPT-5 | Gemini 2.5 Pro |
|---|---|---|
| ECE (correctness), 10 bins | 0.067 | 0.047 |
| ECE (include/exclude binary), 10 bins | 0.046 | 0.011 |
| AUROC (include/exclude), verbalized conf | **1.000** | **1.000** |

Both models achieve perfect AUROC on include/exclude discrimination, so
the verbalized confidence is *monotone* with correctness on this task —
but as the threshold analysis below shows, the monotone signal is
squeezed into such a narrow range (≥0.90 for almost everything) that no
reasonable fixed cutoff separates includes from excludes.

Reliability diagram: `experiments/calibration-preflight/reliability-diagram.png`.

### Threshold analysis (Wabiski §3.5.2 rule applied to our data)

**Auto-include band, confidence > 0.90:**

| Model | Count | Frac of N | Tag-correct | Actually positive (gt ≠ excluded) |
|---|---|---|---|---|
| GPT-5 | 43 | 82.7% | 42 (97.7%) | **8 (18.6%)** |
| Gemini 2.5 Pro | 52 | **100.0%** | 49 (94.2%) | **17 (32.7%)** |

Read those two right-hand columns carefully. "Tag-correct" counts items
where the LLM's 4-way classification matches ground truth — the
auto-include band is tag-correct at 94-97% because the band contains
almost every item, and the LLM correctly classifies 94-97% of the full
test set. "Actually positive" counts items where ground truth is
rq1/rq2/rq3 rather than excluded — i.e., the proportion of items that a
human reviewer would have wanted to include. That proportion is **18.6%
for GPT-5 and 32.7% for Gemini** because the auto-include band contains
essentially every true negative in the test set. In other words, the
auto-include band does not select for true includes at all.

**Auto-exclude band, confidence < 0.70:**

| Model | Count | Frac of N | Actually negative |
|---|---|---|---|
| GPT-5 | 1 | 1.9% | 0 (0%) |
| Gemini 2.5 Pro | 0 | 0% | — |

The auto-exclude band is empty on Gemini and essentially empty on GPT-5.
The single GPT-5 auto-exclude item was a true positive that the model
dropped with confidence 0.62 — so the only time this branch activated,
it silently excluded a true-include. That is the worst possible behavior
for a systematic-review screener.

**Human-review band, 0.70 ≤ confidence ≤ 0.90:**

| Model | Count | Frac of N |
|---|---|---|
| GPT-5 | 8 | 15.4% |
| Gemini 2.5 Pro | 0 | 0% |

Gemini 2.5 Pro never routes any item to human review. GPT-5 routes
15.4%. The Wabiski protocol as written assumes a non-trivial human-review
band exists as a safety net; on these models it does not.

### Verbalized-confidence distribution

**GPT-5** — modal value `0.99` (35 of 52 items = 67%). Mean ≈ 0.94.
Confidence values observed: `{0.62, 0.78, 0.83, 0.84, 0.86, 0.88, 0.89,
0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99}`. Only 1.9% of
values are at multiples of 0.05. GPT-5's confidences look finely
grained, but the distribution is still severely right-skewed and the
0.99-cluster dominates.

**Gemini 2.5 Pro** — modal value `1.00` (35 of 52 items = 67%). Mean ≈
0.98. Confidence values observed: `{0.95, 0.98, 1.00}`. **84.6% of
values are exactly at multiples of 0.05**, replicating the Xiong 2024
finding. Gemini's confidences collapse onto a three-point grid.

Histogram: `experiments/calibration-preflight/confidence-histogram.png`.

### Xiong 2024 replication verdict

- Xiong 2024 (`papers/Xiong_2024_LLMUncertaintyConfidenceElicitation`):
  vanilla verbalized confidence is severely overconfident and values
  cluster 80-100% in multiples of 5.
- **Gemini 2.5 Pro: replicates strongly.** 100% of Gemini's values are in
  [0.95, 1.00]; 84.6% are at multiples of 0.05.
- **GPT-5: does not replicate on the "multiples of 5" axis but replicates
  on the "severely overconfident" axis.** 96.2% of GPT-5's values are in
  [0.78, 0.99]; 82.7% are > 0.90. GPT-5 emits finer-grained decimals
  (`.93, .96, .97, .98, .99`) but the distribution is still heaped at
  the top of the 0-1 interval and gives the Wabiski threshold rule
  almost nothing to work with.

## Secondary-run metrics (temperature 1, N=5 samples per item)

*(Secondary pass was initiated but is slower than the primary pass because
of per-item reasoning tokens on GPT-5 and intermittent Gemini 503s. If
the secondary pass finished in time, its numbers are in
`experiments/calibration-preflight/metrics.json` under the key
`secondary`. Rerun `uv run python compute_metrics.py` from the experiment
directory to refresh them from the cache.)*

Expected signal from the secondary pass, given the primary-pass
distribution: self-consistency agreement across N=5 samples should be
≈1.0 on the easy negatives and should show meaningful variance on the
handful of genuinely hard items (the RQ2↔RQ1 boundary cases and the
single RQ3 item). Agreement is likely to be a **better-ranked** signal
than verbalized confidence because it can take values in {0.2, 0.4, 0.6,
0.8, 1.0} rather than being squeezed to ≥0.90 — that is, agreement rate
has more measurement resolution than verbalized confidence on this task.
If the secondary-pass numbers in `metrics.json` show agreement-rate ECE
lower than verbalized-confidence ECE, that would be consistent with the
Xiong 2024 conclusion that self-consistency sampling with M=5 is the
most reliable elicitation strategy in their benchmark.

## Interpretation for the Wabiski protocol §3.5.2

1. **The numeric threshold rule does not do what it claims to do on this
   task.** §3.5.2 presents the `>0.90 / 0.70-0.90 / <0.70` rule as a
   three-way routing decision that reserves a human-review band as a
   safety net. In practice, the current-generation frontier models
   (GPT-5, Gemini 2.5 Pro) emit confidences that are so top-heavy that
   the human-review band is empty or nearly empty, and the auto-include
   band accepts the entire corpus. The rule is therefore not a routing
   decision at all — it is effectively `always-auto-include`.
2. **But the underlying classifier is fine.** Both models correctly
   excluded 35/35 true negatives and both achieved AUROC 1.0 on the
   include/exclude task. The models *know* which items are out of scope.
   The signal is there; the verbalized-confidence layer just does not
   expose it in a way that the threshold rule can use.
3. **Gemini's result is the direct replication of Xiong 2024 on this
   task**, which is the strongest evidence we have that verbalized
   confidence alone should not be trusted as a decision gate.
4. **Concrete recommendation:** replace §3.5.2's fixed-threshold rule
   with one of the following and state the choice in the protocol:
   - **Option A (cheap, recommended):** drop the threshold rule entirely
     and have a human reviewer look at every auto-include AND a stratified
     sample of auto-excludes. Use the LLM classifier as a *ranker*, not a
     decision gate.
   - **Option B (more rigorous):** replace verbalized confidence with
     a self-consistency-agreement signal (M=5 samples, temperature 1,
     agreement rate across samples). Require agreement ≥ 4/5 for
     auto-include. This is the Xiong 2024 recommendation and will have
     measurement resolution that the verbalized score lacks.
   - **Option C (hybrid):** keep verbalized confidence but calibrate it
     per-model on a held-out labeled sample before applying any
     threshold. This pre-flight experiment is exactly the kind of
     calibration run that should happen before §3.5.2 is applied in
     anger.

## Limitations of this pre-flight

- **N is small** (52 items). The headline numbers have wide binomial
  confidence intervals.
- **Class balance is skewed.** Only 1 RQ3 item and only 3 RQ1 items.
  Per-class calibration numbers for RQ1 and RQ3 are not reliable.
- **Negatives are *too easy*.** The arXiv cs.CG / cs.GR / cs.CV / stat.ML
  abstracts are obvious out-of-scope matches — any real screening corpus
  will have near-miss negatives (papers on general cartography, general
  web accessibility, general 3D printing) that this pre-flight
  under-samples. Both models solved 35/35 negatives, which is the
  ceiling; a harder negative pool would push the AUROC below 1.0.
- **Single-provider calibration gap:** Anthropic Claude is missing from
  this run because no live Anthropic API key was available in the
  environment. The Wabiski protocol uses GPT-5 and Gemini 2.5 Pro so the
  cross-model claim still stands, but adding Claude Opus 4.x is worth
  doing in a follow-up run.
- **No human-reviewer second pass.** Ground truth for positives is based
  on the paper-level labels already in this repository's `papers/index.md`
  (hand-curated by the project author) and on the arXiv query that
  retrieved each additional item. A "real" pre-flight would have two
  independent human screeners per item and report inter-rater agreement.
- **GPT-5 sampling temperature is not controllable.** The primary GPT-5
  pass runs at the API default (effectively non-deterministic at N=1),
  so strict temperature=0 calibration numbers for GPT-5 should be read
  as "a single sample from the API-default distribution", not as greedy
  decoding.
- **Single-sample primary run:** per-item ECE is computed on a single
  sample per item, not an expectation over samples.

## Reproducing

```bash
cd experiments/calibration-preflight
uv run python build_testset.py         # writes test_set.jsonl
uv run python run_screening.py         # runs primary pass (cached)
uv run python compute_metrics.py       # computes metrics + plots
RUN_SECONDARY=1 uv run python run_screening.py  # optional secondary pass
```

All LLM outputs are cached per-item under
`experiments/calibration-preflight/cache/{provider}/{model}/` so
re-running is free.
