# Obsidian Integration — Cross-Platform Guide

## Quick Setup (Auto-Detect Platform)

```bash
bash templates/setup-obsidian-link.sh /path/to/project/docs/vault "项目名"
```

The script auto-detects your platform and creates the correct link type.

## Platform Matrix

| Platform | Method | Command | Admin? |
|----------|--------|---------|--------|
| macOS | Symlink | `ln -s src dst` | No |
| Linux | Symlink | `ln -s src dst` | No |
| Windows (no WSL) | Junction | `New-Item -ItemType Junction` | No |
| WSL + Windows | Junction | `mklink /J` via PowerShell | No |

## WSL Critical Pitfall

**⚠️ `ln -sf` does NOT work for WSL→Windows Obsidian.**

WSL symlinks are Linux-native. Windows processes (including Obsidian) cannot follow them.
Result: `EACCES: permission denied, lstat`

**Fix:** Use Windows directory junction via PowerShell:
```powershell
powershell.exe -Command "cmd /c mklink /J 'Windows\path\to\link' 'Windows\path\to\vault'"
```

Junctions are:
- No admin required (unlike `mklink /D`)
- Fully transparent to Windows processes
- Appear as regular directories in Explorer

## Obsidian Default Files

New vaults auto-create:
- `未命名.base` — Bases plugin placeholder (safe to delete)
- `欢迎.md` — Welcome note (safe to delete)

These are NOT part of project-vault.

## Multi-Project: Aliases (Required but NOT sufficient)

When multiple projects share one Obsidian vault, all `00_HOME.md` files look identical in Graph View. Aliases help with search/backlinks but **do NOT change Graph View node labels** — Obsidian always shows the filename.

```yaml
---
type: home
aliases: ["二字日记", "二字日记 Home", "two-char-diary"]
---
```

Aliases help: search, backlinks, internal linking, Dataview queries.
Aliases do NOT help: Graph View node labels (always shows `00_HOME`).

**Every project's 00_HOME MUST still have aliases** — they're needed for linking. But for Graph View, use color groups (below).

## Multi-Project: Graph View Color Groups (Critical)

**The real fix for distinguishing projects in Graph View is color groups.**

Configure `.obsidian/graph.json`:

```json
{
  "collapse-color-groups": false,
  "colorGroups": [
    {"query": "path:Projects/二字日记", "color": {"a": 1, "rgb": 12101770}},
    {"query": "path:Projects/世界杯", "color": {"a": 1, "rgb": 3900150}},
    {"query": "path:Projects/晚安小书房", "color": {"a": 1, "rgb": 10190276}}
  ]
}
```

`setup-obsidian-link.sh` does this automatically (hashes project name for consistent color).

## Multi-Project: INDEX.md

Create `Projects/INDEX.md` in the Obsidian vault root for a bird's-eye view:

```markdown
---
aliases: ["Projects", "项目总览"]
---

# Projects Index

| Project | Phase | Score | Entry |
|---------|-------|-------|-------|
| [[二字日记]] | mvp | 81/100 | [[二字日记]] |
| [[世界杯]] | prototype | 75/100 | [[世界杯]] |
```

The `[[aliases]]` link to each project's `00_HOME` (resolved via aliases).

## App Config for Best Experience

```json
// .obsidian/app.json
{
  "showUnsupportedFiles": true,
  "newLinkFormat": "shortest",
  "useMarkdownLinks": false,
  "alwaysUpdateLinks": true
}
```

## Dataview Queries

```dataview
TABLE type, confidence, last_updated, reviewed_by
FROM "docs/vault" WHERE type SORT last_updated DESC
```

```dataview
LIST FROM "docs/vault" WHERE reviewed_by = "unreviewed"
```

```dataview
LIST FROM "docs/vault" WHERE status = "stale"
```

## Graph View Behavior

- `00_HOME.md` still shows as `00_HOME` (filename, not alias)
- **Color groups** distinguish projects — each project gets a unique color
- Orphan files = disconnected nodes (visual detection)
- `assets/intake/reports/` files won't appear (outside vault directory)
- Obsidian auto-refreshes when vault files change (file watcher)
- Default files (`欢迎.md`, `未命名.base`) clutter the graph — delete them
