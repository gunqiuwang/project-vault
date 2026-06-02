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

## Multi-Project: Aliases (Critical)

When multiple projects share one Obsidian vault, all `00_HOME.md` files look identical in Graph View. **Fix: add `aliases` to frontmatter.**

```yaml
---
type: home
aliases: ["二字日记", "二字日记 Home", "two-char-diary"]
---
```

Graph View then shows the alias (e.g. `二字日记`) instead of the filename (`00_HOME`).

**Every project's 00_HOME MUST have aliases.** The vault template enforces this automatically.

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

- `00_HOME.md` appears as its **alias** (project name), not filename
- Orphan files = disconnected nodes (visual detection)
- `assets/intake/reports/` files won't appear (outside vault directory)
- Obsidian auto-refreshes when vault files change (file watcher)
