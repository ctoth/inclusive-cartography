# Scout: research-papers plugin commit race

## Headline finding

**The research-papers plugin, as installed at `~/code/research-papers-plugin`, contains ZERO per-paper `git add` or `git commit` instructions.** The only `git add` / `git commit` strings in the entire plugin repository are in the plugin's release-process section of `CLAUDE.md` (`~/code/research-papers-plugin/CLAUDE.md:24-25`), which describe how to ship a new plugin version — not how to commit an ingested paper. No skill SKILL.md, no helper script under any `skills/*/scripts/` directory, and no script under `plugins/research-papers/scripts/` issues `git add` or `git commit` against a paper directory.

That means the commit step described in the bug report — "workers each run `git add <their-paper-dir>/` and then `git commit`" — is not coming from the plugin's code as currently checked out. It must be coming from somewhere outside the plugin: the calling project's `CLAUDE.md`, the user's global instructions, a separate protocol/skill layered on top, or a hand-rolled wrapper the user is running around the plugin. Whatever is issuing those commits is not in this repo.

The rest of this report documents what I verified, where commit logic *could* live if the plugin were to take responsibility for it, and what the candidate fix space looks like.

## Plugin layout (relevant paths)

```
~/code/research-papers-plugin/
  CLAUDE.md                                    # only git add/commit strings live here (release process)
  plugins/research-papers/
    .claude-plugin/plugin.json                 # no hooks, no settings injection
    scripts/
      sync_propstore_source.py                 # wraps `pks source add-*` only; no git
      (20 other scripts — none call git)
    skills/
      paper-process/SKILL.md                   # orchestrator; calls nested skills via /research-papers:*
      paper-process/scripts/emit_nested_process_fallback.py   # no git
      paper-reader/SKILL.md                    # reads PDF, writes notes.md etc.; no git
      paper-reader/scripts/{paper_hash.py,_paper_id.py,emit_nested_reader_fallback.py}  # no git
      paper-retriever/SKILL.md                 # downloads PDFs; no git (forbids destructive git)
      source-bootstrap/SKILL.md                # `pks source init/write-notes/write-metadata`
      source-promote/SKILL.md                  # `pks source promote`
      register-concepts/SKILL.md               # `pks` only
      extract-claims/SKILL.md                  # `pks` only
      extract-justifications/SKILL.md          # `pks` only
      extract-stances/SKILL.md                 # `pks` only
      reconcile/SKILL.md                       # updates paper notes.md cross-refs; no git
      reconcile/scripts/emit_nested_reconcile_fallback.py      # no git
      process-new-papers/SKILL.md              # batch wrapper around paper-reader
      ingest-new-papers/SKILL.md               # batch wrapper around paper-process
      ingest-collection/SKILL.md               # batch wrapper; only mentions `knowledge/.git` existence check
      ...
```

## Commit sites found

**None in the plugin.**

Grep evidence (all matches for `git add` / `git commit` in the plugin repo):

- `~/code/research-papers-plugin/CLAUDE.md:24`:
  ```
  2. git add plugins/research-papers/.claude-plugin/plugin.json
  ```
- `~/code/research-papers-plugin/CLAUDE.md:25`:
  ```
  3. git commit -m "{version}"
  ```

Both are inside a `## Release Process` block (`CLAUDE.md:17-28`) describing how to cut a new plugin version. They do not run during paper processing.

Grep evidence for any `git` reference at all inside `plugins/research-papers/skills/` (14 hits total, reproduced verbatim):

- `adjudicate/SKILL.md:213`: `You may be running alongside other agents. NEVER use git restore/checkout/reset/clean.`
- `extract-claims/SKILL.md:274`: `ls knowledge/.git 2>/dev/null || echo "MISSING: knowledge/.git"`
- `extract-claims/SKILL.md:278`: `` If `knowledge/.git` is missing → STOP. Run `pks init` or use `paper-process`, which initializes the source branch first. ``
- `ingest-collection/SKILL.md:33`: `if [ ! -d "$knowledge_dir/.git" ]; then`
- `paper-reader/SKILL.md:220`: `- NEVER use git restore/checkout/reset/clean`
- `paper-retriever/SKILL.md:160-161`: `**FORBIDDEN GIT COMMANDS - NEVER USE THESE:** / - git stash, git restore, git checkout, git reset, git clean`
- `register-concepts/SKILL.md:20,25`: existence check on `knowledge/.git`
- `source-bootstrap/SKILL.md:20,24`: existence check on `knowledge/.git`
- `source-promote/SKILL.md:17,21`: existence check on `knowledge/.git`
- `research/SKILL.md:95`: `You may be running alongside other agents. NEVER use git restore/checkout/reset/clean.`

All of these are either (a) existence checks against the propstore's private `knowledge/.git` directory, (b) prohibitions against destructive git ops, or (c) prose mentions of git in parallel-swarm warnings. None of them run `git add` or `git commit`.

Inside `plugins/research-papers/scripts/`, the only related file is `sync_propstore_source.py`, which shells out to `pks source add-concepts`, `pks source add-claim`, `pks source add-justification`, and `pks source add-stance` (lines 104, 110, 119, 129). The `add-*` here is `pks` terminology, not `git add`.

## Existing coordination mechanisms

**None in the plugin.** There are no lockfiles, no `flock` calls, no `filelock` imports, no `git worktree` usage, no queue files, no `commit-queue.lock` references anywhere in the plugin. The coordination discipline the plugin currently enforces is purely *don't touch shared files you didn't write*, expressed as prose rules in the parallel-swarm warnings (see next section). Propstore state is assumed to be managed safely by `pks` on its own `knowledge/.git` branch model; the plugin never touches that repository's index directly.

## Parallel-swarm rules already documented in SKILL.md files

Verbatim quotes, in each SKILL.md that has a parallel-swarm block:

`paper-reader/SKILL.md:217-221` (inside the chunk-reader prompt template):
```
## CRITICAL: Parallel Swarm Awareness
You are running alongside other chunk readers.
- Only write to YOUR chunk file in the chunks/ directory
- NEVER use git restore/checkout/reset/clean
```

`paper-retriever/SKILL.md:156-161`:
```
## CRITICAL: Parallel Swarm Awareness

You may be running alongside other agents in parallel.

**FORBIDDEN GIT COMMANDS - NEVER USE THESE:**
- `git stash`, `git restore`, `git checkout`, `git reset`, `git clean`
```

`adjudicate/SKILL.md:213` (one-liner):
```
You may be running alongside other agents. NEVER use git restore/checkout/reset/clean.
```

`research/SKILL.md:95` (one-liner, identical):
```
You may be running alongside other agents. NEVER use git restore/checkout/reset/clean.
```

`process-new-papers/SKILL.md` has no parallel-swarm block at all, even though Step 2 mandates parallel dispatch: "Treat the parallelization instruction in Step 2 as mandatory when subagents are available" (`process-new-papers/SKILL.md:28`). It does not mention git at all.

`ingest-collection/SKILL.md` has no parallel-swarm block either, despite Step 2 saying: "If subagents are available, run one worker per paper in parallel" (`ingest-collection/SKILL.md:49`).

`paper-process/SKILL.md` — the orchestrator the bug report names — does not contain the word `git` at all, and has no parallel-swarm block.

**Net observation:** the plugin's parallel-swarm rules are exclusively negative (don't run destructive git). There is no positive rule about how to safely *commit* work, because the plugin never tells any skill to commit work.

## Candidate fixes per commit site

Because there is no commit site in the plugin, the candidate-fix space is not "patch site X" but "where would a commit step belong if one were added, and what shape should it take". I lay out the option space assuming Q wants the plugin itself to own per-paper commits safely.

### Option A: `git commit --only -- <paths>`

Replace the (hypothetical) `git add <paper-dir>/ && git commit` pair with a single `git commit --only -- <paper-dir>/` invocation.

- Pros (from code): Matches the shape the plugin already uses — a bash block inside a SKILL.md. `--only` commits exactly the named paths regardless of what else is in the index, so worker A's concurrent stage of worker B's files does not leak into worker A's commit. No new dependency. No lockfile to clean up. Works on any platform the plugin already claims to support (Claude Code, Codex CLI, Gemini CLI) since it's plain `git`.
- Cons (from code): `git commit --only` still walks the working tree to build a temporary index; if two workers run it concurrently against the same `.git`, git's own locking (`.git/index.lock`) can still surface as a transient failure and one worker will have to retry. The plugin today has no retry helper; that would need to be added. Also, `--only` is a single, atomic shell step only if you write it as one command — if the skill writes it as "step 1 git add, step 2 git commit" the fix is wasted. Any fix has to be enforced as a **one-shot command**, not a two-step procedure.

### Option B: `git commit --include -- <paths>`

Semantically: stage `<paths>` on top of the current index and commit everything. This is **not safe** for this bug — it's the exact pattern that causes the race. Including it only to document the trap: if anyone reaches for `--include` as a drop-in for `add`+`commit`, they reintroduce the original bug.

- Pros: none for this use case.
- Cons: carries the same shared-index semantics as the buggy `add`+`commit` pair; the skill description (`--include` "adds the content of named paths to the commit, but uses the current content of the index for everything else" per git's own docs) makes it a landmine. Do not recommend.

### Option C: `flock` critical section around add+commit

Serialize the commit step with a POSIX `flock` on a repo-local lock file.

- Pros (from code): Conceptually minimal — the plugin already uses bash blocks, so wrapping one with `flock` is a few lines. Works even if the plugin wanted to keep a two-step add/commit.
- Cons (from code): `flock` is not available on Windows bash-for-Windows out of the box, and the plugin's stated compatibility (`paper-process/SKILL.md:5`, `paper-reader/SKILL.md:6`, etc.) names Claude Code + Codex CLI + Gemini CLI without committing to a single OS. The plugin today relies exclusively on cross-platform tools (`bash`, `ls`, `mkdir`, `magick`, `pdfinfo`, `pks`, `uv`) — no `flock`. Adding `flock` would be the first OS-specific dependency in the plugin and would fail silently on Windows workers. Also adds a lockfile path the plugin must pick, clean up on crash, and document.

### Option D: Python `filelock` in a helper script

Move the critical section into a helper Python script under a skill's `scripts/` dir, using the `filelock` package. The SKILL.md would call `uv run scripts/commit_paper.py <paper_dir>` instead of running `git` inline.

- Pros (from code): The plugin already uses this pattern — `paper-reader/scripts/paper_hash.py`, `paper-reader/scripts/emit_nested_reader_fallback.py`, etc., all get invoked from SKILL.md via `python3` or `uv run`. Adding one more helper is idiomatic. Cross-platform (works on Windows, macOS, Linux). Lock scope, stale-lock handling, and error messages all live in one testable place. A unit test can actually assert the race is closed.
- Cons (from code): Adds a new runtime dependency (`filelock`) and a script the caller has to have available. `uv run` handles the dependency transparently if the script uses inline script metadata, which the plugin already does elsewhere (need to confirm by reading `scripts/*.py` headers, which I did not do in the timebox). Slightly heavier than option A.

### Option E: Worktree isolation per worker

Give each worker its own `git worktree` rooted in a temp directory, merge back at the end.

- Pros (from code): Completely eliminates shared-index races by construction — workers don't share a tree.
- Cons (from code): Massively invasive relative to the current plugin. `paper-reader`'s Step 1 currently does `mv "$work_pdf" "$paper_dir/paper.pdf"` (`paper-reader/SKILL.md:130`) and writes directly under `papers/Author_Year_ShortTitle/` in the main tree. `reconcile` updates *other* papers' `notes.md` files in-place (`reconcile/SKILL.md:116, 137, 142, 229-235`) — those cross-paper writes are inherently shared and cannot be isolated per worker without a merge strategy. The plugin would also have to coordinate a merge-back step, handle conflicts in `papers/index.md`, and invalidate the assumption in `process-new-papers/SKILL.md:32` that "a PDF in `papers/` root is unprocessed" (because worktrees would move the PDF somewhere else first). Out of scope for a minimal-touch fix.

### Option F: `commit-queue.lock` file polled by workers

A repo-root lock file workers acquire before running add+commit. Same as option C but hand-rolled without `flock`.

- Pros (from code): OS-neutral; can be implemented in pure Python or even pure bash. Matches the "one more helper script" pattern the plugin already uses.
- Cons (from code): Reimplements what `filelock` already does correctly, including stale-lock detection (what if a worker crashes mid-commit?). Without careful design, a hand-rolled lock is a new race waiting to happen. If you're writing Python anyway, use `filelock` (option D) rather than rolling your own.

## Minimal-touch recommendation

If (and only if) the plugin is going to take responsibility for per-paper commits, the minimal-touch path is **option A plus a strict rule that the command must be written as a single `git commit --only -- <paper_dir>/` line, never as a two-step `add` + `commit`**. That fits the plugin's existing "bash blocks in SKILL.md" idiom exactly, adds no new dependencies, and closes the specific race in the bug report (concurrent `git add` between another worker's `add` and `commit`). The residual risk — transient failures from `.git/index.lock` contention — is a retry concern, not a correctness concern, and the plugin can handle it with a small retry loop in the same bash block.

However, before recommending any code change, the more important finding is: **this plugin does not perform the commit the bug describes.** The first thing Q should verify is *where* the `git add <paper-dir>/ && git commit` is actually coming from in Q's current workflow. Candidate sources: the inclusive-cartography project's own `CLAUDE.md`, a global instruction file, a protocol that wraps `paper-process`, or a hand-rolled shell loop. Fixing the plugin when the bug lives elsewhere would be wasted effort.

## Files Q will want to read before approving a fix

- `~/code/research-papers-plugin/CLAUDE.md` (full file, 28 lines) — confirms only release-process git usage.
- `~/code/research-papers-plugin/plugins/research-papers/skills/paper-process/SKILL.md` (full, 148 lines) — the orchestrator named in the bug; confirm no git step was elided.
- `~/code/research-papers-plugin/plugins/research-papers/skills/paper-reader/SKILL.md:217-221` — the only parallel-swarm block that actually ships in paper-reader, and the single place paper-reader mentions git.
- `~/code/research-papers-plugin/plugins/research-papers/skills/paper-retriever/SKILL.md:156-161` — the plugin's canonical parallel-swarm prose; any new parallel-safety rule should match this voice.
- `~/code/research-papers-plugin/plugins/research-papers/skills/process-new-papers/SKILL.md` (full, 112 lines) — mandates parallel dispatch; has no parallel-swarm block of its own. Prime place to add one.
- `~/code/research-papers-plugin/plugins/research-papers/skills/ingest-collection/SKILL.md` (full, 103 lines) — also mandates parallel dispatch; also has no parallel-swarm block.
- `~/code/research-papers-plugin/plugins/research-papers/skills/source-bootstrap/SKILL.md` (full, 58 lines) and `source-promote/SKILL.md` (full, 33 lines) — confirm propstore mutation is delegated to `pks`, not done with raw git.
- `~/code/research-papers-plugin/plugins/research-papers/scripts/sync_propstore_source.py:100-160` — confirms the only `add-*` in the plugin's scripts are `pks source add-*` invocations, not `git add`.
- The inclusive-cartography project's own `CLAUDE.md` and any `notes/` files referencing parallel ingestion — to find where the commit step Q is observing actually lives, since it isn't in the plugin.
