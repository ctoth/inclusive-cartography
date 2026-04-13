# Task: Full-collection reconcile sweep across all 17 papers

## Context

The `inclusive-cartography` project just completed a parallel retrieval swarm that added 16 papers to the collection. Per-worker reconcile runs during the swarm caught most cross-references, but a consolidation-pass reconcile was explicitly scoped (only 3 of 17 papers updated). Q has asked for the full sweep now.

## Target collection
`papers/` directory — should contain 17 paper directories after the recent swarm:

1. Brock_2015_InteractiveMapsUsability
2. Brulé_2016_MapSenseMulti-SensoryInteractiveMaps
3. Ducasse_2018_AccessibleInteractiveMapsVisually
4. Götzelmann_2016_LucentMaps3DPrintedAudiovisual
5. Gual_2015_EffectVolumetric3DTactile
6. Holloway_2018_AccessibleMapsBlindComparing
7. Kadavath_2022_LanguageModelsMostlyKnow
8. Lin_2022_TeachingModelsExpressUncertainty
9. Palivcová_2020_InteractiveTactileMapTool
10. Papadopoulos_2018_OrientationMobilityAidsIndividuals
11. Perkins_2002_CartographyProgressTactileMapping
12. Rowell_2003_WorldTouchResultsInternational
13. Taylor_2016_Customizable3DPrintedTactile
14. Tian_2023_JustAskCalibrationStrategies
15. Wabinski_2022_GuidelinesStandardizingTactileMaps
16. Wabiski_2026_CognitiveReviewProtocol
17. Xiong_2024_LLMUncertaintyConfidenceElicitation

(A possible 18th — `Rowell_Ungar_2003_Part1` — may appear if a parallel retrieval worker lands it. If present, include it in the sweep.)

## Procedure

1. `ls papers/` to confirm the list of paper directories present right now (may include 17 or 18 entries depending on whether the parallel BJVI retrieval landed).
2. Invoke the `research-papers:reconcile` skill on each paper directory. Prefer `--all` if the skill supports a collection-wide mode; otherwise loop. Idempotent runs are expected — the skill should be safe to re-run on papers that already have cross-reference sections.
3. The reconcile skill may update:
   - Each paper's `notes.md` "Collection Cross-References" section
   - Each paper's "Related Work Worth Reading" with `→ NOW IN COLLECTION` annotations
   - Backward "Cited By" sections in other papers
4. After reconcile completes, verify with `git status` — confirm only expected files under `papers/*/notes.md` changed. If the skill touched anything outside a paper directory (e.g., `papers/index.md`), revert just that one file with `git checkout -- papers/index.md`.
5. `git add papers/*/notes.md` — specific glob, NOT `git add .`. Commit with message `consolidate: full reconcile sweep across all papers`.

## What to report

Write `reports/full-reconcile-sweep.md` with:

```markdown
# Full reconcile sweep report

## Status
[success | partial | failed]

## Papers in collection at start of sweep
[list, from ls papers/]

## Reconcile invocations
[per-paper or --all, whichever was used]

## Changes summary
- Papers whose notes.md were updated: [list]
- New cross-references added: [count, representative examples]
- Already-idempotent (no changes): [count]

## Commit hash
[hash]

## Issues
[any papers reconcile skipped or errored on; anything unexpected]
```

Return ≤5 sentences summarising status, commit hash, and change counts.

## Rules

- Do NOT retrieve new papers.
- Do NOT modify `papers/index.md`.
- Do NOT modify paper directory contents except via the reconcile skill itself.
- Do NOT use `git add .` or `git add -A`.
- Do NOT run destructive git operations.
- 15-minute budget. If reconcile is slow, run it sequentially with a time limit — do not block indefinitely on any single paper.
