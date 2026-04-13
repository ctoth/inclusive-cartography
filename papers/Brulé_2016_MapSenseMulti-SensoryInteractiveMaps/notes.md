---
title: "MapSense: Multi-Sensory Interactive Maps for Children Living with Visual Impairments"
authors: "Emeline Brulé, Gilles Bailly, Anke Brock, Frédéric Valentin, Grégoire Denis, Christophe Jouffrais"
year: 2016
venue: "CHI 2016 — Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems, San Jose, CA, USA"
doi_url: "https://doi.org/10.1145/2858036.2858375"
pages: "14 (conference + HAL cover)"
affiliations:
  - "LTCI, CNRS, Télécom ParisTech, Paris-Saclay University"
  - "IRIT, CNRS & Université Paul Sabatier, Toulouse"
  - "INRIA Bordeaux / IA Toulouse"
hal_id: "hal-01263056"
produced_by:
  agent: "claude-opus-4-6[1m]"
  skill: "paper-reader"
  timestamp: "2026-04-13T05:27:36Z"
---
# MapSense: Multi-Sensory Interactive Maps for Children Living with Visual Impairments

## One-Sentence Summary
MapSense is a design-research project that produces tangible, multi-sensory (raised-paper + 3D-printed objects + capacitive conductive-ink touch points + audio) interactive maps for visually impaired children, derived from a participatory formative study with 15 specialized caretakers/teachers and evaluated in situ in a specialized French institute for VI children. *(p.1, p.2, p.6)*

## Problem Addressed
Existing geographic education tools for visually impaired (VI) children are fragmented, expensive, or unsuited to classroom use: raised-line paper maps are static and non-interactive; digital accessible maps target adults and require hardware (Talking Tactile Tablet, NOMAD, IVEO) that is unavailable or impractical in specialized schools; mainstream multi-touch tablets are hard for VI children to explore because they offer no passive tactile cues. Moreover, prior HCI work has paid scant attention to the needs of VI *children* (as opposed to adults) and to the role of caretakers/teachers, who are the actual mediators between the child and the technology. *(p.1, p.2)*

## Key Contributions
- **Formative ethnographic study** of 15 specialized caretakers and teachers for VI children to elicit needs, current practices, and D-I-Y adaptation patterns around geography and map-literacy education. *(p.3, p.4, p.5)*
- **Two interactive-map prototypes**, Mappie and MapSense, designed with children and teachers, combining a capacitive tablet, raised-paper figurative maps, and 3D-printed tangible landmarks. *(p.1, p.6, p.7)*
- **Empirical in-the-wild evaluation** of both prototypes with VI children (ages 6–11) at a specialized institute; qualitative findings on engagement, learning, and caretaker appropriation. *(p.7, p.8, p.9)*
- **Design recommendations** for multi-sensory interactive maps for VI children and for supporting caretaker D-I-Y practices (cost, modularity, customization, robustness, sound design, tangible semantics). *(p.9, p.10)*
- A critique of "one-size-fits-all" accessibility solutions: disability is diverse (additional impairments, age, institutional context) and interactive maps must allow teachers to personalize and extend content. *(p.9, p.10)*

## Study Design (empirical)
- **Type:** Qualitative, participatory design + in-situ user study (formative study → iterative prototypes → two evaluations). *(p.3, p.7, p.8)*
- **Formative-study population:** 15 specialized caretakers/teachers (13 interviewed + 2 observed) at the Institute for the Young Blind of Toulouse (IJA) and partner institutions in France. Table 2 lists 13 (C1–C13) with gender and expertise (locomotion instructor, specialist teacher, occupational therapist, speech therapist, transcriber, art teacher, psychologist, etc.). *(p.4, p.5)*
- **Children population (prototype evaluations):** Two rounds; ~6 children (C1–C6) in round one, ~13 more children in round two. Ages roughly 6–11, with a mix of total blindness, low vision, and additional impairments (motor, cognitive). *(p.7, p.8, p.9)*
- **Methods:** Semi-structured interviews; non-participant classroom observation; participatory design sessions; think-aloud during prototype use; video/audio capture; caretaker co-design; thematic analysis of interviews and observation logs. *(p.3, p.4, p.7)*
- **Setting:** Specialized school classrooms and therapy rooms; French context (Institute for the Young Blind, Toulouse). *(p.3, p.4)*
- **Prototypes evaluated:** (1) **Mappie** — first interactive-map prototype; capacitive stylus-readable raised-paper map of an imaginary castle for touch-tablet exploration; (2) **MapSense** — second, more flexible prototype that supports custom regional maps (e.g., a French region with cultural points of interest, class-trip itinerary) and composable D-I-Y 3D-printed tangibles. *(p.6, p.7)*

## Methodology
1. **Needs elicitation** — interviews with 13 caretakers/teachers + observation of 2 specialized classrooms; thematic coding of transcripts to surface current practices, barriers, and adaptation strategies. *(p.3, p.4)*
2. **Design-goal derivation** — translation of findings into explicit design goals (multi-sensory, customizable, caretaker-appropriable, low-cost, robust). *(p.3, p.6)*
3. **First prototype (Mappie)** — imaginary-castle tangible/tablet map; early evaluation with 6 VI children. *(p.6, p.7)*
4. **Second prototype (MapSense)** — extended system supporting user-authored maps and modular 3D-printed tangibles; evaluation with 13 more children + caretakers. *(p.7, p.8)*
5. **Analysis** — qualitative analysis of engagement, learning strategies, collaboration patterns, caretaker appropriation, limits. *(p.8, p.9)*
6. **Recommendations** — synthesized design and policy recommendations for multi-sensory interactive maps for VI children. *(p.10)*

## System Description

### Mappie — first interactive-map prototype *(p.6)*
- **Motivation:** build an interactive map to help VI children access symbolic representations, and to help them compare several scales.
- **Construction:** a raised-paper figurative-map overlay (representing an imaginary castle) placed on a capacitive touch screen. Uses off-the-shelf parts: Samsung Galaxy Note Pro 12.2" (model SM-P900/P905, 2560×1600, 9.1 mm thick, MT140 library compatible).
- **Software:** Android Java application built with the MT140 library. Executes in two phases — (1) a presentation phase introduces the map and associated stories, and (2) an exploration phase responds to touch events with audio (spatialized sound, narration). *(p.6)*
- **Physical stack:** raised-paper overlay on top of the tablet; children explore by running their hands/fingers over the raised lines; touches are detected by the capacitive display through the paper. Conductive ink / capacitive coupling allows the tablet to register touches through the overlay. *(p.1, p.6)*
- **Content:** imaginary castle map with several rooms and stories. First designed for free exploration, later revised for more guided interaction. *(p.6)*

### MapSense — second, iterative prototype *(p.7)*
- Extends Mappie to **user-configurable maps**: teachers/caretakers can author custom regional maps, e.g., a French region's cultural points of interest, or the itinerary of an upcoming class trip (Fig. 6).
- Adds **modular 3D-printed tangibles** that snap onto the map to represent landmarks, people, or events. The tangibles have **four basic shapes** used semantically (landmark type, action marker), enabling pre-lesson customization.
- Introduces a **Do-It-Yourself pipeline** (Fig. 7) so a teacher can assemble a new MapSense map from supplies: raised-paper printout, conductive-ink traces, 3D-printed tangibles, and tablet-side content (audio files, metadata).
- Supports both **locomotion/itinerary planning** ("drive home"-style simulation, Fig. 3 "Driving in Europe") and **curricular geography** (French region map with heritage landmarks). *(p.2, p.7)*
- Provides **audio feedback** in three roles: (1) ambient / spatial sound setting scene; (2) informational sound on touch (name, category, description); (3) narrative / guided storytelling. *(p.6, p.9)*

### Formative-study inputs *(p.3–p.5)*
- **Interview instrument:** semi-structured interview covering: current geography-teaching practice, use of tactile/digital tech in classroom, frustrations, D-I-Y adaptations, collaboration with colleagues, what "an ideal tool" would look like.
- **Observations:** classroom sessions using current tools (raised-paper maps, Braille, plastic reliefs, Play-Doh, Lego, hand-assembled collages).
- **Participants (Table 2, p.5):** 13 caretakers/teachers — 8 women, 5 men — spanning roles: locomotion instructor (3), specialist teacher (4), low-vision specialist, occupational therapist, speech therapist, transcriber, art teacher, psychologist, with expertise covering Braille, raised-line drawing production, mobility training, and curriculum adaptation.

## Findings from the Formative Study

### Children's uses of tactile technologies *(p.3, p.4)*
- Children primarily use **analog** media for geography: raised-paper maps (from the National Institute for the Young Blind collection), thermoform reliefs, Braille legends, Play-Doh, Lego, and teacher-made collages.
- Digital tools (Talking Tactile Tablet, NOMAD, IVEO) are **rare**: expensive, fragile, tied to specific vendor content, or unsuitable for young children.
- Children also use **mainstream devices** (iPads, standard tablets) for reading/games but complain that maps are hard to explore because "nothing stops the finger."
- Children mix the sense of touch with residual vision and audio; **multi-sensory** is the default, not the exception.

### Roles and needs of caretakers / teachers *(p.4)*
- Caretakers are both **educators and translators**: they adapt generic curriculum material into accessible form (Braille, raised-paper, tactile props).
- They have very different backgrounds (mobility instructors vs. art teachers vs. psychologists) and therefore very different design vocabularies.
- They collaborate informally — sharing homemade materials, Braille transcriptions, tactile diagrams — but each institution is largely on its own.
- Their frustration: **"one-size-fits-all" technologies never fit** — they have to customize everything.

### Children's interaction techniques *(p.4)*
- Children explore tactile maps with a combination of **two-handed scanning**, **one-handed detail tracing**, and **stylus/finger probing** on tablets.
- Table 1 lists observed interaction strategies: "low-vision look", "high-vision look", "shift" between zones, "ask for spoken name", "double-tap for details", "drag finger over path", "hold shape", and "stereognosis" (shape identification by touch).
- Tablet-only interfaces frustrate children because **no tactile landmark anchors the exploration** — they lose their place.

### D-I-Y practices of caretakers *(p.6)*
- Caretakers routinely build their own tactile materials using: raised-paper schoolbooks, maps from the National Institute, Braille overlays, thermoform sheets, Inkscape, Microsoft Word, 3D printers, Play-Doh, Lego.
- They adapt materials by consuming a lot of time per student; materials are often not reusable because each child/lesson is different.
- Many caretakers have programming or authoring experience (C1, C2, C4, C5, C7, C10) and **are willing to write simple apps** if the platform allows it.
- Barriers: lack of time; lack of money for professional tools; tools not designed for their workflow; the need to rework materials for every new lesson.

### Summary of needs → design recommendations *(p.6, p.10)*
Design requirements distilled from the study:
- **Multi-sensory** (touch + audio + residual vision): reinforce each channel with redundant encoding.
- **Customizable** at the teacher level: support authoring new maps, new audio, new tangibles.
- **Modular** hardware and content: reusable pieces across lessons.
- **Robust** to rough classroom use.
- **Low-cost** components (consumer tablet, printable supplies).
- **Collaborative**: support multi-child exploration and teacher-child joint use.

## Evaluation — Mappie *(p.7)*
- **Participants:** 6 VI children (C1–C6) at IJA, ages ≈6–11, mix of total blindness and low vision, some with additional impairments (motor, cognitive).
- **Setup:** children explored the castle map freely, then with teacher guidance; sessions were video-recorded.
- **Main observations:** children engaged readily with the tangible-tablet combination; they used **two-handed scanning** and relied heavily on audio labels; total-blindness children needed more guidance to find map boundaries; low-vision children used residual vision as an anchor.
- **Limits observed:** the imaginary-castle content was motivating but had limited curricular transfer; the prototype did not support teacher authoring, so caretakers could not reuse it.

## Evaluation — MapSense *(p.8, p.9)*
- **Participants:** 13 additional VI children + caretakers at IJA.
- **Two content scenarios:**
  1. A map of a French region with cultural points of interest (used for "virtual field trip" lessons).
  2. A map of the itinerary of an upcoming class trip (used as preparation before the actual trip).
- **Interaction strategies observed:**
  - **Two-handed scanning** to locate tangibles.
  - **Finger tracing** of raised-paper borders.
  - **Tangible manipulation**: children physically picked up and placed 3D-printed landmark tangibles, often reorganizing them into narratives.
  - **Collaborative exploration**: children quizzed each other about landmarks, used tangibles as turn-taking tokens.
  - **Adoption and appropriation**: caretakers quickly started to suggest new uses: one teacher proposed using MapSense for language lessons by swapping the audio for foreign-language labels; another proposed a "storytelling" mode where the map plays a pre-recorded journey.
- **Emerging design themes from MapSense sessions (p.9):**
  - **Empowerment** — children felt ownership over the map when they could place tangibles and trigger sounds; this contrasted with adult-mediated raised-paper maps.
  - **Learning strategies and collaboration** — children developed shared vocabulary ("the cold one", "the tall one") for tangibles; teachers used MapSense to scaffold group discussion.
  - **Impact on memorization** — at the end of the first session, a locomotion trainer reported children recalling the spatial layout of a route they had previously only heard described.
  - **Limits identified**: occasional sound-channel conflicts when multiple tangibles were touched; tangibles sometimes slid on the paper overlay; authoring a new map still required >1 hour of caretaker work.

## Discussion *(p.9, p.10)*

### Impact of MapSense on the classroom
- MapSense is one of the first tools the caretakers felt they could **own and extend**; several explicitly said they wanted to use it outside geography (language, storytelling, memory games).
- The authors position MapSense as an instance of **reflective learning and autoethnographic pedagogy**: the map becomes a medium through which children narrate their own experiences (e.g., the itinerary of a trip they just took).
- They note four recurring modalities in which MapSense was used: (1) geography/education of sighted peers, (2) spatial-skills training, (3) narrative / storytelling, and (4) multi-sensory play.
- MapSense was perceived as broadly **inclusive** because it works for children with different levels of vision, with other disabilities (the tangibles are useful for children with both visual and motor impairments), and for sighted classmates.

### Reflection on D-I-Y vs. manufactured solutions *(p.9, p.10)*
- The best outcomes came when caretakers felt **invited to modify** the system. Conversely, locked-down commercial devices (TTT, IVEO) had been abandoned even when technically superior.
- **Not all caretakers wanted to be programmers**: the authors recommend tiered customization — GUI-authoring for most, scripting for power users.
- Cost, repairability, and availability of materials (filament, consumer tablets) are first-order concerns for specialized schools.

### Design recommendations (synthesized) *(p.10)*
1. **Support creativity and improvisation** — provide authoring tools, not just content; expose parameters (sound, tangible shape, map topology) to teachers.
2. **Encourage storytelling** — design audio/tangible pairings that scaffold narration, not just identification.
3. **Enable high-level customization** — let teachers add new maps, tangibles, languages, narratives without developer help.
4. **Engage different expertise** — cooperate with locomotion trainers, art teachers, psychologists; each contributes different design constraints.
5. **Do *not* design for disability in the abstract** — design for a specific classroom's mix of impairments, ages, and curricular goals.
6. **Account for institutional reality** — budgets, device fleets, maintenance, teacher time.

## Parameters / System Specs

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Tablet model | — | — | Samsung Galaxy Note Pro 12.2" (SM-P900/P905) | — | p.6 | Capacitive multitouch, Android |
| Tablet resolution | — | px | 2560×1600 | — | p.6 | Reported by authors |
| Tablet thickness | — | mm | 9.1 | — | p.6 | Relevant for overlay fit |
| Tablet software library | — | — | MT140 (Java / Android) | — | p.6 | Used to build Mappie/MapSense apps |
| Raised-paper overlay | — | — | figurative map printed on swell/capsule paper | — | p.1, p.6 | Placed directly on tablet screen |
| Conductive ink | — | — | — | — | p.1 | Couples raised-paper touch points to capacitive screen |
| 3D-printed tangibles | — | count | 4 basic shapes | — | p.7, p.8 | Modular landmark tokens |
| Ages of child participants | — | years | — | ~6–11 | p.7 | VI children, mixed additional impairments |
| N formative caretakers/teachers | — | count | 15 | 13 interviewed + 2 observed | p.3, p.4 | Table 2 |
| N Mappie evaluation children | — | count | 6 | — | p.7 | C1–C6 |
| N MapSense evaluation children | — | count | 13 | — | p.8 | Second round |
| Audio roles | — | — | 3 | ambient / informational / narrative | p.6, p.9 | Design-theoretic categories |
| Authoring time per new map | — | hours | >1 | — | p.9 | Caretaker-reported limitation |

## Equations / Statistical Models
This paper does **not** present quantitative models, effect sizes, or statistical tests. All results are qualitative. No equations to extract.

## Effect Sizes / Key Quantitative Results
None reported. Findings are qualitative themes from interviews and observation, not numeric outcomes. *(paper is qualitative / formative)* *(p.8, p.9)*

## Methods & Implementation Details
- **Hardware stack:** consumer capacitive tablet + printed raised-paper overlay + conductive-ink traces aligned to touch targets + 3D-printed tangibles. *(p.1, p.6)*
- **Software stack:** Java/Android app built on MT140 library; two-phase execution (presentation then interaction); audio assets keyed to touch regions. *(p.6)*
- **Authoring workflow:** teacher designs map in Inkscape (or similar); prints swell-paper relief; applies conductive-ink to define touch points; records or selects audio; prints tangibles via FDM 3D printer; loads metadata into app. *(p.6, p.7, p.9)*
- **Evaluation protocol:** two iterative rounds of in-situ evaluation at IJA; each session roughly 20–40 minutes; sessions recorded for thematic analysis. *(p.7, p.8)*
- **Ethics / consent:** parental consent for photographs and recordings; caretaker consent for interviews. *(p.3, p.4, implied)*
- **Analytic method:** thematic analysis of interview and observation transcripts, cross-validated between multiple researchers. *(p.3, p.4)*

## Figures of Interest
- **Fig. 1 (p.1/p.2):** A child interacts with MapSense — raised-paper figurative map on tablet, 3D-printed tangible in hand.
- **Fig. 2 (p.2):** Mappie schematic — raised-paper overlay on tablet + 3D tangibles + conductive ink points.
- **Fig. 3 (p.2):** "Driving in Europe" — MapSense route map for locomotion/itinerary scenarios.
- **Fig. 4 (p.3):** Existing tools used by VI children — Proba 3 SciGlobe (3D-printed tactile globe) and Proba 3 SoundBox (tangible audio recorder).
- **Fig. 5 (p.3):** Mappie castle overlay on the tablet, showing rooms with the tangible-overlay method.
- **Fig. 6 (p.7):** Two MapSense instantiations — Left: French region with cultural points of interest; Right: class-trip itinerary.
- **Fig. 7 (p.7):** MapSense D-I-Y supplies — raised paper, conductive ink pen, 3D-printed tangibles, tablet.
- **Table 1 (p.4):** Observed interaction techniques of VI children with tactile technologies and reference codes (CT1..CT14).
- **Table 2 (p.5):** Description of 13 interviewed caretakers — ID, gender, role, expertise.

## Results Summary
- All children engaged positively with both Mappie and MapSense; even totally blind children quickly adopted two-handed scanning over the raised-paper overlay and used tangibles as persistent spatial anchors. *(p.7, p.8, p.9)*
- Caretakers perceived MapSense as **more appropriable** than prior commercial tools and began speculating about uses beyond geography within the first session (language lessons, storytelling, memory games). *(p.9)*
- Children showed improved recall of spatial layouts after short MapSense sessions (locomotion trainer's anecdotal report); the authors flag this as a hypothesis worth formal testing, not a proven effect. *(p.9)*
- MapSense worked across a wide age range and impairment mix; the authors interpret this as evidence for **universal-design** style benefits rather than disability-specific design. *(p.9, p.10)*

## Limitations *(p.9, p.10)*
- **Qualitative only:** no quantitative evaluation of learning outcomes, no control condition, no effect sizes.
- **Small N:** ~19 children across both rounds, single institution (IJA, Toulouse).
- **Single cultural context:** French school system; French Braille conventions; French curricular geography content.
- **Authoring overhead:** >1 hour to author a new map; currently requires technical skill beyond some caretakers.
- **Hardware frailty:** paper overlays degrade with classroom use; tangibles can slide; conductive-ink traces can wear.
- **Audio conflict** when multiple tangibles are touched simultaneously — no mixing/priority policy yet.
- **Content scale:** demo maps are small (one region, one trip); no story about scaling to full-country or world maps.
- **No long-term study:** evaluation sessions were short; no data on retention, classroom integration over a semester, or effect on academic outcomes.

## Arguments Against Prior Work *(p.2, p.9, p.10)*
- Prior digital accessible maps (**Talking Tactile Tablet, NOMAD, IVEO**) are **designed for adults**, expensive, tied to proprietary content libraries, and therefore rarely used in specialized schools for children.
- Mainstream multi-touch tablets (iPad, etc.) lack **passive tactile landmarks** and confuse VI children who lose their place on flat glass.
- Pure raised-paper maps are excellent for tactile reference but are **non-interactive** — no dynamic audio, no updating of content, no collaboration with a tablet-based learning app.
- HCI accessibility research has been **adult-centric**: the authors argue the field has under-invested in tools designed *with* and *for* children, and has ignored the **caretaker-as-mediator** as a primary stakeholder.
- "One-size-fits-all" accessible tools fail in practice because disability is heterogeneous; real classrooms combine children with total blindness, low vision, motor impairments, cognitive differences, and different ages — a single fixed design cannot serve them all. *(p.9, p.10)*

## Design Rationale *(p.6, p.7, p.9, p.10)*
- **Why a raised-paper overlay on a capacitive tablet?** It gives passive tactile cues (paper) with dynamic feedback (tablet audio) without requiring expensive custom hardware.
- **Why 3D-printed tangibles?** They are cheap to produce, can be shape-coded for semantic roles, and give children a physical anchor and a manipulable narrative prop.
- **Why D-I-Y authoring?** Because the formative study showed caretakers will abandon any tool they cannot modify; ownership is a prerequisite for sustained use.
- **Why qualitative study over RCT?** Because the problem space is poorly characterized: the authors argue they need to understand the *kind* of tool to design before measuring its effect.
- **Why involve locomotion trainers, art teachers, and psychologists?** Each domain surfaces different constraints (spatial cognition, aesthetic engagement, emotional support).
- **Why a castle (Mappie) and then a real region (MapSense)?** Mappie tested the hardware/software stack with imaginative content; MapSense tested educational transfer with real curricular content.

## Testable Properties
- Raised-paper overlay + capacitive tablet yields reliable touch events for VI children's typical finger pressure on swell-paper relief. *(p.6)*
- VI children adopt two-handed scanning on MapSense maps within the first session. *(p.7, p.8)*
- Caretakers prefer an authorable system over a fixed-content system when both are available. *(p.9)*
- Children exhibit spontaneous storytelling / collaborative play when modular tangibles are added to a map. *(p.8, p.9)*
- MapSense usage is associated with improved recall of a spatial itinerary compared with verbal description alone (hypothesized, not proven). *(p.9)*
- A single multi-sensory map design can serve children across a range of vision levels and additional impairments (hypothesized as "inclusive-by-design"). *(p.9, p.10)*

## Relevance to Project
Direct relevance to **inclusive cartography**: this is a concrete end-to-end prototype for making maps accessible and educational for VI children, with an explicit formative study of caretaker needs. It argues strongly for (a) multi-sensory redundancy, (b) teacher-level authoring, and (c) heterogeneity-aware design. Useful as:
- A counterexample to any systematic review that treats "accessible map = screen-reader TTS on Leaflet".
- Evidence that caretaker / teacher mediation is a first-class HCI design constraint, not an afterthought.
- A source of design requirements (multi-sensory, modular, cheap, authorable) for any proposed inclusive-cartography system.
- Grounds for critiquing protocols that demand RCT-style effect sizes from a field whose primary tools are qualitative and ethnographic (LLM-confidence-threshold critique context).

## Open Questions
- [ ] What is the actual long-term (semester-scale) effect of MapSense on spatial learning outcomes?
- [ ] Does the benefit generalize outside the French specialized-school context?
- [ ] How do you solve the audio-conflict problem when many tangibles are co-touched?
- [ ] What authoring UI reduces map-creation time from >1 hour to minutes?
- [ ] How does MapSense compare against modern vibro-tactile or force-feedback tablets?

## Related Work Worth Reading
- Brock et al. — TactiPad / interactive tactile maps for VI adults (referenced repeatedly; Brock is a coauthor). → NOW IN COLLECTION: [[Brock_2015_InteractiveMapsUsability]]
- Gual et al. — volumetric 3D tactile symbols (refs 19, 20). → NOW IN COLLECTION: [[Gual_2015_EffectVolumetric3DTactile]]
- Miele — Talking Tactile Tablet and SVG-based accessible maps (cited as the ancestor of this work).
- Ullmer & Ishii — "Emerging frameworks for tangible user interfaces" (ref 52) — foundational TUI work.
- Shams & Seitz — "Benefits of multisensory learning" (ref 50) — cognitive-science justification for multi-sensory design.
- Zeng & Weber — "Accessible Maps for the Visually Impaired" (ref 55) — closely related prior system.
- Winberg & Bowers — "Assembling the senses: cooperative interfaces for visually impaired users" (ref 54).
- Wang et al. — "Instant tactile-audio map" (ref 53).

## Collection Cross-References

### Already in Collection
- [[Brock_2015_InteractiveMapsUsability]] — Brulé's ref [5]. Same research group (Brock, Jouffrais); the quantitative usability study of an interactive tactile map for VI adults that MapSense extends to children. Directly cited as prior art for the tangible+tablet combination.
- [[Gual_2015_EffectVolumetric3DTactile]] — Brulé's ref [19]/[20]. Empirical evidence that volumetric 3D-printed tactile symbols are better recalled than flat swell-paper symbols; underpins MapSense's use of 3D-printed tangible landmarks.

### New Leads (Not Yet in Collection)
- **Miele, Landau, Gilden (2006)** — "Talking TMAP: Automated generation of audio-tactile maps" — defining ancestor of interactive audio-tactile maps; systematic reviews of inclusive cartography should have this.
- **Zeng & Weber (2011)** — "Accessible Maps for the Visually Impaired" — closely related prior system for VI adults; good for comparative synthesis.
- **Winberg & Bowers (2004)** — "Assembling the senses: cooperative interfaces for visually impaired users" — CSCW grounding for multi-user VI interaction.
- **Wang, Li, Hedgpeth & Haven (2009)** — "Instant tactile-audio map" (ASSETS) — another tablet+overlay approach worth direct comparison with MapSense.
- **Ullmer & Ishii (2000)** — "Emerging frameworks for tangible user interfaces" — foundational TUI framework; cited by most tangible-map papers in the collection.
- **Shams & Seitz (2008)** — "Benefits of Multisensory Learning" — the cognitive-science justification for multi-sensory design; important for any systematic review evaluating claims about multi-sensory cartography.
- **Hurst & Tobias (2011)** — "Empowering Individuals with Do-it-Yourself Assistive Technology" — grounds the "caretaker-as-author / D-I-Y" design thread that MapSense extends.

### Supersedes or Recontextualizes
- Brulé et al. 2016 does **not** supersede [[Brock_2015_InteractiveMapsUsability]]; it is a complementary qualitative child-focused extension of the same research program. No backward annotation beyond a see-also on Brock 2015.

### Cited By (in Collection)
- [[Ducasse_2018_AccessibleInteractiveMapsVisually]] — Ducasse's survey groups MapSense in the "Interactive Raised-Line Map" family alongside BATS and LineSpace (p.19 of Ducasse's notes, line 135), and again in "3D printing with embedded interactivity: Brulé, Bailly et al. 2016 (MapSense / pedagogical 3D maps for VI children)" (p.32-33 of Ducasse's notes, line 226) and "3D printed diagrams: ... Brulé et al. 2016 (3D-printed geographic maps)" (line 205). NOTE: a separate earlier mention on line 119 ("MapSense on the IntuiFace MapSense table, cited p.18") appears to be a naming collision with a commercial IntuiFace product called MapSense; it is likely **not** this Brulé paper. Cross-reference reconciliation has flagged this below.
- [[Holloway_2018_AccessibleMapsBlindComparing]] — Holloway groups Brulé et al. with Brock & Jouffrais and Jones et al. in "Interactive tactile maps that rely on expensive capacitive overlays or touchscreens with separate tactile overlays, which are not easily replicated at low cost" (line 176). This is a **critique** of the cost/accessibility profile of MapSense's hardware stack and motivates Holloway's cheaper conductive-filament + Touch Board alternative.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Wabiński cites Brulé et al. 2016 as an exemplar of multimodal/audio-tactile maps (lines 218, 277) when arguing that tactile-map standardization should extend beyond haptics to multi-sensory design.

### Conceptual Links (not citation-based)
**Audio-tactile / multi-sensory interactive maps family:**
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — same year, same problem space: 3D-printed tactile map with registered audio-visual feedback via smartphone. Götzelmann uses a transparent 3D print with a tablet underneath; Brulé uses raised paper on a capacitive tablet with 3D-printed tangibles. Direct methodological contrast for any "design space of audio-tactile maps" synthesis.
- [[Palivcová_2020_InteractiveTactileMapTool]] — later tool-oriented interactive tactile map system. Inherits MapSense's teacher-authoring theme but targets a different user population; useful for discussing the evolution of authorable accessible-map tools.
- [[Taylor_2016_Customizable3DPrintedTactile]] — customizable 3D-printed tactile maps as interactive overlays; contemporaneous alternative hardware stack to MapSense. Different tradeoff: Taylor favors 3D-printed map surface; Brulé favors raised-paper overlay with separate 3D-printed tokens.

**Participatory / inclusive design of accessible cartography:**
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — reviews orientation-and-mobility aids for VI people; MapSense's locomotion-trainer co-design (one C participant) connects directly to the O&M literature Papadopoulos surveys.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — argues for global standardization of tactile-map design principles; MapSense's "refuse one-size-fits-all" stance is in direct tension with Wabiński's call for standardization and is worth surfacing as a substantive disagreement about how to improve inclusive cartography.

**Tactile-symbol cognition and memorability:**
- [[Gual_2015_EffectVolumetric3DTactile]] — provides the empirical basis (volumetric > flat symbols for recall) that MapSense's 3D-printed tangible design implicitly rests on. Already cited directly but the conceptual link is stronger than a pure citation: Gual is the "mechanism-level" evidence for a design choice MapSense treats as given.
- [[Holloway_2018_AccessibleMapsBlindComparing]] — provides the RCT-style comparison (3D vs 2D maps) that MapSense *does not* provide for itself. Reading Brulé (qualitative formative) alongside Holloway (controlled comparison) gives the evidence base MapSense alone lacks.

**Protocol-relevance (for Wabiski_2026):**
- [[Wabiski_2026_CognitiveReviewProtocol]] — MapSense is a high-quality example of a paper that would score **low** on an LLM-confidence-threshold quality checklist tuned for effect sizes, yet is obviously relevant to inclusive cartography. Useful test case for critiquing §3.4–§3.8 of the protocol.

