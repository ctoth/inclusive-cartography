# Worker notes: Brule_2016 retrieval

## GOAL
Retrieve and process MapSense (Brule 2016, CHI) via paper-process pipeline per prompts/retrieve-and-process-paper.md.

## DONE
- Retrieved PDF from HAL direct (https://hal.science/hal-01263056/document), 14 pages, 2.79 MB
- fetch_paper.py materialized metadata.json via DOI 10.1145/2858036.2858375
- Converted to 14 page PNGs via magick
- Confirmed page-000.png readable (HAL cover sheet visible)

## FILES
- papers/Brulé_2016_MapSenseMulti-SensoryInteractiveMaps/paper.pdf (target of work)
- papers/Brulé_2016_MapSenseMulti-SensoryInteractiveMaps/metadata.json (present)
- papers/Brulé_2016_MapSenseMulti-SensoryInteractiveMaps/pngs/page-000..013.png

## OBSERVED so far (pages 000-013 attempted)
- p0: HAL cover sheet
- p1: Title, authors (LTCI/CNRS Telecom ParisTech; Paris-Saclay; INRIA Bordeaux/IA Toulouse/U Toulouse), Abstract, Intro. "MapSense: raised paper figurative map augmented by 3D printed objects + conductive ink; accessed through tablet. Fig 1 shows child exploring map." Target: visually impaired (VI) children. Prior work: raised-line maps, digital accessible maps, visual maps on tablets.
- p2: Fig 2 (Mappie overlay on tablet + 3D objects), Fig 3 (MapSense Europe with audio cues). Related Work — assistive tech for VI; raised paper maps (Edman, Rowell); digital tactile interactive (Wang, Zeng); interactive maps with tablets (Brock TactiPad); TTT Talking Tactile Tablet; Google maps Via tangible Go Maps Accessible; Miele's Braille text. Mentions NOMAD, Talking Tactile Tablet, IVEO, Braille text, and mobile tactile maps with audio feedback.
- p3: Fig 4 (Left Proba 3 SciGlobe tactile 3D printed globe; Right Proba 3 SoundBox audio recorder tangible). Design goals; Involving children in the design process; Involving older children + teacher needs + concerns.
- p4: Table 1 Interviews (15 caretakers/teachers). Findings — children's uses of tactile technologies; role of caretakers/teachers.
- p5: Table 2 Description of 13 caretakers interviewed. Children's needs in the classroom.
- p6: (was black — regenerated) — content on this page
- p7: Fig 6 Left Map of French region cultural points of interest; Right Map of itinerary of class trip. Fig 7 MapSense Do-It-Yourself supplies. Eval/tests with prototypes + interactive tables. MAPSENSE SECOND ITERATIVE RAP PROTOTYPE.
- p8: Follow-up with 13 more children + tests with tangibles. Tangibles design (4 shapes) learning + feedback. Evaluation, design process, methodology. Six tangible objects.
- p9: (was black — regenerated) — content on this page
- p10: Children (several tables), limitations + ethnographic findings; section on design recommendations; CONCLUSION; ACK
- p11: REFERENCES begin
- p12: References continue
- p13: References continue (50-55)

## NEW BLOCKER SOLVED
Pages 006 and 009 rendered black first pass. Re-rendered with `-background white -alpha remove -alpha off`. Need to read them now.

## NEXT
- [x] Read regenerated pages 006 and 009
- [x] Write notes.md (dense, ~200 lines)
- [x] Update metadata.json with full author names + HAL url + abstract
- [ ] Write description.md
- [ ] Write abstract.md
- [ ] Write citations.md
- [ ] Reconcile
- [ ] Stamp provenance
- [ ] Commit own dir only
- [ ] Write reports/retrieve-Brule_2016.md

## TAGS EXISTING IN INDEX
`systematic-review, inclusive-cartography, protocol, accessibility, ai-assisted-screening` — for MapSense chose: accessibility, inclusive-cartography, tactile-maps, visually-impaired, participatory-design.

## FINAL STATE (pre-commit)
- All artifacts present: notes.md (now ~290 lines with reconcile section), metadata.json, abstract.md, description.md, citations.md, pngs/000-013 (pages 6 & 9 regenerated from black), paper.pdf
- Provenance stamped by pks
- Reconcile done: forward links to Brock_2015, Gual_2015; new leads listed; back-annotations added to Gual_2015 (Cited By + Conceptual), Ducasse_2018 (Now in Collection), Holloway_2018 (new Collection Cross-References section), Wabinski_2022 (Now in Collection + Conceptual Links + inline mark)
- Brock_2015 already had Brulé cross-ref (idempotent skip)
- Rowell_2003 "match" was a reconcile-log false positive (Rowell 2003 predates Brulé 2016)
- papers/index.md NOT touched (parallel-swarm rule)
- papers/ root has no stray PDFs
- git status shows two modified notes.md files (Ducasse, Holloway) from reconcile — allowed by parent prompt
- Linter/auto-reconciler also enriched Gual_2015 with more cross-references (benign, kept)

## BLOCKER
None. Ready to commit.

## COMMITTED
Hash: 3d29854 "add: Brule_2016_MapSense via paper-process" — 6 files, 463 insertions. Other parallel workers' commits have since landed on top (Papadopoulos, Tian_2023, Götzelmann dedupe fix). Branch history confirms 3d29854 is present.
Report written: reports/retrieve-Brule_2016.md
TASK COMPLETE.
