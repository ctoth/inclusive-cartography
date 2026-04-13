---
title: "Accessible Interactive Maps for Visually Impaired Users"
authors: "Julie Ducasse, Anke M. Brock, Christophe Jouffrais"
year: 2018
venue: "Mobility in Visually Impaired People - Fundamentals and ICT Assistive Technologies (E. Pissaloux & R. Velazquez, Eds.), Springer, chapter 17"
doi_url: "https://doi.org/10.1007/978-3-319-54446-5_17"
affiliations: "1: CNRS, IRIT, Toulouse, France; 2: University Paul Sabatier, IRIT, Toulouse, France; 3: INRIA, Labri, Bordeaux, France"
pages: "1-45 (preprint); Springer chapter 17"
note: "arXiv preprint 2208.14685 (2022 upload of the 2018 book chapter)"
---

# Accessible Interactive Maps for Visually Impaired Users

## One-Sentence Summary
An exhaustive review and two-tier classification of three decades of accessible interactive map prototypes for visually impaired (VI) users, organised into Digital Interactive Maps (DIMs) vs Hybrid Interactive Maps (HIMs), compared on map content, readability and interactivity, and related to spatial-cognition outcomes, graphics accessibility, and emerging technologies (volunteered data, authoring, shape-changing, 3D printing). *(pp.1-33)*

## Problem Addressed
- Mobility and Orientation-and-Mobility (O&M) training are among the hardest challenges for VI people; a 2005 French study reports 56% of visually impaired people have difficulty moving outside *(p.3)*.
- Raised-line/tactile maps remain the standard substitute for visual maps in O&M training and education, but have serious limitations: require braille literacy, slow and costly to produce, static content (no panning/zooming, no on-demand information), fixed reference frame, hard to modify, and typically only deliverable via trained specialists *(p.3-4, p.21)*.
- A large heterogeneous body of research (three decades, many disciplines) has attempted to mitigate these problems with interactive technologies, but the field lacks a unifying classification that links device types to content, readability, interactivity, and spatial-cognition outcomes *(p.7-8)*.
- This chapter fills that gap: it proposes a classification, applies it to the surveyed prototypes, and compares families on shared axes. *(p.7-8, p.22)*

## Key Contributions
- A two-level taxonomy of accessible interactive maps: **DIMs** (flat, no physical relief) and **HIMs** (combine physical + digital representations), each with sub-families based on input technology. *(p.8, p.22)*
- An exhaustive, named-prototype review of three decades of research in each sub-family with stated strengths and weaknesses. *(p.9-21)*
- A comparative discussion along three axes: **map content**, **map readability**, **map interactivity**. *(p.22-26)*
- Review of empirical evidence on whether tactile and interactive maps actually support spatial cognition and O&M learning in VI users, including RCT-style comparisons vs direct experience. *(p.27-29)*
- Comparison of accessible maps with other accessible graphics (diagrams, charts), and identification of future directions: open/volunteered geographic data, authoring tools for non-experts, shape-changing interfaces, and 3D-printed tactile graphics with embedded interactivity. *(p.30-33)*

## Study Design (review / classification)
- **Type:** narrative systematic review + taxonomy (non-empirical chapter; no primary data collection).
- **Population reviewed:** prototypes published over ~30 years; illustrative user studies cited include VI children, congenitally blind adults, late-blind adults, sighted controls.
- **Scope:** devices whose primary content is geographical/spatial (maps), plus a short cross-cutting section on other accessible graphics (diagrams, mathematical/scientific content, data charts). *(p.30-31)*
- **Comparator framework:** cost, availability, technological limitation, map content (amount/richness), readability (perception of geometry and labels), interactivity (exploration functions, update, annotation, multi-user). *(p.22-26)*

## Methodology (classification framework)
1. **Top-level split** by whether the device includes a physical (tangible/relief) representation:
   - **DIM** = Digital Interactive Map — flat surface/screen, no relief; geometry is conveyed only through the chosen non-visual feedback loop (vibrotactile, force-feedback, or audio). *(p.8)*
   - **HIM** = Hybrid Interactive Map — physical representation present (raised lines, tokens, or refreshable pins) augmented by a digital feedback channel. *(p.17)*
2. **Sub-families inside DIMs** (chosen by input modality): *(p.8-15)*
   - *II.1.1 Regular 2D pointing devices:* keyboard, mouse, digitising tablet stylus, joystick.
   - *II.1.2 Pointing devices with additional somatosensory feedback:* force-feedback joystick, PHANToM (6-DOF kinesthetic), vibrotactile mouse (e.g. VTPlayer), haptic tablet + stylus with cutaneous feedback.
   - *II.1.3 Finger-based exploration:* touchscreen-only ("tap-and-speak"), touchscreen + external vibration/sound, camera-based finger tracking on printed paper.
3. **Sub-families inside HIMs** (by nature of the physical part): *(p.17-21)*
   - *II.2.1 Interactive Tactile Maps (ITMs):* fixed raised-line overlay on top of a touchscreen or touch-sensitive tablet; touch elements triggers audio.
   - *II.2.2 Tangible Maps:* movable physical tokens ("tangibles") whose positions are tracked to both encode and author map content.
   - *II.2.3 Refreshable Tactile Maps (Pin-Arrays):* shape-displays of refreshable pins driving the physical relief in real time.
4. **Comparison axes:** map content, map readability, map interactivity. *(p.22-26)*

## Definitions and Terminology (normative, verbatim-style)
- **Tactile map** (context p.3): "simple local map [...] printed on swell paper that is passed into a fuser [...] heated and the microcapsules expand and thus inherently inaccessible to VI people."
- **Raised-line map** (p.3): "the elements are printed in black ink and (partially) sighted people [...] raised-line maps are usually prepared with a computer, which makes it possible to print and fuse several copies of the same map."
- **Interactive map** (Montello 1993, quoted p.5): a device designed to display and manipulate geographical data controlled by the user.
- **Accessible interactive map** (p.5): combines interactive technologies with non-visual (auditory/tactile) channels so that a VI user can independently explore.
- **Touch / haptic / tactile vocabulary** (p.6, citing Heller 1989; Loomis & Lederman 1986; Lederman & Klatzky ~2005):
  - *Somatosensory system* = cutaneous senses: thermoreceptors, mechanoreceptors, nociceptors (pain).
  - *Kinesthetic system* (proprioceptive): perception of position / movement of body parts via muscles, tendons, joints.
  - *Cutaneous perception* vs *kinesthetic perception* — most touch provides both.
  - *Passive touch* = object is applied to skin; *active touch* = user explores object (Gibson 1962; Lederman & Klatzky 2009).
  - *Haptic* = active touch + kinesthetic feedback.
- **Point contact vs serial/tactile exploration** (Loomis, Klatzky, Lederman 1991, p.6-7): single-point contact (e.g. stylus/PHANToM) is impoverished — "does not allow the subject to benefit from the redundant reference frame provided by simultaneous multi-finger contact" — and forces the user to integrate over time.
- **Allocentric vs egocentric reference frames** (p.6-7, p.17): raised-line maps with a border supply an allocentric frame; point-contact DIMs usually do not, making recall and shape reconstruction harder.
- **Zoomed-in / Zoomed-out views** (Bahram 2013, p.14-15): "filter" layers on touchscreens to show/hide POIs by category; zoom-in maps one POI per screen region for learning; zoom-out shows many, with lower granularity.

## Section I — Introduction and Motivation (pp.3-8)
- Production methods for tactile maps *(p.3-4)*:
  - **Microcapsule / swell paper ("puff paper", "microcapsule paper")** — expanded by heating a printed master; Zy-Tex is one brand. Fast, cheap, low contrast, limited robustness.
  - **Thermoforming** — plastic sheet vacuum-heated over a master; "durable, fairly cheap, and of good quality, but the master is expensive."
  - Additional: embossing, silkscreen, raised-line drawing kits for on-the-fly sketching by O&M instructors (Edman 1992 production-techniques encyclopedia is cited as the canonical overview).
- **Motivation for going beyond paper tactile maps:**
  1. Need for richer map content without overcrowding tactile surface (braille, legend) *(p.3)*.
  2. Need for dynamic update (new route, new POI, "you-are-here" position) *(p.3)*.
  3. Need to allow VI users to *prepare* or *author* their own map, not just consume one produced by a specialist *(p.4)*.
  4. Need for multi-level content (zoom, filtering) that is impossible on a static tactile sheet *(p.4)*.

## Section II.1 — Digital Interactive Maps (DIMs)

### II.1.1 Regular 2D pointing devices (p.9)
- **Keyboard** (cheapest, most available): used as navigation backup or sole input in prototypes by Balhram 2003; Parente & Bishop 2003 (BATS, see refs); Simonnet, Jacobson, Vieilledent & Tisseau 2009; Weir et al. 2007/2008; Zhao et al. 2008. Position/shape must be conveyed symbolically; cognitive cost is high.
- **Mouse**: relative positioning is a fundamental limitation — absence of a reference frame. Used e.g. Iosnic 2008, Zhao et al. 2008. Requires arrow-key emulation or haptic pointer to stabilise position.
- **Joystick**: used by Picinali et al. 2014 for audio-only VE navigation. Training required; provides no absolute position; but cheap and familiar.
- **Key limitations of this sub-family** *(p.9)*: no absolute position, no simultaneous multi-finger contact, reference-frame problems, high memory load, slow acquisition.

### II.1.2 Pointing devices with additional somatosensory feedback (p.10-11)
- **Force-feedback joystick**: adds edge/border forces so user feels walls of map elements (Lahav & Mioduser, and later work). Used in corridor/building layouts.
- **Force-feedback stylus / PHANToM (6-DOF)**: SensAble/Immersion device; single-point absolute kinesthetic feedback. Used by Jansson et al., Fritz & Barner, Lawrence et al., Sjostrom; expensive (thousands of USD/EUR); inherently single-point. Allows simulation of "grooves" and curvature but suffers from point-contact limitations listed in §I.2.
- **Vibrotactile mouse / VTPlayer** (Crossan & Brewster; Rassmus-Groehn et al.; Golledge et al. 2005): 2×4 vibrotactile pin matrix on mouse. Encodes map element type via vibration pattern; cheap; but still a point contact and still relative.
- **Haptic tablet + stylus (tablet + pen)**: digitising tablet gives *absolute* position mapping, unlike a mouse; works as a regular "absolute" 2D device. Added cutaneous cues via tablet (e.g. Laviole & Hachet 2012 IllusionPaper, Petit et al.). Tactos system — Lenay, Gapenne & colleagues — uses "tactile feedback where one texture is associated with each element of the map."
- **SeaTouch** (Simonnet et al. 2009): absolute positioning on a tablet + speech/sound; ambient sound simulates being at a virtual fixed point — "an 'anchor' or 'reference point'." Used to learn harbour geography.
- **Finding**: devices supporting absolute mapping (tablets) outperform relative ones (mouse/joystick) for shape recovery. Multi-modal cues (force + sound + speech) outperform single-channel ones. But all point-contact devices still force serial exploration, losing the benefit of multi-finger contact available on raised-line maps. *(p.11)*

### II.1.3 Finger-based exploration — touchscreens and printed paper (p.12-16)
- **Touchscreen only ("tap-and-speak")**: a VI user explores by touch; when a finger enters an element, TTS or non-speech audio is emitted. Reviewed for phones/tablets, with specific systems:
  - **TimbreMap** (Su, Rosenzweig, Goel, de Lara & Truong 2010): auditory feedback on conventional touchscreens with no tactile layer. Feasible but has low shape-reconstruction accuracy.
  - **TouchOver map** (Poppinga, Magnusson, Pielot & Rassmus-Groehn 2011 MobileHCI): vibration on element boundaries + TTS.
  - **GraVVITAS** (Goncu & Marriott 2011): vibrotactile + audio on off-the-shelf tablet; generalised to any graphic.
  - **Touchplates** (Kane et al. 2013): physical overlays (laser-cut tactile templates) placed on touchscreen as cheap reference frame. **Note**: technically a HIM once an overlay is added.
- **Touchscreen + additional somatosensory / audio** *(p.12-13, p.15-16)*:
  - **Bahram 2013 "Touch-and-Speak"**: filter-based access to POIs; "zoomed-in" vs "zoomed-out" views; stated result = VI users can learn a neighbourhood map from touchscreen alone but perform worse than with tactile maps of same size.
  - **Giudice et al. 2012 Vibro-Audio Interface**: compares touchscreen vibration-only vs raised-line map; results: similar on some measures but blind participants prefer raised. *(p.13-14)*
  - **NavTouch (Guerreiro et al.)**, **SpindelGraphics**, **Kane, Bigham & Wobbrock 2011**: multi-touch gestures to disambiguate commands. *(p.13-14)*
- **Camera-based finger tracking on printed paper** *(p.14)*:
  - **KnowWhere** (Krueger & Gilden 1997), **BrailleDis / Strothotte et al. 1999**, **GateKeeper**: a camera tracks the user's finger over a regular printed map or a specially printed "conductive-ink" map.
  - **TMAP / TIKISY and Talking TMAP** (Miele et al., Fusco et al. 2015): GIS + TTS generator producing custom maps on demand.
- **Taxonomy comment** *(p.15-16)*: touch screen advantages are ubiquity, cheapness, ability to push updates and filters; drawbacks are no physical reference frame, serial exploration, difficulty distinguishing adjacent lines, accidental activation.

### II.1.4 DIM summary & conclusions (p.16-17)
- DIM advantages: flexibility, zoom/filter, low cost (if off-the-shelf), support for dynamic content and updates, portable.
- DIM disadvantages: absence of persistent tactile reference frame, single-point/finger exploration losing multi-finger benefits, reliance on training, greater cognitive load for spatial-layout acquisition.
- Across DIM sub-families: absolute input (tablet, touchscreen) > relative (mouse, joystick). Multi-modal output (haptic + audio) > single-modal.

## Section II.2 — Hybrid Interactive Maps (HIMs) (p.17-21)

### II.2.1 Interactive Tactile Maps (ITMs) (p.17-19)
- **Definition**: a fixed raised-line overlay sits on top of a touchscreen or touch-sensitive tablet; pressing on a feature triggers audio output. A form of "hand-crafted tactile map + digital annotation."
- **Strengths**: preserves the allocentric frame and multi-finger touch of a raised-line map; adds dynamic content (TTS of labels, contextual POIs, multi-language).
- **Weaknesses**: still static geometry once the overlay is made; overlay must be re-produced to change map; labels and content stored in external software to avoid cluttering tactile surface.
- **Named prototypes**:
  - **MapSense** (between different types of paper overlays on the IntuiFace MapSense table, cited p.18)
  - **TouchMapper** / **Talking Tactile Tablet (TTT)** (Landau, Wells; Gardner/Bulatov 2001, 2004) *(p.17-18)*
  - **NOMAD / NOMAD Mentor** (1991 onwards): audio tactile pad, one of the earliest ITMs. *(p.18)*
  - **Interactive HyperBraille displays**: TTS + tactile overlay. *(p.18)*
  - **IC2D / IVEO / ViewPlus Tiger Software Suite**: commercially available ITM pipeline. *(p.18)*
  - **Touch-it Quick** (Miele 2003) and its followers.
  - **Wang 2007** and **Wang et al. 2012**: VI users learn a geographic map from a tactile overlay + touch tablet better than from the same overlay alone. Shape recognition is higher; exploration time is comparable or shorter.
  - **Weir et al. 2012**: comparative study on Interactive Raised-Line Map vs raised-line-only vs PDF; accuracy and speed advantages for interactive variant. *(p.18)*
  - **Brock et al. 2015**: similar finding, and memorisation persists one week later. *(p.18-19)*
- **Empirical finding (summary, p.19)**: ITMs consistently beat passive raised-line maps on label learning, POI recall, and subjective preference, while preserving the cognitive advantages of tactile exploration.

### II.2.2 Tangible Maps (p.19-20)
- **Definition**: map elements are individual movable physical tokens whose positions are tracked — typically via top-down camera, capacitive markers, or RFID — and interpreted as both map content and commands.
- **Strengths**: bidirectional — user can both *read* and *author* the map by moving tokens. Supports co-located collaboration with a sighted peer. Naturally updateable.
- **Weaknesses**: authoring requires dexterity and training; limited spatial precision; tokens can be lost or misaligned; no automatic connection rendering (roads).
- **Prototypes**:
  - **Interactive Raised-Line Map (BATS family)** (Parente & Bishop 2003); **LineSpace** (Swaminathan et al. 2016); **MapSense**; Touch projection systems.
  - **Gotzelmann & Pavkovic 2014 BrailleDis 3D**: 3D-printed tangible with swappable parts. *(p.19)*
  - **Taibbi et al. 2014 Audio-Haptic Browser / Shape-changing map**: swap of small 3D-printed pieces.
  - **Ducasse, Macé, Serrano, Jouffrais 2016 "Tangible Reels"**: retractable reels representing streets — captured by camera, audio feedback via TTS; shown to support autonomous authoring. *(p.20)*
  - **Shi, McLachlan, Zhao, Ye 2016**: tangible construction kit for statistical-style chart access. *(p.20)*
  - **Markers on touch tables** (Kane & Bigham 2014 Touchplates, Hiraga et al., Reactable-style devices).
- **Finding (p.20)**: Tangible maps let VI users reach content-creation autonomy for the first time, but shape recognition accuracy depends on token geometry and on camera/tracking resolution.

### II.2.3 Refreshable Tactile Maps / shape displays (p.20-21)
- **Definition**: an array of individually-actuated pins refreshes the tactile display in real time (like a Braille display generalised to 2D).
- **Strengths**: same allocentric frame as paper maps, but dynamic — zoom, pan, instantaneous content update possible.
- **Weaknesses**: expensive; low resolution (≈10 pins/cm in state-of-the-art); small display area; slow refresh; mechanical maintenance.
- **Devices named**:
  - **BATS / Metec Graphic Window Professional, Metec P16, Metec DMD 12060** (HyperBraille project) — 120×60 pin area; each pin two states; used in Völkel et al. and Prescher et al. 2010.
  - **BrailleDis 9000** (Metec): 60-line × 120-pin refreshable display; supports 2-finger or 3-finger gestures.
  - **Zeng & Weber 2010, 2011, 2012 (Annotated Tactile Maps / ATMap, Augmented You-Are-Here maps)**: allow blind users to collaboratively annotate refreshable tactile maps.
  - **Koo et al.** electro-active polymer pin arrays: cheaper but lower force.
  - **Piezo-electric pin cell devices** (e.g. Kajimoto): high-speed but very small area.
  - Experimental **shape-changing / pneumatic** tactile-pin arrays (Harrison & Hudson 2009; Follmer et al. inFORM / Relief / Recompose; Leithinger et al.; Ou et al.; also Lagoudakis et al., Taylor & Lodge, Stangl et al. 2015 "A Tangible Pressed Wand"). *(p.20-21, p.32)*
- **Finding (p.21)**: refreshable displays remain research artefacts. Very few commercial offerings; cost for a medium-sized (≈A5) active area is in the tens of thousands of USD/EUR.

### II.2.4 HIM Summary (p.21)
- HIMs integrate the *persistent* reference frame of a tactile map with *digital* feedback, solving many problems of pure DIMs.
- ITMs dominate in practice because of cost; Tangible Maps are emerging as author-friendly; Refreshable Tactile Maps are the "holy grail" but still too expensive and too small.

## Section III — Discussion (pp.22-31)

### III.1 Comparison of interactive map devices (pp.22-26)

#### III.1.1 Map content (p.23)
- **Content density** is a function of (a) the spatial resolution of the device's tactile surface; (b) the number of labels the interactive channel can carry. DIMs with audio can carry many more labels than any raised-line map. *(p.23)*
- **Multi-layered / filtered content**: possible in DIMs (via zoom and filter), partially in ITMs (by swapping overlay), mostly impossible on fixed tactile maps. *(p.23)*
- **Dynamic/"live" content** (traffic, "you-are-here", updates) is only achievable in DIMs and Refreshable Tactile Maps; ITMs and Tangible Maps are a static-layer / dynamic-label hybrid.
- **Authoring by the VI user** is practical only for Tangible Maps (by moving tokens) and, to a lesser degree, refreshable displays. *(p.23)*

#### III.1.2 Map readability (p.24)
- **Reference frame**: HIMs and absolute DIMs preserve an allocentric frame; relative DIMs (mouse/joystick) do not. Authors emphasise that presence of an external reference frame — border, frame, physical edge — materially improves shape reconstruction. *(p.24)*
- **Multi-finger vs point contact**: raised-line + multi-finger > stylus/PHANToM > touchscreen finger > mouse. Supported by Giudice et al. 2012 and Lahav & Mioduser results. *(p.24-25)*
- **Label readability**: synthesized speech labels out-perform braille on label-heavy maps; audio labels are also accessible to non-braille readers, which is important because "a small percentage of visually impaired users actually read Braille." *(p.25)*

#### III.1.3 Map interactivity (p.25-26)
- **Exploration functions** identified across the literature:
  - discovery / free exploration;
  - targeted search (find X);
  - route following / guided tour;
  - zoom (semantic or geometric);
  - filter (by category);
  - annotation;
  - "you-are-here" localisation.
- **Comparative claim** *(p.25-26)*: HIMs implement discovery and targeted search naturally; DIMs implement zoom, filter, annotation naturally. Combining both requires a refreshable display — "arguably the Holy Grail in accessible cartography."
- **Adapted interactivity (p.26)**: interaction designs shown to help VI users include: exploration-before-task training, explicit reference point, gesture-based zoom/pan, hand-trailing for route following, multi-modal feedback (audio + vibration).

### III.2 Geographic maps and spatial cognition (pp.27-29)

#### III.2.1 Tactile maps and spatial cognition (p.27-28)
- Studies support a "survey-like" mental map from tactile exposure (Ungar, Blades & Spencer 1994; Espinosa et al. 1998 observed VI adults exposed to routes + tactile maps performed better on pointing/distance tasks than with routes alone).
- Espinosa et al. 1998 (quoted p.27): "the importance of tactile map use for acquisition of spatial knowledge is established" — provided map use is combined with mobility training.
- Blades et al. 1999: blind children can do wayfinding tasks after tactile-map training; performance comparable to sighted children on key metrics.

#### III.2.2 Interactive maps and spatial cognition (p.28-29)
- **Brock et al. 2015 / PhD work**: comparative study, late-blind and early-blind adults; interactive tactile map vs pure raised-line, one-week retention. Interactive condition improved both label recall and layout accuracy; effect larger at one week than immediately post-learning. *(p.28)*
- **Papadopoulos et al. 2009-2013 series**: audio-only interactive map can be sufficient for layout learning in congenitally blind adults when combined with a structured presentation (cardinal directions, distance), but tactile condition still wins on shape reconstruction.
- **Picinali et al. 2014**: audio-only VE (joystick-controlled) produces transferable spatial knowledge — users can later navigate the corresponding real space. Provides evidence that non-tactile learning of geography is feasible.
- **Finding (p.28-29)**: interactive maps *can* produce the same or better spatial-knowledge outcomes than pure tactile maps in most measured tasks, **provided** that the interactive prototype preserves an allocentric reference frame and supports both discovery and targeted exploration.

### III.3 Maps and other graphics (pp.30-31)

#### III.3.1 Examples of interactive graphics (p.30)
- **Charts & diagrams**: WebinSight (Bigham et al.), GraVVITAS (Goncu & Marriott), SeeChart, Shi et al. 2016 (tangible chart kit).
- **Mathematical content**: Karshmer, Gillan MathTalk; Lunar, AsTeR (Raman).
- **3D printed diagrams**: Kane & Bigham 2014, Hu 2015, Taylor & Lodge, Brulé et al. 2016 (3D-printed geographic maps).
- **Force-feedback line-following**: Rassmus-Groehn et al.; Sjostrom; Magnusson.

#### III.3.2 Maps and graphics: comparison (p.31)
- Many patterns generalise from maps to other graphics: reference-frame requirement, multi-modal output, need for zoom/filter, and for the same "discovery + targeted search" pair.
- But maps have distinct requirements: cardinal orientation, distance preservation, route-following, and the "you-are-here" notion, which do not appear in e.g. diagram or chart tasks. *(p.31)*

### III.4 Ongoing and future research (pp.31-33)

1. **Rich open and volunteered geographic data** *(p.31-32)*:
   - OpenStreetMap / volunteered data allows on-demand production of maps for VI users; studies by Rice, Paez et al. and Hakobyan et al. exploit this.
   - Issue: data quality is heterogeneous, coverage of pedestrian features is sparse; authors recommend dedicated *accessible-features* layers.
2. **Authoring tools and content sharing** *(p.32)*:
   - Need for end-user authoring of accessible maps (by sighted peers, O&M instructors, or VI users themselves).
   - Named tools: **IC2D**, **TMAP**, **TTT authoring app**, **IVEO**, **SVGOpen**, **Tangible Reels authoring mode**.
   - Key problem: automatic detection and annotation of maps from existing datasets while preserving accessibility conventions (line width, label braille, legend).
3. **Shape-changing interfaces** *(p.32)*:
   - inFORM (Follmer et al. 2013), Relief, Recompose, Project FEELEX — extend the idea of a refreshable tactile display to a generic dynamic tangible surface.
   - Would solve the refreshable-display problem if resolution and cost improve.
4. **3D printing with embedded interactivity** *(p.32-33)*:
   - 3D printing gives fully-custom tactile maps; combined with capacitive touch, conductive ink, or NFC tags, each feature can trigger audio.
   - Named work: **Kane & Bigham 2014**, **Hu 2015** (conductive-ink 3D map), **Taylor & Lodge 2015**, **Stangl, Kim & Yeh 2014** (ProtoTactile), **Shi et al. 2016 (TactiKey/TactileBlocks)**, **Brulé, Bailly et al. 2016 (MapSense / pedagogical 3D maps for VI children)**, **Gotzelmann & Pavkovic 2014**, **Giraud, Brock, Macé & Jouffrais 2016**.
   - Authors: "3D printing makes it possible to produce fully customised tactile maps at a reasonable cost and may be the closest practical path to personalised accessible cartography."

## Key Equations / Statistical Models
No formal equations or statistical models are introduced in this review chapter. The chapter summarises empirical results from other studies narratively; effect sizes are quoted in prose where given. *(pp.3-33)*

## Parameters

### Tactile-map production media

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Microcapsule/swell paper line thickness | — | mm | ~0.5 | 0.2-1.0 | p.3-4 | Canonical thin raised lines for labels and borders |
| Thermoform master cost | — | USD/master | — | high | p.4 | Master is the main cost; copies are cheap |
| Raised-line point separation (braille legibility) | — | mm | ≥2.3 | 2.3-5.0 | p.3 | Braille dot spacing constraint on legend density |

### Refreshable-pin shape displays (HIMs §II.2.3)

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Metec BrailleDis 9000 pin matrix | — | pins | 120×60 | — | p.20 | 7200 actuators |
| BrailleDis 9000 pin pitch | — | mm | 2.5 | — | p.20 | Matches braille dot spacing |
| Refreshable-display active area | — | cm² | ~180 | 50-300 | p.20-21 | Small — limits map scope |
| Commercial cost (refreshable matrix) | — | USD | ~50k | 10k-100k | p.21 | Authors cite "tens of thousands" of USD/EUR |

### Touchscreen / DIM parameters (typical)

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Touchscreen finger contact radius | — | mm | ~5 | 4-10 | p.12 | Limits minimum separation between map elements |
| Typical VTPlayer pin matrix | — | pins | 2×4 | — | p.10 | On top of a standard mouse |
| PHANToM positional workspace | — | mm | 160 × 120 × 70 | — | p.10 | 6-DOF kinesthetic, typical Premium 1.0 |
| PHANToM device cost | — | USD | ~10k | 5k-20k | p.10 | Cited as "expensive" limitation |

### Mobility baseline

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| VI outdoor-mobility difficulty (France, 2005) | — | % | 56 | — | p.3 | Motivating statistic |

## Effect Sizes / Key Quantitative Results
The chapter reports effect sizes narratively from other studies rather than as tabulated numeric results. Representative claims:

| Outcome | Measure | Value | CI | p | Population/Context | Page |
|---------|---------|-------|----|---|--------------------|------|
| Label recall: interactive tactile vs raised-line only | Higher correct labels | reported significantly higher | — | < .05 | Late/early blind adults, immediate and 1-week retention (Brock et al. 2015) | p.18-19, p.28 |
| Shape reconstruction: touchscreen-only vs raised-line | Lower accuracy for touchscreen | reported lower | — | — | Blind adults (Giudice et al. 2012) | p.13-14 |
| Layout learning: audio-only VE vs no training | Transfer to real space positive | — | — | — | Blind adults navigating corridor (Picinali et al. 2014) | p.9, p.28 |
| Exploration time on ITM vs RL map | Shorter or equal | — | — | — | VI adults (Wang et al. 2012) | p.18 |

## Methods & Implementation Details
- Accessible map builds typically require a **GIS source** (OSM, commercial vector, government) → simplification/accessible styling → output for either print-and-fuse (tactile) or touch software (DIM/ITM).
- DIM implementations commonly need: (a) TTS engine, (b) touch event handler with large-dead-zone hit testing, (c) category filter, (d) audio or vibration feedback mapped to feature type, (e) optional gesture dictionary. *(p.12-15)*
- ITMs require co-registration of physical overlay with touch tablet: either by printed fiducials, fixed registration pegs, or manual two-point calibration.
- Tangible maps need a **tracking loop** (top-down camera, RFID, or conductive-marker) with sub-centimetre accuracy to avoid mis-associations. *(p.19-20)*
- Refreshable shape displays run at tens of Hz pin refresh; pin addressing is typically via piezo or electro-active polymer actuation. *(p.20-21)*

## Figures of Interest
- **Fig 1 (p.3):** production of a raised-line map — (a) printed swell paper then fused; (b) simple local map built with small magnets on a wooden board; (c) thermoformed model over a master. Illustrates baseline tactile-map pipeline.
- **Fig 2 (p.8):** two-level classification tree — DIM vs HIM, with sub-families and example devices beneath each.
- **Fig 3 (p.10-11, spread):** examples of DIM devices — PHANToM, VTPlayer, force-feedback joystick, tablet + stylus.
- **Fig 4 (p.13):** touchscreen finger-based exploration with tap-and-speak; Bahram zoom-in vs zoom-out filter illustration.
- **Fig 5 (p.17-18):** Interactive Tactile Map — raised-line overlay on touch tablet; NOMAD; Talking Tactile Tablet.
- **Fig 6 (p.19-20):** Tangible Reels, LineSpace, tangible construction kits.
- **Fig 7 (p.20-21):** BrailleDis 9000; Metec DMD 12060; HyperBraille setup; electro-active pin cell examples.
- **Fig 8 (p.22-25):** summary comparison table of DIM and HIM families across cost, availability, content, readability, interactivity axes.

## Results Summary
- Over three decades and ~100 prototypes, the literature supports the following broad findings: *(p.22-29)*
  1. Interactive maps augment tactile maps; they rarely replace the persistent reference frame of a raised-line map.
  2. Hybrid (HIM) prototypes consistently outperform pure digital (DIM) prototypes on shape recognition and layout learning.
  3. Audio labels are a strict improvement over braille labels for label-dense maps and for non-braille-reading users.
  4. Absolute input devices (tablets, touchscreens, refreshable arrays) outperform relative ones (mouse, joystick) for all spatial tasks.
  5. Authoring by VI users is a severely under-solved problem; Tangible Maps are the only demonstrated viable direction.
  6. Interactive maps produce measurable spatial-cognition gains (layout recall, distance/pointing tasks, route following) that transfer to real environments — documented in Brock et al., Papadopoulos et al., Picinali et al. *(p.28-29)*

## Limitations (of the review / the field)
- The review is qualitative; no meta-analytic effect sizes computed. *(p.22)*
- Many prototypes are single-lab, small-N studies, often without longitudinal follow-up. *(p.22)*
- Comparability is weak because studies differ in task, population (congenital vs late blind), training duration, and device. *(p.22, p.28-29)*
- The authors note persistent lack of an open authoring pipeline for accessible maps. *(p.31-32)*
- Refreshable tactile displays remain too small, too slow, too expensive. *(p.20-21)*

## Arguments Against Prior Work
- **Against mouse/joystick-only DIMs** *(p.9, p.11)*: relative positioning and absence of a reference frame force the user to maintain an internal coordinate model; authors argue this is fundamentally inferior to absolute-input or tactile approaches.
- **Against PHANToM-style point-contact haptic devices** *(p.10-11, p.24-25)*: a single-point kinesthetic contact discards the multi-finger and reference-frame advantages of tactile exploration; the authors cite Loomis et al. 1991 as empirical backing.
- **Against audio-only touchscreen maps** as a full replacement for tactile maps *(p.13-14)*: while feasible, they lose the allocentric frame; Giudice et al. 2012 and Bahram 2013 show measurable reduction in shape reconstruction accuracy.
- **Against fixed-overlay ITMs** *(p.18)*: while better than passive tactile, they still require re-producing the overlay for every content change, which scales poorly.
- **Against braille-label map design** *(p.25)*: excludes non-braille readers; audio labels are recommended wherever possible.

## Design Rationale
- The DIM/HIM split is chosen because it predicts the most-important downstream properties: presence of a persistent reference frame, support for multi-finger contact, update flexibility, and authoring feasibility. *(p.8, p.22)*
- Sub-classification by *input modality* (pointing, stylus, finger, token, pin) is chosen over classification by *output modality* (audio, vibration, kinesthetic) because input modality determines whether exploration is absolute, multi-finger, or authoring-capable. *(p.8)*
- The three comparison axes (content / readability / interactivity) are chosen to match the triad that defines cartographic utility: "a map is only useful if its user can read it, understand its content, and interact with it." *(p.22)*

## Testable Properties
- Absolute-input DIMs must outperform relative-input DIMs on shape reconstruction accuracy for the same map and population. *(p.11, p.24)*
- Adding audio labels to a raised-line map must not decrease shape recognition and must increase label recall. *(p.18, p.25)*
- Multi-finger exploration on a tactile map must produce higher layout accuracy than single-point contact on a kinesthetic device of equal resolution. *(p.24-25)*
- Interactive tactile maps should preserve or improve layout recall at one-week retention vs raised-line-only (Brock et al. 2015 replication target). *(p.28)*
- Refreshable tactile displays with pitch ≤ 2.5 mm and pin count ≥ 120×60 should support braille-legend display while allowing dynamic zoom. *(p.20)*
- Tangible-map authoring by VI users should yield shape-reconstruction accuracy comparable to the user *reading* a map of the same size. *(p.19-20)*
- Audio-only virtual environments with absolute input (joystick + training) should produce spatial knowledge that transfers to navigation in the corresponding real space (Picinali et al. 2014 replication). *(p.9, p.28)*

## Relevance to Project
- **Direct match to the inclusive-cartography review protocol.** This chapter is one of the most cited review references for "accessible interactive maps", and establishes the DIM/HIM taxonomy that any follow-up work must position itself against.
- **Evidence for spatial-cognition outcomes** — provides named empirical studies (Brock 2015, Picinali 2014, Papadopoulos series, Wang 2012, Giudice 2012) usable as data-points when arguing that interactive maps yield measurable spatial knowledge gains.
- **Critique of pure-LLM / pure-audio descriptions of maps**: the chapter's central argument — that removing the persistent reference frame and multi-finger contact degrades shape recognition — is directly relevant to assessing LLM-only descriptive pipelines used as cartographic surrogates.
- **Authoring gap**: the identified bottleneck — VI users cannot independently author maps except via Tangible Reels / similar — is a live research target.
- **Refreshable-display economics**: the chapter's cost / resolution numbers (10k-100k USD, ~120×60 pins) can be cited in feasibility arguments against shape-display-only solutions.

## Open Questions
- [ ] Exact numerical effect sizes for Brock et al. 2015 one-week retention comparison — not present in this chapter; must be pulled from the primary paper.
- [ ] What is the minimum pin pitch and display area required for a refreshable display to support a useful city map? — chapter cites 2.5 mm and ~120×60 but does not derive a lower bound.
- [ ] Whether 3D-printed interactive maps with capacitive touch scale to large areas — chapter cites feasibility but not an area / cost curve.
- [ ] How does audio-only interactive map performance compare for congenital vs late-blind users on matched tasks? — chapter hints at difference but does not systematise.

## Related Work Worth Reading
- **Brock, A., Truillet, P., Oriola, B., Picard, D., & Jouffrais, C. (2015).** Interactivity improves usability of geographic maps for visually impaired people. HCI 30(2), 156-194. [Primary empirical reference for the review's ITM claims.]
- **Giudice, N. A., Palani, H. P., Brenner, E., & Kramer, K. M. (2012).** Learning non-visual graphical information using a touch-based vibro-audio interface. ASSETS'12, 103-110.
- **Picinali, L., Afonso, A., Denis, M., & Katz, B. F. G. (2014).** Exploration of architectural spaces by blind people using auditory virtual reality for the construction of spatial knowledge. IJHCS 72(4), 393-407.
- **Zeng, L., & Weber, G. (2010-2012).** ATMap and augmented you-are-here maps via BrailleDis 9000 — canonical refreshable-tactile-map references.
- **Kane, S. K., Morris, M. R., & Wobbrock, J. O. (2013).** Touchplates — overlays for accessible touchscreens. ASSETS'13.
- **Ducasse, J., Macé, M., Serrano, M., & Jouffrais, C. (2016).** Tangible Reels: construction and exploration of tangible maps. CHI'16 — introduces the authoring sub-family.
- **Follmer, S., Leithinger, D., Olwal, A., Hogge, A., & Ishii, H. (2013).** inFORM: dynamic physical affordances and constraints through shape and object actuation. UIST'13.
- **Edman, P. K. (1992).** Tactile Graphics. AFB Press. [Canonical production-technique reference cited p.4.]

## Collection Cross-References

### Already in Collection
- [[Brock_2015_InteractiveMapsUsability]] — Ducasse is co-authored by Brock. This review treats Brock 2015 as the primary empirical reference for interactive tactile map usability claims and explicitly flags it as the replication target for one-week retention comparisons. Brock 2015 is the core data point behind this chapter's "interactivity improves usability" argument.
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — See Now in Collection subsection below for the full description and the IntuiFace MapSense naming-collision note.
- [[Gual_2015_EffectVolumetric3DTactile]] — Cited in the 3D-printing pipeline discussion; Gual's volumetric-vs-flat symbol-level evidence grounds Ducasse's taxonomy of tactile-layer fabrication strategies.
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — Cited in the 3D-printed tactile map generation section alongside other OSM-driven pipelines; Götzelmann's translucent-print + CapCode approach is one of the HIM (Hybrid Interactive Map) exemplars Ducasse surveys.
- [[Holloway_2018_AccessibleMapsBlindComparing]] — Same research lineage (Marriott group); Holloway's controlled 3D-vs-2D comparison is the kind of empirical evaluation this review calls for and is concurrent with Ducasse's survey.
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — See Now in Collection subsection below.
- [[Perkins_2002_CartographyProgressTactileMapping]] — Referenced as a historical anchor for the tactile-cartography state-of-field this review builds on.
- [[Rowell_2003_WorldTouchResultsInternational]] — Foundational producer-survey baseline for the static tactile-map era this review extends beyond.
- [[Taylor_2016_Customizable3DPrintedTactile]] — Cited as a customizable 3D-printed tactile map production example; one of the tool-oriented pipelines within Ducasse's accessible-interactive-map taxonomy.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — (Forward conceptual link — Wabinski 2022 post-dates Ducasse 2018 and can serve as the tactile-layer symbol-level invariants consumable by Ducasse's DIM/HIM classes.)

### Now in Collection (previously referenced as leads / inline citations)
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — Papadopoulos, Koustriava & Koukourikos (2017, Assistive Technology 30(4):191-200). This is the specific audio-tactile-vs-verbal-description O&M study whose "Papadopoulos series" was referenced inline on p.196, p.300, and p.332 of this review. Within-subjects design, N=20 totally blind adults, three real Thessaloniki urban areas: audio-tactile map beats verbal-only description on correct O&M answers (M 5.75 vs 4.85, F(1,19) ≈ 30, p < 0.001, large effect) with no significant difference in study time or execution time — direct quantitative support for this chapter's claim that interactive tactile-audio maps "produce measurable spatial-cognition gains that transfer to real environments."
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — Brulé, Bailly, Brock, Valentin, Denis & Jouffrais (CHI 2016). Referenced in Ducasse's survey twice: (a) grouped with "Interactive Raised-Line Map" systems (BATS, LineSpace, MapSense) as a tablet-plus-overlay approach, and (b) cited in the "3D printing with embedded interactivity" section as "Brulé, Bailly et al. 2016 (MapSense / pedagogical 3D maps for VI children)". The paper is actually a *qualitative formative study + participatory design* with 15 caretakers and ~19 VI children, combining a capacitive tablet, raised-paper figurative map, conductive ink, and 3D-printed tangible landmarks — not purely a 3D-printing pipeline. NOTE: an earlier Ducasse mention (line 119 of this notes file) lists "MapSense" in the context of the IntuiFace MapSense commercial touch-table; that is **a different product with the same name** and should not be conflated with Brulé et al. 2016.

### Cited By (in Collection)
- [[Wabiski_2026_CognitiveReviewProtocol]] — Wabiski's 2026 systematic-review protocol targets exactly the inclusive-cartography literature Ducasse's survey organizes. Ducasse's DIM/HIM taxonomy is one of the secondary-literature anchors the protocol's search strategy must retrieve and score correctly.
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — Papadopoulos's reconciliation notes that Ducasse's survey argues interactive maps produce measurable spatial-cognition gains that transfer to real environments, and positions Papadopoulos as the head-to-head effect-size data point substantiating Ducasse's "measurable" claim.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Wabinski 2022 treats Ducasse 2018 as the DIM/HIM taxonomic anchor within which Wabinski's symbol-level guidelines are directly consumable as the tactile-layer design invariants — the two papers compose: Ducasse says *which* device class to build, Wabinski says *how big* its symbols must be.

### Conceptual Links (not citation-based)
- [[Brock_2015_InteractiveMapsUsability]] — Direct research-lineage link (shared author); Ducasse organizes the literature around Brock's Interactive Tactile Map findings as a foundation.
- [[Holloway_2018_AccessibleMapsBlindComparing]] — Strong. Holloway's controlled 3D-vs-2D study provides exactly the comparative-empirical evidence Ducasse's taxonomic survey calls for but does not itself supply.
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — Strong. Ducasse cites the Papadopoulos line as evidence of real-environment spatial-cognition transfer; Papadopoulos provides the F/η² effect sizes that substantiate Ducasse's narrative claims.
- [[Gual_2015_EffectVolumetric3DTactile]] — Moderate. Gual's symbol-level volumetric evidence feeds into Ducasse's 3D-printing pipeline taxonomy as the underlying empirical warrant for 3D-printed tactile layers.

<!--
Worker checkpoint (2026-04-12):
GOAL: Retrieve + process Ducasse_2018 into inclusive-cartography collection (per prompts/retrieve-and-process-paper.md).
DONE: arXiv retrieval of 2208.14685 succeeded; dir renamed to Ducasse_2018_*; all 45 pages read page-by-page; notes.md (this file), abstract.md, description.md, citations.md, metadata.json written; paper.pdf in-dir; 45 PNGs; reconcile appended Collection Cross-References section above (Papadopoulos_2018, Brulé_2016).
COMMITTED: 422fa78d — "add: Ducasse_2018_AccessibleInteractiveMapsVisually via paper-process" (5 markdown+metadata files; pngs/ and paper.pdf are gitignored so not in commit, which matches the collection convention).
papers/index.md: untracked upstream, not modified by this worker.
STUCK: nothing.
NEXT: write reports/retrieve-Ducasse_2018.md. Done after that.
-->

