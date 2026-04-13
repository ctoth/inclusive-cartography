---
tags: [tactile-maps, 3d-printing, accessibility, capacitive-overlay, openstreetmap]
---
Presents an end-to-end system that turns an OpenStreetMap-specified location into a customizable STL, printed on a consumer FDM machine with a non-conductive PLA base and conductive PLA raised features, and then used as a passive capacitive overlay on an unmodified Android tablet whose companion app speaks an audio label whenever a raised feature is touched.
Contributions: a web authoring interface (simple + advanced), a four-corner rigid registration scheme coupling print to tablet, the conductive-PLA touchscreen overlay mechanism, a feasibility study with 12 visually impaired participants across three cities that surfaces real failure modes (intermittent capacitive touch, small-feature misses, roads printed too thin) and explicit design directions for the next iteration.
Directly relevant to inclusive-cartography's scope because it is a clean reference point for commodity-hardware inclusive map production and a useful counter-example for protocol-level LLM-confidence thresholds: the architecture is confidently described while the physical-layer reliability is entirely uncharacterized.
