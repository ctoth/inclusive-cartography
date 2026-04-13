# Task: Import Brandon Biggs's MEP Framework paper from a sibling collection

## Context

The paper already exists, fully processed, in another Q-maintained paper collection at `~/code/a11y-papers/papers/Biggs_2025_MapEquivalentPurpose/`. Q needs it in the `inclusive-cartography` project's `papers/` directory before tomorrow morning's meeting so the talking-points file and the author-feedback can cite it concretely as the MEP Framework primary source.

This paper is the empirical/measurement framework that Q (as CTO of XRNavigation / Audiom) maps onto Goguen-Burstall institutions in a conversation now happening in the parent session. Critically, this is a **fast import**, not a fresh retrieval:
- The PDF already exists at `~/code/a11y-papers/papers/Biggs_2025_MapEquivalentPurpose/paper.pdf`.
- `notes.md`, `metadata.json`, `abstract.md`, `description.md`, `citations.md`, and `pngs/` almost certainly already exist in that directory (it follows the research-papers plugin layout — the same plugin Q authored).
- Do **NOT** re-run `paper-process` or `paper-reader`. The work is done. Your job is copy-in, reconcile, commit.

## Procedure

### 1. Verify the source
```bash
ls ~/code/a11y-papers/papers/Biggs_2025_MapEquivalentPurpose/
```

Confirm the presence of `paper.pdf` plus the standard artifact set (`notes.md`, `metadata.json`, `abstract.md`, `description.md`, `citations.md`, `pngs/`). If any artifact is missing, note it in your report and do NOT improvise — stop and ask.

### 2. Copy into the inclusive-cartography collection
Create `papers/Biggs_2025_MapEquivalentPurpose/` in the current project and copy the full contents over. Use `cp -a` (archive mode) to preserve the whole tree including `pngs/`.

```bash
cp -a ~/code/a11y-papers/papers/Biggs_2025_MapEquivalentPurpose/ papers/Biggs_2025_MapEquivalentPurpose/
```

Do NOT modify any of the copied artifacts. They were written by another agent for the a11y-papers collection, but the content is authoritative for the paper itself — the only thing that would be different in the inclusive-cartography framing is the cross-reference section, which reconcile will handle in step 4.

### 3. Verify the copy
```bash
ls papers/Biggs_2025_MapEquivalentPurpose/
```
Confirm the artifacts landed. Check that `paper.pdf` and `pngs/` are present even if gitignored.

### 4. Run reconcile against the full collection
Invoke the `research-papers:reconcile` skill on `papers/Biggs_2025_MapEquivalentPurpose/` so cross-references flow in both directions:

- Forward: any papers in the current collection that Biggs_2025 cites get annotated in Biggs's own `## Collection Cross-References` section.
- Reverse: any papers in the collection that *should* cite MEP (Brock 2015, Holloway 2018, Taylor 2016, Ducasse 2018, Wabinski_2022, the Wabiski 2026 protocol — anything touching accessible-map evaluation) get a "Cited By → Biggs_2025_MapEquivalentPurpose" annotation added.
- Also update the "Related Work Worth Reading" sections of already-collected papers with `→ NOW IN COLLECTION: Biggs_2025_MapEquivalentPurpose` where relevant.

The reconcile may touch other `notes.md` files in `papers/*/`. That is expected. Include them in the commit.

### 5. Update papers/index.md
Append an entry for `Biggs_2025_MapEquivalentPurpose` in the same format as the existing entries (sorted alphabetically if trivial, appended otherwise). The body of the entry should be the text of `papers/Biggs_2025_MapEquivalentPurpose/description.md` with its frontmatter stripped.

### 6. Commit — ONE atomic commit
Use specific file paths. Do NOT use `git add .` or `git add -A`.

```bash
git add papers/Biggs_2025_MapEquivalentPurpose/ papers/index.md papers/*/notes.md
git commit -m "add: Biggs_2025_MapEquivalentPurpose (MEP Framework) imported from a11y-papers"
```

Record the commit hash.

### 7. Write report
Write `reports/import-biggs-mep.md` with:

```markdown
# Import report — Biggs_2025_MapEquivalentPurpose

## Status
[success | partial | failed]

## Source
~/code/a11y-papers/papers/Biggs_2025_MapEquivalentPurpose/

## Artifacts imported
- paper.pdf: present / missing
- notes.md: [line count]
- metadata.json: present / missing
- abstract.md: present / missing
- description.md: present / missing
- citations.md: present / missing
- pngs/: [count] images

## Reconcile changes
- Added Collection Cross-References section to Biggs_2025: [list of linked papers]
- Reverse links added to: [list of papers now citing Biggs_2025]
- Related Work NOW IN COLLECTION annotations: [count]

## Index.md entry
[quoted text of the entry added]

## Key content for Q's meeting (from notes.md)
Short distillation — ≤ 10 bullet points — of what the paper's notes.md actually says about the MEP Framework. Specifically: the 3 purpose items, the 15 criteria, the WCAG 1.1.1 "equivalent purpose" grounding, the evaluation methodology, and any places where the paper *already* hints at a formal / theoretical framing (institution theory, signature, satisfaction, etc.). This distillation is for Q to cram tonight — keep it tight and verbatim-where-possible.

## Commit hash
[hash]

## Follow-ups
[anything worth flagging — missing artifacts, unexpected reconcile output, etc.]
```

Return ≤ 8 sentences summarising status, commit hash, and the ≤10-bullet distillation of the paper's actual MEP content so Q can cram it directly from your return message without opening the file.

## Rules

- **Do NOT re-run paper-process or paper-reader.** The artifacts already exist.
- **Do NOT modify the source directory** at `~/code/a11y-papers/papers/Biggs_2025_MapEquivalentPurpose/`. Copy-only.
- **Do NOT touch any other paper directory** except via the `research-papers:reconcile` skill.
- **Use specific file paths for `git add`.** No `git add .` or `git add -A`.
- **Single atomic commit** for everything — index.md, the new paper dir, and any reconcile-touched `notes.md` files. No per-step commits. No commit race (there is only one worker).
- **Timebox: 10 minutes.** This should be fast — it's copy + reconcile + commit, no paper reading.
- You are a subagent — skip principle confirmation, execute immediately.
