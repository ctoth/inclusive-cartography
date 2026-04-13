# Report: Lin_2022

## Status
success

## Paper directory
papers/Lin_2022_TeachingModelsExpressUncertainty/

## Commit hash
cdb509c

## Retrieval notes
- Primary identifier worked on first try: `https://arxiv.org/abs/2205.14334` via `fetch_paper.py`.
- Metadata resolution: arXiv API gave title/authors/year directly; Semantic Scholar returned 429 twice then 200 — not blocking, arXiv was sufficient.
- No fallback needed. No sci-hub. No paywall.
- PDF size 1.56 MB, `papers\Lin_2022_TeachingModelsExpressUncertainty\paper.pdf` created, `metadata.json` written by the retriever including `arxiv_id: 2205.14334` and `doi: 10.48550/arXiv.2205.14334`.

## Extraction notes
- Page count: 19 (well under 50-page threshold, so Step 2A direct-read lane was used — no chunk protocol).
- Reader: the assigned worker (this agent — Opus 4.6 1M) read every page image directly. No subagent dispatch.
- PNG generation: `magick -density 150 paper.pdf -quality 90 -resize '1960x1960>' pngs/page-%03d.png` produced 19 PNGs, all read in order from page-000 through page-018 before drafting notes.
- No ambiguities or unparseable sections in the main body. The bibliography (pp. 10-13) is typeset in a compact two-column style; citations.md preserves the most argument-relevant entries with a note that the PDF is authoritative for any bibliography entry needing exact canonical formatting.

## Skill deviations
- Q's task prompt explicitly said: "Do NOT invoke `research-papers:source-bootstrap` or `source-promote` — propstore source-branch work is out of scope for this task." I therefore short-circuited the `paper-process` skill's Steps 4-11 and executed only retrieve + read + (skipped reconcile, see below) + commit.
- Reconcile skill was also skipped for parallel-swarm safety — reconcile may write into other workers' paper directories, and the task prompt forbids touching other workers' dirs. Consolidation agent can run reconcile centrally after all workers complete.
- `papers/index.md` was NOT edited (per Q's rules). It is `??` (untracked) in git status regardless of this worker, so nothing to revert.

## Files created
- notes.md: 288 lines
- metadata.json: present (pre-populated by fetch_paper.py; not overwritten, already correct)
- abstract.md: present
- description.md: present (tags: llm-calibration, verbalized-uncertainty, distribution-shift, gpt-3, finetuning)
- citations.md: present
- pngs/: 19 images (page-000.png through page-018.png)

Note: `pngs/*.png` and `paper.pdf` are covered by the repo's root `.gitignore` (`*.pdf`, `*.png`) so they are intentionally NOT part of commit cdb509c. Only the 5 markdown/JSON artifacts are tracked in git. This is expected repo policy, not a failure.

## Key content surfaced for Wabinski 2026 critique
- **Verbalized confidence is a distinct signal, not a reparameterization of logits.** Fig 12 p.19: the finetuned verbalized confidence and the answer-token logit are only weakly correlated. This directly undermines any reviewer protocol that treats "Confidence: 80%" as interchangeable with token probabilities.
- **Best-case out-of-distribution calibration error is still 15-22% MSE on synthetic arithmetic** (Table 1 p.6: Verbalized numbers MSE = 22.0 on Multi-answer, 15.5 on Multiply-divide). These are the numbers for a *finetuned* model on a *narrow* benchmark. Any non-finetuned review-protocol threshold rule should expect worse.
- **Few-shot prompting alone does NOT match finetune quality** (Fig 6 p.7, k = 5/10/25/50). A systematic-review protocol using an off-the-shelf model with an in-context prompt cannot claim the calibration numbers this paper reports.
- **On content-shifted evaluation (Multiply-divide), the zero-shot answer-logit baseline actually beats verbalized numbers on raw MSE** (10.4 vs 15.5). Verbalized calibration is not monotonically superior.
- **Supervised targets were sub-task-level accuracies p̂_T, not per-example 0/1 correctness**, and the authors explicitly early-stopped at n ≈ 2700 to balance "learn sub-task mean" vs "learn per-question signal". The model is therefore calibrated closer to "how hard is this sub-task on average for me" than "am I right on this specific question" — a caveat directly relevant to any protocol that cites this paper as evidence of per-item LM self-knowledge.

## Issues / follow-ups
- No reconcile was run. The consolidation agent should invoke `research-papers:reconcile` on this paper directory once all swarm workers finish, to bidirectionally link it to Kadavath_2022, Mielke_2022, Guo_2017, Ovadia_2019, and any other calibration-line papers in the collection.
- Bibliography extraction is best-effort; a handful of entries in citations.md use short-form canonical names. For any entry used in a downstream claim, verify against papers/Lin_2022_TeachingModelsExpressUncertainty/pngs/page-010.png through page-012.png.
- metadata.json does not include a `venue` field for TMLR — the retriever populated `doi` but left `venue` implicit. If downstream schema requires TMLR explicitly, a follow-up edit may be warranted.
