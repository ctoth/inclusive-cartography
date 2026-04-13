---
title: "Guidelines for Standardizing the Design of Tactile Maps: A Review of Research and Best Practice"
authors: "Jakub Wabinski, Albina Moscicka, Guillaume Touya"
year: 2022
venue: "The Cartographic Journal 59(3), 239-258"
doi_url: "https://doi.org/10.1080/00087041.2022.2097760"
pages: "239-258"
affiliations:
  - "Military University of Technology, Warsaw"
  - "Universite Gustave Eiffel / IGN France"
funding: "Wojskowa Akademia Techniczna, University Research Grant UGB/22-785/2022/WAT"
note: "Open-access preprint via HAL (hal-03763057). Licensed CC BY-NC-ND 4.0."
produced_by:
  agent: "claude-opus-4-6[1m]"
  skill: "paper-reader"
  timestamp: "2026-04-13T05:25:49Z"
---
# Guidelines for Standardizing the Design of Tactile Maps: A Review of Research and Best Practice

## One-Sentence Summary
A narrative review that consolidates empirical research and existing best-practice documents into a set of concrete, measurable design guidelines for tactile maps — covering symbol inventories, minimum dimensions/spacings, generalization rules, and differences between production methods — and makes the case that no global standard yet exists *(p.3, p.16)*.

## Problem Addressed
Tactile maps for people with visual impairment (PVI) are expensive and slow to produce because every map is quasi-bespoke; much of the research-derived guidance on symbol design, minimum sizes, and spacings is scattered across decades of literature and incompatible national best-practice documents (BANA/CBA, NSW Tactual & Bold Print Mapping Committee, Edman, Perkins). There is no globally accepted standard, which blocks acceleration of tactile map production and prevents practitioners from applying the wider research base *(p.3, p.4, p.15)*.

## Key Contributions
- A review-style synthesis of the corpus of research that empirically evaluated tactile symbols (point/line/area) with blind and sighted-blindfolded participants *(p.5, p.6)*.
- A curated set of "highly distinguishable" recommended symbols organized by type (point, line, area, inscriptions, arrows, miscellaneous), with provenance back to the original study or guideline — presented as the Appendix table of recommended symbols *(p.18-20)*.
- Consolidated parameter tables giving measurable minima/defaults for dimensions, distances, and heights of tactile symbols, drawn from multiple sources and reconciled where possible *(p.12, Tables 2-4)*.
- A discussion of generalization constraints specific to tactile cartography, including a square-root map-reduction heuristic and the practical consequences for point/line/area simplification *(p.11, p.13)*.
- A comparative account of how production method (thermoforming, microcapsule/swell-paper, braille embosser/TIGER, 3D printing) constrains symbol design choices and where each method is preferable *(p.13, p.14)*.
- An explicit call for a global tactile-map design standard, motivated by rising interest in multimodal/accessible maps and by the decrease in Braille literacy among PVI *(p.15)*.

## Study Design
- **Type:** Narrative literature review with structured source selection (not a PRISMA-style systematic review, though the authors describe scope and inclusion criteria).
- **Sources:** Scientific articles indexed in Web of Science (SCIE, SSCI, A&HCI), plus established practitioner guideline documents: BANA/CBA (2010), NSW Tactual & Bold Print Mapping Committee (2006), Perkins (2002), Edman (1992), and related ISO / national bodies *(p.5, p.6)*.
- **Inclusion:** Studies had to evaluate symbols empirically with human participants — either PVI or blindfolded sighted participants — on legibility, discriminability, or preference *(p.6)*.
- **Exclusion:** Work focused solely on automated generation pipelines with no symbol-level evaluation, or purely descriptive essays without measured user outcomes.
- **Populations across studies:** N varied widely (typically 6-30 PVI plus sighted-blindfolded control groups). Participants ranged from congenitally blind to late-blind adults, and in some studies included sighted children.
- **Not applicable:** primary endpoint / follow-up (this is a review, not an RCT).

## Methodology
The authors (a) define four requirements a tactile symbol inventory must satisfy; (b) identify categories of information a tactile map must carry (general, point, line, area, inscriptions, arrows, miscellaneous/floor-plan, roads, water/structures); (c) walk the literature per category and extract recommended symbols plus their source and the method used to produce them; (d) compile the recommended symbols into an Appendix table; (e) extract quantitative design parameters (dimensions, distances, heights) into consolidated tables; (f) discuss generalization rules and production-method trade-offs; (g) identify open issues blocking global standardization *(p.4-15)*.

### The four requirements for a tactile symbol design (p.5)
1. The inventory must be built on empirical **recommendations** — symbol shapes must have been tested with blind or blindfolded participants, not merely proposed by sighted designers.
2. Symbols must remain **legible under mass production** — i.e., tolerate the manufacturing method's limitations (thermoforming resolution, braille-embosser dot grid, swell-paper tonal bleed).
3. Inventory must include **variation in colour and dimension** to serve multi-modal users, low-vision readers, and sighted companions, not only fully blind users.
4. Symbols must be **perceptibly separable** under tactile exploration; the authors note a similarity hierarchy where identical symbols are hardest to distinguish, and symbols differing in dimension are easier to separate than symbols differing only in texture *(p.5)*.

### Source selection (p.6)
- Scientific journals: Web of Science indices SCIE, SSCI, A&HCI.
- Practitioner guideline documents treated as first-class sources (BANA/CBA 2010; NSW 2006; Perkins 2002; Edman 1992; Tatham 1991; ISO 2013/2016).
- Figure 1: production methods actually used in the empirical studies reviewed — thermoforming is dominant, then microcapsule/swell-paper, then braille embosser (TIGER), then 3D printing, then a tail of "other" and "2D printing" *(p.7)*.

## Recommended symbols (Appendix A, pp.18-20)

The paper's central operational artifact is an Appendix table that maps symbol categories to specific geometric forms tested in the literature. For each row the authors give: source, details/criteria, and an exemplary rendering. Structure:

- **Point symbols**
  - Nolan & Morris (1971): *highly distinguishable* set — circle, square, triangle, diamond, cross, filled-circle, "T", upward-tick. Criterion for "highly distinguishable" (p.19 footnote 1): average confusion with other distinguishable symbols <=5% AND confusion with itself and other distinguishable symbols <=10%.
  - Nolan & Morris (1971): a second *highly distinguishable* point-symbol set for vacuum-formed plastic maps.
  - Nolan & Morris (1971): a point-symbol set *recommended for general use* along with the respectively dimensioned sister rows of the table that were left blank.
  - Regis & Nogueira (2012): point-symbol set of *standardized point symbols* for global features, to be used on swell-scale maps.
- **Line symbols**
  - Nolan & Morris (1971): highly-distinguishable line set produced using vacuum-formed plastic.
  - Nolan & Morris (1971): highly-distinguishable line set produced using swell-paper.
  - BANA/CBA (2010): "The set of recommended and highly distinctive line textures."
- **Area symbols**
  - Wiedel & Groves (1969): "most discrete tactually" — from a study on vacuum-formed tactile maps.
  - BANA/CBA (2010): set of area textures to use freely on swell-paper maps.
  - BANA/CBA (2010): subset of those textures that may be *reused on the same map* without tactile confusion.
  - Nolan & Morris (1971): "highly distinguishable" area set produced by Thermoform (discontinued) method.
  - Nolan & Morris (1971): "highly distinguishable" area set produced by vacuum-formed plastic.
  - NSW Tactual & Bold Print Mapping Committee (2006): "recommended textures for area symbols" on swell-paper.
- **Inscriptions**
  - ISO (2013): dimensional parameters of Braille writing — the smaller the diameter and technical conditions between the individual parameters, the smaller the tactile output, the lower the production-time cost; all other dimensions shall be proportional.
- **Arrows**
  - NSW Committee (2006): minimum arrow length 90-105 deg cone visible; arrow should be 3-6 mm wide and at least 3 mm long.
  - Wiejkowska et al. (2012): arrowheads should be a form of triangle with a 3-mm distance between tip and end-of-shaft arrow tail. They should not be presented as solid-wedge shapes. Recommended arrow styles.
- **Miscellaneous**
  - James (1975): first-described attempt to create a *standardized* set of tactile symbols using swell-paper (= Minolta microcapsule); like the point set, line set has to be easily discriminable from one another; non-specified symbol meaning may be adapted depending on the map's topic; it has to be explained in the legend.
  - Wiedel & Groves (1969): the set of symbols that were found most discrete tactually in a study on vacuum-formed tactile maps.
- **Floor-plan**
  - NSW Committee (2006): recommended symbols for floor plans — stairs top-to-the-right, escalator, ramp top-to-the-right, travellator. Although commonly used in the country of origin, they must always be identified in the map legend.
- **Roads**
  - NSW Committee (2006): recommended symbols for roads (single/double lines) and related infrastructure: round-about, traffic-light symbols, pedestrian crossing.
- **Water / structures / door types (ISO 2016)**
  - German and Swedish tactile symbols used mainly for orientation and navigation. Selected examples are presented.

Footnote 1 (p.19): **Criteria for a symbol to be considered highly distinguishable: (1) average confusion with other distinguishable symbols <=5%, (2) confusion with itself and other distinguishable symbols <=10%.**

## Parameters — Dimensions (Table 2, p.12)

*All values in mm unless noted.*

| Name | Category | Default / Min | Source | Page |
|------|----------|---------------|--------|------|
| Minimum diameter of a hole (concave element) | General rules | 6 mm | Bris, 2001 | 12 |
| Minimum size difference between symbols | General rules | at least 25-30% between same geometry subtypes | BANA/CBA, 2010 | 12 |
| Optimal point symbol size | Point symbols | 3-5 mm | Wiejkowska et al., 2012 | 12 |
| Optimal point symbol size | Point symbols | 4-6 mm | NSW Tactual & Bold Print Mapping Committee, 2006 | 12 |
| Optimal point symbol size | Point symbols | 6 mm | BANA/CBA, 2010 | 12 |
| Optimal point symbol size | Point symbols | 10 mm | ISO, 2016 | 12 |
| Point symbol size (construction) | Point symbols | 2-13 mm (bigger points can be mistaken with area) | Regis & Nogueira, 2013 | 12 |
| Minimum point symbol width (construction line) | Point symbols | 0.4 mm | Bris, 2001 | 12 |
| Minimum line symbol length | Line symbols | 12.5 mm | BANA/CBA, 2010 | 12 |
| Minimum line symbol length | Line symbols | 13 mm | Edman, 1992 | 12 |
| Minimum line symbol length | Line symbols | 13-25 mm depending on texture used | James & CBA, 1975 | 12 |
| Optimal line symbol width | Line symbols | 0.5-0.8 mm | Wiedel & Groves, 1969 | 12 |
| Optimal line symbol width | Line symbols | 0.5-1.0 | ISO, 2019 | 12 |
| Optimal line symbol width | Line symbols | Maximum 2.2 mm | Jehoel et al., 2009 | 12 |
| Optimal line symbol width | Line symbols | FOR lines thicker than 2 mm, double lines should be used (NSW Tactual & Bold Print Mapping Committee, 2006) | NSW, 2006 | 12 |
| Minimum dimensions of area symbol | Area symbols | 50 x 50 mm | Edman, 1992 | 12 |
| Minimum dimensions of area symbol | Area symbols | 63 x 63 mm | Nolan, 1971 | 12 |
| Minimum dimensions of area symbol in a legend | Area symbols | 13 x 13 mm | Edman, 1992 | 12 |
| Minimum dimensions of area symbol in a legend | Area symbols | 25 x 125 mm | BANA/CBA, 2010 | 12 |
| Inscriptions — minimum size of tactile character | Inscriptions | 15 mm | ISO, 2016 | 12 |

## Parameters — Distances (Table 3, p.12)

| Name | Values | Source | Page |
|------|--------|--------|------|
| Between pairs of the same symbol | 2.3 mm | Wiejkowska et al., 2013 | 12 |
| Between different symbols | 1 mm | Wabinski et al., 2022 | 12 |
| Between different symbols | 2.3 mm | Bris, 2001 | 12 |
| Between different symbols | 3.5 mm | Wiejkowska et al., 2012 | 12 |
| Between different symbols | 5 mm (3 mm for highly contrasting symbols) | Wiejkowska et al., 2012 | 12 |
| Between 2 lines | 2 mm (narrower spacings reduce discrimination) | Stampach & Mulickova, 2016 | 12 |
| Between 2 parallel lines | 6 mm | James & CBA, 1975 | 12 |
| Between lines forming double line | 1.5 mm | Jehoel et al., 2006 | 12 |
| Between dots in a dotted line | Minimum 2.0 mm | Wiejkowska et al., 2012 | 12 |
| Between dots in a dotted line | 0.5-4 mm | Bris, 2001 | 12 |
| Between dots in a dotted line | 20 dots per inch | Wiedel & Groves, 1969 | 12 |
| Between dashes in dashed line | Breaks should be half of the size of dashes | Edman, 1992 | 12 |
| Between tirkutsu and the main line | 3 mm | Wiejkowska et al., 2013 | 12 |
| Between symbol and its annotation | 5-10 mm | Wiejkowska et al., 2012, Cerveira et al., 2013 | 12 |
| Between symbol and its annotation | 3-6 mm | BANA/CBA, 2010 | 12 |
| Between symbol and its annotation | 6 mm | ISO, 2016 | 12 |

## Parameters — Heights (Table 4, p.12)

| Name | Values | Source | Page |
|------|--------|--------|------|
| Minimum height difference between symbols | 0.04-0.08 mm | Jehoel et al., 2009 | 12 |
| Minimum height difference between symbols | 0.5 mm | Bris, 2001 | 12 |
| Maximum number of height levels on a single map | 3 | Bris, 2001 | 12 |
| Recommended heights for symbol type | Braille: 0.5 mm; line and area: 1 mm; point: 1.5 mm | Wiedel & Groves, 1969 | 12 |
| Minimum symbol height | 0.2 mm | Jehoel et al., 2006 | 12 |
| Minimum symbol height | 0.4 mm | Bris, 2001 | 12 |
| Minimum symbol height | 0.5 mm or 0.3 mm for smooth symbols | ISO, 2016 | 12 |
| Minimum symbol height | 0.7 mm | Tatham, 1991 | 12 |
| Optimal symbol height | 0.5-1.5 mm | ISO, 2019 | 12 |

Implicit design rule from Nagel & Coulson (1990): participants preferred the rougher substrates (textures) over the smoother ones, across all symbol types; in a study by Nagel-Coulson, for area symbols, the majority preferred rougher textures *(p.12)*.

## Equations

### Map reduction / generalization ratio (p.11)

$$
n_f = n_o \sqrt{M_o / M_f}
$$

Where:
- $n_f$ = number of objects that could be shown on the target tactile map
- $n_o$ = number of objects shown on the original source map
- $M_o$ = scale denominator of the original source map
- $M_f$ = scale denominator of the target tactile map

Attributed to Topfer & Pillewizer (1966), applied to tactile cartography by Szaflarski (1955). Used as a *numerical generalization parameter* to decide how many features survive a scale reduction into tactile output *(p.11)*.

## Methods & Implementation Details
- Scope of analysis covers: symbols, generalization, design parameters, production methods *(p.6)*.
- Tactile maps are generally hand-designed; automation is identified as a research frontier but not yet productized for general-purpose tactile maps *(p.4, p.15)*.
- The authors recommend that *every* tactile map carry five categories of features: general rules (legend, cardinal arrow, scale), point features, line features, area features, and inscriptions (braille/tactile labels). Each category has its own empirical constraints *(p.5)*.
- For **point symbols**, build the inventory from sets that were empirically verified as "highly distinguishable" — specifically the Nolan & Morris (1971) sets — rather than inventing new shapes *(p.8, Figs. 3-5, p.18)*.
- For **line symbols**, pick from empirically discriminable line-texture sets; line width is a key degree of freedom (0.5-2.2 mm) and lines thicker than 2 mm should be drawn as double lines to remain distinguishable *(p.12)*.
- For **area symbols**, choose patterns with high tactile contrast; dot-density, line-density, and solid-bold are the three primary strategies *(p.11)*.
- For **generalization**, transcription of traditional maps into tactile maps is not finger-resolution-bounded only — "a single finger resolution has to be considered, but in such cases, a simple reduction of the amount of information is not the same as reducing the value of information. Reducing the quantity usually leads to an improvement in the quality of its reception." (quoted p.11). Apply the sqrt(M_o/M_f) rule to decide how many objects to keep.
- For **generalization operators**, Boczar (1977) lays out: all lines must intersect at the same angles on both original and generalized maps; line authors also indicate that when generalizing area symbols closed by boundaries, the area of the generalized region must be equivalent to the original region, whereas the boundary can be simplified *(p.11)*.
- During transcription of traditional maps into tactile maps, eye and finger resolutions have to be considered, but in such cases a simple reduction of the amount of information is not the same as reducing the value of information *(p.11)*.
- In mind, a numerical generalization parameter proposed by Szaflarski (1955) can also be applied to tactile cartography: the map content reduction ratio should come close to the square of the scale reduction value. Another example of a numerical parameter is that proposed by Topfer and Pillewizer (1966) *(p.11)*.

## Differences between production methods (p.13, p.14)

- **Thermoforming** (vacuum-formed plastic over a master): historically the most common method. Produces clean relief and durable multi-use maps but needs a master for each map, which is expensive. Nolan & Morris's classic distinguishability sets were produced by this method. Preferred when high accuracy and durability are needed, especially for published atlases *(p.13)*.
- **Microcapsule / swell-paper (Minolta)**: paper with alcohol-reactive microcapsules; a photocopied image is passed through a heater to selectively raise inked regions. Cheap and fast — best for small editions, one-off personalized maps, and workflows where a practitioner wants tactile output within minutes. Constraint: tonal bleed makes fine detail fragile; symbols must be larger and better separated than on thermoform *(p.13)*.
- **Braille embosser / TIGER**: discrete dot grid. Resolution is limited to the embosser dot grid; point/line/area symbols must be built out of dot patterns. Best for blind readers already comfortable with braille; less suited for low-vision multimodal users because it lacks color *(p.13, p.14)*.
- **3D printing**: enables variable height (multiple relief levels) and arbitrary 3D shapes; excellent for tactile models and floor plans but slow and equipment-dependent. Useful when tactile height channels are part of the design *(p.13, p.14)*.
- **"Other" and 2D printing**: marginal in the reviewed studies; mostly used for low-relief embossed paper or for combined audio-tactile displays.
- The paper emphasizes: *the same symbol may be legible on thermoform and illegible on swell-paper at the same nominal size*, so design rules must be qualified by method *(p.14)*.

## Figures of Interest
- **Fig 1 (p.7):** Bar chart — production methods used in the reviewed empirical studies. Thermoforming dominates; then microcapsule/swell-paper; then braille embosser/TIGER; then 3D printing; tail of "Other" and "2D printing."
- **Fig 2 (p.7):** Examples of point, line, and area symbols from different reviewed studies.
- **Fig 3 (p.9):** Point symbols found to be most discriminable in Nolan & Morris (1971) — top panel.
- **Fig 4 (p.9):** Tactile symbols in vacuum-formed plastic — Nolan & Morris's preliminary set (Wiedel & Groves, 1969).
- **Fig 5 (p.9):** Selected symbols from James (1975) preliminary standardization attempt on swell-paper (Minolta microcapsule).
- **Fig 6 (p.9):** Highly distinguishable line symbols used on swell-paper, based on BANA/CBA (2010).
- **Fig 7 (p.10):** Recommended symbols for cardinal direction arrows and geographic labels (Arctic Ocean, Southern Ocean, Pacific Ocean, Atlantic Ocean, Indian Ocean, Tropic of Cancer, Equator, Tropic of Capricorn, Greenwich Meridian) from Hojbjerre (2013).
- **Appendix A (pp.18-20):** Full table of recommended symbols by category (point, line, area, inscriptions, arrows, miscellaneous, floor plan, roads, water/structures/door-types) with source, criteria, and exemplary symbols.

## Results Summary

- Research consensus exists on several measurable parameters (minimum point-symbol size ~5-6 mm, minimum separation ~2-3 mm, minimum line width ~0.5 mm, minimum symbol height ~0.3-0.5 mm, braille character ~15 mm), though different authorities give slightly different numbers *(Tables 2-4, p.12)*.
- Highly distinguishable symbol sets from Nolan & Morris (1971), Wiedel & Groves (1969), BANA/CBA (2010), and NSW (2006) remain the empirical backbone of the recommended inventory — no superseding set has emerged in the intervening decades *(p.8-10, Appendix A p.18-20)*.
- Guideline documents themselves are mutually inconsistent (BANA/CBA vs NSW vs ISO vs Edman), which prevents a single global standard from crystallizing *(p.15)*.
- Point symbols, line symbols, and area symbols all have workable inventories in the literature, but very few studies evaluate multi-modal (tactile + print + color) symbols, and the inventories are split along production-method lines *(p.13, p.14)*.
- Arrows and floor-plan symbols have the weakest empirical base; the review relies almost entirely on practitioner guidelines (NSW 2006) for those categories *(Appendix A, p.19-20)*.
- Most research uses only a single production method per study, making cross-method comparison difficult. The authors call for a study that holds symbol design constant while varying production method *(p.14, p.15)*.

## Limitations (Discussion & Conclusions, pp.14-15)

- Review is narrative, not systematic (PRISMA). Selection is based on the authors' field knowledge and Web of Science searches; no inter-rater reliability or documented query strings.
- The parameter values collected are not independent — many trace back to the same few empirical studies (Nolan & Morris 1971; Wiedel & Groves 1969; Edman 1992).
- Most of the source studies test legibility with small Ns (order of 10-30 participants) and often use sighted-blindfolded participants as a proxy for PVI, which may overstate or understate certain effects.
- **Local standardization** — even within a country, institutions use different conventions. E.g., water is blue on topographic maps, but tactile maps have no analogous universally-accepted area convention for water *(p.15)*.
- **Braille literacy decline** — Danish Association of the Blind (2018) reports declining braille literacy among PVI, which weakens the assumption that labels can be braille-only and argues for linguistically independent, standardized inscriptions *(p.15)*.
- Official guidelines for tactile maps seldom form translated publications, which reduces their accessibility and means the next generation of cartographers risks reinventing the wheel *(p.15)*.
- The review focuses primarily on haptic content — but due to the rising popularity of multimodal maps involving multiple senses (Brule et al. 2016, Giudice et al. 2020, Matsuo et al. 2020, Barvir et al. 2021) and universal-design concepts in general, future research should address the challenge of formally describing design principles to consider senses other than touch *(p.15)*.
- Standardization at the global level is the ultimate goal, but different countries currently follow different design principles for the *same* features — e.g., area-symbol conventions for water bodies differ between Polish, German, and Swedish tactile cartography traditions *(p.15)*.

## Arguments Against Prior Work
- Prior guideline documents (BANA/CBA, NSW, Edman, ISO) are mutually inconsistent on measurable parameters — e.g., minimum dot size varies 3-10 mm across sources for the *same* category *(Table 2, p.12; p.15)*.
- Many practitioners still design tactile maps intuitively without consulting the empirical literature, producing maps that are legible only to the specific users they were tested on *(p.3, p.4)*.
- Symbols considered "standard" in one country's practitioner community are often unknown or unused in another's; the review argues this is a failure of translation, publication, and dissemination, not a scientific disagreement *(p.15)*.
- Prior work treats production method as a detail; the authors argue method is first-order — a valid symbol inventory is method-specific and cannot be transplanted naively between thermoform, swell-paper, and embossed dot grids *(p.14)*.
- Existing research is dominated by a small number of seminal studies (Nolan & Morris 1971, Wiedel & Groves 1969); the authors note this concentration as a structural weakness of the evidence base *(p.8, p.9)*.

## Design Rationale
- **Why split requirements into four explicit criteria (p.5)?** Because earlier guideline documents conflate empirical legibility ("has it been tested?") with manufacturability ("can it be reproduced cheaply?") and with inclusivity ("does it serve multi-modal users?"). The authors separate these axes so a practitioner can audit a symbol inventory against each axis independently.
- **Why organize the appendix by symbol type rather than by source document?** Because a practitioner building a tactile map starts from "I need a point symbol for X" rather than "what does BANA say?" — the axis of lookup is category, not provenance.
- **Why include the sqrt(M_o/M_f) Topfer-Pillewizer rule even though it predates empirical tactile studies?** Because it provides a *numerical* generalization target that can be applied mechanically during map production, while most tactile-map generalization guidance is qualitative *(p.11)*.
- **Why keep production-method differences as a dedicated section rather than folding them into each symbol category?** Because the method determines which symbol sizes are achievable, which forces practitioners to think about method *before* choosing symbols *(p.13, p.14)*.

## Testable Properties
- A "highly distinguishable" symbol has average confusion <=5% with other distinguishable symbols AND <=10% confusion with itself/others *(p.19 footnote 1)*.
- Minimum point-symbol diameter for tactile legibility: ~3-10 mm depending on source; the most-cited value is 5-6 mm *(Table 2, p.12)*.
- Minimum separation between different symbols: ~1-5 mm; 3 mm for highly contrasting symbols *(Table 3, p.12)*.
- Minimum line-symbol width: 0.5 mm; practical maximum before double-lining: ~2.0-2.2 mm *(Table 2, p.12)*.
- Minimum tactile relief height: 0.04-0.08 mm detectable difference; 0.3-0.5 mm recommended minimum feature height *(Table 4, p.12)*.
- Number of distinct relief-height levels usable on a single map: **at most 3** (Bris, 2001) *(Table 4, p.12)*.
- Braille character minimum size: 15 mm (ISO 2016) *(Table 2, p.12)*.
- Minimum legend area-symbol dimensions: 13x13 mm (Edman) to 25x125 mm (BANA/CBA) *(Table 2, p.12)*.
- Point-symbol size must differ by at least 25-30% between same-geometry subtypes to be reliably discriminated *(Table 2, p.12)*.
- Rougher area-substrate textures are preferred by users over smoother ones, across symbol categories *(Nagel & Coulson 1990, p.12)*.
- Generalization rule: the number of features retained on the tactile map scales as the square root of the ratio of source-to-target scale denominators *(p.11)*.
- A symbol inventory valid on thermoform will not necessarily remain legible on swell-paper or braille-embossed output *(p.14)*.

## Relevance to Project

This paper is the **current best single reference** for measurable tactile-map design parameters within the inclusive-cartography project. Specifically:

- **Parameter tables** (dimensions / distances / heights on p.12) give concrete lower bounds we can encode as invariants in any automated tactile-map generator: minimum symbol size, minimum spacing, minimum line width, minimum relief height, maximum relief levels.
- **Appendix A** (pp.18-20) is the closest thing in the literature to a ready-to-use symbol inventory; any automated generator should use it as a starting catalogue rather than inventing symbols.
- The **production-method-specific differences** section directly constrains the design of any automation pipeline — the pipeline must know which method the output will be produced by, because legal symbol sets differ.
- The **sqrt map-reduction rule** (p.11) is a concrete formula we can use when deciding how aggressively to generalize a source OSM/topo map into a tactile map at a given reduction ratio.
- The paper's own identification of open problems — production-method sensitivity, multimodal symbology, local vs global standardization — is a ready list of testable claims for the systematic-review protocol that the 2026 Wabinski paper defines.
- The **"highly distinguishable" criterion** (<=5% / <=10% confusion) gives us a concrete, quantitative acceptance threshold for any new symbol-evaluation study run inside the project.

## Open Questions
- [ ] No single quantitative value for "minimum point symbol size" — is the 5-6 mm modal value the right default for a generator, or does it depend on user (age, onset of blindness)?
- [ ] The review does not quantify how much legibility degrades when a thermoform-designed symbol is reprinted on swell-paper — how much larger must it be?
- [ ] How are multimodal (color + tactile) symbols best encoded? The review flags this as open.
- [ ] What is the empirical basis for the "at most 3 relief levels" rule? Does it hold on 3D-printed output where precise height control is possible?
- [ ] Arrows and floor-plan symbols rely almost entirely on NSW (2006) practitioner guidelines — what is the missing empirical validation?
- [ ] The Topfer-Pillewizer generalization rule is borrowed from visual cartography; does it empirically hold for tactile reading?

## Collection Cross-References

### Already in Collection
- [[Rowell_2003_WorldTouchResultsInternational]] — Cited in the reference list. Wabinski et al. use Rowell & Ungar's international survey of 94 producers in 43 countries as evidence of the no-shared-standard status quo that motivates the consolidated guidelines offered here.
- [[Rowell_Ungar_2003_WorldTouchProduction]] — The BJVI "Part 1: Production" companion paper from the same Rowell & Ungar 2003 survey project. Same 146-questionnaire / 87-response dataset reported on the production-technology / organisational-category side (microcapsule-paper dominance, thermoform retention, country breakdown). Wabinski's consolidated guidelines target exactly the standardisation deficit both Rowell & Ungar 2003 papers document.
- [[Perkins_2002_CartographyProgressTactileMapping]] — Cited as the immediate prior-art review for tactile mapping. Wabinski's paper is in effect the 20-years-later successor that can now present measurable parameters Perkins could only call for.
- [[Gual_2015_EffectVolumetric3DTactile]] — Cited in the production-methods discussion; Gual et al.'s volumetric-vs-flat experiment provides one of the few clean empirical comparisons of symbol height as an independent variable and grounds Wabinski's production-method-sensitivity argument.
- [[Holloway_2018_AccessibleMapsBlindComparing]] — Cited (alongside Holloway et al. 2019) as direct empirical support for the claim that 3D-printed maps often outperform swell-paper tactile graphics — one of Wabinski's exemplars for production-method differences.
- [[Taylor_2016_Customizable3DPrintedTactile]] — Cited as a reference example of capacitive-overlay + OpenStreetMap-driven tactile map production — an automation pipeline of the kind Wabinski's parameter tables are meant to constrain.

### Now in Collection (previously listed as leads)
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — Brulé, Bailly, Brock, Valentin, Denis & Jouffrais (CHI 2016). Wabiński et al. cite "Brule et al. 2016" (lines 218, 277) as an exemplar of multimodal/audio-tactile maps when arguing that tactile-map standardization should extend beyond haptics to multi-sensory design. MapSense combines a capacitive tablet, raised-paper figurative overlay, conductive-ink touch points, and 3D-printed tangible landmarks in a participatory-design study with 15 caretakers and ~19 VI children.

### New Leads (Not Yet in Collection)
- **Nolan & Morris (1971)** — *Improvement of Tactual Symbols for Blind Children: Final Report*. Canonical empirical distinguishability study; source of the "highly distinguishable" criterion used throughout Appendix A.
- **Wiedel & Groves (1969)** — Early vacuum-formed distinguishability study; co-source of the appendix symbol inventory.
- **BANA/CBA (2010)** — *Guidelines and Standards for Tactile Graphics*. Practitioner standard competing with NSW 2006 and ISO 19028.
- **NSW Tactual & Bold Print Mapping Committee (2006)** — Primary source for floor-plan, road, and arrow recommendations in the Appendix.
- **Edman (1992)** — *Tactile Graphics*. Practitioner handbook and primary BANA source.
- **ISO 19028 (2016)** and **ISO 17049 (2013)** — International tactile-map and braille standards; candidate anchors for any global standard.
- **Jehoel, Ungar, McCallum & Rowell (2005, 2006, 2009)** — Tactile elevation / substrate / cognitive-tactualization studies; source for the 0.04-0.08 mm minimum relief-height difference claim.
- **Töpfer & Pillewizer (1966)** — The sqrt(M_o/M_f) map-reduction rule Wabinski imports from visual cartography.
- **Højbjerre (2013)** — Cardinal-direction and geographic-label symbol recommendations used in Figure 7.
- **Mukhiddinov & Kim (2021)** — Systematic literature review on automatic tactile-graphics creation; closest prior art for automation pipelines.
- **Giudice, Guenther, Jensen & Haase (2020)** — Multimodal touchscreen-vs-embossed wayfinding study; flagged by Wabinski as evidence for the multimodal gap in current guidelines.
- **Matsuo et al. (2020)** — TMT-Map customizable audio-tactile map tool.
- **Barvir, Vondraková & Brus (2021)** — TouchIt3D + OSM semi-automated workflow.
- **Danish Association of the Blind (2018)** — *Braille Teaching and Literacy: A Report for the European Blind Union*. Used to argue for linguistically-independent standardized inscriptions in the face of declining braille literacy.

### Supersedes or Recontextualizes
- **Relative to [[Perkins_2002_CartographyProgressTactileMapping]]**: Wabinski et al. (2022) is effectively the 20-years-later progress report on the same subject. Perkins documented that no international tactile-symbol standard had emerged and that the field was sighted-led; Wabinski et al. confirm the standardization gap and now offer a consolidated set of measurable parameters. They corroborate and extend Perkins' critique rather than supersede it.
- **Relative to [[Rowell_2003_WorldTouchResultsInternational]]**: Rowell & Ungar documented producer practice in 2001-2002 and argued for a shared design language rather than a rigid standard; Wabinski et al. answer that call with a concrete, empirically-grounded guideline. The two papers are problem-statement and proposed-response across a 20-year gap.

### Cited By (in Collection)
- [[Wabiski_2026_CognitiveReviewProtocol]] — The 2026 systematic-review protocol by the same first author. The 2026 protocol explicitly builds on the 2022 narrative review and uses its identified gaps (no global standard, production-method sensitivity, multimodal encoding) as scoping questions.

### Conceptual Links (not citation-based)
- [[Rowell_2003_WorldTouchResultsInternational]] — Strong conceptual link. Rowell & Ungar (2003) is the empirical motivation for exactly the kind of consolidated design guidelines this paper provides. Their 94-respondent / 43-country survey documents that tactile map producers work largely independently with no shared international standard and explicitly argues for a shared tactile design language; Wabinski et al. (2022) is the delayed response to that gap — a systematic set of symbol-size, production-method, and legibility recommendations. Rowell & Ungar establishes the standardisation deficit; Wabinski 2022 offers a concrete attempt to close it. The two papers are bookends twenty years apart on the same problem.
- [[Perkins_2002_CartographyProgressTactileMapping]] — Moderate link. Perkins 2002 is cited here as a progress review for the field.
- [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] — Substantive tension. Brulé et al. 2016 explicitly argue against one-size-fits-all accessibility solutions and advocate per-classroom customization with teacher-level authoring; Wabinski et al. 2022's entire project is international standardization of tactile-map symbols. Reading them together frames a real methodological debate about whether inclusive cartography should converge on shared standards or support heterogeneity-aware local design. Both are relevant for any systematic review of inclusive cartography.
- [[Brock_2015_InteractiveMapsUsability]] — Strong. Brock et al.'s audio-tactile interactive map experiment with 24 blind adults provides the *effectiveness* counterpart to Wabinski's *design-parameter* guidelines: Brock shows interactive audio-tactile maps improve learning time and satisfaction, but does not prescribe the symbol-level invariants Wabinski compiles. Together they answer "which symbols?" (Wabinski) and "which interaction modality?" (Brock).
- [[Ducasse_2018_AccessibleInteractiveMapsVisually]] — Strong. Ducasse's DIM/HIM taxonomy situates Wabinski's symbol-level guidelines within the tactile layer of hybrid interactive maps; Wabinski's parameters are directly consumable as the tactile-layer design invariants in Ducasse's HIM family. The two papers compose: Ducasse says *which* device class to build, Wabinski says *how big* its symbols must be.
- [[Götzelmann_2016_LucentMaps3DPrintedAudiovisual]] — Moderate. LucentMaps is a concrete production-method case study (~$0.40 3D-print overlay with capacitive markers) of exactly the method-sensitivity issue Wabinski flags — it is the sort of pipeline that needs Wabinski's parameter tables as a legibility floor.
- [[Palivcová_2020_InteractiveTactileMapTool]] — Moderate. Palivcová et al. report concrete numeric guidance (~1 cm/1 m scale, distinct tactile symbols, audio rate adjustability) for older-adult VI users in an indoor setting. Their parameter set partially overlaps Wabinski's tables and extends them into the age/cognition axis that Wabinski does not cover.
- [[Papadopoulos_2018_OrientationMobilityAidsIndividuals]] — Moderate. Papadopoulos provides the *cognitive-map-formation* benchmark (audio-tactile maps beat verbal descriptions) that justifies the tactile channel Wabinski's parameters apply to.
- [[Wabiski_2026_CognitiveReviewProtocol]] — Strong (same lead author). The 2026 protocol operationalizes exactly the open problems Wabinski 2022 flags as systematic-review research questions. The 2022 paper is the motivation document for the 2026 protocol.

### Tensions Found
- **Regional vs global standardization** — Wabinski et al. push for a global tactile-map design standard; [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]] explicitly argues for heterogeneity-aware design that rejects one-size-fits-all accessibility. The positions are not fatally incompatible, but any future global standard must accommodate the Brulé critique.
- **Symbol-level vs artifact-level design** — Wabinski's guidelines are symbol-level (geometric minima); [[Brock_2015_InteractiveMapsUsability]] and [[Ducasse_2018_AccessibleInteractiveMapsVisually]] demonstrate that interaction modality often dominates symbol design for end-task performance. A tactile map that is pixel-perfect by Wabinski standards can still underperform a less-careful interactive audio-tactile map.

## Related Work Worth Reading
- **Nolan & Morris (1971)** — the canonical "highly distinguishable" point/line/area symbol sets; most of the recommended inventory traces here.
- **Wiedel & Groves (1969)** — early empirical distinguishability study on vacuum-formed tactile maps.
- **Edman (1992)** — "Tactile Graphics" practitioner handbook; a primary source for BANA.
- **BANA/CBA (2010)** — "Guidelines and Standards for Tactile Graphics".
- **NSW Tactual & Bold Print Mapping Committee (2006)** — best-practice document for floor plans, roads, and arrows.
- **Perkins (2002)** — "Cartography: progress in tactile mapping".
- **Jehoel, Sharpe, Ungar, Strijbos (2006, 2009)** — experimental work on minimum tactile height differences.
- **Topfer & Pillewizer (1966)** — the sqrt map-reduction rule.
- **Hojbjerre (2013)** — cardinal direction and geographic label symbols.
- **Brule et al. (2016)** → NOW IN COLLECTION: [[Brulé_2016_MapSenseMulti-SensoryInteractiveMaps]]. **Giudice et al. (2020), Matsuo et al. (2020), Barvir et al. (2021)** — multimodal/audio-tactile maps.
- **ISO 17049 / ISO 19028** — international standards for braille and tactile public signage.
- **Danish Association of the Blind (2018)** — declining braille literacy report.
