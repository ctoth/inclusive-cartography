# Report: Ducasse_2018

## Status
success

## Paper directory
papers/Ducasse_2018_AccessibleInteractiveMapsVisually/

## Commit hash
422fa78d61c17bc44c645f08b52098bf18c0cea3

## Retrieval notes
Primary identifier `https://arxiv.org/abs/2208.14685` worked on the first try via `scripts/fetch_paper.py`. No retries, no fallback needed, no sci-hub. arXiv metadata returned Ducasse / Brock / Jouffrais with the exact intended title "Accessible Interactive Maps for Visually Impaired Users", which matches the PAPER_SPEC. The arXiv upload date is 2022 (v1), but the DOI 10.1007/978-3-319-54446-5_17 and the paper's own header ("To appear in 'Mobility in Visually Impaired People - Fundamentals and ICT Assistive Technologies', Pissaloux & Velazquez Eds., Springer") confirm this is the 2018 Springer book chapter. I overrode the retriever's `dirname`/`year=2022` and renamed the directory to `Ducasse_2018_AccessibleInteractiveMapsVisually` and fixed `metadata.json` year to "2018" plus the Springer venue, matching Q's label exactly.

## Extraction notes
- 45 pages, single PDF from arXiv preprint, 1.35 MB, PDF 1.4.
- Under the 50-page threshold, so read directly without chunk workers, per `paper-reader` Step 2A.
- Inspected `pngs/page-000.png` first to prove the page-image lane, then read all 45 pages sequentially. No sub-agent dispatch.
- No formal equations or statistical models in the chapter (it is a narrative review with taxonomy and comparisons). Notes captures the DIM/HIM taxonomy, sub-family named prototypes, reviewed empirical findings, testable properties, parameter tables for tactile-map production media and pin-array shape displays, and an exhaustive related-work trail.
- The `reconcile` process (run by another worker in the parallel swarm, not by me) had already appended a "Collection Cross-References" section at the bottom of `notes.md` linking Papadopoulos_2018 and Brulé_2016. I preserved that block and appended my worker checkpoint after it.
- `papers/index.md` is untracked upstream; I did not modify it per parallel-swarm rules — the consolidation agent will handle it.

## Files created
- notes.md: 367 lines
- metadata.json: present
- abstract.md: present
- description.md: present
- citations.md: present
- pngs/: 45 images
- paper.pdf: present in paper directory (not at papers/ root)

## Issues / follow-ups
- Year mismatch between arXiv (2022 v1 upload) and true publication year (2018 Springer chapter). I resolved this in favour of the PAPER_SPEC (2018) by renaming the directory and editing metadata.json. The arxiv_id 2208.14685 is preserved in metadata.json for provenance.
- `paper.pdf` and `pngs/` are not in the git commit because the repository `.gitignore` excludes them (working tree was clean after `git add papers/Ducasse_2018_AccessibleInteractiveMapsVisually/`). Only the five text artefacts (notes.md, metadata.json, abstract.md, description.md, citations.md) were committed. This matches the convention observed in the rest of this collection.
- Effect sizes for the Brock et al. 2015 one-week retention comparison and for Giudice et al. 2012 are cited narratively in the chapter but not given as numbers — anyone needing exact effect sizes must read the primary papers (flagged in `notes.md` Open Questions and Related Work sections).
- No provenance stamp was run — propstore source-branch work (`source-bootstrap`, `stamp-provenance`, etc.) is explicitly out of scope for the inclusive-cartography retrieve-and-process-paper task per `prompts/retrieve-and-process-paper.md`.
