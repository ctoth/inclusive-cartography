---
title: "Interactivity Improves Usability of Geographic Maps for Visually Impaired People"
authors: "Anke M. Brock, Philippe Truillet, Bernard Oriola, Delphine Picard, Christophe Jouffrais"
year: 2015
venue: "Human-Computer Interaction, 30(2), 156-194 (Taylor & Francis); HAL preprint hal-01077434 (accepted manuscript)"
doi_url: "https://doi.org/10.1080/07370024.2014.924412"
pages: 47
---

# Interactivity Improves Usability of Geographic Maps for Visually Impaired People

## One-Sentence Summary
An empirical comparison showing that a multi-touch + raised-line-overlay + speech-output interactive tactile map is significantly more efficient (≈2.6x faster learning) and more satisfying for 24 blind adults than a classical raised-line map with braille legend, while long-term recall after 2 weeks is comparable for landmarks, routes, and survey knowledge across both map types *(p.2, p.22, p.27)*.

## Problem Addressed
Tactile relief maps for the visually impaired carry severe intrinsic limitations — limited information density, reliance on braille (only 10–15% of VI people read braille in the US per NFB; see p.6), confusing symbols, small legends, and lack of dynamic updates *(p.5–6)*. Interactive tactile maps had been proposed as an alternative, but no study had rigorously compared the *usability* of an interactive map against a classical raised-line map using established efficiency/effectiveness/satisfaction metrics on a reasonable sample of blind users *(p.7–9)*. This paper fills that gap with a controlled within-subjects study.

## Key Contributions
- First direct within-subjects usability comparison of an interactive audio-tactile map against a classical braille-legend raised-line map with 24 blind adults *(p.2, p.16)*.
- Empirical evidence that replacing braille legends with simple single-finger audio-tactile interaction significantly improves efficiency (learning time) and user satisfaction (SUS) without harming effectiveness (spatial knowledge acquisition) *(p.22–24)*.
- Construction and open documentation of a reproducible interactive map prototype built from commodity hardware: 3M M2256PW 22" multi-touch display + A3 thermoformed raised-line overlay + speech synthesis via SAPI 4.0 / TTS, integrated through Microsoft Speech Application Programming Interface v4 *(p.11–13)*.
- Design guidance based on adherence to published tactile-map design rules (Edman 1992; Picard 2012) — symbols, line widths, spacing, braille dimensions — showing interactive maps can satisfy classical accessibility guidelines while adding audio augmentation *(p.13)*.
- A long-term (2-week delayed) evaluation of spatial memory following tactile map exploration — finding that landmark knowledge decays much more than route or survey knowledge, and that learners' confidence is misleading after delay *(p.27–28, p.33–34)*.
- Observation that user self-reported confidence after exploration correlates with efficiency/satisfaction short-term but does NOT track long-term effectiveness: confidence is a misleading proxy for acquired spatial knowledge after two weeks *(p.26, p.28, p.33)*.

## Study Design (empirical papers)
- **Type:** Controlled within-subjects experimental study with a short-term laboratory phase and a long-term delayed-recall phase via telephone interview *(p.18–19)*.
- **Population:** N = 24 blind adults (12 women, 12 men) recruited from IJA (Institut des Jeunes Aveugles, Toulouse) and CSJDV-IJA Villeurbanne; age M = 42 years, SD = 13.15; age at onset of blindness from 0 to 27 (M = 8.71, SD = 8.51); braille reading proficient across scale 1–4, M = 3.3, SD = 1.1; 13 congenital, 11 acquired blindness; various occupations from lawyer/accountant to teacher/student/retired; detailed demographic table on p.16 *(p.15–17)*.
- **Inclusion criteria:** Total or near-total blindness (visual impairment was progressive in two cases; the second value in the age-at-onset column indicates age at total blindness). Excluded participants with known neurological or psychiatric dysfunction *(p.16)*.
- **Intervention (IM):** Interactive map — multi-touch 3M M2256PW 22" capacitive display + A3 raised-line thermoformed overlay without braille, with vacuum-formed 0.4 mm thick PET-G overlay; single-finger touch triggered speech output naming the underlying element via SAPI 4.0 TTS. Double-tap avoided to prevent false triggers during exploration *(p.11–13)*.
- **Comparator (PM):** Classical paper raised-line map — identical A3 raised-line layout but with a braille legend (size 32, line spacing 125%) glued to the back of a second A3 sheet *(p.14)*.
- **Two maps × two conditions = 4 variants:** Map content 1 interactive, 1 braille, 2 interactive, 2 braille — presented in counterbalanced order so each subject saw each map content once and each condition once, but on different contents (within-subjects, counterbalanced order) *(p.14, Figure 2)*.
- **Primary endpoints:** Efficiency (learning time until the participant felt comfortable with the map — capped at 30 minutes), Effectiveness (spatial knowledge acquisition score: six questions per category × L/R/S = 18 questions), Satisfaction (SUS / System Usability Scale, French version, Brooke 1996) *(p.17, p.20)*.
- **Secondary:** Users' confidence (5-point Likert after answering each spatial question), long-term recall after 2 weeks via phone, long-term confidence *(p.20, p.27)*.
- **Follow-up:** One in-lab session (short-term) plus one telephone interview 2 weeks later lasting 10–15 minutes *(p.20)*.

## Methodology
The experiment is a within-subjects counterbalanced design. Each participant used both maps (PM, IM) in one laboratory session, with a one-week familiarization/informed-consent call before the session and a telephone recall interview 2 weeks after. Experimental session structure *(p.18, Figure 4)*:

1. Introduction, informed consent.
2. Familiarization with first map type (learn symbols and interaction).
3. Interview about personal characteristics.
4. Map 1 exploration to comfort threshold (≤30 min).
5. Spatial questions (18 questions: 6 landmark L, 6 route R, 6 survey S).
6. SUS satisfaction survey.
7. Repeat 2-6 with second map type.
8. Two weeks later: phone call, second round of spatial questions from memory + confidence ratings.

### Hypotheses *(p.9–10)*
1. **Efficiency:** IM has shorter learning time than PM (braille reading is slow; see Hinton 1993).
2. **Effectiveness:** IM and PM yield equivalent spatial knowledge because spatial content is identical in the raised-line overlay.
3. **Satisfaction:** IM yields higher SUS scores than PM.

### Map Design Rules Applied *(p.13)*
- Followed Edman (1992) and Picard (2012) for tactile map design.
- Minimum symbol sizes respected.
- Different textures and heights used for buildings, routes of different widths.
- Braille legend on PM: size 32 with 125% line spacing; printed on Tiger printer 1330dh from ViewPlus with max 100 characters per page.
- Interactive map printed with PicoZine cloning-on-demand vacuum former; overlays created with PETG 0.4 mm.
- Legend contained 6 categories: streets, single/couple/three-dot POIs, building outlines, central buildings (hotel), route lines of 3 widths (smallest 1.4 mm, largest 4 mm).

### Map Content *(p.14)*
- Two different neighborhood-style map contents were created.
- Each had same number of POIs (6 per category) and same abstract topology so results can be compared across contents.
- Open Source Inkscape software + SVG Scalable Vector Graphics used to build the maps.
- Each content existed in both interactive (no legend) and braille (with legend) form.
- Lexique database NOS8/French lexicon used to select street names of matched high frequency (POI0 counterbalanced with high frequency words).

## Key Equations / Statistical Models

Paper uses standard inferential statistics rather than closed-form equations. Core analyses:

- **Learning time (Efficiency):** Mixed / repeated-measures ANOVA on log-transformed learning time with factor Map Type (PM vs IM). Reported F(1,12) = 4.8, p = .05, η² = .28 with a 2.63x speedup (IM faster) *(p.22)*. Log transform applied because variances were non-homogeneous (Wilcoxon rank sum, non-parametric check also applied).
- **Spatial Learning (Effectiveness):** 2-way repeated-measures ANOVA with factors Map Type (PM, IM) × Question Type (L, R, S).
  - Effect of Map Type: F(1,22) = 0.45, p = .51 → no significant effect, consistent with hypothesis of equivalence *(p.23)*.
  - Effect of Question Type: F(2,22) = 4.59, p = .04 → significant effect of the knowledge type with L (landmark) > R (route) > S (survey) *(p.23)*.
  - Interaction Map × Type: F(2,22) = 0.08, p = .79 → no interaction *(p.23)*.
  - Post-hoc pairwise Wilcoxon rank-sum with Bonferroni correction (alpha = .017): Landmark > Route (Z = 4.5, p < 5.2e-6), Landmark > Survey (Z = 4.1, p < 4e-5), Route ≈ Survey (n.s. after correction) *(p.24)*.
- **User Satisfaction (SUS):** SUS scores on French version ranged 45–100; mean 83.8, SD 13.9. Shapiro-Wilk W = 0.85, p < .001 → not normally distributed. Used Wilcoxon signed rank test: interactive map SUS M = 88.1, SD = 10.7; paper map M = 79.5, SD = 15.9; difference significant Z = 3.7, p < .001 *(p.24–25)*.
- **Users' Confidence (short-term):** 5-point Likert. Wilcoxon signed-rank on pooled responses showed higher confidence for IM overall (Z = 3.87, p < 0.01). For landmark questions: Z = 2.22, p = 0.04; for route: p = .24 (n.s.); for survey: p = .15 (n.s.) — confidence advantage of IM exists mostly for landmark-type responses *(p.26)*.
- **Long-term recall:** Wilcoxon signed-rank comparing short-term vs long-term scores within map type.
  - L (landmark): PM 14.54 → 7.99, 45% decrease, p < .001; IM 14.48 → 7.79, 47% decrease, p < .001.
  - R (route): PM decrease 21%, Z = 4.72, p < .001; IM decrease from 7.69 → 6.06, 3.14, 13% decrease, Wilcoxon N = 38, Z = 3.99, p < .001.
  - S (survey): similar significant decreases in both conditions *(p.27–28)*.
  - Overall, landmark knowledge decays most sharply, route and survey more robust.
- **Long-term users' confidence:** Did NOT track decay of effectiveness — confidence remained high while spatial scores dropped. Wilcoxon signed-rank showed significant decreases in confidence for PM (Z = 4.33, p < .001) but the magnitude didn't match the effectiveness loss — confidence is misleading as a proxy for acquired knowledge *(p.28)*.
- **Correlation analysis (Figure 8):** Spearman correlations between dependent variables, age-related factors, and personal characteristics; visualised as a network with strength-coded edges (Bastian, Heymann & Jacomy 2009, Gephi). New technology frequency correlated with learning-time IM (positively for experience reducing time), braille reading years correlated with satisfaction on paper map, travel_ease and age correlated with multiple measures *(p.26)*. Edge colors: magenta = positive, blue = negative. Edge widths at 3 thresholds: p < .05, p < .01, p < .001.

## Parameters

### Map design parameters (raised-line and interactive) *(p.13–15)*

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Braille character size (PM legend) | — | pt | 32 | — | 14 | Tiger printer 1330dh ViewPlus, 100 chars/page max |
| Braille line spacing (PM legend) | — | % | 125 | — | 14 | — |
| Minimum line width (routes) | — | mm | 1.4 | 1.4–4.0 | 13–14 | Three widths used in maps |
| Thickest route width | — | mm | 4.0 | — | 14 | Major roads |
| Overlay material thickness (IM) | — | mm | 0.4 | — | 13 | PET-G plastic vacuum-formed |
| Paper size | — | — | A3 | — | 13 | Both maps |
| Number of POI categories | — | — | 6 | — | 14 | streets, 1-POI, 2-POI, 3-POI, building outlines, hotel |
| POIs per category | — | — | 6 | — | 14 | Counterbalanced |
| Number of street names per map | — | — | 6 | — | 14 | From Lexique DB |
| Display size | — | inches | 22 | — | 13 | 3M M2256PW multi-touch |
| Touch input method | — | — | single-tap | — | 12 | Single-finger touch triggers TTS |
| Speech stack | — | — | SAPI 4.0 / TTS Real Speak | — | 12 | Microsoft Speech API |
| Software architecture | — | — | modular | — | 12 | IvyBus (Buisson 2002) messaging |
| Max learning time cap | t_max | minutes | 30 | — | 19 | Hard ceiling before abort |
| Min required learning time | t_min | minutes | 0 | — | 19 | No minimum imposed |

### Study parameters *(p.16–20)*

| Name | Symbol | Units | Default | Range | Page | Notes |
|------|--------|-------|---------|-------|------|-------|
| Participants (total) | N | — | 24 | — | 15–16 | 12F / 12M blind adults |
| Participant age | — | years | 42 (M), 13.15 (SD) | — | 16 | — |
| Age at onset of blindness | — | years | 8.71 (M), 8.51 (SD) | 0–27 | 16 | Second value = age at total blindness if progressive |
| Braille reading scale | — | 1–4 | 3.3 (M), 1.1 (SD) | — | 16 | Self-rated |
| New-technology scale | — | 1–6 | 4 (M), 0.93 (SD) | — | 16 | Mean tech familiarity |
| Santa Barbara Sense of Direction | SBSOD | 1–7 | 3.87 (M), 0.88 (SD) | — | 16 | Self-report direction sense |
| SUS French version | — | 0–100 | 83.8 (M), 13.9 (SD) | 45–100 | 25 | Not normally distributed (Shapiro-Wilk W = 0.85, p < .001) |
| SUS — Interactive map | — | 0–100 | 88.1 (M), 10.7 (SD) | — | 25 | Significant advantage |
| SUS — Paper map | — | 0–100 | 79.5 (M), 15.9 (SD) | — | 25 | — |
| Learning time PM mean | t_PM | min | (mean PM > IM by 2.63x factor) | — | 22 | PM ≈ 14 min vs IM ≈ 5.4 min approx from log plot |
| Number of spatial questions | Q | — | 18 | — | 20 | 6 L + 6 R + 6 S |
| Max L score | — | — | 6 | 0–6 | 20 | Landmark |
| Max R score | — | — | 6 | 0–6 | 20 | Route |
| Max S score | — | — | 6 | 0–6 | 20 | Survey |
| Max confidence score | — | Likert | 5 | 1–5 | 20 | After each question |
| Long-term follow-up delay | — | weeks | 2 | — | 20 | Phone interview |
| Long-term interview duration | — | min | 10–15 | — | 27 | — |

## Effect Sizes / Key Quantitative Results

| Outcome | Measure | Value | CI | p | Population/Context | Page |
|---------|---------|-------|----|---|--------------------|------|
| Learning time IM vs PM | ANOVA F | F(1,12)=4.8 | — | .05 | 24 blind, within-subjects | 22 |
| Learning time IM vs PM | ratio | IM ≈ 2.63× faster | — | — | log-transformed means | 22 |
| Spatial learning Map Type effect | F | F(1,22)=0.45 | — | .51 | n.s. as predicted | 23 |
| Spatial learning Question Type effect | F | F(2,22)=4.59 | — | .04 | L>R>S | 23 |
| Map × Type interaction | F | F(2,22)=0.08 | — | .79 | n.s. | 23 |
| L vs R post-hoc | Wilcoxon Z | Z=4.5 | — | <5.2e-6 | Bonferroni alpha=.017 | 24 |
| L vs S post-hoc | Wilcoxon Z | Z=4.1 | — | <4e-5 | Bonferroni alpha=.017 | 24 |
| SUS IM > PM | Wilcoxon signed-rank Z | Z=3.7 | — | <.001 | 24 | 25 |
| SUS mean (overall) | M (SD) | 83.8 (13.9) | — | — | 24 | 25 |
| SUS mean IM | M (SD) | 88.1 (10.7) | — | — | 24 | 25 |
| SUS mean PM | M (SD) | 79.5 (15.9) | — | — | 24 | 25 |
| Confidence IM > PM overall | Wilcoxon Z | Z=3.87 | — | <0.01 | 24 | 26 |
| Confidence L questions IM > PM | Wilcoxon Z | Z=2.22 | — | .04 | 24 | 26 |
| Confidence R questions | — | n.s. | — | .24 | 24 | 26 |
| Confidence S questions | — | n.s. | — | .15 | 24 | 26 |
| L short→long decrease PM | % change | -45% | — | <.001 | 24 | 27 |
| L short→long decrease IM | % change | -47% | — | <.001 | 24 | 27 |
| R short→long decrease PM | % change | -21% | — | <.001 | 24 | 28 |
| R short→long decrease IM | % change | -13% | — | <.001 | 24 | 28 |

## Methods & Implementation Details
- Experimental map prototype built with commodity multi-touch display (3M M2256PW 22", IR capacitive with projected capacitive) covered by a raised-line thermoformed overlay *(p.11–12)*.
- Vacuum forming via HP EliteBook 8530p + commodity PETG 0.4 mm plastic on the PicoZine device yielded overlays aligned by corner registration marks; simple manual alignment was sufficient for the experiment *(p.11–13)*.
- Software architecture modular: input handling, map model/state, TTS output decoupled; uses IvyBus messaging to connect touch driver, map lookup table, and speech output; developed in C# *(p.12)*.
- Touch recognition: single-finger tap is taken as the unit of intention; multi-touch intentionally disabled to avoid ambiguous triggers during exploratory sweeping with multiple fingers — this matches Kane/McGookin findings that blind users accidentally trigger multiple touches during tactile exploration *(p.12)*.
- Accidental speech output disabled by double-tap design and Talking TMAP approach (Miele et al. 2006) — Brock notes that they deliberately *avoided* double-tap because multiple blind users reported struggling with it; instead used simple single tap with tap-and-hold differentiation *(p.12–13)*.
- Speech output: re-synthesis text cached and pre-generated per label to minimize latency; volume set constant to audible level during experiment; mittens worn by the user (Figure 1) to reduce palm touches *(p.12)*.
- Map pairs: two map content layouts created to prevent memorization transfer between conditions. Each content had identical topology and POI density — 6 categories × 6 POIs = 36 labelled items + street network + building outlines *(p.14)*.
- 30-minute learning time cap imposed to prevent exhaustion and floor/ceiling effects; spatial knowledge test administered immediately after each map phase *(p.19)*.
- Spatial knowledge test: 18 questions — 6 Landmark (what is at X?), 6 Route (how do you go from X to Y?), 6 Survey (what is NE of X? estimate distance). Structure described in Figure 5 with sub-blocks L-POI, L-S, R-DE, R-R, R-wD, S-Dir, S-Loc, S-Dist — each combining 1-4 sub-questions. Route estimation had 6 sub-types: direction estimation, route estimation, cardinal estimation, etc. *(p.21)*.
- Responses scored with Bonferroni-corrected pairwise rank tests; confidence scored on 5-point Likert after each question.
- Confidence and effectiveness tracked across short-term and long-term phases.
- Long-term phase: no pre-announcement of recall test — done to measure genuine retention.

## Figures of Interest
- **Fig 1 (p.12):** Photograph of blind user exploring interactive map with raised-line overlay, wearing mittens to reduce touch triggers.
- **Fig 2 (p.14):** Four map variants — content 1/2 × interactive/braille-legend.
- **Fig 3 (p.16):** Participant characteristics table (demographics).
- **Fig 4 (p.18):** Experimental design flowchart — short-term study (orange) and long-term study (blue).
- **Fig 5 (p.21):** Structure of 18 spatial questions organized by landmark / route / survey sub-categories.
- **Fig 6 (p.23):** Learning time bar chart — IM significantly faster than PM (≈2.63x).
- **Fig 7 (p.24):** Mean L/R/S scores by map type + landmark > route ≈ survey ordering.
- **Fig 8 (p.26):** Correlation network (Spearman) between dependent variables, user characteristics, and age — edges colored magenta/blue by sign.
- **Fig 9 (p.28):** Short-term vs long-term spatial scores and confidence decay per question type.

## Results Summary
- **Efficiency (learning time):** Interactive map is significantly faster, with a ≈2.63x speedup (p = .05). Interpreted as the braille reading overhead in PM dominating.
- **Effectiveness (short-term spatial knowledge):** No significant difference between map types for any question type (L, R, S). Hypothesis 2 confirmed — identical raised-line spatial content, so equivalent effectiveness.
- **Effectiveness breakdown by question type:** Landmark scores highest, route intermediate, survey lowest — consistent with spatial cognition literature showing survey-type (configural) knowledge is hardest to acquire from tactile exploration.
- **Satisfaction (SUS):** Interactive map significantly higher SUS (88.1 vs 79.5, p < .001). 17/24 participants preferred interactive map. "Excellent" SUS ratings: 13/24 on IM vs 6/24 on PM. Most participants cited that interactive map was less tiring, easier to learn, and avoided braille reading fatigue.
- **Users' confidence short-term:** Higher for IM overall (Z=3.87, p<0.01); driven mostly by landmark questions.
- **Long-term recall (2 weeks):** Landmark knowledge decayed 45–47% across both map types; route decayed 13–21%; survey scores also decayed but less dramatically. No significant long-term effectiveness difference between map types — memory durability not enhanced by interaction per se.
- **Long-term confidence:** Significantly decreased but not enough to match the effectiveness decay — users systematically over-estimated their retained spatial knowledge. Confidence is misleading as a proxy for spatial knowledge after delay.

## Limitations
- Learning time capped at 30 min — may create floor effects; some participants on PM could have continued learning beyond cap *(p.19)*.
- Small sample N=24, heterogeneous population (age 18–66, varying braille skill, varying tech familiarity) reduces statistical power for subgroup analyses *(p.16)*.
- Only two map contents tested — ecological validity may not generalize to real maps with more complex topology, more categories, real streets *(p.14)*.
- Single-location, lab-based study — no test on ecological navigation or wayfinding transfer *(p.32–33)*.
- No assistive technology comparison beyond raised-line baseline — doesn't compare to GPS navigation apps, talking maps, etc. *(p.31)*.
- Confounding: IM prototype was heavier and more expensive hardware than PM — aesthetic/effort confounds may drive some SUS difference *(p.32)*.
- Heterogeneous blindness onset (congenital vs late-blind) — authors note that their spatial cognition literature suggests these groups differ in spatial ability, but the sample was too small to segment *(p.17)*.
- Confidence ratings may be biased by recency; not independently validated against external spatial knowledge tests beyond the 18-question test.

## Arguments Against Prior Work
- Prior interactive maps (Parkes 1988 NOMAD and follow-ups by Jacobson, Wang, Zhao, Kane, Miele, McGookin) had NOT been compared head-to-head in a controlled usability study with blind users — prior work was mostly prototype demonstrations with limited quantitative usability measures *(p.6–7, p.29–30)*.
- Landau's PAF (Personal Audio Foot) and Talking Tactile Tablet by Touch Graphics, and iPhone VoiceOver-based maps: these either require specialized expensive hardware (PAF) or use small screens unsuitable for raised-line overlays *(p.7–8)*.
- Talking TMAP/Talking TMAP2 (Miele 2006) used double-tap gestures that Brock et al. found blind users struggled with; this study argues for simpler single-touch input *(p.12)*.
- Earlier studies using touchscreens for visually impaired (McGookin et al. 2008) reported accidental triggering from multiple fingers and palm touches during exploration — solved here by single-touch handling, mittens, and vacuum-formed overlay *(p.12)*.
- Prior work on NOMAD, AudioTouch (Wang et al. 2009), etc., lacked systematic usability evaluation with blind users; this paper directly addresses that gap *(p.29–30)*.
- Assumption in prior work that interactive maps are *more effective* than raised-line — this paper shows effectiveness is equivalent for spatial knowledge acquisition; the advantage is in efficiency and satisfaction, not effectiveness *(p.22–24)*.
- Design recommendation literature (Edman, Picard) has not been empirically tested for transfer to interactive maps — this paper shows the rules still apply *(p.13)*.

## Design Rationale
- **Why multi-touch + raised-line overlay?** Users need tactile exploration to locate features (raised-line carries spatial info) and audio labels to identify them (avoiding braille). Combining them uses cross-modal reinforcement and the overlay keeps classical tactile-map design rules applicable *(p.10–11, p.13)*.
- **Why single-touch instead of multi-touch gestures or double-tap?** Blind users generate many accidental touches during exploration; double-tap was previously reported as unreliable. Single tap with tap-and-hold is simpler and more robust *(p.12)*.
- **Why not stylus-only?** Tactile exploration with multiple fingers is faster than single-stylus scanning; stylus prevents tactile pattern perception *(p.10–11)*.
- **Why commodity hardware?** To show that interactive tactile maps can be built with off-the-shelf components rather than specialized expensive devices — reducing barriers to deployment *(p.11)*.
- **Why A3 paper size?** Balances information density, readability of braille for the control condition, and tactile exploration range *(p.13–14)*.
- **Why counterbalance map content and order?** To prevent learning-transfer between conditions and to separate map-type effects from content-familiarity effects *(p.14, 18)*.
- **Why SUS as satisfaction metric?** Well-validated French translation, widely used benchmark, non-parametric scoring works with small non-normal samples *(p.24)*.
- **Why 2-week delay for long-term test?** Long enough for memory consolidation effects, short enough for reasonable participant retention *(p.20, 27)*.
- **Why not pre-announce long-term test?** To measure genuine incidental retention, not strategic rehearsal.
- **Why 3 question types (L/R/S)?** Follow established spatial cognition taxonomy: landmark = declarative, route = procedural/sequential, survey = configural/allocentric; each taps different memory systems *(p.4, p.20)*.

## Testable Properties
- Interactive audio-tactile map reduces learning time for a new map by a factor of ≈2.6 compared to braille-legend raised-line map *(p.22)*.
- SUS score of interactive map > SUS score of braille map by ≈8.6 points on average *(p.25)*.
- No significant spatial-knowledge difference (p > .05) between map types for landmark, route, or survey questions *(p.23)*.
- Landmark knowledge decays by ~45% over 2 weeks regardless of map type *(p.27)*.
- Route knowledge decays less than landmark knowledge (13–21% vs 45–47%) *(p.28)*.
- User confidence after exploration is NOT a reliable indicator of long-term effectiveness — confidence decay lags behind score decay *(p.28, p.33)*.
- Classical tactile map design rules (Edman/Picard) can be applied to interactive maps without sacrificing usability *(p.13)*.
- Single-touch input outperforms double-tap for blind users exploring tactile maps *(p.12)*.
- Landmark > Route ≈ Survey ordering of question-type difficulty holds across map type *(p.23)*.

## Relevance to Project
High relevance to the inclusive-cartography systematic review on cognitive accessibility of maps for visually impaired users.

- Provides a rigorous baseline for the claim that **interactivity improves map usability** — a foundational piece often cited by later audio-tactile, vibrotactile, and AR tactile-map systems.
- Gives concrete empirical parameters (N=24, SUS scores, learning-time ratio, L/R/S decomposition) usable as benchmarks for newer interactive-map studies.
- Provides a critical caveat for the Wabiski 2026 cognitive review protocol: users' self-reported **confidence is misleading** after delay — any instrument relying on user-confidence for effectiveness assessment will over-estimate retained knowledge. Directly relevant to the protocol's LLM-confidence thresholds critique (the meeting Q is preparing for tomorrow).
- Establishes the precedent that effectiveness is determined by spatial *content*, not interaction modality — a finding that bounds the claimed benefits of novel interaction techniques.
- Demonstrates a reproducible build from commodity hardware (3M multi-touch + PETG overlay + SAPI TTS).
- Confirms L > R > S difficulty ordering which should inform weighting of question types in evaluation instruments.

## Open Questions
- [ ] Does a single-touch design still dominate with modern capacitive sensing that can distinguish palm vs fingertip?
- [ ] Would larger sample sizes with congenital vs late-blind subgroup analyses reveal effectiveness differences the current study couldn't detect?
- [ ] How do these findings transfer to dynamic/real-world maps with live updates (e.g., GPS route guidance)?
- [ ] Does audio augmentation change the route-vs-survey knowledge acquisition profile if audio verbally encodes configural relations?
- [ ] Would non-speech sonification (spatial audio) complement or replace TTS for identification?
- [ ] Why is confidence long-term so persistent compared to effectiveness — is this a general property of tactile memory or specific to map exploration?
- [ ] Can the learning-time advantage be decomposed into "time saved not reading braille" vs "time saved via faster lookup" vs "time saved via better legend organization"?
- [ ] Would a hybrid approach (audio primary, optional braille) outperform either alone?

## Related Work Worth Reading
- Parkes (1988) — NOMAD, original interactive tactile map prototype.
- Edman (1992) — Tactile Graphics design rules.
- Picard (2012) — Modern tactile map production guidelines.
- Miele, Marston, Landau (2006) — Talking TMAP, double-tap interactions.
- McGookin, Brewster & Jiang (2008) — Investigations into touchscreen accessibility.
- Kane, Bigham, Wobbrock (2008) — SlideRule touchscreen accessibility.
- Thinus-Blanc & Gaunet (1997) — Representation of space in blind persons (classic review).
- Hegarty & Waller — Santa Barbara Sense of Direction Scale (used as personal-characteristic measure).
- Brooke (1996) — SUS System Usability Scale.
- Landau & Wells (2003) — Tactile map effectiveness baseline.
- Jacobson (1998) — Tactile maps for orientation/mobility.
- Tatham (1991) — US braille reading statistics (only 10% of legally blind US adults read braille).
- Hatwell, Streri & Gentaz (2003) — Touching for Knowing, tactile cognition.
- Ungar (2000) — Cognitive mapping without visual experience.
- Siegel & White (1975) — Landmark/Route/Survey knowledge taxonomy.
- Thorndyke & Hayes-Roth (1982) — Spatial knowledge acquisition differences between map and navigation learning.

## Collection Cross-References

### Already in Collection
- None of the references cited by this paper are currently present in the collection as dedicated paper entries. The closest match is Perkins (2001) "Tactile campus mapping" which is a different paper from the collection's [[Perkins_2002_CartographyProgressTactileMapping]] but by the same author and in the same research program.

### New Leads (Not Yet in Collection)
- Parkes, D. (1988). NOMAD — first audio-tactile interactive map system; foundational prior work for interactive tactile maps.
- Miele, J. A., Landau, S., & Gilden, D. (2006). Talking TMAP — used the double-tap interactions that this paper explicitly argued against.
- Edman, P. (1992). Tactile graphics — canonical tactile map design rules applied in the raised-line overlay.
- Picard, D. (2012). VISUO-TACTILE ATLAS — modern tactile map production guidelines.
- Brooke, J. (1996). SUS — System Usability Scale (methods paper, used for the satisfaction measurement).
- Thinus-Blanc, C., & Gaunet, F. (1997). Representation of space in blind persons — foundational review of blind spatial cognition.
- Hegarty, M. et al. (2002). Santa Barbara Sense of Direction Scale — participant characteristic instrument used here.
- McGookin, Brewster & Jiang (2008). Investigating touchscreen accessibility for people with visual impairments — key prior work on touchscreen false-trigger issues.
- Kane, Bigham & Wobbrock (2008). SlideRule — touchscreen accessibility for blind users.
- Siegel & White (1975). Landmark/Route/Survey knowledge taxonomy — spatial cognition framework used to structure the 18-question test.
- Thorndyke & Hayes-Roth (1982). Map vs navigation spatial knowledge differences.
- Ishikawa, Fujiwara et al. (2008). Wayfinding with GPS vs maps vs direct experience.
- Jacobson, R. D. (1998). Audio-tactile approach to navigating maps with little or no sight.
- Zhao, Plaisant, Shneiderman & Lazar (2008). Data Sonification for Users with Visual Impairment.
- Yatani, Banovic & Truong (2012). SpaceSense — spatial tactile feedback on mobile devices.
- Poppinga, Magnusson et al. (2011). TouchOver map — audio-tactile mobile map exploration.
- Giudice, Palani, Brenner & Kramer (2012). Touch-based vibro-audio graphical information — directly related to the same problem space.

### Supersedes or Recontextualizes
- (none — this paper is an early empirical baseline and does not supersede any collection paper)

### Cited By (in Collection)
- [[Ducasse_2018_AccessibleInteractiveMapsVisually]] — cites this paper as the "primary empirical reference for the review's ITM claims"; notes that interactive condition improved both label recall and layout accuracy, with the effect larger at one week than immediately post-learning; treats this as a replication target for one-week retention comparisons. Ducasse is co-authored by Brock, so this is an author-continuation link. Ducasse also lists an explicit open question asking for "exact numerical effect sizes for Brock et al. 2015 one-week retention comparison" — this paper's 2-week recall data (L: -45% to -47%, R: -13% to -21%) partially answers that, though Ducasse focuses on the Brock PhD 1-week extension.
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — references Brock-coauthored prior work on TactiPad / interactive tactile maps for VI adults; Brock is also a co-author of Brulé 2016, making this a direct research-lineage link.
- [[Holloway_2018_AccessibleMapsBlindComparing]] — cites Brock et al. as one of the prior 3D/interactive tactile map attempts that either focused on production pipelines or had limited controlled comparisons; Holloway positions their own 3D-printed comparative study as addressing the empirical gap this paper's interactive study opened.
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — lists "Brock & Jouffrais (2015). Interactive Audio-tactile Maps for Visually Impaired People" as a collection lead; Götzelmann's Lucent Maps design is positioned as a more affordable audio-visual 3D alternative to the Brock-style raised-overlay-on-multitouch approach.
- [[Gual_2015_EffectVolumetric3DTactile]] — mentions Brock et al. 2015 in a broader list of prior tactile/3D map work that was judged insufficient to substitute controlled comparison of 3D printed vs 2D tactile graphics.
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — references Brock et al. 2015 as present in the collection for interactive tactile map usability in the O&M space.
- [[Rowell_2003_WorldTouchResultsInternational]] — mentions Brock-coauthored later work in its forward-reconciliation placeholder (Rowell predates Brock 2015, so the direction of reference is forward in time from Rowell's reconcile pass).

### Conceptual Links (not citation-based)

**Confidence-vs-truth measurement (directly relevant to the protocol-critique meeting):**
- [[Kadavath_2022_LanguageModelsMostlyKnow]] — Kadavath studies LLM self-assessed confidence vs actual answer correctness; Brock here provides the *human* analogue — blind users' self-reported confidence after tactile map exploration correlates with spatial scores short-term but NOT long-term (landmarks decay ~45% while confidence holds). This is a cross-species replication of "confidence is a noisy proxy for retained knowledge" and directly bears on the Wabiski_2026 protocol's LLM-confidence threshold (>0.90 auto-include) critique: if confidence-effectiveness dissociation happens even in blind human users performing a controlled spatial task with a 2-week delay, the threshold's reliability for LLM screening decisions needs re-examination.
- [[Lin_2022_TeachingModelsExpressUncertainty]] — Lin teaches LLMs to calibrate expressed uncertainty; the Brock finding that confidence tracks short-term scores but not long-term scores is exactly the kind of temporal mis-calibration this line of work tries to fix. Mechanism (Brock) ↔ fix (Lin): different domains, same phenomenon.
- [[Tian_2023_JustAskCalibrationStrategies]] — Tian evaluates "Just ask for calibration" strategies in LLMs; Brock's data show that asking humans for Likert confidence ratings produces a short-term-valid but long-term-invalid signal — evidence that "just ask" calibration is not temporally robust even in humans, which argues for longitudinal validation in any confidence-based screening pipeline.

**Interactive tactile map design lineage:**
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — direct methodological descendant (Brock is co-author); extends from adult usability to pedagogical use with visually impaired children.
- [[Ducasse_2018_AccessibleInteractiveMapsVisually]] — survey/review paper that explicitly positions this work as the core empirical foundation for interactive tactile maps in O&M.
- [[Holloway_2018_AccessibleMapsBlindComparing]] — 3D-printed map comparison — provides the "effectiveness equivalence across map types" finding in a different media (3D print) that mirrors Brock's effectiveness equivalence across audio vs braille legend. Convergent empirical pattern across two different interaction paradigms.
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — alternative audiovisual 3D printed design targeting the same usability goal this paper establishes; Götzelmann is the low-cost answer to Brock's commodity-but-still-expensive 22" multi-touch + PETG overlay stack.
- [[Palivcová_2020_InteractiveTactileMapTool]] — later interactive tactile map tool in the same design tradition.

**Tactile-map design rules and evaluation baseline:**
- [[Perkins_2002_CartographyProgressTactileMapping]] — Perkins 2002 is a progress review of tactile mapping that contextualizes the classical raised-line map baseline this paper compares against. Not cited directly but provides the pre-interactive landscape Brock's paper argues to transcend.
- [[Wabinski_2022_GuidelinesStandardizingTactileMaps]] — Wabiński's tactile map standardization guidelines post-date this paper and operationalize many of the Edman/Picard rules Brock adhered to; conceptual link is design-rule lineage.
- [[Rowell_2003_WorldTouchResultsInternational]] — international survey of tactile map use; provides the population-level usage context against which Brock's N=24 lab study is situated.
- [[Gual_2015_EffectVolumetric3DTactile]] — Gual 2015 studies volumetric 3D tactile map effects, same year as this paper, different interaction paradigm; empirically complements Brock's audio-tactile channel with a purely tactile volumetric channel.
- [[Taylor_2016_Customizable3DPrintedTactile]] — 3D-printed customizable tactile maps in the same evaluation space.

**Spatial cognition and long-term memory:**
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — O&M aids review; Brock's effectiveness findings (landmark > route > survey ordering; survey-type memory robustness) are the kind of empirical data this review aggregates.

**Governing protocol:**
- [[Wabiski_2026_CognitiveReviewProtocol]] — this is the systematic-review protocol governing the project. Brock 2015 is in scope for §3.3 seed selection and provides both (a) a concrete high-quality empirical data point for the review's quality-checklist and (b) a *critique payload*: the confidence-vs-effectiveness dissociation challenges the protocol's >0.90 LLM auto-include confidence threshold.
