# Meeting brief — 2026-04-13 morning
## Wabiski protocol review + seed-paper retrieval status

## What got done
- **16 of 17 target papers retrieved and processed into `papers/{Author_Year_ShortTitle}/`** with per-paper notes.md, description.md, and claims/stances artifacts.
- **13 seed papers for §3.3 inclusive-cartography retrieved** (1 failed: Lobben_2015 — strict paywall, Anna's Archive DNS-blocked, ILL-only).
- **4 LLM-verbalised-confidence papers retrieved** for the §2.2 critique in `author-feedback.md` — Tian 2023, Lin 2022, Kadavath 2022, Xiong 2024.
- **`papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md` updated** to splice in direct citations from all four LLM-confidence papers at §2.2(e)-(h) and close the §2.5 coverage gap (commit `ad6a8b2`).
- **`papers/index.md` rebuilt** with all 17 paper entries (commit `be52bf3`).

## Papers ready for discussion

| label | rq_tags | notes_lines | commit | key_finding_for_meeting |
|---|---|---|---|---|
| Perkins_2002 | rq1 framing, ethics | 235 | c05d7c1 | Canonical framing of inclusive cartography; critical-ethics lens on sighted-led, western, urban research bias |
| Rowell_2003 | rq1 survey, rq2 tech | 273 | 957c869 | 94-producer / 43-country survey; microcapsule + thermoform dominate; **IDENTITY MISMATCH** with BJVI "Part 1" (see caveats) |
| Brock_2015 | rq1, rq2 usability | 332 | 8f4f314 | Audio-tactile interactive map vs raised-line: **landmark recall decays 45% in 2 wks while self-reported confidence does not** — human-side analogue to LLM calibration problem |
| Gual_2015 | rq2 3D tactile | 246 | 8839cd1 | N=16 within-subjects; 3D-printed ABS point symbols beat flat swell-paper on all profiles, largest gains for blind users |
| Taylor_2016 | rq2 3D, rq3 transferability | 252 | 30ee464 | OSM → STL → conductive-PLA capacitive overlay on Android; end-to-end pipeline; explicit physical-layer failure modes documented |
| Götzelmann_2016 | rq2 3D, rq3 transferability | 245 | 5ae0296+5de8142 | Translucent PLA overlays + CapCode capacitive ID; ~$0.40/print, ~1 hr, consumer printer; n=5 VIP feasibility study |
| Brulé_2016 | rq1, rq2 participatory | 293 | 3d29854 | MapSense/Mappie for VI children; 4 design guidelines; counter-evidence to "screen-reader-over-Leaflet" framing |
| Holloway_2018 | rq2 3D, rq3 | 232 | 7cd31f1 | Desktop-3D-printed relief maps beat swell-paper on identification accuracy with N=16 BLV; 9 design guidelines |
| Papadopoulos_2018 | rq1, rq2 audio-tactile | 217 | 5ae0296 | N=20 blind adults; audio-tactile map > verbal-only description for routes (M=5.75 vs 4.85 correct answers) |
| Ducasse_2018 | rq3 taxonomy, rq2 | ~232 | 422fa78 | Canonical DIM/HIM taxonomy; HIMs beat pure DIMs on shape recognition; refreshable pin displays not yet field-ready |
| Palivcová_2020 | rq1, rq2 older adults | 255 | d93fe95 | N=10 VI older adults (mean 81.4); intersection of aging + visual impairment; indoor tactile-map guidelines |
| Wabinski_2022 | rq1, rq3 guidelines | 332 | 9736d5d | Review consolidating measurable tactile-map guidelines (Tables 2-4, Appendix A); same lead author as the 2026 protocol |
| Lobben_2015 | rq1, rq3 | — | — | **FAILED — paywall** (see open decisions) |
| Tian_2023 | LLM-confidence | 238 | 1686704 | ECE ≈ 0.03-0.04 for GPT-4/Claude-2 but ONLY in-distribution factoid QA; two-step + top-k elicitation are cheap Wabiski-protocol upgrades |
| Lin_2022 | LLM-confidence | 288 | cdb509c | Finetuned GPT-3 best-case MSE 15-22% on OOD; verbalized signal only weakly correlated with answer-token logits (Fig 12 p.19); few-shot does not reach finetune |
| Kadavath_2022 | LLM-confidence | 240 | 301bf53 | 52B LMs calibrated on MC/TF in favorable formats (RMS ECE ≈ 0.04); "None of the Above" collapses calibration; RLHF miscalibrated; P(IK) flips sign OOD |
| Xiong_2024 | LLM-confidence | 293 | ccb6dc1 | **Strongest refutation of Wabiski's threshold rule.** Verbalized confidence clusters 80-100% in multiples of 5 across all 5 tested models; GPT-4 CoT GSM8K achieves ECE 0.064 by assigning 100% to everything while AUROC ≈ random |

## What Q should raise first

1. **Seed coverage is complete enough to proceed with §3.3 claim extraction.** 13 of 14 seed papers retrieved; the one gap (Lobben_2015) is paywall-bound and does not block execution. RQ1 coverage is strongest (Perkins, Brock, Gual, Palivcová, Rowell, Brulé, Papadopoulos). RQ2 (Holloway, Taylor, Götzelmann, Ducasse, Gual, Brock, Papadopoulos) is well-covered on technology/tools/media. RQ3 (Wabinski_2022, Ducasse, Perkins) has solid literature-review anchors but empirical transferability studies are thinner — worth flagging for the protocol author.

2. **The `author-feedback.md` critique now rests on direct empirical evidence, not analogues.** Xiong 2024's finding that verbalized confidence clusters 80-100% in multiples of 5 *regardless of ground truth* is the single most important talking point for the meeting. It means Wabiski's 0.70/0.85/0.90 thresholds are inside the model's noise envelope by construction — the thresholds are not discriminating on the signal they claim to. Kadavath 2022's format-sensitivity result (`"None of the Above"` collapses calibration) and RLHF-miscalibration result (T > 1 rescaling required) are the second-strongest supports. Lin 2022 gives the OOD ceiling; Tian 2023 gives the positive result in its narrowest form. All four papers agree on the direction of the conclusion.

3. **Lobben_2015 paywall — decide ILL vs author email vs drop.** Canonical DOI is 10.1007/978-3-319-17738-0_7 (Springer Modern Accessible Cartography chapter). Sci-hub failed; Anna's Archive DNS-blocked; UNAM copy is a 4-page note not the full chapter. Options for Q:
   - **(A) Institutional ILL request** — Springer chapter is held by most R1 libraries; 2-10 day turnaround.
   - **(B) Author email** — Amy Lobben (Oregon) is still active; direct request has high success rate.
   - **(C) Drop from seed list** — Lobben's contribution is cognitive-cartography framing; Perkins 2002 + Brock 2015 + Ducasse 2018 already cover the same conceptual space for RQ1/RQ3.
   - **Recommendation:** (B) + (C) in parallel — email the author as a courtesy, proceed with seed extraction without waiting.

## Known issues / caveats

- **Rowell_2003 identity mismatch.** Worker's DOI (10.1179/000870403225012961) resolved to the TCJ "Results of an International Survey" paper, not the BJVI "Part 1: Production" paper Q originally specified (DOI 10.1177/026461960302100303). Both are by Rowell & Ungar; both are from 2003. The TCJ version is canonically cited and covers the survey methodology; the BJVI version focuses on production technology. Decision point for Q — do we retrieve BJVI Part 1 as a separate paper or accept TCJ as the seed?
- **Papadopoulos dirname says `_2018` but the protocol spec said 2017.** Online publication year is 2018; print-year is 2017. The dirname matches the record-of-record. Leaving as-is.
- **Götzelmann_2016 dirname contains a Unicode umlaut (ö).** Windows-path handling is OK in the current toolchain but worth watching if we migrate build steps to POSIX-only tooling.
- **Gotzelmann / Papadopoulos cross-commit artifact.** Due to a git-index race during the parallel retrieval swarm, one worker's staged files were swept into the other's commit. Files are on disk and tracked correctly — a follow-up commit (`5de8142`) deduped conceptual links. Not destructive, but the commit graph is slightly messy.
- **Reconcile ran per-worker during the swarm** despite the foreman rule; some cross-reference annotations were added incrementally. Consolidation-pass reconcile has not been run yet (see open decisions below).
- **PDFs + PNGs gitignored** by repo `.gitignore`. Only markdown/JSON artifacts are tracked. Anyone checking out the repo will need to re-retrieve the PDFs from the per-paper doi_url.

## Open decisions

- **Rowell_Ungar Part 1 (BJVI).** Retrieve as a separate seed paper? It covers production technology rather than survey methodology and would non-trivially strengthen RQ3 coverage. Low cost to retrieve via sci-hub; moderate effort to add to the collection.
- **Lobben_2015.** ILL, author email, or drop? (See recommendation above.)
- **When to send `author-feedback.md` to Wabiski?** The draft is now citation-complete. Options: (a) send as-is for immediate response before the protocol is registered; (b) hold until after the meeting to incorporate discussion outcomes; (c) convert to a pull-request-style annotated diff against v.2.0 of the protocol and share as a reviewable document rather than a memo.
- **Calibration pre-flight step (§3.5.3 recommendation in the feedback).** Should we prototype it before sending the feedback, or leave implementation to the protocol author? Doing it ourselves would give us the empirical ECE/AUROC numbers on inclusive-cartography screening as a by-product, closing the one remaining gap flagged in §2.5.
- **Full cross-collection reconcile.** Not yet run as a consolidation pass (ran per-worker during the swarm only). Low risk to run before the meeting; moderate value since per-worker runs already caught most cross-references. Flag for decision — skip, run now, or run after the meeting.

## Commit hashes (consolidation)
- `be52bf3` — `consolidate: papers/index.md update`
- `ad6a8b2` — `feedback: augment author-feedback with Tian/Lin/Kadavath/Xiong citations`
- (reconcile pass — not yet run; see open decisions)
