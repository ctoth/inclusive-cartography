# Task: Retrieve and process one paper into the inclusive-cartography collection

You are a worker agent in a parallel swarm. Your job: retrieve **one** scientific paper and run it through the full `research-papers:paper-process` pipeline so it becomes an entry in `papers/{Author_Year_ShortTitle}/` with `notes.md`, `metadata.json`, `abstract.md`, `description.md`, `citations.md`, and `pngs/`.

## Context — why you are doing this

Q's project `inclusive-cartography` is executing §3.3 "Seed selection & scoping" of a systematic-review protocol (`papers/Wabiski_2026_CognitiveReviewProtocol/notes.md` if you need to reference it). A second batch of 4 papers is being retrieved to back a critique of the protocol's LLM-confidence thresholds. Q will use the resulting `notes.md` files at a meeting tomorrow morning.

You are running **in parallel** with up to 16 other workers, each handling one paper. Parallel-swarm rules:

- You MUST only touch files inside **your own paper directory** `papers/{Author_Year_ShortTitle}/`.
- You MUST NOT edit `papers/index.md`. A consolidation agent will handle the index after all workers finish.
- You MUST NOT touch any other worker's paper directory, even if the `research-papers:reconcile` skill suggests cross-references.
- You MUST NOT run `git restore`, `git checkout`, `git reset`, `git clean`, or any destructive git operation on files outside your own paper directory.
- If the `research-papers:paper-process` skill's internal `reconcile` step writes files outside your paper directory, let it — but do not initiate cross-paper work yourself.

## Inputs (from the inline prompt that invoked you)

You will receive **one** `PAPER_SPEC` block identifying exactly one paper to retrieve, with fields:
- `label`: short human-readable tag like `Perkins_2002`
- `title`: full title
- `authors`: comma-separated author list
- `year`: publication year
- `venue`: journal / conference / book
- `identifier`: the primary retrieval handle — arxiv URL, DOI, HAL URL, or title string (in that preference order)
- `fallback_identifier`: optional, secondary handle to try if primary fails
- `report_path`: relative path in `reports/` where your final report goes

## Your procedure

### 1. Retrieve the paper
Invoke the `research-papers:paper-retriever` skill with the `identifier`. This will download a PDF into `papers/` root. If the primary identifier fails (network error, 404, retrieval loop), retry once with `fallback_identifier`. If both fail, STOP, write a short report explaining the failure, and do not proceed.

For paywalled papers the retriever uses sci-hub via Chrome — let it run. Do not second-guess the retriever skill.

### 2. Process the paper
Invoke the `research-papers:paper-process` skill with the downloaded PDF path. This runs:
- `paper-reader` (page images + notes.md + metadata.json + abstract.md + description.md + citations.md)
- internal `reconcile` for cross-references (may touch other papers — that is allowed)
- provenance stamping

If `paper-reader` would delegate to chunk workers for a long paper, use the strongest available full-size model for those workers. **Never** use a mini/small/nano tier model for paper extraction. If the strongest model is unavailable, do the reading yourself.

**Do NOT invoke `research-papers:source-bootstrap` or `source-promote` — propstore source-branch work is out of scope for this task.**

### 3. Verify before committing
- Confirm `papers/{Author_Year_ShortTitle}/notes.md` exists and is at least 50 lines (sanity check that extraction produced content).
- Confirm `metadata.json`, `abstract.md`, `description.md`, `citations.md`, and `pngs/page-000.png` are present.
- Confirm the paper's original PDF was moved (not copied) into the paper directory — `papers/` root should not still contain the source PDF after processing.
- Confirm `papers/index.md` was NOT modified by you. If the paper-reader skill tried to append to it, revert only that one file to its prior state using `git checkout -- papers/index.md` (this is the ONLY destructive git operation allowed, and only against `papers/index.md`).

### 4. Commit — atomic, scoped, race-free

**Critical:** do NOT use the `git add <paths>` + `git commit` sequence that previous versions of this prompt specified. That sequence is vulnerable to a git-index race: if another worker in the same swarm stages files between your `add` and your `commit`, the other worker's files get swept into *your* commit. This actually happened during an earlier retrieval run in this project and caused the Gotzelmann / Papadopoulos cross-commit artifact.

**Use `git commit --only` with explicit pathspec.** The `--only` flag stages and commits exactly the named paths regardless of what's in the index, so parallel workers cannot contaminate your commit. Exact command:

```bash
git commit -m "add: {Author_Year_ShortTitle} via paper-process" --only -- papers/{Author_Year_ShortTitle}/
```

Order matters: `-m "message"` comes **before** `--`, and the pathspec comes **after** `--`. If you put `-m` after `--`, git treats it as a pathspec and the commit fails with `error: pathspec '-m' did not match any file(s) known to git`. This is a one-shot command — no separate `git add` step needed; `--only` stages and commits in one atomic operation.

**Do not use `git add .` or `git add -A`** at any point. Specific paths only.

**Do not use plain `git commit` after `git add`.** That is the race-vulnerable pattern this section exists to prevent.

Record the commit hash.

### 5. Write report
Write to `{report_path}` (e.g., `reports/retrieve-Perkins_2002.md`) with:

```markdown
# Report: {label}

## Status
[success | partial | failed]

## Paper directory
papers/{Author_Year_ShortTitle}/

## Commit hash
[git commit hash]

## Retrieval notes
[Which identifier worked, any retries, any access notes — paywall hit, sci-hub used, arxiv direct, etc.]

## Extraction notes
[Page count, chunked? which subagent model used for reading? any ambiguities or unparseable sections]

## Files created
- notes.md: [line count]
- metadata.json: present/missing
- abstract.md: present/missing
- description.md: present/missing
- citations.md: present/missing
- pngs/: [count] images

## Issues / follow-ups
[anything downstream code should know: failed reconcile, unclear DOI, missing references section, etc.]
```

If status is `failed`, explain exactly what failed and at which step. Do not leave partial state behind in the paper directory if retrieval failed cleanly — but if retrieval succeeded and processing partially failed, leave what you produced and flag it in the report.

## Rules — condensed

- **ONE paper, ONE commit, ONE report.**
- Do NOT edit `papers/index.md`.
- Do NOT touch other workers' paper directories.
- Do NOT run `git reset`, `git checkout` (except the specific `papers/index.md` revert), `git restore`, `git clean`.
- Use `mv` not `cp` for the source PDF.
- Report in full even on failure. A failed report is more useful than silence.
