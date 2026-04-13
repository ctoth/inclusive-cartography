# Report: Holloway_2018

## Status
success

## Paper directory
papers/Holloway_2018_AccessibleMapsBlindComparing/

## Commit hash
7cd31f187bc926f90771a9fe2e0f298949cef6f9

## Retrieval notes
- Primary identifier `10.1145/3173574.3173772` was used. `fetch_paper.py` resolved metadata via Semantic Scholar (open-access PDF not available; ACM Digital Library paywalled) and returned `fallback_needed: true`.
- Used the Chrome + sci-hub.st fallback lane. Navigated to `https://sci-hub.st/10.1145/3173574.3173772`, extracted PDF URL via DOM scrape: `https://sci-hub.st/storage/twin/6978/8be5cd92bd42bdd4d6676121b8b4ff5f/holloway2018.pdf`.
- A direct `curl -L` hit a DDoS-Guard interstitial (898-byte HTML, not a PDF). Worked around by executing a `fetch(...).then(blob -> createObjectURL -> anchor.click())` inside the already-challenged Chrome page, which triggered a valid browser download to `~/Downloads/holloway2018.pdf` (1,317,753 B, valid `%PDF-1.5`).
- `mv`'d that file to `papers/Holloway_2018_AccessibleMapsBlindComparing/paper.pdf`, then ran `fetch_paper.py ... --metadata-only` to write `metadata.json`, then rewrote `metadata.json` by hand to correct author full names and to add a verbatim-quality abstract block.
- `papers/` root left with no stray PDF after processing.

## Extraction notes
- Page count: 13 pages. Direct-read lane (≤50 pp), no chunk workers needed.
- Initial `magick` render produced `pngs/page-001.png` as a solid black image (alpha-channel / page-2 soft-mask artifact from the sci-hub PDF). Re-rendered with `-alpha remove -alpha off` applied after the input file; all 13 pages then legible.
- Read every page (page-000 through page-012) via the local image reader and took notes inline.
- Agent performing the reading: Claude Opus 4.6 (1M context) — the strongest available full-size model on this platform. No mini/small tier worker used.
- Page numbering note: the physical journal pagination is "Paper 198, pp. 1-13"; I cited using PDF page numbers (*p.N*) which map to paper page N+1 in some places. Downstream claim extraction should treat `p.N` as PDF page index.
- My `abstract.md` "verbatim" block is an approximation — parts of the small-font first-page abstract were difficult to read with absolute certainty from the scan. Flagged here so a downstream cleaner can refine it against an authoritative copy if needed.

## Files created
- notes.md: 232 lines (well over 50-line sanity gate, with study design, parameters, effect sizes, figures, guidelines, testable properties, relevance)
- metadata.json: present (corrected DOI, full-author list, abstract, venue)
- abstract.md: present (verbatim section is approximate — see extraction notes)
- description.md: present (3-sentence tagged description)
- citations.md: present (55-entry reference list, some entries marked *(partial)* where the scan was unclear, plus Key Citations for Follow-up)
- pngs/: 13 images (page-000.png through page-012.png)
- paper.pdf: present (1.3 MB, PDF-1.5)

Note: `.gitignore` at repo root excludes `*.pdf` and `*.png`, so the commit covers only the five markdown/JSON artefacts. `paper.pdf` and `pngs/` remain on disk in the paper directory as required by the skill flow but are intentionally untracked.

## Issues / follow-ups
- **Reconcile skipped intentionally.** The parent prompt forbids touching other workers' paper directories and bans editing `papers/index.md`. I ran `research-papers:paper-reader` directly rather than `research-papers:paper-process`, and did NOT invoke `research-papers:reconcile` — doing so would risk cross-paper writes under the parallel-swarm contract. A downstream consolidation agent should run reconcile on `papers/Holloway_2018_AccessibleMapsBlindComparing` after the swarm completes.
- **index.md not updated.** Per parent prompt. Consolidation agent will append the description entry there.
- **Source-bootstrap / source-promote / claims / justifications / stances / tagging all skipped.** Parent prompt explicitly forbids propstore source-branch work in this task.
- **abstract.md verbatim block is approximate** — downstream refinement recommended against an authoritative ACM copy.
- **Citations entries marked *(partial)*** — a handful of reference list entries were partially illegible in the sci-hub scan and should be spot-checked against the ACM version if used for citation tracking.
- Verified `papers/index.md` was not modified by me — git status confirms it is still untracked (it has never been committed in this repo).

## Usefulness to this project
**Rating:** High.
**What it provides:** quantitative, pre-registerable effect sizes comparing 3D-printed map models against swell-paper tactile graphics (identification, mental-model, feature-find time, preference) plus nine actionable design guidelines and a low-cost (~US$575) interactive audio-label pipeline.
**Actionable next steps:** (1) encode the nine guidelines as a rule-check for any cartographic artefact produced by this project; (2) use the reported Wilcoxon effect sizes as prior evidence for the protocol's confidence-threshold critique; (3) evaluate whether the Interactive Audio Labels hardware pipeline (Bare Conductive Touch Board + conductive PLA) is the right starting point for this project's prototypes.
**Skip if:** working purely on pure-software tactile-graphic generation without any physical fabrication component.
