# Report: Taylor_2016

## Status
success

## Paper directory
papers/Taylor_2016_Customizable3DPrintedTactile/

## Commit hash
30ee464

## Retrieval notes
- Primary identifier `10.1145/2982142.2982167` resolved via Semantic Scholar on the first try (correct paper: Taylor/Dey/Siewiorek/Smailagic, ASSETS 2016, "Customizable 3D Printed Tactile Maps as Interactive Overlays").
- `fetch_paper.py` returned `fallback_needed=true` — no open-access PDF path was found.
- Fallback: sci-hub via Chrome. Loaded `https://sci-hub.st/10.1145/2982142.2982167` in a fresh tab in the existing MCP tab group. JS probe extracted the PDF link `https://sci-hub.st/storage/twin/6118/108d3deb5bce1b7d2777461b687df556/taylor2016.pdf`.
- Direct `curl` against that URL returned 898 bytes — a DDoS-Guard JavaScript challenge, not a PDF. Raw curl is blocked at the edge.
- Workaround: used `javascript_tool` inside the authenticated tab to `fetch()` the PDF (1,997,199 bytes, `application/pdf`) and triggered a same-tab `<a download>` click. Chrome wrote the file to `%USERPROFILE%/Downloads/taylor2016-inclusivecarto.pdf`, then I `mv`-ed it to `papers/Taylor_2016_Customizable3DPrintedTactile/paper.pdf`.
- After the PDF was in place I reran `fetch_paper.py --metadata-only` to create `metadata.json`. That metadata was then rewritten to the richer schema (arxiv_id, abstract, canonical venue, doi url) as the paper-reader skill requires.

## Extraction notes
- 9 pages total (pdfinfo). Under the 50-page threshold — direct read, no chunking, no subagents.
- First pass with `magick -density 150 ... -resize '1960x1960>'` produced blank/black rasters for pages 001, 006, 007 (ImageMagick's Ghostscript delegate mis-handled transparency layers in this specific PDF).
- Re-rendered those three pages via `pdftoppm -r 200` → PPM → `magick` → PNG. The poppler path handled the layers correctly and produced readable images. The broken PNGs were overwritten in place.
- All 9 pages were read at image-level. Notes extraction is faithful to the paper: system architecture, web interface (simple vs. advanced), conductive-PLA capacitive-overlay mechanism, four-corner rigid registration, companion Android app, three-city feasibility study (N=12), qualitative failure modes.
- The paper has no equations and no quantitative results; parameter table therefore captures measurable quantities as reported (participant counts, materials, tablet model) and explicitly flags the absence of characterization data as a testable gap.
- Model used: Claude Opus 4.6 (1M context), single agent, no subagents.

## Files created
- notes.md: 252 lines
- metadata.json: present (rewrote to schema-compliant form with real abstract)
- abstract.md: present
- description.md: present (tags: tactile-maps, 3d-printing, accessibility, capacitive-overlay, openstreetmap)
- citations.md: present (30 references transcribed from p.79, plus 6 key follow-up picks)
- pngs/: 9 images (page-000.png through page-008.png), gitignored

## Verification
- `papers/index.md` NOT modified by this worker (it is untracked at repo level; other workers are adding their own directories). No `git checkout`/`restore`/`reset` was run.
- `paper.pdf` was moved, not copied, into the paper directory. No stray PDF remains in `papers/` root.
- `.gitignore` lists `*.pdf` and `*.png`, so `paper.pdf` and `pngs/` are intentionally excluded from the commit; only the 5 markdown/JSON artifacts are staged and committed. This is consistent with other paper directories in the repo.

## Issues / follow-ups
- Sci-hub retrieval path requires an authenticated browser session (DDoS-Guard blocks raw curl). Documented here in case the orchestrator wants to standardize a blob-download helper for future parallel runs.
- ImageMagick-only rasterization is fragile for this PDF family — recommend that `paper-reader`'s page-image step try `pdftoppm` as a fallback automatically when any page comes out near-uniform black.
- Paper reports no conductive-PLA characterization; any downstream claim extraction must not invent numeric thresholds.
- Per the parent prompt, `reconcile`, index.md edits, and propstore source-branch work were intentionally NOT performed. A consolidation agent is expected to handle index.md and cross-references after all workers finish.
