# Report: Xiong_2024

## Status
success

## Paper directory
papers/Xiong_2024_LLMUncertaintyConfidenceElicitation/

## Commit hash
ccb6dc1 (5 files, 390 insertions: notes.md, metadata.json, abstract.md, description.md, citations.md). Note: `paper.pdf` and `pngs/` are excluded by repo-global `.gitignore` (`*.pdf`, `*.png`); they exist on disk but are not tracked.

## Retrieval notes
Direct arXiv path worked on the first try. Previous worker had stalled in a Semantic Scholar 429 loop on `/graph/v1/paper/ArXiv:2306.13063`; this recovery bypassed S2 entirely.

- Downloaded `https://arxiv.org/pdf/2306.13063.pdf` via `curl -sSL` straight to `papers/xiong-2024.pdf` (1.21 MB).
- Moved to `papers/Xiong_2024_LLMUncertaintyConfidenceElicitation/paper.pdf` with `mv` (not `cp`).
- Confirmed arXiv v2 stamp (17 Mar 2024), ICLR 2024 header.
- **S2 was not touched at all.** No calls to `api.semanticscholar.org`.
- `research-papers:paper-retriever` was not invoked - per the recovery prompt, direct download was the primary path.

## Extraction notes
- **Page count:** 29 (verified via `pypdf.PdfReader`; `file` command misreports as "4 page(s)" because of PDF version 1.5 trailer format).
- **Not chunked:** 29 <= 50 page threshold, so direct read applied.
- **Reader model:** this worker (Claude Opus 4.6, 1M context) - no subagent dispatch.
- **Reading method:** hybrid. Read `pngs/page-000.png` as image to confirm title/authors/venue/layout, then used `pdftotext -layout` to produce `paper.txt` for the body pass (pulled in entirety through `Read` on offsets 1-1000 and 1000-1400 and 1400-1770, covering all 29 pages' worth of text). `paper.txt` was deleted after notes were written (temp artifact).
- **Ambiguities:** Appendix B tables are pdftotext-ugly (columns misaligned), but the key numbers in Tables 2, 3, 4, 13 were readable. A second-pass direct image read of a few appendix tables would firm up the parameter table, but the core numbers are in `notes.md`.
- **Equations captured:** Multi-Step product, Consistency (eq 1), Avg-Conf (eq 2), Pair-Rank MLE objective (eq 3-4), Pair-Rank Proposition 3.1 conditional.
- **notes.md line count:** 293, exceeds the 50-line sanity threshold by a wide margin.
- **Five full prompt templates (Vanilla, CoT, Self-Probing, Multi-Step, Top-K)** captured from Tables 14-18.

## Files created
- notes.md: 293 lines
- metadata.json: present
- abstract.md: present
- description.md: present
- citations.md: present
- pngs/: 29 images (page-000.png through page-028.png)
- paper.pdf: present (moved from papers/ root)

No `chunks/` directory (not needed for <=50 page paper).

## Cross-citations relevant to the Wabiski LLM-confidence critique

High-value findings for Q's meeting:

1. **Vanilla verbalized confidence is systematically overconfident.** Values cluster in 80-100% in multiples of 5, mimicking human dialogue patterns (Zhou et al. 2023). True across all 5 tested models (GPT-3, GPT-3.5, GPT-4, Vicuna, LLaMA2). This is the load-bearing empirical claim for the critique.

2. **ECE alone is an insufficient gate.** Xiong explicitly shows that CoT on GPT-4 GSM8K achieves near-optimal ECE=0.064 by assigning 100% confidence to every sample (accuracy 93.6%) - but AUROC is near random because all samples receive identical confidence. *Any* protocol that uses ECE as the sole calibration test is broken by construction. *(p.7-8)*

3. **The best black-box configuration is Top-K + Self-Random (M=5) + Avg-Conf or Pair-Rank**. This is a concrete counter-prescription the critique can propose.

4. **The white-box / black-box gap is narrow** (~0.522 to ~0.605 in AUROC). So switching to a logit-exposing model does not rescue the situation. *(p.9, Appendix B.1)*

5. **Professional-knowledge tasks defeat all methods.** Prf-Law (MMLU) is the hardest dataset; even Pair-Rank AUROC stays near 0.66. If the cartography protocol applies LLMs in specialist sub-domains (tactile-map standards, specialized cartographic conventions), confidence signals are unreliable. *(p.9)*

6. **Persona prompts ("You are a confident GPT" vs "You are a cautious GPT") do not shift calibration.** Any protocol that relies on *instructed* calibration rather than *measured* calibration has no empirical support. *(p.18, Table 7)*

7. **Sampling variance is the single biggest lever for failure prediction.** GSM8K AUROC jumps from 54.8 (CoT M=1) to 92.7 (Self-Random M=5 + Consistency). Any protocol that issues one query per confidence-sensitive decision is leaving the most important calibration signal on the table. *(p.8)*

Cross-links to collection papers already retrieved:
- `papers/Tian_2023_JustAskCalibrationStrategies/` - closest concurrent work; Top-K originated there.
- `papers/Lin_2022_TeachingModelsExpressUncertainty/` - the fine-tuning approach Xiong's black-box framework is positioned against.
- `papers/Kadavath_2022_LanguageModelsMostlyKnow/` - white-box self-evaluation counterpart.

New leads worth retrieving:
- Kuhn, Gal, Farquhar 2023 - Semantic Uncertainty (motivation for going black-box).
- Zhou, Jurafsky, Hashimoto 2023 - Navigating the Grey Area (explains the 80-100% clustering).

## Issues / follow-ups
- **Skipped `source-bootstrap`, `register-concepts`, `extract-claims`, `extract-justifications`, `extract-stances`, `source-promote`, `pks build`.** Per the base `retrieve-and-process-paper.md` prompt, propstore source-branch work is out of scope for swarm workers. The nested `paper-process` skill attempted to run all 12 steps; only Steps 2-3 (read, clean root PDF) + my own write/verify/commit were executed.
- **Did not update `papers/index.md`.** Per parallel-swarm rules, the consolidation agent handles the index. Verified `papers/index.md` is in the same state as the git snapshot (untracked, unchanged by this worker).
- **Did not run reconcile.** Base prompt allows the internal reconcile step inside paper-process, but I did not invoke paper-process; I invoked paper-reader-equivalent steps manually to respect the 8-minute budget and to avoid the reconcile step touching other workers' dirs. Cross-citations to collection papers are documented in `citations.md` and in this report instead.
- **paper.txt deleted** after notes extraction (was a temp pdftotext dump).
- **Eight-minute budget:** under budget. No retries on the arXiv URL.
