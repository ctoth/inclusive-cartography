# Task: Scout the research-papers plugin for the parallel-worker commit race

## What we know (bug description only)

When multiple worker agents run the `research-papers:paper-process` / `paper-reader` skill in parallel against the same repository, the per-worker commit step has a race: workers each run `git add <their-paper-dir>/` and then `git commit`, but the git index is shared across processes in the same working tree. Between one worker's `add` and its `commit`, a second worker's `add` can stage additional files into the index, and the first worker's `commit` then sweeps up both sets of files.

**The bug is general.** It is not specific to any particular paper or project. Your job is read-only — scout the skill code, identify where the commit happens, and document the fix space. Do NOT modify anything.

## Scout target

Plugin root: `~/code/research-papers-plugin`

Specifically look inside the `research-papers` plugin directory, likely at a path like:
- `~/code/research-papers-plugin/plugins/research-papers/skills/paper-reader/`
- `~/code/research-papers-plugin/plugins/research-papers/skills/paper-process/`
- any helper scripts under `scripts/` referenced by those skills

## What to find

1. **The commit step.** Find every place in the plugin where a skill or script issues `git add` and `git commit` as part of processing a single paper. Quote the exact lines with file:line citations.
2. **The surrounding context.** How does the commit step get triggered? Is it inside a loop? Inside a subagent prompt? Inside a shell script? Is it in the SKILL.md of paper-reader, paper-process, or both?
3. **Is there any existing coordination?** Lockfiles, mutexes, serialization, `git stash` usage, worktree isolation? Report what's there today.
4. **Are there multiple commit steps across the skill chain?** `paper-reader`, `paper-process`, and `reconcile` might each have their own commit logic. Map all of them.
5. **What does the SKILL.md say about parallel execution?** Look for any "Parallel Swarm Awareness" blocks, worker rules, or concurrency guidance already present in the plugin. Quote verbatim.
6. **Candidate fixes.** For each commit site, note what fixes would work without changing the skill's contract. Candidates to consider:
   - `git commit --only -- <specific paths>` — commits only the named paths, bypasses the rest of the index.
   - Lockfile around the add+commit critical section using `flock` (POSIX) or a Python `filelock` equivalent.
   - Replace `git add` + `git commit` with a single `git commit --include -- <paths>` invocation if that's available and safe.
   - Worktree isolation per worker — more invasive, probably out of scope.
   - Serialize via a `commit-queue.lock` file in the repo root.
   For each candidate, note the pros/cons you observe in the code as written. Do not pick a winner — your job is to lay out the option space.

## What to output

Write to `reports/scout-research-papers-commit-race.md`:

```markdown
# Scout: research-papers plugin commit race

## Plugin layout
[tree excerpt showing the relevant paths]

## Commit sites found
### Site 1: {skill}/{file}:{line}
[verbatim code block]
Context: [why/when it runs]

### Site 2: ...
[etc.]

## Existing coordination mechanisms
[what's there today, verbatim]

## Parallel-swarm rules already documented in SKILL.md files
[verbatim quotes, with file:line]

## Candidate fixes per commit site
### Site 1
- Option A: `git commit --only -- <paths>`
  - Pros (from code): ...
  - Cons (from code): ...
- Option B: flock critical section
  - ...
[etc.]

## Minimal-touch recommendation
[one paragraph: which option minimizes changes while fixing the bug, based on what the code actually looks like — NOT based on general preference]

## Files Q will want to read before approving a fix
[list of file paths with line ranges]
```

## Rules

- **Read-only.** Do not edit any file in `~/code/research-papers-plugin`.
- **Do not commit anything.** Not to the plugin repo, not to the current project.
- **Do not try to reproduce the bug.** Static analysis only.
- **Do not reference the inclusive-cartography project, the Wabiski protocol, the author feedback, or any specific paper.** The plugin is a general tool; your scout report must be usable for fixing the plugin in isolation.
- **Cite file:line for every factual claim about the code.** No paraphrasing without a citation.
- **Timebox: 10 minutes.**
- Return a short final message (≤5 sentences) pointing at the report file.
