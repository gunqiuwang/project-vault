# Obsidian Graph View Aliases Pattern

## Problem

When multiple projects connect to one Obsidian vault via symlinks/junctions, all `00_HOME.md` files appear as identical nodes in Graph View. You can't tell which `00_HOME` belongs to which project.

## Solution

Add `aliases` to the `00_HOME.md` frontmatter:

```yaml
---
type: home
aliases: ["二字日记", "二字日记 Home", "two-char-diary"]
---
```

Obsidian Graph View displays the first alias instead of the filename.

## Template

The vault template already includes this pattern:
```yaml
aliases: ["{PROJECT_NAME}", "{PROJECT_NAME} Home", "{PROJECT_SLUG}"]
```

## Multi-Project Index

For 3+ projects, create `Projects/INDEX.md` in the Obsidian vault root:

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

The `[[二字日记]]` wikilinks resolve to the aliased `00_HOME.md`, creating proper Graph View connections.

Template: `templates/PROJECTS_INDEX.md`
