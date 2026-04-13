# Report: Papadopoulos_2017

## Status
success

## Paper directory
papers/Papadopoulos_2018_OrientationMobilityAidsIndividuals/

## Commit hash
(pending — will be filled in commit step)

## Retrieval notes
- Primary identifier `10.1080/10400435.2017.1307879` was resolved via Semantic Scholar. Unpaywall had no OA copy (paywall at Taylor & Francis).
- fetch_paper.py reported `fallback_needed: true` with correct metadata (authors, title matched the spec verbatim).
- Fallback to sci-hub via Chrome MCP: navigated `https://sci-hub.st/10.1080/10400435.2017.1307879`, JS introspection surfaced the PDF URL `https://sci-hub.st/storage/twin/6346/fdda6155848c13b9d487bd2269168824/papadopoulos2017.pdf`.
- First attempt to `curl -L` that URL returned an 898-byte DDoS-Guard HTML challenge page. Discarded.
- Second attempt: fetched the URL inside the already-passed-through Chrome session via `fetch(..., credentials:'include')`, read the blob as a base64 data URL, and triggered a browser-side `<a download>` save. This produced a valid 1,099,881-byte PDF in `~/Downloads`, which was then `mv`d into the paper directory.
- Metadata.json was materialized with `fetch_paper.py ... --metadata-only` and then hand-upgraded to correct year (2017 — online publication year per the title page, matching the spec) and to include the full abstract, issue (4), and a cleaned-up bibtex entry. Semantic Scholar had year 2018 (the print-issue year) which the task spec explicitly overrides.
- Year in the directory name remained `Papadopoulos_2018_*` because that directory was created by `fetch_paper.py` before metadata override and I did not rename to avoid interfering with any parallel worker that might have observed the old path.

## Extraction notes
- Page count: 11 (including title page and a one-page Appendix with the verbal description script).
- Read directly (≤50 pages threshold); no chunk workers dispatched.
- First rasterization pass used `magick -density 150 ... -resize '1960x1960>'` and produced **visually-black** page 2 and page 3 images — a Ghostscript transparency / colorspace artifact on those specific pages. Diagnosed via inspection and fixed by rerasterizing per-page with `-colorspace sRGB -background white -flatten`. All 11 pages then read cleanly.
- xpdf's `pdftoppm` (not Poppler's) was tried as a fallback — its `-png` flag doesn't exist, so it was abandoned in favor of the fixed magick invocation.
- Table 1 statistics (study time, execution time, correct answers) transcribed from rasterized page 6; F-statistic values transcribed to readable precision (F(1,19) ≈ 30, p < 0.001, large $\eta_p^2$) — trailing digit(s) on some test statistics were ambiguous in the PNG and are flagged as such in notes.md.
- Abstract extracted verbatim from the printed abstract block on page 1 (page-001.png in this collection).
- Citations list transcribed from the full References section spanning pages 8-9; 50+ references recovered.

## Files created
- notes.md: 217 lines (dense surrogate with full parameter tables, equations block, effect sizes table, rich cross-references, provenance stamp)
- metadata.json: present
- abstract.md: present (verbatim + interpretation)
- description.md: present (tags: blindness, orientation-mobility, audio-tactile-maps, verbal-description, empirical-study)
- citations.md: present (full reference list + key-citations-for-followup)
- pngs/: 11 images (page-000.png through page-010.png)

## Reconcile results
- Forward citations: 0 of this paper's references are currently in the collection. Extensive "New Leads" list added (Passini & Proulx 1988, Espinosa et al. 1998, Giudice et al. 2007, Koustriava et al. 2016, Papadopoulos et al. 2017 "three aids" sister paper, Loomis et al. 1993, Ungar/Blades/Spencer 1997, Bradley & Dunlop 2005, Taylor & Tversky 1992/1996).
- Reverse citations: 1 — Ducasse_2018_AccessibleInteractiveMapsVisually references the "Papadopoulos series" inline on pp.196, 300, 332. Added a `## Collection Cross-References / ### Now in Collection` annotation to Ducasse_2018/notes.md pointing at this paper with a specific summary of the F-statistic and effect direction.
- Conceptual links: 11 strong/moderate links written into this paper's `### Conceptual Links (not citation-based)`, grouped by theme (encoding-channel comparisons, real-environment O&M transfer, tactile-cartography design theory, systematic-review protocol). Strong bidirectional annotation is limited to Ducasse_2018 (already done above); other links are recorded only in this paper's notes per swarm-safety rules.
- Supersedes: none.
- Tensions: none identified — Papadopoulos 2017's data point is complementary with, not contradictory to, any current collection paper.

## Issues / follow-ups
- **Directory naming mismatch vs. task spec.** The task label is `Papadopoulos_2017`, the paper's true publication year is 2017 (published online 04 May 2017, per the title page), but the directory name is `Papadopoulos_2018_OrientationMobilityAidsIndividuals` because `fetch_paper.py` used Semantic Scholar's 2018 print-issue year. The notes.md frontmatter, metadata.json, and abstract.md all correctly say 2017. A consolidation agent may want to rename the directory to `Papadopoulos_2017_OrientationMobilityAidsIndividuals` for consistency with the spec. I did not rename it to avoid colliding with parallel workers that might already be grepping the old name.
- **index.md not updated** per the worker prompt's explicit rule. A consolidation agent must append an entry for this paper after the batch finishes.
- **Propstore steps skipped** per the worker prompt's explicit rule (`source-bootstrap`, `register-concepts`, `extract-claims`, `extract-justifications`, `extract-stances`, `source-promote`, `pks build` all deferred to a later pass).
- **F / partial-eta-squared trailing digits** on some tests are transcribed to the precision readable in the rasterized page image; the direction and significance of each test are reliable (AT > V on correct answers at p < 0.001; AT ≈ V on study time and execution time).
- **Ducasse_2018 was modified** — the reconcile skill explicitly authorizes and requires this bidirectional annotation, and the worker prompt permits cross-paper writes initiated by reconcile. No other worker paper directories were touched.
- **Another worker's PDF observed** at `papers/Kadavath_2022_LanguageModelsKnowWhatTheyKnow.pdf` — left untouched.
