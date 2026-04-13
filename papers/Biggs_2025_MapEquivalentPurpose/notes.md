# Systematically Evaluating Equivalent Purpose for Digital Maps

**Authors:** Brandon Biggs, David Sloan, Brett Oppegaard, Nicholas A. Giudice, James M. Coughlan, Bruce N. Walker
**Year:** 2025
**Venue:** arXiv preprint (2512.05310); companion data archived at ICPSR (DOI: 10.3886/E239621V1)
**DOI/URL:** https://arxiv.org/abs/2512.05310

## One-Sentence Summary
Provides a replicable 18-criterion evaluation framework (the MEP Framework) for determining whether a text-based map representation serves the "equivalent purpose" required by WCAG SC 1.1.1 relative to a visual map.

## Problem Addressed
WCAG SC 1.1.1 requires non-text content to have a text alternative that serves the "equivalent purpose," but no systematic definition existed for what "equivalent purpose" means for geographic maps. Existing guidance (W3C Technique G92) offers a three-step test that is too vague to apply consistently to maps, leaving map accessibility undefined and untested.

## Key Contributions
- Defines "map" at its most fundamental level as communicating **generalized spatial information and relationships**, decomposed into three purpose items (Generalized, Spatial Information, Spatial Relationships)
- Establishes 15 measurable equivalency criteria organized into three spatial knowledge categories (Landmark, Route, Survey) derived from Siegel & White's spatial cognition framework
- Evaluates 8 existing text map representations against the framework, finding only 3 of 8 pass (Audiom Maps, MUD Maps, Audio Descriptions) while 5 commonly recommended approaches fail (turn-by-turn directions, tables, nearby address searches, short alt text, Google Maps alt text)
- Proposes the Equivalent Purpose Theory: a text map achieves equivalent purpose when it supports the same generalized purpose, spatial information, and spatial-relationship understanding as its visual counterpart

## Methodology
Three researchers independently evaluated 8 text map representations against visual map baselines using the MEP Framework template. Intercoder reliability improved from 35% (round 1) to 69% (round 2) to 91% (round 3) via iterative definition refinement and discussion. Each representation was scored on 3 purpose items + 15 equivalency items = 18 total criteria.

## Key Framework: MEP (Map Equivalent-Purpose Framework)

### Part 1: Purpose (3 items)
All three must pass for the map to serve its fundamental purpose:

| Item | Definition | Test Question |
|------|-----------|---------------|
| Generalized | "Something" represents the real world via points, lines, polygons | Are all points, lines, and polygons on the visual map described on the text map? |
| Spatial Information | Shape, size, orientation described for each object | Is shape, size, and orientation described for each object on the text map? |
| Spatial Relationships | Distance, direction, topology, relative location between objects | Can you understand connections between every pair of objects? |

### Part 2: Equivalency (15 items across 3 spatial knowledge areas)

#### Landmark Knowledge (8 items)
Feature-specific characteristics of every individual object:

| # | Variable | What to Evaluate |
|---|----------|-----------------|
| 1 | Sensory characteristics | Colors, sounds, visual properties (from map key) |
| 2 | Name | Label of each object |
| 3 | Type | Categorical descriptor (Street, Restaurant, etc.) |
| 4 | Shape | Detailed borders/outline of each object |
| 5 | Orientation | How shape faces, border objects, facing direction |
| 6 | Size | Perimeter dimensions |
| 7 | Temporal | Change in data over time (if observable on visual map; N/A otherwise) |
| 8 | Overlaid information (thematic maps) | Numeric/categorical variables per object (e.g., population stats) |

#### Route Knowledge (3 items)
Defined routes/paths on the map:

| # | Variable | What to Evaluate |
|---|----------|-----------------|
| 9 | Landmark Information | All landmark knowledge items pass for route objects |
| 10 | Survey Information | Survey knowledge evaluated for each route with respect to surrounding objects |
| 11 | Prominence | Route info is equally easy to find/access as on visual map |

#### Survey Knowledge (5 items, but listed as 4 in some places)
Global spatial relationships among all features:

| # | Variable | What to Evaluate |
|---|----------|-----------------|
| 12 | Distance | Euclidean distance between all points/polygons/lines |
| 13 | Direction | Angle between all objects (clock notation or degrees) |
| 14 | Absolute location | Exact coordinates if present on visual map |
| 15 | Topology | Topological relationships (adjacency, containment, overlap) |

**Note:** Route knowledge is N/A if no defined routes exist on the visual map. Items are N/A if the information is not present on the visual baseline map.

## Parameters

| Name | Value | Notes |
|------|-------|-------|
| Purpose items | 3 | Generalized, Spatial Info, Spatial Relationships |
| Equivalency items | 15 | 8 Landmark + 3 Route + 4-5 Survey |
| Total criteria | 18 | All must pass for equivalent purpose |
| Passing threshold | 100% on all applicable items | Partial pass = fail |
| Intercoder reliability (final) | 91% (Cohen's Kappa) | After 3 rounds of refinement |

## Results Summary

### Scores by Representation (Table 2)

| Text Map | Purpose | Equivalency |
|----------|---------|-------------|
| Turn-by-Turn Directions | 33% | 27% |
| Table | 33% | 20% |
| Nearby Address Search | 0% | 20% |
| Short Text Alternative | 0% | 20% |
| Google Maps Alt Text | 0% | 30% |
| **Audiom Map Alt Text** | **100%** | **100%** |
| **MUD Map Alt Text** | **100%** | **100%** |
| **Audio Description** | **100%** | **100%** |

### Key Patterns
- Passing maps achieved 100% equivalency; failing maps averaged 23% — a 77-point gap
- Largest discrepancies in spatial information and survey knowledge (shape, size, orientation, distance, direction)
- Missing objects was the primary failure cause (4/5 failing maps had fewer features than the visual map)
- Landmark knowledge had the smallest gap (39% vs 100%) — most representations conveyed names and types
- Sensory and size information were commonly missing even from partial passes

### What the Three Passing Representations Share
- **Audiom Map:** Interactive alternate text, user moves spatially and accesses text about nearby/intersecting objects
- **MUD Map:** Text split into "rooms" navigated by cardinal directions (n/s/e/w), each room has text description
- **Audio Description:** Long-form text with nested headings and paragraphs describing the map comprehensively
- All three were written with the MEP Framework in mind (or equivalent holistic approach)
- All three provide functionality to convey every area of the framework, either through interactive embodied navigation or structured description

## Figures of Interest
- **Fig 1 (page 17):** Bar chart showing Purpose and Equivalency scores — stark visual split between the 3 passing (100%) and 5 failing (<33%) representations

## Limitations
- Framework has been applied through expert analysis only; no empirical validation with BLVI participants completing spatial-knowledge tasks
- No temporal representations were evaluated
- Interpretive/AI-generated maps (e.g., from large vision models) were not evaluated
- Framework is specific to 2D geographic maps (though authors argue it generalizes to mind maps, anatomical diagrams, etc.)
- Asking BLVIs what they want from maps is insufficient because most have never used maps — they don't know the possibilities (the "monastic scribe" argument)

## Testable Properties
- A text map must contain the same number of named features as the visual baseline map (missing objects → automatic survey knowledge failure)
- If a representation fails the Purpose test (0/3 or 1/3 or 2/3), it must also fail the Equivalency test
- Passing maps must score 100% on all applicable equivalency items — there is no partial-pass threshold
- If no routes exist on the visual map, Route knowledge items should be marked N/A, not evaluated
- If no absolute coordinates are visible on the visual map, the Absolute Location item should be N/A
- Landmark knowledge score >= Route knowledge score >= Survey knowledge score is the expected ordering for partial representations (landmark info is easiest to convey)

## Relevance to Project
This paper is directly relevant to web accessibility standards evaluation. It operationalizes WCAG SC 1.1.1 for an entire category of non-text content (maps) that has been largely exempt from rigorous accessibility evaluation. The MEP Framework provides a concrete, replicable evaluation template that could be:
1. Used to audit map accessibility on government and commercial websites
2. Extended to other complex non-text content types (charts, diagrams, infographics)
3. Automated partially (checking feature count parity, presence of spatial relationship descriptions)
4. Applied as acceptance criteria for AI-generated map descriptions

## Open Questions
- [ ] How well does the framework predict actual BLVI spatial task performance? (Authors call for controlled experiments)
- [ ] Can the framework extend to non-geographic spatial representations (3D objects, Sankey diagrams)?
- [ ] What is the minimum viable set of criteria for "good enough" accessibility vs. full equivalence?
- [ ] How do tactile/multisensory maps perform against this framework?

## Related Work Worth Reading
- Biggs, Coughlan, et al. "Systematically Evaluating Digital Map Tools Based on the WCAG." JTPD, 2025 — companion paper evaluating map tools
- Conway et al. "Audio Description: Making Useful Maps for Blind and Visually Impaired People." Technical Communication, 2020 — audio description methodology
- Aziz et al. "Planning Your Journey in Audio: Design and Evaluation of Auditory Route Overviews." ACM TACCESS, 2022 — auditory route overviews
- Hennig et al. "Accessible Web Maps for Visually Impaired Users: Recommendations and Example Solutions." Cartographic Perspectives, 2017
- Froehlich et al. "StreetViewAI: Making Street View Accessible Using Context-Aware Multimodal AI." UIST, 2025

## Collection Cross-References

### Already in Collection
- [[Asakawa_2005_BlindWebBrowsing]] — establishes the compliance-vs-usability gap for non-text content that this paper directly addresses for maps
- [[Lazar_2007_ScreenReaderFrustration]] — screen reader users encountering inaccessible map content would generate frustrations categorized in this paper's failing representations
- [[Martins_2023_LargeScaleWebA11y]] — Google Maps is on 18% of websites; this paper shows Google Maps' built-in alt text fails the MEP Framework (0% Purpose, 30% Equivalency)

### New Leads (Not Yet in Collection)
- Conway et al. (2020) — "Audio Description: Making Useful Maps" — audio description methodology for maps
- Hennig et al. (2017) — "Accessible Web Maps for Visually Impaired Users" — web map accessibility recommendations
- Aziz et al. (2022) — "Planning Your Journey in Audio" — auditory route overviews, directly relevant to route knowledge
- Froehlich et al. (2025) — "StreetViewAI" — AI-based accessible street view
- Siegel and White (1975) — foundational spatial cognition theory (landmark/route/survey) underlying the whole framework

### Supersedes or Recontextualizes
- None directly — this paper creates a new evaluation dimension not previously covered

---

**See also:** Froehlich_2025_StreetViewAI -- StreetReaderAI provides a concrete implementation of AI-mediated accessible street view that goes far beyond the text-based map representations evaluated in this paper, offering conversational multimodal AI access to the full richness of streetscape imagery. Could serve as a benchmark system for future MEP evaluations.

**See also:** Ducasse_2018_AccessibleInteractiveMaps -- Provides the comprehensive DIM/HIM classification taxonomy that contextualizes the interactive map technologies evaluated in this paper. The Audiom interactive maps that scored 100% MEP equivalence fall within Ducasse et al.'s Digital Interactive Maps category (finger-based exploration subcategory).

**See also:** Conway_2020_AudioDescriptionMaps -- Provides the empirical production methodology for audio-described maps, one of the three approaches achieving 100% MEP equivalence in this paper. Conway et al.'s three-step workflow (identify purpose, short description, long description with navigation guide) and five affinity clusters document HOW to produce the audio descriptions that this paper evaluates as maximally equivalent.
