# Report: Tian_2023

## Status
success

## Paper directory
papers/Tian_2023_JustAskCalibrationStrategies/

## Commit hash
1686704e6d05accb560560542f3771ab8a418d69

## Retrieval notes
- Primary identifier `https://arxiv.org/abs/2305.14975` worked. No fallback needed.
- First invocation attempted as a backgrounded bash command; the harness captured only stderr (INFO lines showing S2 metadata getting repeated 429 rate-limit responses). Re-ran synchronously, S2 recovered on the 2nd retry, and the arxiv direct-download path produced the canonical paper directory and PDF in one shot. Treat the background-mode stdout capture as a harness quirk, not a fetch_paper.py bug.
- Source path: arxiv direct download. No sci-hub / Chrome automation required.
- `paper.pdf` = 964830 bytes. Confirmed valid PDF by downstream processing (page image extraction succeeded).

## Extraction notes
- Page count: 10 pages (`pdfinfo` confirmed).
- Read mode: direct read (≤50 pages threshold), no chunk workers dispatched.
- All 10 page images read by this worker (no sub-agent delegation).
- Venue from the LaTeX footer: "Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing" i.e. EMNLP 2023; added to metadata.json explicitly (fetch_paper only populated arxiv_id + abstract, not venue).
- Tables 1-3 were read visually. Exact per-cell numbers (e.g. GPT-4 / TriviaQA ECE ≈ 0.039, Claude-2 / SciQ ECE ≈ 0.028) are captured in notes.md but should be cross-checked if precise numbers are load-bearing for the critique.
- Prompt templates in appendix B (page 8) and appendix C (page 9) were captured verbatim in notes.md under Methods & Implementation Details.
- No unparseable sections.

## Files created
- notes.md: 238 lines
- metadata.json: present (augmented with `doi: null` and `venue: "EMNLP 2023"` on top of the fetch_paper seed)
- abstract.md: present (verbatim + interpretation)
- description.md: present (tags: `llm-calibration, rlhf, verbalized-uncertainty, confidence-elicitation, prompting`)
- citations.md: present (full reference list from pages 5-6 + 5 key follow-ups)
- pngs/: 10 images (page-000.png .. page-009.png) — NOTE: not tracked by git per `.gitignore` (`*.png`)
- paper.pdf: present — NOTE: not tracked by git per `.gitignore` (`*.pdf`)

Commit `1686704` contains only the 5 markdown + JSON files; the 10 PNGs and 1 PDF live on disk but are .gitignore'd, consistent with the rest of the collection.

## Reconciliation notes
Cross-references added to `papers/Tian_2023_JustAskCalibrationStrategies/notes.md`:
- **Already in Collection:** `Kadavath_2022_LanguageModelsMostlyKnow` (P(True) baseline that Tian beats; Kadavath also observed RLHF miscalibration), `Lin_2022_TeachingModelsExpressUncertainty` (Tian's direct predecessor — Lin required finetuning on GPT-3, Tian achieves the same signal zero-shot on RLHF-LMs via prompting).
- **New Leads:** Xiong et al. 2024 (flagged in Wabiski_2026/author-feedback.md §2.5 as the next paper in the LLM-calibration cluster), Kuhn/Gal/Farquhar 2023 "Semantic Uncertainty", Zhou/Jurafsky/Hashimoto 2023 "Navigating the grey area", Guo et al. 2017 (canonical ECE), Xiao et al. 2022.
- **Cited By:** `Brock_2015_InteractiveMapsUsability` — Brock's own reconcile pass (peer worker, earlier today) already added a conceptual link to Tian in Brock/notes.md line 312 on the grounds that Brock's human-side Likert-confidence degradation is an analog to Tian's ECE story.
- **Conceptual Links:** `Wabiski_2026_CognitiveReviewProtocol` — Tian et al. 2023 is the primary empirical citation needed to ground (or contest) Wabiski's 0.90/0.70 confidence-threshold rule (Wabiski notes.md line 58). Tian's in-distribution ECE of ~0.03-0.04 on GPT-4/Claude-2 bounds how good the thresholds can be; the lack of OOD evaluation bounds how confidently they can be transferred to systematic-review screening. Wabiski_2026/author-feedback.md §2.5 explicitly flagged this paper as a coverage gap.

**Reconcile scoped to forward-references from Tian_2023 only.** I did not write reciprocal entries into Lin_2022/notes.md, Kadavath_2022/notes.md, or Wabiski_2026/notes.md because the parallel-swarm rule in `prompts/retrieve-and-process-paper.md` says: "You MUST only touch files inside your own paper directory" and "do not initiate cross-paper work yourself." The consolidation agent that runs after the swarm should finish the bidirectional annotation using the forward-refs in this paper's Collection Cross-References section as input.

`papers/index.md` was not modified by this worker and remains in whatever state the other workers + the consolidation agent are managing (currently it is untracked, containing only the Wabiski_2026 entry).

## Provenance stamping
Skipped: the parent prompt `prompts/retrieve-and-process-paper.md` explicitly forbids `source-bootstrap` / `source-promote` and by extension `pks source stamp-provenance`, which requires an initialized source branch. No provenance stamp was written to `notes.md`.

## Issues / follow-ups
- **Numeric cells in Tables 1-3 are approximate in notes.md.** They were read from page images visually, not parsed from a LaTeX source. If the Wabiski critique pins a specific number (e.g. "GPT-4 ECE on TriviaQA = 0.039"), re-verify against the PDF before quoting.
- **Appendix tables 5+ not inventoried.** Only Tables 1-4 and the prompt templates were transcribed; any further appendix tables (if present beyond the linguistic-usage histograms) were not captured.
- **Xiong et al. 2024 is flagged as a new lead** — the author-feedback.md §2.5 "cluster of four" becomes "cluster of three + Xiong pending" after this retrieval. Worth retrieving in a follow-up batch.
- **.gitignore excludes the PDF and PNGs.** Per project convention this is fine, but it means the committed paper directory has only the markdown + JSON; the page images and source PDF live only on the local filesystem for this working copy. Any downstream agent that needs to re-read the PDF should re-fetch via the arxiv ID in metadata.json.
- **Bidirectional reconcile annotation is incomplete by design.** Lin_2022, Kadavath_2022, and Wabiski_2026 do not yet have reciprocal `### Cited By` / `### Conceptual Links` entries pointing to Tian_2023. Left for the post-swarm consolidation agent.
