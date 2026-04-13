# Report: Brock_2015

## Status
success

## Paper directory
papers/Brock_2015_InteractiveMapsUsability/

## Commit hash
8f4f31469c51bb55f6784d3b6ce95accbb93bb2f

## Retrieval notes
Primary identifier `https://hal.science/hal-01077434` (HAL landing page) was a weak URL — normalized by fetching `https://hal.science/hal-01077434/json` to resolve the direct PDF URL `https://hal.science/hal-01077434v1/file/AcceptedManuscript-HCI-2014.pdf` (author's accepted manuscript, open access, 1.7 MB, 47 pages). Downloaded directly via `curl -sL`. No sci-hub, no paywall hit, no retries, no fallback identifier needed. The fallback DOI `10.1080/07370024.2014.924412` was not used.

## Extraction notes
- 47 pages total, ≤50 so read directly without chunk protocol.
- Read by Claude Opus 4.6 (1M context), no subagent delegation.
- Page 0 is the HAL cover sheet; actual paper content runs pages 1–47 (author's accepted manuscript layout with internal page numbers "-1-" to "-45-").
- All 47 page images inspected via Read tool.
- Paper is an empirical within-subjects usability study with a clean hypothesis structure; extraction includes ANOVA F-values, Wilcoxon Z-values, SUS means, learning-time ratios, and a full Landmark/Route/Survey decomposition across short-term and 2-week long-term phases.
- Supplementary material section (pp. 42–45) repeats figure descriptions — included in notes implicitly via the primary figure captions.

## Files created
- notes.md: 332 lines
- metadata.json: present
- abstract.md: present
- description.md: present
- citations.md: present
- pngs/: 47 images (gitignored per project `.gitignore` — *.png excluded)
- paper.pdf: present in paper directory (gitignored per project `.gitignore` — *.pdf excluded)

## Issues / follow-ups
- papers/index.md was deliberately NOT updated per parallel-swarm rules in `prompts/retrieve-and-process-paper.md`. The consolidation agent should add an index entry for Brock_2015_InteractiveMapsUsability.
- Per parent prompt, `research-papers:source-bootstrap`, `register-concepts`, `extract-claims`, `extract-justifications`, `extract-stances`, `source-promote`, and `pks build` were NOT invoked — out of scope.
- Reconcile: bidirectional annotation of citing papers in the collection was skipped (per parent rules: "You MUST only touch files inside your own paper directory"). Forward-only cross-references (Already in Collection / New Leads / Cited By / Conceptual Links) were written to this paper's notes.md based on read-only grep across collection notes. Consolidation agent should propagate reciprocal "Cited By" annotations to the seven citing papers identified (Ducasse_2018, Brulé_2016, Holloway_2018, Götzelmann_2016, Gual_2015, Papadopoulos_2018, Rowell_2003).
- Key cross-reference payload for the tomorrow-morning meeting: Brock's finding that user self-reported confidence correlates with spatial scores short-term but dissociates from them after a 2-week delay (landmarks decay ~45% while confidence holds) is a direct empirical parallel to the Kadavath_2022/Lin_2022/Tian_2023 LLM-confidence calibration literature and is usable as a critique payload against the Wabiski_2026 protocol's >0.90 LLM auto-include confidence threshold.
- No ambiguities or unparseable sections. No OCR/extraction blockers.
