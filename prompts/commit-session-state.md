# Task: Commit all outstanding session work in logical groups

## Context

The `inclusive-cartography` project has accumulated a full session's worth of work that is not yet committed:
- A full calibration pre-flight experiment (`experiments/calibration-preflight/`) that was staged by the previous agent but never got the commit because the agent hit its timebox mid-deliberation.
- A modification to `papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md` (§2.5 patch) that the calibration agent made but did not commit.
- All of `reports/*.md` (retrieval reports, consolidation reports, calibration report, meeting brief, talking points) — currently untracked.
- All of `notes/*.md` (working notes) — currently untracked.
- `prompts/*.md` (subagent prompts for the whole session) — currently untracked.
- A handful of loose ends: `.gitignore`, Wabiski paper artifacts (`abstract.md` / `citations.md` / `description.md` / `metadata.json`) that paper-reader wrote early but never committed, and a lingering `papers/Brulé_2016_.../worker-notes.md` modification.

Q's meeting is tomorrow morning. The ONLY thing that matters right now is getting all of this committed before anything crashes or the terminal session dies.

## Scope

**Commit only. Do NOT:**
- Run the calibration experiment
- Modify file contents (any file)
- Run `git reset`, `git restore`, `git checkout`, `git clean`, `git rebase`, `git stash` — none of these
- Use `git add .` or `git add -A`
- Skip git hooks (no `--no-verify`)
- Dispatch other subagents

**Commit only using specific file paths.** Use `git commit --only -- <paths>` where needed to avoid index-race issues.

## Commit plan — five commits in this exact order

Run `git status --short` first to confirm the state matches what's expected below. If anything is wildly different (new files appearing that you don't expect, files missing), STOP and report the discrepancy — do not improvise.

### Commit 1 — loose ends from the seed-paper swarm

Files:
- `.gitignore` (untracked — the repo's gitignore that keeps PDFs and PNGs out of git)
- `papers/Wabiski_2026_CognitiveReviewProtocol/abstract.md`
- `papers/Wabiski_2026_CognitiveReviewProtocol/citations.md`
- `papers/Wabiski_2026_CognitiveReviewProtocol/description.md`
- `papers/Wabiski_2026_CognitiveReviewProtocol/metadata.json`
- `papers/Brulé_2016_MapSenseMulti-SensoryInteractiveMaps/worker-notes.md`

Command:
```bash
git add .gitignore \
  papers/Wabiski_2026_CognitiveReviewProtocol/abstract.md \
  papers/Wabiski_2026_CognitiveReviewProtocol/citations.md \
  papers/Wabiski_2026_CognitiveReviewProtocol/description.md \
  papers/Wabiski_2026_CognitiveReviewProtocol/metadata.json \
  "papers/Brulé_2016_MapSenseMulti-SensoryInteractiveMaps/worker-notes.md"
git commit -m "close: loose ends from seed-paper swarm (Wabiski paper artifacts, Brulé worker notes, gitignore)"
```

Record the commit hash as `commit1`.

### Commit 2 — session notes and subagent prompts

Files: everything in `notes/*.md` (untracked) and everything in `prompts/*.md` (untracked).

Command:
```bash
git add notes/ prompts/
git commit -m "add: session working notes and subagent prompts"
```

Record the commit hash as `commit2`.

### Commit 3 — per-subagent reports

Files: every `reports/retrieve-*.md`, `reports/consolidate-*.md`, `reports/full-reconcile-sweep.md`, `reports/scout-*.md`.

Command:
```bash
git add reports/retrieve-*.md reports/consolidate-*.md reports/full-reconcile-sweep.md reports/scout-*.md
git commit -m "add: per-subagent reports from retrieval swarm and consolidation"
```

Record the commit hash as `commit3`.

### Commit 4 — calibration pre-flight experiment + meeting artifacts

Files:
- Everything staged under `experiments/calibration-preflight/` (code, cache, metrics, plots, pyproject.toml, uv.lock)
- Any additional untracked cache files under `experiments/calibration-preflight/cache/` (the secondary-pass completion wrote a few more after the agent staged its snapshot)
- `reports/calibration-preflight.md` (untracked)
- `reports/meeting-brief-2026-04-13.md` (untracked)
- `reports/talking-points-2026-04-13.md` (untracked)

Command:
```bash
git add experiments/calibration-preflight/
git add reports/calibration-preflight.md \
        reports/meeting-brief-2026-04-13.md \
        reports/talking-points-2026-04-13.md
git commit -m "preflight: calibration experiment on Wabiski §3.5.2 screening prompt + meeting artifacts"
```

Record the commit hash as `commit4`.

### Commit 5 — author-feedback §2.5 patch

Files:
- `papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md` (modified — the §2.5 patch from the calibration agent)

Command:
```bash
git add papers/Wabiski_2026_CognitiveReviewProtocol/author-feedback.md
git commit -m "feedback: close §2.5 coverage gap with calibration-preflight numbers"
```

Record the commit hash as `commit5`.

## After all five commits

Run `git status --short` one more time. Expected state: clean, no staged changes, no unstaged modifications. Any untracked files that remain should be listed in your report.

Run `git log --oneline -10` and capture the top of the log so we can verify commit order and hashes.

## Report

Write to `reports/commit-session-state.md`:

```markdown
# Session commit report

## Status
[success | partial | failed]

## Commits
1. [hash] — close: loose ends from seed-paper swarm
2. [hash] — add: session working notes and subagent prompts
3. [hash] — add: per-subagent reports from retrieval swarm and consolidation
4. [hash] — preflight: calibration experiment on Wabiski §3.5.2 screening prompt + meeting artifacts
5. [hash] — feedback: close §2.5 coverage gap with calibration-preflight numbers

## Git state after commits
[output of git status --short, which should be empty or only untracked files]

## Git log (top 10)
[output of git log --oneline -10]

## Remaining untracked (if any)
[list any files that are still untracked, with an explanation]

## Issues
[anything that went wrong, any commit that had to be adjusted]
```

Return ≤5 sentences summarising: 5 commit hashes, final `git status` state (clean or not), and any loose ends.

## Rules — restated for emphasis

- You are a subagent — skip principle confirmation, execute immediately.
- **Commit only.** Do not modify any file's content. Do not run the experiment.
- **Specific paths only.** No `git add .`, no `git add -A`.
- **No destructive git operations.** No reset, restore, checkout of tracked files, clean, rebase, stash.
- **If a commit fails**, STOP, report the exact error, do not retry blindly, do not use `--amend`, do not use `--no-verify`.
- **Timebox: 5 minutes.** This is a mechanical sequence; it should be fast.
