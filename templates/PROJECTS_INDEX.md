---
aliases: ["Projects", "项目总览"]
---

# Projects Index

> All projects in one view. Each project's details are in its `00_HOME.md`.

## Active Projects

| Project | Phase | Score | Status | Entry |
|---------|-------|-------|--------|-------|
| [[项目名]] | mvp | 85/100 | Active | [[项目名]] |

<!-- Add new projects above -->

## Phase Legend

| Phase | Files | Description |
|-------|-------|-------------|
| idea | 3 | Just the vision |
| prototype | 5 | Demo exists |
| mvp | 10 | First users |
| growth | 13 | Full vault |
| maintenance | 13 | Focus on decisions + incidents |
| sunset | 2 | Read-only |

## How to Add

1. Run vault init on the project
2. Run `setup-obsidian-link.sh` to connect Obsidian
3. Add a row to the table above

## Cross-Project Query

```dataview
TABLE project_phase AS "Phase", confidence AS "Confidence"
FROM "Projects"
WHERE type = "home"
```
