# Obsidian + WSL Integration Pattern

WSL `ln -sf` creates Linux symlinks that Windows Obsidian CANNOT read.
Obsidian reports: `EACCES: permission denied, lstat`

## Fix: Windows Directory Junction

```powershell
# From WSL — no admin required
powershell.exe -Command "cmd /c mklink /J 'C:\Users\YOU\Documents\Obsidian Vault\Projects\项目名' 'C:\Users\YOU\Desktop\project\docs\vault'"
```

| Method | Works in Obsidian? | Admin? |
|--------|-------------------|--------|
| `ln -sf` (WSL) | ❌ EACCES | — |
| `mklink /D` (Windows) | ✅ | Yes |
| `mklink /J` (junction) | ✅ | **No** |

## Requirement: Windows Volume

Project must be on `/mnt/c/` or `/mnt/d/`. WSL-only paths (`/home/`) are invisible to Windows.

```
❌ /home/guoku/project/docs/vault        → Obsidian can't see
✅ /mnt/d/C1/project/docs/vault          → Works
✅ /mnt/c/Users/guoku/Desktop/project/   → Works
```

## Obsidian Aliases Don't Change Graph View Display

`aliases: ["项目名"]` in frontmatter affects search and linking, NOT the Graph View node label.
Graph View shows the **filename** (`00_HOME.md`), not the alias.

### Fix: Graph Color Groups

Assign unique colors per project in `.obsidian/graph.json`:

```json
{
  "colorGroups": [
    {"query": "path:Projects/二字日记", "color": {"a": 1, "rgb": 12101770}},
    {"query": "path:Projects/世界杯", "color": {"a": 1, "rgb": 3900150}},
    {"query": "path:Projects/星爻", "color": {"a": 1, "rgb": 8895933}}
  ]
}
```

Color reference (decimal RGB):
- Copper/Gold `#B8A88A` = 12101770
- Blue `#3B82F6` = 3900150
- Purple `#9B7DC4` = 10190276
- Green `#10B981` = 1088512

`setup-obsidian-link.sh` auto-generates a consistent color from `md5sum` of project name.

## Obsidian Default Files

New vaults auto-create `未命名.base` and `欢迎.md`. Safe to delete. `setup-obsidian-link.sh` removes them automatically.

## Multi-Project Index

Create `Projects/INDEX.md` in Obsidian vault root for a bird's-eye view:

```markdown
| Project | Phase | Score | Entry |
|---------|-------|-------|-------|
| [[二字日记]] | mvp | 81/100 | [[二字日记]] |
| [[世界杯]] | prototype | 75/100 | [[世界杯]] |
```
