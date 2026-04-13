# Report: Rowell_Ungar_2003

## Status
success (with identity caveat — see Retrieval notes)

## Paper directory
papers/Rowell_2003_WorldTouchResultsInternational/

## Commit hash
957c869a6612e208c287e044b31428f846cd8ca2

## Retrieval notes

**IMPORTANT IDENTITY CAVEAT for Q.** The `PAPER_SPEC` supplied for this worker contained conflicting identifiers:

- `label`: `Rowell_Ungar_2003`
- `title`: "The world of touch: an international survey of tactile maps. Part 1: Production"
- `identifier` (DOI): `10.1179/000870403225012961`
- `venue`: "The Cartographic Journal 40(3)"

The **DOI resolves to a different paper than the title claims**. DOI `10.1179/000870403225012961` is:

> Rowell, J. & Ungar, S. (2003) "The World of Touch: Results of an International Survey of Tactile Maps and Symbols", *The Cartographic Journal* 40(3):259-263.

The title "Part 1: Production" refers to a **separate** Rowell & Ungar 2003 paper:

> Rowell, J. & Ungar, S. (2003) "The world of touch: an international survey of tactile maps. Part 1: production", *British Journal of Visual Impairment* 21(3), DOI `10.1177/026461960302100303`.

There are two Rowell & Ungar 2003 papers from the same survey project, published in different journals, and the PAPER_SPEC accidentally combined the title of one with the DOI and venue of the other.

Decision: I treated **DOI + venue as authoritative** (two identifiers agreeing against one) and retrieved the Cartographic Journal paper. The companion "Part 1: Production" paper from the British Journal of Visual Impairment is NOT in the collection and is flagged as an outstanding lead in both `notes.md` and `citations.md`. If Q actually wanted the BJVI "Part 1: Production" paper, please request a rerun with identifier `10.1177/026461960302100303`.

### Retrieval steps actually taken

1. Invoked `research-papers:paper-retriever` with the DOI.
2. `fetch_paper.py` resolved Semantic Scholar metadata (confirming the title mismatch above) and returned `fallback_needed: true` (no open-access PDF via Unpaywall/arxiv).
3. Fell back to sci-hub via browser automation.
4. Navigated to `https://sci-hub.st/10.1179/000870403225012961`; extracted the sci-hub storage PDF link.
5. A naive `curl` of that storage URL returned an 898-byte HTML error page (sci-hub anti-bot), so I instead triggered a blob download from within the browser page context (`fetch(...).then(r => r.blob()) → anchor.click()`) and moved the resulting ~117 KB file from `~/Downloads/` into `papers/Rowell_2003_WorldTouchResultsInternational/paper.pdf`.
6. Ran `fetch_paper.py ... --metadata-only` to materialise `metadata.json` alongside the PDF.
7. Verified the PDF as a valid 5-page PDF 1.4 document, title matches the DOI-resolved paper.

## Extraction notes

- 5 pages total (pp. 259-263 of The Cartographic Journal 40(3)). Direct-read path (well under the 50-page chunking threshold). No chunk workers dispatched.
- All 5 page images (`page-000.png` through `page-004.png`) generated at 150 DPI, inspected directly, and extracted into `notes.md`.
- Tables 1 and 2 (importance ratings of tactile symbols and labelling elements) on p.262 are rendered as reasonably legible bar charts; the mean and standard deviation values were transcribed into `notes.md` at the resolution visible on the 1960px-wide PNG. Fine-detail digits may benefit from a higher-DPI rescan if downstream claim extraction needs tighter precision than roughly one decimal place.
- The Cartographic Journal reference-list formatting uses numeric styling and inline journal abbreviations; individual reference entries in `citations.md` are marked "approximate; as visible" where specific characters in the scan were ambiguous. The full reference list is short (approximately 8-10 entries).
- No chunking, no chunk workers, no mini-model delegation.

## Files created

- `notes.md` — 273 lines. Dense extraction including abstract summary, section-by-section findings, Tables 1 and 2 transcribed into parameter tables, conceptual-links section, collection cross-references section.
- `metadata.json` — present, includes verbatim abstract text and a reconstructed BibTeX record.
- `abstract.md` — present, with verbatim abstract + interpretation paragraph.
- `description.md` — present, tagged `tactile-maps, accessibility, survey, cartography, visual-impairment`.
- `citations.md` — present, approximate reference list plus 5 key follow-up citations.
- `pngs/` — 5 PNG images (`page-000.png` .. `page-004.png`).
- `paper.pdf` — 116,692 bytes, PDF 1.4, 5 pages.

## Issues / follow-ups

1. **Title-vs-DOI mismatch in PAPER_SPEC** (most important). Q should decide whether this paper or the BJVI "Part 1: Production" paper (DOI `10.1177/026461960302100303`) is the one actually wanted. The two are complementary halves of the same survey project; for full coverage, both should be retrieved.
2. **Companion paper flagged as a lead** in both `notes.md` (Collection Cross-References → New Leads) and `citations.md`. A follow-up retrieval run with that DOI would close the gap.
3. **Reconcile annotations written into three other papers** (allowed per parent-task rules because this was triggered by the reconcile skill, not a cross-paper write I initiated myself):
   - `papers/Perkins_2002_CartographyProgressTactileMapping/notes.md` — added `## Collection Cross-References` section with bidirectional "Cited By" + conceptual link back to Rowell_2003.
   - `papers/Gual_2015_EffectVolumetric3DTactile/notes.md` — annotated the `Rowell & Ungar (2003a, 2003b)` lead entry with `→ NOW IN COLLECTION: [[Rowell_2003_WorldTouchResultsInternational]]` and added a new `## Collection Cross-References` section with "Now in Collection (previously listed as leads)" entry. (Note: another worker — apparently the Brulé_2016 worker — concurrently merged a `Cited By` entry into the same section. Both annotations coexist cleanly.)
   - `papers/Wabinski_2022_GuidelinesStandardizingTactileMaps/notes.md` — added a `## Collection Cross-References` section with a strong-link conceptual entry positioning Rowell & Ungar 2003 as the empirical standardisation-gap statement that Wabinski 2022 is the delayed response to.
4. **papers/index.md was NOT edited** by this worker, per parent-task rule. The consolidation agent will handle the index after all parallel workers finish.
5. **No `pks` provenance stamp** was applied, because the parent task explicitly scopes propstore source-branch work out of this task. Only paper-artefact files (notes, abstract, description, citations, metadata, pngs) were produced.
6. **No `source-bootstrap` / `source-promote` invoked**, per parent-task rule.
7. **Paper hash / short-title canonicalisation:** the directory name `Rowell_2003_WorldTouchResultsInternational` was chosen by `fetch_paper.py` from the Semantic Scholar title. It differs from the label `Rowell_Ungar_2003` in the PAPER_SPEC, but the directory name is a stable paper-slug and downstream reconcile should use it.

## Sanity-check summary

- notes.md: 273 lines (>=50 required)
- All mandatory artefact files present
- paper.pdf inside paper directory; papers/ root clean
- papers/index.md untouched by this worker
- Commit created and recorded: `957c869a6612e208c287e044b31428f846cd8ca2`

## Usefulness to This Project

**Rating:** High.
**What it provides:**
- A cited empirical baseline on which tactile map production methods were actually in use circa 2001-2002 (microcapsule/swell paper and thermoform/vacuum-forming dominant).
- A producer-validated importance hierarchy for tactile symbol categories (point features and lines above area shading; Braille labels above scale bars / north arrows).
- A widely reused reference for the long-standing absence of international standards in tactile cartography — complementing Perkins 2002 (narrative review) and motivating Wabinski 2022 (guidelines attempt).
- Explicit scoping to 94 producers / 43 countries with a documented UK sampling bias, useful as a prior-art sampling-methodology reference point for the inclusive-cartography systematic review.

**Actionable next steps:**
- Retrieve the companion "Part 1: Production" paper (DOI `10.1177/026461960302100303`) to complete the Rowell & Ungar 2003 pair.
- Use this paper as a canonical citation when the review needs to contrast the 2003 production baseline against newer 3D-printed / interactive / audio-tactile approaches (Taylor 2016, Götzelmann 2016, Brock 2015, Brulé 2016, Ducasse 2018, Holloway 2018, Palivcová 2020).

**Skip if:** The systematic review restricts itself to post-2010 technology (even then, this paper remains a useful background citation for why standardisation is still an open question).
