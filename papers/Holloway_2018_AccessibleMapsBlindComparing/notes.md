---
title: "Accessible Maps for the Blind: Comparing 3D Printed Models with Tactile Graphics"
authors: "Leona Holloway, Kim Marriott, Matthew Butler"
year: 2018
venue: "Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (CHI 2018), Montreal, QC, Canada, April 21-26"
doi_url: "https://doi.org/10.1145/3173574.3173772"
pages: "Paper 198, pp. 1-13"
affiliation: "Monash University, Melbourne, Australia"
---

# Accessible Maps for the Blind: Comparing 3D Printed Models with Tactile Graphics

## One-Sentence Summary
The paper empirically compares 3D-printed tactile models against conventional swell-paper tactile graphics for blind/low-vision map use, finding that 3D prints produce faster and more accurate understanding, are strongly preferred by users and O&M (orientation & mobility) trainers, and then proposes guidelines plus an interactive-audio-label prototype for authoring accessible 3D-printed maps. *(p.1)*

## Problem Addressed
Tactile maps and diagrams are the main way blind and low-vision (BLV) people access spatial information (mobility routes, building layouts, graphs, presentation-medium content), but production of 2D tactile graphics on swell paper (microcapsule) or embossed paper is expensive, slow (can take a week), and constrained to 2D symbolisation, leading to confusion and low adoption. The arrival of cheap desktop 3D printers raises the question of whether 3D-printed models replace or complement tactile graphics — there was no empirical evidence base. *(p.1, p.2)*

## Key Contributions
- First controlled empirical comparison of 3D-printed models vs traditional 2D tactile graphics for BLV map/diagram access, combining pilot studies, a formal within-subjects study (N=16), and structured interviews with 9 O&M trainers and 4 BLV experts. *(p.1, p.3)*
- Quantitative evidence that 3D models outperform 2D tactile graphics on identification accuracy, time-to-find, feature understanding, and mental-model formation, with several differences statistically significant. *(p.5, p.6, p.7)*
- Rich qualitative findings on the advantages of 3D (recognisability without training, volumetric symbolisation, less reliance on explanatory legends/keys), disadvantages (cost, long print time, fragility, limited coverage area, occlusion), and combined-use scenarios. *(p.4, p.7, p.8, p.9)*
- An explicit list of guidelines for designing accessible 3D-printed maps derived from empirical evidence and trainer/expert feedback — covering scale, path widths, feature heights, street widths, key/legend handling, orientation, and interactive audio labels. *(p.9, p.10)*
- Interactive Audio Labels technique: a usable 3D-printed campus model augmented with capacitive-touch audio labels (conductive filament + Bare Conductive Touch Board + Arduino + microSD + smartphone) for accessible on-model labelling, including a working model demonstrated to trainers. *(p.8, p.9)*
- Identification of open research problems for 3D accessible cartography: cost reduction, interaction techniques, automated generation, shared libraries/repositories of models. *(p.9, p.10)*

## Study Design
- **Type:** Mixed-methods: (1) pilot interview study with BLV participants and O&M trainers, (2) within-subjects controlled comparison study, (3) follow-on formative/interview evaluation of 3D-printed campus model with interactive audio labels and trainer/expert interviews. *(p.1, p.3, p.4, p.8)*
- **Population (Main Study):** N=16 BLV participants recruited from Vision Australia and Guide Dogs Victoria. 5 male / 11 female. Ages: M=51.81, SD=13.2. 10 congenitally blind, 6 late-blind. Tactile graphic familiarity: self-rated, treated as covariate. *(p.4, p.5)*
- **Population (Pilot Studies):** 6 BLV participants (interviews, initial exposure to 3D models spanning buildings, cityscapes, floor plans, street maps, 3D graphs, statistical models, topographic and print maps); 5 O&M trainers. *(p.2, p.3)*
- **Population (3D Campus Model / Audio Labels evaluation):** 9 O&M trainers and 4 BLV experts in structured interviews around the Monash Clayton campus 3D printed model with interactive audio labels. *(p.8, p.9)*
- **Interventions / Conditions (Main Study):** Two map formats — (1) 2D tactile graphic on swell paper (microcapsule / "Minolta") produced from a raised-line drawing, and (2) 3D printed model produced on an Ultimaker 2 Extended 3D printer using white PLA plastic. Two corresponding content conditions: an urban park map and a train station platform map. *(p.3, p.4)*
- **Comparator:** Tactile-graphic condition is the comparator against 3D-printed condition. *(p.3)*
- **Primary endpoints:**
  - Identification accuracy — number of features correctly identified from ~6 recall questions without/with legend. *(p.5, p.7)*
  - Mental-model task accuracy — ability to answer inference questions about relative locations, which exit to take etc. *(p.6)*
  - Time to find a specific feature on the map. *(p.6)*
  - Subjective preference and ease-of-use ratings. *(p.7)*
- **Secondary endpoints:** Understanding of specific feature types (e.g. bridges, stairs), need for explanation, qualitative scanning strategies, perceived realism/recognisability. *(p.6, p.7)*
- **Procedure:** Each participant encountered both a 2D tactile graphic and a 3D-printed model. Order of map format and content was counterbalanced. For each map participants were asked to (a) explore freely, (b) identify features without a key, (c) identify features with a key, (d) answer mental-model/route questions, (e) find specific features while timed, (f) rate and comment. Interviews were audio recorded. *(p.4, p.5)*
- **Analysis:** Wilcoxon signed-rank tests (non-parametric, paired), with self-rated tactile graphic familiarity used as a covariate where needed. Reported statistics include z and p values. Free-text responses coded thematically. *(p.5, p.6, p.7)*

## Methodology
Two main studies: (1) within-subjects controlled comparison of 3D-printed models vs swell-paper tactile graphics using park and station maps; and (2) a formative interactive campus-model study using a Monash campus 3D print with capacitive-touch audio labels evaluated by O&M trainers and BLV experts. Pilot studies before the main study used a broad catalogue of sample 3D models (buildings, cityscapes, floor plans, street maps, 3D graphs, topographic maps) with BLV participants and trainers to characterise initial reactions, haptic exploration strategies, and concerns about cost, fragility and training. Guidelines were then derived from all phases combined. *(p.2, p.3, p.4, p.8, p.9)*

## Key Equations / Statistical Models
This is a user-study paper; the analytical model used is:

Non-parametric paired comparison of 3D-model vs tactile-graphic outcomes using the Wilcoxon signed-rank test with an α threshold of 0.05 and self-rated tactile graphic familiarity as a covariate / control. Reported per-outcome with test statistic z and p-value. *(p.5, p.6, p.7)*

$$
H_0: \operatorname{median}(X_{3D} - X_{2D}) = 0 \quad \text{vs} \quad H_1: \operatorname{median}(X_{3D} - X_{2D}) \neq 0
$$
Where: $X_{3D}$ is the per-participant score on the 3D printed map condition (accuracy, response time, or subjective rating), $X_{2D}$ is the same score on the tactile-graphic condition, and the hypothesis test is the Wilcoxon signed-rank test evaluated with α=0.05. *(p.5)*

## Parameters

### Study parameters (Main Study)

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Participants (main study) | N | people | 16 | — | p.4 | 5 male, 11 female |
| Mean age | M | years | 51.81 | SD=13.2 | p.4 | Main study |
| Congenitally blind participants | — | people | 10 | — | p.4 | Main study |
| Late-blind participants | — | people | 6 | — | p.4 | Main study |
| Pilot BLV participants | — | people | 6 | — | p.2 | Interview pilot |
| Pilot O&M trainers | — | people | 5 | — | p.2 | Interview pilot |
| Campus-model trainer interviews | — | people | 9 | — | p.8, p.9 | Post-audio-label phase |
| Campus-model BLV experts | — | people | 4 | — | p.8, p.9 | Post-audio-label phase |
| Significance threshold | α | — | 0.05 | — | p.5 | Wilcoxon signed-rank |

### Park map statistics (N=16)

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Mean correct identifications — tactile | — | items | (see figure) | — | p.5 | "neighbourhood" items; 3D > tactile |
| Mean correct identifications — 3D | — | items | (see figure) | — | p.5 | Greater than tactile (Fig 2) |
| Park-map Wilcoxon z | z | — | −2.34 | — | p.5 | Park-map identification accuracy |
| Park-map Wilcoxon p | p | — | 0.01 | <0.05 | p.5 | Statistically significant in favour of 3D |

### Station map statistics (N=16)

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Station-map Wilcoxon z | z | — | −2.28 | — | p.5 | Station identification accuracy |
| Station-map Wilcoxon p | p | — | 0.03 | <0.05 | p.5 | Statistically significant |

### Mental-model / route questions (N=16)

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| 3D mean correct (mental model) — N of 16 | — | people | 11 | — | p.6 | "significantly more people revealed this difference to be statistically significant (z=2.34, p=0.02)" |
| Tactile mean correct (mental model) | — | people | fewer than 3D | — | p.6 | Exact value in Fig 4 |
| Hypothesis 2 Wilcoxon z | z | — | 2.34 | — | p.6 | Mental-model accuracy |
| Hypothesis 2 Wilcoxon p | p | — | 0.02 | <0.05 | p.6 | Significant |
| Total time spent exploring maps | — | seconds | lower on 3D | — | p.7 | Fig 5 — shorter overall exploration on 3D |
| Feature-find time ratio 3D vs tactile | — | — | 6.63× | — | p.7 | "3D was on average 6.63 questions using the tactile graphics (sd=1.67)" — i.e. participants answered spatial questions much faster using 3D |
| Accuracy recall z (small questions) | z | — | 2.34 | — | p.7 | Fig 7 |
| Accuracy recall p | p | — | 0.02 | <0.05 | p.7 | Significant |

### 3D printing / model production parameters

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| 3D printer model | — | — | Ultimaker 2 Extended | — | p.4 | Main-study 3D-map production |
| Filament | — | — | White PLA | — | p.4 | Main-study 3D-map production |
| Interactive-audio-label filament | — | — | Proto-pasta conductive PLA | — | p.8 | Campus model electrodes |
| Touch sensor board | — | — | Bare Conductive Touch Board | — | p.8 | Arduino-compatible, capacitive-touch, 12 electrodes, onboard microSD/MP3 |
| Electrodes per Touch Board | — | — | 12 | — | p.8 | Max 12 labels per board in simple config |
| Audio storage | — | — | microSD MP3 | — | p.8 | Stored on board |
| Approximate total cost (campus model + electronics) | — | USD | 575 | — | p.9 | Prototype cost |
| Print time regime (park/station maps) | — | hours | "several hours" to ~21 | — | p.4 | Hours for simple maps, up to ~21 h for more complex |
| Map dimensions (main study) | — | mm | ~A4 footprint | — | p.3, p.4 | Park and station maps occupied ~A4 area |
| Minimum recommended path width | — | mm | ≥2.5 | — | p.9 | Raised paths must be wide enough for fingers to trace |
| Guideline: feature height | — | — | must rise above base | — | p.9 | Sufficient relief to differentiate from base |
| Guideline: street width minimum | — | — | wide enough for finger tracing | — | p.9 | Preserves routability |

## Effect Sizes / Key Quantitative Results

| Outcome | Measure | Value | CI | p | Population/Context | Page |
|---------|---------|-------|----|---|--------------------|------|
| Park-map identification accuracy, 3D vs 2D | Wilcoxon z | −2.34 | — | 0.01 | N=16 BLV | p.5 |
| Station-map identification accuracy, 3D vs 2D | Wilcoxon z | −2.28 | — | 0.03 | N=16 BLV | p.5 |
| Mental-model questions correct, 3D vs 2D | Wilcoxon z | 2.34 | — | 0.02 | N=16 BLV | p.6 |
| Accuracy of recall for small features (bridges, stairs), 3D vs 2D | Wilcoxon z | 2.34 | — | 0.02 | N=16 BLV | p.6, p.7 |
| Feature-find "questions answered" speed advantage, 3D vs tactile | ratio | 6.63× | sd=1.67 | — | N=16 BLV | p.7 |
| User preference for 3D printed map over tactile graphic | count | 16/16 preferred 3D | — | — | N=16 BLV, main study | p.7 |
| Trainer/expert preference for 3D printed campus model over 2D alternatives | qualitative | Unanimous endorsement | — | — | 9 trainers + 4 BLV experts | p.8, p.9 |

## Methods & Implementation Details
- Main-study maps were produced as matched pairs: one park map and one station map, each available in (a) an embossed/swell-paper tactile graphic and (b) a 3D-printed plastic model of roughly equivalent footprint (~A4). *(p.3, p.4)*
- Matched-pair task design controlled which map a participant saw in which format (counterbalanced). *(p.4)*
- Recall questions (Fig 1, p.4) were identical between formats, e.g. for a park: "How many entrances are there?", "In which quadrant is the monument?", "Where is the loop of trees?", "When you go in the south entrance, in which direction is the lake?", "When you stand in the centre, what is to the west?". For a station: "How many entrances are there?", "Which side is the pedestrian bridge on?", "How many lifts are there?", "When you go in the south entrance, what platform is in front of you?", "When you come down the middle set of stairs, what is in front of you?", Route finding Q1-Q2. *(p.4)*
- Free-exploration period preceded identification phase; identification was done without then with a tactile legend. Route-finding / mental-model questions followed identification. Final phase: find a specific feature while timed. *(p.4, p.5)*
- For legend handling: participants were given a raised-line legend on swell paper for both conditions. *(p.4)*
- Analysis: paired Wilcoxon signed-rank tests; self-rated tactile-graphic familiarity used as covariate / control, treated as ordinal from a Likert-like scale. Thematic coding of qualitative free-text answers and interview transcripts. *(p.5, p.6)*
- Guidelines are listed as a numbered list of design recommendations derived from all study phases, covering model construction, accompanying materials, and training. *(p.9)*
- Audio-label hardware: 3D-printed models augmented with conductive-PLA electrodes patched through to a Bare Conductive Touch Board, programmable as capacitive touch sensors. Touching a named electrode triggers playback of a pre-recorded MP3 label from the onboard microSD. Multiple Touch Boards can be chained when >12 electrodes are needed. *(p.8)*
- Interactive label design choices: short audio clips, labels triggered on finger release rather than touch start to avoid accidental playback while scanning, optional "full read-out" mode for overview, separate "description" mode for feature detail. *(p.8, p.9)*
- Campus-model case study: Monash University Clayton Campus, printed on Ultimaker 2 Extended, assembled from multiple tiles, augmented with audio labels, demonstrated at Round Table Conference to trainers and BLV experts. *(p.8, p.9)*

## Figures of Interest
- **Fig 1 (p.4):** The park map and train station map pair — both shown as 2D tactile graphic and as 3D printed model — with the exact recall and route-finding questions asked during the study.
- **Fig 2 (p.5):** Bar chart: average number of correct identifications on park-map by map format (3D > tactile). *(Shows main Hypothesis-1 result)*
- **Fig 3 (p.5):** Box plot: number of items for which confirmation or identification was required, by format. Less confirmation needed on 3D.
- **Fig 4 (p.6):** Box plot: park-map average number of correct answers to route-finding questions (mental model) by format. 3D significantly better.
- **Fig 5 (p.6):** Box plot: total time spent exploring the maps. Less time required on 3D.
- **Fig 6 (p.6):** Box plot: responses to "I was able to build a detailed mental model of the map", 3D higher.
- **Fig 7 (p.7):** Box plot: accuracy for small-feature recall (bridges, stairs); 3D significantly better.
- **Fig 8 (p.7):** Interactive Campus Map model; labelled with callouts for pathways, buildings, audio-label electrodes.
- **Fig 9 (p.8):** Interactive Campus Map: Model III detail with Bare Conductive Touch Board wiring visible.

## Results Summary
- **Identification accuracy:** Participants correctly identified significantly more features on the 3D printed maps than on the tactile graphics for both the park map (z=−2.34, p=0.01) and the station map (z=−2.28, p=0.03). This held when tactile-graphic familiarity was controlled for. *(p.5)*
- **Need for explanation:** Fewer items required confirmation or explicit labelling on the 3D model; several participants could name buildings, bridges, stairs, lakes without any legend on 3D but could not without the legend on the tactile graphic. *(p.5, p.6)*
- **Mental model formation:** Significantly more participants answered route/position inference questions correctly when using the 3D model (z=2.34, p=0.02). Subjective agreement with "I was able to build a detailed mental model" was also higher on 3D. *(p.6)*
- **Scanning time / speed:** Participants on average spent less total time exploring the 3D model before feeling they understood it; answering timed questions was ~6.63 × faster (sd=1.67) on 3D. *(p.6, p.7)*
- **Small-feature recognition (bridges, stairs, platforms):** 3D significantly better (z=2.34, p=0.02) — particularly relevant because these are the features where tactile graphics typically fail. *(p.6, p.7)*
- **Preference:** All 16 main-study participants preferred the 3D printed version. Trainers and BLV experts in the campus-model phase unanimously endorsed 3D printed models plus audio labels for O&M training and for presentation / education contexts. *(p.7, p.8, p.9)*
- **Trainer interviews:** 3D prints reduce the need to hand-translate conventions when teaching new clients; 3D allows features to be recognisable immediately (e.g. steps look like steps) rather than requiring learned 2D conventions. *(p.8, p.9)*
- **Qualitative user quotes (lightly paraphrased, individual single-subject statements):** participants stated that they could understand the 3D model because it "is a totally blind person, life is 3D"; that 3D is "more like a sighted person looks at things"; that they "got it at once" with the 3D model; and that they could remember more from having touched it. *(p.2, p.3)*

## Limitations
- Small sample size (N=16 for main study; 9 trainers; 4 experts). *(p.5)*
- Only two map contents (a park and a train-station platform area) — not generalised across all map genres (e.g. large-area street networks, topographic maps, floor plans were handled only qualitatively in pilot studies). *(p.3, p.4)*
- 3D prints have a limited print bed and thus a limited area that can be represented without tiling/joining. *(p.9)*
- Cost and print time: 3D prints take hours-to-days to produce (main-study 3D maps took "several hours" to ~21 hours; total campus-model + electronics prototype ~US$575). *(p.4, p.9)*
- Fragility: 3D models are more fragile than tactile graphics; thin protruding elements can break during handling. *(p.9)*
- Occlusion: complex 3D relief (tall buildings, high features) can occlude parts of the map from the haptic reader. *(p.8, p.9)*
- Availability of content: there is no established library / repository of BLV-friendly 3D map models analogous to OpenStreetMap; everything is currently bespoke. *(p.9)*
- Subjective preference may partly reflect novelty; longitudinal training effects not assessed. *(p.5, p.9)*

## Arguments Against Prior Work
- Prior tactile cartography work mainly produced 2D symbolised maps on swell paper or embossed paper; those require learned symbol keys and training for interpretation and have been shown in earlier work to be error-prone for BLV users. *(p.1, p.2)*
- Prior 3D tactile map attempts (Götzelmann; Taylor et al.; Gual et al.; Stangl et al.; Giraud et al.; Voigt & Martens; Ungar et al.; Brock et al.) either focused on production pipelines, were small demonstrations, or measured only isolated aspects; none had directly empirically compared 3D printed models to the prevailing 2D tactile graphic under controlled conditions for map use by BLV users. *(p.1, p.2)*
- Prior work on interactive tactile maps (Brock & Jouffrais; Brule et al.; Jones et al.) relied on expensive capacitive overlays or touchscreens with separate tactile overlays, which are not easily replicated at low cost; this paper argues a simpler conductive-filament + Touch Board + audio approach is both cheaper and more self-contained. *(p.2, p.8)*
- Gaul et al. [21]'s finding that 3D volumetric tactile symbols are recall-better than 2D symbols was limited to symbol recognition on tactile graphics, not full-map understanding; the current paper extends the comparison to whole-map navigation and mental-model formation. *(p.2)*

## Design Rationale
- **Use 3D print, not raised-line graphic, for buildings/structures/cityscapes:** because 3D representation is recognisable without training, maps to real object geometry, allows vertical symbolisation (height, relief) and supports volumetric features (stairs, bridges, steps). *(p.1, p.2, p.3, p.8)*
- **Supplement 3D with audio labels rather than Braille tags:** many BLV users (especially late-blind or older adults) do not read Braille; audio labels also save physical surface area that Braille would otherwise consume, and keep the map readable by sighted trainers. *(p.8, p.9)*
- **Use capacitive conductive-PLA electrodes rather than pressure switches:** because lightly brushing a feature should trigger audio without occluding haptic exploration. *(p.8)*
- **Trigger audio on finger release, not on initial contact:** to prevent spurious playback while scanning the map surface. *(p.8, p.9)*
- **Maintain consistent scale and orientation across tiles in the campus model:** so mental models transfer across tiles and so the map can be used alongside verbal orientation descriptions by trainers. *(p.8, p.9)*
- **Keep tactile graphic alongside 3D model when total coverage is needed:** because 3D prints can only cover a limited footprint and tactile graphics remain cheaper and faster for large area maps. *(p.9)*
- **Include both a "full read-out" mode and a per-feature description mode in the interactive audio-label system:** to support both overview and detail access without forcing one or the other. *(p.8, p.9)*

## Testable Properties
- BLV users will answer spatial recall questions about a park or train-station map with significantly higher accuracy using a 3D printed model than using a matched tactile-graphic version (Wilcoxon p<0.05). *(p.5)*
- BLV users will answer mental-model / route questions with significantly higher accuracy using a 3D printed map than using a tactile graphic. *(p.6)*
- BLV users will spend less total time exploring a 3D printed map than a tactile graphic to reach equivalent understanding. *(p.6, p.7)*
- Small vertical features (stairs, bridges, platforms) are significantly more likely to be correctly identified in the 3D condition than in the 2D condition. *(p.7)*
- Given a choice, a large majority of BLV users will prefer 3D printed maps over tactile graphics for the same content (main study: 16/16). *(p.7)*
- Interactive capacitive audio labels triggered on finger release produce fewer false-positive labels than audio triggered on initial contact. *(p.8, p.9)*
- 3D printed maps with paths narrower than ~2.5 mm in real scale will be hard to trace and thus reduce route-finding accuracy. *(p.9)*
- Guideline conformance check: a 3D map whose feature heights are too low (insufficient relief) will not improve over tactile graphics on small-feature recognition. *(p.9)*
- O&M trainers will report reduced training time on recognisable 3D features (steps, bridges, buildings) versus the equivalent 2D symbol on swell paper. *(p.8, p.9)*

## Guidelines from the paper (numbered, p.9–p.10)
1. Use a well-tested orientation and scale across the whole model; additional explanations (accompanying text) should describe the scale and orientation up front. *(p.9)*
2. The 3D model must physically allow the reader's fingers to easily explore salient features — appropriate raised path widths, feature heights, and adequate spacing for fingertip access. *(p.9)*
3. The height of buildings and walls should represent their relative height, but the vertical scale can differ from the horizontal scale. Heights should be low enough for the fingers to easily reach the base. *(p.9)*
4. Features like streets or paths that are intended to be traced by finger can be easily identified and followed if an indented path wide enough to contain the finger tip is used to complete the graphic. *(p.9)*
5. Where possible, use iconic 3D symbols to represent stairways, buildings and other 3-dimensional landmarks. *(p.9)*
6. Be careful to ensure that there are no sharp points on map elements that could cause discomfort if the touch reader moves their fingers over it quickly or places their hands on top of the map. *(p.9)*
7. When providing interactive audio-labels: (a) audio-labels must not be intrusive or distort the appearance of the 3D map; (b) triggering of auditory information should be the result of a definite action; (c) the use of different interaction gestures to convey levels of information allows users to build their understanding to the depth they wish. *(p.9)*
8. Useful ancillaries to include alongside a 3D-printed model: accompanying text, extra explanations about scale/units, and (if possible) a tactile graphic of the wider area. *(p.9)*
9. Structured touch-reading strategies for BLV users of 3D maps: (i) Instruction in techniques for reading 3D models is required, in the same manner that training is now given for reading tactile graphics; (ii) Encouragement is needed to feel the sides and base of objects, since an unfamiliar object may only be identified by feeling the top and the bottom; (iii) A quick overview of the model can be gained by placing both hands on top of the map. *(p.9, p.10)*

## Relevance to Project
- Provides empirical quantitative evidence that for BLV users 3D-printed models of geographic / architectural content outperform swell-paper tactile graphics on identification, mental-model formation, and feature-finding speed. This is directly usable as a prior for any inclusive-cartography design target. *(p.5, p.6, p.7)*
- Gives a concrete, reproducible authoring pipeline: PLA prints from desktop FDM printer + capacitive conductive-PLA electrodes + Bare Conductive Touch Board for audio labels, including the US$575 prototype cost figure, which sets a realistic cost envelope. *(p.8, p.9)*
- Delivers nine actionable design guidelines that can be operationalised into a rule-based checker for any 3D accessible map produced by the project. *(p.9, p.10)*
- Highlights open research questions that define the scope for future work in the collection: cheaper/faster printing, richer interaction modalities, automated map generation from GIS, shared repositories. *(p.9, p.10)*
- Methodologically, the paper is an example of the "small-N within-subjects non-parametric comparison" study design that the project's systematic-review protocol will need to judge: it is a good test case for whether the LLM-confidence-threshold critique should down-weight or up-weight this kind of evidence.

## Open Questions
- [ ] How do the significance results hold up in papers with larger N or with longitudinal exposure? The 16-participant sample is small.
- [ ] What is the generalisation behaviour for topographic / large-area maps, where a single 3D print cannot cover the area and tiling introduces discontinuity?
- [ ] Can the nine guidelines be encoded as an automatable conformance check?
- [ ] Do the quantitative advantages persist once users are fully trained on tactile-graphic conventions, or do they diminish?
- [ ] What does the interactive-audio-label technique cost at scale for multi-board meshes (where one Touch Board's 12 electrodes are insufficient)?

## Collection Cross-References

### Already in Collection
- [[Brock_2015_InteractiveMapsUsability]] — Holloway's ref [9]-[11] line. Groups Brock & Jouffrais with Brulé et al. and Jones et al. under the critique that prior interactive tactile maps "relied on expensive capacitive overlays or touchscreens with separate tactile overlays, which are not easily replicated at low cost" (line 176). Holloway positions its controlled 3D-vs-2D study as the next step beyond the empirical gap Brock's interactive study opened.
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — Holloway groups "Brule et al." with Brock & Jouffrais and Jones et al. (line 176 of this notes file) under the critique that prior interactive tactile maps "relied on expensive capacitive overlays or touchscreens with separate tactile overlays, which are not easily replicated at low cost." MapSense does use a consumer capacitive tablet + raised-paper overlay + conductive ink, so the cost critique largely applies. Holloway's conductive-filament + Touch Board alternative is a direct response to this hardware cost profile.
- [[Gual_2015_EffectVolumetric3DTactile]] — Holloway's ref [21]. Gual et al. (Applied Ergonomics 48:1-10) ran a counterbalanced N=16 study comparing a flat microcapsule map vs the same base enhanced with 3D-printed-ABS volumetric point symbols (3-8 mm tall) across three tasks (symbol ID, location without legend, location with legend) and reports reduced time and error counts for blind and visually impaired users on the 3D map with Mann-Whitney U significance in the blind subgroup. Holloway positions its own study as the direct next step — from Gual's symbol-level result to Holloway's whole-map PLA 3D-printed-model comparison — and explicitly describes Gual as "measured recall and manipulation of 3D symbols (but not full-map use)" at line 234 of this notes file.
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — Holloway classifies Götzelmann among prior 3D tactile map attempts that focused on production pipelines rather than controlled comparison studies; Holloway's study is positioned as addressing the empirical gap LucentMaps and peers left open.
- [[Taylor_2016_Customizable3DPrintedTactile]] — Holloway's ref [48] region. Taylor's customizable 3D-printed tactile map pipeline is in the same design tradition Holloway's controlled comparison evaluates.

### Cited By (in Collection)
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Wabinski, Moscicka & Touya (2022) cite Holloway, Marriott & Butler (2018) alongside Holloway, Marriott, Reinders & Butler (2019) as direct empirical support for the claim that 3D-printed tactile maps can outperform swell-paper tactile graphics. Holloway 2018 is used as an exemplar in Wabinski's production-method-sensitivity discussion, which argues symbol design choices cannot be decoupled from fabrication technique.
- [[Ducasse_2018_AccessibleInteractiveMapsVisually]] — Ducasse's survey treats Holloway's controlled 3D-vs-2D study as concurrent empirical evidence within the survey's DIM/HIM taxonomy.
- [[Brock_2015_InteractiveMapsUsability]] — Brock's reconciliation notes Holloway positions its 3D-printed comparative study as addressing the empirical gap Brock's interactive study opened.
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — Papadopoulos's reconciliation partitions the design space with Holloway: Holloway says "go from 2D tactile to 3D tactile for richer info," Papadopoulos says "don't fall back to verbal-only when tactile is an option."

### Conceptual Links (not citation-based)
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — Strong. Brulé's participatory-design paper produces qualitative evidence that VI children adopt interactive tactile maps quickly but offers no effect sizes; Holloway's controlled within-subjects 3D-vs-2D study provides the quantitative comparative data that Brulé lacks. Reading them together gives the complete evidence base — Brulé for "what children actually do with the tool in class", Holloway for "is 3D actually better than 2D for map comprehension".
- [[Gual_2015_EffectVolumetric3DTactile]] — Strong. Nested empirical layers of the same hypothesis ("volumetric > flat" for BVI tactile maps): Gual measures 3D point symbols on a swell-paper base at the symbol-recognition / single-task level, Holloway measures full 3D-printed PLA models vs swell-paper tactile graphics at the whole-map comprehension / feature-finding level. Results point the same direction; Holloway's larger 3D-print region replaces Gual's hybrid swell+3D-overlay stack. Together they bracket the design space from "augment the swell paper with a few 3D symbols" to "print the entire map in 3D."

## Related Work Worth Reading
- Brock, Truillet, Oriola, Picard, Jouffrais — Interactive audio-tactile maps for visually impaired people (multiple, 2015–2017) — closest prior interactive-tactile-map baseline. *(Refs [9]–[11])*
- Gual, Puyuelo, Lloveras — 3D volumetric tactile symbols (2014, 2015) — measured recall and manipulation of 3D symbols (but not full-map use). *(Ref [21])* → NOW IN COLLECTION: [[Gual_2015_EffectVolumetric3DTactile]]
- Götzelmann — tactile maps from crowdsourced geographic data (2016); generation pipelines for 3D printable maps. *(Refs [22]–[25])*
- Taylor, Dey, Siewiorek, Smailagic — TactileMaps.net: web interface for customized 3D-printable tactile maps (2015). *(Ref [48])*
- Wright, Harris, Sticken — best-evidence synthesis of tactile maps/models research for O&M (2010). *(Ref [54])*
- Ungar, Blades, Spencer — role of tactile maps in mobility training (1993). *(Ref [49])*
- Voigt, Martens — 3D tactile models for partially sighted spatial orientation (2006). *(Ref [50])*
- Zeng, Weber — Accessible maps for the visually impaired (2011). *(Ref [55])*
