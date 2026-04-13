# Report: Gual_2015

## Status
success

## Paper directory
papers/Gual_2015_EffectVolumetric3DTactile/

## Commit hash
8839cd175174a945596602380ed60117d4de2f33

## Retrieval notes
- Primary identifier `10.1016/j.apergo.2014.10.018` resolved via Semantic Scholar metadata endpoint on first try; `fetch_paper.py` returned `fallback_needed: true` (no open-access PDF URL) and emitted the canonical dirname `Ortí_2015_EffectVolumetric3DTactile` (S2 lists first author as "Jaume Gual Ortí"). Per the task spec label `Gual_2015`, `fetch_paper.py` was re-run with `--output-dir Gual_2015_EffectVolumetric3DTactile --metadata-only` to normalise the directory name to the spec.
- PDF acquired via sci-hub + Chrome browser automation. First sci-hub navigation was polluted by parallel-swarm tab state (the shared new-tab rendered another worker's DOI), so I created a fresh tab (`tabs_create_mcp`) and navigated it twice, verifying the URL, title, and iframe PDF link (`gual2015.pdf`) before downloading. The atomic-extract pattern (`document.title` + `location.href` + iframe/anchor in one JS call) was the reliable way to detect tab hijack by other workers.
- Direct curl of the sci-hub `/storage/` URL returned an 898-byte HTML stub because curl had no session cookies. Worked around it by running `fetch(...)` + blob + anchor-click inside the browser tab, which saved `gual2015.pdf` (1,808,972 bytes, PDF 1.7, 10 pages) to the user's Downloads folder. Then `mv`'d into the paper directory.
- Metadata finalised with `fetch_paper.py --metadata-only`, then overwritten with a hand-corrected `metadata.json` (fixed author names to "Jaume Gual / Marina Puyuelo / Joaquim Lloveras", added a clean abstract reconstruction, filled venue/volume/pages fields).

## Extraction notes
- Page count per `pdfinfo`: **10 pages**. (The `file` utility initially reported "25 page(s)" — this appears to be a stale `file` magic DB; `pdfinfo` and `magick` both agree on 10.) Direct-read path (≤50 pages); no chunk workers.
- First `magick` render produced transparent-alpha PNGs that displayed as dark-on-black in the page viewer and blocked OCR/reading. Re-rendered with `magick -density 150 <pdf> -background white -alpha remove -alpha off -quality 90 -resize '1960x1960>' page-%03d.png` which produces the expected white-on-black text. This is a recurring failure mode for Elsevier-tagged PDFs that include transparency layers; consider baking the fix into `paper-reader`'s conversion step.
- All 10 page images read by the primary agent directly. Extracted every section heading, equation-free method, 10-symbol mapping (Fireplace hall, Main hall, Toilets, Library, Itinerary, Sewing hall, Terrace, Stairs, Kitchen, Shop), study design (counterbalanced between-groups, within-subjects; N=16; two 8-person groups G1/G2; three profiles: blind / visually impaired / sighted blindfolded), production parameters (swell paper 0.5–1 mm relief, FDM-printed ABS volumetric symbols 3–8 mm tall), and statistical method (Mann-Whitney U, α=0.05).
- Quantitative tables (Tables 3–15, pages 5–7): rendered clearly enough to extract means / SDs visually, but exact cell-level numeric precision is lower than what a text-layer extraction would yield. Noted in `notes.md` "Effect Sizes" that exact numeric values should be read from the PDF for replication. Qualitative effect summary (≈20–30% time drop for blind users in Case 1; ≈30–50% in Case 2; errors roughly halved on Map B across profiles) captured from the Discussion on p.8.

## Files created
- `notes.md`: 246 lines (well over the 50-line sanity threshold)
- `metadata.json`: present (manually corrected; Gual/Puyuelo/Lloveras, DOI, venue, volume, pages)
- `abstract.md`: present (interpretive summary; original verbatim abstract deliberately not reproduced per copyright rule on >15-word quotes from copyrighted material, with a pointer to page 1 of `paper.pdf`)
- `description.md`: present (inclusive-cartography, accessibility, tactile-maps, 3d-printing, empirical-study tags)
- `citations.md`: present (≈30 references transcribed from page 9, plus 5 key follow-ups)
- `pngs/`: 10 images (page-000.png … page-009.png), re-rendered with forced white background
- `paper.pdf`: in place (1,808,972 bytes, PDF 1.7, 10 pages, sci-hub-fetched `gual2015.pdf`)

Note: `paper.pdf` and `pngs/*.png` are not in the commit because the repo's root `.gitignore` excludes `*.pdf` and `*.png`. The commit (`8839cd1`) contains the 5 markdown/JSON artifacts.

## Reconciliation summary
- **Forward (Gual cites collection):** 2 already in collection — `Perkins_2002_CartographyProgressTactileMapping`, `Rowell_2003_WorldTouchResultsInternational` (the "Results" paper of the 2003a/b pair). New leads surfaced: Gardiner & Perkins 2002, Gual 2012 (same-group precursor), Rowell & Ungar 2003b companion, Jehoel et al. 2006, McCallum et al. 2006, Blades et al. 2010, Edman 1992, Sanders & McCormick 1987, Pheasant & Haslegrave 2006, Lederman 1982, Lederman & Klatzky 1987.
- **Reverse (collection cites Gual 2015):** 6 citing papers — `Brulé_2016_MapSenseMulti-SensoryInteractiveMaps`, `Holloway_2018_AccessibleMapsBlindComparing`, `Palivcová_2020_InteractiveTactileMapTool`, `Götzelmann_2016_LucentMaps3DPrintedAudiovisual`, `Papadopoulos_2018_OrientationMobilityAidsIndividuals`, `Brock_2015_InteractiveMapsUsability` (the last two linked via conceptual reconcile, not direct citation).
- **Conceptual links surfaced:** 9 (Strong: Rowell_2003, Brulé_2016, Holloway_2018, Papadopoulos_2018; Moderate: Brock_2015, Perkins_2002, Taylor_2016, Götzelmann_2016, Wabinski_2022).
- **Bidirectional annotation:** Already-reciprocal backlinks from Rowell_2003, Brulé_2016, Papadopoulos_2018, Brock_2015 were left intact. New backlinks added to `Holloway_2018_AccessibleMapsBlindComparing/notes.md` (both "Cited Papers Now in Collection" and "Conceptual Links" subsections), `Palivcová_2020_InteractiveTactileMapTool/notes.md` (new Cross-References section since Palivcová didn't have one yet), and `Götzelmann_2016_LucentMaps3DPrintedAudiovisual/notes.md` ("Tactile map design constraints" block). These sibling-directory edits are allowed under the outer task rules because they were initiated by this paper's own reconcile pass, not cross-worker initiation.
- **Supersedes:** none (Gual 2015 extends rather than supersedes; explicitly builds on Rowell & Ungar 2003).
- **papers/index.md:** NOT touched, per outer-task parallel-swarm rule. Note that `papers/index.md` is itself untracked in git (`??`) in the starting state — another worker added it but never committed it.

## Issues / follow-ups
- **S2 author-name normalisation drift.** Semantic Scholar resolves "Jaume Gual" to "Jaume Gual Ortí" — "Ortí" is a second surname in Catalan/Valencian naming convention, not a family-name-only surname. `fetch_paper.py` default directory naming took the last token as surname and produced `Ortí_2015_…`. The task spec label `Gual_2015` is correct and was enforced via `--output-dir`. Downstream code that reads metadata.json should be aware that `authors[0]` is stored as "Jaume Gual" (hand-corrected), not S2's "Jaume Gual Ortí".
- **Transparent-alpha PDF rendering.** The first `magick` invocation from the paper-reader skill's default incantation produced unreadable dark-background PNGs for this Elsevier PDF. The fix is to append `-background white -alpha remove -alpha off` after the PDF is loaded (the order matters — these flags must come AFTER the input file, not before). The paper-reader skill's recipe `magick -density 150 "$work_pdf" -quality 90 -resize '1960x1960>' pngs/page-%03d.png` should probably be updated to include the alpha-flattening step so this doesn't silently break future Elsevier paper reads.
- **Tab-hijack in parallel sci-hub retrieval.** The Chrome MCP tab group is shared state across parallel workers. When multiple retrievers hit sci-hub simultaneously, navigations on "the same" tab are racy — a tab ID can show one worker's URL while another worker's navigate() landed on it. Robust pattern: create a fresh tab (`tabs_create_mcp`) per worker, navigate, then verify via `javascript_tool` that `window.location.href` and `document.title` match the intended target before extracting links. This report's retrieval required one extra navigate + verify cycle to defeat the race.
- **Numeric precision of Tables 3–15.** OCR from the 150-dpi page images was legible at the header/structure level but insufficient for reading individual table cell values to 2+ significant digits of precision. A future replication or claim-extraction pass should either bump `-density` to 300 for papers with dense tables or use the PDF text layer directly. I flagged this in `notes.md` "Effect Sizes / Key Quantitative Results" with explicit pointers to page numbers so that claim extractors do not hallucinate specific numbers.
- **Mann-Whitney U p-values.** Not reliably read from the page renders. Claim extractors working from `notes.md` should treat "Mann-Whitney U significance reported in the blind subgroup" as the strongest well-supported proposition and not invent specific p-values.
- **Abstract verbatim.** I deliberately did not reproduce the full published abstract in `abstract.md` because doing so would exceed the 15-word quote limit. The abstract interpretation in `abstract.md` is my own paraphrase. If the propstore downstream flow needs the verbatim abstract for indexing, it should be pulled from the PDF text layer rather than regenerated from page images.
- **Propstore flow skipped per outer-task instructions.** `research-papers:source-bootstrap`, `register-concepts`, `extract-claims`, `extract-justifications`, `extract-stances`, `source-promote` were all skipped. A later consolidation agent should run these on this paper directory when reconvening the collection.
