# Calibration pre-flight

Empirical test of whether the Wabiński 2026 §3.5.2 LLM-screening threshold
rule (`confidence > 0.90` auto-include, `< 0.70` auto-exclude, `0.70–0.90`
human review) is defensible on the inclusive-cartography title/abstract
screening task.

This is the first experiment in the repository and it exists to answer one
question before the protocol gets applied in anger: **does the verbalized
confidence emitted by current frontier models actually route anything to
the human-review band, or does the rule collapse to "always auto-include"?**

## Headline finding

The threshold rule is **effectively inoperative on this task.** Both
GPT-5 and Gemini 2.5 Pro emit verbalized confidences so top-heavy that
the human-review band is nearly empty (GPT-5 15.4%, Gemini 0%) and the
auto-include band swallows almost every item, true positive or true
negative. The underlying classifier is fine — both models hit AUROC 1.0
on the include/exclude binary — but the calibration layer is the failure
point.

Gemini 2.5 Pro strongly replicates the Xiong 2024 finding that 80–100% of
verbalized confidences cluster at multiples of 0.05 (84.6% on this run).
GPT-5 does not replicate on the multiples-of-5 axis but is still severely
right-skewed, with 67% of values at exactly `0.99`.

**Full writeup with metrics, confusion matrices, threshold analysis, and
recommended §3.5.2 replacements:** [`reports/calibration-preflight.md`](../../reports/calibration-preflight.md).

## Test set

- **N = 52** items. 17 positives (13 repo seed papers + 4 arXiv keyword
  retrievals) and 35 negatives drawn from arXiv `cs.CG`, `cs.GR`, `cs.CV`,
  `stat.ML` plus "hard-negative" queries (`self-organizing map`, WCAG).
- **Label distribution:** rq1 = 3, rq2 = 13, rq3 = 1, excluded = 35.
  Intentionally unbalanced toward negatives and light on rq3.
- **Ground truth:** positives hand-assigned to rq1/rq2/rq3 from each
  paper's `index.md` tags mapped to Wabiński research-question
  definitions; negatives are `excluded` by construction.
- **Provenance:** every abstract is verbatim from a real published paper.
  Seeds come from `papers/<name>/abstract.md`; arXiv items come from the
  arXiv Atom API. No abstracts were synthesized.
- **File:** `test_set.jsonl` — one JSON object per line with `id`, `title`,
  `abstract`, `ground_truth`, `source`, `justification`.

## Models

- **OpenAI `gpt-5`** via the Responses API. Does not accept user-controlled
  temperature on its Responses API, so the primary pass runs at API
  default — read single-sample ECE numbers accordingly.
- **Google `gemini-2.5-pro`** via `google-genai` with
  `response_mime_type=application/json`.
- **Anthropic Claude: not run.** No live `ANTHROPIC_API_KEY` was available
  in the environment (`~/.claude/.credentials.json` holds OAuth tokens for
  a Claude Max subscription, which is not usable against the Anthropic
  API). This is the primary limitation of this run — a follow-up should
  add Claude Opus 4.x.

Prompt is the Wabiński §3.5.2 screening dictionary pulled verbatim from
`papers/Wabiski_2026_CognitiveReviewProtocol/notes.md` lines 193–232,
wrapped in a minimal instruction that asks for a JSON object with
`tag`, `confidence_score`, `exclusion_reason`.

Primary-pass cost: ~$0.25 OpenAI + ~$0.09 Gemini. Well under the
$10-per-provider budget cap. Wall-time ~11 minutes, Gemini occasionally
throttled by 503 `UNAVAILABLE` from the public API.

## Layout

```
experiments/calibration-preflight/
├── README.md                  # this file
├── pyproject.toml             # uv project
├── build_testset.py           # builds test_set.jsonl from repo + arXiv
├── run_screening.py           # runs LLM passes, caches per item
├── compute_metrics.py         # ECE / AUROC / confusion / plots
├── test_set.jsonl             # 52 items, generated
├── cache/
│   ├── openai/gpt-5/          # per-item JSON responses
│   └── gemini/gemini-2.5-pro/
├── metrics.json               # primary + (optional) secondary metrics
├── reliability-diagram.png    # from compute_metrics.py
└── confidence-histogram.png   # from compute_metrics.py
```

The full report lives outside the experiment directory at
[`reports/calibration-preflight.md`](../../reports/calibration-preflight.md);
investigation notes and the decision trail live at
[`notes/calibration-preflight.md`](../../notes/calibration-preflight.md).

## Reproducing

```bash
cd experiments/calibration-preflight
uv run python build_testset.py            # writes test_set.jsonl
uv run python run_screening.py            # primary pass (cached)
uv run python compute_metrics.py          # metrics + plots
RUN_SECONDARY=1 uv run python run_screening.py   # optional N=5 temp=1 pass
```

All LLM outputs are cached per item under `cache/{provider}/{model}/`,
so re-running after the first pass is free. Delete a cache subdirectory
to force a re-query for that provider.

Required environment variables: `OPENAI_API_KEY`, `GEMINI_API_KEY`.
Set `ANTHROPIC_API_KEY` to extend the run to Claude once keys are
available (the run scripts will need a small addition — not wired up in
this pre-flight).

## Known limitations

- **N is small** (52). Headline numbers carry wide binomial CIs.
- **Negatives are too easy.** arXiv `cs.CG`/`cs.GR`/`cs.CV`/`stat.ML`
  abstracts are obvious out-of-scope; a harder near-miss pool would push
  AUROC below 1.0.
- **Class skew:** only 1 rq3 item and only 3 rq1 items. Per-class
  numbers for rq1 and rq3 are not reliable.
- **Single-provider gap:** Anthropic Claude missing (see above).
- **No human-reviewer second pass.** Ground truth is derived from
  existing repo labels and arXiv query provenance, not from two
  independent screeners with inter-rater agreement.
- **GPT-5 primary is not greedy:** the Responses API does not honor
  `temperature=0`, so the GPT-5 primary is a single sample from the
  API-default distribution.
- **Single-sample primary:** per-item ECE is computed on one sample per
  item, not an expectation over samples. The optional secondary pass
  (N=5, temperature=1) exists to produce an agreement-rate signal with
  more measurement resolution than verbalized confidence.
