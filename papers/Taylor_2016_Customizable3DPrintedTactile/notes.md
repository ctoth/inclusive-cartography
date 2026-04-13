---
title: "Customizable 3D Printed Tactile Maps as Interactive Overlays"
authors: "Brandon Taylor, Anind Dey, Dan Siewiorek, Asim Smailagic"
year: 2016
venue: "ASSETS 2016 — Proceedings of the 18th International ACM SIGACCESS Conference on Computers and Accessibility"
doi_url: "https://doi.org/10.1145/2982142.2982167"
affiliation: "Carnegie Mellon University, Human-Computer Interaction Institute, Pittsburgh PA"
---

# Customizable 3D Printed Tactile Maps as Interactive Overlays

## One-Sentence Summary
Presents an end-to-end system in which a visually impaired user (or proxy) enters a location on a web form, the system auto-generates a 3D model from OpenStreetMap (OSM) data, the map is 3D printed, and the printed map is then registered as a conductive capacitive overlay on a standard Android touchscreen so that finger touches on raised tactile features trigger audio labels spoken by the phone — demonstrated on three NIH/Samsung Galaxy Tab 10.1 tablets with 12 visually impaired participants using maps of Pittsburgh, Nevada (MO), and a college campus. *(p.71, p.75, p.76)*

## Problem Addressed
Commercial 3D printing has made custom tactile maps economically feasible, but (a) the resulting maps are purely passive, (b) the only widely available interactive tactile-map systems (e.g. Touch Graphics' Talking Tactile Tablet) require a large specialized proprietary tablet and a pre-built map catalog, and (c) existing toolchains for authoring new tactile maps either require sighted expert labor (inkjet-on-microcapsule, swell-paper) or build the interactive/labeling data out of band from the tactile artifact itself. The paper asks: can we generate a **customizable, interactive, audio-labeled tactile map for arbitrary locations** that runs on a **commodity smartphone/tablet** using only **conductive 3D prints as passive overlays**, with **no modification to the touchscreen device and no specialized receiver hardware**. *(p.71, p.72)*

## Key Contributions
- A web interface (simple + advanced) that converts a user-specified location into an STL model from OSM data, printable directly on a consumer FDM printer. *(p.72-74)*
- A 3D-printable map format (PLA base + conductive PLA features) that acts as a **capacitive touchscreen overlay**: the conductive raised feature is grounded by the user's finger, so a touch on the tactile landmark registers under it on the underlying tablet. *(p.74-75)*
- A four-registration-hole mechanical alignment scheme that keeps the print and tablet in fixed relative coordinates so touchscreen (x,y) → map feature ID is deterministic. *(p.74, p.75)*
- An Android application that pairs OSM feature IDs to text labels and speaks them via TTS when the corresponding capacitive contact is detected, built as an **audio overlay** rather than a new map renderer. *(p.75)*
- A user study with 12 visually impaired participants across three sites (Pittsburgh, Nevada MO, Carnegie Mellon campus) showing feasibility and surfacing the real-world failure modes of conductive PLA + capacitive sensing. *(p.75-77)*
- Three explicit categories of design improvement derived from study data: improve web-interface usability, improve modeling algorithm (symbol library, thicker roads, better symbol choice), and iterate on the interactive application (gestures, other tap layers). *(p.78)*

## Study Design (empirical papers)
- **Type:** Mixed-method, qualitative-dominant feasibility study with three regional user groups. Not a controlled experiment. Data = observational feedback + qualitative interviews during guided interaction sessions. *(p.75-76)*
- **Population:** 12 visually impaired participants across three sites. Pittsburgh group = Blind and Vision Rehabilitation Services of Pittsburgh (4 participants). Nevada, MO group = Missouri School for the Blind / local community (4 participants). Carnegie Mellon College campus group = 4 participants. Each group received a map tailored to their own region so that landmarks would be familiar. *(p.75-76)*
- **Intervention(s):** Participants were handed a 3D-printed tactile map aligned to a Samsung Galaxy Tab 10.1 and allowed to freely explore it with the interactive audio application active. Features touched triggered spoken labels. *(p.75-77, Figures 7-9)*
- **Comparator(s):** None. No within-subject comparison to passive tactile maps or to TTT-style commercial systems. *(p.75, p.77)*
- **Primary endpoint(s):** Qualitative feedback on (i) map readability, (ii) usefulness of audio labels, (iii) desired features and issues, plus observational notes on touch-recognition failures. *(p.77)*
- **Secondary endpoint(s):** Concrete feature requests (simpler/coarser symbols, adjustable road thickness, tap gestures, alternate data layers) and observed hardware failure modes (capacitive contact intermittent, small features missed by fingertip). *(p.77-78)*
- **Follow-up:** Single session per group. No longitudinal use or home deployment. *(implicit, p.77)*

## Methodology

### System overview
Two decoupled but interlocking subsystems. *(p.72, p.75)*

1. **Map generation pipeline** (web-hosted).
   - Input = user-supplied location + parameters.
   - Data source = OpenStreetMap (OSM). *(p.73)*
   - Output = STL model of a square plate with raised tactile features (roads/landmarks/labels) and **registration holes in the four corners**. STL is downloaded to the user, then printed on any consumer FDM printer using white PLA for the base and conductive PLA for features. *(p.74)*

2. **Interactive overlay subsystem** (client-side).
   - A standard Samsung Galaxy Tab 10.1 with a capacitive touchscreen, mounted under the print.
   - The print physically registers to the tablet via the four corner holes that mate with corner pegs/bumps, giving a fixed print↔screen coordinate transform. *(p.74, p.75, Figure 5)*
   - An Android application is launched that maintains a manifest (feature → label) exported by the map generator at print time. When a capacitive touch lands inside a feature polygon, the label is spoken. *(p.75)*

### Web interface — two modes

#### Simple interface *(p.73, Figure 1)*
Minimum inputs: address / place / coordinates, "create map". Used for one-click map generation by someone unfamiliar with GIS concepts.

#### Advanced interface *(p.73-74, Figures 2, 3)*
Two tabs: **Places** and **General Subject Data**.
- **Places tab:** free-form "Place Name" field (user-chosen plain-text label) paired with an address lookup; adds a marker/location to the current map. Multiple places can be added to build a custom "My List". *(p.73)*
- **General Subject Data tab:** drop-down of OSM feature classes (e.g., streets/roads of configurable thickness; parks; building footprints; water; etc.) that the user toggles on/off so the generated print includes only the chosen layers. *(p.74, Figure 3)*

### Map model generation (authoring pipeline) *(p.74, §3.3)*
- Queries OSM for the user-specified bounding box / place set.
- Produces a 3D model in two steps: (1) a flat rectangular **base plate** in STL, (2) OSM vector features extruded above the plate with different heights/widths per feature class so they are distinguishable by touch.
- Embeds four corner registration holes in the plate for alignment.
- Stops before material assignment: the user is responsible at print time for swapping filament so the tactile raised features are printed in **conductive PLA** and the surrounding base in standard (non-conductive) PLA. *(p.74-75)*
- The output is a standard STL plus a companion feature manifest (OSM id → textual label → geometry polygon in map coordinates) consumed by the Android app.

### Conductive-PLA overlay mechanism *(p.75, §3.4, Figure 5)*
- Conductive PLA (commercially available) is electrically continuous from the top surface of a raised feature down through the plate to the tablet's capacitive glass.
- A human finger touching the top of a raised conductive feature is grounded; the capacitance path through the conductive PLA down to the screen surface appears to the capacitive touchscreen as a touch at that (x,y) under the print. This makes the tactile feature itself the input transducer — no electronics, no battery, no receiver.
- Plate material is standard (non-conductive) PLA so that only deliberate touches on conductive features register. *(p.75)*
- The paper notes that real-world capacitive detection is sensitive to feature size/area, feature height, material contact continuity, and how the user places their fingertip. *(p.77)*

### Interactive Android application *(p.75, §3.4.1)*
- Runs fullscreen on the tablet under the print.
- Takes raw touch events and looks up the enclosing feature polygon via the companion manifest.
- Speaks the feature's label through the device's text-to-speech.
- Current prototype's interaction model is tap-only (no gestures, no multi-tap meaning, no alternate label layers). *(p.77-78)*

### Validation approach *(p.75, §4)*
- Qualitative, formative validation. Three groups of visually impaired users, each in a different city, each exploring a region-appropriate printed map while the app is active.
- Data captured: subjective feedback on readability, audio usefulness, desired features; observational notes on failed touches. No quantitative accuracy metric is reported. *(p.77)*

## Key Equations / Statistical Models

This paper is a systems / HCI paper and **contains no formal equations or statistical models**. Effect sizes, hypothesis tests, and confidence intervals are not reported. *(p.71-79)*

## Parameters

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Tablet model (validation platform) | — | — | Samsung Galaxy Tab 10.1 | — | p.75, p.77 | Standard consumer capacitive tablet; nothing modified |
| Touchscreen type | — | — | Capacitive | — | p.75 | Overlay mechanism requires capacitive sensing |
| Base plate material | — | — | Standard PLA | — | p.74-75 | Non-conductive, insulates surrounding area |
| Feature material | — | — | Conductive PLA | — | p.74-75 | Carries capacitance from fingertip to screen |
| Registration hole count | — | count | 4 | — | p.74, p.75 | One per corner; constrains print to tablet |
| Map data source | — | — | OpenStreetMap | — | p.73 | Queried per user-selected bounding box / place |
| Output model format | — | — | STL | — | p.74 | Printable on any consumer FDM printer |
| Participant count | N | count | 12 | — | p.75 | Aggregated across three sites |
| Pittsburgh site | — | count | 4 | — | p.75-76 | Blind & Vision Rehabilitation Services of Pittsburgh |
| Nevada, MO site | — | count | 4 | — | p.75-76 | MO School for the Blind / community |
| Carnegie Mellon site | — | count | 4 | — | p.76 | College-campus map group |
| Road thickness (prototype critique) | — | print units | "too thin" | — | p.77 | Users reported default road widths were hard to feel; called out for a later iteration |
| Symbol size vs fingertip | — | print units | "sometimes smaller than fingertip" | — | p.77 | Observed failure: features smaller than a fingertip were unreliably touched |
| Validation session type | — | — | free exploration + structured Q&A | — | p.75-77 | No quantitative accuracy metric |

*(All values above are exactly as reported in the paper. The paper does not quote numerical thresholds for feature dimensions, touch activation area, PLA conductivity, or registration tolerance — those numbers are simply not given.)*

## Effect Sizes / Key Quantitative Results

The paper reports **no effect sizes, no confidence intervals, and no statistical results**. Findings are entirely qualitative. *(p.75-78)*

## Methods & Implementation Details
- Map generator is implemented as a **web application**; user does not install tooling. Input via HTML forms, output is an STL download. *(p.73-74)*
- The advanced interface separates **"Places" (point-of-interest labeling)** from **"General Subject Data" (OSM feature layers)** so users can both drop custom labels and toggle which OSM classes are rendered. *(p.73-74)*
- Registration of print to tablet: four corner registration holes in the base plate mate to corresponding corner features (pegs/edges) on the tablet/bezel, providing a repeatable rigid transform without any electronic calibration. *(p.74, p.75, Figure 5)*
- Print recipe: a standard consumer FDM printer, two filaments (standard PLA for the base, conductive PLA for raised features). The user must perform a **filament swap** at the slicer-defined layer separating base from features. *(p.74-75)*
- The Android app does not render a map; it binds touch events to pre-defined feature polygons exported alongside the STL. This keeps authoring and runtime coupled by the same generator output. *(p.75)*
- Observational finding: **small features are missed** because the conductive contact area under a fingertip is finite and uneven, so tiny dots do not reliably trigger. *(p.77)*
- Observational finding: **road widths printed "too thin" are hard to both feel and touch-activate** at default settings. *(p.77)*
- Observational finding: **capacitive contact is intermittent** — users sometimes had to press harder or re-place the finger for the label to trigger, which users reported felt "frustrating" and reduced trust in the label. *(p.77)*
- The prototype is a **single-layer interaction**: one feature → one label. It has no modal gestures and no support for alternate label layers (e.g., switch between "street names" and "hazards"). *(p.77-78)*
- Authors explicitly note the system is **not intended as a navigation aid**; it is a map surrogate to build spatial familiarity with an area before/after travel. *(p.77)*

### Pseudo-code (authoring pipeline, reconstructed from §3.1–3.4)

```
input: location_query (address/place/bbox), feature_classes[], places_list[]
osm_data = query_osm(location_query, feature_classes)
base_plate = make_rectangular_plate(bbox, thickness)
add_registration_holes(base_plate, corners=4)
for feature in osm_data:
    poly3d = extrude(feature.geometry, height_by_class[feature.class])
    base_plate.union(poly3d)
for place in places_list:
    marker = extrude(place.point, height=marker_height)
    base_plate.union(marker)
stl = export_stl(base_plate)
manifest = export_feature_map(osm_data + places_list)   # OSM id -> label, polygon
return stl, manifest
```

### Pseudo-code (runtime overlay app)

```
load manifest.json               // feature polygons + labels, in map coords
calibrate:
    map_corner_pixels := four registration holes on tablet
    T := affine_fit(map_corners, tablet_corners)
on touch (x_touch, y_touch):
    (x_map, y_map) := T⁻¹ · (x_touch, y_touch)
    f := first feature whose polygon contains (x_map, y_map)
    if f is not None:
        tts.speak(f.label)
```

*(Paper does not publish real source, but the above is the algorithm as described in §3.3–3.4. *(p.74-75)*)*

## Figures of Interest
- **Figure 1 (p.73):** Simple web interface. Single form field for location plus a "Generate map" action. Demonstrates the low-ceremony entry point for end users. *(p.73)*
- **Figure 2 (p.73):** Advanced web interface — "Places" tab. Free-form place name and address field, produces a "My List" of annotated points on the current map. *(p.73)*
- **Figure 3 (p.74):** Advanced web interface — "General Subject Data" tab. Drop-down selector of OSM feature classes to include in the print. *(p.74)*
- **Figure 4 (p.74):** Tactile maps generated by the system: left = blue/ridged OSM street grid, right = color-coded rendering of topography. Documents that the pipeline can emit both high-contrast street maps and topographic maps from the same generator. *(p.74)*
- **Figure 5 (p.75):** Headline mechanism diagram — a 3D printed tactile map sits over a tablet and the finger on a conductive feature registers as a touch on the screen. *(p.75)*
- **Figure 6 (p.75):** A map with conductive features printed. Shows the physical artifact used in the study. *(p.75)*
- **Figure 7 (p.76):** Interactive map of a college campus on a Samsung Galaxy Tab 10.1, buildings printed as tall tactile blocks. *(p.76)*
- **Figure 8 (p.77):** Map of Nevada, MO showing the same features represented on the map as presented to participants. Uses shaded lines with X-marks at end-points to represent paths described by participants when asked to provide directions from a triangle to a square on the map. *(p.77)*
- **Figure 9 (p.77):** Interactive map of a college campus on a Samsung Galaxy Tab 10.1 tablet — the black buildings act as touchpoints and announce building names when touched. *(p.77)*

## Results Summary
- **Feasibility result:** The conductive-PLA overlay mechanism works on commodity Android tablets with no hardware modification. Touching raised conductive features grounded via a human fingertip does trigger touchscreen events that the companion app can resolve to a label. *(p.75, p.77)*
- **Authoring result:** The pipeline successfully produced region-appropriate tactile maps for three different sites (Pittsburgh street map, Nevada MO town map, CMU campus map) from OpenStreetMap data without requiring a cartographer in the loop. *(p.75-76)*
- **Usability result (positive):** Participants who had prior tactile-map experience generally understood the raised features and were able to trace roads / buildings; audio labels were valued especially for places/buildings that would otherwise require external annotation. *(p.77)*
- **Usability result (negative) — 1:** Capacitive touch recognition was **intermittent**. Users had to press more deliberately on some features than on others; "it doesn't feel good to me at all" was a recurring complaint. *(p.77)*
- **Usability result (negative) — 2:** **Small features were missed** because the activation zone for a fingertip is larger than tiny printed dots / symbols. *(p.77)*
- **Usability result (negative) — 3:** Road representations at the default width were **"too thin" to feel reliably**, both tactilely and as touch targets. *(p.77)*
- **Usability result (negative) — 4:** Because there was no gesture vocabulary, users could not ask for more detail about a feature once they'd triggered its single label, and they could not switch layers (names vs hazards vs elevation). They reported this as a clear limitation. *(p.78)*
- **Qualitative directions task:** Users were asked to describe a path between two landmarks on the Nevada, MO map. Their described paths (Figure 8) clustered around clearly-marked routes, indicating the raised features were legible enough for route reasoning even with the touch limitations. *(p.77)*

## Limitations
- **Capacitive touch is unreliable** on small / thin / uneven features. The paper frames this as the dominant real-world pain point. *(p.77)*
- **Fingertip area bounds minimum feature size** — features smaller than a fingertip were routinely missed. *(p.77)*
- **The current app supports only tap → single label.** No gestures, no multi-tap, no layered annotations, no cross-links between features. *(p.77-78)*
- **The map generator does not adapt thickness / symbol choice to the target user.** Users explicitly asked for thicker roads and coarser, more distinguishable symbols. *(p.77-78)*
- **Conductive PLA properties are not characterized** in the paper. The authors do not report conductivity, touch activation thresholds, or contact resistance, so reproducing the result depends on filament-specific behavior. *(p.77)*
- **No navigation or turn-by-turn functionality** is supported; the system is explicitly a *pre-travel or post-travel* orientation aid, not a mobility aid. *(p.77)*
- **Study is qualitative and small (N=12)** with no control condition and no accuracy metrics. *(p.75-77)*
- **No longitudinal or home use**; session-only observations. *(implicit, p.77)*
- **Print cost and print time** are not reported, so economic viability for real deployment is not established in the paper. *(implicit)*
- **Filament-swap requirement at print time** puts the final burden of material continuity on the end user — a failure mode the paper acknowledges can break conductivity silently. *(p.74-75)*

## Arguments Against Prior Work
- **Against manual / expert tactile-map production** (swell-paper, microcapsule paper, braille embosser workflows): these required a specialized workflow and either a cartographer or specialized equipment per map, so users could not easily get a map for **their** location. 3D printing, the paper argues, reduces the incremental cost per map to filament + print time and can be done by a non-expert once the STL is generated. *(p.72)*
- **Against Touch Graphics' Talking Tactile Tablet (TTT) / TMAP**: TTT is cited as the reference interactive tactile map system, but it requires a large proprietary tablet and a curated catalog of physical maps that must each be authored and shipped. The Taylor system, in contrast, generates arbitrary maps from OSM and runs on a consumer smartphone/tablet that the user already owns. *(p.72-73)*
- **Against capacitive-stylus and electronic-widget overlays** (systems that embed electronics into the tactile artifact to drive the touchscreen): those require batteries, electronics, or active receiver hardware on the map; this paper's conductive-PLA path is a **purely passive artifact** that exploits the existing touchscreen. *(p.72, p.75)*
- **Against geocoded tactile maps that keep the label data outside the printed artifact** (e.g., separate audio files triggered by an external barcode scanner): Taylor et al. argue the label metadata should be generated *co-incidentally* with the STL so they stay in sync — drift between print and label data is a known failure mode for older pipelines. *(p.73)*

## Design Rationale
- **Why OpenStreetMap as the data source:** OSM covers arbitrary regions at arbitrary zooms and is freely licensable, so a single pipeline can cover every user's locale without per-region licensing. *(p.73)*
- **Why a web front-end instead of a local tool:** visually impaired end users (or more often, sighted caregivers/teachers generating maps for them) should not need to install slicer/GIS tooling. A web form plus an STL download minimizes the setup to one link and one print. *(p.73)*
- **Why a two-tier UI (simple + advanced):** the paper explicitly chooses to expose both a one-click entry point and a full feature-selection UI, because caregivers/educators often want control over what appears on the map, while an end user wants a single "generate" action. *(p.73-74)*
- **Why conductive PLA + passive overlay instead of active electronics:** passive means no battery, no pairing, no per-device firmware — the map is just a plastic plate and the intelligence lives on a phone the user already owns. *(p.75)*
- **Why four registration holes:** four corners pin translation, rotation, and shear so that the feature manifest can use a single rigid affine transform from map coords to tablet pixel coords; fewer registration points would underconstrain. *(p.74-75, Figure 5)*
- **Why author labels alongside the STL:** guarantees that every printed feature has a corresponding label entry in the runtime manifest, preventing silent label misalignment. *(p.74-75)*
- **Why reject cartographer-built symbol libraries for v1:** the paper's pipeline deliberately uses direct OSM geometry extrusions so that adding a new city or a new feature class does not require hand-authoring symbols; users complained that this produced symbols they found ambiguous, and the paper explicitly defers a symbol library to future work. *(p.77-78)*
- **Why study three geographically different sites:** exercising the pipeline on a dense city center, a small town, and a college campus demonstrates that the OSM-to-STL path produces recognizable maps across scales, not just in the authors' own neighborhood. *(p.75-76)*

## Testable Properties
- A touch on a raised **conductive** feature must produce a screen-space capacitive event at the same location on the underlying tablet. *(p.75)* 
- A touch on the **non-conductive base plate** must NOT register as a touch event. *(p.75)*
- Given the four-corner registration, the screen-space touch coordinates must map to the correct feature polygon via a single affine transform. *(p.74-75)*
- Every feature present in the printed STL must have a corresponding entry in the runtime feature manifest (no unlabeled features). *(p.74-75)*
- The system must produce a valid STL for arbitrary OSM bounding boxes within the covered feature classes. *(p.73-74)*
- Printed features smaller than the effective fingertip contact area will have lower activation reliability — an observed empirical property, not a guaranteed bound. *(p.77)*
- Road geometry extruded at the default thickness will be rated "too thin" by users of this population; increasing road thickness is predicted to improve both tactile legibility and touch activation. *(p.77-78)*
- Adding a gesture vocabulary (e.g., double-tap, two-finger tap) must be able to switch label layers without changing the printed artifact. *(p.78, §6.3)*
- The system should not require any driver / firmware / pairing on the host tablet — i.e., it must work with only an installed application and standard touch input. *(p.75)*

## Relevance to Project
Directly relevant to the inclusive-cartography project's §3.3 "Seed selection & scoping" because this paper sits at the intersection of (a) **automated generation of tactile cartographic artifacts from OSM**, (b) **inclusive interaction design for blind/low-vision users**, and (c) **commodity-device deployment** (no custom hardware). For the protocol critique on LLM-confidence thresholds, the paper is a useful counter-example to "high-confidence = well-characterized": the system is reliably reproducible in principle (OSM → STL → print) but the *effective* reliability of interaction is dominated by poorly characterized physical properties (conductive PLA behavior, fingertip contact, feature geometry). That gap is exactly the kind of thing protocol-level confidence gating based on textual description can overlook, because the paper itself is confident in the architecture but observational about the failures. *(p.71-78)*

Specific reuse candidates for our review:
- **Authoring pipeline shape** (OSM → feature selection → STL + label manifest) is reusable for any downstream inclusive-map work.
- **Four-corner rigid registration** is a simple, copyable mechanical-to-digital coupling.
- **Capacitive conductive-PLA overlay** is a candidate technique when we need low-cost audio-augmented artifacts but must be treated as empirically fragile until characterized.
- **The three study-group feedback themes** (symbol legibility, feature thickness, gesture vocabulary) give us a prior for what will fail when we deploy similar artifacts.

## Open Questions
- [ ] What conductive PLA filament did they use, and how does conductivity vary with print parameters (layer height, extrusion temperature, bed temperature, feed rate)?
- [ ] What is the minimum reliable feature area for touch activation on Samsung Galaxy Tab 10.1 with their filament?
- [ ] What registration tolerance is required between print and tablet before touch-to-feature mapping becomes wrong?
- [ ] How does the system handle two simultaneous touches on adjacent conductive features?
- [ ] How expensive (print time, filament cost) is a typical map? The paper argues commodity 3D printing makes this viable but gives no numbers.
- [ ] Is the advanced web interface accessible (screen-reader-friendly) for blind users to generate their own maps, or does it require a sighted helper?
- [ ] What is the failure mode when conductive PLA continuity is broken mid-print (e.g., filament gap) — silent dead feature?
- [ ] Could the Android app be ported to iOS, or is the capacitive-touch routing Android-specific in practice?

## Collection Cross-References

### Already in Collection
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — Same venue (ASSETS '16), directly companion 3D-printed tactile map approach. Taylor cites Götzelmann & Pavkovic's OSM → 3D-print line of work in §2.1 / §2.2 as prior art showing the OSM pipeline without interactive overlay. Taylor's contribution is the capacitive-overlay + interactivity layer on top of Götzelmann-style OSM-driven 3D printing.

### Cited By (in Collection)
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Wabinski, Moscicka & Touya (2022) cite Taylor, Dey, Siewiorek & Smailagic (2016) as an example of end-to-end OSM-driven capacitive-overlay tactile map production. It appears in the production-method discussion as a concrete automation pipeline of the kind Wabinski's parameter tables are meant to constrain (minimum feature size, minimum line width, minimum relief height). Taylor et al.'s acknowledgement of "roads printed too thin" failure mode is exactly what Wabinski's minimum-line-width parameter (~0.5-2.0 mm) would have predicted.
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — Götzelmann's reconciliation notes Taylor 2016 as the same-venue directly competing approach: Taylor targets a general 3D-printed interactive overlay with conductive-PLA touch input, Götzelmann targets a translucent overlay + OSM + CapCodes pipeline on commodity Android. Critical head-to-head reference for the tools/technologies question.
- [[Brock_2015_InteractiveMapsUsability]] — Brock's reconciliation lists Taylor 2016 as a 3D-printed customizable tactile map contribution in the same evaluation space as Brock's audio-tactile interactive map.
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — Brulé's reconciliation describes Taylor 2016 as a contemporaneous alternative hardware stack — Taylor favors a 3D-printed map surface; Brulé favors a raised-paper overlay with separate 3D-printed tokens. Different tradeoffs within the same design space.
- [[Gual_2015_EffectVolumetric3DTactile]] — Gual's conceptual-link section notes Taylor 2016 as the tooling side of the "add 3D relief to tactile maps" design hypothesis Gual provides the empirical justification for.
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — Papadopoulos's reconciliation notes Taylor's customizable 3D-printed tactile map overlays as a fabrication pathway for the kind of embossed map used in Papadopoulos's audio-tactile condition.
- [[Rowell_2003_WorldTouchResultsInternational]] — Rowell's reconciliation classes Taylor 2016 as a post-2003 3D-printed production method absent from Rowell & Ungar's seven-method taxonomy.
- [[Ducasse_2018_AccessibleInteractiveMapsVisually]] — Ducasse's survey treats Taylor as one of the customizable 3D-printed tactile map production tools within the DIM/HIM taxonomy.

### Conceptual Links (not citation-based)
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — Strong. Same ASSETS'16 venue, two independent 2016 groups converging on "consumer 3D printing + commodity touchscreens" as the practical substrate for personalized accessible cartography. Taylor uses opaque 3D-printed overlay with conductive-ink input; Götzelmann uses translucent PLA with passive capacitive markers. Convergent finding.
- [[Holloway_2018_AccessibleMapsBlindComparing]] — Strong. Holloway's later controlled within-subjects 3D-vs-2D study provides the empirical comparison Taylor's pipeline paper explicitly does not publish. Reading Holloway alongside Taylor answers "does the fabrication effort Taylor automates actually matter for end-task performance."
- [[Gual_2015_EffectVolumetric3DTactile]] — Strong. Gual provides the symbol-level empirical warrant (volumetric > flat for BVI recall) that Taylor's fabrication pipeline operationalizes at whole-map scale.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Moderate. Wabinski's parameter tables are directly applicable as the design-invariant floor Taylor's pipeline should honor; Taylor's "roads printed too thin" failure is the paradigmatic example Wabinski's minimum-line-width rule would prevent.
- [[Wabiski_2026_CognitiveReviewProtocol]] — Moderate. Taylor 2016 is the paradigmatic "high apparent confidence, low empirical characterization" paper whose handling tests the protocol's confidence-threshold rule.

## Related Work Worth Reading
- **Touch Graphics — Talking Tactile Tablet (TTT) and TMAP** (cited throughout §2.2): the reference commercial interactive tactile-map platform this paper compares against. *(p.72)*
- **Götzelmann and Pavkovic** — OpenStreetMap-based 3D printed tactile maps (cited in §2.1, §2.2): prior art showing the OSM → 3D print path without interactive overlay. *(p.72)*
- **South/Kettlewell Eye Research Institute — Tactile Maps Automated Production (TMAP)** (cited §2.2): upstream TIGER-based tactile map generator. *(p.72)*
- **OrientaMap / TMACS** (cited §2.2): independent tactile map production systems in Europe. *(p.72)*
- **Lenovo Showroom at IBM / Ladner et al.** on automatic braille annotation on tactile prints (cited §2): adjacent prior art on inkjet labeling of tactile artifacts. *(p.72)*

## Open Questions for the protocol critique (notes for tomorrow's meeting)
- This paper is a clean example of "high apparent confidence, low empirical characterization." A LLM-confidence threshold that scores textual plausibility will rate it high; a threshold that requires quantified testable properties will rate it low. That tension is exactly what the protocol critique needs.
- The paper never publishes a single number about conductive-PLA touch behavior, minimum feature size, or cost. Any downstream synthesis that cites this paper as "solved" is overreaching.

## Provenance
- Read by: claude-opus-4-6[1m] (parallel-swarm worker)
- Source: sci-hub mirror of ACM DL (DOI 10.1145/2982142.2982167) via Chrome-authenticated session
- Pages read: 9/9 (full paper, including original and re-rendered PNGs for pages 001, 006, 007)
- Re-render tool: pdftoppm + ImageMagick (ImageMagick alone produced blank rasters for those three pages due to transparency handling)
