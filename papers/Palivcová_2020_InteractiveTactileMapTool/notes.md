---
title: "Interactive Tactile Map as a Tool for Building Spatial Knowledge of Visually Impaired Older Adults"
authors: "Dominika Palivcová, Miroslav Macík, Zdeněk Míkovec"
year: 2020
venue: "CHI 2020 Extended Abstracts (Late-Breaking Work), April 25-30, 2020, Honolulu, HI, USA"
doi_url: "https://doi.org/10.1145/3334480.3382912"
affiliation: "Czech Technical University in Prague"
pages: 9
note: "Paper ID LBW039. Spec label used 'Daniela Palivcova' but the PDF gives 'Dominika Palivcová' — dir and citation use the correct first-author name."
---

# Interactive Tactile Map as a Tool for Building Spatial Knowledge of Visually Impaired Older Adults

## One-Sentence Summary
An interactive tactile map of a complex indoor environment (a residential care home), tailored for visually-impaired older adults (mean age 81.4), combines haptically salient key objects, large touch-sensitive segments, and an audio route-guidance mode to help users acquire survey and route knowledge of a previously unknown indoor space. *(p.1, 9)*

## Problem Addressed
- Visually impaired (VI) older adults are a largely ignored intersection: most accessibility research focuses on younger blind users, and most aging-in-place research ignores VI. *(p.1)*
- Acquired late-life vision impairment leaves many older adults without well-trained mobility strategies; white-cane / guide-dog / Braille / screen-reader approaches do not generalize to them. *(p.1)*
- When VI older adults move into a residential care home, they must learn a complex indoor environment that is novel to them; traditional tools (paper tactile maps, large-print maps, GPS outdoor apps, ultrasonic / shoulder-worn aids) are either unusable or unsuited to indoor navigation at the scale of a care home. *(p.1, p.2)*
- Prior digital tactile map work (audio-haptic / interactive overlays, 3D-printed tactile maps, pin-array refreshable displays, vibrotactile smartphone overlays) has generally targeted younger blind users and outdoor/public spaces, not the indoor care-home use case. *(p.2)*

## Key Contributions
- **A specific tactile map design** for a complex indoor environment (residential care home), with haptically salient key objects (landmarks) and large touch-sensitive segments (rooms/corridors). *(p.1, p.3)*
- **Route-guidance function**: an audio mode that, after a user selects start and destination rooms, reads the route step-by-step so that users acquire route knowledge in addition to survey (layout) knowledge. *(p.1, p.4, p.5)*
- **Iterative user-centered design process** with three prototype generations (V0 paper map, V1 with QR/NFC on screen, V2 final prototype) co-designed with VI older adults. *(p.2, p.3)*
- **Qualitative evaluation with 10 VI older adult participants** (mean age 81.4) in two sessions (familiarization + route-guidance), showing the concept helps them build spatial knowledge of an indoor environment. *(p.1, p.4, p.5, p.6)*
- **Design guidelines / feedback catalog** for tactile indoor maps targeted at VI older adults: tactile symbol choice, scale, route-guidance phrasing, audio properties, physical map properties (see Testable Properties section). *(p.5, p.6)*

## Study Design (empirical papers)
- **Type:** Qualitative, iterative user-centered design with an in-situ evaluation of the final prototype (small-N formative study, no statistical inference). *(p.2, p.3, p.4)*
- **Population:** 10 VI older adults living in a residential care home, age 62-87, mean age 81.4, 5 female / 5 male. Severity: P1 mild; P2 RD (A); P3 BL, LC, MY (A); P4 MY (C); P5 EG (A); P6 DR (A); P7 RD (A); P8 EG (A); P9 RD (A); P10 BL (F). (Category A = partial sight; F = total blindness; see Table 1 abbreviation list: RD = retinal detachment, MY = myopia, BL = blind, LC = lens clouding, DR = diabetic retinopathy, EG = eye globe loss, CAT = cataract.) *(p.4, p.5)*
- **Intervention(s):** Exposure to the V2 interactive tactile map for two tasks: (1) familiarization / free-exploration mode to build survey knowledge; (2) route-guidance mode to learn a specific path between two rooms. *(p.3, p.4, p.5)*
- **Comparator(s):** None (formative, within-subjects use of the prototype; no control condition). *(p.4)*
- **Primary endpoint(s):** Ability to build spatial knowledge (survey + route), observed user behavior and interviews; qualitative design feedback. *(p.4, p.5, p.6)*
- **Secondary endpoint(s):** Subjective ratings of the audio/tactile design and of the individual tactile symbols; usability obstacles; preferred interaction patterns. *(p.5, p.6)*
- **Follow-up:** Two evaluation sessions per participant; no long-term follow-up reported. *(p.4)*

## Methodology
- **Related work scan** of tactile map research for VI users (small-scale vs. complex layouts, paper vs. electronic overlay, refreshable displays, swell paper, 3D-printed overlays), and of mobility aids (white cane, guide dog, GPS/voice, ultrasonic, vibrotactile smartphone). *(p.1, p.2)*
- **Use-case definition**: residential care home as the target environment; VI older adults as the audience, with explicit acknowledgement that prior research omits them. *(p.2, p.3)*
- **Iterative design process**, three prototypes:
  - **V0**: paper tactile map with handmade symbols; exploratory sessions with 2 VI older adults yielded the key insight that a scale of ~1 cm per 1 m of reality (approx., i.e., 1:100 range) is usable. *(p.2, p.3)*
  - **V1**: larger fixed tactile map with QR/NFC markers and a smartphone overlay; evaluated with 10 experts + 5 VI older adults; provided early feedback on symbol legibility and interaction. *(p.2, p.3)*
  - **V2 final**: 3D-printed composite tactile map of the residential care home, with capacitive touch-sensitive segments corresponding to rooms/corridors, haptically salient key objects (landmarks), and an audio layer driven by a connected computer; supports two modes — free exploration and route-guidance. *(p.2, p.3)*
- **User-centered co-design**: decisions about tactile symbols, audio description wording, map size, and interaction style were made in collaboration with VI older adults. *(p.3)*
- **Final evaluation**: in situ at a residential care home; two sessions per participant (familiarization + route-guidance); semi-structured interviews; observation notes. *(p.3, p.4)*
- **Qualitative analysis** of observations and interviews to surface recurring usability and design issues; no statistical tests reported. *(p.5, p.6)*

## Key Equations / Statistical Models

### Demographics (reported summary statistics) *(p.3)*

$$
\bar{age} = 81.4 \text{ years}
$$
Where: $\bar{age}$ is the mean participant age across N = 10 VI older adult participants, computed as the arithmetic mean of the individual ages in Table 1. *(p.3, p.4)*

$$
SD_{age} = 8.6
$$
Where: $SD_{age}$ is the sample standard deviation of participant age. *(p.3)*

$$
\text{age range} = [62, 87]
$$
Where: minimum 62 years (P2), maximum 87 years (P7, P9). *(p.4)*

$$
N = 10,\ \; N_F = 5,\ \; N_M = 5
$$
Where: $N$ is total participants, $N_F$ female, $N_M$ male. *(p.3, p.4)*

### Map scale *(p.2)*

$$
s \approx \frac{1\ \text{cm on map}}{1\ \text{m in reality}} = 1{:}100
$$
Where: $s$ is the approximate cartographic scale chosen for V0 after exploratory sessions — a larger scale than conventional tactile maps, motivated by fingertip resolution and the physical size of tactile symbols for older adults with reduced tactile sensitivity. *(p.2)*

*No inferential statistical models appear; the paper is qualitative and formative.*

## Parameters

### Participant demographics (population-level)

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Number of participants | N | — | 10 | — | 3, 4 | Final evaluation sample. |
| Mean age | $\bar{age}$ | years | 81.4 | — | 3 | VI older adults in a residential care home. |
| Age standard deviation | $SD_{age}$ | years | 8.6 | — | 3 | Reported in §Evaluation. |
| Age minimum | — | years | 62 | — | 4 | P2. |
| Age maximum | — | years | 87 | — | 4 | P7, P9. |
| Female participants | $N_F$ | — | 5 | — | 3, 4 | 5F / 5M balanced. |
| Male participants | $N_M$ | — | 5 | — | 3, 4 | — |

### Per-participant table (reproduction of Table 1) *(p.4)*

| ID | Age | Gender | Diagnosis | Category | Notes |
|----|-----|--------|-----------|----------|-------|
| P1 | 82 | Female | mild (age-related) | A | Grey stain in left eye. |
| P2 | 62 | Female | RD (A), CAT (A), MY (A) | A | No spatial perception, only light/dark; no ability to distinguish colors. |
| P3 | 86 | Female | BL, LC, MY | A | Dark shadows, shrinking field of view. |
| P4 | 86 | Female | MY (C) | A | Can see color. |
| P5 | 83 | Female | EG (A) | A | Sees colors from a distance. |
| P6 | 52 | Male | DR (A) | A | — |
| P7 | 87 | Male | RD (A) | A | — |
| P8 | 83 | Male | EG (A) | A | Total blindness (one eye enucleated); no light perception on affected side. |
| P9 | 87 | Male | RD (A) | A | — |
| P10 | 86 | Male | BL total blindness | F | Total blindness; can see "everything" in his own words (metaphor). |

**Abbreviations (per Table 2):** MP = Methylprednisolone; A = Advanced; C = Congenital; F = Self-reported (total blindness); *additional entries*: Leftsight, Rightsight, RD = Retinal detachment, MY = Myopia, BL = Blindness, EG = Eye globe (enucleation), LC = Lens clouding (cataract-related), DR = Diabetic retinopathy, CAT = Cataract, Glasses. *(p.5, Table 2)*

*Table 2 lists “self-description of their visual condition” per participant; because the LBW layout used tight abbreviations, some categories are coarse approximations.*

### Map / device parameters

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Map cartographic scale | $s$ | — | 1:100 (≈ 1 cm/m) | — | 2 | Selected in V0 after exploratory sessions; larger than conventional. |
| Number of prototype generations | — | — | 3 | V0, V1, V2 | 2, 3 | Paper → QR/NFC overlay → final composite 3D-printed map. |
| V2 touch-sensitive segments | — | — | per room/corridor | — | 2, 3 | Large capacitive areas, one per room and corridor. |
| Key objects (landmarks) | — | — | several per floor | — | 2, 3 | Haptically salient 3D shapes placed on map. |
| Modes | — | — | 2 | {free exploration, route guidance} | 3, 4, 5 | Mode switch on device. |
| Number of use-case sessions per participant | — | — | 2 | — | 4 | Session 1 = familiarization; Session 2 = route-guidance. |

## Effect Sizes / Key Quantitative Results

| Outcome | Measure | Value | CI | p | Population/Context | Page |
|---------|---------|-------|-----|---|--------------------|------|
| Mean age of participants | Mean | 81.4 yrs | — | — | VI older adults in care home | 3 |
| SD of age | SD | 8.6 yrs | — | — | Same | 3 |
| Age range | Range | 62–87 yrs | — | — | Same | 4 |
| Gender balance | Ratio | 5F/5M | — | — | Same | 3, 4 |

*No statistical tests, inferential effect sizes, confidence intervals, or p-values are reported. Findings are qualitative observations from interviews and task observation.*

## Methods & Implementation Details
- **Target environment**: a residential care home selected as the reference complex indoor environment; the map was physically built to represent this specific home. *(p.2)*
- **Three iterative prototypes**:
  - **V0 – paper tactile map** with handmade symbols; evaluated with 2 VI older adults in free exploration; surfaced the scale requirement (~1 cm/1 m) and the need for tactilely distinctive landmarks. *(p.2, p.3)*
  - **V1 – enlarged tactile map with smartphone overlay**; evaluated with 10 sighted experts and 5 VI older adults; triggered audio information about rooms via QR codes / NFC tags placed at symbol locations. Provided data on symbol legibility and interaction patterns. *(p.2, p.3)*
  - **V2 – final interactive tactile map**: 3D-printed base layer with large capacitive touch-sensitive segments (rooms, corridors) and haptically salient key objects (landmarks); a connected computer plays synthesized audio via speakers/headphones. Modes: (a) free-exploration / familiarization mode, which reads the label of the touched segment or object; (b) route-guidance mode, which guides the user step-by-step from a chosen start to a chosen destination. *(p.2, p.3, p.4, p.5)*
- **Tactile symbol design**: two classes — (i) "key objects", small 3D shapes (landmarks) meant to be immediately distinguishable by touch; (ii) "large touch-sensitive segments" corresponding to rooms/corridors, designed to be disambiguable by area shape and location. Figure 1 shows a selection of symbols (e.g., Stairs, Hallway-1, Doors, interactive symbol for the room, room buttons (when pushed for audio), "Culture Room"). *(p.2)*
- **Audio layer**:
  - Text-to-speech of segment labels and route instructions.
  - Volume control and adjustable speech rate were discussed with participants; some participants asked for slower speech; others for faster. *(p.5, p.6)*
  - In route-guidance mode the instructions were phrased in a first-person, step-by-step manner.
- **Interaction protocol for route-guidance mode** (conceptual pseudo-code):
  1. User selects starting room by touching its segment.
  2. User selects destination room.
  3. System computes and verbalizes the route as an ordered sequence of directives (turn left/right, follow corridor X, pass landmark Y) synchronized with tactile landmarks on the map.
  4. User traces the route on the map with a finger while listening.
  5. Free re-play or step-back supported on user request.
  *(p.4, p.5)*
- **Familiarization protocol**:
  1. User freely explores the tactile map.
  2. Touching a segment or landmark triggers its audio label.
  3. User builds survey knowledge (layout of rooms, corridors, and landmarks). *(p.4, p.5)*
- **Evaluation procedure**: in situ at the care home; observers took field notes; semi-structured interview after each session probing comprehension, preferred symbols, audio preferences, and subjective difficulty. *(p.4, p.5)*
- **Compensation**: participants were informed volunteers (formal ethical acknowledgments at end of paper). *(p.6)*

## Figures of Interest
- **Figure 1 (p.2):** Tactile symbol legend with examples: Stairs (staircase icon), Hallway-1 (linear corridor segment), Doors, an interactive room symbol, pushable room buttons, and a "Culture Room" symbol. Used to illustrate tactile symbol classes.
- **Figure 2 (p.3):** Advanced V2 prototype with route-guidance mode turned on. Shows participant interacting with the 3D-printed composite map that has touch-sensitive segments and physically distinct landmarks. *(p.3)*
- **Figure 3 (p.4):** Photograph of setup of the user-study with the advanced V2 prototype at the care home. *(p.4)*
- **Table 1 (p.4):** Demographic information of the 10 participants, including age, gender, diagnosis, and category. *(p.4)*
- **Table 2 (p.5):** Participants' self-descriptions of their visual condition and abbreviation legend. *(p.5)*
- **Table 3 (p.6):** Participants' self-description of their visual condition and acknowledgments table. *(p.6)*

## Results Summary
- **Survey-knowledge acquisition**: The advanced prototype's familiarization mode enabled participants to build a mental layout of the care home they had not previously known in detail; users could identify key rooms (dining room, culture room, their own room, bathroom) by their tactile footprint and audio label. *(p.5)*
- **Route-knowledge acquisition**: In route-guidance mode, participants were able to follow guided routes between chosen start and destination rooms; most successfully described the path after the session. One participant remark indicated real utility: *"But I could not focus on anything but the route-guidance mode was perceived correctly."* (paraphrased summary from p.5). *(p.5)*
- **Tactile symbol feedback**:
  - Large touch-sensitive segments were clearly locatable and distinguishable, but some participants had trouble agreeing on the meaning of individual tactile icons (e.g., distinguishing certain door symbols). *(p.5, p.6)*
  - Haptically salient key objects were the most useful reference anchors ("landmarks") for orientation — several participants used them as mental pegs for route-guidance instructions. *(p.5)*
  - Several design lessons: tactile symbols should be large and tactilely contrasted; border thicknesses matter; rounded corners are easier; coupling each symbol with distinct audio labels amplifies learning. *(p.5, p.6)*
- **Audio feedback**:
  - Participants generally found synthesized audio useful; some requested higher volume and slower speech rate, while others preferred faster playback. *(p.5, p.6)*
  - Audio should be adjustable per user (speech rate, volume) and offered through speakers or headphones. *(p.5, p.6)*
  - Route-guidance instructions should be phrased in plain, first-person, step-by-step form; ambiguous spatial references (e.g., "turn right") need to be anchored to tactile landmarks on the map. *(p.5, p.6)*
- **Physical / ergonomic feedback**:
  - Map should be held in a stable position (non-slipping) so the user can work with both hands. *(p.5, p.6)*
  - Size: large enough for visible and haptic resolution but small enough to reach all segments without straining; a single care-home-level map fits on a table. *(p.5, p.6)*
  - Weight and portability tradeoff: fixed tabletop placement preferred by most, but some wanted a portable version. *(p.5, p.6)*
- **Conclusion from the authors**: the prototype meaningfully supports building spatial (both survey and route) knowledge for VI older adults in a complex indoor environment, and provides concrete guidelines for follow-up work. *(p.6)*

## Limitations
- **Qualitative, small-N, no control condition**: N = 10, no statistical tests, no comparison against other tactile maps or audio-only guidance. *(p.4, p.6)*
- **Mean age 81.4 with wide variance**: findings may not generalize to all VI older adults; one participant (P6) was much younger (52), shifting the average only slightly. *(p.4)*
- **Non-homogeneous impairment levels**: most participants were category A (advanced partial sight) rather than total blindness; the single totally-blind participant (P10) may not represent the broader blind population. *(p.4, p.5)*
- **Single residential care home**: the environment is the actual home the participants live in; this biases evaluation because some participants already had partial mental models of the space. *(p.4)*
- **No long-term retention or transfer measurement**: authors did not test whether the spatial knowledge acquired via the map translates into actual safer / more independent navigation in the home over days/weeks. *(p.6)*
- **Tactile symbol interpretation was not consistent across participants**: some symbols were misread or confused — indicating that the symbol set needs standardization and training. *(p.5)*
- **Audio delivery variability**: participants disagreed on ideal speech rate and volume; the prototype did not fully personalize these. *(p.5, p.6)*
- **No formal cognitive-assessment control**: older age can entail mild cognitive decline which confounds the spatial-knowledge task; the authors did not screen for MoCA/MMSE or similar. *(p.4, p.6)*

## Arguments Against Prior Work
- **Current research largely omits VI older adults**: "Interestingly current research largely omits visually impaired older adults" — the paper calls out that accessibility research concentrates on younger blind users and on mainstream older users without VI. *(p.1)*
- **Traditional paper tactile maps have usability issues for older VI users**: small scale and fine-grained tactile detail of standard tactile maps are not legible to older fingertips; V0 exploration confirmed the need for a much larger scale (~1 cm/1 m). *(p.2)*
- **Refreshable pin-array / graphical displays are expensive and complicated**: prior interactive tactile displays aimed at blind users rely on specialized hardware that is neither cost-effective nor familiar to older adults. *(p.2)*
- **Mobile device + tactile overlay designs require smartphone literacy**: prior work pairing tactile overlays with tablets/phones assumes interaction patterns (touch, swipe, screen reader) that older VI users rarely have mastered. *(p.2)*
- **Outdoor navigation aids (GPS, ultrasonic, vibrotactile body-worn) do not solve indoor care-home navigation** and do not build survey knowledge of building layout. *(p.1, p.2)*

## Design Rationale
- **Choice of residential care home**: chosen because it is a complex indoor environment where VI older adults genuinely need orientation support; the authors want to match the audience's real environment rather than a generic public building. *(p.2)*
- **Tactile map + audio rather than audio-only**: tactile modality gives a persistent spatial layout that the user can revisit; audio alone provides instructions but no spatial anchoring. The combination supports building both survey (layout) and route knowledge. *(p.1, p.2)*
- **Large segments + salient landmarks** instead of fine tactile patterns: chosen because older fingertips have reduced tactile sensitivity; a large touch area is easier to locate and a haptically distinctive landmark is easier to remember than a fine symbol. *(p.2, p.3)*
- **Route-guidance mode in addition to free exploration**: free exploration builds survey knowledge; guided mode builds route knowledge; both are needed because older adults often forget unassisted exploration and need reinforcement of actual paths. *(p.1, p.4, p.5)*
- **Iterative design with VI older adults** rather than with proxies (blind younger participants or sighted volunteers): authors argue the target audience's specific abilities and expectations cannot be inferred from surrogates. *(p.2, p.3)*
- **Capacitive touch with audio labels** chosen because QR/NFC (V1) required users to align a phone camera or scanner — difficult for VI older users. *(p.2, p.3)*
- **3D-printed composite fabrication**: 3D printing lets the authors fabricate both large touch-sensitive segments and small haptically distinctive landmarks in one piece, with repeatable production. *(p.2, p.3)*
- **Audio rate/volume adjustable**: acknowledged during design because participants varied in hearing ability and preferred pace. *(p.5, p.6)*

## Testable Properties
- **Scale property**: A tactile map for VI older adults targeting building-level indoor environments should use a scale of approximately 1 cm per 1 m of physical space (≈ 1:100), larger than conventional tactile maps. *(p.2)*
- **Landmark density**: Haptically salient landmarks should be placed at decision points (junctions, doorways, key rooms) so that audio route instructions can reference them. *(p.2, p.3, p.5)*
- **Symbol distinctness**: Each tactile symbol class should be distinguishable by shape alone, without requiring explicit label training; the V0-V1-V2 iterations progressively increased symbol contrast. *(p.2, p.3, p.5)*
- **Audio adjustability**: Speech rate and volume must be user-configurable per session; the paper reports divergent preferences and recommends per-user adaptation. *(p.5, p.6)*
- **Mode separation**: A VI older-adult tactile map should offer at least two modes, exploration (free touch → audio label) and guidance (turn-by-turn), with a clear switch between them. *(p.3, p.4, p.5)*
- **Ergonomic stability**: The map must rest in a stable, non-slipping orientation so users can touch it with both hands. *(p.5, p.6)*
- **Physical size bound**: The map must fit within reach of a seated user without requiring them to lean or walk to reach distant areas. *(p.5, p.6)*
- **Training-free usability bound**: First-use exploration should produce recognizable survey knowledge within a single familiarization session (authors' observation after Session 1). *(p.4, p.5)*
- **Route-learning bound**: After one guided session, users should be able to describe the taught route unaided — this was qualitatively observed for most participants. *(p.5)*
- **Population bound**: Findings apply specifically to VI older adults (mean 81.4 yrs, category A partial sight), not necessarily congenitally-blind users or younger VI adults. *(p.4, p.5)*

## Relevance to Project
This paper is a direct, domain-specific data point for inclusive cartography and tactile map research:
- It is one of very few studies focused on **older adults with vision impairment** (not just "blind users" in general), which matches the gap the inclusive-cartography review is highlighting.
- It provides a **concrete prototype and evaluation** of an interactive tactile map in a realistic complex indoor environment (care home) — useful as a benchmark design and a reference set of design guidelines.
- It gives **qualitative design feedback** (scale, symbol, audio, route-guidance) that can inform both the Wabiski_2026 cognitive review protocol and any downstream system-design claims about indoor VI navigation.
- It is a **late-breaking work (LBW)** rather than a full CHI paper, so claims should be flagged as formative and small-N when extracted into the propstore.
- The data enriches the project's discussion of **LLM-confidence thresholds** for inclusion: this paper has high topical relevance but low statistical power, so any automated scoring that weights statistical rigor alone would underrate it.

## Open Questions
- [ ] How does the 1:100 scale heuristic scale to larger environments (whole floor, multiple floors) and still remain within reach of a seated older user?
- [ ] What is the retention of the acquired spatial knowledge after days/weeks without refresher sessions?
- [ ] Would totally-blind older adults benefit similarly, or do they require different symbol/audio design (only 1 of 10 participants in this study was totally blind)?
- [ ] How well do the route-guidance instructions transfer from the tabletop map to actual walking through the real care home?
- [ ] What is the incremental benefit of the tactile layer beyond audio-only descriptions (no control condition in this study)?
- [ ] Does the interactive tactile map generalize to other complex indoor contexts (hospitals, shopping malls, transit hubs)?
- [ ] How should the tactile symbol library be standardized across care homes / buildings?

## Related Work Worth Reading
- Taylor et al. 2016, "Customizable 3D printed tactile maps as interactive overlays", ACM SIGACCESS — most direct predecessor on interactive 3D-printed tactile maps. *(ref [33], p.7, p.9)*
- Holloway et al. 2018, "3D printing tactile maps" (CHI 2018) — produced the tactile-map fabrication pipeline this work builds on. *(implied by cross-references and sci-hub tab title; confirm via citations.md)*
- Morash, Connell Pensky, Tseng, Miele 2014, "Effects of using multiple hands and fingers on haptic performance in individuals who are blind", Perception 43(6):569–588 — relevant to the "two-hand use" ergonomic property. *(ref [28], p.9)*
- Rowell & Ungar 2005, "Feeling our way: tactile map user requirements — a survey" — baseline user-requirements source. *(ref [30], p.9)*
- Ungar, Blades, Spencer 1993, "The role of tactile maps in mobility training", Br. J. Visual Impairment 11(2):59–61 — foundational reference on tactile maps for mobility. *(ref [34], p.9)*
- Wahl 2013, "The psychological challenge of late-life vision impairment", J. Ophthalmology — informs the older-adult-specific framing. *(ref [35], p.9)*
- Ward & Banks 2017, "Older people's experiences of sight loss in care homes" — contextualizes the target population. *(ref [36], p.9)*
- Wijntjes, van Lienen, Verstijnen, Kappers 2008, "Influence of picture size on recognition and exploratory behaviour in raised-line drawings" — directly supports the scale/size discussion. *(ref [37], p.9)*
- Siekierska et al. (Atlas for VI) and Espinosa et al. 1998 "Comparing methods for introducing blind and VI people to unfamiliar urban environments" — prior art on introducing VI people to new environments. *(refs [11], [13], p.6, p.7)*
- Gual et al. 2015, "The effect of volumetric (3D) tactile symbols within inclusive tactile maps", Applied Ergonomics — directly related to symbol design choices in this paper. → NOW IN COLLECTION: [[Gual_2015_EffectVolumetric3DTactile]]

## Collection Cross-References

### Cited Papers Now in Collection
- [[Gual_2015_EffectVolumetric3DTactile]] — Palivcová et al. cite Gual 2015 (Applied Ergonomics 48:1-10) as the empirical basis for volumetric tactile symbol design choices. Gual's counterbalanced N=16 study compares flat microcapsule maps vs the same base with 3D-printed-ABS volumetric point symbols (3-8 mm) across three tasks (symbol ID, location without legend, location with legend), reporting reduced time and error counts on the 3D map especially for blind users. This underpins Palivcová's use of raised/volumetric symbols on the interactive tactile map tool for older adults with late-life vision impairment.

### Cited By (in Collection)
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — Brulé's reconciliation positions Palivcová as a later tool-oriented interactive tactile map system in the MapSense design tradition, inheriting the teacher/caretaker-authoring theme but targeting a different user population (older adults).
- [[Brock_2015_InteractiveMapsUsability]] — Brock's reconciliation lists Palivcová as a later interactive tactile map tool in the same design lineage Brock 2015 helped establish.
- [[Rowell_2003_WorldTouchResultsInternational]] — Rowell's reconciliation notes that Palivcová cites the 2005 Rowell & Ungar ICC user-requirements paper (successor to Rowell 2003's producer survey), forming the producer↔user Rowell & Ungar pair.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Wabinski's reconciliation notes Palivcová reports concrete numeric guidance (~1 cm/1 m scale, distinct tactile symbols, audio rate adjustability) for older-adult VI users in an indoor setting, extending Wabinski's parameter tables into the age/cognition axis Wabinski does not cover.
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — Papadopoulos's reconciliation links the two as a younger-adult↔older-adult pair: Papadopoulos established the audio-tactile-vs-verbal effect for younger BVI adults; Palivcová tests a related hypothesis in older-adult populations where tactile sensitivity and working memory differ.
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — Götzelmann's reconciliation lists Palivcová 2020 as a later interactive tactile map system building on LucentMaps-era design approaches.

### Conceptual Links (not citation-based)
- [[Gual_2015_EffectVolumetric3DTactile]] — Strong. Same design hypothesis ("volumetric symbols outperform flat for BVI tactile maps") operationalised at different life stages: Gual tests the hypothesis across the 14–74 age band with a mixed blind / visually impaired / sighted-blindfolded sample; Palivcová is specifically targeted at older adults with late-life vision impairment in care homes. Gual is the symbol-level empirical ground; Palivcová is the domain-specific interactive-prototype application.
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — Moderate. Both papers share a caretaker/teacher-authoring theme for interactive tactile maps, but Brulé targets VI children in classrooms while Palivcová targets older adults with late-life vision impairment in care homes. Different populations, same design pattern.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Moderate. Palivcová's age-adjusted parameters (larger symbols, slower audio) are the kind of population-specific adaptation that would need to sit alongside Wabinski's symbol-level invariants in any production-ready standard.
- [[Wabiski_2026_CognitiveReviewProtocol]] — Moderate. Palivcová is exactly the kind of small-N prototype paper the systematic-review protocol must decide whether to include or exclude — an edge case for the confidence-threshold rule.
- WHO 2018 ICD-11 — used as the definitional source for vision impairment categories. *(ref [29], p.9)*
