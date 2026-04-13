# Task: Consolidate papers/index.md, full reconcile, update author-feedback.md, meeting brief

You are the single consolidation agent running **after** 16 of 17 parallel retrieval workers finished processing papers into `papers/{Author_Year_ShortTitle}/` directories. One retrieval (Lobben_2015) failed permanently due to paywall — leave it failed and flag it for Q.

## Context

Q's project `inclusive-cartography` executed a seed-paper retrieval swarm + 4 LLM-confidence papers for a systematic-review protocol critique. Q has a meeting tomorrow morning and needs:
1. A clean `papers/index.md` with all new paper entries.
2. Full cross-collection reconcile (workers ran per-paper reconcile but saw incomplete state).
3. The existing draft feedback file updated with the four new LLM-confidence citations.
4. A one-page meeting brief.

All worker commits and caveats are captured in `notes/seed-retrieval-swarm.md` — **read that first** before anything else. Also read each `reports/retrieve-*.md` for per-worker details.

## Procedure

### 1. Inventory and read reports
- `ls papers/` — list current paper directories.
- Read `notes/seed-retrieval-swarm.md` in full for the coordinator's synthesis of worker output.
- Read every `reports/retrieve-*.md` — there should be ~17 of them. Extract: commit hash, paper dir name, any flagged caveats.
- Note known issues from the swarm notes:
  - **Rowell_Ungar_2003 identity mismatch:** DOI resolved to TCJ "Results" paper, not BJVI "Part 1: Production". Flag but do not retry.
  - **Gotzelmann / Papadopoulos cross-commit:** files from one got swept into the other's commit via git-index race. Files are on disk; nothing lost. Note in report.
  - **Papadopoulos_2018 dirname vs 2017 year:** online publication year is 2018 so the dirname is technically correct for the record-of-record but the paper-spec said 2017. Leave as-is.
  - **Palivcová first-author name:** worker corrected "Daniela" → "Dominika". Correct.
  - **Lobben_2015 FAILED:** strictly paywalled. Do NOT retry. Flag for Q.
  - **Unicode umlaut in Götzelmann_2016 dirname:** Windows path with umlaut — watch for any tool that can't handle it.

### 2. Rebuild papers/index.md
- Read the current `papers/index.md` (one of the workers may have touched it despite the rule).
- For every paper directory that exists under `papers/`, verify there is an `index.md` entry. If missing, append one in the format `## {dirname}  (tag1, tag2, tag3)` followed by the body of `papers/{dirname}/description.md` (strip the frontmatter).
- Sort entries alphabetically if the file is small; otherwise preserve existing order and append missing entries at the end.
- Commit the index update as ONE commit.

### 3. Full-collection reconcile
- Invoke the `research-papers:reconcile` skill on each paper directory (or with `--all` if supported). This idempotently fixes cross-references that per-worker runs missed due to parallel execution.
- If reconcile touches paper-directory files, `git add` them in ONE commit with message `consolidate: full reconcile after seed-paper swarm`. Do not split per paper.

### 4. Update papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md
The existing draft feedback file in that directory contains a §2.2 with citations to Freedman 2025, Guo 2017, Sensoy 2018, Fang 2025 (all from the propstore collection). The swarm just added FOUR directly-relevant LLM-verbalised-confidence papers to this repo's own `papers/`:

- `Tian_2023_JustAskCalibrationStrategies/notes.md` — EMNLP 2023. Key finding: ECE ~= 0.03-0.04 for GPT-4/Claude-2 on in-distribution factoid QA with two prompt fixes (two-step + top-k elicitation). In-distribution only — OOD behavior unvalidated.
- `Lin_2022_TeachingModelsExpressUncertainty/notes.md` — TMLR 2022. Key finding: verbalized confidence only weakly correlated with answer-token logits (Fig 12); OOD calibration MSE 15-22% even after finetuning; training targets were sub-task level not per-example.
- `Kadavath_2022_LanguageModelsMostlyKnow/notes.md` — Anthropic 2022, 43 pages. Anthropic mixed-results paper on LLM self-evaluation.
- `Xiong_2024_LLMUncertaintyConfidenceElicitation/notes.md` — ICLR 2024, 293-line notes. **Strongest direct refutation of Wabiski's rule:** LLMs verbalize confidence in 80-100% multiples-of-5 regardless of ground truth. GPT-4 CoT on GSM8K achieves ECE 0.064 by assigning 100% to every answer while AUROC ≈ random. White-box vs black-box AUROC gap narrow (0.522 vs 0.605). Recommended stable config: Top-K prompt + Self-Random M=5 + Avg-Conf or Pair-Rank.

**Your job:** read each of those four `notes.md` files, extract 2-4 verbatim key findings with page citations per paper, and splice them into `author-feedback.md` §2.2 as new subsections **(e)**, **(f)**, **(g)**, **(h)** with the same prose structure as the existing (a)-(d). Do NOT delete or rewrite existing content — add to it. Also update §2.5 "Coverage gap" to note that these four papers are NOW in the collection and the gap is closed.

Commit as `feedback: augment author-feedback with Tian/Lin/Kadavath/Xiong citations`.

### 5. Write the meeting brief
Write `reports/meeting-brief-2026-04-13.md`:

```markdown
# Meeting brief — 2026-04-13 morning
## Wabiski protocol review + seed-paper retrieval status

## What got done
- 16 of 17 target papers retrieved and processed.
- 13 seed papers for §3.3 (1 failed, Lobben_2015 paywall).
- 4 LLM-verbalised-confidence papers for the critique section of author-feedback.

## Papers ready for discussion
[table with columns: label | rq_tags | notes_lines | commit | key_finding_for_meeting]

## What Q should raise first
1. [most important talking points — seed coverage, RQ assignment]
2. [LLM-confidence critique now has direct empirical citations — specifically Xiong 2024's 80-100% multiples-of-5 finding]
3. [Lobben_2015 paywall — ILL request or author email]

## Known issues / caveats
- Rowell_Ungar_2003 identity mismatch (TCJ vs BJVI Part 1) — decide whether to retry
- Papadopoulos year (2017 vs 2018 dirname)
- Götzelmann Unicode dirname
- Gotzelmann/Papadopoulos cross-commit artifact

## Open decisions
- Do we retrieve Rowell_Ungar Part 1 (BJVI) as a separate paper?
- Do we pursue Lobben_2015 via ILL?
- When do we send author-feedback to Wabiski?
```

### 6. Commit everything
Separate commits per logical unit:
- `consolidate: papers/index.md update`
- `consolidate: full reconcile after seed-paper swarm`
- `feedback: augment author-feedback with Tian/Lin/Kadavath/Xiong citations`

Record all three commit hashes.

### 7. Final report
Write `reports/consolidate-index-and-reconcile.md` with:

```markdown
# Consolidation report

## Status
[success | partial]

## Commits
- index.md: [hash]
- reconcile: [hash]
- author-feedback: [hash]

## Papers indexed
[list]

## Retrieval summary
- Succeeded: 16 (list)
- Failed: 1 (Lobben_2015 — paywall)
- Partial / caveats: [list with reasons]

## Reconcile summary
[what reconcile changed this pass]

## Author-feedback update summary
[which sections were edited, what was added]

## Meeting brief
Written to: reports/meeting-brief-2026-04-13.md

## Follow-ups for Q
[open decisions from the brief]
```

## Rules

- Do NOT retrieve additional papers. The Lobben_2015 failure is out of scope for you.
- Do NOT overwrite worker content inside paper directories except via the reconcile skill.
- Do NOT use `git reset`, `git checkout`, `git restore`, `git clean`, `git add -A`, `git add .`. Specific paths only.
- Do NOT touch `papers/Wabiski_2026_CognitiveReviewProtocol/notes.md` or any of its other files except `author-feedback.md`.
- 15-minute budget. If you cannot finish everything in 15 minutes, prioritize: (1) author-feedback update, (2) meeting brief, (3) index.md, (4) reconcile. Commit whatever you finished and flag the rest.
