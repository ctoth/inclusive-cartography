---
title: "LucentMaps: 3D Printed Audiovisual Tactile Maps for Blind and Visually Impaired People"
authors: "Timo Goetzelmann"
year: 2016
venue: "ASSETS '16 — Proceedings of the 18th International ACM SIGACCESS Conference on Computers and Accessibility"
doi_url: "https://doi.org/10.1145/2982142.2982163"
pages: "81-90"
affiliation: "Nuremberg Institute of Technology, Germany"
---

# LucentMaps: 3D Printed Audiovisual Tactile Maps for Blind and Visually Impaired People

## One-Sentence Summary
LucentMaps fabricates translucent, low-cost FDM 3D-printed tactile map overlays that lie flat on a consumer smartphone/tablet touchscreen, using embedded height-coded capacitive markers ("CapCodes") to self-identify the printed map to the device so that standard mobile software can deliver per-POI speech output and route information when a blind user touches the surface (p.81-83).

## Problem Addressed
Blind and visually impaired (BVI) people need accessible geographic maps for orientation and mobility, but traditional swell-paper tactile maps and braille labels are limited — small percentage of BVI read braille (US <10%), only limited info fits on one map, and no dynamic feedback is possible (p.81). Prior interactive tactile maps (audio-tactile tablets, raised-line overlays on capacitive surfaces, projection/vision-based setups, tangible augmented paper maps) each have disqualifying drawbacks: special hardware, tethering, cost, bulky installation, or a need for centralized infrastructure — preventing individual at-home production and use of personalized maps (p.81-82). The paper targets a cheap, portable, personal pipeline that any BVI user could run on their own with a consumer 3D printer and smartphone.

## Key Contributions
- A novel class of 3D-printed **translucent** tactile maps ("LucentMaps") producible on a commodity consumer FDM printer in translucent PLA, which physically sit on top of a commodity capacitive touchscreen and permit optical and capacitive interaction through the print (p.81, p.83).
- Technical investigation of FDM print parameters (layer height, nozzle, infill, fill patterns) needed so the resulting maps remain translucent and electrically transparent enough for simultaneous visual display and capacitive touch sensing through the overlay (p.83).
- A set of **3D-printed capacitive markers** (aka CapCodes, ref [30]) embedded at the map corners to encode a map ID readable by the host device's capacitive touchscreen — letting the device automatically identify which map has been placed on it, so the app loads matching annotations (p.83-84).
- An Android application (API 4.0.3+) implementing map identification, touch mapping, pinpoint announcement, gesture-activated disambiguation, and feature-category filtering, integrated with OpenStreetMap data (p.85-86).
- A small qualitative user evaluation (n=5 BVI participants, ages 15-57, both congenitally and later blind) that exercised two map-identification procedures, pinpoint exploration, route following, and augmented tactile-map recognition using real OSM data for a small German city (p.86-87).
- Analysis of cost and availability showing consumer-grade production: ~10 g PLA per ~30×30 cm overlay at ~$0.40, roughly ~1 h print time, hardware ≈$500 (p.87).
- Discussion of how LucentMaps compares to CustomMaps/TouchOver-like approaches and why the combination of 3D printing, OSM data, translucent PLA, and capacitive coupling yields a more practical dissemination path (p.87).

## Study Design (empirical papers)
- **Type:** Qualitative usability study / feasibility evaluation (not a controlled comparison).
- **Population:** 5 BVI participants, ages 15-57 years; mix of congenitally blind and those blinded later; recruited near Nuremberg, Germany; each offered a 30 cm × 30 cm LucentMaps overlay of their home area as incentive (p.86).
- **Intervention(s):** Interaction with a LucentMaps overlay bonded to a consumer tablet (ODROID 10" tablet used as the target device, 1024 px screen, resolution up to 20 microns / 20 μm per tactile line width) running the Android LucentMaps app backed by OSM. Two identification procedures (code-A then code-B at a single corner vs. all four corners) and multiple usage scenarios: blind person using smartphone, blind person using tablet, and visually-impaired person using tablet-with-visual-augmentation (p.86).
- **Comparator(s):** No formal comparator arm; informally, the paper contrasts its approach against non-augmented swell-paper tactile maps and prior audio-tactile/vision-based map systems (p.86).
- **Primary endpoint(s):** Whether the touchscreen reliably identified the map, whether participants could locate features and hear correct speech feedback, whether the route-following feature conveyed direction and distance usefully (p.86-87).
- **Secondary endpoint(s):** Subjective feedback on button labeling, gesture discoverability, usefulness of the speech synthesis, and whether visually impaired users benefited from the underlying screen display shining through the translucent map (p.86-87).
- **Follow-up:** Single-session; no follow-up measured.

## Methodology
Two engineering pipelines run in parallel then meet at the device: (1) an OSM-driven map-generation pipeline produces a 3D model in Python + Blender that places extruded features (line walls for roads, planar blocks for buildings/water bodies) plus four corner CapCode markers onto a flat translucent slab; (2) the Android client loads the same underlying OSM geometry, authenticates the physical map via CapCodes (via the touchscreen), and then services touches on the overlay as touches on the corresponding on-screen map. Touches anywhere under a map feature produce an audio announcement; predefined gestures give "what's at this point", category filtering, and route/direction queries. The overlay is bonded in registration to the corners of the device, so the touchscreen's screen-pixel coordinates correspond one-to-one with the printed map's features (p.83-86).

The translucency enables a second mode for users with residual vision: a high-contrast or magnified rendering of the same map can be displayed on the tablet underneath the tactile overlay, visually reinforcing the haptic features (p.82, p.86-87).

## Key Equations / Statistical Models
None — this is a systems / HCI paper with no mathematical models or statistical inference.

## Parameters

### Print / Fabrication Parameters

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Filament material | — | — | translucent PLA | — | p.85 | FelixPrinters FelixPro 1 test rig; tuned specifically for translucency |
| Printer type | — | — | consumer FDM (fused deposition modeling) | — | p.83, 85 | Chosen over resin / SLA for cost and accessibility |
| Layer height | — | mm | not explicitly numbered in text, but "high print density" used to get translucency | — | p.83 | Coarser layers reduce clarity; finer improves light transmission |
| Nozzle diameter | — | mm | consumer-grade (standard) | — | p.83 | Affects line width on roads |
| Infill strategy | — | — | solid / high fill | — | p.83 | Partial infill makes the overlay opaque / electrically noisy |
| Overlay PLA per ~30×30 cm map | — | g | ~10 | — | p.87 | From Costs & Availability section |
| Overlay filament cost per map | — | USD | ~$0.40 | — | p.87 | At ~$40/kg PLA |
| Print time per overlay | — | hours | ~1 | — | p.87 | Commodity consumer printer |
| Hardware cost (printer) | — | USD | ~$500 | — | p.87 | Entry-level consumer FDM |
| Overlay minimum line/feature width | — | μm | ≈20 | ≥20 | p.83, p.85 | Smallest tactile line width that remained readable both tactually and visually |

### CapCode / Identification Parameters

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Markers per map | — | count | 4 | 1-4 | p.83-84 | One in each corner; used for map-ID and registration |
| CapCode axis granularity | — | — | multi-level height codes | — | p.83-84 | Ref [30]; heights encode a small ID alphabet |
| Required touch gesture (Procedure A) | — | — | single-corner touch | — | p.85-86 | Press one corner to read its code, then slide to read the next |
| Required touch gesture (Procedure B) | — | — | all-four-corners simultaneous | — | p.85-86 | Faster but harder for BVI to perform |
| Map-ID touch recognition latency | — | ms | ≤700 | — | p.85 | "below 700ms" required before TTS speaks identity |
| Map-ID recognition pause before speaking | — | — | short dwell required | — | p.85 | So the system doesn't treat routine touches as ID probes |

### Tablet / Device Parameters

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Target OS | — | — | Android | ≥4.0.3 | p.85 | Android API 14 |
| Evaluation device | — | — | ODROID 10" tablet | — | p.85-86 | Used in the n=5 feasibility study |
| Screen diagonal used | — | inches | 10 | 4-10+ | p.86 | System works on smartphone and tablet |
| Underlying data source | — | — | OpenStreetMap | — | p.85 | Fetched via OSM APIs |
| Blender generator | — | — | Python plugin for Blender | — | p.85 | Produces STL for slicing |
| Feature categories | — | — | Overview, Slow, Which, Map | — | p.85 | Four gesture-invoked filters (Buildings, Streets, Points of Interest…) |

## Effect Sizes / Key Quantitative Results

| Outcome | Measure | Value | CI | p | Population/Context | Page |
|---------|---------|-------|----|---|--------------------|------|
| Participants who successfully identified a map via CapCodes | Proportion | All 5 succeeded (5/5) | — | — | n=5 BVI, after instruction | p.86-87 |
| Preferred CapCode procedure | Qualitative | Procedure A (one-corner-then-slide) preferred over four-corner simultaneous | — | — | n=5 | p.86 |
| CapCode recognition time budget | ms | ≤700 | — | — | System spec | p.85 |
| Bill of materials for one 30×30 cm overlay | USD | ~$0.40 filament | — | — | PLA at ~$40/kg | p.87 |
| Print time for one overlay | h | ~1 | — | — | Consumer FDM | p.87 |
| Hardware cost (one-time) | USD | ~$500 | — | — | Entry-level FDM | p.87 |
| Smallest distinguishable tactile feature | μm | ~20 | — | — | 10" tablet target | p.85 |

## Methods & Implementation Details
- **Map generation pipeline** — Python plugin for Blender pulls OSM data (streets, buildings, water, POIs) and produces a single 3D model composed of: (i) extruded "walls" for streets, (ii) flat blocks for buildings, (iii) four CapCode towers at the corners, (iv) a thin translucent backplate (p.85).
- **Fabrication** — Model is sliced and printed in translucent PLA on a consumer FDM (FelixPrinters FelixPro 1 used for testing). Print parameters are tuned to maximize light transmission while preserving electrical "opacity" for capacitive coupling of fingertips through the overlay (p.83, p.85).
- **CapCode fabrication** — Each corner marker is a height-coded capacitive tower that presents a passive capacitive footprint to the touchscreen. Different code heights produce different capacitance signatures so the device can distinguish Code-A from Code-B and thus identify which map it is holding (p.83-84, Fig. 2).
- **Registration** — The overlay is bonded to the device with its corners aligned to the four corners of the screen; this gives a fixed affine mapping between printed-map coordinates and screen pixels (p.85-86).
- **Android app architecture** —
  - Android API ≥ 4.0.3 (p.85).
  - Listens to multi-touch events from the capacitive digitizer (p.85).
  - Detects the CapCode signature(s) and uses the coded ID to look up which prepared OSM region the overlay corresponds to (p.85-86).
  - Debounces identification so it only speaks the map name after a short dwell.
  - Converts raw touches within the bonded region into feature queries against the OSM feature set.
  - Invokes system TTS to speak feature names, categories, or route descriptions (p.85-86).
  - Supports gesture-driven mode switching: gestures correspond to Overview (buildings/streets/POIs), Slow (single category), Which (name/type/etc. at point), Map (distance/direction to point) (p.85).
- **Speech interaction / TTS** — Used to announce feature identity, category filtering state, route segment direction and length (p.85-86).
- **Visual-augmentation mode for visually impaired users** — Because PLA layer is translucent, the tablet underneath can simultaneously display a high-contrast / magnified rendering of the same OSM map, so residual-vision users get both the haptic and the optical signal in register (p.82, p.86-87).
- **Route-following feature** — Intended to guide the user along a multi-segment OSM route; after touching a "start" feature, the system announces direction and distance to the next waypoint, updating as the finger moves (p.86-87).
- **Feedback modalities** — Primary: speech. The system does not use vibration for feature identification (discussed as potential future work under Limitations) (p.87).

## Figures of Interest
- **Fig. 1 (p.83):** Ramp of height differences used to measure the range of distances at which proximity touches of touch displays respond ("at blue dots"). Shows the empirical calibration curve for how raised features interact with capacitive sensing.
- **Fig. 2 (p.83):** Geometry of a CapCode pair — "Start of code", "Code A", "Code B", with 12 mm / 16 mm+5 mm / 16 mm+5 mm spacing. Defines the physical layout of the identification towers at a map corner.
- **Fig. 3 (p.83):** Capacitive code for a map — paths of selection lines have been prolabeled as 1/2/3/4/5/6. Shows how the embedded code lines read out as a sequence under the user's finger.
- **Fig. 4 (p.84):** User touches ID code at the map's top-left corner and explores the map using a small tablet device. By touching the code on the bottom-left another part of the map can be explored.
- **Fig. 5 (p.85):** User queries for public transport and traffic map features (left); double-tap on the street (center); and double-tap on the building (right). For each of these interactions the TTS announces feature name and type.
- **Fig. 6 (p.86):** Augmented tactile map: adjacent buildings on the left weren't recognized as individual buildings by one participant — motivating the discussion of feature-separation heuristics.

## Results Summary
- All five participants eventually succeeded in identifying the map via the CapCodes, locating features via touch, and completing simple route queries (p.86-87).
- Participants preferred the "touch one corner, slide to the next" ID procedure over requiring four simultaneous corner touches, because the simultaneous procedure was physically awkward for users without sight (p.86).
- Participants found the speech feedback for points-of-interest categories useful, though the label set needed tuning (some category names were ambiguous to blind users) (p.87).
- Users with residual vision benefited from the underlying screen display shining through the translucent overlay (the whole reason the overlay is PLA and not opaque filament) (p.87).
- Some ambiguity in feature separation — e.g., adjacent buildings in dense blocks were not always distinguishable as separate entities to a fingertip (Fig. 6) (p.86-87).
- Hardware feasibility confirmed: ≈$500 printer, ≈$0.40 filament, ≈1 hour per overlay, on a consumer smartphone or tablet running standard Android (p.87).

## Limitations
- **Tactile resolution bounded by FDM line width**, ~20 μm minimum, which restricts how dense street/building detail can be in a small map (p.85, p.87).
- **CapCode discrimination is bounded** — only a finite set of map IDs can be encoded in the corner towers before they become too big or too close together to read reliably on a consumer touchscreen (p.87).
- **No haptic feedback from the device itself** — the overlay is passive; vibration-based feedback for feature selection is future work (p.87).
- **Limited gesture vocabulary** — the current app offers only a small set of gestures and category filters; complex queries must be chained manually (p.87).
- **n=5 qualitative study only** — no statistical comparison with alternatives, no long-term use study, no quantitative accuracy/latency metrics beyond the 700 ms ID budget (p.86-87).
- **Keyword set for features is static** — built from a subset of the OSM ontology, not extensible at runtime.
- **Feature-separation failures** — densely adjacent features (e.g., row-houses) may be perceived as one block by the fingertip even though the system treats them as distinct entities (p.86, Fig. 6).
- **Registration depends on bonding the overlay to the screen** — removing or shifting the overlay breaks the mapping; users have to re-align the corners (p.85).

## Arguments Against Prior Work
- **Against Virtual Acoustic Maps (ref [6])** — require special hardware (audio-spatialization rig) and expert calibration; not user-producible (p.81-82).
- **Against audio-tactile tablets** (TTT, etc., refs [20-22]) — require a specialized touch overlay on a custom reader and cannot re-use commodity smartphones/tablets; dissemination cost high (p.82).
- **Against swell-paper tactile maps with braille labels** — braille literacy is low among BVI users (quoted as ~15% in France, <10% in US), so braille labels serve only a minority; also, swell-paper maps are static — no route guidance or disambiguation (p.81-82).
- **Against CustomMaps-style 3D-printed tactile overlays (Taylor et al., ref [24])** — TouchOver and similar approaches do not carry embedded, machine-readable identification of which map is placed on the device, so the system cannot automatically load the corresponding annotations (p.82, p.87).
- **Against projection/vision-based systems (e.g., Holloway et al.)** — requires a top-down projector or camera rig; destroys portability and at-home applicability (p.82).
- **Against tangible augmented-paper systems (e.g., Pietrzak, ref [25])** — need extra capture hardware above the map (stylus/pen or overhead camera) (p.82).
- **Against Braille-only workflows** — excludes the majority of BVI users who cannot read braille fluently (p.81).
- **Against prior interactive audio-haptic maps on bespoke hardware (e.g., Zeng & Weber [35][36][37])** — all require either bespoke tactile displays or central fabrication; LucentMaps targets at-home production (p.82, p.87).

## Design Rationale
- **Use FDM consumer 3D printing** — chosen for accessibility, low cost, and the fact that typical households can already afford a ~$500 FDM printer; resin printers give better resolution but are more expensive and messy (p.83, p.87).
- **Use translucent PLA specifically** — key enabler for two-modal feedback: light from the underlying display can pass through the overlay so residual-vision users still see the map, and the capacitive field still couples through the ~few-mm-thick print for touch sensing (p.82, p.83, p.85).
- **Embed passive capacitive markers (CapCodes) in the print rather than stickers/RFID** — so the map is self-identifying at no extra bill of materials and cannot be separated from its data: what you touch is what it is (p.83-84, p.87).
- **Bond overlay to the four screen corners** — gives a fixed linear mapping between tactile feature positions and OSM feature coordinates, removing the need for on-screen fiducial detection (p.85).
- **Use the system TTS** — no extra audio pipeline required; labels and route descriptions come out of Android's stock speech engine, which is already tuned for accessibility (p.85-86).
- **Gesture vocabulary mirrors OSM feature ontology** — separating "what's here" from "give me direction/distance" and from "filter to this category" reduces the cognitive cost of each query (p.85).
- **Procedure A (touch-then-slide) over Procedure B (touch all four corners)** — participants without sight cannot reliably place four fingers on four corners, so the sequential code-sliding variant is privileged, even though it is slower (p.86).
- **Prefer translucent over pigmented PLA** — pigmented filament looks prettier but kills the visual-augmentation mode and can degrade capacitive coupling (p.83, p.85).

## Testable Properties
- Any printed overlay ≤ 4 mm thick and ≥ some minimum translucency passes enough capacitance through PLA that standard Android multi-touch digitizers still register fingertip touches at human-scale latency (p.83, p.85).
- Capacitive recognition of the map ID via CapCodes must complete within ≤ 700 ms for the system to consider the map identified and to begin speech output (p.85).
- The smallest tactile feature width resolved by consumer FDM print is ≈ 20 μm (p.85) — i.e., anything narrower cannot be relied on to be felt.
- Four corner markers are sufficient and necessary for both ID encoding and geometric registration in the current implementation (p.83-84, p.85-86).
- Participants with no sight can execute Procedure A (one-corner-then-slide) for map ID reliably, but not Procedure B (all four corners simultaneously) (p.86).
- Per-overlay material cost ≤ $0.50 at $40/kg PLA and ≤10 g per 30×30 cm map (p.87).
- Per-overlay fabrication time ≤ 1 h on a ≤ $500 consumer FDM printer (p.87).
- Adjacent features closer than finger-width cannot be distinguished tactually, even if they are distinct entities in OSM (p.86, Fig. 6).
- Residual-vision users with the overlay bonded to a tablet display benefit from simultaneous visual and tactile feedback (p.86-87).

## Relevance to Project
LucentMaps is directly on-theme for the inclusive-cartography systematic review of accessible tactile-map fabrication and assistive-cartography HCI, and the paper is one of the canonical 2016-era "3D-print your own tactile overlay on a phone" references alongside Taylor et al. [24] Customizable 3D Printed Tactile Maps and earlier audio-tactile map work. It matters for this project because it (1) establishes a concrete, cheap, BOM-level recipe for end-user tactile map production (so it's a good yardstick against which newer LLM-assisted cartography proposals must justify their complexity), (2) demonstrates the CapCode / embedded-fiducial pattern that later work builds on, (3) provides explicit cost and fabrication parameters that can be used when arguing about feasibility thresholds in §3.3 of the review protocol, and (4) gives us a real n=5 BVI feasibility data point for the confidence-threshold critique — a qualitative feasibility claim is what LucentMaps actually supports, not a quantitative accuracy claim.

## Open Questions
- [ ] What exact layer height / infill percentage does the paper use? (Only described qualitatively — "fine layers, high infill" — but no table.)
- [ ] How many distinct CapCode IDs can be reliably discriminated by a commodity touchscreen? (Paper says "finite, depends on screen", no number given.)
- [ ] What is the measured touch localization error through the overlay compared to bare glass? (Not reported quantitatively.)
- [ ] Does the system handle partial occlusion by the hand during exploration? (Not discussed.)
- [ ] How is the route-following feature evaluated beyond a single session? (No long-term use data.)
- [ ] What is the failure mode when two CapCodes collide in capacitance space (e.g., manufacturing variation)?
- [ ] Are there OSM feature types where the TTS labels are unintelligible to BVI users? (Paper hints yes, but no enumeration.)

## Related Work Worth Reading
- Taylor, Dey, Siewiorek, Smailagic (2016). Customizable 3D Printed Tactile Maps as Interactive Overlays. ASSETS '16 — DOI 10.1145/2982142.2982167. **(already in the project leads)**
- Götzelmann, T. & Schneider, D. (2016). CapCodes: Capacitive 3D Printable Identification and On-screen Tracking for Tangible Interaction. Nordic CHI. [30]
- Brock & Jouffrais (2015). Interactive Audio-tactile Maps for Visually Impaired People. [already in collection as Brock/Jouffrais leads]
- Zeng, Miao, Weber (2015). Interactive Audio-haptic Map Explorer on a Tactile Display. [35]
- Zeng & Weber (2011). Accessible Maps for the Visually Impaired. [36]
- Zeng & Weber (2012). ATMap: Annotated Tactile Maps for the Visually Impaired. [37]
- Wang, Li, Hedgpeth, Haven (2009). Instant Tactile-audio Map. [32]
- Way & Barner (1997). Automatic visual-to-tactile translation. [33]
- Wiethoff et al. (2012). Sketch-a-TUI: Low-cost prototyping of tangible interactions using cardboard and conductive ink. [34]
- Voelker et al. (2013). PUCs: Detecting transparent, passive untouched capacitive widgets on unmodified multi-touch displays. [31]
- Tatham (1991). The design of tactile maps: theoretical and practical considerations. [29]

## Collection Cross-References

### Already in Collection
- [[Brock_2015_InteractiveMapsUsability]] — Götzelmann cites Brock & Jouffrais 2015 for the interactive audio-tactile map usability result; LucentMaps is positioned as the cheap 3D-printed + consumer-touchscreen alternative to Brock's raised-overlay-on-multitouch interaction (p.81-82).
- [[Taylor_2016_Customizable3DPrintedTactile]] — Same venue (ASSETS '16), directly competing 3D-printed tactile map approach (DOI 10.1145/2982142.2982167). Taylor et al. target a general 3D-printed interactive overlay; Götzelmann targets a translucent overlay + OSM + CapCodes pipeline on commodity Android. Critical head-to-head reference for the review's tools/technologies question (p.82, p.87).

### New Leads (Not Yet in Collection)
- Götzelmann & Schneider (2016). CapCodes: Capacitive 3D Printable Identification and On-screen Tracking for Tangible Interaction. NordiCHI. **Ref [30]** — the companion paper defining the passive capacitive marker scheme LucentMaps depends on. Without this, the CapCode identification step is not reproducible.
- Zeng, Miao, Weber (2015). Interactive Audio-haptic Map Explorer on a Tactile Display. Interacting with Computers 27, 4: 413-429. **Ref [35]** — closest interactive-map competitor on dedicated tactile-display hardware.
- Zeng & Weber (2011). Accessible Maps for the Visually Impaired. IFIP INTERACT Workshop. **Ref [36]**.
- Zeng & Weber (2012). ATMap: Annotated Tactile Maps for the Visually Impaired. In Cognitive Behavioural Systems, Springer, 290-298. **Ref [37]**.
- Wang, Li, Hedgpeth, Haven (2009). Instant Tactile-audio Map. ASSETS '09, 43-50. **Ref [32]**.
- Voelker et al. (2013). PUCs: Detecting Transparent, Passive Untouched Capacitive Widgets on Unmodified Multi-touch Displays. ITS '13. **Ref [31]** — the passive-capacitive-widget ancestor of CapCodes.
- Wiethoff et al. (2012). Sketch-a-TUI: Low Cost Prototyping of Tangible Interactions Using Cardboard and Conductive Ink. TEI '12. **Ref [34]**.
- Tatham (1991). The design of tactile maps: theoretical and practical considerations. **Ref [29]** — foundational tactile-map design considerations.
- Way & Barner (1997). Automatic visual-to-tactile translation. IEEE Trans. Rehabilitation Engineering 5, 1: 81-94. **Ref [33]**.

### Supersedes or Recontextualizes
- (none — LucentMaps is an early consumer-3D-printing + capacitive-touch approach in a line that later papers (Holloway 2018, Ducasse 2018 review, Palivcová 2020) build on or contextualize.)

### Cited By (in Collection)
- [[Taylor_2016_Customizable3DPrintedTactile]] — cites Götzelmann & Pavkovic as prior OSM→3D-print art (refs Götzelmann's broader line of work) in §2.1 / §2.2 (Taylor notes p.72). Same venue companion.
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — treats LucentMaps as a same-year direct methodological contrast: Götzelmann's transparent-3D-print-over-tablet vs Brulé's raised-paper + 3D-printed tangibles on capacitive tablet. Part of any "design space of audio-tactile maps" synthesis.
- [[Ducasse_2018_AccessibleInteractiveMapsVisually]] — survey lists Götzelmann's 3D-printable tactile map generation work alongside other pipelines (Ducasse notes p.19).
- [[Holloway_2018_AccessibleMapsBlindComparing]] — classifies Götzelmann among prior 3D tactile map attempts that focused on production pipelines rather than controlled comparison studies; Holloway's study addresses the empirical gap that LucentMaps and peers left open (Holloway notes p.1-2).
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — identifies LucentMaps as present in the collection as an audiovisual 3D-printed O&M aid that should be evaluated on real-environment O&M transfer against Papadopoulos's baseline.
- [[Rowell_2003_WorldTouchResultsInternational]] — moderate reverse conceptual link; Rowell's 2003 snapshot predates 3D-printed+audio overlays, so LucentMaps is the canonical example of the technology Rowell's era lacked.
- [[Brock_2015_InteractiveMapsUsability]] — bidirectional conceptual link: LucentMaps explicitly positions itself as the low-cost answer to Brock's commodity-but-still-expensive 22" multi-touch + PETG overlay stack.

### Conceptual Links (not citation-based)

**Cost / consumer-production feasibility:**
- [[Taylor_2016_Customizable3DPrintedTactile]] — Strong. Both papers, at the same 2016 venue, argue that consumer 3D printing plus commodity touchscreens can replace bespoke audio-tactile hardware. Taylor's approach uses an opaque 3D-printed overlay with interactive input via conductive ink; Götzelmann uses translucent PLA with passive capacitive markers. Convergent finding from two independent groups: consumer FDM is the practical 2016 substrate for personalized accessible cartography.
- [[Brock_2015_InteractiveMapsUsability]] — Strong. Brock's raised-overlay-on-multitouch design is the immediate prior art LucentMaps explicitly targets for cost reduction. Same usability goal (audio-tactile interactive map for BVI users), different fabrication and registration strategy.

**Empirical gap this paper leaves:**
- [[Holloway_2018_AccessibleMapsBlindComparing]] — Strong. Holloway's later controlled comparison is exactly the empirical study LucentMaps's n=5 feasibility study does not provide. Reading Holloway's finding ("no strong effectiveness difference across 3D vs 2D tactile media") alongside LucentMaps's cost numbers is the key synthesis for the review's transferability question.
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — Moderate. Same-year companion on multi-sensory accessible maps; useful as a design-space anchor across venues (CHI vs ASSETS).

**O&M transfer:**
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — Moderate. Papadopoulos provides the real-environment O&M baseline that LucentMaps's lab feasibility study would need to be validated against.

**Tactile map design constraints:**
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Moderate. Wabinski's later standardization guidelines are the backdrop against which LucentMaps's ~20 μm minimum feature width and dense-block readability failures (Fig. 6) should be evaluated.
- [[Gual_2015_EffectVolumetric3DTactile]] — Moderate. Gual 2015 (Applied Ergonomics 48:1-10) reports that 3D-printed ABS volumetric point symbols on a swell-paper base cut location time and error counts for blind users versus flat swell-paper-only symbols. Götzelmann cites Gual in passing (citations.md ref [22]) as prior art for PLA volumetric tactile signs; LucentMaps extends the same volumetric-symbol idea with an embedded audiovisual (translucent + CapCode) channel on commodity smartphones. Gual is the tactile-only empirical ancestor; LucentMaps is the audiovisual 3D-printed successor.
- [[Perkins_2002_CartographyProgressTactileMapping]] — Moderate. Perkins's historical review of tactile cartography progress is the pre-3D-printing baseline LucentMaps advances beyond.

**Inclusive-cartography review pipeline:**
- [[Wabiski_2026_CognitiveReviewProtocol]] — Strong. LucentMaps is exactly the kind of n=5 feasibility paper the review protocol's confidence-threshold critique needs as a counterexample: a high-impact, well-cited, reproducible design paper whose empirical evidence is qualitative and small-sample, and which would be scored low by any accuracy-focused LLM screener despite being central to the tools/technologies research question.

