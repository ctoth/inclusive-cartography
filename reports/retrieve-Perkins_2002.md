# Report: Perkins_2002

## Status
success

## Paper directory
papers/Perkins_2002_CartographyProgressTactileMapping/

## Commit hash
c05d7c1247ab5477c14330c30626a0d101f43e96

## Retrieval notes

- Primary identifier `10.1191/0309132502ph383pr` went through `fetch_paper.py`. Semantic Scholar resolved metadata correctly (title, author, year, journal 26(4) 521-530) but returned `fallback_needed: true` with no open-access PDF URL. Unpaywall also had nothing.
- Fell back to Chrome + sci-hub. **sci-hub.st** returned a metadata-only page with "..." and no iframe, embed, or PDF link — mirror does not hold this DOI. Same result at **sci-hub.ru** and **sci-hub.se** (the latter had DNS_PROBE_FINISHED_NXDOMAIN).
- **sci-hub.ee worked.** Page rendered an iframe with `src="https://sci.bban.top/pdf/10.1191/0309132502ph383pr.pdf#view=FitH"`. Downloaded via `curl -L` to `papers/Perkins_2002_CartographyProgressTactileMapping/paper.pdf`. Verified with `file`: PDF document v1.4, 10 pages, 131762 bytes.
- Google Scholar: only the SAGE paywalled landing; CORE API returned metadata but `fullText: null`, `sourceFulltextUrls: []`; Manchester Research Explorer had metadata only; SAGE direct PDF URL was behind Cloudflare challenge (not bypassed, per policy).
- One transient false lead: the first sci-hub.st page-scrape captured a stale DOM that showed a `rowell2003.pdf` link — this was from a sibling tab redirect to a *different* paper (Rowell 2003 "World of Touch") opened by a parallel worker. Did NOT download it. Moved on.
- Metadata was then materialized via `fetch_paper.py --metadata-only`, then hand-enriched with abstract text, venue, issue, pages, affiliation, and corrected author name ("Chris Perkins" in place of the S2 "C. Perkins").

## Extraction notes

- 10 pages. Under the 50-page threshold → direct read (Step 2A), no chunk subagents.
- Converted via ImageMagick `-density 150 -resize '1960x1960>'` to `pngs/page-000.png` through `page-009.png`.
- Read all 10 page images directly with Claude Code's Read tool. Cross-checked the extraction against `pdftotext -layout` output to ensure reference-list accuracy (the page images were at the edge of legibility for the dense two-column reference pages). The `paper.txt` intermediate was deleted after use.
- The paper is a non-empirical narrative progress report: no equations, no parameters in the tuneable sense, no statistical models, no figures/tables. Notes.md captures the six-theme framing verbatim, full thematic extraction per section, and the full reference list.
- No ambiguous or unparseable sections. Page citations (p.N) were attached throughout per the skill's extraction guidelines.
- Model used for extraction: Claude Opus 4.6 (1M context), primary agent, no subagent delegation.

## Files created
- notes.md: 235 lines
- metadata.json: present
- abstract.md: present (verbatim abstract + interpretation)
- description.md: present (frontmatter tags + 3-sentence body)
- citations.md: present (full reference list + 5 key follow-ups)
- pngs/: 10 images (page-000.png through page-009.png), gitignored
- paper.pdf: present in paper directory, gitignored

## Issues / follow-ups

- The repo's `.gitignore` excludes `*.pdf` and `*.png`, so `paper.pdf` and all page images are tracked only on disk, not in git. The commit shows 5 files (abstract, citations, description, metadata, notes). Parent prompt's acceptance criterion requires the PDF to have been *moved* (not copied) into the paper directory and `papers/` root to not contain the source — both satisfied on disk.
- A parallel worker (`Rowell_2003_WorldTouchResultsInternational`) appended a "Collection Cross-References" section to my `notes.md` after I wrote it. This is explicitly permitted by the parent prompt's parallel-swarm rules ("if the skill's internal `reconcile` step writes files outside your paper directory, let it"). I did not initiate any cross-paper reconcile myself.
- `papers/index.md` was NOT modified by me. It appears as untracked in `git status` but that is pre-existing state from another worker/flow — not in the diff of my commit.
- The propstore source-branch steps (`source-bootstrap`, `register-concepts`, `extract-claims`, `extract-justifications`, `extract-stances`, `source-promote`) and the `pks build` step were intentionally skipped per the parent prompt's instruction ("Do NOT invoke `research-papers:source-bootstrap` or `source-promote` — propstore source-branch work is out of scope"). Downstream consolidation can run these later against the committed paper directory.
- Provenance stamping (`pks source stamp-provenance`) was also skipped because it is a propstore operation and out of scope for this worker.
- The `Gardiner (2001)` unpublished PhD thesis is cited repeatedly by this paper as the authoritative treatment of tactile-map production technology; it is not currently in the collection and may warrant a follow-up lead.
- No reconcile skill was initiated by me, but the Rowell_2003 worker's reconcile touched my notes.md with cross-references — downstream reconcile consolidation should confirm there are no stale or incorrect backlinks.

## Usefulness assessment

**Rating:** High
**What it provides:** the canonical six-theme framing (cognition, design, standardization, production, technological substitutes, ethics) of post-1990 tactile cartography research, plus the ethics critique that tactile-mapping research is sighted-led, western-urban, academy-based, and built on an inappropriate medical model of disability. Also supplies Gill (1999)'s "25 years of electronic mobility aids, none popular with more than a handful of users" benchmark and Gardiner (2001)'s 4-family production taxonomy.
**Actionable next steps:** use this paper as the ethical-framing anchor for the LLM-confidence-threshold critique (notes/llm-confidence-critique-propstore.md); any protocol in this project that skips the participatory/positionality dimension Perkins identifies is in trouble. Also use its reference list as a citation backbone for the tactile-cartography literature survey.
**Skip if:** looking for empirical results, numerical benchmarks, or implementation-level algorithm detail — this is a narrative review with zero equations and no tables.
