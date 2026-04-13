# Report: Wabinski_2022

## Status
success

## Paper directory
papers/Wabinski_2022_GuidelinesStandardizingTactileMaps/

## Commit hash
9736d5d

## Retrieval notes
- Primary identifier (HAL URL `https://hal.science/hal-03763057`) is a weak landing-page URL. Normalized to DOI `10.1080/00087041.2022.2097760` via Semantic Scholar and used that as the strong identity-preserving input.
- `fetch_paper.py` resolved metadata cleanly against Semantic Scholar but the Tandfonline direct-PDF URL returned HTTP 403 (paywalled).
- Per Q's explicit instruction ("HAL has an open preprint — prefer the HAL URL"), bypassed sci-hub fallback and extracted the open-access preview link from the HAL landing page HTML: `https://hal.science/hal-03763057v1/file/00087041.2022.pdf` (3.4 MB, 22-page PDF v1.4). Curl'd it directly into the paper directory.
- Materialized `metadata.json` via `fetch_paper.py --metadata-only`.
- Distinct ASCII directory name `Wabinski_2022_GuidelinesStandardizingTactileMaps` chosen to avoid (a) auto-generated non-ASCII dirname `Wabiński_...` and (b) any visual confusion with the existing `Wabiski_2026_CognitiveReviewProtocol` directory, per Q's warning that the same author's 2026 review protocol already lives in the collection and must not be overwritten.

## Extraction notes
- 22 pages. Under the 50-page threshold, read end-to-end in a single pass — no chunking, no subagents dispatched.
- Initial ImageMagick PNG render (`magick -density 150`) produced transparent black backgrounds on several pages (12-17, 18, 20, 21), making text invisible. Re-rendered those pages with `-density 200 -background white -alpha remove -alpha off` which produced legible white-background PNGs. All 22 page images are now readable.
- Reader: claude-opus-4-6[1m] (this worker), no delegation. Paper is in standard two-column journal format; tables (Tables 2-4 on p.12) and Appendix A (pp.18-20) were the highest-value structural content and were fully transcribed.
- Parameter tables 2-4 contain roughly 50 numerical parameters (dimensions in mm, distances in mm, relief heights in mm) drawn from ~15 sources. All extracted into `notes.md` with per-row page citations.
- One equation extracted: the Töpfer-Pillewizer map-reduction rule `n_f = n_o * sqrt(M_o/M_f)` applied to tactile generalization (p.11).
- Appendix A symbol catalogue transcribed as prose because the glyphs are figures — page references preserved for every category.
- Provenance stamped on notes.md via `pks source stamp-provenance` with agent `claude-opus-4-6[1m]` and skill `paper-reader`.

## Files created
- notes.md: 332 lines
- metadata.json: present
- abstract.md: present
- description.md: present
- citations.md: present (full reference list + 9 key-follow-up entries)
- pngs/: 22 images
- paper.pdf: present (3.4 MB, HAL v1 preprint). Note: `*.pdf` and `*.png` are in `.gitignore`, so paper.pdf and pngs/ are on disk but intentionally not tracked in git per the project's existing convention.

## Cross-references established (reconcile)
Direct citations from Wabinski_2022 already in the collection (added to "Already in Collection" in its notes.md):
- Rowell_2003_WorldTouchResultsInternational
- Perkins_2002_CartographyProgressTactileMapping
- Gual_2015_EffectVolumetric3DTactile
- Holloway_2018_AccessibleMapsBlindComparing
- Taylor_2016_Customizable3DPrintedTactile

"Now in Collection (previously listed as leads)" preserved (written by a prior parallel worker):
- Brulé_2016_MapSenseMulti-SensoryInteractiveMaps

Cited-by (in collection):
- Wabiski_2026_CognitiveReviewProtocol (same lead author; the 2026 systematic-review protocol directly builds on the 2022 narrative review)

Backward annotations added to cited papers (forced reciprocal "Cited By" entries):
- papers/Perkins_2002_CartographyProgressTactileMapping/notes.md
- papers/Holloway_2018_AccessibleMapsBlindComparing/notes.md
- papers/Taylor_2016_Customizable3DPrintedTactile/notes.md
- papers/Wabiski_2026_CognitiveReviewProtocol/notes.md

Rowell_2003 and Gual_2015 already contained a Wabinski_2022 reference from prior reconcile passes — left unchanged (idempotent).

Conceptual links and tensions documented in notes.md:
- Strong: Brock_2015, Ducasse_2018, Wabiski_2026
- Moderate: Götzelmann_2016, Palivcová_2020, Papadopoulos_2018
- Two tensions identified: regional-vs-global standardization (Brulé vs Wabinski) and symbol-level-vs-artifact-level design (Brock/Ducasse vs Wabinski).

## Issues / follow-ups
- `papers/index.md` is currently *untracked* (not yet committed to git). I deliberately did not touch it, per the parent prompt's rule that a consolidation agent will maintain the index. When that agent runs it will need to add a Wabinski_2022 entry whose tags match the description.md frontmatter: `tactile-maps, accessibility, inclusive-cartography, design-guidelines, review`.
- The Wabiski_2026 directory was also previously untracked — my commit is the first to land it in git because I appended a backward-annotation "Collection Cross-References" section to its notes.md. If a parallel worker is also trying to commit Wabiski_2026 for the first time, there may be a merge conflict; recommend the consolidation agent resolve by taking the union of both notes.md edits.
- `paper.pdf` and `pngs/*.png` live on disk but are gitignored — this is the project convention. Downstream tools that need the PDF or page images should read them from the working tree, not from git.
- Several other papers' notes.md files are currently modified in the working tree by parallel workers (Ducasse_2018, Palivcová_2020, Brulé_2016/worker-notes.md); I did not stage those changes since they are not my edits and not part of my paper scope.
- No PRISMA-style systematic review methodology was claimed by the paper; it is explicitly narrative, which matters for any downstream claim extraction that weights "systematic review" higher than "narrative review."
- The paper predates and motivates the 2026 Wabinski cognitive-review protocol in the collection; this supports the project's use of this paper as a seed for §3.3 "Seed selection & scoping."

## Usefulness to this project
**Rating: High.**
This paper is the collection's single best source of measurable tactile-map design invariants (Tables 2-4 on p.12), a ready-to-use recommended-symbol catalogue (Appendix A on pp.18-20), the sqrt(M_o/M_f) generalization rule (p.11), and a clean statement of the three open problems — no global standard, production-method sensitivity, multimodal encoding — that the 2026 Wabinski review protocol operationalizes. Any automated tactile-map generator the project builds should encode these parameters as hard invariants and use Appendix A as a starting symbol library.
