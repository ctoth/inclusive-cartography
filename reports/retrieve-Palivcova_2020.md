# Report: Palivcova_2020

## Status
success

## Paper directory
papers/Palivcová_2020_InteractiveTactileMapTool/

## Commit hash
d93fe95

## Retrieval notes
- Primary identifier `10.1145/3334480.3382912` (ACM DL DOI) resolved metadata via Semantic Scholar on the first try; PDF direct download was blocked (ACM paywall → `fallback_needed: true`).
- Fell back to sci-hub via the claude-in-chrome MCP browser.
  - `https://sci-hub.st/10.1145/3334480.3382912` returned a page with a direct link to `https://sci-hub.st/storage/moscow/8638/d0e3f54fb24e0c956199f2c69690ec01/10.1145@3334480.3382912.pdf`.
  - Direct `curl` of that URL hit DDoS-Guard (898-byte HTML challenge), so the PDF was fetched through the authenticated Chrome session with `fetch(..., {credentials: 'include'})`, then delivered to the local filesystem via a Blob/anchor click → `Downloads/Palivcova_2020_paper.pdf`, then moved into the paper directory.
  - Resulting file is 2,583,496 bytes, `PDF document, version 1.6 (zip deflate encoded)`.
- Metadata file was rematerialized via `fetch_paper.py --metadata-only` after the PDF was in place, then hand-extended to include full accented author names ("Miroslav Macík", "Zdeněk Míkovec") and an `arxiv_id: null` field.
- Author-name correction: the inline PAPER_SPEC listed the first author as "Daniela Palivcova"; the PDF title page gives "Dominika Palivcová" (Czech Technical University in Prague). I trusted the PDF per project principles and used the correct first name. The directory name uses the accented form `Palivcová_2020_InteractiveTactileMapTool`.

## Extraction notes
- 9 pages (well under the 50-page chunking threshold), read directly as page images (no chunk subagents).
- Working model: Claude Opus 4.6 1M-context (this subagent, reading images itself — no delegation).
- All 9 page PNGs were inspected by the reader before any writes.
- Page 1-6: paper body (abstract, introduction, use-case, prototype iterations, evaluation, discussion, conclusion).
- Page 6-9: references list [1]–[37]. The two-column Late-Breaking Work layout with small fonts made a small number of middle-range entries (around refs [6], [21]–[27]) partially hard to resolve from the image; those are explicitly flagged with `[…]` / "verify from PDF" markers in `citations.md` so downstream propstore ingestion will re-check instead of silently accepting noise.
- The paper reports no inferential statistics, no confidence intervals, no p-values — it is a qualitative formative study with N=10. The `Effect Sizes / Key Quantitative Results` section in notes.md contains only demographic summary statistics, flagged as such.
- Per-participant demographic Table 1 was reproduced in full, including the cryptic abbreviations used in Table 2 (RD = retinal detachment, MY = myopia, BL = blind, etc.). Some Table 2 codes are approximations because the abbreviation column was compressed; this is noted in notes.md.

## Files created
- notes.md: 255 lines
- metadata.json: present (rewritten with accented full author names, DOI, ACM venue, BibTeX)
- abstract.md: present (verbatim abstract + interpretation)
- description.md: present (tags: tactile-maps, accessibility, older-adults, indoor-navigation, user-study)
- citations.md: present (37 reference entries, with uncertain ones flagged)
- pngs/: 9 images (page-000.png through page-008.png, gitignored via `*.png`)
- paper.pdf: present (2.58 MB, gitignored via `*.pdf`)

## Skipped steps (per outer prompt scope)
The top-level prompt says: "Do NOT invoke `research-papers:source-bootstrap` or `source-promote` — propstore source-branch work is out of scope." It also says "You MUST NOT edit `papers/index.md`" and "You MUST NOT touch any other worker's paper directory." Accordingly I did **not** run:
- `research-papers:source-bootstrap`
- `research-papers:register-concepts`
- `research-papers:extract-claims`
- `research-papers:extract-justifications`
- `research-papers:extract-stances`
- `research-papers:source-promote`
- `pks build`
- `research-papers:reconcile` (cross-paper writes)
- `pks source stamp-provenance` (mutates a source branch)
- Updating `papers/index.md` (explicit prohibition)

Paper-reader Steps 7, 8, 9 (reconcile, index update, provenance stamp) are therefore deferred to the consolidation agent.

## Issues / follow-ups
- **Author first name correction**: spec label `Palivcova_2020` with first name "Daniela" is wrong. PDF title page gives "Dominika Palivcová". metadata.json uses the correct form. Downstream indexers should use `Palivcová_2020_InteractiveTactileMapTool` as the directory and "Dominika Palivcová" as the first author. The report filename (`retrieve-Palivcova_2020.md`) still follows the spec's plain-ASCII label per instructions.
- **Partial references**: citations.md flags refs `[6]` and `[21]–[27]` (approximately) as needing a PDF re-read because the LBW two-column layout made them hard to resolve from page images. The high-confidence references are fully captured.
- **No statistical rigor**: the paper contains no inferential statistics, only a demographic mean/SD. Any automated LLM-confidence scorer that weighs statistical rigor should flag this paper as formative/small-N, not reject it — that is actually the protocol-critique point this paper is being collected for, per the outer prompt.
- **Reconcile not run**: this paper has meaningful cross-references to other workers' papers (Taylor_2016, Holloway_2018, Götzelmann_2016, Gual_2015, Brock_2015, Perkins_2002, Wabinski_2022) — all visible in the parallel worker list. The consolidation agent should run reconcile across the batch to wire up forward/backward citations.
- **Provenance stamp deferred**: the paper-reader skill normally stamps notes.md with `pks source stamp-provenance`, but that mutates a propstore source branch, which the outer prompt forbade. Consolidation agent should stamp as part of its source-bootstrap → promote pass.
- **Gitignore of PDFs and PNGs**: the project's `.gitignore` contains `*.pdf` and `*.png`, so `paper.pdf` and `pngs/*.png` are present on disk but intentionally not committed. The commit contains only the 5 markdown/JSON artifacts.
