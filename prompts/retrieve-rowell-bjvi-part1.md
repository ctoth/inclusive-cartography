# Task: Retrieve Rowell & Ungar 2003 "Part 1: Production" (BJVI version)

Read `prompts/retrieve-and-process-paper.md` for the full retrieval pipeline. This is a supplemental retrieval — the TCJ "Results" version is already in the collection as `papers/Rowell_2003_WorldTouchResultsInternational/`. Your job is to add the BJVI "Part 1: Production" companion paper as a **distinct** entry.

## PAPER_SPEC
```
label: Rowell_Ungar_2003_Part1
title: The world of touch: an international survey of tactile maps. Part 1: Production
authors: Jonathan Rowell, Simon Ungar
year: 2003
venue: British Journal of Visual Impairment 21(3), 98-104
identifier: 10.1177/026461960302100303
fallback_identifier: Rowell Ungar 2003 world of touch tactile maps Part 1 Production British Journal Visual Impairment
report_path: reports/retrieve-Rowell_Ungar_2003_Part1.md
```

## Critical rules

1. **Do NOT overwrite** the existing `Rowell_2003_WorldTouchResultsInternational/` directory — that's the TCJ "Results" paper, a separate publication by the same authors in the same year. Use a **distinct directory name** for Part 1. Suggested: `Rowell_Ungar_2003_WorldTouchProduction` or similar — just make sure it does not collide with the existing Results dirname.
2. This paper covers **production technology** (microcapsule paper, thermoforming, UV curing, embossed paper) whereas the TCJ Results paper covers survey methodology and findings. Both are seed-relevant.
3. If sci-hub fails on the BJVI DOI, try the SAGE publisher URL directly, then ResearchGate, then Anna's Archive. If all fail, write a failure report — do NOT silently substitute the TCJ version.
4. After successful retrieval and processing, the new paper directory should have a distinct entry ready for the next index.md update. You do NOT need to update `papers/index.md` yourself — that will be handled by a subsequent consolidation.
5. Commit only your own paper directory. Do NOT touch `papers/index.md` or other paper directories. One commit, message `add: {Author_Year_ShortTitle} via paper-process`.

Return ≤5 sentences summarising status and pointing at your report file.
