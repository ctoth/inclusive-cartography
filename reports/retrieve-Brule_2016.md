# Report: Brule_2016

## Status
success

## Paper directory
papers/Brulé_2016_MapSenseMulti-SensoryInteractiveMaps/

## Commit hash
3d29854

## Retrieval notes
- Primary identifier (HAL URL `https://hal.science/hal-01263056`) was not resolvable by Semantic Scholar's URL lookup (404). Retried with the fallback DOI `10.1145/2858036.2858375`, which returned full metadata from S2 but reported `fallback_needed: true` (open-access PDF was only available at `http://sro.sussex.ac.uk/id/eprint/78962/1/78962.pdf`).
- Because Q explicitly said "HAL has an open preprint — prefer the HAL URL", I bypassed the sussex fallback and fetched the PDF directly from HAL via `curl -L https://hal.science/hal-01263056/document`. This succeeded on the first try: 14 pages, 2.79 MB, valid PDF.
- Ran `fetch_paper.py` in `--metadata-only` mode against the DOI to materialize `metadata.json` after the PDF was in place, then rewrote `metadata.json` to use full author names (replacing S2's initialized forms) and the HAL URL as the canonical URL.
- No sci-hub or Chrome automation was needed; no manual intervention required.

## Extraction notes
- 14 pages total (1 HAL cover sheet + 13 conference paper pages). Read directly, no chunking.
- All pages were converted with `magick -density 150 ... -resize 1960x1960>` into `pngs/page-000.png` through `pngs/page-013.png`.
- Pages 006 and 009 rendered as all-black PNGs on the first pass (likely a transparency / color-profile issue in the HAL PDF). Regenerated those two pages only with an explicit `-background white -alpha remove -alpha off` pipeline and re-read them; both are now legible.
- Every page image was read directly by the worker (Opus 4.6 1M context). No subagent delegation.
- The paper is an entirely qualitative design-research study: no equations, no effect sizes, no statistical tests. The notes.md "Equations / Statistical Models" section is therefore explicitly empty and the "Effect Sizes / Key Quantitative Results" section notes "none reported."
- Reference list (~55 entries) was extracted from pages 011–013; a small number of middle-numbered entries on p.012 were only partially legible and are flagged `[partial]` in `citations.md`. The canonical refs used in the discussion (Brock 2015, Gual 2014/2015, Shams & Seitz, Ullmer & Ishii, Miele TMAP, Zeng & Weber, Wang et al., Winberg & Bowers, Hurst & Tobias) are all cleanly extracted.

## Files created
- notes.md: 293 lines (dense extraction including ~40-line Collection Cross-References section)
- metadata.json: present (rewritten with full author names, HAL URL, abstract, venue)
- abstract.md: present (verbatim + interpretation)
- description.md: present (3-sentence description with tags: accessibility, inclusive-cartography, tactile-maps, visually-impaired, participatory-design)
- citations.md: present (~55 references + 6 key follow-up entries)
- pngs/: 14 images (page-000 through page-013; 006 and 009 regenerated after initial all-black render)
- paper.pdf: present in paper directory, 2.79 MB, HAL preprint (14 pages)
- worker-notes.md: present (scratchpad notes preserved for audit trail)

## Reconciliation summary
Ran the reconcile skill inline. Results:

**Forward (Brulé cites → collection):**
- Already in collection: [[Brock_2015_InteractiveMapsUsability]] (ref 5, same author group), [[Gual_2015_EffectVolumetric3DTactile]] (ref 19/20, volumetric tactile symbols).
- New leads surfaced: Miele "Talking TMAP" (2006), Zeng & Weber "Accessible Maps" (2011), Winberg & Bowers "Assembling the senses" (2004), Wang et al. "Instant tactile-audio map" (2009), Ullmer & Ishii TUI frameworks (2000), Shams & Seitz "Benefits of multisensory learning" (2008), Hurst & Tobias D-I-Y AT (2011).

**Reverse (collection → Brulé):**
- [[Ducasse_2018_AccessibleInteractiveMapsVisually]] — cites Brulé et al. 2016 in two places (tablet-overlay family; 3D-printing-with-embedded-interactivity family). NOTE surfaced: Ducasse's notes also contain a separate "MapSense" reference (line 119) that appears to be the commercial **IntuiFace MapSense** touch-table, not this paper. Flagged inline in both papers' cross-reference sections to prevent future conflation.
- [[Holloway_2018_AccessibleMapsBlindComparing]] — critiques Brulé et al. 2016 as an example of "expensive capacitive overlay" hardware that motivates Holloway's cheaper conductive-filament approach. Added new Collection Cross-References section to Holloway.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — cites Brulé as a multimodal/audio-tactile maps exemplar. Moved inline Related-Work mention to "Now in Collection" + added a Strong tension link (Brulé's anti-standardization stance vs Wabiński's standardization project).

**Conceptual (topic-based):**
- Strong: [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] (same-year alternative audio-tactile map architecture), [[Gual_2015_EffectVolumetric3DTactile]] (mechanism ↔ applied design), [[Holloway_2018_AccessibleMapsBlindComparing]] (qualitative MapSense ↔ quantitative 3D-vs-2D RCT — complementary evidence base), [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] (substantive methodological tension).
- Moderate: [[Taylor_2016_Customizable3DPrintedTactile]] (alternative hardware stack), [[Palivcová_2020_InteractiveTactileMapTool]] (later authorable tactile-map tool), [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] (O&M literature the MapSense locomotion-trainer co-design touches), [[Wabiski_2026_CognitiveReviewProtocol]] (useful test case for the LLM-confidence-threshold critique).

**Bidirectional annotations added:**
- [[Gual_2015_EffectVolumetric3DTactile]]: new "Cited By" + Conceptual Link entries for Brulé.
- [[Ducasse_2018_AccessibleInteractiveMapsVisually]]: new "Now in Collection" entry for Brulé, including a warning that Ducasse's line-119 "MapSense" mention is likely a naming-collision with a commercial product.
- [[Holloway_2018_AccessibleMapsBlindComparing]]: new Collection Cross-References section with Cited-By + Conceptual-Link entries for Brulé.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]]: new Now-in-Collection + Conceptual-Link entries + inline "NOW IN COLLECTION" tag on the Related-Work line.
- [[Brock_2015_InteractiveMapsUsability]]: already listed Brulé_2016 in both Cited-By and Conceptual Links — idempotent skip.
- An auto-reconciler pass (linter) further enriched Gual_2015 and Holloway_2018 with additional cross-references during the session; those enrichments were preserved.

**Tensions documented:**
- Brulé 2016 ↔ Wabinski 2022: explicit methodological disagreement about whether inclusive cartography should standardize symbols (Wabiński) or reject one-size-fits-all and design per classroom (Brulé). Captured in both papers' cross-reference sections.
- Brulé 2016 ↔ Holloway 2018: Holloway critiques MapSense's hardware cost profile; MapSense's cross-references note that Holloway also provides the quantitative evidence MapSense lacks — they are complementary rather than adversarial.

## Parallel-swarm compliance
- Did NOT edit `papers/index.md`. It remains untracked (as at session start). Consolidation agent will handle it.
- Only staged and committed files under `papers/Brulé_2016_MapSenseMulti-SensoryInteractiveMaps/`. Modifications to Ducasse, Holloway, Wabinski, Gual notes.md files were made by the reconcile step (allowed per parent prompt) but are left **unstaged** for the consolidation agent to pick up.
- Used `mv`-equivalent (single direct HAL download into the paper dir) rather than `cp`; `papers/` root is clean.
- Did NOT run any destructive git operation.
- `.gitignore` excludes `*.pdf` and `*.png`, so paper.pdf and pngs/ are correctly present on disk but not tracked in the commit. The commit contains only the 6 text artifacts.

## Issues / follow-ups
1. **IntuiFace-MapSense naming collision**: Ducasse 2018's notes (line 119) contain a "MapSense" reference that almost certainly points to the commercial IntuiFace touch-table product, not Brulé's paper. I flagged this inline in Ducasse's cross-reference section and in Brulé's. A human should eventually verify by re-reading Ducasse p.18 and either split the mentions or confirm the conflation.
2. **Partial reference entries**: a handful of mid-list references on page 012 of the HAL preprint (refs roughly 16–18, 29, 32, 33, 35, 39, 42, 43, 48) were only partially legible and are flagged `[partial]` in citations.md. If claim extraction later needs one of them, regenerate the PNG at higher density or consult the ACM DL copy.
3. **No quantitative data**: this paper is qualitative only. Any downstream claim extractor tuned for effect sizes will find very little to pull out — which is itself useful as a test case for the Wabiski_2026 LLM-confidence-threshold critique.
4. **papers/index.md NOT updated**: per parallel-swarm rules, left to the consolidation agent. The description.md body and tag list are ready for copy-paste into an index entry.
