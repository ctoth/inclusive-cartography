# Task: Run the calibration pre-flight experiment recommended in `author-feedback.md` §2.4

## Context

The project `inclusive-cartography` is critiquing a systematic-review protocol (`papers/Wabiski_2026_CognitiveReviewProtocol/`) that uses LLM-reported confidence scores as decision gates (`> 0.90` auto-include, `< 0.70` auto-exclude). The author-feedback file §2.4 recommends a "calibration pre-flight" — hold out a sample of citations, have humans screen them, run the LLM screening prompt against them, and compute ECE / AUROC / a reliability diagram to determine whether the thresholds are empirically defensible for inclusive-cartography screening.

Q has explicitly asked for this to be run end-to-end rather than left as a recommendation. The deliverable is a set of empirical numbers for Q's meeting tomorrow morning.

## Objective

Run the minimal-but-complete version of the calibration pre-flight experiment against the inclusive-cartography screening task and produce:

1. A calibration report with concrete ECE, AUROC, confusion-matrix, and reliability-diagram numbers for verbalized LLM confidence on the screening task.
2. An assessment of whether Wabiski's thresholds (0.70 / 0.85 / 0.90) are empirically supported **on this specific task type** (not on in-distribution factoid QA, which is the only regime Tian 2023 reports positive numbers for).
3. A follow-up patch for `papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md` §2.5 ("Coverage gap — now closed") with the generated numbers inserted as the final citation.

## Step 0 — Scout the repo

Before writing any code, check what's already here. `ls` the project root, check for `pyproject.toml` / `requirements.txt` / `uv.lock` / existing Python harness / existing LLM API setup. If the project already has a calibration harness or a similar experiment scaffolding, reuse it. If not, build new under `experiments/calibration-preflight/`.

Also check for an `ANTHROPIC_API_KEY` in the environment. If not present, check `.env` / `~/.claude/`. If the API key is genuinely not available, STOP and report this as a concrete blocker — do not fake the numbers.

## Step 1 — Assemble the test set

You need **both positive and negative citations** for the screening task. Ground-truth labels are:

- **Positive labels:** `screening:rq1`, `screening:rq2`, or `screening:rq3` (all three RQs in the Wabiski protocol).
- **Negative label:** `screening:excluded`.

### Positives (target ~40 items)

- Use the abstracts already in this repo from the retrieval swarm. Read `papers/*/abstract.md` for every inclusive-cartography seed paper (NOT the Wabiski protocol itself, and NOT the 4 LLM-confidence papers). That gives you ~12 positives already labeled.
- Per-paper, also extract 2-3 "Key Citations for Follow-up" entries from `papers/*/citations.md` — these are references that the seed papers cite. Use Semantic Scholar / CrossRef / arXiv APIs to fetch just the abstract for each. Label each based on which seed paper referenced it and which RQ that seed paper addresses. If an abstract is unavailable, skip it.
- Target: ~30-40 positives total across RQ1/RQ2/RQ3.

### Negatives (target ~40 items)

- Negatives are abstracts that SHOULD be excluded by the Wabiski protocol: wrong topic, wrong date range, wrong language, wrong format, or simply not about inclusive cartography.
- Sources:
  - Random arXiv pulls from `cs.CG` (computational geometry), `cs.GR` (graphics), `cs.CV` (computer vision), `stat.ML` — pick abstracts that are clearly not about cartography accessibility.
  - CrossRef queries for "cartography" without accessibility terms — general cartography papers that are out of scope.
  - CrossRef queries for "accessibility" without map/spatial terms — general web/software accessibility papers.
  - Optional: 5-10 "hard negatives" — papers that mention maps AND accessibility but are about something else (e.g., "map" in a data-structure sense, or "accessibility" in a web-dev sense).
- Target: ~30-40 negatives.

**Do not exceed 100 total items for this pre-flight.** Keep the test set small enough that the full experiment finishes in under 2 hours.

Store the test set as `experiments/calibration-preflight/test_set.jsonl` with one item per line: `{"id": ..., "title": ..., "abstract": ..., "ground_truth": "rq1"|"rq2"|"rq3"|"excluded", "source": ..., "justification": ...}`.

## Step 2 — Build the screening pipeline

Use the **exact LLM screening-prompt JSON dictionary** from §3.5.2 of the Wabiski protocol. You can read it verbatim from `papers/Wabiski_2026_CognitiveReviewProtocol/notes.md` (look for the "LLM screening prompt dictionary" section).

For each item in the test set, call the LLM with:
- The Wabiski screening prompt JSON dictionary as the system/user prompt.
- The item's title and abstract as the input.
- Ask for a structured response: `{tag: "screening:rq1" | "screening:rq2" | "screening:rq3" | "screening:excluded", confidence_score: float, exclusion_reason: string | null}`.

**Model choice:** Q confirmed that `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, and `GEMINI_API_KEY` should all be set in this environment. Check them in this order: shell env, project `.env`, `~/.claude/settings.json`, `~/.claude/backups`, `direnv` exports. If only `ANTHROPIC_API_KEY_OLD` is found, **look harder** — Q stated the live keys are present. Check via `env | grep -i -E 'anthropic|openai|gemini'`, check `.envrc`, check any `~/.claude/*.toml` or `~/.claude/env*` files.

**Multi-provider experiment (preferred):** run the test set through ALL THREE providers — Claude (Opus 4.6 or Sonnet 4.6), GPT-4.x / GPT-5 (best available), and Gemini 2.5 Pro — so the calibration report shows cross-model numbers. The Wabiski protocol itself uses GPT-5 and Gemini 2.5, so matching those is high-value. Cross-model ECE/AUROC comparison is the strongest possible evidence for the meeting.

**Budget cap: $10 per API provider.** Do not exceed. Keep the test set ≤ 80 items and estimate cost before running. If a full temperature=1 N=5 pass would exceed the cap on any provider, drop that provider's secondary pass but keep the temperature=0 primary pass.

Do NOT use a mini / haiku / nano / flash-lite tier model. Use the strongest full-size frontier model available from each provider.

**Sampling:** run at temperature 0 for the primary run. Also run a secondary pass at temperature 1 with N=5 samples per item so we can compute self-consistency agreement rate as a secondary confidence signal — BUT only if the budget allows it. Check cost estimates first.

**Fallback rule:** if only ONE provider is accessible, run the full experiment on that one provider and note the single-provider limitation in the report. If ZERO providers are accessible after a thorough search, STOP and report the blocker — do not fake numbers.

Cache LLM outputs to disk so the experiment is reproducible and re-runnable without re-spending tokens.

## Step 3 — Compute metrics

For the primary run (temperature 0, single sample per item):

1. **Confusion matrix** (4 classes: rq1, rq2, rq3, excluded). Overall accuracy. Per-class precision, recall, F1.
2. **Expected Calibration Error (ECE)** using 10 equal-width bins on the verbalized `confidence_score`. Report ECE for:
   - the binary task "correct or not correct" (is the predicted tag the ground truth?)
   - the binary task "include or not include" (is the predicted tag one of rq1/rq2/rq3?)
3. **AUROC** for the "is this item actually an include?" task using the LLM's verbalized `confidence_score` as the classifier score.
4. **Reliability diagram** — plot predicted confidence vs empirical accuracy, 10 bins. Save as PNG.
5. **Threshold analysis** — Wabiski's rule is `>0.90 auto-include, <0.70 auto-exclude`. Report:
   - Number of items that would be auto-included at `confidence > 0.90`. How many of those are actually positives?
   - Number of items that would be auto-excluded at `confidence < 0.70`. How many of those are actually negatives?
   - Number of items in the `0.70-0.90` human-review band. What fraction of the test set?
6. **Histogram** of verbalized confidence scores. Report the modal value and whether the distribution clusters at multiples of 5 (the Xiong 2024 finding).

For the secondary run (temperature 1, N=5 samples per item):

7. Agreement rate per item (fraction of N=5 samples that agree with the modal tag).
8. ECE and AUROC using agreement rate as the confidence signal instead of the verbalized score.
9. Comparison — does self-consistency agreement outperform verbalized confidence as a calibration signal?

Save all metrics to `experiments/calibration-preflight/metrics.json` and `experiments/calibration-preflight/reliability-diagram.png`.

## Step 4 — Write the calibration report

Write `reports/calibration-preflight.md` with:

```markdown
# Calibration pre-flight experiment — inclusive-cartography screening

## Test set
- N = [total]
- Positives: [n_rq1] rq1, [n_rq2] rq2, [n_rq3] rq3
- Negatives: [n_excluded] excluded
- Sources: [breakdown]

## Model and configuration
- Model: [name]
- Temperature: 0 (primary), 1 (secondary, N=5)
- Prompt: verbatim Wabiski §3.5.2 screening dictionary
- API cost: ~$[estimate]
- Wall-time: [duration]

## Primary-run metrics (temperature 0)

### Overall accuracy
[number]

### Per-class performance
| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|

### Confusion matrix
[4×4 table]

### Calibration
- ECE (correctness): [number]
- ECE (include/exclude binary): [number]
- AUROC (include/exclude): [number]
- Reliability diagram: `experiments/calibration-preflight/reliability-diagram.png`

### Threshold analysis
- Auto-include band (>0.90): [count], of which [fraction] correct
- Auto-exclude band (<0.70): [count], of which [fraction] correct
- Human-review band (0.70-0.90): [count] ([fraction of N])

### Confidence distribution
- Modal value: [number]
- Clustering at multiples of 5: [yes/no, which values dominate]
- Comparison to Xiong 2024 finding: [observation]

## Secondary-run metrics (temperature 1, N=5)

### Self-consistency agreement
[numbers]

### Agreement-rate calibration vs verbalized calibration
[which is better, by how much]

## Interpretation for the Wabiski protocol

[3-5 sentences: what do these numbers say about the >0.90 / <0.70 threshold rule in §3.5.2 of the protocol? Do they support or refute the rule as written? What is the concrete recommendation?]

## Limitations of this pre-flight
- [list: small N, synthetic negatives, single model, no human-reviewer second-pass ground truth, etc.]

## Commit hashes
- Code: [hash]
- Results: [hash]
```

## Step 5 — Patch `author-feedback.md` §2.5

After the report exists, append a short paragraph to `papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md` §2.5 "Coverage gap" (or rewrite it as "Coverage gap — empirically closed"). The paragraph should:

- State that the pre-flight was run as recommended.
- Report the headline numbers (ECE, AUROC, percentage of auto-include-band items that were actually correct).
- Point to `reports/calibration-preflight.md` for details.
- Include the concrete recommendation the numbers justify.

This patch is the ONLY edit you make to `author-feedback.md`. Do not touch anything else in the Wabiski paper directory.

## Step 6 — Commit

Use specific file paths — do NOT use `git add .` or `git add -A`.

Separate commits:
1. `experiments/calibration-preflight/` — test set, code, LLM output cache, metrics, plots. Message: `preflight: calibration experiment for Wabiski screening rule`.
2. `papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md` — the §2.5 patch. Message: `feedback: close §2.5 coverage gap with calibration-preflight numbers`.
3. `reports/calibration-preflight.md` — the report. Message: `report: calibration-preflight results`.

Record all commit hashes.

## Step 7 — Final report to foreman

Return ≤10 sentences summarising:
- Whether the experiment ran end-to-end or got blocked (if blocked, exactly where).
- Headline metrics (ECE, AUROC, threshold-band correctness rates).
- Did the Xiong 2024 "80-100% multiples of 5" clustering finding replicate on this task? yes/no and what was observed.
- Whether self-consistency agreement outperformed verbalized confidence.
- The concrete recommendation for the Wabiski protocol (keep / modify / abandon the threshold rule).
- Commit hashes.
- Any items Q should know before opening the report tomorrow morning.

## Rules

- **Timebox: 2 hours wall-time.** If you are not done in 2 hours, commit what you have and write a partial report explaining exactly where you stopped and why.
- **Do not fake numbers.** If the LLM API is unavailable, stop and report that. Do not synthesize confidence scores.
- **Do not install global packages** unless absolutely necessary. Prefer `uv run` with a local venv.
- **Do not run `git add .` or `git add -A`.** Specific paths only.
- **Do not modify any paper directory under `papers/` except `papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md`.** All the seed papers and LLM-confidence papers are read-only for this task.
- **Use the strongest available full-size model** for the LLM calls. No haiku / mini / nano tier.
- **Log everything.** Every API call, every metric computation, every decision should be traceable from the report back to the test set.
